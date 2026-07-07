# Workflow: Architecture Accessibility Audit

## Required Reading
Load [references/wcag-aa-docs-criteria.md](../references/wcag-aa-docs-criteria.md) before proceeding.

---

## Overview

Architecture changes touch templates, JS, CSS, and config — places where a single pattern can affect every page on the site. This workflow reads the changed files, checks for WCAG 2.2 Level AA patterns relevant to the Braze Docs site, and presents findings ordered by criterion impact. **Nothing is auto-fixed** (except P4-A meta tags on explicit request).

---

## Step 1: Inventory the changed architecture files

Categorize each changed architecture file by type. This determines which checks to run.

| File type | Checks to run |
|---|---|
| `assets/css/**`, `assets/scss/**` | 2.4.7 (focus visible), 1.4.3 (contrast), 1.4.11 (non-text contrast), 2.4.3 (focus order), 2.4.11 (focus not obscured), 2.5.8 (target size) |
| `_layouts/**`, root `*.html` | 2.4.1 (skip nav), 4.1.2 (ARIA validity, iframes), 1.3.1 (heading semantics), 3.1.1 (language of page), P4-A (meta tags) |
| `_includes/**/*.html` | 4.1.2 (ARIA validity, input labels, iframes), 4.1.3 (live regions), 2.4.4 (new-tab links), 1.3.1 (heading semantics) |
| `assets/js/**` | 4.1.3 (live regions), 4.1.2 (dynamic ARIA) |
| `_config*.yml`, `.github/workflows/**`, `Gemfile`, `package.json` | No accessibility checks — skip |

Run only the checks relevant to the file types that changed. Don't run every check on every file.

---

## Step 2: Read each changed file and check for patterns

For each changed file, read the file content and look for the patterns listed below. Record every finding with:
- **File and line number** (or range)
- **WCAG criterion** (e.g., WCAG 2.4.7)
- **Plain-English description** of the issue
- **What was found** — quote the exact pattern that triggered the finding
- **Why it matters** — one sentence (use `wcag-aa-docs-criteria.md` for the explanation)
- **Fix direction** — what the author should do

### CSS / SCSS checks

**WCAG 2.4.7 — Focus Visible:**
- Look for `:focus` blocks that set `outline: none` or `outline: 0`
- Check whether a `:focus-visible` alternative exists in the same selector scope with a visible replacement (border, box-shadow, or background change)
- Flag if `outline: none` / `outline: 0` appears without a paired `:focus-visible` rule
- Also flag `*:focus { outline: none }` or similar broad resets
- Note: `:focus { outline: none }` plus `:focus-visible { outline: ... }` is the acceptable modern pattern — do not flag it

**WCAG 1.4.3 — Contrast (Minimum):**
- Look for new or changed `color:` and `background-color:` pairs on text-bearing elements
- Hotspots: alert/callout component colors, code block syntax highlighting, badge/tag elements, link colors, inline code
- **Do not compute ratios** — flag the color pair and ask the author to verify with a contrast checker

**WCAG 1.4.11 — Non-text Contrast:**
- Look for new border or outline colors on UI components (buttons, inputs, checkboxes)
- Look for icon colors that are the only indicator of meaning
- Look for focus indicator replacement colors (when outline is replaced by a custom indicator)
- Same caution: flag the value, ask the author to verify

**WCAG 2.4.3 — Focus Order:**
- Look for `order:` CSS property on flex/grid containers that have focusable children — visual order may differ from DOM order
- Look for `tabindex` values greater than 0 in associated templates (tabindex="1" or higher creates custom focus order, which is almost always wrong)
- Flag patterns that could cause keyboard focus to jump unexpectedly

**WCAG 2.4.11 — Focus Not Obscured (WCAG 2.2):**
- Look for new or modified `position: sticky` or `position: fixed` on header or navigation elements
- Check whether `scroll-padding-top` or `scroll-margin-top` is set on `html` or `body` to offset sticky elements — if a sticky header is introduced without a corresponding scroll offset, flag it
- Note: this criterion requires browser verification; flag the pattern and ask the author to test with keyboard navigation

**WCAG 2.5.8 — Target Size Minimum (WCAG 2.2):**
- Look for CSS rules on interactive elements (`.btn`, `button`, `a`, `.nav-link`, `.tab`, `.icon-btn`, `.badge`, `.tag`, `.toggle`, `.checkbox`) where `width` or `height` is set below 24px
- Flag candidates below the 24×24 CSS px minimum and ask the author to verify size or confirm adequate spacing

---

### Layout / HTML template checks

**WCAG 2.4.1 — Bypass Blocks:**
- Scan changed `_layouts/` and root `.html` for a skip link (`<a href="#main-content">` or equivalent) as one of the first focusable elements in `<body>`
- Check that an element with `id="main-content"` exists in the same template
- Flag if the skip link is missing, if the target ID is missing, or if the skip link uses `display: none` (visually hidden with `position: absolute` is acceptable)

**WCAG 3.1.1 — Language of Page:**
- Look for `<html` tags in changed layout files
- Verify `lang="en"` (or appropriate language code) is present and non-empty
- Flag if `lang` is missing or empty

**WCAG 4.1.2 — Name, Role, Value (ARIA validity):**
- Scan for `role=` attribute changes — verify the value is a valid ARIA landmark, widget, or document structure role
- Flag `role="presentation"` or `role="none"` on elements that have focusable descendants (links, buttons, inputs inside the element)
- Flag duplicate `id` attributes — `aria-labelledby` breaks silently when IDs collide

**WCAG 4.1.2 — iframe titles (layout templates):**
- Grep for `<iframe` tags
- Flag any `<iframe` without a `title="[non-empty string]"` attribute

**WCAG 1.3.1 — Info and Relationships (heading semantics):**
- Look for elements styled visually as headings but using `<div>`, `<p>`, or `<span>` instead of `<h2>`–`<h6>`
- Look for heading level skips: an `<h4>` appearing after an `<h2>` with no `<h3>` between them
- Alert `_includes/` files are a common hotspot — check that alert headings use semantic elements

**P4-A — Obsolete meta tags (non-WCAG cleanup):**
- Scan `<head>` for `<meta http-equiv="X-UA-Compatible">` or similar IE-era directives
- This is the only finding that may be auto-removed (on explicit author request)

---

### JavaScript checks

**WCAG 4.1.3 — Status Messages:**
- Look for code that updates DOM content in response to user interaction (search, filter, pagination, tab switches, async loads)
- Check whether the results container has `aria-live="polite"` or `aria-live="assertive"`
- Flag if a visible results update has no `aria-live` region
- Check that existing `aria-live` regions are not being removed or their containers replaced

**WCAG 4.1.2 — Dynamic ARIA manipulation:**
- Look for `setAttribute('role', ...)`, `setAttribute('aria-*', ...)`, or similar calls
- Verify the role/attribute values being set are valid
- Flag calls that remove ARIA attributes (`.removeAttribute('aria-label')`, setting `aria-hidden="true"` on interactive elements)

---

### Includes checks

**WCAG 2.4.4 — New-tab link warnings:**
- Grep for `target="_blank"`
- For each instance, check whether the adjacent HTML provides a screen-reader notice: visually hidden `<span>` text, `aria-label` on the `<a>` that includes "opens in new tab" (or equivalent), or an icon with descriptive alt text
- Flag bare `target="_blank"` with no notice

**WCAG 4.1.2 — Input labels:**
- Grep for `<input`, `<select`, `<textarea`
- For each input, verify one of: `<label for="[id]">` pair, `aria-label="..."`, or `aria-labelledby="[id]"`
- Flag inputs where only `placeholder` text is present (placeholder is not an accessible label)

---

## Step 3: Collect all findings

After reading all relevant files, compile every finding into a structured list. Do not stop to ask questions mid-audit.

For each finding record:
```
WCAG [criterion ID] — [criterion name]
File: path/to/file (line N)
Found: [quoted pattern or description]
Why it matters: [one sentence]
Fix: [what the author should do]
```

If a file has no issues for any of its applicable checks, note it as clean.

**If no findings were recorded across all checked files:** present the following and stop:

> Architecture accessibility audit complete — no issues found. All [N] changed file(s) are clean.

---

## Step 4: Present findings

Present all findings in a single response. Order by WCAG level impact: criteria affecting the broadest user groups and most pages first.

Suggested ordering:
1. **Critical (sitewide):** 2.4.7 (focus visible), 2.4.1 (skip nav), 4.1.2 (ARIA validity)
2. **High (color/dynamic):** 1.4.3 (contrast), 1.4.11 (non-text contrast), 4.1.3 (live regions)
3. **Medium (component-specific):** 3.1.1 (lang), 2.4.11 (focus not obscured), 2.5.8 (target size), 2.4.4 (new-tab links), 2.4.3 (focus order), 1.3.1 (heading semantics)
4. **Low (cleanup):** P4-A (meta tags)

Use this format:

---

### Accessibility audit — architecture changes

**[N] issue(s) found across [M] file(s)**

---

#### Critical

**WCAG [criterion] — [criterion name]** · `path/to/file:line`
> [Quoted pattern]

[Why it matters — 1 sentence]
**Fix:** [What to do]

---

*(Repeat for High, Medium, Low)*

**Clean files:** [list any checked files with no findings]

---

**STOP.** Do not make any changes — with one exception: **P4-A (obsolete meta tags)** may be auto-removed if the author explicitly asks. For all other findings, wait for explicit direction before touching any file.

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
- [ ] All applicable WCAG checks have been run for each file type
- [ ] Every finding includes WCAG criterion, file, line, quoted pattern, impact, and fix direction
- [ ] Findings are presented in impact order in a single response
- [ ] No changes have been made to any file (except P4-A on explicit request)
