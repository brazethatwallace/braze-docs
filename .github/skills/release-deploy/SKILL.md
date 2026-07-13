---
name: release-deploy
description: >
  Generate the deploy-PR text used in monthly release notes by running
  scripts/generate_releases_deploy.py. Lists merged `deploy` PRs from the last
  v.* release tag through today, with contributor PRs nested underneath. Use when
  preparing release notes, generating the deploy list, or when asked for the
  "deploy text" for a release.
allowed-tools: Bash(python3 scripts/generate_releases_deploy.py*), Bash(git fetch*), Bash(git tag*), Read
---

# Release deploy text generation

Monthly release notes list every `deploy` pull request merged since the previous release, with each deploy PR's merged contributor PRs nested underneath. This skill generates that list so you can paste it into the release notes draft — no need to reconstruct it by hand from GitHub.

The generator is [`scripts/generate_releases_deploy.py`](../../../scripts/generate_releases_deploy.py). Human-facing docs: [`docs/contributing/bdocs.md`](../../../docs/contributing/bdocs.md) (the `release` section).

> **Not the same as `./bdocs deploy`.** `deploy` builds the body of a single nightly *deployment* PR (`develop` → `main`). This workflow builds the *release notes* deploy list spanning many deployments since the last release tag.

> **Deprecated:** `./bdocs release` is a thin wrapper around the script and prints a deprecation notice. Always prefer `python3 scripts/generate_releases_deploy.py`.

## When to generate deploy text

Generate the deploy text when you are **drafting a monthly release notes article** ([`_docs/_releases`](../../../_docs/_releases)) and need the list of what shipped since the previous release. Concretely, run this:

- **After** the previous release has been published and tagged with a `v.*` tag (the tag is the window's start anchor).
- **When** you begin assembling the new release notes and need the deploy/contributor PR list to summarize.
- **Before** you write the summary prose — the generated file is your raw source material, not the final copy.

The default window is: 00:00:00 UTC on the calendar day **after** the latest `v.*` tag's commit → 23:59:59 UTC **today**.

## Prerequisites

- `gh` CLI installed and authenticated for `braze-inc/braze-docs` (the script checks for `gh` and calls `gh pr list` / `gh pr view`).
- `git` in a braze-docs clone. The script auto-detects the repo root, fetches `origin` tags by default, then resolves the latest `v.*` tag.

## Command to run

Run from the repo root (or any subdirectory in the clone):

**Default — day after latest `v.*` tag through today:**

```bash
python3 scripts/generate_releases_deploy.py
```

**Custom output path (same auto window):**

```bash
python3 scripts/generate_releases_deploy.py scripts/temp/my_deploy_list.md
```

**Explicit date range** (`<start> <end> <month-title> [output.md]`, dates `YYYY-MM-DD`, inclusive UTC):

```bash
python3 scripts/generate_releases_deploy.py 2026-03-06 2026-04-02 "April 2026"
```

### Flag-based invocation

Use flags when you need finer control:

```bash
# Explicit window
python3 scripts/generate_releases_deploy.py \
  --merged-search "2026-03-06..2026-04-02" \
  --window-start "2026-03-06T00:00:00Z" \
  --window-end "2026-04-02T23:59:59Z" \
  --month-title "April 2026" \
  --output scripts/temp/releases_deploy_2026-03-06_to_2026-04-02.md

# Skip tag fetch (e.g. offline or tags already current)
python3 scripts/generate_releases_deploy.py --no-fetch-tags
```

Key arguments:

| Argument | Purpose |
|----------|---------|
| `--git-repo-root` | Override repo used to resolve the latest `v.*` tag (default: auto-detect). |
| `--auto-from-last-release-tag` | Explicitly request auto window (default when no explicit window is passed). |
| `--merged-search` | `gh` merged-date range, e.g. `2026-03-06..2026-04-02`. |
| `--window-start` / `--window-end` | Inclusive ISO UTC bounds for a second, exact filter on merge time. |
| `--month-title` | Heading label, e.g. `"April 2026"` (defaults to the end date's month/year in auto mode). |
| `--output` / `-o` | Output `.md` path (see below). |
| `--no-fetch-tags` | Skip `git fetch origin --tags` before resolving the latest `v.*` tag. |

## Where the output goes

By default the file is written to:

```
scripts/temp/releases_deploy_<start>_to_<end>.md
```

`scripts/temp/` is a scratch location — the file is your source for drafting, not something you commit. Copy the relevant lines into the release notes article.

On success the script prints (to stderr / stdout):

```
Merged deploy PRs: 2026-04-03..2026-04-13 (2026-04-03T00:00:00Z → 2026-04-13T23:59:59Z)
Wrote /path/to/braze-docs/scripts/temp/releases_deploy_2026-04-03_to_2026-04-13.md (45123 bytes)
```

The generated Markdown looks like:

````markdown
# Deploy PRs for April 2026 (2026-03-06T00:00:00Z → 2026-04-02T23:59:59Z)

*Merged contributor PRs only: … Each sub-bullet links `[#NNNN](url) - subject` when the PR number is known.*

## Nightly Deploy — April 02, 2026
- https://github.com/braze-inc/braze-docs/pull/12955 - Nightly Deploy — April 02, 2026
  - [#12947](https://github.com/braze-inc/braze-docs/pull/12947) - [BD-5977] Replace link in alert
  - [#12637](https://github.com/braze-inc/braze-docs/pull/12637) - Release notes - April 2026
````

## Verify the output before using it

Before you use the generated list in release notes, confirm:

1. **The window is right.** The printed `Merged deploy PRs: <range>` and the heading dates should start the day *after* the previous release tag and end today (or match your explicit range). If tags were stale, rerun without `--no-fetch-tags` or run `git fetch origin main --tags` first.
2. **The file was actually written.** Look for the `Wrote … (N bytes)` line and a non-trivial byte count. A tiny file usually means an empty window or an auth problem.
3. **Deploy PRs are present.** Each `##` section is a `deploy`-labeled PR. If there are none, either nothing shipped in the window or the `deploy` label / `gh` auth is off — spot-check on GitHub.
4. **Contributor bullets look complete.** Sub-bullets are the merged contributor PRs. A section showing *"(no squash/merge-PR commits …)"* means the script couldn't extract contributor PRs from that deploy PR — verify that PR manually on GitHub before trusting the list.
5. **Suggestion/sync churn is excluded.** The script filters out "Apply suggestion", Copilot, and `develop`/`main` sync-merge commits by design; make sure nothing you *need* was legitimately excluded.

If any check fails, fix the input (tags, `gh` auth, date range) and rerun — don't hand-edit the generated file to paper over a bad window.
