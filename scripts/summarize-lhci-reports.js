#!/usr/bin/env node
/**
 * summarize-lhci-reports.js
 *
 * Aggregates Lighthouse JSON reports into CSV, Markdown summary, and a
 * prioritized fix backlog grouped by template pattern.
 *
 * Usage:
 *   node scripts/summarize-lhci-reports.js --input lhci-reports --output lhci-summary.csv
 *   node scripts/summarize-lhci-reports.js --from-csv lhci-summary.csv --markdown lhci-summary.md
 *   node scripts/summarize-lhci-reports.js --input lhci-reports --baseline previous/lhci-summary.csv
 */

'use strict';

const fs = require('fs');
const {
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
} = require('./lhci-report-utils.js');

function parseArgs(argv) {
  const args = argv.slice(2);
  const get = (flag) => {
    const idx = args.indexOf(flag);
    return idx !== -1 ? args[idx + 1] : null;
  };
  return {
    inputDir: get('--input') || 'lhci-reports',
    fromCsv: get('--from-csv'),
    outputCsv: get('--output') || 'lhci-summary.csv',
    outputMd: get('--markdown') || 'lhci-summary.md',
    outputBacklogCsv: get('--backlog-csv') || 'lhci-fix-backlog.csv',
    outputBacklogMd: get('--backlog-markdown') || 'lhci-fix-backlog.md',
    baselineCsv: get('--baseline'),
  };
}

function main() {
  const {
    inputDir,
    fromCsv,
    outputCsv,
    outputMd,
    outputBacklogCsv,
    outputBacklogMd,
    baselineCsv,
  } = parseArgs(process.argv);

  let rows;
  let reportFileCount = 0;
  let collectFailures = [];

  if (fromCsv) {
    if (!fs.existsSync(fromCsv)) {
      console.error(`ERROR: CSV not found: ${fromCsv}`);
      process.exit(1);
    }
    rows = readCsvRows(fromCsv);
    reportFileCount = rows.length;
  } else {
    const reportFiles = walkJsonFiles(inputDir);
    if (!reportFiles.length) {
      console.error(`ERROR: no Lighthouse JSON reports found under ${inputDir}`);
      process.exit(1);
    }
    rows = summarizeReports(reportFiles);
    reportFileCount = reportFiles.length;
    collectFailures = readCollectFailures(inputDir);
  }

  if (!rows.length) {
    console.error('ERROR: no URL rows to summarize');
    process.exit(1);
  }

  const baselineDelta = buildBaselineDelta(rows, baselineCsv);
  const backlogRows = buildBacklogRows(rows);
  const templateSummary = buildTemplateSummary(rows);

  writeSummaryCsv(rows, outputCsv);
  writeBacklogCsv(backlogRows, outputBacklogCsv);
  fs.writeFileSync(outputMd, buildMarkdown(rows, collectFailures, baselineDelta), 'utf8');
  fs.writeFileSync(outputBacklogMd, buildBacklogMarkdown(backlogRows, templateSummary, collectFailures), 'utf8');

  console.log(`Summarized ${rows.length} URL(s) from ${reportFileCount} source report(s).`);
  console.log(`Wrote ${outputCsv}`);
  console.log(`Wrote ${outputMd}`);
  console.log(`Wrote ${outputBacklogCsv} (${backlogRows.length} prioritized page(s))`);
  console.log(`Wrote ${outputBacklogMd}`);
  if (collectFailures.length) {
    console.log(`Collect failures: ${collectFailures.length}`);
  }
}

main();
