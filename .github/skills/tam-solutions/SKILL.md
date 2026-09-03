---
name: tam-solutions
description: >
  Generalizes Technical Account Management (TAM) solutions from Confluence or Google Drive into public
  User Guide Example library articles under _docs/_user_guide/example_library/. Audits completeness and
  product accuracy, applies FakeBrandz generalization, and opens draft PRs. Use when migrating TAM
  solutions, building the Operator Example library, or when the user mentions tam-solutions or TAM
  solution docs.
---

# TAM solutions → User Guide example library

Turn internal TAM solution assets into generalized, product-accurate articles for the Braze User Guide.

**REQUIRED SUB-SKILL:** For prose and structure use [braze-docs](../braze-docs/SKILL.md) (`braze-docs:braze-docs`). 
**REQUIRED SUB-SKILL:** For product verification use [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`). Open [`braze-workspace.code-workspace`](../../../braze-workspace.code-workspace) so `platform` and SDK repos are sibling folders when verifying behavior.
**Output location:** `_docs/_user_guide/example_library/` (English canonical only; do not edit `_lang/`).

## Context
- Current branch: !`git branch --show-current`
- Modified files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only $(git merge-base HEAD $(git rev-parse --verify origin/develop 2>/dev/null || git rev-parse --verify develop 2>/dev/null || echo HEAD~1))..HEAD 2>/dev/null`
- Open PR: !`gh pr view --json number,title,body 2>/dev/null || echo "none"`

---

## Source material

TAM solutions may live in any of these sources. Use whichever the user provides, or search Drive and Confluence when auditing inventory.

| Source | Location |
|--------|----------|
| **Google Doc URL** | User supplies a `docs.google.com/document/d/<ID>/` link — read via Google Docs MCP (see below) |
| **Google Drive folder** | [TAM Assets folder](https://drive.google.com/drive/folders/1APchTnf3UWN6MGpGkeBfryGMn73LBUM0) |
| **Confluence** | TAM solution pages (user supplies URL), or Atlassian MCP when available |
| **Local JSON export** | `_data/tam_solutions/export_<YYYYMMDD>.json` from [`scripts/tam-solutions/export_drive_solutions.py`](../../../scripts/tam-solutions/export_drive_solutions.py) |
| **Example library tracker** | [TAM solutions to Docs tracker — Example library](https://docs.google.com/spreadsheets/d/1YChWu-L-hPMRo9cVIMfqSYKBQQdNRs4PkFnXPnKk5RE/edit) — **Product team** per solution (used as **Product team:** on the BD Story). After the draft PR exists, write the PR URL into **PR link** on the matching row (see Step 7). |

### Google Doc URL

Do **not** `WebFetch` private Docs URLs (SSO). When the user gives a Google Doc link:

1. Parse the document ID from `https://docs.google.com/document/d/<DOCUMENT_ID>/edit` (the path segment after `/d/`).
2. If Google Docs MCP is available, call `get_document` with `document_id` set to that ID. Do **not** set `include_comments` (comment metadata can include emails).
3. Run Step 1 audit on the returned plain text. Record the original Docs URL for the PR **TAM source** line.
4. If MCP is missing, unauthorized, or the call fails (no access, not a native Doc), ask the user to **paste** the relevant sections or to run the Drive export below. Do not guess the TAM content.

Word uploads (`.doc` / `.docx`) may still return via `get_document`. PDFs and other Drive files are not Google Docs — use paste, convert to a Doc, or `gdrive` file read if available.

### Google Drive export (optional)

For bulk inventory or offline triage (a folder of Docs, not a single URL), run the Drive export script locally:

```bash
pip install google-api-python-client google-auth
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
export TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1
python3 scripts/tam-solutions/export_drive_solutions.py
```

- Share the TAM Assets folder with the service account email (Viewer), or use `--oauth` (see [scripts/tam-solutions/README.md](../../../scripts/tam-solutions/README.md)).
- Output defaults to `_data/tam_solutions/export_<YYYYMMDD>.json` (gitignored). JSON includes `title`, `path`, `category`, `web_view_link`, and plain-text `text` per Google Doc.
- **Google Docs only** — PDFs in Drive are listed in `skipped`; paste those or convert to Google Docs.
- Treat exports as sensitive until generalized. Do not commit raw JSON to `develop`.

When the user invokes this skill with a local export file, read the matching `solutions[]` entry by `title`, `path`, or `web_view_link` instead of fetching Drive.

**Reading sources (fallback order):** Google Doc URL (Docs MCP `get_document`) → local JSON export → user paste → Confluence (MCP) → Drive folder URL (not a substitute for a single Doc). If all fail, ask the user to paste or export before continuing.

**Traceability:** Record the exact source URL (Google Doc URL, Drive `web_view_link`, Confluence page URL, or export path) for the PR body. Never paste raw internal content that contains customer PII into public PR descriptions.

---

## Hard-skip (do not publish)

Do not draft or open a PR when the TAM solution is primarily:

| Category | Why |
|----------|-----|
| **Workaround** | Docs describe intended product behavior, not temporary fixes for defects |
| **Bug / product defect** | Escalate to Engineering; do not document as an example |
| **Unreleased feature** | Not yet available to customers |
| **Account-specific setup** | Requires Braze internal access, one-off config, or customer-specific identifiers that cannot be generalized |

If only part of a solution is skippable, extract the generalizable portion only when the published article still stands alone without the skipped material.

---

## Step 1: Read and audit the TAM solution

For each solution the user assigns. If they provide a Google Doc URL, follow **Google Doc URL** above before auditing.

### 1a. Completeness

A **complete** TAM solution has all three internal parts. Map them to public sections in Step 4.

| TAM part | Maps to public section |
|----------|------------------------|
| Example summary | **About this example** |
| Solution explanation | **Step-by-step setup** |
| General considerations | **General considerations** |

If any part is missing or too thin to generalize, report the gap in the audit output and **stop** unless the user explicitly approves proceeding with partial content.

### 1b. Product accuracy

Cross-check claims against source code per [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`). Do not rely on the TAM text or existing docs alone.

- Pull sibling repos before searching (`git pull --ff-only` in each repo you need).
- If behavior is verified, note which repos you searched in your analysis.
- If you cannot verify, say so explicitly. Do not infer or speculate.
- If TAM text contradicts source, flag **Docs discrepancy** and align the draft with source (or stop and ask the user if the gap is unclear).

For **public** PR descriptions, use **Verified against Braze source code.** — do not paste internal `platform` or SDK repo paths in the PR body (see Step 7).

### 1c. PII and customer-specific content

Remove or replace before drafting:

- Customer or company names
- Real product, event, campaign, or Canvas names from a customer workspace
- Customer-specific custom attributes, API keys, workspace IDs, or account details
- Support case references tied to a real customer

Follow workspace privacy rules in [`.cursor/rules/privacy-and-security.mdc`](../../../.cursor/rules/privacy-and-security.mdc).

### 1d. Duplicate check

Before drafting, search `_docs/` (and root `_includes/` if relevant) for existing coverage of the same example. Pay special attention to:

- `_docs/_user_guide/example_library/` (the TAM Example library)
- Other use case libraries (not the Example library—for example `liquid/liquid_use_cases.md`, `brazeai/agents/use_cases.md`, `ecommerce_use_cases.md`, `b2b_use_cases/`)

| Outcome | Action |
|---------|--------|
| Same example already documented | **Skip** — link the existing page in the audit output |
| Partial overlap | Draft only net-new content; cross-link instead of duplicating |
| No overlap | Proceed |

### Audit output format

Write to the chat console (optional local file `output--tam--<ddmmyyyy>.md`):

```markdown
### TAM solution: [title or slug]
- **Source**: [Drive or Confluence URL]
- **Completeness**: [Complete | Incomplete — list missing parts]
- **Category**: [feature/channel/topic for folder grouping]
- **Skip?**: [No | Workaround | Bug | Unreleased | Account-specific | Duplicate]
- **Verified behavior**: [Summary, or "Could not verify — …"]
- **Duplicate check**: [No match | Overlap with `_docs/...` | Duplicate of `_docs/...`]
- **PII scrubbed**: [Yes | Issues found — list]
- **Target doc**: `_docs/_user_guide/example_library/<category>/<slug>.md` (or "SKIP")
- **Suggested change**: [One-line summary if actionable]
```

**Wait gate:** Do not draft until the user confirms the audit (especially skip vs proceed, target path, and any unverified behavior).

---

## Step 2: Generalize with FakeBrandz

Replace **all** customer identifiers with fictional equivalents:

| Replace | With |
|---------|------|
| Company / brand names | FakeBrandz company from [FakeBrandz](https://confluence.atl.braze.com/wiki/spaces/CBO/pages/264165481/FakeBrandz) — pick a name that fits the vertical |
| Product names | Fictional product names consistent with that FakeBrandz company |
| Event names | Generic or fictional event names (for example `product_viewed`, `booking_started`) |
| Custom attributes | Generic names (for example `loyalty_tier`, `last_search_city`) with fictional example values |

**Keep as-is:** Braze product names, official feature names, UI labels, and standard Braze event names where they are part of the platform.

**Screenshots:** When images are needed, prefer [dashboard-06](https://dashboard-06.braze.com/) with a FakeBrandz workspace per the [writing style guide](../../../docs/contributing/style_guide/writing_style_guide.md#example-company-names).

---

## Step 3: Confirm target path and category

Organize files under `_docs/_user_guide/example_library/` by feature or channel category (for example `canvas/`, `email/`, `sms/`, `segments/`). Use lowercase slug filenames (for example `abandoned_cart_retargeting.md`).

- One example per file for v1.
- Add or update a category landing page only when the user asks or when a new category folder is introduced.

Infer `doc_path` from the solution’s primary Braze feature. Search `_docs/` for the canonical feature article to link in **Related resources**.

---

## Step 4: Draft the example article

Follow [braze-docs](../braze-docs/SKILL.md) (`braze-docs:braze-docs`) and [`docs/contributing/style_guide/`](../../../docs/contributing/style_guide/).

Draft all Example library prose per the [Braze style guide](../../../docs/contributing/style_guide/) (voice, headings, links, Liquid formatting). When the style guide conflicts with TAM source wording, follow the style guide.

### Required sections (in order)

1. **About this example** — What problem this solves, who it is for, and which Braze features or channels are involved.
2. **Considerations** — Limits, prerequisites, data requirements, compliance, timing, and when this pattern is not appropriate.
3. **Setup** — Numbered steps to implement the pattern in Braze (Canvas, campaign, segment, integration, etc.).
4. **Related articles** — Links to canonical feature docs in `_docs/` (use `{{site.baseurl}}` link style). Do not duplicate full feature documentation.

### YAML frontmatter (minimum)

```yaml
---
nav_title: [Short nav label]
article_title: [Example title]
page_order: [integer within category]
page_type: reference
description: "[Quoted meta description — what this example covers.]"
---
```

Adjust `page_order` relative to siblings in the same category folder.

### Drafting rules

- Prefer concise bullets and numbered steps over long narrative.
- Do not document workarounds, unreleased features, or account-specific internals.
- Do not copy large blocks from the TAM source; rewrite in Braze docs voice.
- When behavior was verified in reference repos, you may cite repo-relative paths in **local audit notes** only — not in public PR text.

---

## Step 5: Branch, commit, and push

**Branch pattern:** `tam-cursor-<topic>-<ddmmyyyy>`

Example: `tam-cursor-abandoned_cart_retargeting-12062026`

- `<topic>` — short slug, no spaces
- `<ddmmyyyy>` — day, month, year as digits

Branch from **`develop`**. Stage and commit only `_docs/_user_guide/example_library/` (plus root `_includes/` only if required).

---

## Step 6: Wait gate — approval before PR

**Do not open a PR** until the user explicitly approves the draft (audit + generalized markdown).

Offer a short summary: target file, sections added, verification status, and anything still unverified.

---

## Step 7: Open a draft pull request

**REQUIRED SUB-SKILL:** Use [create-pr](../create-pr/SKILL.md) (`braze-docs:create-pr`) for Steps 0–1, 3–4, quality checklist, and anti-patterns. **Override Step 2 only** as follows.

### Step 2 override (tam-solutions)

| Field | Value |
|-------|--------|
| **Title** | `[TAM solutions] <short summary>` |
| **Label** | `tam solutions` — `gh pr edit --add-label "tam solutions"` after create |
| **Assignees** | Longest-prefix match in [`.github/support_analyzer_doc_assignees.csv`](../../support_analyzer_doc_assignees.csv) for paths touched; otherwise `braze-inc/docs-team` |

**Jira:** Parent epic [**BD-7190**](https://jira.atl.braze.com/browse/BD-7190) (Migrate generalized TAM solutions to Example library). After the draft PR exists, create one **Story** under that epic (see **After the PR is created** below).

**Body** — use the create-pr template and include:

```markdown
### Why are you making this change? (required)

<What example this adds to the Operator Example library and for whom.>

### Changes

- [What was added or updated — scope for reviewers, no internal repo paths]

### Verification

- Source verification: [Verified against Braze source code. | Partially verified — … | Not verified — …]
- [Manual checks from create-pr as needed]

### TAM source

- [Confluence or Google Drive URL for the solution this PR generalizes]

### Jira

- Parent epic: [BD-7190](https://jira.atl.braze.com/browse/BD-7190)
- Story: pending (agent fills the new key after create)

### Contributor checklist

<Copy from create-pr Step 2.>
```

If verified against product source, include **Verified against Braze source code.** — do **not** paste `platform/` or SDK paths in the PR description.

### After the PR is created (Jira Story under BD-7190)

Run this only after `gh pr create` succeeds and the user already approved the draft (Step 6). Do not create a Story during audit or for skipped solutions.

Tracker sync and Jira Story create are **independent**. Always match the tracker row and write **PR link** after the draft PR exists, even if you skip Story create (Dedup) or Jira create fails.

1. **Match the tracker row** — Resolve the Example library tracker row from the [TAM solutions to Docs tracker — Example library](https://docs.google.com/spreadsheets/d/1YChWu-L-hPMRo9cVIMfqSYKBQQdNRs4PkFnXPnKk5RE/edit) Google Sheet (spreadsheet ID `1YChWu-L-hPMRo9cVIMfqSYKBQQdNRs4PkFnXPnKk5RE`). Do **not** `WebFetch` the Sheet (SSO). Use Google Sheets MCP `get_sheet_data`.

   1. Read both tabs: **Customer agnostic — Confluence** and **TAM assets — Google Drive**.
   2. Match the TAM source to a row: Google Doc ID in the **Link** cell, or the Confluence page URL. Prefer URL/ID match over title.
   3. Keep the matched tab name, row number, and **Product team** cell for later steps. Do not copy customer names from tracker titles. Do not read the **PM** column unless the user asks.

2. **Write the PR onto the tracker** — Always run this after `gh pr create`, using the row from step 1. Do **not** wait for Story create. Use Google Sheets MCP `update_cell` (Editor access on the Sheet). Do **not** `WebFetch`. Do **not** insert a new row.

   Resolve the cell from **row 1 of the matched tab**. Use the column whose header is exactly **PR link**. Do **not** hardcode column `E` for both tabs — layouts differ:

   | Tab | **PR link** | Adjacent columns (do not write) |
   |-----|-------------|--------------------------------|
   | **Customer agnostic — Confluence** | Column `E` (`E1` is already **PR link**) | `D` = **PM**, `F` = **Status** |
   | **TAM assets — Google Drive** | Column `D` (`D1` is already **PR link**) | `E` = **Status**, `F` = **Note** |

   If row 1 has no **PR link** header, stop and tell the user. Do **not** create `E1` as **PR link** on Drive (that overwrites **Status**). Never write a PR URL into a **Status**, **PM**, **Product team**, or **Note** cell.

   Call `update_cell` with `spreadsheet_id` `1YChWu-L-hPMRo9cVIMfqSYKBQQdNRs4PkFnXPnKk5RE`, the tab name, the resolved cell (for example `E3` on Confluence, `D31` on Drive), and content `[{"text": "<pr url>", "url": "<pr url>"}]`.

   - If **PR link** is empty, write the new PR URL.
   - If it already equals this PR, skip.
   - If it is a **different** URL, do not overwrite; tell the user.
   - If no row matched, Sheets MCP lacks write access, or `update_cell` fails: leave the PR up and tell the user. Do not block the PR or skip later Jira steps.

3. **Dedup Story create** — Skip **only** Story create (step 4) if the PR title or body already has a `BD-####` other than `BD-7190`, or if JQL finds an open child of the epic for this PR:
   `parent = BD-7190 AND description ~ "<github pull request url>"`
   Dedup does **not** skip tracker write (step 2).

4. **Create the Story** — Prefer Rovo `createJiraIssue` (workspace Jira access). Project `BD`, issue type `Story`, parent **BD-7190** (`parent` and epic-link field if required). Priority **P4**. Summary: `TAM solutions - <example title>`.

   **Assignee** — Assign every Story this skill creates to **Lydia Xie** (GitHub `lydia-xie`). Before create, call Rovo `lookupJiraAccountId` with search string `Lydia Xie` and pass the returned account ID as `assignee_account_id` on `createJiraIssue`. If lookup returns more than one person, pick the Braze Docs / Technical Writing match. If lookup or assign fails, still create the Story unassigned and tell the user.

   **Product team:** — Copy the **Product team** cell from the matched tracker row (step 1) as-is, including multiple values separated by `;`. If step 1 found no row, Sheets MCP failed, or that cell is empty, set **Product team:** to `Unknown — confirm in tracker` and tell the user. Still create the Story.

   Description must be markdown in this exact shape (fill each value; do not omit labels). Confirm required BD fields with issue-type metadata if create fails.

   ```markdown
   **GitHub PR:**
   <pull request URL>

   **Docs path for example:**
   `_docs/_user_guide/example_library/<category>/<slug>.md`

   **TAM source:**
   <Google Doc, Drive, or Confluence URL>

   **Product team:**
   <Product team from the matching tracker row>

   **Example description:**
   <one line on what the example covers>
   ```

   Do not put customer names or other PII in **Example description**.

5. **Write back** — If step 4 created a Story, `gh pr edit` the title to `[TAM solutions][BD-####] <short summary>` (child Story key, not `BD-7190`). Set **### Jira** to the Story URL and keep the BD-7190 epic link. Optionally comment on the Story with the PR URL. Skip this step when Dedup skipped create.

6. **Jira failure** — If Jira MCP is unavailable or create fails, leave the PR up, keep the epic link in the PR body, and tell the user the Story was not created. Still complete tracker write (step 2) if it has not run yet. Do not block the PR. Do not use branch names like `jira-BD-####` (reserved for feedback-handler).

---

## Manual workflow summary

| Step | Action | Wait gate |
|------|--------|-----------|
| 1 | Read source; audit completeness, accuracy, PII, duplicates | User confirms audit |
| 2 | Generalize with FakeBrandz | — |
| 3 | Confirm path under `example_library/` | Part of Step 1 confirmation |
| 4 | Draft article with four required sections | User reviews draft |
| 5 | Branch, commit, push | — |
| 6 | — | **User approves before PR** |
| 7 | Open draft PR; create a BD Story under [BD-7190](https://jira.atl.braze.com/browse/BD-7190); write the PR URL to the tracker **PR link** cell; patch PR with the Story key | — |

No CI or scripts for v1 — Cursor-driven only.

---

## Example prompts

Natural-language example requests:

```
Audit and generalize this TAM solution from Confluence: [URL]
```

```
Audit this TAM solution Google Doc and draft an example: https://docs.google.com/document/d/<DOCUMENT_ID>/edit
```

```
Process the abandoned cart Canvas solution from the TAM Assets Drive folder and draft an example under example_library/canvas/.
```

```
Audit only — list completeness and duplicates for solutions in [Drive folder or Confluence space] without drafting.
```

```
Triage solutions from _data/tam_solutions/export_<date>.json — audit completeness by category and list gaps.
```
