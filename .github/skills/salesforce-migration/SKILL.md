---
name: salesforce-migration
description: >
  Salesforce Knowledge → Braze public docs (Epic BD-6308): Phase 1 triage, Phase 2 PRs,
  `kb_articles.csv` / `sf_kb_articles.csv` backlog. Use for @salesforce-migration or Salesforce KB migration.
---

# Salesforce Knowledge → Braze Docs (Epic BD-6308)

Invoke with **`@salesforce-migration`**. Human workflow and gates: this file. **Verification:** [`reference-repos`](../reference-repos/SKILL.md). **Prose:** [`docs/contributing/style_guide/`](../../../docs/contributing/style_guide.md).

**Inputs:** `_data/kb_articles.csv` (+ optional `_data/sf_kb_articles.csv`) and `scripts/salesforce-analyzer/*.py`.

---

## Data files

| File | Role |
|------|------|
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | Backlog — `article_id`, `suggested_change`, `doc_path`, `conflict_resolution`, etc. |
| [`_data/kb_articles_actioned.md`](_data/kb_articles_actioned.md) | **Generated** Phase 2 queue (PR batches by `doc_path`) |
| [`_data/kb_articles_skipped.md`](_data/kb_articles_skipped.md) | **Generated** skipped rows + reasons |
| [`_data/sf_kb_articles.csv`](_data/sf_kb_articles.csv) | Optional full `Resolution` text (`encoding='latin-1'`) when `suggested_change` is not enough |

---

## Scripts

Phase 1 is the only routine that **writes** `kb_articles_actioned.md`, `kb_articles_skipped.md`, and may edit `kb_articles.csv`. Phase 2 automation **reads** those outputs; `sf_kb_sync_tracker.py` may trim the CSV when you run it explicitly.

```bash
# Phase 1 — from repo root
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --infer-doc-paths --no-prune
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune

# Optional: remove article_ids already named in open/merged `salesforce migration` PRs, then refresh Phase 1 markdown
python3 scripts/salesforce-analyzer/sf_kb_sync_tracker.py [--dry-run]

# Phase 2 bulk runner — docs-only PRs; does not write _data/
python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py [--limit N] [--doc-path '_docs/...']

# Phase 2 — Jira task under BD-6308 (needs JIRA_USER_EMAIL + JIRA_API_TOKEN)
python3 scripts/salesforce-analyzer/sf_kb_jira_ticket.py --pr-url '...' --pr-title '[BD-####](SF) ...' --doc-path '_docs/...'

# Retrofit PR titles for existing epic children
python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py [--dry-run]
```

| Script | Purpose |
|--------|---------|
| `generate_kb_phase1_outputs.py` | Phase 1 gates, path inference, writes actioned/skipped markdown; optional CSV prune / `doc_path` inference (flags above) |
| `sf_kb_sync_tracker.py` | Drop `article_id`s found in migration PR bodies from `kb_articles.csv`; regenerates actioned/skipped via Phase 1 script |
| `sf_kb_phase2_run_batches.py` | Bulk Phase 2 PR opener (`gh` + optional Jira); commits `_docs/` / `_includes/` only |
| `sf_kb_jira_ticket.py` | Create BD Task linked to epic BD-6308 |
| `sf_kb_sync_epic_pr_titles.py` | Rename PRs to `[BD-####](SF) …` format |

---

## Phase 1: Triage

1. Update [`_data/kb_articles.csv`](_data/kb_articles.csv) if needed.
2. Run Phase 1: `--infer-doc-paths --no-prune` first when paths are missing or stale, then `--no-prune` to refresh markdown only.
3. Work from **`kb_articles_actioned.md` section 1** (one PR per primary `_docs` file).
4. For skipped rows with `overlap` or `codebase confirms knowledge` but no path: fix `doc_path` in the CSV (or rely on `--infer-doc-paths`), re-run.

**Skip (no public docs):** workarounds/bugs, INTERNAL titles, support-only/account-specific content, sensitive internal notes.

**`inconclusive` rows:** stay actionable if they resolve to a `doc_path`; **verify in reference repos before drafting** in Phase 2.

**Do not target** `_docs/_help/help_articles/` — use `_user_guide/`, `_developer_guide/`, or `_api/` instead.

### Resolve `doc_path` (when empty or stale)

1. Prefer a real on-disk `_docs/...` path in the CSV.
2. Use `--infer-doc-paths` (generator remaps + routing); extend maps in `generate_kb_phase1_outputs.py` only after you confirm targets.
3. If still empty, search `_docs/` by title, error strings, or feature names (FAQ/troubleshooting first).
4. Use SF `Environment` / product area as a hint for which neighborhood of `_docs/` to search.

---

## Phase 2: Draft + PR

**Scope:** one **PR batch** from section 1 of `kb_articles_actioned.md` — rows sharing one primary `doc_path`, **one `_docs` file per PR** (plus `_includes/` only if required).

1. Read backlog rows; optional `sf_kb_articles.csv` `Resolution` by title; redact PII.
2. **Verify behavior** in reference repos before drafting (`inconclusive` rows especially). Prefer source over SF text when they conflict.
3. Draft concise updates per style guide; refine existing prose over new alerts/FAQs.
4. Branch off `develop`: `sf-cursor-<doc-slug>-<YYYYMMDD>` (suggested slug appears in actioned file).
5. Open PR to `develop`, label **`salesforce migration`**, title **`[BD-####](SF) short theme`**. Create the Jira task with `sf_kb_jira_ticket.py` when needed.
6. **Assignee:** longest-prefix match in [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv). `sf_kb_phase2_run_batches.py` passes `--assignee` only when that resolves to a GitHub username; otherwise add reviewers manually.
7. **PR scope:** `_docs/` / `_includes/` only. **Do not** commit `_data/kb_articles*` in migration PRs.

### PR body (minimum)

- **Product vertical** (routing only)
- **Summary** — reviewer-facing overview of what changed
- **Changes** — files touched; repo-relative verification paths (e.g. `platform/shared_code/...`)
- **Salesforce Knowledge sources** — bullet per `article_id` + title

Use `build_sf_kb_github_pr_body()` in `sf_kb_jira_ticket.py` for section order. For hand-edited PRs, pass explicit `summary_bullets`; bulk runner derives bullets from CSV `suggested_change`.

### Jira (BD-6308)

One **Task** per PR under epic [**BD-6308**](https://jira.atl.braze.com/browse/BD-6308): GitHub PR link, article list, product vertical. Summary: `Salesforce KB batch - <theme>`.

---

## Example prompts

```
@salesforce-migration Run Phase 1 (--infer-doc-paths) and summarize the backlog.
```

```
@salesforce-migration Run Phase 2 for the PR batch `_docs/_user_guide/channels/push/troubleshooting.md`.
```

```
@salesforce-migration Run Phase 2 for the next doc-file batch in kb_articles_actioned.md section 1.
```
