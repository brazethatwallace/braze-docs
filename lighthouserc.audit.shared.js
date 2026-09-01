'use strict';

/**
 * Shared Lighthouse CI settings for the monthly full-site audit.
 */

const collectSettings = {
  numberOfRuns: 1,
  settings: {
    formFactor: 'mobile',
    screenEmulation: {
      mobile: true,
      width: 412,
      height: 823,
      deviceScaleFactor: 1.75,
      disabled: false,
    },
    throttlingMethod: 'simulate',
    throttling: {
      rttMs: 40,
      throughputKbps: 10240,
      cpuSlowdownMultiplier: 4,
    },
    skipAudits: ['uses-http2'],
  },
};

const assertConfig = {
  assertions: {
    'largest-contentful-paint': ['warn', { maxNumericValue: 2500 }],
    'cumulative-layout-shift':  ['warn', { maxNumericValue: 0.1 }],
    'total-blocking-time':      ['warn', { maxNumericValue: 300 }],
    'categories:performance':   ['warn', { minScore: 0.7 }],
  },
};

const uploadConfig = {
  target: 'filesystem',
  outputDir: './lhci-reports',
  reportFilenamePattern: '%%PATHNAME%%-%%DATETIME%%-report.%%EXTENSION%%',
};

module.exports = {
  collectSettings,
  assertConfig,
  uploadConfig,
};
