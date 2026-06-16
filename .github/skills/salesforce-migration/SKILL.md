---
name: salesforce-migration
description: >
  Migrates Salesforce Knowledge gaps into Braze public docs (Epic BD-6308). Use for Phase 1 triage,
  Phase 2 drafting and PRs, kb_articles.csv backlog work, sf_kb_articles.csv Resolution lookups,
  or when the user mentions @salesforce-migration or Salesforce KB migration.
---

# Salesforce Knowledge → Braze Docs (Epic BD-6308)

Migrate Salesforce Knowledge gaps into public docs. Invoke with **`@salesforce-migration`**.

**Dependencies:** `_data/` files below + `scripts/salesforce-analyzer/`. For behavior verification use [`reference-repos`](../reference-repos/SKILL.md). For prose style use `docs/contributing/style_guide/`.

---

## Data files

| File | Role |
|------|------|
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | Backlog — `article_id`, `suggested_change`, `doc_path`, `conflict_resolution`, etc. |
| [`_data/kb_articles_actioned.md`](_data/kb_articles_actioned.md) | **Generated** Phase 2 queue (PR batches by `doc_path`) |
| [`_data/kb_articles_skipped.md`](_data/kb_articles_skipped.md) | **Generated** skipped rows + reasons |
| [`_data/kb_epic_bd6308.txt`](_data/kb_epic_bd6308.txt) | In-flight / completed `article_id` values (excluded from queue) |
| [`_data/sf_kb_articles.csv`](_data/sf_kb_articles.csv) | Optional full `Resolution` text (`encoding='latin-1'`) when `suggested_change` is not enough |

**Phase 1 only:** `generate_kb_phase1_outputs.py` writes `kb_articles_actioned.md`, `kb_articles_skipped.md`, and may update `kb_articles.csv`. Phase 2 and PR automation **read** these files but do not modify them.

---

## Scripts

```bash
# Phase 1 — from repo root (only step that updates _data/kb_articles*)
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --infer-doc-paths --no-prune
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune

# Phase 2 bulk runner — docs-only PRs; does not write _data/
python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py [--limit N] [--doc-path '_docs/...']

# Phase 2 — Jira task under BD-6308 (needs JIRA_USER_EMAIL + JIRA_API_TOKEN)
python3 scripts/salesforce-analyzer/sf_kb_jira_ticket.py --pr-url '...' --pr-title '[BD-####](SF) ...' --doc-path '_docs/...'

# Retrofit PR titles for existing epic children
python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py [--dry-run]
```

| Script | Purpose |
|--------|---------|
| `generate_kb_phase1_outputs.py` | Gates, path inference, writes actioned/skipped markdown (and CSV when infer/prune flags apply) |
| `sf_kb_phase2_run_batches.py` | Bulk Phase 2 PR opener (reads `_data/`; docs-only commits) |
| `sf_kb_jira_ticket.py` | Create BD Task linked to epic BD-6308 |
| `sf_kb_sync_epic_pr_titles.py` | Rename PRs to `[BD-####](SF) …` format |

---

## Phase 1: Triage

1. Update [`_data/kb_articles.csv`](_data/kb_articles.csv) if needed.
2. Run both commands above (`--infer-doc-paths` then refresh).
3. Work from **`kb_articles_actioned.md` section 1** (one PR per primary `_docs` file).
4. For skipped rows with `overlap` or `codebase confirms knowledge` but no path: infer `doc_path`, update CSV, re-run.

**Skip (no public docs):** workarounds/bugs, INTERNAL titles, support-only/account-specific content, sensitive internal notes.

**`inconclusive` rows:** actionable when they resolve to a `doc_path`; **must verify in reference repos before drafting** in Phase 2.

**Do not target** `_docs/_help/help_articles/` — find the equivalent `_user_guide/`, `_developer_guide/`, or `_api/` page.

### Resolve `doc_path` (when empty or stale)

1. CSV `doc_path` if file exists on disk.
2. `_docs/...` strings in `suggested_change` / `codebase_evidence` (apply IA remaps in the generator).
3. Search `_docs/` by title, error strings, feature names — prefer FAQ/troubleshooting over new pages.
4. Map SF `Environment` to doc neighborhood (Email, Canvas, Currents, SDK, etc.).

---

## Phase 2: Draft + PR

**Scope:** one **PR batch** from section 1 of `kb_articles_actioned.md` — all articles sharing one primary `doc_path`, **one file edited per PR** (plus `_includes/` only if required).

1. Read backlog rows; optional `sf_kb_articles.csv` `Resolution` by title; redact PII.
2. **Verify behavior** in reference repos before drafting (`inconclusive` rows especially). Prefer source over SF text when they conflict.
3. Draft concise updates per style guide; refine existing prose over new alerts/FAQs.
4. Branch off `develop`: `sf-cursor-<doc-slug>-<YYYYMMDD>` (see suggested slug in actioned file).
5. Open PR to `develop`, label **`salesforce migration`**, title **`[BD-####](SF) short theme`** (create Jira task first or via `sf_kb_jira_ticket.py`).
6. Assignee: longest-prefix match in [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv), else `@braze-inc/docs-team`.
7. **PR scope:** edit `_docs/` (and `_includes/` only when required). **Do not** modify or commit `_data/kb_articles*` or `kb_epic_bd6308.txt` during Phase 2.

### PR body (minimum)

- **Product vertical** (routing only)
- **Summary** — reviewer-facing overview (bullets or a short paragraph) of what changed in the PR
- **Changes** — files touched; repo-relative verification paths (e.g. `platform/shared_code/...`)
- **Salesforce Knowledge sources** — bullet per `article_id` + title

Use `build_sf_kb_github_pr_body()` in `sf_kb_jira_ticket.py` for the standard section order. Pass explicit `summary_bullets` when hand-editing docs (bulk append PRs derive summary bullets from CSV `suggested_change`).

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
