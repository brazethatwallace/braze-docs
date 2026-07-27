---
name: create-pr
description: >
  Create high-quality draft pull requests for braze-docs with descriptive summaries,
  pre-PR gate checks, and repo-aligned templates. Use when creating a PR, opening a
  pull request, submitting changes for review, or after finishing a docs or site edit branch.
allowed-tools: Bash(git *), Bash(gh *), Read, Grep
---

# Creating Pull Requests

A good PR description tells a reviewer what changed, why, and what to check — without making them reconstruct it from the diff. This skill produces that description and opens the PR as a **draft** to `develop`.

Human-facing PR guidance: [`.github/PULL_REQUEST_TEMPLATE`](../../../.github/PULL_REQUEST_TEMPLATE) and [your first contribution](../../../docs/contributing/your_first_contribution.md).

## Context

- Branch: !`git branch --show-current`
- Changed files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only $(git merge-base HEAD $(git rev-parse --verify origin/develop 2>/dev/null || git rev-parse --verify develop 2>/dev/null || echo HEAD~1))..HEAD 2>/dev/null`

## Team PR template variants

Some workflows use a different PR body format while sharing this workflow (Steps 0–1, 3–4, quality checklist, anti-patterns):

| Skill | When to use |
| ----- | ----------- |
| [`support-analyzer`](../support-analyzer/SKILL.md) | Support case–driven doc updates (`[SA]` title, case links) |
| [`slack-to-docs`](../slack-to-docs/SKILL.md) | Slack SME channel mining → source-verified doc PRs with thread citations |
| [`docs-discrepancies`](../docs-discrepancies/SKILL.md) | Doc vs platform source audits (`[DD]` title) |
| [`image-pruner`](../image-pruner/SKILL.md) | Unreferenced image cleanup (`[IP]` title) |
| [`tam-solutions`](../tam-solutions/SKILL.md) | TAM → example library articles (`[TAM solutions]` title) |
| [`salesforce-migration`](../salesforce-migration/SKILL.md) | Salesforce KB migration batches (`[BD-####](SF)` title) |
| [feedback-handler agent](../../../.cursor/agents/feedback-handler.md) | Jira feedback automation (`[BD-1234] - title`, assignee mapping from ticket) |

Team variant skills are **thin wrappers** — they delegate here for shared workflow and only override Step 2 (description format). **Edits to Steps 0–1, 3–4, checklist, or anti-patterns in this file apply to all variants.**

The [feedback-handler](../../../.cursor/agents/feedback-handler.md) agent **must** run Steps 0–1 here (including Style QA on prose) before opening its draft PR, and should follow Steps 3–4 for title/draft conventions except where that agent overrides title, body, assignee, or label rules.

## Step 0: Pre-PR gates

Run applicable gates **before** writing the PR description. Skip gates that do not match changed files.

| Changed paths | Run first |
|---------------|-----------|
| `_docs/**`, root `_includes/**`, `_layouts/**`, `assets/js/**`, `assets/css/**`, `assets/scss/**` | **REQUIRED SUB-SKILL:** [check-accessibility](../check-accessibility/SKILL.md) (`braze-docs:check-accessibility`) |
| `_docs/**/*.md`, root `_includes/**/*.md` | **REQUIRED SUB-SKILL:** [spell-check](../spell-check/SKILL.md) (`braze-docs:spell-check`) |
| `_docs/**/*.md`, root `_includes/**/*.md` (prose edits) | **Style QA (required):** follow [style-qa-changed-files.md](../braze-docs/workflows/style-qa-changed-files.md) — load [writing-style.md](../braze-docs/references/writing-style.md) and [glossary.md](../braze-docs/references/glossary.md), fix bold-for-emphasis and glossary casing on **changed lines only**, and never touch `_docs/_hidden/other/support_contact.md` unless the change is explicitly about that page |
| `assets/img/**` (new or updated screenshots) | **REQUIRED SUB-SKILL:** [screenshot-pii-audit](../screenshot-pii-audit/SKILL.md) (`braze-docs:screenshot-pii-audit`). Skip for deletion-only image-pruner batches with no added or replaced images. |
| Root `_includes/**` added/deleted/renamed, or `{% multi_lang_include %}` / `{% include %}` lines added or removed in `_docs/**` or root `_includes/**` | **Include hygiene (advisory):** follow [include-hygiene.md](../braze-docs/workflows/include-hygiene.md) — run `python3 scripts/find_single_use_includes.py`, confirm `jekyll build` passes, and note remaining single-use count in the PR body when the change is part of include cleanup |
| Product behavior claims in prose | **REQUIRED SUB-SKILL:** [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) when verifying against source; note verification in the PR body without pasting `platform/` or SDK paths |

If Style QA finds issues in the prose diff, fix them (or note intentional exceptions in the PR body) before continuing to Step 1.

If the user invoked a team variant skill, follow that skill's wait gates (for example tam-solutions approval) before continuing.

## Step 1: Understand the full change

Find the base branch (`develop`), then read the **complete** diff against it — not just the latest commit.

```bash
BASE=develop
MERGE_BASE=$(git merge-base HEAD "origin/$BASE")

git status
git log --reverse "$MERGE_BASE"..HEAD --format='%h %s'   # every commit on the branch
git diff "$MERGE_BASE"..HEAD --stat                      # files touched
git diff "$MERGE_BASE"..HEAD                             # the actual change
```

Also confirm the branch tracks `origin` and is pushed (or push before opening the PR).

Confirm the diff does not include credentials, `.env` files, or other secrets before pushing.

From the diff and surrounding code, pin down:

- **What changed for readers** — not which files, but what the docs site or content now does differently.
- **Why it exists** — ticket, support case theme, doc gap, or the problem that motivated it. Check branch name and commits for a ticket key (for example `BD-1234`, `WA-1234`).
- **What was decided** — alternatives rejected, tradeoffs accepted, scope constraints.
- **What's risky** — shared `_includes/`, layouts, JS/CSS, redirects, `_lang/` scope, revert path.

If anything is unclear from the code alone (especially the *why*), ask the user before writing — a confident but wrong rationale is worse than asking.

## Step 2: Write the description

Use this structure. It mirrors [`.github/PULL_REQUEST_TEMPLATE`](../../../.github/PULL_REQUEST_TEMPLATE). Scale to the change: a typo fix needs **Why** and maybe a ticket link; a large refactor needs every section. Drop any section that would be empty or trivially obvious.

When a team variant skill is active, use that skill's Step 2 override for title prefix, label, reviewer rules, and any extra body sections — then still include the **Contributor checklist** from below unless the variant explicitly replaces it.

```markdown
### Why are you making this change? (required)

<1–2 sentences on the outcome this PR enables for readers — the user or business effect, not the implementation. Save the "how" for Approach.>

### Related PRs, issues, or features (optional)

- [BD-1234](https://jira.atl.braze.com/browse/BD-1234)
- Fixes #ISSUE_NUMBER

### Feature release date (optional)

- N/A

### Approach (optional — drop for trivial PRs)

<Decisions, not narration. The diff already shows what changed; explain what it doesn't:
- alternatives considered and why this one won
- tradeoffs accepted (scope vs timeline, prose vs new page)
- non-obvious constraints (redirects, canonical English vs `_lang/`, shared includes)

Skip this section entirely for trivial PRs.>

### Verification

<Manual verification only — see examples below. Never list steps CI already runs.>

### Contributor checklist

- [ ] I confirm that my PR meets the following:
    - My style and voice follow the [in-repo Braze Docs style guide](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/style_guide.md), especially the [writing style guide](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/style_guide/writing_style_guide.md). For images, alerts, and API pages, see [image style](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/style_guide/image_style_guide.md), [alerts](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/style_guide/alerts.md), and [API endpoint guidelines](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/style_guide/api_endpoint_guidelines.md) as needed.
    - My content contains correct spelling and grammar.
    - All links are working correctly.
    - If I renamed or moved a file or directory, I set up [URL redirects](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md) for each file.
    - If I updated or replaced an image, I did not remove the original image file from the repository. (For more information, see [Updating an image](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/images.md).)
    - If my PR is related to a paid SKU, third party, SMS, AI, or privacy, I have received written approval from Braze Legal.
```

### Verification examples (manual only)

**Do not** checklist CI jobs — CI already runs these on every PR:

- `broken-links.yml`, `check-content-accessibility.yml`, `check-table-accessibility.yml`, `check-screenshot-pii.yml`, `check-snippet-pii.yml`, `cspell.yml`, `review-docs-style.yml`, `lighthouse-ci.yml`

**Do** checklist what a human must verify:

- [ ] Vercel preview: open changed pages (comment `@braze-inc/docs-team` for a preview if needed)
- [ ] Local preview (`rake` or `bdocs`) — especially nav, TOC, or alerts when site chrome changed
- [ ] Click through moved URLs and redirect targets after renames
- [ ] Spot-check new or updated screenshots and alt text on affected pages
- [ ] Keyboard and focus behavior for layout or JS changes CI cannot fully cover

### Docs house checklist

Call these out in **Approach** or **Verification** when relevant — do not leave reviewers to ask:

| Topic | braze-docs rule |
|-------|-----------------|
| **Locale** | English canonical under `_docs/` and root `_includes/` only; `_lang/` edits only when the user scoped locale work |
| **Redirects** | `broken_redirect_list.js` and [redirecting URLs](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md) when renaming or moving pages |
| **Images** | Do not delete replaced originals; run screenshot PII audit when adding or updating screenshots |
| **Legal** | Paid SKU, third party, SMS, AI, or privacy — written Braze Legal approval |
| **URLs** | `{{site.baseurl}}` and **no** trailing slashes on internal links (production uses `trailingSlash: false`) |
| **Includes** | Run [include-hygiene.md](../braze-docs/workflows/include-hygiene.md) when adding, removing, or renaming root `_includes/` files or changing include references |
| **Revertibility** | Especially for shared `_includes/`, layouts, JS, and CSS |

## Step 3: Write the title

**Default:** `[BD-1234] Imperative description`

- Imperative mood: "Add rate limiting docs", not "Added rate limiting docs".
- Include the ticket key when one exists (check branch name and commits; `BD` is the usual docs Jira project).
- Specific over generic: "Clarify segment export limits", not "Fix docs".
- Under ~72 characters when possible.

**Variant prefixes** (when invoked via a wrapper skill):

| Prefix | Skill |
|--------|-------|
| `[SA]` | support-analyzer |
| `[DD]` | docs-discrepancies |
| `[IP]` | image-pruner |
| `[TAM solutions]` | tam-solutions |
| `[BD-####](SF)` | salesforce-migration |
| `[BD-1234] - title` | feedback-handler (Jira feedback automation) |

## Step 4: Open as a draft

**Always `--draft` and `--base develop`.** This lets CI and bots run before human reviewers are notified; the author marks the PR ready once checks pass.

Push the branch if needed, then create the PR with a heredoc so formatting survives:

```bash
git push -u origin HEAD

gh pr create --draft --base develop \
  --title "[BD-1234] Imperative description" \
  --body "$(cat <<'EOF'
### Why are you making this change? (required)

...

### Contributor checklist

- [ ] I confirm that my PR meets the following:
    ...
EOF
)"
```

After create (when applicable):

```bash
gh pr edit --add-label "<workflow label>"    # variant skills only
gh pr edit --add-assignee <github-login>     # vertical tech writer — see below
```

### Tech writer assignee (not reviewer)

After creating the draft PR, set the **assignee** to the [tech writer for the vertical](https://confluence.atl.braze.com/wiki/x/nAZuE) (Technical Writing page on Confluence). Use their **GitHub login**, not their display name.

```bash
gh pr edit --add-assignee <github-login>
```

- **Do not** add the vertical tech writer as a reviewer (`--add-reviewer`). Ownership is tracked via assignee.
- If the contributor **is** the vertical tech writer, they are already the default assignee — leave assignee as-is.
- If you cannot determine the vertical owner, leave assignee unset and note it in the handoff for the contributor to set.
- Optionally request review from SMEs or engineers cited in the PR; that is separate from assignee.
- Use [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) or variant-specific assignee rules when they apply.

**Confirm with the user before running `gh pr create`** unless they have already asked you to open the PR without asking.

After CI passes, the author selects **Ready for review** and requests review from relevant SMEs or engineers per [PULL_REQUEST_TEMPLATE](../../../.github/PULL_REQUEST_TEMPLATE). The vertical tech writer is already the assignee.

## Quality checklist

- [ ] **Pre-PR gates ran** — accessibility, spell-check, Style QA, screenshot PII, include hygiene, or reference verification when changed files require them.
- [ ] **The "why" is clear** — a reader cold to this work understands the motivation.
- [ ] **Decisions are explained, not the diff** — no "updated `_doc_guide.scss`" without reader impact.
- [ ] **Verification is real** — manual scenarios only; no CI-automated steps in the checklist.
- [ ] **House checklist addressed** — locale scope, redirects, images, legal, URLs, revertibility where relevant.
- [ ] **Title is specific** and carries the ticket key or variant prefix.
- [ ] **Draft first** — not opened as ready for review before CI runs.

## Anti-patterns

- **Summary that's just a Jira link** — the PR must stand alone.
- **"Updated docs"** — say what, why, and what's better now.
- **Narrating the diff** — explain why the content exists, not what files changed.
- **Pasting the whole diff** — summarize and explain; don't duplicate.
- **Skipping risk signal** — even "low risk, copy-only" helps the reviewer.
- **Checklisting CI's job** — "run broken links / cspell / accessibility checks" is noise; CI does it. The checklist is for manual verification only.
- **Editing `_lang/`** in the same PR as English canonical fixes without calling it out.
- **Customer or account PII in the PR body** — link to Jira or Salesforce cases only; do not paste customer names, emails, or ticket prose that may contain PII.
- **Marking the contributor checklist complete** (`[x]`) unless the author has confirmed each item.
- **Skipping Style QA on prose diffs** — bold-for-emphasis and glossary casing slips are common; run [style-qa-changed-files.md](../braze-docs/workflows/style-qa-changed-files.md) before opening the PR.
