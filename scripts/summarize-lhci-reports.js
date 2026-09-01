#!/usr/bin/env node
/**
 * summarize-lhci-reports.js
 *
 * Aggregates Lighthouse JSON reports into CSV + Markdown summaries.
 *
 * Usage:
 *   node scripts/summarize-lhci-reports.js --input lhci-reports --output lhci-summary.csv
 */

'use strict';

const fs = require('fs');
const path = require('path');

const THRESHOLDS = {
  lcpMs: 2500,
  cls: 0.1,
  tbtMs: 300,
  perfScore: 70,
};

function parseArgs(argv) {
  const args = argv.slice(2);
  const get = (flag) => {
    const idx = args.indexOf(flag);
    return idx !== -1 ? args[idx + 1] : null;
  };
  return {
    inputDir: get('--input') || 'lhci-reports',
    outputCsv: get('--output') || 'lhci-summary.csv',
    outputMd: get('--markdown') || 'lhci-summary.md',
  };
}

function walkJsonFiles(dir) {
  const files = [];
  if (!fs.existsSync(dir)) return files;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...walkJsonFiles(fullPath));
      continue;
    }
    if (entry.isFile() && entry.name.endsWith('-report.json')) {
      files.push(fullPath);
    }
  }
  return files;
}

function median(values) {
  const nums = values.filter((v) => typeof v === 'number' && !Number.isNaN(v)).sort((a, b) => a - b);
  if (!nums.length) return null;
  const mid = Math.floor(nums.length / 2);
  return nums.length % 2 === 0
    ? (nums[mid - 1] + nums[mid]) / 2
    : nums[mid];
}

function collectionFromUrl(url) {
  try {
    const pathname = new URL(url).pathname.replace(/^\/docs\/?/, '');
    const segment = pathname.split('/').filter(Boolean)[0] || 'other';
    return segment;
  } catch (_err) {
    return 'other';
  }
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

function csvEscape(value) {
  const str = value == null ? '' : String(value);
  if (/[",\n]/.test(str)) return `"${str.replace(/"/g, '""')}"`;
  return str;
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
    const perfScore = (data.categories?.performance?.score ?? null);
    const row = {
      url,
      path: url.replace(/^https?:\/\/[^/]+/, ''),
      collection: collectionFromUrl(url),
      perfScore: perfScore == null ? null : Math.round(perfScore * 100),
      lcpMs: auditValue(audits, 'largest-contentful-paint'),
      cls: auditValue(audits, 'cumulative-layout-shift'),
      tbtMs: auditValue(audits, 'total-blocking-time'),
      unsizedImages: unsizedImageCount(audits),
      lcpFail: false,
      clsFail: false,
      tbtWarn: false,
      perfWarn: false,
    };

    row.lcpFail = row.lcpMs != null && row.lcpMs > THRESHOLDS.lcpMs;
    row.clsFail = row.cls != null && row.cls > THRESHOLDS.cls;
    row.tbtWarn = row.tbtMs != null && row.tbtMs > THRESHOLDS.tbtMs;
    row.perfWarn = row.perfScore != null && row.perfScore < THRESHOLDS.perfScore;

    if (!byUrl.has(url)) byUrl.set(url, []);
    byUrl.get(url).push(row);
  }

  const rows = [...byUrl.entries()].map(([url, runs]) => {
    const first = runs[0];
    return {
      url,
      path: first.path,
      collection: first.collection,
      perfScore: Math.round(median(runs.map((r) => r.perfScore))),
      lcpMs: median(runs.map((r) => r.lcpMs)),
      cls: median(runs.map((r) => r.cls)),
      tbtMs: median(runs.map((r) => r.tbtMs)),
      unsizedImages: Math.max(...runs.map((r) => r.unsizedImages)),
      runs: runs.length,
      lcpFail: runs.some((r) => r.lcpFail),
      clsFail: runs.some((r) => r.clsFail),
      tbtWarn: runs.some((r) => r.tbtWarn),
      perfWarn: runs.some((r) => r.perfWarn),
    };
  }).sort((a, b) => a.path.localeCompare(b.path));

  return rows;
}

function buildMarkdown(rows) {
  const total = rows.length;
  const lcpFails = rows.filter((r) => r.lcpFail).length;
  const clsFails = rows.filter((r) => r.clsFail).length;
  const tbtWarns = rows.filter((r) => r.tbtWarn).length;
  const perfWarns = rows.filter((r) => r.perfWarn).length;
  const unsized = rows.filter((r) => r.unsizedImages > 0).length;

  const byCollection = {};
  for (const row of rows) {
  (byCollection[row.collection] = byCollection[row.collection] || []).push(row);
  }

  const lines = [
    '# Lighthouse (Full Site) summary',
    '',
    `Pages audited: **${total}**`,
    '',
    '| Gate | Threshold | Failures |',
    '|---|---|---|',
    `| LCP | ≤ ${THRESHOLDS.lcpMs}ms | ${lcpFails} |`,
    `| CLS | ≤ ${THRESHOLDS.cls} | ${clsFails} |`,
    `| TBT (warn) | ≤ ${THRESHOLDS.tbtMs}ms | ${tbtWarns} |`,
    `| Perf score (warn) | ≥ ${THRESHOLDS.perfScore} | ${perfWarns} |`,
    `| Unsized images | > 0 | ${unsized} |`,
    '',
    '## Failures by collection',
    '',
    '| Collection | Pages | LCP fail | CLS fail | TBT warn | Perf warn | Unsized images |',
    '|---|---:|---:|---:|---:|---:|---:|',
  ];

  for (const [collection, collRows] of Object.entries(byCollection).sort(([a], [b]) => a.localeCompare(b))) {
    lines.push(
      `| ${collection} | ${collRows.length} | ${collRows.filter((r) => r.lcpFail).length} | ${collRows.filter((r) => r.clsFail).length} | ${collRows.filter((r) => r.tbtWarn).length} | ${collRows.filter((r) => r.perfWarn).length} | ${collRows.filter((r) => r.unsizedImages > 0).length} |`
    );
  }

  const worstLcp = [...rows].filter((r) => r.lcpMs != null).sort((a, b) => b.lcpMs - a.lcpMs).slice(0, 15);
  lines.push('', '## Worst LCP (top 15)', '');
  for (const row of worstLcp) {
    lines.push(`- ${Math.round(row.lcpMs)}ms — \`${row.path}\``);
  }

  const worstCls = [...rows].filter((r) => r.cls != null).sort((a, b) => b.cls - a.cls).slice(0, 15);
  lines.push('', '## Worst CLS (top 15)', '');
  for (const row of worstCls) {
    lines.push(`- ${row.cls.toFixed(4)} — \`${row.path}\``);
  }

  return lines.join('\n') + '\n';
}

function main() {
  const { inputDir, outputCsv, outputMd } = parseArgs(process.argv);
  const reportFiles = walkJsonFiles(inputDir);
  if (!reportFiles.length) {
    console.error(`ERROR: no Lighthouse JSON reports found under ${inputDir}`);
    process.exit(1);
  }

  const rows = summarizeReports(reportFiles);
  const headers = [
    'url', 'path', 'collection', 'perf_score', 'lcp_ms', 'cls', 'tbt_ms',
    'unsized_images', 'runs', 'lcp_fail', 'cls_fail', 'tbt_warn', 'perf_warn',
  ];

  const csvLines = [
    headers.join(','),
    ...rows.map((row) => [
      csvEscape(row.url),
      csvEscape(row.path),
      csvEscape(row.collection),
      row.perfScore ?? '',
      row.lcpMs != null ? Math.round(row.lcpMs) : '',
      row.cls != null ? row.cls.toFixed(4) : '',
      row.tbtMs != null ? Math.round(row.tbtMs) : '',
      row.unsizedImages,
      row.runs,
      row.lcpFail ? 'true' : 'false',
      row.clsFail ? 'true' : 'false',
      row.tbtWarn ? 'true' : 'false',
      row.perfWarn ? 'true' : 'false',
    ].join(',')),
  ];

  fs.writeFileSync(outputCsv, csvLines.join('\n') + '\n', 'utf8');
  fs.writeFileSync(outputMd, buildMarkdown(rows), 'utf8');

  console.log(`Summarized ${rows.length} URL(s) from ${reportFiles.length} report file(s).`);
  console.log(`Wrote ${outputCsv}`);
  console.log(`Wrote ${outputMd}`);
}

main();
