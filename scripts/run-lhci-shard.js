#!/usr/bin/env node
/**
 * run-lhci-shard.js
 *
 * Collect Lighthouse results for a shard URL list, continuing past per-URL
 * failures so one bad page does not drop the entire shard.
 *
 * Usage:
 *   node scripts/run-lhci-shard.js --input lhci-urls.txt
 *   node scripts/run-lhci-shard.js --input lhci-urls.txt --config lighthouserc.audit.js
 */

'use strict';

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const DEFAULTS = {
  input: 'lhci-urls.txt',
  config: 'lighthouserc.audit.js',
  collectConfig: 'lighthouserc.audit-collect.js',
  failuresLog: 'lhci-collect-failures.txt',
};

function parseArgs(argv) {
  const args = argv.slice(2);
  const get = (flag) => {
    const idx = args.indexOf(flag);
    return idx !== -1 ? args[idx + 1] : null;
  };
  return {
    input: get('--input') || DEFAULTS.input,
    config: get('--config') || DEFAULTS.config,
    collectConfig: get('--collect-config') || DEFAULTS.collectConfig,
    failuresLog: get('--failures-log') || DEFAULTS.failuresLog,
  };
}

function run(command, args) {
  const result = spawnSync(command, args, { stdio: 'inherit' });
  return result.status ?? 1;
}

function readUrls(inputPath) {
  if (!fs.existsSync(inputPath)) {
    console.error(`ERROR: URL list not found: ${inputPath}`);
    process.exit(1);
  }

  const urls = fs
    .readFileSync(inputPath, 'utf8')
    .split('\n')
    .map((url) => url.trim())
    .filter(Boolean);

  if (!urls.length) {
    console.error(`ERROR: no URLs found in ${inputPath}`);
    process.exit(1);
  }

  return urls;
}

function writeFailuresLog(failuresLog, failures) {
  fs.mkdirSync(path.dirname(failuresLog), { recursive: true });
  const lines = failures.map(({ url, status }) => `${url}\texit=${status}`).join('\n');
  fs.writeFileSync(failuresLog, `${lines}\n`, 'utf8');
}

function main() {
  const { input, config, collectConfig, failuresLog } = parseArgs(process.argv);

  // upload/assert configs read lhci-urls.txt at load time.
  if (path.resolve(input) !== path.resolve(DEFAULTS.input)) {
    fs.copyFileSync(input, DEFAULTS.input);
  }

  const urls = readUrls(input);
  const failures = [];

  console.log(`Collecting Lighthouse data for ${urls.length} URL(s).`);

  const healthcheckStatus = run('npx', [
    '--no-install', 'lhci', 'healthcheck', '--fatal', `--config=${config}`,
  ]);
  if (healthcheckStatus !== 0) {
    process.exit(healthcheckStatus);
  }

  for (let index = 0; index < urls.length; index += 1) {
    const url = urls[index];
    const collectArgs = [
      '--no-install', 'lhci', 'collect',
      `--config=${collectConfig}`,
      `--url=${url}`,
      '-n', '1',
    ];
    if (index > 0) {
      collectArgs.push('--additive');
    }

    console.log(`\n--- [${index + 1}/${urls.length}] ${url} ---\n`);
    const status = run('npx', collectArgs);
    if (status !== 0) {
      failures.push({ url, status });
      console.warn(`WARNING: collect failed for ${url} (exit ${status})`);
    }
  }

  const successCount = urls.length - failures.length;
  if (failures.length) {
    writeFailuresLog(failuresLog, failures);
    console.warn(
      `\n${failures.length}/${urls.length} URL(s) failed collect — see ${failuresLog}`
    );
  }

  if (successCount === 0) {
    console.error('ERROR: all URLs failed collect; skipping upload.');
    process.exit(1);
  }

  const uploadStatus = run('npx', ['--no-install', 'lhci', 'upload', `--config=${config}`]);
  if (uploadStatus !== 0) {
    console.error('ERROR: upload failed.');
    process.exit(uploadStatus);
  }

  const assertStatus = run('npx', ['--no-install', 'lhci', 'assert', `--config=${config}`]);
  if (assertStatus !== 0) {
    console.warn(`WARNING: assert exited ${assertStatus} (thresholds are warn-only).`);
  }

  console.log(`Done: ${successCount}/${urls.length} URL(s) collected and uploaded.`);
}

main();
