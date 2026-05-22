'use strict';

/**
 * Lighthouse CI configuration for braze-docs.
 *
 * Thresholds are taken from the Braze Docs Web App Performance Standards doc:
 *   - LCP  ≤ 2,500ms  (error if exceeded)
 *   - CLS  ≤ 0.1      (error if exceeded)
 *   - TBT  ≤ 300ms    (warn if exceeded — heavier pages like the Currents glossary
 *                       will exceed this until the JS audit work is complete)
 *   - Performance score ≥ 0.7 (warn — directional signal, not a hard gate)
 *
 * URLs to test are written by scripts/generate-lhci-urls.js before this runs.
 * See that script for sampling strategy and pinned high-traffic pages.
 *
 * Reports are uploaded as GitHub Actions artifacts (filesystem target).
 * To view: Actions → run → Artifacts → lhci-reports → open report.html.
 */

module.exports = {
  ci: {
    collect: {
      url: require('fs')
        .readFileSync('lhci-urls.txt', 'utf8')
        .split('\n')
        .map(u => u.trim())
        .filter(Boolean),
      numberOfRuns: 3,
      settings: {
        // Simulate a mid-tier Android phone on a throttled connection —
        // consistent with how Google measures Core Web Vitals field data.
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
        // Skip audits that aren't actionable for a static docs site.
        skipAudits: ['uses-http2'],
      },
    },

    assert: {
      assertions: {
        // Hard failures — these block the run and create a visible CI failure.
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'cumulative-layout-shift':  ['error', { maxNumericValue: 0.1 }],

        // Warnings — flagged in the report but don't fail the workflow.
        // TBT is a warn until the JS audit work (Step 2 of the perf brief) lands.
        'total-blocking-time':      ['warn', { maxNumericValue: 300 }],
        'categories:performance':   ['warn', { minScore: 0.7 }],
      },
    },

    upload: {
      target: 'filesystem',
      outputDir: './lhci-reports',
      reportFilenamePattern: '%%PATHNAME%%-%%DATETIME%%-report.%%EXTENSION%%',
    },
  },
};
