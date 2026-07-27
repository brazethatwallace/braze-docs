---
name: support-analyzer
description: >
  Analyzes Braze support case CSVs to find documentation gaps, triages tickets, verifies behavior against source,
  and drafts docs updates in _docs. Use when analyzing support tickets, running the support analyzer,
  triaging Looker exports on support-analyzer-data, or drafting docs from _data support CSVs.
---

# Drafting docs updates from support tickets

Use support-case exports to find doc gaps, triage by category, verify against product source when possible, then propose **`_docs`** updates. Two paths coexist: **scheduled CI** (digest + optional Phase 2 rules) and **manual Cursor triage** (this rule, full steps below).

## Context
- Current branch: !`git branch --show-current`
- Modified files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only $(git merge-base HEAD $(git rev-parse --verify origin/develop 2>/dev/null || git rev-parse --verify develop 2>/dev/null || echo HEAD~1))..HEAD 2>/dev/null`
- Open PR: !`gh pr view --json number,title,body 2>/dev/null || echo "none"`

---

## How the pieces fit together

| Path | What it does | When to use it |
|------|----------------|----------------|
| **CI — Support analyzer (Looker)** | Looker → CSV on `support-analyzer-data` → digest MD + artifact → optional **Phase 2** draft PRs from [`.github/support_analyzer_phase2_rules.yml`](.github/support_analyzer_phase2_rules.yml) → may close digest PR | Recurring themes; allowlisted inserts; no per-ticket judgment |
| **Manual — this skill (Steps 1–8)** | Full triage, source verification, custom targets, style decisions | Themes outside YAML rules, ambiguous tickets, docs discrepancies |

Before investing manual triage, check whether the theme belongs in **Phase 2 rules** (regex + anchored snippets + optional `verification` / `rg` when a product checkout exists locally, for example `../platform`). Prefer one YAML rule over duplicating automation in ad-hoc analysis.

---

## CI pipeline (Support analyzer / Looker)

Workflow file: [`.github/workflows/export-support-cases-from-looker.yml`](.github/workflows/export-support-cases-from-looker.yml).

**Order of jobs:** `export` → `digest_and_pr` → `phase2_doc_prs` → (optional) `close_digest_pr` → `notify` (Slack).

1. **Export** — Secrets `LOOKER_CLIENT_ID`, `LOOKER_CLIENT_SECRET`. Optional repository **variable** `LOOKER_SUPPORT_CASES_QUERY_ID` (saved Look id; date filters stay in Looker). Pushes `_data/support_cases_latest.csv` to branch **`support-analyzer-data`** (CSV only on that branch; the export script and `_data/pii_patterns.yml` are taken from the workflow ref, usually **`develop`**). Requires `SUPPORT_ANALYZER_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1` in Actions (CSV may contain PII). The export script **redacts embedded credential-like strings** (patterns in `_data/pii_patterns.yml` — for example AWS access key IDs, SendGrid API keys, Twilio account/API key SIDs, GitHub/Slack/Stripe tokens) before write so GitHub **push protection** does not reject the data-branch push. Add or change redaction patterns in that YAML file only; no Python change required. **Local API export:** with `pip install requests pyyaml`, set the same env vars and run `python scripts/export_support_cases_from_looker.py`; optional `SUPPORT_ANALYZER_OUTPUT`, `LOOKER_BASE_URL`, `LOOKER_SUPPORT_CASES_QUERY_ID`.
2. **Digest** — Keyword digest to `.github/support_analyzer_weekly_digest.md`; artifact **`support-analyzer-weekly-digest`**; draft digest PR to **`develop`** with labels **`support analyzer`** and **`do not merge`** (create them in the repo if missing). PR body includes the **stakeholder blurb** plus **do not merge / analysis-only** guidance. **Schedule:** roughly twice weekly (Tuesday and Friday mornings, `America/New_York`) to align with the Looker export’s rolling ~3-day window; see workflow `cron` (see [Schedule events](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)).
3. **Phase 2** — Checks out the **triggering ref** (`github.ref`: default branch on schedule, selected branch on **`workflow_dispatch`**), then runs `scripts/support_analyzer_phase2.py` with **`--strict-anchors`** against the same CSV. May open **draft** PRs (label **`support analyzer`**, base **`develop`**, branch `support-analyzer/phase2-<rule_id>-<YYYY-MM-DD>-<run_id>`). Skips opening another draft for the same rule while an **open** PR already uses that branch prefix. Skips per-file edits when **`fingerprint`**, **`skip_if_contains`**, or **`skip_if_contains_in_files`** already match on **`develop`** (merge Phase 2 PRs with the HTML fingerprint comment, or add skip phrases, to avoid duplicate prose); each PR body starts with the same kind of **stakeholder blurb** as the digest PR. **Assignees:** paths touched by the rule are matched against [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv) (export your spreadsheet to that shape: `page path`, `writer`, `team`, `github username`). Longest path prefix wins; multiple files can yield multiple assignees. The **GitHub Username** cell may contain **comma-separated** logins (for example `lydia-xie,zairro`) to assign more than one person for the same path. If `gh pr create --assignee` fails (invalid username or permissions), the script retries **without** assignees. Artifact **`support-analyzer-phase2-verification`**. Skipped when **`workflow_dispatch`** input **Skip Phase 2** is true (export + digest still run).
4. **Close digest PR** — If a digest PR was opened **and** Phase 2 **succeeded**, that digest PR is closed automatically; the digest remains in the **artifact**.
5. **Slack (`notify`)** — Posts to **#docs_request** via Docs PR Bot when configured (`SLACK_BOT_TOKEN`, `SLACK_DOCS_REQUEST_CHANNEL` channel ID; optional fallback `SLACK_DEPLOY_NOTIFY_CHANNEL`). **Failures** in export, digest, Phase 2, or close-digest post `:x:` with the workflow run link. **Success with Phase 2 PRs** lists each draft PR and **@mentions** assignees (Slack member lookup by GitHub username, with optional `SUPPORT_ANALYZER_GITHUB_TO_SLACK` JSON override). Digest-only runs (no matching Phase 2 rules) post a short success note when a digest PR was opened.

**Phase 2 and product source:** The Looker workflow does **not** clone `Appboy/platform` (or other product repos). Per-rule **`verification`** in `.github/support_analyzer_phase2_rules.yml` runs **ripgrep** only when the referenced root (for example `platform/`) exists—for example on a developer machine with [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`). In GitHub Actions those checks are typically skipped. Use **`verification.required: true`** only in environments where that checkout is always present.

**Manual / local CSV:** Export from the [Support Cases dashboard](https://braze.looker.com/x/4git0QPwJ9xjVtdBphbkPE) or Snowflake; save under `_data/` (or path you pass in the prompt). Default Look export window is defined in Looker (e.g. recent resolved cases), not in this repo.

---

## PII and public output

- Treat CSV and message bodies as **sensitive**. Do not paste raw case text, customer names, or emails into **public** PRs, issues, or external posts.
- For **public** PR descriptions, never list internal paths under `platform` or SDK repos. Use **Verified against Braze source code.** per [reference-repos](../reference-repos/SKILL.md). Internal paths may appear in **Cursor chat / local notes** or **workflow artifacts**, not customer-facing copy.

---

## CSV schema

| Column | Description |
|--------|-------------|
| `Support Cases Email Message Case ID` | Primary case identifier (e.g. `500VP00000nQrMKYA0`) |
| `Support Cases Closed or Resolved Date` | Timestamp of resolution |
| `Support Cases Email Message Sent Date` | Timestamp of message |
| `Support Cases Description` | Original support question |
| `Support Cases Email Message Text Body Cleaned` | Cleaned message for analysis |

For CI, the canonical file on branch **`support-analyzer-data`** is **`_data/support_cases_latest.csv`**.

---

## Step 1: Triage and categorize

For each **unique Case ID**, decide if docs work is needed:

| Category | Criteria | Action |
|----------|----------|--------|
| **Docs Gap** | Customer could not find existing info; answer exists but is unclear | Update existing docs |
| **Docs Discrepancy** | Docs and source code contradict each other | Update existing docs |
| **New Feature** | Question about recently released or undocumented feature | Draft new section |
| **Edge Case** | Unusual but valid use case not covered | Add FAQ or troubleshooting |
| **Support-Only** | Account-specific, requires Braze internal access, or one-off config | Skip (no docs change) |
| **Bug/Product** | Issue requiring code fix, not docs | Skip (escalate to eng) |

> **Never document workarounds or bugs.** Documentation must describe how the product works — or is intended to work — not temporary workarounds for issues that will be (or should be) fixed. If a ticket's resolution relies on a workaround for a product defect, categorize it as **Bug/Product** and skip it.

---

## Step 2: Per-ticket analysis

For each **actionable** ticket:

1. **Extract Q&A** — Distill the core question and resolution from the message thread.
2. **Verify** — **REQUIRED SUB-SKILL:** Use [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) to cross-check behavior against main product source (local workspace: `../platform` when using the sibling-clone layout). Do not rely on support text or docs alone. If you verified behavior against source, say so in your analysis; if you could not verify, say that explicitly. For **public** PR descriptions and customer-facing copy, never paste internal `platform` or SDK repository paths—use **Verified against Braze source code.** per [reference-repos](../reference-repos/SKILL.md).
3. **Identify target** — Which existing `_docs` page to update (or flag a new location).
4. **Record case IDs** — For traceability in PR bodies (Salesforce links only; see Step 7).

**Never publish internal source file paths in PR descriptions** (see Step 7).

### Output format (per ticket)

Write to `output--<ddmmyyyy>.md` and the chat console:

```markdown
### Case: [CASE_ID]
- **Category**: [Docs Gap | Docs Discrepancy | New Feature | Edge Case]
- **Question**: [One-sentence summary]
- **Resolution**: [Brief answer]
- **Verified behavior**: [Complete answer]
- **Target Doc**: `_docs/_user_guide/path/to/file.md` (or "NEW: suggested_location")
- **Suggested Change**: [What to add or update]
```

---

## Step 3: Consolidate and prioritize

1. **Merge duplicates** — Group tickets with the same or overlapping issue.
2. **Prioritize** by verification strength, frequency, impact, effort.
3. **Batch by doc** — Group edits that touch the same file.
4. **Maintain sources** — List Case IDs you used.
5. **Confirm with the user** — Get explicit approval before Step 4 (drafting).

---

## Step 4: Draft updates

Before creating branches, confirm the user wants to proceed.

1. **Prefer refining existing prose** over new alerts or FAQ entries unless the content cannot fit naturally.
2. Follow [Braze docs style guides](docs/contributing/style_guide.md).
3. Keep additions concise (bullets, tables, code samples where appropriate).
4. When documenting a product limitation or enhancement ask, use `_includes/product_feedback_cta.md` per [Product feedback CTAs](docs/contributing/style_guide/product_feedback_ctas.md). Do not add ad hoc `portal.braze.com` or legacy portal links.

---

## Step 5: Branch naming

For each distinct change (often one branch per doc file or coherent theme):

**Pattern:** `SA-Cursor-<short-topic>-<ddmmyyyy>`

Example: `SA-Cursor-liquid_use_cases-02122026`

Use a short **topic** slug (no spaces); date is **day month year** as digits.

---

## Step 6: Commit and push

Stage and commit only relevant **`_docs`** (and linked includes if needed) with a clear message.

---

## Step 7: Open the pull request

**REQUIRED SUB-SKILL:** Use [create-pr](../create-pr/SKILL.md) (`braze-docs:create-pr`) for Steps 0–1, 3–4, quality checklist, and anti-patterns. **Override Step 2 only** as follows.

### Step 2 override (support-analyzer)

| Field | Value |
|-------|--------|
| **Title** | `[SA] <short summary>` (example: `[SA] Add FAQ entry about machine opens vs other opens`) |
| **Label** | `support analyzer` — `gh pr edit --add-label "support analyzer"` after create |

**Body** — use the create-pr template and add these sections:

```markdown
### Why are you making this change? (required)

<Reader outcome in 1–2 sentences.>

### Related PRs, issues, or features (optional)

- [BD-1234](https://jira.atl.braze.com/browse/BD-1234) (if applicable)

### Changes

- [Scope for reviewers — no internal repo paths]
- If verified against product source: **Verified against Braze source code.** — do **not** paste `platform/` or SDK paths.

### Cases

- https://braze.lightning.force.com/lightning/r/Case/<case ID>/view (case ID only — no customer names or other PII from ticket prose)

### Verification

<Manual checks only — see create-pr.>

### Contributor checklist

<Copy from create-pr Step 2.>
```

### Reviewers (Step 4 follow-up)

If [`.github/CODEOWNERS`](.github/CODEOWNERS) lists owners for the paths you changed, assign them. Otherwise assign **`braze-inc/docs-team`** via `gh pr edit --add-reviewer`.

---

## Step 8: Prune stale support CSVs (optional)

After manual triage is complete and any related digest or Phase 2 PRs have merged, remove **dated local exports** you no longer need. The CI canonical file is always **`_data/support_cases_latest.csv`** on branch **`support-analyzer-data`** — never prune that path.

Local exports from `scripts/export_support_cases_from_looker.py` default to `_data/support_cases_<YYYYMMDD>.csv` when `SUPPORT_ANALYZER_OUTPUT` is unset. Prune only snapshots you have finished analyzing.

From the repo root:

```bash
python3 scripts/prune_data_files.py --dry-run --group support-csv
python3 scripts/prune_data_files.py --confirm --group support-csv
```

[`scripts/prune_data_files.py`](../../../scripts/prune_data_files.py) only deletes files under `_data/` and refuses live site config, sitemaps, and `support_cases_latest.csv`.

---

## Source layout (verification)

| Context | Product source |
|---------|----------------|
| Local Cursor + [reference-repos](../reference-repos/SKILL.md) | `../platform` (sibling clone) |
| GitHub Actions Phase 2 | No product-repo checkout; optional `verification` is skipped unless you change the workflow |

---

## Example prompts

Natural-language example requests:

```
Analyze the CSV in _data/ and draft docs updates.
Focus on [product area] if applicable.
```

```
After reviewing the latest weekly digest, triage cases that are not covered by .github/support_analyzer_phase2_rules.yml and propose manual doc updates.
```
