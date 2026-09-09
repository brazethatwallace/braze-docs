---
name: sdk-sync
description: >
  Syncs SDK repository guides into braze-docs using scripts/sync_sdk_repository_guides.py
  and the sync-sdk-repository-guides workflow. Use when repository guide pages under
  _docs/_developer_guide/sdk_repository_guides/ drift from upstream SDK READMEs, or when
  asked to run or validate a sync.
allowed-tools: Bash(python3 scripts/sync_sdk_repository_guides.py*), Read, Glob
---

# SDK repository guides sync

Use this workflow to sync SDK repository guides in docs with the mapped upstream SDK READMEs.

## Source of truth

Treat these documents as canonical and keep this skill aligned with them:

- [`scripts/sdk_repository_guides_sync_guide.md`](../../../scripts/sdk_repository_guides_sync_guide.md)
- [`scripts/sdk_repository_guides_sync_internal.md`](../../../scripts/sdk_repository_guides_sync_internal.md)

If this skill and those docs conflict, follow the script docs and update this skill in the same PR.

## When to use this skill

Use this skill when:

- A contributor asks to run or verify SDK repository guides sync.
- The CI workflow `.github/workflows/sync-sdk-repository-guides.yml` opens/updates sync changes and you need to review or reproduce them locally.
- Pages under `_docs/_developer_guide/sdk_repository_guides/` appear out of sync with SDK repository READMEs.
- You are changing sync mappings or post-processing rules in `scripts/sync_sdk_repository_guides.py` and need to validate output.

## Before you start

1. Confirm you are at the `braze-docs` repo root.
2. Read both source-of-truth docs listed above.
3. Avoid hand-editing generated regions between:
   - `<!-- BEGIN GENERATED README CONTENT -->`
   - `<!-- END GENERATED README CONTENT -->`
4. Decide scope:
   - Full sync: all mapped repos.
   - Targeted sync: `--repo <slug>` for one or more repo guides.

## Run the sync

From repo root:

```bash
python3 scripts/sync_sdk_repository_guides.py --write
python3 scripts/sync_sdk_repository_guides.py --check
```

Targeted (example):

```bash
python3 scripts/sync_sdk_repository_guides.py --write --repo web
python3 scripts/sync_sdk_repository_guides.py --check --repo web
```

## What to verify on completion

1. `--write` exits successfully and only updates expected files.
2. `--check` exits cleanly after `--write` (idempotent output).
3. Changes are limited to intended repository guide pages (and any deliberate script/workflow edits).
4. Sample changed pages still render expected alert and code-fence conversions.
5. No manual edits were made inside generated README regions.

For deeper verification criteria (post-processing behavior, workflow behavior, and operational guardrails), use the two source-of-truth docs directly.
