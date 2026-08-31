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
 *   - Skip redirect stubs, hidden pages, and URLs that fail a live preflight.
 *   - Deduplicate and shuffle before writing so the run order isn't biased.
 *
 * Usage:
 *   node scripts/generate-lhci-urls.js [--output lhci-urls.txt] [--skip-preflight]
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
  '_user_guide/channels/email/drag_and_drop.md',
  '_user_guide/messaging/canvas/create_a_canvas.md',
  '_user_guide/audience/segments/creating_a_segment.md',
  // API reference (api_page layout) — canonical user guide page, not redirect stub
  '_user_guide/channels/transactional_email/create_a_transactional_email.md',
  // Developer guide
  '_developer_guide/sdk_integration.md',
  // Partner page
  '_partners/ecommerce/shopify/discount_codes.md',
  // User guide (migrated from legacy help article path)
  '_user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources.md',
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

function docPathFor(key) {
  return path.join(__dirname, '..', '_docs', key);
}

function readFrontmatter(key) {
  const docPath = docPathFor(key);
  if (!fs.existsSync(docPath)) return null;
  const content = fs.readFileSync(docPath, 'utf8');
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  return match ? match[1] : null;
}

function permalinkToUrl(permalink) {
  const cleaned = String(permalink)
    .replace(/^["']|["']$/g, '')
    .replace(/^\/+|\/+$/g, '');
  if (!cleaned || cleaned === '404.html') return null;
  return `${BASE_URL}/${cleaned}`;
}

function keyToUrl(key) {
  const frontmatter = readFrontmatter(key);
  if (frontmatter) {
    const permalinkMatch = frontmatter.match(/^permalink:\s*["']?([^"'\n]+)["']?/m);
    if (permalinkMatch) {
      const url = permalinkToUrl(permalinkMatch[1]);
      if (url) return url;
    }
  }
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

/**
 * Returns true when the English source page uses layout: redirect (client-side
 * redirect stub). Lighthouse should measure canonical destinations, not stubs.
 */
function isRedirectStub(key) {
  const frontmatter = readFrontmatter(key);
  if (!frontmatter) return false;
  return /^layout:\s*redirect\s*$/m.test(frontmatter);
}

/**
 * Returns true when the page is hidden from navigation/search. These often use
 * custom permalinks and are not representative public docs pages.
 */
function isHidden(key) {
  const frontmatter = readFrontmatter(key);
  if (!frontmatter) return false;
  return /^hidden:\s*true\s*$/m.test(frontmatter);
}

function isEligibleKey(key) {
  return !isRedirectStub(key) && !isHidden(key);
}

async function urlIsReachable(url) {
  try {
    let res = await fetch(url, { method: 'HEAD', redirect: 'follow' });
    if (res.status === 405 || res.status === 501) {
      res = await fetch(url, { method: 'GET', redirect: 'follow' });
    }
    return res.ok;
  } catch (err) {
    return false;
  }
}

async function preflightUrls(urls) {
  const reachable = [];
  for (const url of urls) {
    if (await urlIsReachable(url)) {
      reachable.push(url);
      continue;
    }
    console.warn(`WARNING: skipping URL after preflight check failed: ${url}`);
  }
  return reachable;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  const args            = process.argv.slice(2);
  const outputFlag      = args.indexOf('--output');
  const outputFile      = outputFlag !== -1 ? args[outputFlag + 1] : 'lhci-urls.txt';
  const skipPreflight   = args.includes('--skip-preflight');

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
  const redirectPinned = PINNED_KEYS.filter(k => sitemap[k] !== undefined && isRedirectStub(k));
  if (redirectPinned.length > 0) {
    console.warn(`WARNING: ${redirectPinned.length} pinned key(s) are redirect stubs — use canonical pages instead:`);
    redirectPinned.forEach(k => console.warn(`  - ${k}`));
  }
  const hiddenPinned = PINNED_KEYS.filter(k => sitemap[k] !== undefined && isHidden(k));
  if (hiddenPinned.length > 0) {
    console.warn(`WARNING: ${hiddenPinned.length} pinned key(s) are hidden — use public pages instead:`);
    hiddenPinned.forEach(k => console.warn(`  - ${k}`));
  }
  const selectedKeys = new Set(
    PINNED_KEYS.filter(k => sitemap[k] !== undefined && isEligibleKey(k))
  );

  for (const [coll, count] of Object.entries(SAMPLE_PER_COLLECTION)) {
    if (!count) continue;
    const pool = (byCollection[coll] || []).filter(k => !selectedKeys.has(k) && isEligibleKey(k));
    for (const k of sample(pool, count)) selectedKeys.add(k);
  }

  let urls = shuffle([...selectedKeys].map(keyToUrl));

  const trailingSlashUrls = urls.filter((url) => url.endsWith('/'));
  if (trailingSlashUrls.length > 0) {
    console.error('ERROR: generated URLs must not end with a trailing slash (vercel.json trailingSlash: false):');
    trailingSlashUrls.forEach((url) => console.error(`  - ${url}`));
    process.exit(1);
  }

  if (!skipPreflight) {
    const before = urls.length;
    urls = await preflightUrls(urls);
    if (urls.length < before) {
      console.warn(`WARNING: preflight removed ${before - urls.length} unreachable URL(s).`);
    }
  }

  if (urls.length === 0) {
    console.error('ERROR: no reachable URLs remain after filtering.');
    process.exit(1);
  }

  fs.writeFileSync(outputFile, urls.join('\n') + '\n', 'utf8');

  console.log(`Wrote ${urls.length} URLs to ${outputFile}`);
  for (const [coll, keys] of Object.entries(byCollection)) {
    const count = [...selectedKeys].filter(k => collectionOf(k) === coll).length;
    console.log(`  ${coll}: ${count} selected of ${keys.length} total`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
