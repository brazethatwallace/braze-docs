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

**REQUIRED SUB-SKILL:** For prose and structure use [braze-docs](../braze-docs/SKILL.md) (`braze-docs:braze-docs`). **REQUIRED SUB-SKILL:** For product verification use [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`). Open [`braze-workspace.code-workspace`](../../../braze-workspace.code-workspace) so `platform` and SDK repos are sibling folders when verifying behavior.

**Output location:** `_docs/_user_guide/example_library/` (English canonical only; do not edit `_lang/`).

---

## Source material

TAM solutions may live in either location. Use whichever the user provides, or search both when auditing inventory.

| Source | Location |
|--------|----------|
| **Google Drive** | [TAM Assets folder](https://drive.google.com/drive/folders/1APchTnf3UWN6MGpGkeBfryGMn73LBUM0) |
| **Confluence** | TAM solution pages (user supplies URL), or Atlassian MCP when available |
| **Local JSON export** | `_data/tam_solutions/export_<YYYYMMDD>.json` from [`scripts/tam-solutions/export_drive_solutions.py`](../../../scripts/tam-solutions/export_drive_solutions.py) |

### Google Drive export (optional)

Cursor cannot read private Google Docs URLs directly. For bulk inventory or offline triage, run the Drive export script locally:

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

**Reading sources (fallback order):** Local JSON export → user paste → Confluence (MCP) → Drive URL (often fails without auth). If all fail, ask the user to paste or export before continuing.

**Traceability:** Record the exact source URL (Drive `web_view_link`, Confluence page URL, or export path) for the PR body. Never paste raw internal content that contains customer PII into public PR descriptions.

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

For each solution the user assigns:

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

**Jira:** A parent epic or ticket is **not yet created**. When it exists, link each PR to that parent. Until then, omit Jira links or note "Parent epic pending."

**Body** — use the create-pr template and include:

```markdown
### Why are you making this change? (required)

<What example this adds to the Operator Example library and for whom.>

## Changes

- [What was added or updated — scope for reviewers, no internal repo paths]

## Verification

- [Verified against Braze source code. | Partially verified — … | Not verified — …]

## TAM source

- [Confluence or Google Drive URL for the solution this PR generalizes]

## Jira

- Parent epic: pending

### Contributor checklist

<Copy from create-pr Step 2.>
```

If verified against product source, include **Verified against Braze source code.** — do **not** paste `platform/` or SDK paths in the PR description.

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
| 7 | Open draft PR with label and TAM source link | — |

No CI or scripts for v1 — Cursor-driven only.

---

## Example prompts

Natural-language example requests:

```
Audit and generalize this TAM solution from Confluence: [URL]
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
