'use strict';

/**
 * Lighthouse CI configuration for the monthly full-site audit.
 *
 * Differences from lighthouserc.js (weekly sample):
 *   - Single run per URL (breadth over precision)
 *   - All thresholds are warnings — collect data, do not fail the workflow
 *
 * Shard jobs pass URLs via scripts/run-lhci-shard.js (per-URL collect).
 */

const fs = require('fs');
const { collectSettings, assertConfig, uploadConfig } = require('./lighthouserc.audit.shared.js');

function readShardUrls() {
  return fs
    .readFileSync('lhci-urls.txt', 'utf8')
    .split('\n')
    .map((u) => u.trim())
    .filter(Boolean);
}

module.exports = {
  ci: {
    collect: {
      ...collectSettings,
      url: readShardUrls(),
    },
    assert: assertConfig,
    upload: uploadConfig,
  },
};
