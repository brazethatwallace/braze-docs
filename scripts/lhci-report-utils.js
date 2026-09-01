'use strict';

const fs = require('fs');
const path = require('path');

const THRESHOLDS = {
  lcpMs: 2500,
  cls: 0.1,
  tbtMs: 300,
  perfScore: 70,
};

const CLS_SEVERITY = {
  pass: { label: 'pass', max: 0.1 },
  near_miss: { label: 'near_miss', max: 0.15 },
  moderate: { label: 'moderate', max: 0.5 },
  severe: { label: 'severe', max: Infinity },
};

const TEMPLATE_PATTERNS = [
  { id: 'liquid', label: 'Liquid personalize', pattern: /\/liquid\// },
  { id: 'in_app_messages', label: 'In-app messages', pattern: /\/in_app_messages\// },
  { id: 'legacy_sdks', label: 'Legacy SDKs', pattern: /\/legacy_sdks\// },
  { id: 'content_cards', label: 'Content cards', pattern: /\/content_cards\// },
  { id: 'push_notifications', label: 'Push notifications', pattern: /\/push_notifications\// },
  { id: 'canvas', label: 'Canvas', pattern: /\/canvas\// },
  { id: 'whatsapp', label: 'WhatsApp', pattern: /\/whatsapp\// },
  { id: 'sms_mms', label: 'SMS/MMS/RCS', pattern: /\/sms_mms/ },
  { id: 'api_endpoints', label: 'API endpoints', pattern: /\/api\/endpoints\// },
  { id: 'api_objects', label: 'API objects/filters', pattern: /\/api\/objects/ },
  { id: 'currents', label: 'Currents', pattern: /\/currents\// },
  { id: 'shopify', label: 'Shopify partners', pattern: /\/shopify\// },
  { id: 'sdk_integration', label: 'SDK integration', pattern: /\/sdk_integration/ },
  { id: 'banners', label: 'Banners', pattern: /\/banners\// },
  { id: 'decisioning_studio', label: 'Decisioning Studio', pattern: /\/decisioning_studio/ },
  { id: 'query_builder', label: 'Query Builder / SQL', pattern: /\/query_builder\// },
];

function median(values) {
  const nums = values.filter((v) => typeof v === 'number' && !Number.isNaN(v)).sort((a, b) => a - b);
  if (!nums.length) return null;
  const mid = Math.floor(nums.length / 2);
  return nums.length % 2 === 0 ? (nums[mid - 1] + nums[mid]) / 2 : nums[mid];
}

function percentile(values, p) {
  const nums = values.filter((v) => typeof v === 'number' && !Number.isNaN(v)).sort((a, b) => a - b);
  if (!nums.length) return null;
  const idx = Math.min(nums.length - 1, Math.max(0, Math.floor((nums.length - 1) * p)));
  return nums[idx];
}

function collectionFromUrl(url) {
  try {
    const pathname = new URL(url).pathname.replace(/^\/docs\/?/, '');
    return pathname.split('/').filter(Boolean)[0] || 'other';
  } catch (_err) {
    return 'other';
  }
}

function templateForPath(pagePath) {
  for (const template of TEMPLATE_PATTERNS) {
    if (template.pattern.test(pagePath)) return template;
  }
  return { id: 'other', label: 'Other' };
}

function csvEscape(value) {
  const str = value == null ? '' : String(value);
  if (/[",\n]/.test(str)) return `"${str.replace(/"/g, '""')}"`;
  return str;
}

function parseCsvLine(line) {
  const values = [];
  let current = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i += 1) {
    const ch = line[i];
    if (inQuotes) {
      if (ch === '"' && line[i + 1] === '"') {
        current += '"';
        i += 1;
      } else if (ch === '"') {
        inQuotes = false;
      } else {
        current += ch;
      }
      continue;
    }
    if (ch === '"') inQuotes = true;
    else if (ch === ',') {
      values.push(current);
      current = '';
    } else current += ch;
  }
  values.push(current);
  return values;
}

function toBool(value) {
  return value === true || value === 'true';
}

function clsSeverityFor(cls) {
  if (cls == null || cls <= CLS_SEVERITY.pass.max) return CLS_SEVERITY.pass.label;
  if (cls <= CLS_SEVERITY.near_miss.max) return CLS_SEVERITY.near_miss.label;
  if (cls <= CLS_SEVERITY.moderate.max) return CLS_SEVERITY.moderate.label;
  return CLS_SEVERITY.severe.label;
}

function fixCategoriesFor(row) {
  const categories = [];
  if (row.clsSeverity === CLS_SEVERITY.severe.label) categories.push('cls_severe');
  if (row.clsSeverity === CLS_SEVERITY.moderate.label) categories.push('cls_moderate');
  if (row.clsSeverity === CLS_SEVERITY.near_miss.label) categories.push('cls_near_miss');
  if (row.lcpFail) categories.push('lcp_fail');
  if (row.unsizedImages >= 10) categories.push('unsized_images_high');
  else if (row.unsizedImages > 0) categories.push('unsized_images');
  if (row.tbtWarn) categories.push('tbt_warn');
  if (row.perfWarn) categories.push('perf_warn');
  if (!categories.length) categories.push('pass');
  return categories;
}

function priorityScoreFor(row) {
  let score = 0;
  if (row.clsSeverity === CLS_SEVERITY.severe.label) score += 100;
  if (row.clsSeverity === CLS_SEVERITY.moderate.label) score += 50;
  if (row.clsSeverity === CLS_SEVERITY.near_miss.label) score += 25;
  if (row.lcpFail && !row.clsFail) score += 20;
  if (row.lcpFail && row.clsFail) score += 35;
  if (row.unsizedImages >= 20) score += 25;
  else if (row.unsizedImages >= 10) score += 15;
  else if (row.unsizedImages >= 5) score += 8;
  if (row.perfWarn) score += 5;
  return score;
}

function recommendedActionFor(row) {
  const actions = [];
  if (row.clsSeverity === CLS_SEVERITY.severe.label) {
    actions.push('Fix severe CLS (image/video dimensions, tabs, or late-loading embeds)');
  } else if (row.clsSeverity === CLS_SEVERITY.moderate.label) {
    actions.push('Fix CLS (add width/height or reserve space for media)');
  } else if (row.clsSeverity === CLS_SEVERITY.near_miss.label) {
    actions.push('Quick CLS win (small layout shift near threshold)');
  }
  if (row.lcpFail) {
    actions.push('Investigate LCP (shared layout/third-party scripts likely; check page-specific media if outlier)');
  }
  if (row.unsizedImages >= 10) {
    actions.push('Bulk image dimension pass (many unsized images)');
  } else if (row.unsizedImages > 0 && row.clsFail) {
    actions.push('Add width/height to unsized images');
  }
  return actions.length ? actions.join('; ') : 'No action — passes hard gates';
}

function toOptionalNumber(value) {
  if (value === '' || value == null) return null;
  if (typeof value === 'number') return Number.isFinite(value) ? value : null;
  const num = Number(value);
  return Number.isFinite(num) ? num : null;
}

function normalizeRow(row) {
  const pagePath = row.path || row.url?.replace(/^https?:\/\/[^/]+/, '') || '';
  const template = templateForPath(pagePath);
  const lcpMs = row.lcpMs ?? toOptionalNumber(row.lcp_ms);
  const cls = toOptionalNumber(row.cls);
  const tbtMs = row.tbtMs ?? toOptionalNumber(row.tbt_ms);
  const perfScore = row.perfScore ?? toOptionalNumber(row.perf_score);
  const unsizedImages = Number(row.unsizedImages ?? row.unsized_images ?? 0);
  const lcpFail = row.lcpFail ?? toBool(row.lcp_fail) ?? (lcpMs != null && lcpMs > THRESHOLDS.lcpMs);
  const clsFail = row.clsFail ?? toBool(row.cls_fail) ?? (cls != null && cls > THRESHOLDS.cls);
  const tbtWarn = row.tbtWarn ?? toBool(row.tbt_warn) ?? (tbtMs != null && tbtMs > THRESHOLDS.tbtMs);
  const perfWarn = row.perfWarn ?? toBool(row.perf_warn) ?? (perfScore != null && perfScore < THRESHOLDS.perfScore);
  const enriched = {
    url: row.url,
    path: pagePath,
    collection: row.collection || collectionFromUrl(row.url || `https://www.braze.com${pagePath}`),
    templateId: template.id,
    templateLabel: template.label,
    perfScore,
    lcpMs,
    cls,
    tbtMs,
    unsizedImages,
    runs: Number(row.runs || 1),
    lcpFail,
    clsFail,
    tbtWarn,
    perfWarn,
  };
  enriched.clsSeverity = clsSeverityFor(enriched.cls);
  enriched.priorityScore = priorityScoreFor(enriched);
  enriched.fixCategories = fixCategoriesFor(enriched);
  enriched.recommendedAction = recommendedActionFor(enriched);
  return enriched;
}

function readCsvRows(csvPath) {
  const content = fs.readFileSync(csvPath, 'utf8').trim();
  if (!content) return [];
  const lines = content.split('\n');
  const headers = parseCsvLine(lines[0]);
  return lines.slice(1).map((line) => {
    const values = parseCsvLine(line);
    const row = {};
    headers.forEach((header, index) => {
      row[header] = values[index] ?? '';
    });
    return normalizeRow(row);
  });
}

function auditValue(audits, id) {
  const audit = audits[id];
  if (!audit) return null;
  if (typeof audit.numericValue === 'number') return audit.numericValue;
  if (typeof audit.score === 'number') return audit.score;
  return null;
}

function unsizedImageCount(audits) {
  return audits['unsized-images']?.details?.items?.length ?? 0;
}

function summarizeReports(reportFiles) {
  const byUrl = new Map();
  for (const file of reportFiles) {
    let data;
    try {
      data = JSON.parse(fs.readFileSync(file, 'utf8'));
    } catch (err) {
      console.warn(`WARNING: skipping unreadable report ${file}: ${err.message}`);
      continue;
    }
    const url = data.requestedUrl || data.finalUrl;
    if (!url) continue;
    const audits = data.audits || {};
    const perfScore = data.categories?.performance?.score ?? null;
    const row = normalizeRow({
      url,
      path: url.replace(/^https?:\/\/[^/]+/, ''),
      collection: collectionFromUrl(url),
      perf_score: perfScore == null ? '' : Math.round(perfScore * 100),
      lcp_ms: auditValue(audits, 'largest-contentful-paint'),
      cls: auditValue(audits, 'cumulative-layout-shift'),
      tbt_ms: auditValue(audits, 'total-blocking-time'),
      unsized_images: unsizedImageCount(audits),
      runs: 1,
      lcp_fail: auditValue(audits, 'largest-contentful-paint') > THRESHOLDS.lcpMs,
      cls_fail: auditValue(audits, 'cumulative-layout-shift') > THRESHOLDS.cls,
      tbt_warn: auditValue(audits, 'total-blocking-time') > THRESHOLDS.tbtMs,
      perf_warn: perfScore != null && perfScore * 100 < THRESHOLDS.perfScore,
    });
    if (!byUrl.has(url)) byUrl.set(url, []);
    byUrl.get(url).push(row);
  }
  return [...byUrl.entries()].map(([url, runs]) => normalizeRow({
    url,
    path: runs[0].path,
    collection: runs[0].collection,
    perf_score: Math.round(median(runs.map((r) => r.perfScore))),
    lcp_ms: median(runs.map((r) => r.lcpMs)),
    cls: median(runs.map((r) => r.cls)),
    tbt_ms: median(runs.map((r) => r.tbtMs)),
    unsized_images: Math.max(...runs.map((r) => r.unsizedImages)),
    runs: runs.length,
    lcp_fail: runs.some((r) => r.lcpFail),
    cls_fail: runs.some((r) => r.clsFail),
    tbt_warn: runs.some((r) => r.tbtWarn),
    perf_warn: runs.some((r) => r.perfWarn),
  })).sort((a, b) => a.path.localeCompare(b.path));
}

function walkJsonFiles(dir) {
  const files = [];
  if (!fs.existsSync(dir)) return files;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) files.push(...walkJsonFiles(fullPath));
    else if (entry.isFile() && entry.name.endsWith('-report.json')) files.push(fullPath);
  }
  return files;
}

function walkCollectFailureFiles(dir) {
  const files = [];
  if (!fs.existsSync(dir)) return files;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) files.push(...walkCollectFailureFiles(fullPath));
    else if (
      entry.isFile()
      && (entry.name === 'lhci-collect-failures.txt' || /^collect-failures-shard-\d+\.txt$/.test(entry.name))
    ) files.push(fullPath);
  }
  return files;
}

function readCollectFailures(inputDir) {
  const urls = [];
  for (const file of walkCollectFailureFiles(inputDir)) {
    for (const line of fs.readFileSync(file, 'utf8').split('\n')) {
      const url = line.split('\t')[0].trim();
      if (url) urls.push(url);
    }
  }
  return [...new Set(urls)].sort();
}

function metricStats(rows, key) {
  const values = rows.map((row) => row[key]).filter((v) => typeof v === 'number' && !Number.isNaN(v));
  return { p50: percentile(values, 0.5), p75: percentile(values, 0.75), p90: percentile(values, 0.9), p95: percentile(values, 0.95) };
}

function countBy(rows, keyFn) {
  const counts = {};
  for (const row of rows) counts[keyFn(row)] = (counts[keyFn(row)] || 0) + 1;
  return counts;
}

function buildTemplateSummary(rows) {
  const byTemplate = {};
  for (const row of rows) {
    if (!byTemplate[row.templateId]) byTemplate[row.templateId] = { label: row.templateLabel, pages: [] };
    byTemplate[row.templateId].pages.push(row);
  }
  return Object.entries(byTemplate).map(([templateId, data]) => {
    const pages = data.pages;
    return {
      templateId,
      label: data.label,
      pages: pages.length,
      lcpFail: pages.filter((r) => r.lcpFail).length,
      clsFail: pages.filter((r) => r.clsFail).length,
      clsSevere: pages.filter((r) => r.clsSeverity === CLS_SEVERITY.severe.label).length,
      clsNearMiss: pages.filter((r) => r.clsSeverity === CLS_SEVERITY.near_miss.label).length,
      medianLcp: median(pages.map((r) => r.lcpMs)),
      topPages: [...pages].sort((a, b) => b.priorityScore - a.priorityScore).slice(0, 5),
    };
  }).sort((a, b) => b.clsSevere - a.clsSevere || b.clsFail - a.clsFail || b.pages - a.pages);
}

function buildBacklogRows(rows) {
  return [...rows]
    .filter((row) => row.priorityScore > 0)
    .sort((a, b) => b.priorityScore - a.priorityScore || b.cls - a.cls || b.lcpMs - a.lcpMs)
    .map((row, index) => ({ rank: index + 1, ...row, fixCategories: row.fixCategories.join('|') }));
}

function buildBaselineDelta(rows, baselineCsv) {
  if (!baselineCsv || !fs.existsSync(baselineCsv)) return null;
  const baselineByPath = new Map(readCsvRows(baselineCsv).map((row) => [row.path, row]));
  let compared = 0;
  let lcpImproved = 0;
  let lcpRegressed = 0;
  let clsImproved = 0;
  let clsRegressed = 0;
  for (const row of rows) {
    const previous = baselineByPath.get(row.path);
    if (!previous) continue;
    compared += 1;
    if (row.lcpMs != null && previous.lcpMs != null) {
      if (row.lcpMs < previous.lcpMs - 50) lcpImproved += 1;
      if (row.lcpMs > previous.lcpMs + 50) lcpRegressed += 1;
    }
    if (row.cls != null && previous.cls != null) {
      if (row.cls < previous.cls - 0.01) clsImproved += 1;
      if (row.cls > previous.cls + 0.01) clsRegressed += 1;
    }
  }
  return { compared, lcpImproved, lcpRegressed, clsImproved, clsRegressed };
}

function formatMs(value) {
  return value == null ? '—' : `${Math.round(value)}ms`;
}

function formatCls(value) {
  return value == null ? '—' : value.toFixed(4);
}

function pct(count, total) {
  return total ? `${Math.round((count / total) * 1000) / 10}%` : '0%';
}

function buildMarkdown(rows, collectFailures, baselineDelta) {
  const total = rows.length;
  const hardPass = rows.filter((r) => !r.lcpFail && !r.clsFail).length;
  const clsSeverityCounts = countBy(rows, (row) => row.clsSeverity);
  const templateSummary = buildTemplateSummary(rows);
  const lcpStats = metricStats(rows, 'lcpMs');
  const clsStats = metricStats(rows, 'cls');
  const tbtStats = metricStats(rows, 'tbtMs');
  const byCollection = {};
  for (const row of rows) (byCollection[row.collection] = byCollection[row.collection] || []).push(row);

  const lines = [
    '# Lighthouse (Full Site) summary',
    '',
    `Pages audited: **${total}**`,
    `Hard-gate pass (LCP + CLS): **${hardPass}** (${pct(hardPass, total)})`,
    collectFailures.length ? `Collect failures: **${collectFailures.length}** URL(s)` : 'Collect failures: **0**',
    '',
    '## Gate failures',
    '',
    '| Gate | Threshold | Failures | Rate |',
    '|---|---|---:|---:|',
    `| LCP | ≤ ${THRESHOLDS.lcpMs}ms | ${rows.filter((r) => r.lcpFail).length} | ${pct(rows.filter((r) => r.lcpFail).length, total)} |`,
    `| CLS | ≤ ${THRESHOLDS.cls} | ${rows.filter((r) => r.clsFail).length} | ${pct(rows.filter((r) => r.clsFail).length, total)} |`,
    `| TBT (warn) | ≤ ${THRESHOLDS.tbtMs}ms | ${rows.filter((r) => r.tbtWarn).length} | ${pct(rows.filter((r) => r.tbtWarn).length, total)} |`,
    `| Perf score (warn) | ≥ ${THRESHOLDS.perfScore} | ${rows.filter((r) => r.perfWarn).length} | ${pct(rows.filter((r) => r.perfWarn).length, total)} |`,
    `| Unsized images | > 0 | ${rows.filter((r) => r.unsizedImages > 0).length} | ${pct(rows.filter((r) => r.unsizedImages > 0).length, total)} |`,
    '',
    '## Metric percentiles',
    '',
    '| Metric | p50 | p75 | p90 | p95 |',
    '|---|---:|---:|---:|---:|',
    `| LCP | ${formatMs(lcpStats.p50)} | ${formatMs(lcpStats.p75)} | ${formatMs(lcpStats.p90)} | ${formatMs(lcpStats.p95)} |`,
    `| CLS | ${formatCls(clsStats.p50)} | ${formatCls(clsStats.p75)} | ${formatCls(clsStats.p90)} | ${formatCls(clsStats.p95)} |`,
    `| TBT | ${formatMs(tbtStats.p50)} | ${formatMs(tbtStats.p75)} | ${formatMs(tbtStats.p90)} | ${formatMs(tbtStats.p95)} |`,
    '',
    '## CLS severity',
    '',
    '| Bucket | Range | Pages |',
    '|---|---|---:|',
    `| Pass | ≤ ${THRESHOLDS.cls} | ${clsSeverityCounts.pass || 0} |`,
    `| Near miss | 0.10–0.15 | ${clsSeverityCounts.near_miss || 0} |`,
    `| Moderate | 0.15–0.50 | ${clsSeverityCounts.moderate || 0} |`,
    `| Severe | > 0.50 | ${clsSeverityCounts.severe || 0} |`,
    '',
  ];

  if (baselineDelta?.compared > 0) {
    lines.push(
      '## Month-over-month delta', '',
      `Compared against baseline for **${baselineDelta.compared}** overlapping URL(s):`, '',
      `- LCP improved (>50ms): **${baselineDelta.lcpImproved}**`,
      `- LCP regressed (>50ms): **${baselineDelta.lcpRegressed}**`,
      `- CLS improved (>0.01): **${baselineDelta.clsImproved}**`,
      `- CLS regressed (>0.01): **${baselineDelta.clsRegressed}**`, '',
    );
  }

  lines.push(
    '## Failures by collection', '',
    '| Collection | Pages | LCP fail | CLS fail | CLS severe | Hard pass |',
    '|---|---:|---:|---:|---:|---:|',
  );
  for (const [collection, collRows] of Object.entries(byCollection).sort(([a], [b]) => a.localeCompare(b))) {
    lines.push(`| ${collection} | ${collRows.length} | ${collRows.filter((r) => r.lcpFail).length} | ${collRows.filter((r) => r.clsFail).length} | ${collRows.filter((r) => r.clsSeverity === CLS_SEVERITY.severe.label).length} | ${collRows.filter((r) => !r.lcpFail && !r.clsFail).length} |`);
  }

  lines.push('', '## Template clusters', '', '| Template | Pages | LCP fail | CLS fail | CLS severe | CLS near miss | Median LCP |', '|---|---:|---:|---:|---:|---:|---:|');
  for (const entry of templateSummary.filter((item) => item.templateId !== 'other').slice(0, 20)) {
    lines.push(`| ${entry.label} | ${entry.pages} | ${entry.lcpFail} | ${entry.clsFail} | ${entry.clsSevere} | ${entry.clsNearMiss} | ${formatMs(entry.medianLcp)} |`);
  }

  lines.push('', '## Worst LCP (top 15)', '');
  for (const row of [...rows].filter((r) => r.lcpMs != null).sort((a, b) => b.lcpMs - a.lcpMs).slice(0, 15)) {
    lines.push(`- ${Math.round(row.lcpMs)}ms — \`${row.path}\``);
  }
  lines.push('', '## Worst CLS (top 15)', '');
  for (const row of [...rows].filter((r) => r.cls != null).sort((a, b) => b.cls - a.cls).slice(0, 15)) {
    lines.push(`- ${row.cls.toFixed(4)} — \`${row.path}\``);
  }
  lines.push('', '## Prioritized fix backlog', '', 'See `lhci-fix-backlog.csv` and `lhci-fix-backlog.md`.');
  return `${lines.join('\n')}\n`;
}

function buildBacklogMarkdown(backlogRows, templateSummary, collectFailures) {
  const lines = [
    '# Lighthouse fix backlog', '',
    'Prioritized by estimated fix impact. Use template clusters for bulk fixes, and the ranked list for outliers.', '',
    `Pages needing action: **${backlogRows.length}**`,
    collectFailures.length ? `Collect failures (no report): **${collectFailures.length}**` : '',
    '', '## Recommended fix order', '',
    '1. **Severe CLS pages** (>0.5)',
    '2. **CLS near-miss pages** (0.10–0.15)',
    '3. **Template clusters** with high CLS/LCP counts',
    '4. **Systemic LCP** — shared layout/third-party scripts',
    '5. **TBT** — deprioritize until site-wide JS audit', '',
    '## Template clusters', '',
    '| Template | Pages | CLS severe | CLS fail | LCP fail | Top page |',
    '|---|---:|---:|---:|---:|---|',
  ];
  for (const entry of templateSummary.filter((item) => item.clsSevere > 0 || item.clsFail >= 5 || item.lcpFail >= 10)) {
    const top = entry.topPages[0];
    lines.push(`| ${entry.label} | ${entry.pages} | ${entry.clsSevere} | ${entry.clsFail} | ${entry.lcpFail} | \`${top?.path || '—'}\` |`);
  }
  lines.push('', '## Top 50 pages by priority', '');
  for (const row of backlogRows.slice(0, 50)) {
    lines.push(`${row.rank}. **${row.priorityScore}** — \`${row.path}\` (${row.templateLabel}; CLS ${formatCls(row.cls)}, LCP ${formatMs(row.lcpMs)})`, `   - ${row.recommendedAction}`);
  }
  if (collectFailures.length) {
    lines.push('', '## Collect failures', '');
    for (const url of collectFailures.slice(0, 50)) lines.push(`- ${url}`);
    if (collectFailures.length > 50) lines.push(`- …and ${collectFailures.length - 50} more`);
  }
  return `${lines.filter(Boolean).join('\n')}\n`;
}

function writeSummaryCsv(rows, outputCsv) {
  const headers = [
    'url', 'path', 'collection', 'template_id', 'template_label', 'perf_score', 'lcp_ms', 'cls', 'tbt_ms',
    'unsized_images', 'runs', 'lcp_fail', 'cls_fail', 'tbt_warn', 'perf_warn',
    'cls_severity', 'priority_score', 'fix_categories', 'recommended_action',
  ];
  const csvLines = [headers.join(','), ...rows.map((row) => [
    csvEscape(row.url), csvEscape(row.path), csvEscape(row.collection), csvEscape(row.templateId), csvEscape(row.templateLabel),
    row.perfScore ?? '', row.lcpMs != null ? Math.round(row.lcpMs) : '', row.cls != null ? row.cls.toFixed(4) : '',
    row.tbtMs != null ? Math.round(row.tbtMs) : '', row.unsizedImages, row.runs,
    row.lcpFail ? 'true' : 'false', row.clsFail ? 'true' : 'false', row.tbtWarn ? 'true' : 'false', row.perfWarn ? 'true' : 'false',
    row.clsSeverity, row.priorityScore, csvEscape(row.fixCategories.join('|')), csvEscape(row.recommendedAction),
  ].join(','))];
  fs.writeFileSync(outputCsv, `${csvLines.join('\n')}\n`, 'utf8');
}

function writeBacklogCsv(backlogRows, outputBacklogCsv) {
  const headers = ['rank', 'priority_score', 'path', 'template_label', 'collection', 'lcp_ms', 'cls', 'cls_severity', 'unsized_images', 'fix_categories', 'recommended_action', 'url'];
  const csvLines = [headers.join(','), ...backlogRows.map((row) => [
    row.rank, row.priorityScore, csvEscape(row.path), csvEscape(row.templateLabel), csvEscape(row.collection),
    row.lcpMs != null ? Math.round(row.lcpMs) : '', row.cls != null ? row.cls.toFixed(4) : '', row.clsSeverity,
    row.unsizedImages, csvEscape(row.fixCategories), csvEscape(row.recommendedAction), csvEscape(row.url),
  ].join(','))];
  fs.writeFileSync(outputBacklogCsv, `${csvLines.join('\n')}\n`, 'utf8');
}

module.exports = {
  THRESHOLDS,
  CLS_SEVERITY,
  TEMPLATE_PATTERNS,
  normalizeRow,
  toOptionalNumber,
  summarizeReports,
  readCsvRows,
  walkJsonFiles,
  readCollectFailures,
  buildBacklogRows,
  buildTemplateSummary,
  buildBaselineDelta,
  buildMarkdown,
  buildBacklogMarkdown,
  writeSummaryCsv,
  writeBacklogCsv,
};
