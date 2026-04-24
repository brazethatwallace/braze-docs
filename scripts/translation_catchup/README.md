# Translation catch-up (post–March 31, 2026)

Use this when you need to backfill auto-translation after automation was paused.

## Baseline

- **Cutoff:** end of day **2026-03-31 UTC** on `develop`.
- **Default base commit** (last commit strictly before that moment on `origin/develop` when this tooling was added):

  `3e2a7ea3cac0f973b2cf6a901954739e285c512e`

Recompute if your cutoff differs (timezone, date, or branch moved):

```bash
git fetch origin develop
git rev-list -n 1 --before="2026-03-31 23:59:59 UTC" origin/develop
```

## Option A — One workflow run (no path list size limit)

Manual `workflow_dispatch` **must** set `since_commit` and/or `files` (empty runs are rejected).

In GitHub Actions, run **Auto-translate** with:

| Input | Value |
|--------|--------|
| `since_commit` | `3e2a7ea3cac0f973b2cf6a901954739e285c512e` (or your recomputed SHA) |
| `skip_orphan_cleanup` | `true` for intermediate catch-up runs; `false` on the **final** run to delete stale `_lang/` mirrors |

This diffs that commit to the current ref and translates every changed English `.md` under `_docs/` and `_includes/`. `since_commit` takes precedence over `files` if both are set.

**CLI example:**

```bash
gh workflow run auto-translate.yml --repo braze-inc/braze-docs --ref develop \
  -f since_commit=3e2a7ea3cac0f973b2cf6a901954739e285c512e \
  -f skip_orphan_cleanup=true
```

For ~1000+ files this is one very large job (API + Jekyll). Prefer **Option B** unless you have raised timeouts and accept a single huge PR.

## Option B — Batched runs (smaller PRs, same `since_commit`)

1. Generate lists and batch files (writes to `generated/`, gitignored):

   ```bash
   ./scripts/translation_catchup/generate_batches.py
   ```

   Options: `--base SHA`, `--head SHA|BRANCH`, `--max-per-batch 40`, `--no-find-renames`.

2. Dispatch one batch (paths joined for the `files` input):

   ```bash
   ./scripts/translation_catchup/dispatch_batch.sh scripts/translation_catchup/generated/batches/phase_a_includes_batch_001.txt
   ```

   Set `REPO` (default `braze-inc/braze-docs`), `REF` (default `develop`), `SKIP_ORPHAN` (`true`/`false`, default `true` for catch-up).

3. Merge each PR to `develop` before the next batch when order matters (e.g. `_includes` before heavy `_user_guide` batches).

4. On the **last** batch (or a dedicated run), set `skip_orphan_cleanup` to **false** so `clean_orphaned_translations.py` runs once `_lang/` mirrors the new English IA.

## Phase order (IA / `_user_guide`)

Generated batches follow:

1. **Phase A** — `_includes/*.md` (shared snippets first).
2. **Phase B** — `_docs/_user_guide/...` grouped by first subdirectory under `_user_guide/` (e.g. `message_building`, `engagement_tools`), chunked to `--max-per-batch`.
3. **Phase C** — remaining `_docs/` markdown.

See `generated/batches/MANIFEST.txt` after generation for the ordered list of batch files.
