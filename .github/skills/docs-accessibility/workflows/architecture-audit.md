# Workflow: Architecture Accessibility Audit

## Required Reading
Load [references/ada-issues-priority.md](../references/ada-issues-priority.md) before proceeding.

---

## Overview

Architecture changes touch templates, JS, CSS, and config — places where a single pattern can affect every page on the site. This workflow reads the changed files, checks for the known ADA issue patterns, and presents findings ordered by priority × impact. **Nothing is auto-fixed.**

---

## Step 1: Inventory the changed architecture files

Categorize each changed architecture file by type. This determines which checks to run.

| File type | Checks to run |
|-----------|--------------|
| `assets/css/**`, `assets/scss/**` | P1-A (focus rings), P2-A (color contrast) |
| `_layouts/**`, root `*.html` | P1-B (skip nav), P1-C (ARIA), P3-A (iframes), P3-C (heading semantics), P4-A (meta tags) |
| `_includes/**/*.html` | P1-C (ARIA), P2-B (live regions), P2-C (new-tab links), P3-A (iframes), P3-B (input labels), P3-C (heading semantics) |
| `assets/js/**` | P2-B (live regions), P1-C (ARIA via JS DOM manipulation) |
| `_config*.yml` | No accessibility checks — skip |
| `.github/workflows/**` | No accessibility checks — skip |
| `Gemfile`, `package.json` | No accessibility checks — skip |

Run only the checks relevant to the file types that changed. Don't run every check on every file.

---

## Step 2: Read each changed file and check for patterns

For each changed file, read the file content and look for the patterns listed below. Record every finding with:
- **File and line number** (or range)
- **Priority ID** (P1-A through P4-A)
- **What was found** — quote the exact pattern that triggered the finding
- **Why it matters** — one sentence from the priority catalog
- **Fix direction** — what the author should do (from the catalog)

### CSS / SCSS checks (P1-A, P2-A)

**P1-A — Focus rings:**
- Look for `:focus` blocks that set `outline: none` or `outline: 0`
- Check whether a `:focus-visible` alternative exists in the same selector scope
- Flag if `outline: none` / `outline: 0` appears without a paired `:focus-visible` rule providing a visible replacement (border, box-shadow, or background change)
- Also flag if `*:focus { outline: none }` or similar broad resets appear anywhere

**P2-A — Color contrast:**
- Look for new color variables or hardcoded hex/rgb values being introduced or changed on text-bearing elements
- Flag any new `color:` or `background-color:` pairs that you cannot confirm meet 4.5:1 (normal text) or 3:1 (large text)
- Do not compute ratios — flag the pair and ask the author to verify with a contrast checker
- Specific hotspots: alert/callout components, code block syntax highlighting, badge/tag elements, link colors

### Layout / HTML template checks (P1-B, P1-C, P3-A, P3-C, P4-A)

**P1-B — Skip navigation:**
- Scan `_layouts/default.html` (or whatever the primary layout file is) for a skip link near the top of `<body>`
- Expected pattern: `<a href="#main-content"` (or equivalent) as one of the first focusable elements
- Also check that an element with `id="main-content"` exists in the same template
- Flag if the skip link is missing, if the target ID is missing, or if the skip link is hidden with `display: none` (visually hidden with `position: absolute; left: -9999px` is acceptable)

**P1-C — ARIA validity:**
- Scan for `role=` attribute changes
- Verify that the role value is a valid ARIA landmark, widget, or document structure role
- Flag `role="presentation"` or `role="none"` on elements that have focusable descendants (links, buttons, inputs inside the element)
- Flag duplicate `id` attributes — `aria-labelledby` breaks silently when IDs collide

**P3-A — iframe titles:**
- Grep for `<iframe` tags
- Flag any `<iframe` without a `title="[non-empty string]"` attribute

**P3-C — Heading semantics:**
- Look for elements styled visually as headings but using `<div>`, `<p>`, or `<span>` instead of `<h2>`–`<h6>`
- Look for heading level skips: an `<h4>` appearing after an `<h2>` with no `<h3>` between them
- Alert `_includes/` files are a common hotspot — check that alert headings use semantic elements

**P4-A — Obsolete meta tags:**
- Scan `<head>` for `<meta http-equiv="X-UA-Compatible">` or other IE-era directives
- This is the only finding that is safe to auto-remove — but still present it for confirmation, don't do it silently

### JavaScript checks (P2-B, P1-C)

**P2-B — Live regions:**
- Look for code that updates DOM content in response to user interaction (search, filter, pagination, tab switches)
- Check whether the results container has `aria-live="polite"` or `aria-live="assertive"`
- Flag if a visible results update has no `aria-live` region
- Also check that existing `aria-live` regions are not being removed or their containers replaced in ways that would detach the attribute

**P1-C in JS — Dynamic ARIA manipulation:**
- Look for `setAttribute('role', ...)`, `setAttribute('aria-*', ...)`, or similar calls
- Verify the role/attribute values being set are valid
- Flag calls that remove ARIA attributes (`.removeAttribute('aria-label')`, setting `aria-hidden="true"` on interactive elements)

### Includes checks (P2-C, P3-B)

**P2-C — New-tab link warnings:**
- Grep for `target="_blank"`
- For each instance, check whether the adjacent HTML provides a screen-reader notice: visually hidden `<span>` text, `aria-label` on the `<a>` that includes "opens in new tab" (or equivalent), or an icon with descriptive `alt`
- Flag bare `target="_blank"` with no notice

**P3-B — Input labels:**
- Grep for `<input`, `<select`, `<textarea`
- For each input, verify one of: `<label for="[id]">` pair, `aria-label="..."`, or `aria-labelledby="[id]"`
- Flag inputs where only `placeholder` text is present (placeholder is not an accessible label)

---

## Step 3: Collect all findings

After reading all relevant files, compile every finding into a structured list. Do not stop to ask questions mid-audit.

For each finding record:
```
[Priority ID] [Issue name]
File: path/to/file.html (line N)
Found: [quoted pattern or description]
Why it matters: [one sentence]
Fix: [what the author should do]
```

If a file has no issues for any of its applicable checks, note it as clean.

**If no findings were recorded across all checked files:** present the following and stop — do not proceed to Step 4:

> Architecture accessibility audit complete — no issues found. All [N] changed file(s) are clean.

---

## Step 4: Present findings

Present all findings in a single response, ordered by priority (P1 before P2, etc.). Within each priority, order by frequency of occurrence (most common pattern first).

Use this format:

---

### Accessibility audit — architecture changes

**[N] issue(s) found across [M] file(s)**

---

#### 🔴 Priority 1 — Critical

**[Issue name]** · `path/to/file.html:line`
> [Quoted pattern]

[Why it matters — 1 sentence]
**Fix:** [What to do]

---

#### 🟠 Priority 2 — High
[Same format]

#### 🟡 Priority 3 — Medium
[Same format]

#### 🟢 Priority 4 — Low
[Same format]

---

**Clean files:** [list any checked files with no findings]

---

**STOP.** Do not make any changes. The author reviews these findings and decides what to act on. If they ask you to help fix a specific finding, assist them — but wait for explicit direction on each one.

---

## Step 5: Post-flagging assistance

If the author asks you to help fix a specific finding:

1. Read the affected file again to get current context
2. Propose the specific change in a code block — don't apply it yet
3. Explain the trade-off if the fix has any ambiguity (e.g., `aria-label` vs `<caption>` for a table)
4. Wait for confirmation before applying
5. After applying, re-read the file to confirm the fix landed correctly and didn't introduce adjacent issues

Never fix multiple findings in one pass without the author confirming each one.

---

## Success Criteria

- [ ] All relevant changed files have been read
- [ ] All applicable patterns from the priority catalog have been checked
- [ ] Every finding includes file, line, quoted pattern, impact, and fix direction
- [ ] Findings are presented in priority order in a single response
- [ ] No changes have been made to any file
