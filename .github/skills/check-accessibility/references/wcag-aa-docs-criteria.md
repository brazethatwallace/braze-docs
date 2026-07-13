# WCAG 2.2 Level AA — Documentation Site Criterion Catalog

Coverage of the WCAG 2.2 Level AA criteria applicable to a Jekyll markdown documentation site. Criteria that apply only to video, audio, animations, or timing-dependent interactions are out of scope for static docs.

Entries are organized by where they fire. Each entry includes: what the criterion means for a docs contributor, what to check, which mechanism runs the check, whether it's auto-fixable, and historical context from the Braze Docs BD-6188 audit.

---

## Content Path Checks

These fire for `_docs/**/*.md`, `_includes/**/*.md`, and `_includes/**/*.html` changes.

---

### 1.1.1 Non-text Content

**Plain English:** Every image that conveys meaning must have a text description (alt text) so screen reader users know what the image shows. Purely decorative images must use an empty alt attribute (`alt=""`) so screen readers skip them.

**What to check:**
- Markdown images: `![alt text](url)` — flag when the `alt text` part is empty (i.e., `![](url)`)
- Distinguish decorative from informational using filename heuristics: filenames containing `divider`, `spacer`, `separator`, `bg-`, `background` → likely decorative (empty alt is correct); all others → likely informational (needs a description)
- For HTML `<img>` tags in includes: check `alt=` attribute; flag missing entirely or `alt=""` on what looks like an informational image

**Check mechanism:** `scripts/check_content_accessibility.py` (structural detection) + LLM judgment during "ask" step for suggested alt text.

**Auto-fixable:**
- Likely-decorative images with empty alt: `ask (high confidence)` — confirm the image is purely decorative before accepting
- Informational images missing alt text: `ask (medium confidence)` — LLM will suggest alt text based on filename and surrounding context; author must confirm or provide their own

**Historical context:** No prior findings in the BD-6188 audit (not covered by the previous check). This is the highest-impact new check added in the WCAG rebuild.

---

### 2.4.4 Link Purpose (In Context)

**Plain English:** A link's visible text (alone or together with the sentence around it) must make it clear where the link goes. Generic text like "click here", "here", "learn more", or "this page" forces users to lose context to understand what the link does.

**What to check:**
- Markdown links `[link text](url)` where the visible text matches a non-descriptive pattern (case-insensitive): `here`, `click here`, `this`, `this link`, `this page`, `learn more`, `read more`, `more`, `link`, `click`, `see more`, `details`
- HTML `<a>` tags in includes with the same non-descriptive patterns
- A special case: links with `target="_blank"` (opening in a new tab) should ideally indicate this in the link text or an adjacent label. Flag bare `target="_blank"` without any new-tab notice.

**Check mechanism:** `scripts/check_content_accessibility.py` (pattern match on link text).

**Auto-fixable:** `Ask (medium confidence)` — fix requires knowing the destination. LLM will show the surrounding sentence and URL for context; author provides or confirms the replacement text.

**Historical context (new-tab):** BD-6188 audit found bare `target="_blank"` links in includes (T7). Related PRs: #13437.

---

### 1.3.1 Info and Relationships — Tables

**Plain English:** Data tables need an accessible name so screen readers can announce what the table is about before reading it. Layout tables (used for visual structure, not data) need `role="presentation"` to tell screen readers to ignore the table structure.

**What to check:**
- GFM markdown tables (`|col1|col2|…`) missing an `aria-label` in an IAL attribute block immediately after the last row
- Existing IAL blocks on tables that are missing `aria-label=`
- HTML `<table>` elements in includes without a `<caption>` or `aria-label` attribute

**Check mechanism:** `scripts/check_table_accessibility.py`

**Auto-fixable:**
- Missing IAL with a clear heading nearby: `Yes (high confidence)` — script derives `aria-label` from nearest heading
- Missing or generic IAL: `Ask (medium confidence)` — author confirms or provides label
- HTML tables, files with 4+ violations: `Ask (low confidence)`

**Historical context:** BD-6188 table accessibility was the primary motivation for the original `check-accessibility` skill. The `check_table_accessibility.py` script and `check-table-accessibility.yml` CI workflow were added during BD-6188 remediation.

---

### 2.4.6 Headings and Labels

**Plain English:** Heading levels in a document should follow a logical hierarchy. Skipping levels (for example, going from an `##` (h2) directly to an `####` (h4) with no `###` (h3) in between) breaks the document outline that screen reader users rely on to navigate.

**What to check:**
- Parse all heading lines (`#` through `######`) in each changed markdown file in the order they appear
- Flag when heading level increases by more than one step (e.g., h2 → h4)
- Ignore headings inside code fences (` ``` ` delimited blocks) and YAML frontmatter (`---` block at file start)
- Focus on the structural skip, not stylistic choices about nesting depth in nested callouts or tabs

**Check mechanism:** `scripts/check_content_accessibility.py`

**Auto-fixable:** `No` — always low confidence. Heading level adjustments change document structure; only the author can decide whether a skipped level should be added as a new heading or the offending heading should be promoted.

**Historical context:** BD-6188 audit found heading level skips in alert components (T5/T10). Related PRs: #13434.

---

### 1.3.3 Sensory Characteristics — Spatial Directionals

**Plain English:** Instructions must not rely on where content appears on the page ("see the table below", "use the operators above"). Screen reader users and mobile readers may not experience the same visual layout, so name the section, tab, or anchor instead.

**What to check:**
- Words such as `above`, `below`, `to the left`, `on the right`, `left of`, and `right of` when they point readers to other content by position
- Allow numeric comparisons: `below the input field`, `above the threshold`
- Allow text-direction terms: `left-to-right`, `right-to-left`, `bi-directional`

**Check mechanism:** `scripts/check_content_accessibility.py` (pattern match with allowlist).

**Auto-fixable:** `Ask (medium confidence)` — replacement wording depends on document structure; author names the target section or anchor.

**Historical context:** Added during filter-operators documentation work (2026) to prevent layout-only cross-references in `_docs/`.

---

### 4.1.2 Name, Role, Value — Inline Iframes (Content)

**Plain English:** Embedded `<iframe>` elements must have a `title` attribute so screen readers can announce what the frame contains before the user enters it. This applies to iframes embedded directly in markdown files (inline HTML).

**What to check:**
- `<iframe` tags in markdown files (inline HTML blocks)
- Flag any `<iframe` missing a `title="[non-empty string]"` attribute

**Check mechanism:** `scripts/check_content_accessibility.py` (regex match on `<iframe` in markdown files).

**Auto-fixable:** `Ask (medium confidence)` — title wording is contextual. Script flags; author provides a descriptive title.

**Historical context:** BD-6188 audit found untitled iframes in template files (BD-6192). Related PRs: #13628. This entry covers the inline markdown case; the template/layout case is in the Architecture section below.

---

## Architecture Path Checks

These fire for `_layouts/**`, `_includes/**/*.html`, `assets/js/**`, `assets/css/**`, `assets/scss/**`, `_config*.yml`, `*.html` at repo root, `Gemfile`, `package.json`, and `.github/workflows/**` changes.

---

### 2.4.7 Focus Visible

**Plain English:** Every interactive element (links, buttons, inputs) must display a visible focus indicator when navigated by keyboard. CSS rules that hide the focus ring (`outline: none`) without a visible replacement break keyboard navigation for sighted keyboard users.

**What to check (CSS/SCSS files):**
- `:focus` blocks that set `outline: none` or `outline: 0`
- Whether a `:focus-visible` alternative with a visible replacement (border, box-shadow, background change) exists in the same selector scope
- Broad resets like `*:focus { outline: none }` that affect all elements
- Note: `:focus { outline: none }` paired with `:focus-visible { outline: ... }` is acceptable — this pattern hides rings for mouse users while preserving them for keyboard users

**Check mechanism:** LLM reads changed CSS/SCSS.

**Auto-fixable:** No — CSS scope judgment required.

**Historical context:** BD-6188 focus ring issues found sitewide (BD-6195). Related PRs: #13993.

---

### 2.4.1 Bypass Blocks

**Plain English:** A "skip to main content" link at the top of every page lets keyboard users jump past the navigation to the main content without tabbing through the entire header on every page load.

**What to check (layout template files):**
- `_layouts/default.html` (or primary layout) for a skip link (`<a href="#main-content">` or equivalent) as one of the first focusable elements in `<body>`
- A corresponding `id="main-content"` on the main content landmark
- Skip link must be reachable by keyboard — hidden with `position: absolute; left: -9999px` is acceptable; `display: none` is not (the link would be unfocusable)

**Check mechanism:** LLM reads changed layout templates.

**Auto-fixable:** No — structural change to the layout template.

**Historical context:** BD-6188 found missing skip nav on the Braze Docs site (BD-6194). Related PRs: #13631.

---

### 1.4.3 Contrast (Minimum)

**Plain English:** Text must have at least 4.5:1 contrast against its background (3:1 for large text: 18px+ or 14px bold+). This affects users with low vision.

**What to check (CSS/SCSS files):**
- New or changed `color:` and `background-color:` pairs on text-bearing elements
- Hotspots: alert/callout component colors, code block syntax highlighting, badge/tag elements, link colors, inline code on light and dark backgrounds
- Both light mode and dark mode when applicable
- Note: do not compute ratios — flag the pair and ask the author to verify with a contrast checker (WebAIM or browser DevTools)

**Check mechanism:** LLM reads changed CSS/SCSS.

**Auto-fixable:** No — needs ratio verification by author.

**Historical context:** BD-6188 found contrast issues in alert components and code block syntax highlighting (BD-6189, BD-6195). Related PRs: #13432, #13550, #13554.

---

### 1.4.11 Non-text Contrast

**Plain English:** UI component boundaries, icons, and focus indicators used to convey state must have at least 3:1 contrast against adjacent colors. This extends contrast requirements beyond text to interactive UI elements.

**What to check (CSS/SCSS files):**
- Border or outline colors on UI components (buttons, inputs, checkboxes, form fields)
- Icon colors when the icon is the only indicator of meaning
- Focus indicator colors (when added as a replacement for outline)
- Note: same caution as 1.4.3 — flag new color values; do not compute ratios; ask author to verify

**Check mechanism:** LLM reads changed CSS/SCSS.

**Auto-fixable:** No — needs ratio verification.

**Historical context:** No specific BD-6188 finding for non-text contrast. Part of the WCAG 2.2 AA addition to the skill's coverage.

---

### 4.1.2 Name, Role, Value — ARIA, Input Labels, Template Iframes

**Plain English:** Every interactive element in templates must have a name (so screen readers can announce it), a valid role (so assistive tech understands what it is), and correct values (so state changes are communicated). This covers ARIA attribute validity, form input labels, and iframes in layout templates.

**What to check (layout and include files):**

*ARIA validity:*
- `role=` attribute changes — verify the value is a valid ARIA role
- `role="presentation"` or `role="none"` on elements with focusable descendants (links, buttons, inputs inside the element)
- Duplicate `id` attributes — `aria-labelledby` breaks silently when IDs collide
- `setAttribute('role', ...)` or `setAttribute('aria-*', ...)` in JS — verify valid values
- `.removeAttribute('aria-label')`, setting `aria-hidden="true"` on interactive elements

*Form input labels (include files with inputs):*
- `<input>`, `<select>`, `<textarea>` elements
- Each must have one of: `<label for="[id]">` pair, `aria-label="..."`, or `aria-labelledby="[id]"`
- `placeholder` text alone is not an accessible label — flag bare placeholder-only inputs

*Iframes in templates:*
- `<iframe` tags without `title="[non-empty string]"` attribute

**Check mechanism:** LLM reads changed template/include/JS files.

**Auto-fixable:** No — semantic judgment required.

**Historical context:** BD-6188 found ARIA validity issues sitewide (BD-6193, Related PRs: #13632), iframe titles (BD-6192, Related PRs: #13628), and input label issues (BD-6191, Related PRs: #13625).

---

### 4.1.3 Status Messages

**Plain English:** When the page updates content in response to user action (search results appearing, filters updating, form submission feedback), screen readers must be notified without the user having to move focus. This is done with ARIA live regions.

**What to check (JS files and dynamic include templates):**
- Code that updates DOM content in response to user interaction (search, filter, pagination, tab switches, async loads)
- Whether the results container has `aria-live="polite"` (or `aria-live="assertive"` for critical updates)
- Existing `aria-live` regions that are being removed, or their containers replaced in ways that detach the attribute
- Use `aria-live="polite"` (not `assertive`) for non-critical updates like search results

**Check mechanism:** LLM reads changed JS and dynamic template files.

**Auto-fixable:** No — JS behavior context needed.

**Historical context:** BD-6188 found missing live regions on search and filter components (BD-6190). Related PRs: #13647, #13651.

---

### 2.4.3 Focus Order

**Plain English:** When the page receives keyboard focus, elements should receive focus in an order that makes sense for the content — typically top-to-bottom, left-to-right. CSS that visually reorders content (flex/grid order, absolute positioning) can create a mismatch between visual order and focus order.

**What to check (CSS/SCSS and layout template files):**
- `order:` CSS property on flex/grid containers with focusable children — visual order may differ from DOM order, which is what keyboard navigation follows
- `position: absolute` or `position: fixed` on elements that pull them out of the normal flow, creating focus-order confusion
- `tabindex` values greater than 0 — these create custom focus order that is almost always a mistake (tabindex 0 and -1 are fine)

**Check mechanism:** LLM reads changed CSS/SCSS and template files.

**Auto-fixable:** No — layout-level change with side effects.

**Historical context:** No specific BD-6188 finding. Part of the WCAG 2.2 AA addition to the skill's coverage.

---

### 3.1.1 Language of Page

**Plain English:** The `<html>` element must have a `lang` attribute identifying the page's primary language. Screen readers use this to select the correct pronunciation rules for text-to-speech.

**What to check (layout template files):**
- Changed `_layouts/` or root `.html` files — look for `<html` tag
- `lang="en"` (or appropriate language code) must be present and non-empty
- Flag if `lang` is missing, empty (`lang=""`), or visibly wrong (e.g., `lang="en"` on a `_lang/ja/` layout would be a problem, but `_lang/` is out of scope for this check)

**Check mechanism:** LLM reads changed layout files. Also scriptable with grep: `grep -L 'lang=' changed_layouts.html`.

**Auto-fixable:** `Ask (medium confidence)` — adding `lang="en"` to `<html>` is mechanical, but the correct language code depends on the site's language setup. Flag and ask author to confirm.

**Historical context:** Not covered in BD-6188 audit. New check added in the WCAG 2.2 AA rebuild.

---

### 2.4.11 Focus Not Obscured (Minimum) *(WCAG 2.2 new)*

**Plain English:** When a user tabs to an interactive element, the focus indicator must be at least partially visible — not entirely hidden behind a sticky header, sticky navigation, or overlay. This is a WCAG 2.2 addition that specifically addresses sticky/fixed UI elements that scroll over keyboard focus.

**What to check (CSS/SCSS files):**
- New or modified `position: sticky` or `position: fixed` elements, especially headers, navigation bars, or sidebars
- Check whether the page has a sticky header that could cover focused links near the top of the content area — this is a common pattern on documentation sites
- Look for `scroll-padding-top` or `scroll-margin-top` — these are the CSS-based fix for obscured focus when a sticky header is present. If a sticky header is introduced or modified without a corresponding scroll offset, flag it.
- Note: do not compute pixel values — flag the pattern and ask the author to verify in a browser with keyboard navigation

**Check mechanism:** LLM reads changed CSS/SCSS.

**Auto-fixable:** No — requires browser verification and may need `scroll-padding-top` adjustment on the `<html>` element.

**Historical context:** Not covered in BD-6188 audit. WCAG 2.2-specific addition.

---

### 2.5.8 Target Size (Minimum) *(WCAG 2.2 new)*

**Plain English:** Interactive elements (buttons, links, checkboxes, toggles) must be at least 24×24 CSS pixels in size (or have sufficient spacing if smaller) so they're reachable by users with motor impairments or small-touch interactions.

**What to check (CSS/SCSS files):**
- New or changed CSS rules on interactive elements where both `width` and `height` (or `min-width`/`min-height`) are set below 24px
- Element patterns to watch: `.btn`, `button`, `a`, `.nav-link`, `.tab`, `.icon-btn`, `.badge`, `.tag`, `.toggle`, `.checkbox`
- Inline elements (links, inline buttons) with constrained dimensions
- Note: WCAG 2.5.8 provides an offset mechanism — elements smaller than 24×24 can comply if there's sufficient spacing (target area + spacing ≥ 24×24). Flag candidates below threshold and ask author to verify spacing.

**Check mechanism:** LLM reads changed CSS/SCSS.

**Auto-fixable:** No — layout trade-offs required.

**Historical context:** Not covered in BD-6188 audit. WCAG 2.2-specific addition.

---

## Non-WCAG Cleanup

### P4-A: Obsolete Meta Tags *(not a WCAG requirement)*

**Plain English:** Legacy `<meta http-equiv="X-UA-Compatible">` tags were used to force Internet Explorer compatibility modes. These are meaningless in modern browsers and add noise to the `<head>`.

**What to check:**
- `<meta http-equiv="X-UA-Compatible" content="IE=edge">` or similar IE-era directives in layout `<head>`

**Check mechanism:** LLM or grep on changed layout files.

**Auto-fixable:** `Ask (low risk)` — may be auto-removed if the author explicitly asks. This is the only finding in this catalog where auto-removal is offered.

**Note:** This is not a WCAG 2.2 AA requirement. It is a cleanup item retained from the BD-6188 audit because it's low-risk and often surfaces alongside layout changes.

**Historical context:** BD-6188 cleanup item (T10). Related PRs: #13434.

---

## Quick-Reference Table

| Criterion | Description | Path | Auto-fixable |
|---|---|---|---|
| 1.1.1 | Alt text on images | Content | Ask (medium for informational) |
| 1.3.1 | Table accessible names | Content | Yes/Ask (confidence-tiered) |
| 1.4.3 | Text/background contrast | Architecture | No |
| 1.4.11 | Non-text contrast | Architecture | No |
| 2.4.1 | Skip navigation | Architecture | No |
| 2.4.3 | Focus order | Architecture | No |
| 2.4.4 | Descriptive link text | Content | Ask |
| 2.4.6 | Heading hierarchy | Content | No |
| 2.4.7 | Focus visible (focus rings) | Architecture | No |
| 2.4.11 | Focus not obscured (WCAG 2.2) | Architecture | No |
| 2.5.8 | Target size minimum (WCAG 2.2) | Architecture | No |
| 3.1.1 | Language of page | Architecture | Ask |
| 4.1.2 | ARIA validity, labels, iframes | Both | No |
| 4.1.3 | Status messages / live regions | Architecture | No |
| P4-A | Obsolete meta tags (non-WCAG) | Architecture | Ask (on request only) |
