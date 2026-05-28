---
name: salesforce-migration
description: >
  Analyzes Jira Salesforce Knowledge Base migration tickets and SF KB CSV exports to find doc gaps and draft updates.
  Use for SF migration Phase 1 triage, Phase 2 drafting, _data/sf_migration_tasks.xml, sf_kb_articles.csv,
  or kb_articles.csv backlog work.
---

# Drafting docs updates from Jira SF migration tickets

Analyze Jira RSS/XML exports of Salesforce Knowledge Base migration tickets to identify documentation gaps and draft docs updates.

## XML file location

The XML file is located at: `_data/sf_migration_tasks.xml`

## XML Schema

The file is a Jira RSS export (`<rss version="0.92">`) containing `<item>` elements inside `<channel>`. Each `<item>` represents one migration ticket.

### Core fields

| XML Element | Description |
|-------------|-------------|
| `<key>` | Jira ticket ID (e.g., `BD-4670`) |
| `<title>` | Ticket key + summary (e.g., `[BD-4670] How to edit Currents settings...`) |
| `<link>` | Jira URL for the ticket |
| `<summary>` | Title without the key prefix |
| `<status>` | Workflow status (e.g., `Backlog`, `In Progress`, `Done`) |
| `<priority>` | Priority level (e.g., `P1`, `P2`, `P3`) |
| `<assignee>` | Assigned team member (or `Unassigned`) |
| `<reporter>` | Person who filed the ticket |
| `<created>` | Creation timestamp |
| `<updated>` | Last update timestamp |
| `<component>` | Component tag (e.g., `PQ`) |
| `<comments>` | Contains `<comment>` elements with follow-up context |
| `<parent>` | Parent epic ticket ID |

### Custom fields (inside `<customfields>`)

| Custom Field Name | Description |
|-------------------|-------------|
| `Epic Link` | Parent epic name (e.g., `Migrate Salesforce Knowledge Base: Articles`) |
| `Team` | Assigned Braze team (e.g., `Currents`, `Email`) |
| `URL` | Link to the original Salesforce Knowledge article (inside `CDATA`) |
| `Number of Linked Issues` | Count of related support cases — higher = more customer impact |
| `Sprint` | Sprint assignment (if any) |

### Description field structure

The `<description>` field contains **HTML-encoded** content. You must decode HTML entities (`&lt;` → `<`, `&amp;` → `&`, `&apos;` → `'`, `&#160;` → non-breaking space, etc.) before parsing.

After decoding, the description follows a structured format with bolded section headers:

| Section | What it contains |
|---------|------------------|
| **Migration request** | What the ticket is asking to add or change in docs |
| **Knowledge gap** | What's missing or unclear in current public docs |
| **Recommended actions** | Specific steps to take (the most actionable field) |
| **Explanations for actions** | Additional context for why the change matters |
| **Flag sensitive information** | Content that should NOT be made public |
| **Related PQ** | Related product questions or linked tickets |
| **Recommended Braze Docs page** | Target URL(s) where the change should go |

Not every ticket uses all sections. Some tickets use a simpler format with just a paragraph of context. Adapt parsing accordingly.

---

## SF Knowledge Base article CSV

The file `_data/sf_kb_articles.csv` contains the full content of Salesforce Knowledge Base articles exported as CSV. This is the primary source of article content for Phase 2.

### CSV schema

| Column | Description |
|--------|-------------|
| `Title` | Article title — **used to match to Jira tickets** |
| `Summary` | Short article summary (may be empty) |
| `Environment` | Product area (e.g., "Dashboard", "SDK and Segmentation") |
| `Resolution` | **The main article content** — contains the customer-facing answer, steps, examples, and internal notes |
| `URL Name` | URL-friendly slug of the title |
| `Visible to Customer` | `1` if visible to customers |
| `Knowledge ID` | Salesforce record ID (different format from the Jira `sf_url` ID) |

When using the Phase 1 backlog CSV (`_data/kb_articles.csv`), also use:

| Column | Description |
|--------|-------------|
| `article_id` | Salesforce Knowledge record ID |
| `doc_path` | Resolved `_docs/...` target (may be empty — infer per [Resolve target doc path](#resolve-target-doc-path)) |
| `team` | Owning docs team label (e.g., `docs`, `kb`) |
| `codebase_evidence` | Paths or notes from reference-repo verification (Phase 1) |

### Matching tickets to articles

Match Jira tickets to CSV articles by comparing the ticket `summary` field (case-insensitive) against the CSV `Title` column. This produces an ~81% exact match rate. For unmatched tickets, try substring matching. If no match is found, the user must provide the article content manually.

**Important:** The CSV uses `latin-1` encoding (not UTF-8) due to non-breaking spaces and special characters. Always open with `encoding='latin-1'`.

### Reading article content

The `Resolution` column contains the article's answer. It may be multi-line and contain embedded newlines, HTML fragments, and special characters. The CSV is large (~48K rows with many duplicates across article versions), so when looking up an article by title, use the **first matching row** with a non-empty `Resolution` field.

---

## Two-phase workflow

Jira tickets contain **triage metadata** (what the gap is, where it should go, why it matters) but generally do NOT contain the **source content** needed to draft the docs update. The actual content lives in the linked Salesforce Knowledge Base articles, which are now available locally in the CSV.

- **Phase 1 (XML and/or CSV):** Parse, triage, categorize, prioritize, resolve target docs, assign product verticals, and produce a ranked backlog.
- **Phase 2 (CSV auto-lookup + drafting):** Draft docs updates using reference repos, open PRs **batched by product vertical** (solo PR per article when vertical is unknown), then **append actioned `article_id` values** to [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt).

Always complete Phase 1 first. For Phase 2, use the CSV to auto-retrieve article content whenever possible.

### BD-6308 actioned-article tracker

| File | Purpose |
|------|---------|
| [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt) | One `article_id` per line — Jira epic in-flight work **plus** IDs actioned in Phase 2 PRs |
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | Backlog; set `implementation_status` to `actioned` when a PR ships (optional but recommended) |

Phase 1 must treat any ID already listed in `kb_epic_bd6308.txt` like other in-flight epic work (exclude from the actionable queue or mark skipped with reason **BD-6308 tracker**).

---

# Phase 1: Triage & Prioritize

## Step 1: Parse the XML

1. Parse the RSS XML, iterating over each `<item>` element.
2. For each item, extract the core fields listed above.
3. Decode the HTML-encoded `<description>` and extract the structured sections.
4. Extract any `<comment>` elements — these often contain critical follow-up context, related article links, and refinements to the original request.
5. Extract the `URL` custom field to find the source Salesforce Knowledge article link.
6. Extract `Number of Linked Issues` to gauge customer impact.

---

## Step 2: Triage & Categorize

For each ticket, determine if docs action is needed:

| Category | Criteria | Action |
|----------|----------|--------|
| **Docs Gap** | Knowledge gap identified; answer exists but is missing or unclear in docs | Update existing docs |
| **New Content** | Topic not covered anywhere in public docs; recommended actions describe new page/section | Draft new section or page |
| **Edge Case** | Unusual but valid use case; FAQ-worthy | Add FAQ or troubleshooting entry |
| **Already Addressed** | Docs have been updated since ticket was filed | Skip (verify and close) |
| **Support-Only** | Account-specific, requires Braze internal access, or one-off config | Skip (no docs change) |
| **Sensitive** | "Flag sensitive information" section indicates content should remain internal | Skip (do not publish) |

Pay attention to `<status>` — tickets marked `Done` may already be resolved. Prioritize `Backlog` and `In Progress` tickets.

> **Never document workarounds or bugs.** Documentation must describe how the product works — or is intended to work — not temporary workarounds for issues that will be (or should be) fixed. If a ticket or SF article's resolution relies on a workaround for a product defect, skip it. Workaround content creates maintenance burden and misleads customers once the underlying issue is resolved.

---

## Step 3: Per-Ticket Analysis

For each **actionable** ticket:

1. **Extract the request** — Read the "Migration request" and "Recommended actions" sections
2. **Check for sensitive content** — Review the "Flag sensitive information" section; omit anything flagged
3. **Read comments** — Comments often refine, expand, or link related tickets
4. **Resolve target doc** — Follow [Resolve target doc path](#resolve-target-doc-path) (below). Do not rely on a stale or missing "Recommended Braze Docs page" URL alone.
5. **Assign product vertical** — Follow [Product vertical and ownership](#product-vertical-and-ownership) so Phase 2 can batch PRs correctly.
6. **Verify against existing docs** — Read the target file to check if the gap still exists
7. **Assess drafting readiness** — Determine whether the ticket description contains enough detail to draft the update, or whether the SF article content is required

### Output Format Per Ticket (to output.md and chat console)

```markdown
### Ticket: [BD-XXXX] Title
- **Category**: [Docs Gap | New Content | Edge Case]
- **Priority**: [P1 | P2 | P3]
- **Linked Cases**: [Number of Linked Issues value — indicates customer impact]
- **Knowledge Gap**: [Summary from description]
- **Recommended Action**: [What to add/update, from description]
- **Target Doc**: `_docs/_user_guide/path/to/file.md` (or "NEW: suggested_location")
- **Target doc confidence**: [Explicit ticket URL | Inferred from docs search | Inferred from article content]
- **Product vertical**: [e.g., Canvas, Email, Currents, SDK, Analytics] — or **Unknown** if ownership cannot be determined
- **SF Knowledge Article**: [URL from custom field, if present]
- **Ready to Draft**: [Yes — ticket has enough detail | No — needs SF article content]
- **Suggested Change**: [Specific content to add/update, or summary of what the SF article would need to provide]
```

---

## Step 4: Consolidate & Prioritize

After processing all tickets:

1. **Merge related tickets** — Group tickets targeting the same doc page or topic (check comments for cross-references like `Similar to ticket BD-XXXX`)
2. **Prioritize** by:
   - **Number of Linked Issues** (higher = more customers affected)
   - **Priority field** (P1 > P2 > P3)
   - **Impact** (blocks core functionality vs. nice-to-have)
   - **Effort** (quick FAQ entry vs. new guide)
3. **Batch by doc** — Group changes targeting the same primary file (candidates for a single PR when they share a vertical)
4. **Batch by product vertical** — Group actionable items by [product vertical](#product-vertical-and-ownership) for Phase 2 PR routing (one PR per vertical per run, unless vertical is unknown)
5. **Maintain sources** — Keep a list of which BD-XXXX ticket IDs (and/or `article_id` from CSV) inform each update
6. **Present the backlog** — Output the prioritized list grouped by vertical and prompt the user to provide SF article content for the top items

### Backlog prompt to the user

After Phase 1 is complete, present a summary like:

```markdown
## Phase 1 Complete — Prioritized Backlog

| Rank | Ticket | Summary | Product vertical | Target Doc | CSV Match? | Linked Issues |
|------|--------|---------|------------------|------------|------------|---------------|
| 1 | BD-XXXX | ... | Canvas | `_docs/...` | Yes | 274 |
| 2 | BD-YYYY | ... | Unknown | `_docs/...` | No | 235 |

**X of Y tickets have CSV matches and can be auto-drafted.**

**Phase 2 PR plan:** N vertical batches + M solo PRs (articles with unknown vertical).
To proceed, say: "Run Phase 2 for the top N tickets" or "Run Phase 2 for BD-XXXX".
For tickets without CSV matches, paste the article content manually.
```

---

## Resolve target doc path

Use this whenever a ticket or CSV row has no reliable `doc_path`, the recommended URL is missing, returns 404, points at deprecated IA (`_help/help_articles/`), or the cited page no longer matches the article topic.

**Priority order:**

1. **Explicit, valid path** — Ticket "Recommended Braze Docs page" maps to an existing `_docs/...` file (not under `_docs/_help/help_articles/`). Use it.
2. **Phase 1 / CSV `doc_path`** — If already populated and the file exists on disk, use it.
3. **Same-topic search in `_docs/`** — From the article `Title`, `Resolution`, and ticket summary, search the repo (grep or semantic search) for:
   - Matching UI terms, error strings, metric names, API paths, or feature names
   - Existing FAQ, troubleshooting, or glossary pages in the same product area
   - Prefer updating an existing FAQ/troubleshooting section over creating a new page
4. **SF `Environment` (CSV)** — Map product areas to doc neighborhoods (e.g., "Dashboard" → `_docs/_user_guide/administrative/`, "SDK and Segmentation" → `_docs/_developer_guide/` or `_docs/_user_guide/audience/`, "Currents" → `_docs/_user_guide/data/distribution/braze_currents/`).
5. **IA bucket from path** — If you only know the vertical folder (e.g. `_docs/_user_guide/messaging/canvas/`), pick the most specific existing page (FAQ, troubleshooting, or parent guide) that already covers the feature class.
6. **Record inference** — In Phase 1 output, set **Target doc confidence** to `Inferred from docs search` or `Inferred from article content` and note why (one line). If no defensible target exists, mark **Ready to Draft: No** and ask the user.

**Do not** leave content in `_docs/_help/help_articles/` or publish new pages under that tree. Always land updates in `_docs/_user_guide/`, `_docs/_developer_guide/`, `_docs/_api/`, or shared `_includes/` as appropriate.

---

## Product vertical and ownership

**Product vertical** is the docs/product area used to **batch pull requests** so the right reviewers see related changes together (Email, Push, SMS, Canvas, API, Currents, SDK, Analytics, Partners, Dashboard & administration, etc.).

### How to determine vertical

Apply the first match that applies:

| Signal | Source | Example |
|--------|--------|---------|
| Jira team | XML `Team` custom field | `Currents`, `Email` |
| CSV team / assignee | `kb_articles.csv` `team`, `assigned_to` | `docs`, product-aligned assignee |
| SF environment | CSV `Environment` | "Dashboard", "Email" |
| Resolved `doc_path` | Longest-prefix match in [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv) `Team` column | `Core Messaging`, `Core Objects` |
| IA bucket | First meaningful segment under `_docs/_user_guide/` or `_docs/_developer_guide/` | `messaging/canvas` → **Canvas**; `channels/email` → **Email**; `data/distribution/braze_currents` → **Currents** |
| Article + code topic | Feature names in Resolution + reference-repo domain | Canvas → `platform/.../canvas`; push KVP → channel push docs |

If two signals disagree, prefer **Jira `Team`** or **assignees CSV `Team`** over path-only guesses. Document the choice in the PR body.

### When vertical is unknown

If you cannot assign a vertical with reasonable confidence after the steps above, set **Product vertical: Unknown**. Those articles get **their own PR** (one article per PR), not merged into a vertical batch.

---

# Phase 2: Draft Updates

## Do not edit `_docs/_help/help_articles/`

**Do not make updates to any files under `_docs/_help/help_articles/`.** If a ticket's recommended Braze Docs page or target file is under that path, do not use it as the target. Instead, look for related content elsewhere in the docs (e.g., the same product area in `_docs/_user_guide/`, relevant FAQ, or a closely related topic) and **recommend that better location** as the place to make the update. Draft and commit changes only to that alternative location.

## Step 5: Retrieve article content

For each ticket being processed:

1. **Auto-lookup from CSV:** Use Python to read `_data/sf_kb_articles.csv` (with `encoding='latin-1'`) and find the first row where the `Title` column matches the Jira ticket's `summary` (case-insensitive). Extract the `Resolution` column as the article content.
2. **If no CSV match:** Prompt the user to paste the article content manually before proceeding.
3. **If the `Resolution` field is empty:** The CSV row exists but has no useful content. Prompt the user.

Before pasting any Salesforce Knowledge Base content into chats, pull requests, or using it to draft public documentation or commit changes, **redact or remove all PII, customer-identifying details, and internal or sensitive notes**. Only include anonymized, generalized technical information that is appropriate for public Braze Docs.
Example Python lookup:
```python
import csv
def lookup_article(ticket_summary):
    with open('_data/sf_kb_articles.csv', 'r', encoding='latin-1') as f:
        for row in csv.DictReader(f):
            if row['Title'].strip().lower() == ticket_summary.strip().lower():
                if row['Resolution'].strip():
                    return row['Resolution'].strip()
    return None  # No match — ask user
```

## Step 6: Draft updates (reference repos + target path)

For each ticket or KB article where content is available (from CSV or user):

### A. Resolve where the content goes

1. If `doc_path` is missing or the ticket URL is stale, follow [Resolve target doc path](#resolve-target-doc-path) before writing.
2. **Evaluate the full doc site**, not only the ticket URL — search for related guides, FAQs, and troubleshooting in the same vertical.
3. **Do not edit** `_docs/_help/help_articles/` — use an alternative location in `_user_guide/`, `_developer_guide/`, or `_api/`.

### B. Use reference repos to shape the draft

Follow [`../reference-repos/SKILL.md`](../reference-repos/SKILL.md). Reference repos are the **source of truth for what to write**, not only a post-draft check.

1. **Select repo(s)** before drafting — e.g. `platform` for dashboard/product rules (`shared_code/domains/` first), SDK folders for client behavior, `liquid` for templating, `grapesjs` for editor UI.
2. **Update repos** — Run `git pull --ff-only` in each sibling repo you will search (only those needed for this vertical).
3. **Research behavior** — Confirm APIs, limits, UI labels (`dashboard/app/javascript/src/`), error messages, and feature flags. Use feature naming (Canvas → `canvas`, Campaigns → `campaign`, etc.).
4. **Draft from verified facts** — Write steps, limitations, and metric definitions that match code. If the SF article contradicts source, prefer source and [flag the discrepancy](../reference-repos/SKILL.md); do not silently copy outdated SF text.
5. **Unverified claims** — If behavior cannot be found in source, keep prose minimal and do not claim verification in the PR.

### C. Write for Braze Docs

1. **Prefer refining existing content** over new alerts or FAQ entries unless the information cannot fit in existing prose.
2. **Separate public from internal content** — Omit internal notes and channels; generalize internal workflows (e.g., "contact your customer success manager").
3. Follow style guides in `docs/contributing/style_guide/*`; keep additions concise (bullets, tables, code blocks).
4. **Alerts and FAQ entries are a last resort.**
5. Do not include content flagged sensitive in the ticket or SF article.

### D. PR description (verification)

When content was verified using reference repos, list **repo-relative source paths** in the PR body (e.g. `platform/shared_code/domains/...`) per reference-repos rules. Do not paste local absolute paths.

---

## Batch processing and PR grouping

When the user requests batch Phase 2 (e.g., "run Phase 2 on the top 10" or "run Phase 2 for all matched Email articles"), **group work by product vertical**, not one PR per article by default.

### PR batching rules

| Situation | PR strategy |
|-----------|-------------|
| Same **product vertical**, multiple articles/tickets | **One PR per vertical** for that run — all doc edits for that vertical on one branch |
| Same vertical **and** same primary `doc_path` | Strongly prefer one PR (combine sections in one file) |
| **Unknown** product vertical | **One PR per article** (solo PR) |
| User asks for isolated review | Honor explicit request (e.g., single BD ticket only) |

Within a vertical PR, you may touch **multiple files** if different articles map to different targets in the same vertical.

**Recommended scope per conversation:** one vertical batch (or 3–5 solo PRs), then summarize and offer the next vertical.

### Batch processing flow

1. Identify scope (tickets, CSV rows, or vertical filter).
2. Filter to items with CSV `Resolution` (or user-provided content).
3. Assign **product vertical** to each item; mark **Unknown** where needed.
4. **Group** items by vertical; split **Unknown** into solo groups.
5. For each PR group (vertical batch or solo article):
   - `git checkout develop && git pull origin develop`
   - Create branch (see Step 7)
   - For each item in the group: resolve path → reference-repo research → draft → stage
   - One commit (or logical commits) per PR group
   - Push → open PR (Step 9)
   - Record each successful PR's `article_id`(s) for Step 10
6. **Update BD-6308 tracker** (Step 10) — once per Phase 2 run, after all PRs for that run are open
7. Output a summary table: vertical | articles/tickets | branch | PR URL | Jira keys | `article_id`(s) appended to tracker

---

## Step 10: Update `_data/kb_epic_bd6308.txt`

**Required at the end of every Phase 2 execution** (single-ticket or batch). Do this after doc PR(s) are created, not before.

### Which IDs to append

For every article processed in the run whose docs PR was opened successfully, append its Salesforce Knowledge **`article_id`** (`ka…`):

| Source | Where to get `article_id` |
|--------|---------------------------|
| CSV backlog | `article_id` column in `_data/kb_articles.csv` |
| Jira ticket | `ka…` in the `URL` custom field, description, or PR body you drafted |
| User-provided | ID the user supplied with pasted article content |

Do **not** append IDs for skipped items, failed PRs, or articles left in draft without an open PR.

### How to update the file

1. Read [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt). Preserve all `#` comment lines at the top.
2. Parse existing IDs (non-empty, non-comment lines).
3. Add new IDs from this Phase 2 run; **skip duplicates**.
4. Rewrite the ID block: **one ID per line**, entire list **sorted alphabetically** (case-sensitive).
5. Optionally set `implementation_status` to `actioned` for those rows in `_data/kb_articles.csv` on the workflow branch (do not block the tracker update if CSV columns differ).

Example:

```python
from pathlib import Path

TRACKER = Path("_data/kb_epic_bd6308.txt")

def update_bd6308_tracker(new_ids: list[str]) -> list[str]:
    lines = TRACKER.read_text(encoding="utf-8").splitlines()
    header, ids = [], []
    for line in lines:
        s = line.strip()
        if not s or s.startswith("#"):
            header.append(line)
        else:
            ids.append(s)
    existing = set(ids)
    added = [i.strip() for i in new_ids if i.strip() and i.strip() not in existing]
    if not added:
        return []
    merged = sorted(existing | set(added))
    body = "\n".join(header + [""] if header and header[-1].strip() else header)
    if body and not body.endswith("\n"):
        body += "\n"
    TRACKER.write_text(body + "\n".join(merged) + "\n", encoding="utf-8")
    return added
```

### Commit the tracker

Commit `_data/kb_epic_bd6308.txt` (and CSV `implementation_status` updates if any) on the **workflow/data branch** (e.g. `sf-main-branch`), not on doc feature branches:

```bash
git checkout sf-main-branch && git pull origin sf-main-branch
# apply tracker + optional CSV updates
git add _data/kb_epic_bd6308.txt _data/kb_articles.csv
git commit -m "Track Phase 2 actioned SF KB articles (BD-6308)"
git push origin sf-main-branch
```

In the Phase 2 summary, list **newly appended** `article_id` values and confirm the tracker commit was pushed.

---

## Step 7: Create a properly named branch

**Always branch off `develop`**, not `main`. Before creating the branch:

```bash
git checkout develop && git pull origin develop
```

| PR type | Branch naming |
|---------|----------------|
| Vertical batch | `sf-cursor-<vertical-slug>-<YYYYMMDD>` — e.g. `sf-cursor-canvas-20260526` |
| Solo (unknown vertical) | `sf-cursor-<ticket-key>` or `sf-cursor-<article_id>` — e.g. `sf-cursor-bd-4040`, `sf-cursor-ka0VP0000001IkTYAU` |

Use lowercase slugs with hyphens (no spaces).

---

## Step 8: Commit and push changes

Stage and commit all changes for that PR group in `_docs/` (and `_includes/` when needed). Use a message that reflects the vertical or theme (e.g., `SF KB: Canvas FAQ and troubleshooting updates`). Push the branch before opening the PR.

---

## Step 9: Generate the PR

Create each PR **targeting `develop`** (`--base develop`). Always add label **`salesforce migration`** (`--label "salesforce migration"`).

### PR title

| PR type | Title |
|---------|--------|
| Single Jira ticket drives the whole PR | **Exactly** `issue.title` (including `[BD-NUMBER]` prefix) — do not alter |
| Vertical batch (multiple tickets/articles) | `[SF KB] <Product vertical>: <short theme>` — e.g. `[SF KB] Canvas: FAQ and troubleshooting updates` |
| Solo article, no Jira | `[SF KB] <Article title shortened>` |

### PR body

Follow `docs/contributing/style_guide.md` and `.github/PULL_REQUEST_TEMPLATE`. Include:

```text
## Product vertical
<Vertical name> — for reviewer routing

## Changes
* Files updated and what changed
* Reference-repo paths used for verification (repo-relative, e.g. platform/shared_code/...)

## Jira / Salesforce sources
* https://jira.atl.braze.com/browse/<ticket key> (one bullet per ticket)
* SF Knowledge article IDs or URLs where applicable
```

### Reviewers

Use [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv): longest prefix match on changed `_docs` paths → `GitHub Username` for `--assignee`. If no match or assignee fails, request **`@braze-inc/docs-team`**. `CODEOWNERS` may also apply when populated.

## Source Code References

| Resource | Path |
|----------|------|
| Docs repo | (current repo) |
| Main product | `../platform` |
| Jira XML export | `_data/sf_migration_tasks.xml` |
| Jira parsed JSON | `_data/sf_migration_parsed.json` |
| SF KB articles CSV | `_data/sf_kb_articles.csv` |
| BD-6308 actioned / in-flight article IDs | `_data/kb_epic_bd6308.txt` |


## Example Prompts

### Phase 1: Triage and prioritize

```
@salesforce-migration Run Phase 1 on the Jira XML export.
Focus on [specific product area or priority level] if applicable.
```

```
@salesforce-migration Run Phase 1 on only P1 tickets from the Jira XML.
```

```
@salesforce-migration Run Phase 1 on tickets assigned to the Currents team.
```

### Phase 2: Draft updates (auto-lookup from CSV)

```
@salesforce-migration Run Phase 2 for BD-4670.
```

```
@salesforce-migration Run Phase 2 for the top 5 tickets by linked issues.
```

```
@salesforce-migration Run Phase 2 for all matched Email team tickets (one PR per vertical).
```

```
@salesforce-migration Run Phase 2 for the Canvas vertical batch from Phase 1.
```

```
@salesforce-migration Run Phase 2 for BD-4670. The CSV didn't have a match, so here is the SF article content:
[paste article content here]
```
