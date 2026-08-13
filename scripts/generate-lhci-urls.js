#!/usr/bin/env node
/**
 * generate-lhci-urls.js
 *
 * Reads _data/sitemap_en.json and writes a representative sample of live
 * production URLs to lhci-urls.txt for use by Lighthouse CI.
 *
 * Sampling strategy:
 *   - Always include the pinned high-traffic / high-importance pages below.
 *   - Then pick a random sample from each collection so every template type
 *     is covered without running Lighthouse against all 1,400+ pages.
 *   - Deduplicate and shuffle before writing so the run order isn't biased.
 *
 * Usage:
 *   node scripts/generate-lhci-urls.js [--output lhci-urls.txt]
 */

'use strict';

const fs   = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// Config
// ---------------------------------------------------------------------------

const BASE_URL = 'https://www.braze.com/docs';

// Always include these regardless of random sampling — high-traffic pages,
// pages we know have had performance issues, and one per major template type.
//
// IMPORTANT: These must be valid keys in _data/sitemap_en.json. Run
// `node scripts/generate-lhci-urls.js` locally after updating paths here —
// the script logs a warning for any pinned key not found in the sitemap.
const PINNED_KEYS = [
  // Home
  '_home/home.md',
  // Currents glossary (our known worst performer — always measure it)
  '_user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events.md',
  // High-traffic user guide pages (paths reflect the 2026 IA revamp)
  '_user_guide/get_started/sdk_overview.md',
  '_user_guide/channels/email/drag_and_drop/overview.md',
  '_user_guide/messaging/canvas/create_a_canvas.md',
  '_user_guide/audience/segments/creating_a_segment.md',
  // API reference (api_page layout)
  '_api/api_campaigns/transactional_api_campaign.md',
  // Developer guide
  '_developer_guide/sdk_integration.md',
  // Partner page
  '_partners/ecommerce/shopify/discount_codes.md',
  // Help article
  '_help/help_articles/api/attribute_name_id_across_sources.md',
];

// How many random pages to sample per collection (in addition to pinned pages).
const SAMPLE_PER_COLLECTION = {
  user_guide:      10,
  developer_guide:  5,
  api:              5,
  partners:         5,
  help:             2,
  home:             0, // already pinned
};

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function keyToUrl(key) {
  // '_user_guide/foo/bar.md' → 'https://www.braze.com/docs/user_guide/foo/bar'
  // Production uses vercel.json trailingSlash: false — do not append a trailing slash
  // or Lighthouse will record an extra 308 redirect (~300ms) before the page loads.
  return BASE_URL + '/' + key.replace(/^_/, '').replace(/\.md$/, '');
}

function collectionOf(key) {
  return key.split('/')[0].replace(/^_/, '');
}

function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function sample(arr, n) {
  return shuffle([...arr]).slice(0, n);
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

const args       = process.argv.slice(2);
const outputFlag = args.indexOf('--output');
const outputFile = outputFlag !== -1 ? args[outputFlag + 1] : 'lhci-urls.txt';

const sitemapPath = path.join(__dirname, '..', '_data', 'sitemap_en.json');
if (!fs.existsSync(sitemapPath)) {
  console.error(`ERROR: sitemap not found at ${sitemapPath}`);
  process.exit(1);
}

const sitemap = JSON.parse(fs.readFileSync(sitemapPath, 'utf8'));
const allKeys = Object.keys(sitemap);

// Group keys by collection
const byCollection = {};
for (const key of allKeys) {
  const coll = collectionOf(key);
  (byCollection[coll] = byCollection[coll] || []).push(key);
}

// Build the URL set: pinned first, then random samples
const missingPinned = PINNED_KEYS.filter(k => sitemap[k] === undefined);
if (missingPinned.length > 0) {
  console.warn(`WARNING: ${missingPinned.length} pinned key(s) not found in sitemap and will be skipped:`);
  missingPinned.forEach(k => console.warn(`  - ${k}`));
}
const selectedKeys = new Set(PINNED_KEYS.filter(k => sitemap[k] !== undefined));

for (const [coll, count] of Object.entries(SAMPLE_PER_COLLECTION)) {
  if (!count) continue;
  const pool = (byCollection[coll] || []).filter(k => !selectedKeys.has(k));
  for (const k of sample(pool, count)) selectedKeys.add(k);
}

const urls = shuffle([...selectedKeys].map(keyToUrl));

const trailingSlashUrls = urls.filter((url) => url.endsWith('/'));
if (trailingSlashUrls.length > 0) {
  console.error('ERROR: generated URLs must not end with a trailing slash (vercel.json trailingSlash: false):');
  trailingSlashUrls.forEach((url) => console.error(`  - ${url}`));
  process.exit(1);
}

fs.writeFileSync(outputFile, urls.join('\n') + '\n', 'utf8');

console.log(`Wrote ${urls.length} URLs to ${outputFile}`);
for (const [coll, keys] of Object.entries(byCollection)) {
  const count = [...selectedKeys].filter(k => collectionOf(k) === coll).length;
  console.log(`  ${coll}: ${count} selected of ${keys.length} total`);
}
