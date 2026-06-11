---
name: check-accessibility
description: >
  Pre-PR WCAG 2.2 Level AA gate for Braze Docs contributors. Run before opening a PR to check
  documentation and architecture changes against the documentation-relevant subset of WCAG 2.2 AA.
  Detects changed file types and routes automatically: architecture changes (layouts, JS, CSS,
  templates) are audited against WCAG 2.2 AA criteria; markdown and include changes run two
  accessibility scripts (table names + content checks) with confidence-gated auto-fixing. Use when
  asked to "check accessibility", "run a11y", "WCAG check", or before any PR touching site files or
  documentation.
allowed-tools: Bash(git *), Bash(python3 scripts/check_table_accessibility.py*), Bash(python3 scripts/check_content_accessibility.py*), Read, Write, StrReplace, Grep
---

# Content Accessibility Audit (WCAG 2.2 AA)

## Context
- Branch: !`git branch --show-current`
- Changed files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only $(git merge-base HEAD $(git rev-parse --verify origin/develop 2>/dev/null || git rev-parse --verify develop 2>/dev/null || echo HEAD~1))..HEAD 2>/dev/null`

## Route Detection

Classify each changed file from the list above:

| Changed file pattern | Route |
|---|---|
| `_layouts/**`, `_includes/**/*.html`, `assets/js/**`, `assets/css/**`, `assets/scss/**`, `_config*.yml`, `*.html` at repo root, `Gemfile`, `package.json`, `.github/workflows/**` | **Architecture** |
| `_docs/**/*.md`, `_includes/**/*.md`, `_includes/**/*.html` | **Content** (table + content checks) |
| `_lang/**` | Skip silently — localized files are out of scope |

Note: `_includes/**/*.html` matches both routes — run Architecture first, then also run the Markdown (table) path on those same files.

Override with `$ARGUMENTS`:
- Contains "architecture" → Architecture path only
- Contains "markdown" → Markdown path only
- Contains "ci" or "headless" → non-interactive mode: skip all prompts, treat medium/low confidence markdown violations as "skip", proceed to final summary
- Both file types changed → run Architecture first, then Markdown
- No changed files detected → ask the user to provide file paths; classify the provided paths using the route table above and proceed (do not re-run `git diff`)

## Paths

**Architecture changed files detected →** Load and follow [workflows/architecture-audit.md](workflows/architecture-audit.md).

**Markdown changed files detected →** Load and follow [workflows/markdown-audit.md](workflows/markdown-audit.md).

## Core Principles

1. **No auto-fixes on architecture.** See the architecture workflow — it owns this constraint.

2. **Confidence-gated markdown fixes.** Three tiers: auto-apply (high), stop and ask (medium/low). See the markdown workflow for thresholds.

3. **Criterion × impact ordering.** Lead every findings report with the highest-impact criterion. Use [references/wcag-aa-docs-criteria.md](references/wcag-aa-docs-criteria.md) for the full catalog.

4. **Flag root causes, not symptoms.** When a single pattern is responsible for multiple violations (a function, a template block, a shared include), identify the root once — don't list each downstream instance separately.

5. **One stop per path.** See each workflow for when to collect and present.

## Enforcement

This skill runs interactively inside Cursor. Two additional enforcement layers run the same
Python scripts automatically:

| Layer | How it works | Install |
|---|---|---|
| **Pre-commit hook** (local) | Runs on every `git commit`. Auto-fixes high-confidence table violations, re-stages fixed files, blocks the commit if any violations remain. | `bash scripts/install_hooks.sh` |
| **CI status check** (GitHub) | Runs on every PR (`check-content-accessibility.yml`). Strict mode — fails immediately on any violation and posts exact `file:line` guidance as a PR comment. | Enabled by default; set as a required status check in branch protection settings. |

**Skip the local hook in an emergency:** `SKIP_A11Y=1 git commit`

## Examples

**Typical invocation (auto-detect):**
`/check-accessibility` on a branch with one changed CSS file and two changed markdown files → runs Architecture path first (CSS), then Content path (two `.md` files).

**Force a single path:**
`/check-accessibility architecture` → Architecture path only, even if markdown files also changed.

**Non-interactive (CI or automation):**
`/check-accessibility ci` → runs both paths, auto-fixes high-confidence violations, skips medium/low with no prompts, exits with summary report.

**Expected routing output (no violations):**
> Architecture accessibility audit complete — no issues found. All 1 changed file(s) are clean.
> Content accessibility audit complete — no violations found in the 2 changed markdown file(s).
