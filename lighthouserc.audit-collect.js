'use strict';

/**
 * Collect-only Lighthouse CI config for full-site shard jobs.
 *
 * URLs are passed per run via `lhci collect --url=...` so a single bad page
 * does not abort the rest of the shard. See scripts/run-lhci-shard.js.
 */

const { collectSettings } = require('./lighthouserc.audit.shared.js');

module.exports = {
  ci: {
    collect: collectSettings,
  },
};
