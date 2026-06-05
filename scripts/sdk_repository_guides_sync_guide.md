# Repository guides sync guide

This guide explains the production behavior for syncing SDK repository README files into docs pages.

For full operational details and maintenance procedures, refer to `scripts/sdk_repository_guides_sync_internal.md`.

## What this system does

The repository guides feature mirrors public README files from Braze SDK repositories into docs pages under:

- `_docs/_developer_guide/sdk_repository_guides/`

Each target page includes:

1. Front matter owned by docs.
2. A generated content region between:
   - `<!-- BEGIN GENERATED README CONTENT -->`
   - `<!-- END GENERATED README CONTENT -->`
3. A docs-owned repository footer link.

The generated README content is post-processed before being committed so it follows Braze docs formatting and style standards.

## Source repositories and target pages

The source mapping is defined in `scripts/sync_sdk_repository_guides.py` in `REPO_GUIDES`.

## Script behavior

Script path:

- `scripts/sync_sdk_repository_guides.py`

### Post-processing pipeline

For every source README, the script applies deterministic post-processing:

1. Removes `<script>` and `<style>` blocks to keep generated pages performant and safe.
2. Converts Setext headings to ATX headings for stable markdown rendering.
3. Removes top logo/badge noise from the README title region.
4. Normalizes relative links and image references to absolute GitHub URLs.
5. Converts README alert formats into Braze liquid alerts:
   - GitHub alerts (`> [!NOTE]`, `> [!WARNING]`, etc.)
   - Colon alerts (`::: note` style)
   - Blockquote-prefix alerts (`> **Note:** ...`)
   - Warning-style markdown headings (for example, `#### ⚠ ...`) into warning alerts.
6. Normalizes code fences and ensures fence language tags are present.
7. Removes README table-of-contents blocks to avoid duplicate navigation in docs.
8. Removes leading README preamble text before the first section heading so pages begin with clean article sections.
9. Injects a standardized intro section (`About the Braze <SDK>`) for consistent page starts across repository guide pages.
10. Adds markdown table accessibility labels automatically (`{: ... aria-label="..." }`) using the nearest section heading.
11. Removes the README top-level H1 to avoid duplicate page titles in docs templates.
12. Collapses excessive whitespace.

### CLI usage

From repo root:

```bash
python3 scripts/sync_sdk_repository_guides.py --check
python3 scripts/sync_sdk_repository_guides.py --write
python3 scripts/sync_sdk_repository_guides.py --write --repo web --repo android
```

### Exit behavior

- `--check`
  - Exit `0` when all pages are in sync.
  - Exit `1` when one or more pages are out of sync.
- `--write`
  - Exit `0` after writing changed pages.
  - Exit `2` on runtime failure.

## Automation behavior

Workflow path:

- `.github/workflows/sync-sdk-repository-guides.yml`

### Triggers

- Weekly schedule (every Sunday at 07:00 UTC).
- Manual trigger (`workflow_dispatch`).

### What workflow does

1. Runs sync in write mode.
2. Opens or updates one automation PR against `develop`.
3. Attempts to auto-approve and enable auto-merge (best effort).

If there are no generated changes, no PR is created.

## Testing checklist

1. Run `python3 scripts/sync_sdk_repository_guides.py --write`.
2. Run `python3 scripts/sync_sdk_repository_guides.py --check`.
3. Confirm the second command exits cleanly (idempotent output).
4. Review changed files under `_docs/_developer_guide/sdk_repository_guides/`.
5. Validate converted alert syntax and code fences in sampled pages.
