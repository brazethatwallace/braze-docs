---
name: salesforce-migration
description: >
  Salesforce KB → Braze docs (Epic BD-7051): Phase 1 script-driven triage, Phase 2 PRs + Jira,
  Phase 3 CSV write-back. `kb_articles.csv` / optional `sf_kb_articles.csv`.
---

# Salesforce Knowledge → Braze Docs (Epic BD-7051)

**Verify:** **REQUIRED SUB-SKILL:** Use [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) when confirming product behavior. · **Prose:** [`docs/contributing/style_guide/`](../../../docs/contributing/style_guide.md)

## Context
- Current branch: !`git branch --show-current`
- Modified files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only $(git merge-base HEAD $(git rev-parse --verify origin/develop 2>/dev/null || git rev-parse --verify develop 2>/dev/null || echo HEAD~1))..HEAD 2>/dev/null`
- Open PR: !`gh pr view --json number,title,body 2>/dev/null || echo "none"`

---

## Data files

| File | Role |
|------|------|
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | Backlog — pass raw to Cursor; do not pre-process or strip columns. **`suggested_change`** = strong draft user docs, not shorthand-only triage (Phase 1) |
| [`_data/kb_articles_actioned.md`](_data/kb_articles_actioned.md) | **Generated** — Phase 2 queue by `doc_path` |
| [`_data/kb_articles_skipped.md`](_data/kb_articles_skipped.md) | **Generated** — skipped rows + reasons |
| [`_data/sf_kb_articles.csv`](_data/sf_kb_articles.csv) | Optional — full SF `Resolution` (`encoding='latin-1'`) |

> **CSV note:** `kb_articles.csv` may have many columns and long cell content. Pass it to Cursor raw — the script handles all column parsing and triage logic. Do not strip columns or summarize content before running Phase 1.

---

## Local Jira credentials

Copy [`.jira.env.example`](../../../.jira.env.example) to `.jira.env` and run `source scripts/jira_env.sh` before Jira scripts. **Never commit `.jira.env`** — it is gitignored and blocked by the pre-commit hook.

## Scripts

Phase 1 **writes** the two markdown files and may edit the CSV. Phase 2 **reads** them. `sf_kb_sync_tracker.py` trims the CSV when run explicitly.

```bash
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --infer-doc-paths --no-prune
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune

python3 scripts/salesforce-analyzer/sf_kb_sync_tracker.py [--dry-run]

python3 scripts/salesforce-analyzer/sf_kb_overlap_scan.py [--doc-path '_docs/...']

python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --verify-only --doc-path '_docs/...' [--pull-reference-repos] [--write-verification]
python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --prepare [--limit N] [--doc-path '_docs/...'] [--verification-file '.sf-kb-verification-<slug>.md'] [--pull-reference-repos]
python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --open-pr --doc-path '_docs/...' --verification-file '.sf-kb-verification-<slug>.md'

python3 scripts/salesforce-analyzer/sf_kb_jira_ticket.py --pr-url '...' --pr-title '[BD-####](SF) ...' --doc-path '_docs/...'   # needs JIRA_USER_EMAIL + JIRA_API_TOKEN

python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py [--dry-run]

python3 scripts/prune_data_files.py --dry-run [--group support-csv|kb-generated|all]
python3 scripts/prune_data_files.py --confirm [--group support-csv|kb-generated|all]
```

| Script | Purpose |
|--------|---------|
| `generate_kb_phase1_outputs.py` | Phase 1 gates, path inference, actioned/skipped markdown; `--infer-doc-paths` / prune flags; overlap scan in actioned output |
| `sf_kb_overlap_scan.py` | Overlap scan before Phase 2: open/draft/merged PRs, `article_id` claims, `develop` marker/commits, remote `sf-cursor-*` branches |
| `sf_kb_sync_tracker.py` | PR-labeled `article_id`s → drop from CSV → rerun Phase 1 markdown |
| `prune_data_files.py` | Remove stale `_data/` artifacts (`--group kb-generated` after Phase 3 write-back) |
| `sf_kb_phase2_run_batches.py` | **Verify → prepare → polish → PR:** resolves CSV `codebase_evidence` against sibling repos, `--verify-only`, blocks `--prepare` until paths verify, `--open-pr` for draft PR |
| `sf_kb_jira_ticket.py` | BD Task under epic BD-7051 |
| `sf_kb_sync_epic_pr_titles.py` | PR titles → `[BD-####](SF) …` |

---

## Phase 1: Script-driven triage

> **The script is the sole triage authority.** `generate_kb_phase1_outputs.py` applies all classification gates. Your job is to run the script and fix `doc_path` values — not to re-evaluate whether individual rows should be actionable or skipped.

### Skip gates (script decides — do not override)

If the script marks something actionable, accept it and proceed to Phase 2 without second-guessing.

| Gate | Skip condition |
|------|----------------|
| `implementation_status` | First line is `archived` or `actioned`, or any value other than empty, `not started`, `to be actioned`, or `delta ka` |
| `target` | Value is `inconclusive` |
| `conflict_resolution` | Contains `human review`, `no source`, `codebase inconclusive`, or `inconclusive —` |
| `suggested_change` | Empty, whitespace, or first line starts with an author-brief phrase (for example `add to`, `ensure`, `consider adding`, `document`, `update`, `optional`, `might`, `may`, `consider reviewing`, `review`, `tbd`, `unclear`, `needs investigation`, `needs sme`, `flag for`) — see `sf_kb_suggested_change.py` |
| `_docs/` paths | All extracted paths are under `_docs/_help/help_articles/` |
| `target` + paths | `target` is `knowledge_article` and no `_docs/` path found in any field |
| Path resolution | No on-disk `_docs/...` target found after path extraction, IA remaps, scripted inference, and best-fit placement |

### What you fix (only this)

- `doc_path` is blank or stale but you can identify the correct current path → update the CSV field, then re-run.
- A path failed because it's under an old IA layout (e.g. `engagement_tools/`, `message_building_by_channel/`) → extend `PATH_INFERENCE_EXACT` or `PATH_INFERENCE_PREFIXES` in `generate_kb_phase1_outputs.py` after confirming the mapping.
- A row landed in skipped with reason "no locatable on-disk target" but has a clear `suggested_change` and a valid topic → search `_docs/` for the best-fit page, set `doc_path`, re-run.

**Never manually move rows between the actioned and skipped files.**

### Steps

1. Edit [`_data/kb_articles.csv`](_data/kb_articles.csv) only to fix `doc_path` values.
2. Run `--infer-doc-paths --no-prune` when `doc_path` is missing or wrong, then `--no-prune` to refresh markdown. Omit `--no-prune` to also prune `archived`/`actioned` rows from the CSV. Extend path maps in `generate_kb_phase1_outputs.py` only after you confirm targets; otherwise search `_docs/` (FAQ/troubleshooting first).
3. Inspect `kb_articles_skipped.md` — address only rows where fixing `doc_path` would recover them. Do not override the skip on any other gate.
4. Inspect `kb_articles_actioned.md` section 1 — one PR per primary `_docs` file.

**`inconclusive`:** still actionable with a `doc_path` — **verify in reference repos** before Phase 2.

**Paths:** not `_docs/_help/help_articles/` — use `_user_guide/`, `_developer_guide/`, or `_api/`.

**`suggested_change`:** Write as **ship-ready public prose** — customer-facing headings (`###` for FAQ entries), full sentences, concrete facts, limits, and steps. Avoid author briefs (`Add to…`, `Ensure…`, `Consider adding…`) that only tell an editor what to do; those are skipped in Phase 1 and must not ship in PRs.

---

## Phase 2: Verify → prepare → polish → PR

**Scope:** section 1 of `kb_articles_actioned.md` — same `doc_path` → one PR, one primary `_docs` file (`_includes/` only if needed).

**Do not draft or open a PR until reference repos are verified** for `inconclusive` articles. The Phase 2 runner blocks `--prepare` until verification proof is recorded; `--open-pr` still requires ship-ready prose (no phase-2 markers).

### Step A — Verify (reference repos)

1. Read backlog; optional `sf_kb_articles.csv`; redact PII.
2. **Verify** in reference repos (`inconclusive` especially). Prefer platform/source over SF copy.
3. Run the script to resolve CSV `codebase_evidence` paths against sibling clones and block early:

```bash
python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --verify-only \
  --doc-path '_docs/.../faq.md' \
  --pull-reference-repos
```

The runner checks that cited `platform/...` (and SDK) files exist under sibling repos opened via [`braze-workspace.code-workspace`](../../../braze-workspace.code-workspace), runs keyword search in those files, and auto-generates verification bullets. Use `--write-verification` to save `.sf-kb-verification-<slug>.md`.

Exits non-zero when `inconclusive` articles lack resolvable evidence or cited reference files are missing. Re-run after fixing paths or adding manual bullets to the verification file.

### Step B — Prepare (script)

```bash
python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --prepare \
  --doc-path '_docs/.../faq.md' \
  --verification-file '.sf-kb-verification-faqs.md' \
  --pull-reference-repos
```

Requires reference verification to pass **before** bulk-inserting CSV draft text. Creates `sf-cursor-<slug>-<YYYYMMDD>`, appends `suggested_change` between markers, commits **locally only**.

### Step C — Polish (agent / contributor)

**Replace the marker block** with integrated, ship-ready user docs:
- FAQ batches: `###` question headings with direct answers (not `Ensure…` / `Add to…` briefs).
- Match [`docs/contributing/style_guide/`](../../../docs/contributing/style_guide/) — tone, Liquid, heading levels, links, redundancy.
- Remove `<!-- sf-kb-phase2-batch -->` / `<!-- /sf-kb-phase2-batch -->` entirely.

### Step D — Publish (script + create-pr)

```bash
python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py --open-pr \
  --doc-path '_docs/.../faq.md' \
  --verification-file '.sf-kb-verification-faqs.md'
```

Run on the prepared `sf-cursor-*` branch after polish. The script validates ship-ready prose, re-checks verification proof, pushes, and opens a **draft** PR (then runs Jira when credentials are set).

**Overlap scan (required before prepare):** Run `sf_kb_overlap_scan.py` or `sf_kb_phase2_run_batches.py` (which runs the scan automatically). A batch is **blocked** when any of the following apply:

- An **open** or **draft** PR (any label) already edits the target `_docs/` / `_includes/` file
- The batch `article_id`(s) already appear in an open or merged PR body
- `develop` already contains the Phase 2 batch marker (`<!-- sf-kb-phase2-batch -->`) in that file
- A remote `sf-cursor-<slug>-*` branch exists for the doc path

**Warnings** (non-blocking unless you pass `--ignore-warnings` to the Phase 2 runner): recent merged PRs that touched the same file, or recent `SF KB` commits on `develop` for that path.

4. **Open PR** — **REQUIRED SUB-SKILL:** Use [create-pr](../create-pr/SKILL.md) (`braze-docs:create-pr`) for Steps 0–1, 3–4, quality checklist, and anti-patterns. **Override Step 2 only** as follows. Or use `sf_kb_phase2_run_batches.py --open-pr` after polish. Then run Jira: `sf_kb_jira_ticket.py` if the runner did not create the ticket.
5. Assignee and product vertical: [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv) (longest path) → GitHub `--assignee` on the PR (`GitHub Username`), **Product vertical** in PR/Jira from `Team`, Jira assignee via [`.github/github_to_jira_assignees.json`](.github/github_to_jira_assignees.json). Skips `docs-team` and unmapped users unless `JIRA_ASSIGNEE_ACCOUNT_ID` is set.
6. Commits: `_docs/` / `_includes/` only — **no** `_data/kb_articles*` in migration PRs.

#### Step 2 override (salesforce-migration)

| Field | Value |
|-------|--------|
| **Title** | `[BD-####](SF) <short summary>` |
| **Label** | `salesforce migration` — `gh pr edit --add-label "salesforce migration"` after create |
| **Base** | `develop` |
| **Draft** | Yes — `gh pr create --draft` (per [create-pr](../create-pr/SKILL.md); mark ready after checks pass) |

**PR body:** Prefer `build_sf_kb_github_pr_body()` in `sf_kb_jira_ticket.py` for product vertical (`Team` from assignees CSV), summary, changes, **`## Verification`** (reference-repo proof), and `article_id` sources. Merge that output into the create-pr template sections (**Why**, **Approach**, **Verification**, **Contributor checklist**).

**Verification proof (required before prepare):** The runner resolves `codebase_evidence` `platform/...` paths under sibling clones, keyword-searches those files, and auto-generates bullets. Use `--pull-reference-repos` before verify/prepare. Manual notes go in `.sf-kb-verification-<slug>.md` (`--write-verification` or `--verification-file`).

**Jira:** one Task per PR under [**BD-7051**](https://jira.atl.braze.com/browse/BD-7051) — PR link, articles, vertical, assignee (same writer as the PR when mapped). Summary: `Salesforce KB batch - <theme>`.

---

## Phase 3: CSV write-back (after all PRs)

After Phase 2 is complete for a batch, write the PR and Jira ticket IDs back to `kb_articles.csv`. This lets you export the updated spreadsheet to Google Sheets so stakeholders can locate both actioned and unactionable articles in one place.

### Steps

1. Add columns `jira_ticket_id` and `pr_url` to `kb_articles.csv` if they don't exist yet.
2. For each row that received a PR in this batch, populate:
   - `jira_ticket_id` — the BD ticket key (e.g. `BD-1234`) from `sf_kb_jira_ticket.py` output
   - `pr_url` — the full GitHub PR URL (e.g. `https://github.com/braze-inc/braze-docs/pull/1234`)
3. Set `implementation_status` = `actioned` on those rows.
4. Save the updated `kb_articles.csv`.

**After saving:** Export `kb_articles.csv` to a new sheet in the source Google Spreadsheet. Rows with `jira_ticket_id` and `pr_url` are the actioned articles; rows without are unactionable or pending.

> **Do not run Phase 1 prune** until after write-back is complete and the CSV has been exported — the prune step drops `actioned` rows, removing the write-back data before it can be shared.

### Prune Phase 1 markdown (after write-back)

After Phase 3 write-back is saved and `kb_articles.csv` has been exported to the stakeholder spreadsheet, remove the generated queue files so `_data/` does not accumulate stale triage output. Phase 1 regenerates these files on the next run.

```bash
python3 scripts/prune_data_files.py --dry-run --group kb-generated
python3 scripts/prune_data_files.py --confirm --group kb-generated
```

Run this **after** Phase 2 PRs for the batch have merged and write-back is complete — not while `kb_articles_actioned.md` still lists open work. [`scripts/prune_data_files.py`](../../../scripts/prune_data_files.py) only deletes files under `_data/`.

---

## Example prompts

Natural-language example requests:

```
Run Phase 1 (--infer-doc-paths) and summarize the backlog.
```

```
Run Phase 2 for `_docs/_user_guide/channels/push/troubleshooting.md`.
```

```
Run Phase 2 verify-only for `_docs/_user_guide/channels/push/troubleshooting.md` before preparing.
```

```
Phase 2 is complete. Write back PR URLs and Jira ticket IDs to kb_articles.csv.
```
