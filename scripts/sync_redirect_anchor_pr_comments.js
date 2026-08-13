// Syncs redirect/anchor check results onto the PR as two comments (errors +
// warnings). Invoked from .github/workflows/validate-doc-redirects.yml via
// actions/github-script.
//
// Values below (old_url, source_file, link, title fields, etc.) come from
// the PR's own file paths, link text, and frontmatter, so a PR author fully
// controls their content. Do NOT wrap untrusted values in markdown backtick
// spans: CommonMark/GFM code-span matching pairs backtick runs of equal
// length wherever they next occur in the block, not just adjacently, so any
// single backtick anywhere in the value can still close the span early and
// let the remaining markdown after it render live (spoofed links/headings).
// Use an HTML <code> element with HTML entity-escaping instead, which
// sidesteps markdown code-span parsing entirely.
//
// Collapse embedded line breaks to a single space FIRST. A value that spans
// multiple physical lines can otherwise break out of its enclosing list item
// / inline context entirely -- a blank line ends the current list item
// regardless of an unclosed <code> tag, and a bare "text\n===" line pair
// then forms a live Setext heading -- neither of which requires any of the
// punctuation below. Reducing the value to a single line removes the
// possibility of block-level (heading/list/blockquote/etc.) constructs
// forming inside it at all.
//
// Then:
//   - htmlEscape for <code> content (and any raw-HTML contexts) so
//     attacker-controlled "<"/">"/"&" cannot form real HTML tags/attributes
//     for the browser's tokenizer (e.g. literal "<script>" or
//     "<img onerror=...>"), including inside <summary> which receives NO
//     CommonMark inline processing.
//   - mdEscape for markdown-rendered prose so CommonMark's inline pipeline
//     (links, emphasis, autolinks, etc.) cannot turn PR-controlled text into
//     live markup. CommonMark renders "\X" as a literal "X" for punctuation.
//
// For <code>-wrapped identifiers we apply both: entity-escape first, then
// backslash-escape, so HTML and markdown surfaces are both closed.

const fs = require('fs');

const ERRORS_MARKER = '<!-- braze-docs-redirect-anchor-bot:errors -->';
const WARNINGS_MARKER = '<!-- braze-docs-redirect-anchor-bot:warnings -->';

const flatten = (s) => String(s).replace(/\r\n|\r|\n/g, ' ');

const htmlEscape = (s) => flatten(s)
  .replace(/&/g, '&amp;')
  .replace(/</g, '&lt;')
  .replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;');

const mdEscape = (s) => flatten(s)
  .replace(/([\\`*_{}\[\]()#+\-.!=:|<>~])/g, '\\$1');

// Wrapped in <code> for technical identifiers (anchors, paths, raw links).
const code = (s) => `<code>${mdEscape(htmlEscape(s))}</code>`;

// Plain escaped text for human-readable prose (article titles).
const text = (s) => mdEscape(s);

// Only used inside the ```js fenced block below, which is a different
// injection surface (a lone line of 3+ backticks could close the fence
// early): break up any run of backticks so a run of 3 can never form.
const escForFence = (s) => String(s).replace(/`/g, '`' + '\u200b');

const MAX_ITEMS_PER_SECTION = 30;
const MAX_GROUPS = 20;
const MAX_BODY_LEN = 60000; // GitHub's issue-comment limit is 65536 chars

module.exports = async ({ github, context, core }) => {
  const prNumber = context.payload.pull_request.number;
  const { owner, repo } = context.repo;
  const runUrl = `${context.serverUrl}/${owner}/${repo}/actions/runs/${context.runId}`;
  const reportPath = process.env.REPORT_PATH || 'redirect-report.json';

  const listItems = (items, render, moreRender) => {
    const shown = items.slice(0, MAX_ITEMS_PER_SECTION).map(render);
    if (items.length > MAX_ITEMS_PER_SECTION) {
      const remaining = items.length - MAX_ITEMS_PER_SECTION;
      shown.push(moreRender
        ? moreRender(remaining)
        : `- …and ${remaining} more (see the full report in the workflow run log)`);
    }
    return shown;
  };

  // Last-resort safety net -- MAX_ITEMS_PER_SECTION and MAX_GROUPS already keep
  // real-world bodies well under this in practice. A hard slice at this length
  // could in theory land mid-<details> block, leaving an unclosed tag before
  // the truncation notice; that's a cosmetic rendering risk (not a security
  // one, since escaping has already run on everything before this point), and
  // is judged acceptable given how rarely this path should trigger.
  const truncate = (body) => body.length > MAX_BODY_LEN
    ? body.slice(0, MAX_BODY_LEN) +
      `\n\n…(truncated for GitHub comment length -- see the [workflow run](${runUrl}) log for the full report)`
    : body;

  // Groups anchor_issues/anchor_warnings entries (each one link) by the
  // heading they point at (target_path + anchor [+ category, for issues, so a
  // pre-existing renamed-heading break and a brand-new typo pointing at the
  // same anchor don't get merged into one misleading message]). This answers
  // the two questions a human actually needs, in priority order: (A) which
  // heading broke, (B) which articles link to it -- rather than a flat list of
  // raw links that's hard to parse when one heading rename breaks dozens of
  // pages at once.
  const groupAnchorItems = (items) => {
    const groups = new Map();
    for (const item of items) {
      const key = [item.target_path, item.anchor, item.category || ''].join(' ');
      if (!groups.has(key)) {
        groups.set(key, {
          anchor: item.anchor,
          target_title: item.target_title || item.target_path,
          sources: new Map(), // source_file -> source_title, dedupes repeats
        });
      }
      const g = groups.get(key);
      if (!g.sources.has(item.source_file)) {
        g.sources.set(item.source_file, item.source_title || item.source_file);
      }
    }
    return [...groups.values()]
      .map((g) => ({ ...g, sources: [...g.sources.values()].sort((a, b) => a.localeCompare(b)) }))
      .sort((a, b) => b.sources.length - a.sources.length); // most-affected heading first
  };

  const summaryFor = (kind, g) => {
    const anchorCode = code('#' + g.anchor);
    const titleCode = code(g.target_title);
    const count = g.sources.length;
    const article = count === 1 ? 'article' : 'articles';
    if (kind === 'renamed') {
      return `${anchorCode} on ${titleCode} no longer exists -- referenced by ${count} ${article}`;
    }
    return `${anchorCode} on ${titleCode} doesn't exist -- check for a typo (referenced by ${count} ${article})`;
  };

  // Bold summary line (always visible) naming what broke, using ordinary
  // markdown -- not <details>/<summary>, a raw HTML block that receives no
  // inline markdown processing, which is why mdEscape's backslash escapes are
  // actually consumed here instead of showing up literally in the comment. The
  // (potentially long) list of referencing articles nests inside a <details>
  // block underneath so it doesn't dominate the comment. That <summary> label
  // is always a fixed string plus a plain integer count -- never attacker
  // content -- so it doesn't matter that <summary> skips inline processing.
  // The list itself is still ordinary markdown (blank line before/after, inside
  // the raw HTML block, lets it render as a normal <ul>).
  const renderGroups = (groups, kind) => {
    const capped = groups.slice(0, MAX_GROUPS);
    const blocks = capped.map((g) => {
      const count = g.sources.length;
      const label = count === 1 ? 'Show referencing article' : `Show ${count} referencing articles`;
      return [
        `**${summaryFor(kind, g)}**`,
        '',
        '<details>',
        `<summary>${label}</summary>`,
        '',
        ...listItems(g.sources, (t) => `- ${text(t)}`),
        '',
        '</details>',
      ].join('\n');
    });
    if (groups.length > MAX_GROUPS) {
      blocks.push(`…and ${groups.length - MAX_GROUPS} more affected heading(s) -- see the full report in the workflow run log.`);
    }
    return blocks.join('\n\n');
  };

  const buildErrorsBody = (report) => {
    const redirectRel = 'assets/js/broken_redirect_list.js';
    const sections = [];

    if (report.deleted_pages && report.deleted_pages.length) {
      sections.push([
        `#### Deleted pages (need a manual redirect target in \`${redirectRel}\`)`,
        '',
        ...listItems(report.deleted_pages, (r) => `- ${code(r.old_url)}`),
      ].join('\n'));
    }

    if (report.missing && report.missing.length) {
      sections.push([
        `#### Missing redirects (add to \`${redirectRel}\`)`,
        '',
        '```js',
        ...listItems(
          report.missing,
          (r) => `validurls['${escForFence(r.old_url)}'] = '${escForFence(r.expected_new)}';`,
          (n) => `// …and ${n} more (see the full report in the workflow run log)`
        ),
        '```',
      ].join('\n'));
    }

    if (report.wrong_target && report.wrong_target.length) {
      sections.push([
        '#### Wrong redirect target',
        '',
        ...listItems(report.wrong_target, (r) => [
          `- ${code(r.old_url)}`,
          `  - expected: ${code(r.expected_new)}`,
          `  - mapped: ${code(r.mapped_new)}`,
        ].join('\n')),
      ].join('\n'));
    }

    const anchorIssues = report.anchor_issues || [];
    const renamedGroups = groupAnchorItems(anchorIssues.filter((a) => a.category === 'heading_renamed'));
    const typoGroups = groupAnchorItems(anchorIssues.filter((a) => a.category === 'new_link_wrong_anchor'));

    if (renamedGroups.length) {
      sections.push([
        '#### Broken anchors (heading renamed or removed)',
        '',
        renderGroups(renamedGroups, 'renamed'),
      ].join('\n'));
    }

    if (typoGroups.length) {
      sections.push([
        '#### Broken anchors (new link, nonexistent anchor)',
        '',
        renderGroups(typoGroups, 'typo'),
      ].join('\n'));
    }

    if (!sections.length) return null;

    return truncate([
      ERRORS_MARKER,
      '',
      '### ❌ Redirect / anchor check failed',
      '',
      'This PR changes a doc URL or a heading anchor without a matching fix. Details below.',
      '',
      sections.join('\n\n'),
    ].join('\n'));
  };

  const buildWarningsBody = (report) => {
    const warnings = report.anchor_warnings || [];
    if (!warnings.length) return null;

    const entries = listItems(
      warnings,
      (w) => [`Page: ${code(w.source_title)}`, `Link: ${code(w.link)}`].join('\n'),
      (n) => `…and ${n} more (see the full report in the workflow run log)`
    );

    return truncate([
      WARNINGS_MARKER,
      '',
      '### ⚠️ Anchor warnings (non-blocking)',
      '',
      'These links resolve fine, but they point to the first heading on the target page. If this was intentional, you can ignore this message. Otherwise, update the link to remove the anchor.',
      '',
      entries.join('\n\n'),
    ].join('\n'));
  };

  const syncComment = async (marker, body) => {
    const comments = await github.paginate(github.rest.issues.listComments, {
      owner,
      repo,
      issue_number: prNumber,
      per_page: 100,
    });
    const existing = comments.find((c) => c.body && c.body.includes(marker));

    if (!body) {
      if (existing) {
        await github.rest.issues.deleteComment({ owner, repo, comment_id: existing.id });
        core.info(`Deleted comment ${existing.id} (${marker})`);
      }
      return;
    }

    if (existing) {
      await github.rest.issues.updateComment({ owner, repo, comment_id: existing.id, body });
      core.info(`Updated comment ${existing.id} (${marker})`);
    } else {
      await github.rest.issues.createComment({ owner, repo, issue_number: prNumber, body });
      core.info(`Created comment (${marker})`);
    }
  };

  let report = null;
  try {
    report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
  } catch (e) {
    core.warning(`${reportPath} missing or unreadable: ` + e.message);
  }

  if (!report) {
    // The script failed before it could write a report (e.g. worktree setup
    // failure) -- point at the Actions log instead of guessing at content. No
    // new data exists for warnings, so leave that comment untouched either way.
    if (process.env.VALIDATE_OUTCOME === 'failure') {
      await syncComment(ERRORS_MARKER, [
        ERRORS_MARKER,
        '',
        '### ❌ Redirect / anchor check failed',
        '',
        `The check failed before it could produce a structured report. See the [workflow run](${runUrl}) log for details.`,
      ].join('\n'));
    }
    return;
  }

  // Errors and warnings are independent: warnings are non-blocking and can be
  // present (or resolved) regardless of whether the check is currently passing
  // or failing for an unrelated reason, so each comment is synced on its own.
  await syncComment(ERRORS_MARKER, buildErrorsBody(report));
  await syncComment(WARNINGS_MARKER, buildWarningsBody(report));
};

// Exported for lightweight unit checks without github-script.
module.exports._test = { htmlEscape, mdEscape, code, text, escForFence };
