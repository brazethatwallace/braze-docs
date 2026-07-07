---
name: redirect-management
description: >
  Add, update, and validate URL redirects in assets/js/broken_redirect_list.js when
  documentation pages are renamed, moved, or deleted. Covers make_redirects.py,
  update_old_links.py, redirect chain cleanup, and pre-PR verification. Use when
  editing broken_redirect_list.js, adding redirects for renamed pages, refreshing
  stale redirect chains, or validating that redirects resolve correctly.
---

# Redirect management

Preserve old Braze Docs URLs when pages move, rename, or are deleted. Redirects live in [`assets/js/broken_redirect_list.js`](../../../assets/js/broken_redirect_list.js). The [`bdocs`](../../../bdocs) wrapper runs the Python and Ruby helpers.

**Canonical human guide:** [`docs/contributing/content_management/redirecting_urls.md`](../../../docs/contributing/content_management/redirecting_urls.md)

**General link conventions** (Liquid links, YAML `link:` fields, cross-references): **REQUIRED SUB-SKILL:** [braze-docs](../braze-docs/SKILL.md) Links mode — [site-conventions.md](../braze-docs/references/site-conventions.md).

## Context

- Branch: !`git branch --show-current`
- Redirect file changed: !`git diff --name-only HEAD -- assets/js/broken_redirect_list.js 2>/dev/null || true`

## Mode detection

Detect mode from `$ARGUMENTS`, modified files, then ask.

| Signal | Mode | Workflow |
|--------|------|----------|
| `$ARGUMENTS`: "rename", "moved", "new redirect", "mredirects" | **Add** | [Add a redirect for a renamed page](#add-a-redirect-for-a-renamed-page) |
| `$ARGUMENTS`: "chain", "stale", "ulinks", "collapse" | **Refresh** | [Refresh stale redirect chains](#refresh-stale-redirect-chains) |
| `$ARGUMENTS`: "validate", "verify", "test", "fblinks", "check" | **Validate** | [Validate redirects](#validate-redirects) |
| Modified `assets/js/broken_redirect_list.js` only | **Add** or **Validate** | Ask which applies, or infer from whether renames are in the branch diff |
| Modified `_docs/` with renames (no redirect file yet) | **Add** | Run **Add** workflow |

If mode is still ambiguous, ask what the user needs.

If AskUserQuestion is available:
- **Add a redirect** — Page was renamed or moved; need a new `validurls` entry
- **Refresh stale chains** — Collapse A→B→C chains or update in-doc links to final URLs
- **Validate redirects** — Confirm entries are valid JS and destinations resolve

Otherwise ask: "What do you need? (1) Add redirect, (2) Refresh chains, (3) Validate"

---

## Redirect entry format

Each redirect is one JavaScript assignment in `assets/js/broken_redirect_list.js`:

```javascript
validurls['/docs/REDIRECT_FROM'] = '/docs/REDIRECT_TO';
```

| Rule | Detail |
|------|--------|
| Syntax | `validurls['OLD'] = 'NEW';` — single quotes, semicolon, no locale prefix |
| Prefix | Both paths start with `/docs/` |
| Case | **Lowercase only** in URL strings, even when the Markdown filename uses uppercase |
| Trailing slash | Prefer **no** trailing slash on either side (`vercel.json` `trailingSlash: false`). Exception: keep a trailing slash only when an existing entry or anchor pattern requires it |
| Anchors | Include `#fragment` on either side when redirecting a heading URL: `validurls['/docs/page#old-heading'] = '/docs/other_page#new-heading';` |
| Query strings | Preserve `?` parameters when they are part of the bookmarked URL |
| Locale | Never use `/docs/en/`, `/docs/es/`, etc. — canonical English paths only |
| Chains | Point **OLD → final** destination directly. Do not create A→B when B already redirects to C |
| Placement | Insert near related entries (same path prefix). The file ends with a placeholder comment `// validurls['OLD'] = 'NEW';` — remove duplicate placeholders when adding manually |
| Identity | Do not add rows where OLD and NEW normalize to the same path |

**Example (page move):**

```javascript
validurls['/docs/user_guide/data_and_analytics/engagement_reports'] = '/docs/user_guide/data_and_analytics/your_reports/engagement_reports';
```

**Example (heading redirect via global list — prefer `local_redirect` in frontmatter when only a heading moved):**

```javascript
validurls['/docs/dashboard_features#frequency-capping'] = '/docs/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping';
```

### Convert a renamed file path to URLs

When adding a redirect manually (or verifying `mredirects` output), map `_docs/` paths to `/docs/` URLs:

1. Start from the repo-relative Markdown path under `_docs/`.
2. Remove the `.md` extension.
3. Replace each `/_collection` segment with `/collection` (drop the leading underscore on collection folders only).
4. Prepend `/docs` to the path.
5. Lowercase the full URL string.
6. Strip trailing slashes unless the URL has `#` or `?`.

| File path | Redirect URL |
|-----------|--------------|
| `_docs/_user_guide/channels/email.md` | `/docs/user_guide/channels/email` |
| `_docs/_api/endpoints/user_data/post_user_track.md` | `/docs/api/endpoints/user_data/post_user_track` |
| `_docs/_developer_guide/push_notifications.md` | `/docs/developer_guide/push_notifications` |

For a rename `old.md` → `new.md` in the same directory, **REDIRECT_FROM** uses the old URL; **REDIRECT_TO** uses the new URL.

---

## Scripts and `bdocs` commands

| Task | Command | Script |
|------|---------|--------|
| Auto-generate redirects for **committed** renames on this branch | `./bdocs mredirects` | [`scripts/make_redirects.py`](../../../scripts/make_redirects.py) |
| Update in-doc links to newest redirect target | `./bdocs ulinks PATH` | [`scripts/update_old_links.py`](../../../scripts/update_old_links.py) (+ [`scripts/utils/merge_redirect_descendants.py`](../../../scripts/utils/merge_redirect_descendants.py)) |
| Validate redirects vs Jekyll URL map for doc moves | `./bdocs check_redirects` | [`scripts/validate_doc_redirects.rb`](../../../scripts/validate_doc_redirects.rb) |
| Find broken internal links site-wide | `./bdocs fblinks` | [`scripts/find_broken_links.ts`](../../../scripts/find_broken_links.ts) |
| List new redirect URLs for manual browser testing | `./bdocs lredirects [BASE_URL]` | [`scripts/list_new_redirect_urls.sh`](../../../scripts/list_new_redirect_urls.sh) |
| Collapse A→B→C chains inside the redirect file | `bundle exec ruby scripts/collapse_validurls_chains.rb --jekyll-map MAP.json --dry-run` then `--apply` | [`scripts/collapse_validurls_chains.rb`](../../../scripts/collapse_validurls_chains.rb) |

Run all commands from the **repository root**.

### `make_redirects.py` (`./bdocs mredirects`)

**When to use:** After you **commit** one or more renames or moves under `_docs/` on the current branch.

**Behavior:**
- Uses `git diff -M --summary` against `origin/develop` for committed renames.
- Appends `validurls['OLD'] = 'NEW';` lines near related entries.
- Skips duplicates already in the file.
- Logs unparseable renames to `scripts/temp/mredirect_logs` for manual follow-up.

**Requirements:**
- Renames must be **committed** (staged-only renames are ignored).
- Branch needs an upstream (`git push -u origin <branch>`) so the script can diff against `origin/develop`.

**When not to use:** Deleted pages without a rename, heading-only moves (`local_redirect` in frontmatter), redirects for URLs that never had a Markdown file, or cross-repo URL changes. Add those entries manually.

### `update_old_links.py` (`./bdocs ulinks`)

**When to use:** After adding or updating redirects — refresh **stale links inside Markdown** so readers do not hop through redirect chains.

**Behavior:**
- Builds a merged redirect map (handles A→B→C descendants).
- Replaces `({{site.baseurl}}/old/path)` links with the canonical new path.
- Updates YAML `link: /docs/...` lines in frontmatter and landing configs.

**Scope:** Pass a single file or directory, for example:

```bash
./bdocs ulinks _docs/_user_guide/channels/email/
```

**Test fixture:** [`docs/contributing/update_old_links.md`](../../../docs/contributing/update_old_links.md)

**Why:** Redirects are for external traffic and bookmarks. In-doc links should point to the **final** URL, not an obsolete path that redirects.

---

## Add a redirect for a renamed page

1. **Confirm the rename** — Verify the old file path no longer exists and the new path is correct under `_docs/`.
2. **Commit the rename** if it is not committed yet.
3. **Generate the redirect:**
   ```bash
   ./bdocs mredirects
   ```
4. **Review the diff** in `assets/js/broken_redirect_list.js`:
   - OLD and NEW paths are lowercase `/docs/...` URLs.
   - No duplicate of an existing entry.
   - Destination matches the new file location.
5. **If `mredirects` skipped a rename**, add the entry manually using [Convert a renamed file path to URLs](#convert-a-renamed-file-path-to-urls). Check `scripts/temp/mredirect_logs` for lines that need manual handling.
6. **Refresh in-doc links** in the touched area:
   ```bash
   ./bdocs ulinks _docs/_<collection>/<affected/path>/
   ```
7. **Validate** — Run the [Validate redirects](#validate-redirects) checklist before opening a PR.

### Manual add (given old and new file paths)

When the user supplies renamed paths (for example `_docs/_user_guide/foo/old.md` → `_docs/_user_guide/bar/new.md`):

1. Convert both paths to `/docs/...` URLs with the conversion table above.
2. Add one line: `validurls['<old_url>'] = '<new_url>';`
3. Insert near other entries sharing the same path prefix.
4. Run `node --check assets/js/broken_redirect_list.js`.

---

## Refresh stale redirect chains

Two layers: the **redirect file** (global chains) and **in-doc links** (reader experience).

### 1. Collapse chains in `broken_redirect_list.js`

When entry A→B and B→C both exist, replace A→B with A→C (and remove redundant intermediates when safe).

1. `node --check assets/js/broken_redirect_list.js`
2. Generate a Jekyll URL map:
   ```bash
   bundle exec ruby scripts/jekyll_url_map_dump.rb
   ```
3. Dry-run chain collapse:
   ```bash
   bundle exec ruby scripts/collapse_validurls_chains.rb --jekyll-map scripts/temp/jekyll_url_map.json --dry-run
   ```
4. Review output; apply when correct:
   ```bash
   bundle exec ruby scripts/collapse_validurls_chains.rb --jekyll-map scripts/temp/jekyll_url_map.json --apply
   ```
5. `node --check assets/js/broken_redirect_list.js` again.

See [Redirect list maintenance order](../../../docs/contributing/content_management/redirecting_urls.md#redirect-list-maintenance-order) in the human guide for bulk-edit sequencing.

### 2. Update stale links in Markdown (`ulinks`)

Even with a collapsed redirect file, articles may still link to obsolete paths.

```bash
./bdocs ulinks _docs/_user_guide/   # or a narrower path
```

Re-run after large IA moves. Prefer scoping `ulinks` to directories you changed to keep diffs reviewable.

---

## Validate redirects

Run these checks before opening a PR that touches `broken_redirect_list.js` or renames `_docs/` files.

### 1. JavaScript syntax

```bash
node --check assets/js/broken_redirect_list.js
```

Must pass with exit code 0 before and after edits.

### 2. Redirect coverage for renames on this branch

```bash
./bdocs check_redirects
```

Compares Jekyll-computed URLs between `origin/develop` and `HEAD` and reports missing `validurls` mappings for moved pages.

### 3. Broken link scan

Requires `yarn install` once.

```bash
./bdocs fblinks
```

Writes `scripts/temp/broken-links.csv`. Fix any broken links your change introduced; unrelated pre-existing breaks can be noted in the PR but are out of scope unless the user asked to fix them.

### 4. Manual redirect resolution (deployment or preview)

After adding redirects on the branch, list old URLs against a preview base:

```bash
./bdocs lredirects https://your-preview-url.vercel.app
```

Open each listed URL; it should resolve to the **REDIRECT_TO** destination. In VS Code, Cmd+click terminal links.

### 5. Destination exists (bulk / audit workflows)

For large redirect edits, generate a Jekyll map and audit targets:

```bash
bundle exec ruby scripts/jekyll_url_map_dump.rb
bundle exec ruby scripts/audit_validurls_targets_vs_jekyll.rb
```

Details: [Auditing redirect targets](../../../docs/contributing/content_management/redirecting_urls.md#auditing-redirect-targets-against-the-url-map) in the human guide.

### Validation checklist

- [ ] `node --check assets/js/broken_redirect_list.js` passes
- [ ] New renames have matching `validurls` entries (`./bdocs check_redirects` or manual review)
- [ ] No new redirect chains (OLD points to final URL)
- [ ] `./bdocs ulinks` run on affected `_docs/` trees when in-doc links used old paths
- [ ] `./bdocs fblinks` shows no new breaks from this branch
- [ ] Spot-check new redirects with `./bdocs lredirects` on a preview URL (when available)

---

## Gotchas

- **Don't add redirects for uncommitted renames and expect `mredirects` to work**, because the script only reads committed `git diff` renames. Commit first, or add the entry manually.
- **Don't leave uppercase in URL strings**, because production routing is case-sensitive and redirects will silently fail. Lowercase the full path even when the `.md` filename is mixed case.
- **Don't create redirect chains (A→B plus B→C)** when a single A→C entry suffices. Collapse chains in the redirect file and run `ulinks` on affected docs.
- **Don't use redirects to patch in-doc cross-links** — update the Markdown link to the canonical path instead. Redirects are for external/bookmarked URLs.
- **Don't edit `_lang/` for English redirect follow-up**, because the translation pipeline owns localized files. English redirects in `broken_redirect_list.js` apply site-wide.
- **Don't forget `node --check`** after hand-editing the redirect file. A missing semicolon or quote breaks the entire `validurls` object and fails CI.
- **Don't assume `ulinks` rewrites every link style** — it targets `{{site.baseurl}}` Markdown links and YAML `link: /docs/...` fields. Hardcoded `https://www.braze.com/docs/...` URLs in prose may need manual updates; see [cross_referencing.md](../../../docs/contributing/content_management/cross_referencing.md).

---

## Related skills

| Skill | When |
|-------|------|
| [braze-docs](../braze-docs/SKILL.md) | General link fixes, Liquid syntax, site conventions |
| [create-pr](../create-pr/SKILL.md) | Open a draft PR after redirect work; run **check-accessibility** when `_docs/` changed |
