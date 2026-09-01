#!/usr/bin/env node
/**
 * split-lhci-url-shards.js
 *
 * Splits a newline-delimited Lighthouse URL list into shard files for
 * parallel GitHub Actions matrix jobs.
 *
 * Usage:
 *   node scripts/split-lhci-url-shards.js --input lhci-urls.txt --output-dir lhci-shards
 *   node scripts/split-lhci-url-shards.js --input lhci-urls.txt --output-dir lhci-shards --shards 20
 *   node scripts/split-lhci-url-shards.js --input lhci-urls.txt --output-dir lhci-shards --target-per-shard 75
 */

'use strict';

const fs = require('fs');
const path = require('path');

function parseArgs(argv) {
  const args = argv.slice(2);
  const get = (flag) => {
    const idx = args.indexOf(flag);
    return idx !== -1 ? args[idx + 1] : null;
  };
  return {
    input: get('--input') || 'lhci-urls.txt',
    outputDir: get('--output-dir') || 'lhci-shards',
    shards: get('--shards') ? parseInt(get('--shards'), 10) : null,
    targetPerShard: get('--target-per-shard') ? parseInt(get('--target-per-shard'), 10) : 75,
  };
}

function shardCountFor(urlCount, shards, targetPerShard) {
  if (shards && shards > 0) return shards;
  return Math.max(1, Math.ceil(urlCount / targetPerShard));
}

function main() {
  const { input, outputDir, shards, targetPerShard } = parseArgs(process.argv);
  if (!fs.existsSync(input)) {
    console.error(`ERROR: input file not found: ${input}`);
    process.exit(1);
  }

  const urls = fs.readFileSync(input, 'utf8')
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean);

  if (urls.length === 0) {
    console.error('ERROR: input URL list is empty.');
    process.exit(1);
  }

  const shardTotal = shardCountFor(urls.length, shards, targetPerShard);
  fs.mkdirSync(outputDir, { recursive: true });

  const buckets = Array.from({ length: shardTotal }, () => []);
  urls.forEach((url, index) => {
    buckets[index % shardTotal].push(url);
  });

  buckets.forEach((bucket, index) => {
    const filename = `shard-${String(index).padStart(2, '0')}.txt`;
    fs.writeFileSync(path.join(outputDir, filename), bucket.join('\n') + '\n', 'utf8');
    console.log(`  ${filename}: ${bucket.length} URL(s)`);
  });

  const manifest = {
    urlCount: urls.length,
    shardCount: shardTotal,
    shardMatrix: [...Array(shardTotal).keys()],
    shards: buckets.map((bucket, index) => ({
      id: index,
      file: `shard-${String(index).padStart(2, '0')}.txt`,
      urlCount: bucket.length,
    })),
  };

  fs.writeFileSync(
    path.join(outputDir, 'manifest.json'),
    JSON.stringify(manifest, null, 2) + '\n',
    'utf8'
  );

  console.log(`Wrote ${shardTotal} shard file(s) for ${urls.length} URL(s) to ${outputDir}/`);
  console.log(`shard_matrix=${JSON.stringify(manifest.shardMatrix)}`);
}

main();
