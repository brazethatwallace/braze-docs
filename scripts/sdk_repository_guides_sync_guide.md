# Repository guides sync guide

This document explains the end-to-end behavior for syncing SDK repository README files into docs pages.

## What this system does

The Repository guides feature mirrors public README files from Braze SDK GitHub repositories into docs pages under:

- `_docs/_developer_guide/sdk_repository_guides/`

Each mirrored page contains:

1. A generated README section between markers:
   - `<!-- BEGIN GENERATED README CONTENT -->`
   - `<!-- END GENERATED README CONTENT -->`
2. One docs-owned footer line at the end of the page with a clickable repository URL:
   - `For repository details and sample projects, see [<repo URL>](<repo URL>).`

The generated content is the source README content with render-safe URL normalization and excludes the large top Braze logo block.

## Source repositories and target pages

| SDK repo | Branch | Source README | Target page |
|---|---|---|---|
| `braze-web-sdk` | `master` | `https://raw.githubusercontent.com/braze-inc/braze-web-sdk/master/README.md` | `_docs/_developer_guide/sdk_repository_guides/web.md` |
| `braze-android-sdk` | `master` | `https://raw.githubusercontent.com/braze-inc/braze-android-sdk/master/README.md` | `_docs/_developer_guide/sdk_repository_guides/android.md` |
| `braze-swift-sdk` | `main` | `https://raw.githubusercontent.com/braze-inc/braze-swift-sdk/main/README.md` | `_docs/_developer_guide/sdk_repository_guides/swift.md` |
| `braze-javascript-sdk` | `main` | `https://raw.githubusercontent.com/braze-inc/braze-javascript-sdk/main/README.md` | `_docs/_developer_guide/sdk_repository_guides/javascript.md` |
| `braze-cordova-sdk` | `master` | `https://raw.githubusercontent.com/braze-inc/braze-cordova-sdk/master/README.md` | `_docs/_developer_guide/sdk_repository_guides/cordova.md` |
| `braze-flutter-sdk` | `master` | `https://raw.githubusercontent.com/braze-inc/braze-flutter-sdk/master/README.md` | `_docs/_developer_guide/sdk_repository_guides/flutter.md` |
| `braze-react-native-sdk` | `master` | `https://raw.githubusercontent.com/braze-inc/braze-react-native-sdk/master/README.md` | `_docs/_developer_guide/sdk_repository_guides/react_native.md` |
| `braze-roku-sdk` | `main` | `https://raw.githubusercontent.com/braze-inc/braze-roku-sdk/main/README.md` | `_docs/_developer_guide/sdk_repository_guides/roku.md` |
| `braze-unity-sdk` | `master` | `https://raw.githubusercontent.com/braze-inc/braze-unity-sdk/master/README.md` | `_docs/_developer_guide/sdk_repository_guides/unity.md` |
| `braze-xamarin-sdk` | `master` | `https://raw.githubusercontent.com/braze-inc/braze-xamarin-sdk/master/README.md` | `_docs/_developer_guide/sdk_repository_guides/xamarin.md` |

## Script behavior

Script path:

- `scripts/sync_sdk_repository_guides.py`

### What the script does

For each mapped repository:

1. Fetches `README.md` from `raw.githubusercontent.com`.
2. Normalizes line endings.
3. Normalizes relative URLs for docs rendering:
   - Relative markdown links (`[text](relative/path)`) -> GitHub `blob` URLs.
   - Relative markdown images (`![alt](relative/path)`) -> GitHub `raw` URLs.
   - Relative HTML `href`/`src` in inline HTML tags -> normalized absolute GitHub URLs.
4. Removes large top Braze logo blocks so docs pages render cleanly.
5. Builds deterministic page output:
   - Front matter.
   - Generated content markers.
   - One repo footer line with a clickable URL.
6. Compares expected output with current file.
7. In `--write` mode, writes only changed files.
8. In `--check` mode, exits non-zero when any page is out of sync.

### CLI usage

From repo root:

```bash
python3 scripts/sync_sdk_repository_guides.py --check
python3 scripts/sync_sdk_repository_guides.py --write
```

### Exit behavior

- `--check`:
  - Exit `0` when all pages are in sync.
  - Exit `1` when any page is out of sync.
- `--write`:
  - Exit `0` after updating changed pages.

## Automation behavior

Workflow path:

- `.github/workflows/sync-sdk-repository-guides.yml`

### Where to look for what

- **Executable automation configuration** lives in:
  - `.github/workflows/sync-sdk-repository-guides.yml`
- **Human-readable implementation and testing guidance** lives in:
  - `scripts/sdk_repository_guides_sync_guide.md`

Use the workflow file when you need to change trigger cadence, permissions, PR behavior, or runtime steps. Use this guide when you need to understand system behavior, run manual checks, or onboard maintainers.

### Triggers

- Weekly cron schedule.
- Manual trigger via `workflow_dispatch`.

### What workflow does

1. Checks out `braze-docs`.
2. Sets up Python.
3. Runs:
   - `python scripts/sync_sdk_repository_guides.py --write`
4. Uses `peter-evans/create-pull-request` to open/update an automated PR when changes exist.
5. PR scopes to:
   - `_docs/_developer_guide/sdk_repository_guides/`

If there are no content changes, no PR is created.

### Automatic vs manual execution

- **Automatic weekly mode:** Runs on cron with no human action required.
- **Manual mode:** Runs only when someone triggers `workflow_dispatch` in GitHub Actions or runs the script locally.
- **Impact between modes:** A manual run does not disable scheduled runs. Scheduled runs continue as configured. If a manual run already synced and merged the same updates, the next scheduled run usually no-ops because there is no diff.

## How to test

## Local testing (script only)

1. Verify clean baseline:
   ```bash
   python3 scripts/sync_sdk_repository_guides.py --check
   ```
2. Force regeneration:
   ```bash
   python3 scripts/sync_sdk_repository_guides.py --write
   ```
3. Confirm idempotency:
   ```bash
   python3 scripts/sync_sdk_repository_guides.py --check
   ```
4. Inspect changed files:
   ```bash
   git status --short
   ```

## Workflow testing (manual run)

1. Go to GitHub Actions.
2. Run `Sync SDK repository guides` via **Run workflow** (`workflow_dispatch`).
3. Validate expected behavior:
   - If upstream README content changed, automation opens/updates PR.
   - If nothing changed, no PR is created.

## Manual script runs vs scheduled automation

Running the script manually does **not** disable, break, or otherwise impact the scheduled automation.

Behavior details:

- Manual local run only affects your local branch/files until you commit and push.
- Scheduled workflow always runs on its own schedule in GitHub Actions regardless of local runs.
- If you manually commit synced updates before the scheduled run, the scheduled run will likely find no diff and open no PR.
- If you manually edit generated pages away from upstream README state, next manual or scheduled sync will revert them back to generated content.

## Operational notes and guardrails

- Treat the README as source-of-truth for generated regions.
- Avoid manual edits inside generated marker blocks.
- If repository default branches change, update mapping in `sync_sdk_repository_guides.py`.
- If a repo moves or is renamed, update both source URL mapping and footer repo URL.
- If markdown rendering issues appear, update URL normalization rules in the script and re-run `--write`.
