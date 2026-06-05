---
name: check-accessibility
description: >
  Pre-PR accessibility gate for Braze Docs contributors. Run before opening a PR to check for
  accessibility issues. Detects changed file types and routes automatically: architecture changes
  (layouts, JS, CSS, templates, config) are audited against known ADA findings and flagged by
  priority and impact; markdown changes (_docs/, _includes/) run the table accessibility script
  with confidence-gated auto-fixing. Use when asked to "check accessibility", "run a11y audit",
  or before opening any PR that touches site files or documentation.
allowed-tools: Bash(git *), Bash(python3 scripts/check_table_accessibility.py*), Read, Write, StrReplace, Grep
---

# Docs Accessibility Audit

## Context
- Branch: !`git branch --show-current`
- Changed files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only $(git merge-base HEAD $(git rev-parse --verify origin/develop 2>/dev/null || git rev-parse --verify develop 2>/dev/null || echo HEAD~1))..HEAD 2>/dev/null`

## Route Detection

Classify each changed file from the list above:

| Changed file pattern | Route |
|---|---|
| `_layouts/**`, `_includes/**/*.html`, `assets/js/**`, `assets/css/**`, `assets/scss/**`, `_config*.yml`, `*.html` at repo root, `Gemfile`, `package.json`, `.github/workflows/**` | **Architecture** |
| `_docs/**/*.md`, `_includes/**/*.md`, `_includes/**/*.html` | **Markdown** (table checks) |
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

3. **Priority × impact ordering.** Lead every findings report with the highest-priority item. Use [references/ada-issues-priority.md](references/ada-issues-priority.md) for the full catalog.

4. **Flag root causes, not symptoms.** When a single pattern is responsible for multiple violations (a function, a template block, a shared include), identify the root once — don't list each downstream instance separately.

5. **One stop per path.** See each workflow for when to collect and present.

## Examples

**Typical invocation (auto-detect):**
`/docs-accessibility` on a branch with one changed CSS file and two changed markdown files → runs Architecture path first (CSS), then Markdown path (two `.md` files).

**Force a single path:**
`/docs-accessibility architecture` → Architecture path only, even if markdown files also changed.

**Non-interactive (CI or automation):**
`/docs-accessibility ci` → runs both paths, auto-fixes high-confidence markdown violations, skips medium/low with no prompts, exits with summary report.

**Expected routing output (no violations):**
> Architecture accessibility audit complete — all 1 changed file(s) are clean.
> No table accessibility violations found in the 2 changed markdown file(s).
