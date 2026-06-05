---
name: docs-accessibility
description: >
  Pre-PR accessibility gate for Braze Docs contributors. Run before opening a PR to check for
  accessibility issues. Detects changed file types and routes automatically: architecture changes
  (layouts, JS, CSS, templates, config) are audited against known ADA findings and flagged by
  priority and impact; markdown changes (_docs/, _includes/) run the table accessibility script
  with confidence-gated auto-fixing. Use when asked to "check accessibility", "run a11y audit",
  or before opening any PR that touches site files or documentation.
allowed-tools: Bash(git *), Bash(python3 scripts/check_table_accessibility.py*), Read, Write, StrReplace
---

# Docs Accessibility Audit

## Context
- Branch: !`git branch --show-current`
- Changed files: !`git diff --name-only origin/develop...HEAD 2>/dev/null || git diff --name-only HEAD 2>/dev/null`

## Route Detection

Classify each changed file from the list above:

| Changed file pattern | Route |
|---|---|
| `_layouts/**`, `_includes/**/*.html`, `assets/js/**`, `assets/css/**`, `assets/scss/**`, `_config*.yml`, `*.html` at repo root, `Gemfile`, `package.json`, `.github/workflows/**` | **Architecture** |
| `_docs/**/*.md`, `_includes/**/*.md` | **Markdown** |
| `_lang/**` | Skip silently — localized files are out of scope |

Override with `$ARGUMENTS`:
- Contains "architecture" → Architecture path only
- Contains "markdown" → Markdown path only
- Both file types changed → run Architecture first, then Markdown
- No changed files detected → ask the user to provide file paths

## Paths

**Architecture changed files detected →** Load and follow [workflows/architecture-audit.md](workflows/architecture-audit.md).

**Markdown changed files detected →** Load and follow [workflows/markdown-audit.md](workflows/markdown-audit.md).

## Core Principles

1. **Never auto-fix architecture issues.** Template and JS accessibility changes have non-obvious side effects. Always stop, present findings, and wait for the author to act.

2. **Confidence-gated markdown fixes.** Three tiers: auto-apply (high), stop and ask (medium/low). See the markdown workflow for thresholds.

3. **Priority × impact ordering.** Lead every findings report with the highest-priority item. Use [references/ada-issues-priority.md](references/ada-issues-priority.md) for the full catalog.

4. **Flag root causes, not symptoms.** When a single pattern is responsible for multiple violations (a function, a template block, a shared include), identify the root once — don't list each downstream instance separately.

5. **One stop per path.** Collect all findings for a path before presenting. Don't interrupt mid-audit.

## Gotchas

- **`_lang/` files are always out of scope.** If a changed markdown file lives under `_lang/`, skip it and note the skip at the end of the report.
- **`role="presentation"` is valid on genuine layout tables.** A table with no `<th>` or `<thead>` that is used for side-by-side layout (not data) is correct with `role="presentation"`. Don't flag these as violations.
- **HTML tables: `aria-label` vs `<caption>` is a judgment call.** The script defaults to `aria-label`, but `<caption>` is semantically richer for complex data tables. Always ask before applying an HTML table fix.
- **Don't auto-fix if the nearest heading is missing or generic** ("Overview", "Details", "Notes", "Table"). A vague label is worse than no label — escalate to medium confidence and ask.
- **Dynamic context injection may show a short diff on a new branch.** If the changed files list is empty or incomplete, fall back to asking for paths rather than scanning everything.
