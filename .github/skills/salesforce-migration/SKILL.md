---
alwaysApply: false
---

# Drafting docs updates from Salesforce Knowledge Base articles

Identify documentation gaps from the **KB backlog CSV**, draft updates in Braze Docs, and track completed work under Epic **BD-6308**. Triage and Phase 2 batching start from [`_data/kb_articles.csv`](_data/kb_articles.csv) and the generated queue files below.

**Self-contained workflow:** This skill needs only the `_data/` files listed below and the scripts under [`scripts/salesforce-analyzer/`](scripts/salesforce-analyzer/). No Cursor rules are required. Invoke with **`@salesforce-migration`** (or open this file directly).

---

## Primary data sources

| File | Role |
|------|------|
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | **Source of truth for backlog** — one row per article with triage fields, `doc_path`, and `suggested_change` |
| [`_data/kb_articles_actioned.md`](_data/kb_articles_actioned.md) | Generated **Phase 2 queue** — rows that passed automated Phase 1 gates |
| [`_data/kb_articles_skipped.md`](_data/kb_articles_skipped.md) | Generated **skipped** rows with skip reasons |
| [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt) | `article_id` values already in-flight or completed (Phase 2 PRs + epic); excluded from the actionable queue |
| [`_data/sf_kb_articles.csv`](_data/sf_kb_articles.csv) | Optional **full article text** (`Resolution`) for drafting when `suggested_change` is not enough |

---

## `_data/kb_articles.csv` (backlog)

UTF-8 CSV. Each row is one Salesforce Knowledge article slated for docs migration.

| Column | Description |
|--------|-------------|
| `article_id` | Salesforce Knowledge record ID (`ka…`) — **primary key** for tracking and PRs |
| `title` | Article title |
| `conflict` | Analyzer notes on docs vs. knowledge article |
| `conflict_resolution` | Triage outcome (e.g., `codebase confirms knowledge`, `overlap`, `inconclusive`) |
| `suggested_change` | What to add or update in public docs (most actionable for drafting) |
| `doc_path` | Target `_docs/...` file (may be empty — infer per [Resolve target doc path](#resolve-target-doc-path)) |
| `codebase_evidence` | Reference-repo paths or verification notes |
| `implementation_status` | Optional disposition (`actioned`, `archived`, etc.) |
| `notes` | Path-inference or SME notes |
| `phase1_skip_category` / `phase1_skip_explanation` | Populated when regenerating skipped output |

Rows whose `article_id` appears in [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt) should be **removed from this CSV** after Phase 2 PRs open (they remain in the tracker only).

---

## `_data/sf_kb_articles.csv` (full article body, optional)

Use when Phase 2 needs the original Knowledge **Resolution** text beyond `suggested_change`.

| Column | Description |
|--------|-------------|
| `Title` | Match to `title` in `kb_articles.csv` (case-insensitive) |
| `Resolution` | Full customer-facing answer (may include HTML; redact PII before publishing) |
| `Environment` | Product area hint |
| `Knowledge ID` | Salesforce ID (format may differ from `article_id`) |

**Encoding:** open with `encoding='latin-1'` (not UTF-8). The export is large with duplicate versions — use the **first row** with a non-empty `Resolution` for a given title.

**Lookup by `article_id`:** match `title` from the backlog row to `Title`, or use the user-provided article content if no match.

---

## Two-phase workflow

- **Phase 1 (backlog CSV):** Run [`scripts/salesforce-analyzer/generate_kb_phase1_outputs.py`](scripts/salesforce-analyzer/generate_kb_phase1_outputs.py), fix `doc_path` where needed, and use `_data/kb_articles_actioned.md` as the ranked queue.
- **Phase 2 (draft + PRs):** For each **PR batch** in `_data/kb_articles_actioned.md` (one primary `_docs` file per PR), draft all articles for that file, verify in reference repos, open one PR, remove those `article_id` rows from `kb_articles.csv`, and **append IDs** to [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt).

Refresh Phase 1 outputs after every CSV or tracker change. Complete Phase 1 before starting a new Phase 2 batch.

### BD-6308 actioned-article tracker

| File | Purpose |
|------|---------|
| [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt) | One `article_id` per line — epic in-flight work **plus** IDs actioned in Phase 2 PRs |
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | Backlog; set `implementation_status` to `actioned` when a PR ships (optional but recommended) |

Phase 1 must treat any ID already listed in `kb_epic_bd6308.txt` like other in-flight epic work (exclude from the actionable queue or mark skipped with reason **BD-6308 tracker**).

### Automated Phase 1 script vs agent path inference

| Step | Who / what |
|------|------------|
| **Mechanical triage** | [`scripts/salesforce-analyzer/generate_kb_phase1_outputs.py`](scripts/salesforce-analyzer/generate_kb_phase1_outputs.py) — gates, `_docs/...` extraction (including `conflict` column), IA remaps, exact/prefix maps, unique basenames, **best-fit doc placement** (topic routes + keyword scoring over FAQ/troubleshooting/reporting pages) |
| **Agent or SME** | Full [Resolve target doc path](#resolve-target-doc-path) — semantic search, reading article text, judgment when automation cannot pick a defensible file |

**Recommended workflow after updating `_data/kb_articles.csv`:**

```bash
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --infer-doc-paths --no-prune
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune
```

1. **`--infer-doc-paths`** — Writes `doc_path` when conflict text, remaps, topic routes, or **best-fit placement** resolve to a file (automated subset of [Resolve target doc path](#resolve-target-doc-path) steps 1–2 and part of 3–5). Applies to **`inconclusive`** rows too.
2. **Second run (no flag)** — Regenerates `_data/kb_articles_actioned.md` and `_data/kb_articles_skipped.md`.
3. **Manual / Cursor** — For remaining skipped rows with `codebase confirms knowledge` or `overlap`, use article title and [Resolve target doc path](#resolve-target-doc-path) (grep/semantic search), update `doc_path` in the CSV, re-run the script.

Rows with **`conflict_resolution` = `inconclusive`** are **not** auto-skipped. They enter `_data/kb_articles_actioned.md` when they resolve to a `doc_path` and pass other gates. **Phase 2 must verify behavior in reference repos** ([Step 6](#step-6-draft-updates-reference-repos--target-path)) before drafting; prefer source code over Salesforce Knowledge when they disagree.

The script does **not** replace agent review for redundant-with-live-docs checks or bug/workaround filtering.

---

# Phase 1: Triage & Prioritize

## Step 1: Regenerate the backlog queue

1. Ensure [`_data/kb_articles.csv`](_data/kb_articles.csv) is current (new analyzer rows, updated `doc_path`, dispositions).
2. From the repo root, run:

```bash
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --infer-doc-paths --no-prune
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune
```

3. Read [`_data/kb_articles_actioned.md`](_data/kb_articles_actioned.md) for the **actionable** queue and [`_data/kb_articles_skipped.md`](_data/kb_articles_skipped.md) for skips.
4. Exclude any `article_id` already in [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt) (the script treats these as skipped epic work).

For rows in `skipped` with `codebase confirms knowledge` or `overlap` but no `doc_path`, use [Resolve target doc path](#resolve-target-doc-path), update the CSV, and re-run the script.

---

## Step 2: Triage & Categorize

For each **actionable** row (or when manually reviewing a skipped row), determine if docs action is still needed:

| Category | Criteria | Action |
|----------|----------|--------|
| **Docs Gap** | Knowledge gap identified; answer exists but is missing or unclear in docs | Update existing docs |
| **New Content** | Topic not covered anywhere in public docs; recommended actions describe new page/section | Draft new section or page |
| **Edge Case** | Unusual but valid use case; FAQ-worthy | Add FAQ or troubleshooting entry |
| **Already Addressed** | Docs have been updated since ticket was filed | Skip (verify and close) |
| **`conflict_resolution`: inconclusive** | Pre-analysis did not commit to a docs change | **Actionable** if `doc_path` resolves — **must verify in reference repos** in Phase 2 before drafting |
| **Support-Only** | Account-specific, requires Braze internal access, or one-off config | Skip (no docs change) |
| **Sensitive** | "Flag sensitive information" section indicates content should remain internal | Skip (do not publish) |

> **Never document workarounds or bugs.** Documentation must describe how the product works — or is intended to work — not temporary workarounds for issues that will be (or should be) fixed. If an SF article's resolution relies on a workaround for a product defect, skip it.

Skip rows marked **INTERNAL** in the title or `suggested_change` unless the user explicitly wants public docs.

---

## Step 3: Per-article analysis

For each **actionable** row in `kb_articles_actioned.md` (or a row you are promoting from skipped):

1. **Extract the request** — Read `suggested_change`, `conflict`, and `conflict_resolution`
2. **Check for sensitive content** — Omit internal-only notes, customer PII, and support-only workflows
3. **Resolve target doc** — Follow [Resolve target doc path](#resolve-target-doc-path). Do not rely on a stale `doc_path` alone.
4. **Assign reviewer vertical** — Follow [Product vertical and ownership](#product-vertical-and-ownership) for PR assignee routing only (not PR batching)
5. **Verify against existing docs** — Read the target file; skip if the gap is already addressed
6. **Assess drafting readiness** — `suggested_change` is usually enough; otherwise look up `Resolution` in `_data/sf_kb_articles.csv` by title

### Output format per article (chat or `output.md`)

```markdown
### Article: `ka0VP…` — Title
- **Category**: [Docs Gap | New Content | Edge Case]
- **conflict_resolution**: [from CSV]
- **Knowledge gap**: [from `conflict` / analyzer notes]
- **Suggested change**: [from CSV]
- **Target doc**: `_docs/...` (or NEW: suggested_location)
- **Target doc confidence**: [CSV doc_path | Inferred from docs search | Inferred from article content]
- **Product vertical**: [e.g., Canvas, Email, Push] — or **Unknown**
- **Ready to draft**: [Yes — suggested_change sufficient | No — needs sf_kb_articles Resolution]
```

---

## Step 4: Consolidate & prioritize

Use **section 1** of `_data/kb_articles_actioned.md` (**Phase 2 PR batches — one primary `_docs` file per PR**), then:

1. **One PR per primary `doc_path`** — All articles in that batch share one file; do not split by product vertical
2. **Prioritize** — User-stated doc batch, table order (article count), or tier/score if present in CSV
3. **Route reviewers** — Use path → [assignees CSV](.github/support_analyzer_doc_assignees.csv) and the **Suggested reviewer vertical** hint ([PR batching rules](#pr-batching-rules))
4. **Maintain sources** — List every `article_id` in the PR body and tracker

### Backlog prompt to the user

After Phase 1 is complete, present a summary like:

```markdown
## Phase 1 complete — prioritized backlog

**CSV:** X rows — **Y actionable** (`kb_articles_actioned.md`) — **Z skipped** (`kb_articles_skipped.md`) — **N** in epic tracker (`kb_epic_bd6308.txt`)

| PR batch | Articles | Primary `_docs` file | Reviewer hint |
|----------|----------|----------------------|---------------|
| … | … | `_docs/...` | Email |

**Phase 2 PR plan:** N PRs (one per doc file).
To proceed: "Run Phase 2 for the PR batch `_docs/...`" or "Run Phase 2 for the next doc in `kb_articles_actioned.md`."
```

---

## Resolve target doc path

Use this whenever a backlog row has no reliable `doc_path`, paths in `codebase_evidence` or `suggested_change` are stale, URLs point at deprecated IA (`_help/help_articles/`), or the cited page no longer matches the article topic.

**Priority order:**

1. **CSV `doc_path`** — If populated and the file exists on disk, use it (confirm with a quick read of the target page).
2. **Paths in `suggested_change` / `codebase_evidence`** — Extract `_docs/...` strings; apply IA remaps (see script `PATH_FRAG_REMAPS`).
3. **Same-topic search in `_docs/`** — From `title`, `suggested_change`, and optional `sf_kb_articles` `Resolution`, search the repo (grep or semantic search) for:
   - Matching UI terms, error strings, metric names, API paths, or feature names
   - Existing FAQ, troubleshooting, or glossary pages in the same product area
   - Prefer updating an existing FAQ/troubleshooting section over creating a new page
4. **SF `Environment` (CSV)** — Map product areas to doc neighborhoods (e.g., "Dashboard" → `_docs/_user_guide/administrative/`, "SDK and Segmentation" → `_docs/_developer_guide/` or `_docs/_user_guide/audience/`, "Currents" → `_docs/_user_guide/data/distribution/braze_currents/`).
5. **IA bucket from path** — If you only know the vertical folder (e.g. `_docs/_user_guide/messaging/canvas/`), pick the most specific existing page (FAQ, troubleshooting, or parent guide) that already covers the feature class.
6. **Record inference** — In Phase 1 output, set **Target doc confidence** to `Inferred from docs search` or `Inferred from article content` and note why (one line). If no defensible target exists, mark **Ready to Draft: No** and ask the user.

**Do not** leave content in `_docs/_help/help_articles/` or publish new pages under that tree. Always land updates in `_docs/_user_guide/`, `_docs/_developer_guide/`, `_docs/_api/`, or shared `_includes/` as appropriate.

---

## Product vertical and ownership

**Product vertical** (Email, Push, Canvas, API, etc.) is for **reviewer routing and PR descriptions only**. Phase 2 PRs are **batched by primary `_docs` file**, not by vertical — one doc per PR, with multiple `article_id` values allowed per PR.

### How to determine vertical

Apply the first match that applies:

| Signal | Source | Example |
|--------|--------|---------|
| CSV `team` | `kb_articles.csv` | `docs`, product-aligned label |
| Resolved `doc_path` | Longest-prefix match in [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv) `Team` column | `Core Messaging`, `Core Objects` |
| IA bucket | First meaningful segment under `_docs/_user_guide/` or `_docs/_developer_guide/` | `messaging/canvas` → **Canvas**; `channels/email` → **Email** |
| Article + code topic | `suggested_change`, `conflict`, reference-repo domain | Canvas → `platform/.../canvas` |
| SF `Environment` | `_data/sf_kb_articles.csv` (optional lookup) | "Dashboard", "Email" |

If signals disagree, prefer **assignees CSV `Team`** (from `doc_path`) over path-only guesses. Document the choice in the PR body.

### When vertical is unclear

If reviewer ownership is unclear, set **Product vertical: TBD** in the PR body and use `@braze-inc/docs-team` or the longest-prefix match from the assignees CSV. Still batch by **`doc_path`** — do not open a separate PR per vertical guess.

---

# Phase 2: Draft Updates

## Do not edit `_docs/_help/help_articles/`

**Do not make updates to any files under `_docs/_help/help_articles/`.** If a ticket's recommended Braze Docs page or target file is under that path, do not use it as the target. Instead, look for related content elsewhere in the docs (e.g., the same product area in `_docs/_user_guide/`, relevant FAQ, or a closely related topic) and **recommend that better location** as the place to make the update. Draft and commit changes only to that alternative location.

## Step 5: Retrieve article content

For each `article_id` in the Phase 2 batch:

1. **Start from the backlog row** in `_data/kb_articles.csv` — use `title`, `suggested_change`, `conflict`, and `doc_path`.
2. **Optional full text:** If you need the original Knowledge answer, look up `title` in `_data/sf_kb_articles.csv` (`encoding='latin-1'`) and read `Resolution` (first non-empty match).
3. **If content is still insufficient:** Ask the user to paste the article body before drafting.

Before pasting any Salesforce Knowledge Base content into chats, pull requests, or public docs, **redact PII, customer-identifying details, and internal notes**.

Example lookup:

```python
import csv

def lookup_resolution(article_title: str) -> str | None:
    with open("_data/sf_kb_articles.csv", "r", encoding="latin-1") as f:
        for row in csv.DictReader(f):
            if row["Title"].strip().lower() == article_title.strip().lower():
                if row["Resolution"].strip():
                    return row["Resolution"].strip()
    return None
```

## Step 6: Draft updates (reference repos + target path)

For each backlog article where content is available (`kb_articles.csv` and optional `sf_kb_articles.csv`):

### A. Resolve where the content goes

1. If `doc_path` is missing or stale, follow [Resolve target doc path](#resolve-target-doc-path) before writing.
2. **Evaluate the full doc site**, not only the ticket URL — search for related guides, FAQs, and troubleshooting in the same vertical.
3. **Do not edit** `_docs/_help/help_articles/` — use an alternative location in `_user_guide/`, `_developer_guide/`, or `_api/`.

### B. Use reference repos to shape the draft

Follow [`.github/skills/reference-repos/SKILL.md`](.github/skills/reference-repos/SKILL.md). Reference repos are the **source of truth for what to write**, not only a post-draft check.

1. **Select repo(s)** before drafting — e.g. `platform` for dashboard/product rules (`shared_code/domains/` first), SDK folders for client behavior, `liquid` for templating, `grapesjs` for editor UI.
2. **Update repos** — Run `git pull --ff-only` in each sibling repo you will search (only those needed for this vertical).
3. **Research behavior** — Confirm APIs, limits, UI labels (`dashboard/app/javascript/src/`), error messages, and feature flags. Use feature naming (Canvas → `canvas`, Campaigns → `campaign`, etc.).
4. **Draft from verified facts** — Write steps, limitations, and metric definitions that match code. If the SF article contradicts source, prefer source and flag the discrepancy per the reference-repos skill; do not silently copy outdated SF text.
5. **Unverified claims** — If behavior cannot be found in source, keep prose minimal and do not claim verification in the PR.

### C. Write for Braze Docs

1. **Prefer refining existing content** over new alerts or FAQ entries unless the information cannot fit in existing prose.
2. **Separate public from internal content** — Omit internal notes and channels; generalize internal workflows (e.g., "contact your customer success manager").
3. Follow style guides in `docs/contributing/style_guide/*`; keep additions concise (bullets, tables, code blocks).
4. **Alerts and FAQ entries are a last resort.**
5. Do not include sensitive or internal-only content from the SF article.

### D. PR description (verification)

When content was verified using reference repos, list **repo-relative source paths** in the PR body (e.g. `platform/shared_code/domains/...`) per the reference-repos skill. Do not paste local absolute paths.

---

## Batch processing and PR grouping

When the user requests Phase 2, work from **`_data/kb_articles_actioned.md` section 1** — **one PR per primary `_docs` file**. Each PR edits **only that file** (and `_includes/` only when that file pulls shared includes you must update).

### PR batching rules

| Situation | PR strategy |
|-----------|-------------|
| Same primary `doc_path` | **One PR** — all listed `article_id` values for that path |
| Different `doc_path` values | **Separate PRs** — never combine two primary docs in one PR |
| User names a doc path | Run Phase 2 for that **PR batch** only |
| User names one `article_id` | Use its row’s `doc_path`; if others share that path, include **all** articles in that batch unless the user asks for a single article only |
| `_includes/` only | Rare — prefer the user-guide or developer-guide page that owns the topic; one primary `_docs` file per PR still applies |

Do **not** batch by product vertical. Vertical labels are for assignees and PR descriptions only.

**Recommended scope per conversation:** one doc-file PR batch (or 2–3 small single-article doc PRs), then summarize and offer the next batch from section 1.

### Batch processing flow

1. Identify scope — a **PR batch** heading in `kb_articles_actioned.md`, a `doc_path`, or explicit `article_id`(s) that resolve to one `doc_path`.
2. Confirm each article in the batch has enough content (`suggested_change` and/or `sf_kb_articles` `Resolution`).
3. For rows with **`conflict_resolution` = `inconclusive`**, **verify behavior in reference repos** ([Step 6B](#b-use-reference-repos-to-shape-the-draft)) before drafting; skip the article if source contradicts the SF text or behavior cannot be verified.
4. Pick **reviewer** from changed paths via assignees CSV (vertical hint is advisory).
5. For that **single primary doc**:
   - `git checkout develop && git pull origin develop`
   - Create branch (see Step 7)
   - Draft all sections for every `article_id` in the batch into **that file only**
   - One commit (or logical commits) per PR
   - Push → open PR (Step 9)
   - Create Jira Task under Epic **BD-6308** (Step 9b)
   - Record every `article_id` in the batch for Step 10
6. **Update BD-6308 tracker** (Step 10) after the PR is open
7. Output a summary table: primary `doc_path` | `article_id`(s) | branch | PR URL | tracker updated
8. **Refresh backlog** — Remove actioned `article_id` rows from `kb_articles.csv`, re-run `python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune`

---

## Step 10: Update `_data/kb_epic_bd6308.txt`

**Required at the end of every Phase 2 execution** (single-ticket or batch). Do this after doc PR(s) are created, not before.

### Which IDs to append

For every article processed in the run whose docs PR was opened successfully, append its Salesforce Knowledge **`article_id`** (`ka…`):

| Source | Where to get `article_id` |
|--------|---------------------------|
| CSV backlog / PR body | `article_id` column in `_data/kb_articles.csv` or PR description |
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
| Doc-file batch (default) | `sf-cursor-<doc-slug>-<YYYYMMDD>` — use **Suggested branch slug** from `kb_articles_actioned.md`, e.g. `sf-cursor-push-troubleshooting-20260527` |
| Single article, unique doc | Same as doc-file batch (still one doc per PR) |

Use lowercase slugs with hyphens (no spaces). Do not use vertical-only slugs (for example, `sf-cursor-email-…`) when multiple docs belong to that vertical.

---

## Step 8: Commit and push changes

Stage and commit changes for **one primary `_docs` file** (plus `_includes/` only when required for that page). Use a message that names the doc (e.g., `SF KB: push troubleshooting FAQ updates`). Push the branch before opening the PR.

---

## Step 9: Generate the PR

Create each PR **targeting `develop`** (`--base develop`). Always add label **`salesforce migration`** (`--label "salesforce migration"`).

### PR title

Use this format so Jira–GitHub integration can track work under Epic [**BD-6308**](https://jira.atl.braze.com/browse/BD-6308) without manual status updates:

```text
[BD-####](SF) TICKET_NAME
```

| Segment | Value |
|---------|--------|
| `[BD-####]` | Jira Task key created under BD-6308 (create the Jira issue **before** opening the PR, or rename immediately after — see Step 9b) |
| `(SF)` | Salesforce KB migration marker |
| `TICKET_NAME` | Short theme (article title or doc batch theme); omit legacy prefixes `[SF KB]` / `SF KB:` |

**Examples:** `[BD-6402](SF) Push troubleshooting and subscription updates`, `[BD-6416](SF) Liquid abort_message limitations`

Helper: `format_sf_kb_pr_title()` in [`scripts/salesforce-analyzer/sf_kb_jira_ticket.py`](scripts/salesforce-analyzer/sf_kb_jira_ticket.py). Retrofit existing PRs: `python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py`.

Include **Product vertical** in the PR body (for routing), not in the title.

### PR body

Follow `docs/contributing/style_guide.md` and `.github/PULL_REQUEST_TEMPLATE`. Include:

```text
## Product vertical
<Vertical name> — for reviewer routing

## Changes
* Files updated and what changed
* Reference-repo paths used for verification (repo-relative, e.g. platform/shared_code/...)

## Salesforce Knowledge sources
* `article_id` values (one bullet per article, e.g. `ka0VP000000…`)
* Article titles for traceability
```

### Reviewers

Use [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv): longest prefix match on changed `_docs` paths → `GitHub Username` for `--assignee`. If no match or assignee fails, request **`@braze-inc/docs-team`**. `CODEOWNERS` may also apply when populated.

---

## Step 9b: Create Jira task under Epic BD-6308

**Required after each Phase 2 PR is open** (before Step 10). Create one **BD** **Task** per PR, parent-linked to Epic [**BD-6308**](https://jira.atl.braze.com/browse/BD-6308). Match the description layout of [**BD-6402**](https://jira.atl.braze.com/browse/BD-6402):

| Section | Content |
|---------|---------|
| **GitHub PR** | Markdown link: PR title → PR URL |
| **Salesforce Knowledge articles** | Bullet per `article_id`: `` `ka…` — Article title `` (title from `_data/kb_articles.csv` when available) |
| **Product vertical** | **Suggested reviewer vertical** from `kb_articles_actioned.md` or `product_vertical_hint()` for the primary `doc_path` |

**Jira summary:** `Salesforce KB batch - <short theme>` (strip `[BD-####](SF)` / `[SF KB]` / `SF KB:` prefixes from the PR title).

**PR title (required):** `[BD-####](SF) <short theme>` — create the Jira Task first, then open the PR with this title (Phase 2 scripts do this automatically).

**Fields:** Issue type **Task**, priority **P4**, Epic Link / parent **BD-6308** (`customfield_10014` and `parent`).

### Automation

[`scripts/salesforce-analyzer/sf_kb_jira_ticket.py`](scripts/salesforce-analyzer/sf_kb_jira_ticket.py) creates the issue via Jira REST API when `JIRA_USER_EMAIL` and `JIRA_API_TOKEN` are set (same Atlassian API token as [`.github/workflows/jira-pr-comment.yml`](.github/workflows/jira-pr-comment.yml)). Optional: `JIRA_BASE_URL` (default `https://jira.atl.braze.com`), `JIRA_ASSIGNEE_ACCOUNT_ID`.

Phase 2 helper scripts call this automatically after `gh pr create` unless you pass `--skip-jira`:

```bash
python3 scripts/salesforce-analyzer/sf_kb_jira_ticket.py \
  --pr-url 'https://github.com/braze-inc/braze-docs/pull/NNNN' \
  --pr-title '[BD-6402](SF) Push troubleshooting updates' \
  --articles-from-summary "$(cat pr_summary_snippet.md)" \
  --doc-path '_docs/_user_guide/channels/push/troubleshooting.md'
```

Include the new Jira key (for example `BD-6402`) in the Phase 2 summary table: `doc_path` | `article_id`(s) | branch | PR URL | **Jira** | tracker updated.

## Source Code References

| Resource | Path |
|----------|------|
| Docs repo | (current repo) |
| Main product | `../platform` |
| KB backlog (triage + queue) | `_data/kb_articles.csv` |
| Phase 1 actionable queue | `_data/kb_articles_actioned.md` |
| Phase 1 skipped rows | `_data/kb_articles_skipped.md` |
| Full SF article text (optional) | `_data/sf_kb_articles.csv` |
| BD-6308 actioned / in-flight IDs | `_data/kb_epic_bd6308.txt` |
| Phase 1 generator | `scripts/salesforce-analyzer/generate_kb_phase1_outputs.py` |
| Phase 2 Jira task (BD-6308) | `scripts/salesforce-analyzer/sf_kb_jira_ticket.py` |
| Retrofit PR titles for BD-6308 | `scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py` |
| Phase 2 batch helper (hardcoded articles) | `scripts/salesforce-analyzer/sf_kb_phase2_one_pr_per_article.py` |

---

## Example prompts

### Phase 1: Triage and prioritize

```
@salesforce-migration Run Phase 1 on _data/kb_articles.csv (regenerate actioned/skipped).
```

```
@salesforce-migration Run Phase 1 with --infer-doc-paths and fix doc_path for skipped rows with codebase confirms knowledge.
```

### Phase 2: Draft updates

```
@salesforce-migration Run Phase 2 for the PR batch `_docs/_user_guide/channels/email/reporting/analytics_glossary.md` from kb_articles_actioned.md.
```

```
@salesforce-migration Run Phase 2 for article_id ka0VP000000NCWjYAO.
```

```
@salesforce-migration Run Phase 2 for the next doc-file PR batch in kb_articles_actioned.md section 1.
```

```
@salesforce-migration Run Phase 2 for ka0VP…. Here is the SF article Resolution:
[paste article content here]
```