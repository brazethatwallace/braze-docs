# ADA Issue Priority Catalog

Prioritized issue list from the Braze Docs ABA audit (Epic BD-6188). Use this as the ordering
framework when presenting findings for architecture changes. Always lead with Priority 1.

---

## Priority 1 — Critical: Sitewide / Core Navigation

These affect all keyboard and AT users on every page. Flag immediately and prominently.

### P1-A: Focus-visible rings (BD-6195)
- **What it is:** Interactive elements (buttons, links, inputs) without a visible focus indicator when navigated by keyboard.
- **Why it matters:** Keyboard-only users cannot see where focus is on the page — WCAG 2.4.7 (AA).
- **What to check:** CSS/SCSS files changing `outline`, `box-shadow`, or `focus` selectors. Look for `:focus` without `:focus-visible`, or any `outline: none` / `outline: 0` that isn't paired with a `:focus-visible` replacement.
- **Pattern to flag:** `outline: none`, `outline: 0` without a corresponding `:focus-visible` rule in the same selector scope.
- **Fix direction:** Use `outline` or `box-shadow` on `:focus-visible`. Do not suppress focus rings without a visible alternative.
- **Related PRs:** #13993

### P1-B: Skip navigation (BD-6194)
- **What it is:** Missing or broken skip-to-main-content link at the top of every page.
- **Why it matters:** Without skip nav, keyboard users must tab through the entire header/nav on every page before reaching content — WCAG 2.4.1 (A).
- **What to check:** `_layouts/default.html` or the primary layout file. Look for a skip link (`<a href="#main-content">`) early in the `<body>`. Check that `id="main-content"` exists on the main landmark.
- **Pattern to flag:** No skip link present; skip link present but `id="main-content"` target is missing or wrong; skip link that is permanently hidden (not just visually hidden until focused).
- **Related PRs:** #13631

### P1-C: ARIA validity — invalid roles and missing required labels (BD-6193)
- **What it is:** `role=` attributes with invalid values, ARIA attributes on elements that don't support them, or required ARIA properties missing.
- **Why it matters:** Invalid ARIA actively breaks screen reader announcements — worse than no ARIA at all — WCAG 4.1.2 (AA).
- **What to check:** Any `role=` being added or changed. Verify the value is a valid ARIA role. Check that required owned elements and properties are present (e.g., `role="listbox"` needs `role="option"` children).
- **Pattern to flag:** `role="presentation"` on elements that have focusable children or semantic meaning (headings, links, buttons). `aria-label` on elements that don't support it. Duplicate `id` attributes (breaks `aria-labelledby`).
- **Related PRs:** #13632

---

## Priority 2 — High: Dynamic Content and Color

These affect significant user groups and commonly arise from feature changes.

### P2-A: Color contrast — text and UI elements (BD-6189, BD-6195)
- **What it is:** Text or UI elements with insufficient contrast against their background.
- **Why it matters:** Affects users with low vision — WCAG 1.4.3 (AA) requires 4.5:1 for normal text, 3:1 for large text (18px+ or 14px bold+).
- **What to check:** When CSS color values change — look for foreground/background pairs in alerts, code blocks, buttons, links, badges, and inline callouts. Check both light and dark mode if applicable.
- **Pattern to flag:** Any new color pairing introduced without a contrast check. Alert component colors (especially `--color-warning`, `--color-info`, `--color-tip`). Code block syntax highlight colors against the code background.
- **Fix direction:** Use a contrast checker (WebAIM or equivalent) before introducing new color pairings. Document the ratio in a comment.
- **Related PRs:** #13432, #13550, #13554

### P2-B: VoiceOver / live region announcements (BD-6190)
- **What it is:** Dynamic content changes (search results, filter updates, glossary entries) not announced to screen readers.
- **Why it matters:** Screen reader users don't hear UI updates that happen without a focus move — WCAG 4.1.3 (AA).
- **What to check:** Any JS or Liquid template that updates visible content in response to user interaction (search, filter, sort, tab switches, async loads). Look for the relevant container element.
- **Pattern to flag:** Interactive UI components (search inputs, filters, paginated results, tabs) without `aria-live` on their results container. Also check that `aria-live="polite"` is used (not `assertive`) for non-critical updates.
- **Pattern to flag (specific):** Changes to `_includes/` search or glossary components that don't carry or preserve the existing `aria-live` region.
- **Related PRs:** #13647, #13651

### P2-C: Links opening in new tabs without warning (T7)
- **What it is:** Links with `target="_blank"` that don't warn screen reader users they'll open in a new tab.
- **Why it matters:** Unexpected context switches disorient screen reader and keyboard users — WCAG 3.2.2 (AA).
- **What to check:** Any new `target="_blank"` in templates, `_includes/`, or JS. Check for either: a visually hidden `<span>` like "opens in new tab", or an `aria-label` that includes the warning, or an icon with descriptive alt text.
- **Pattern to flag:** Bare `target="_blank"` without any screen-reader notice.
- **Related PRs:** #13437

---

## Priority 3 — Medium: Component-Specific

Scoped to specific components or pages; won't affect the full site if missed.

### P3-A: iframe title attributes (BD-6192)
- **What it is:** Embedded `<iframe>` elements without a `title` attribute.
- **Why it matters:** Screen readers use `title` to announce the frame's purpose before the user enters it — WCAG 4.1.2 (AA).
- **What to check:** Any file adding or modifying `<iframe>` tags. Check for `title="[descriptive label]"` on every `<iframe>`.
- **Pattern to flag:** `<iframe src="...">` without `title=`.
- **Related PRs:** #13628

### P3-B: Form input accessible labels (BD-6191)
- **What it is:** Form inputs (search boxes, filters, text fields) without an associated accessible label.
- **Why it matters:** Screen readers announce the label when the user focuses the input — without it, the field is unnamed — WCAG 1.3.1 (AA).
- **What to check:** Any `<input>`, `<select>`, or `<textarea>` being added or changed. Verify it has either: a `<label for="id">` pair, `aria-label`, or `aria-labelledby`.
- **Pattern to flag:** Bare input elements (especially search inputs with placeholder text only — placeholder is not an accessible label).
- **Related PRs:** #13625

### P3-C: Alert and heading semantics (T5/T10)
- **What it is:** Alert components using `<div>` headings styled as headings but not using semantic heading elements, or heading levels that skip ranks.
- **Why it matters:** Screen reader users navigate by heading structure — improper semantics break the document outline — WCAG 1.3.1 (AA).
- **What to check:** Alert/callout `_includes/` files and layout templates. Check that visual headings inside alerts use `<h2>`–`<h6>` (not `<p>` or `<strong>`), and that heading levels don't skip (e.g., `<h2>` → `<h4>`).
- **Related PRs:** #13434

---

## Priority 4 — Low: Cleanup

Minor improvements; generally safe to batch with other changes.

### P4-A: Obsolete meta tags (T10)
- **What it is:** Legacy meta tags that no longer serve a purpose (e.g., `<meta http-equiv="X-UA-Compatible">`).
- **Pattern to flag:** `<meta http-equiv="X-UA-Compatible" content="IE=edge">` or similar IE-era directives in layout `<head>`.
- **Related PRs:** #13434

---

## Issue Quick-Reference Table

| ID | Issue | Impact scope | Auto-fixable by AI |
|----|-------|--------------|-------------------|
| P1-A | Focus-visible rings | Sitewide | No — CSS scope judgment required |
| P1-B | Skip navigation | Sitewide | No — structural change |
| P1-C | ARIA validity | Per component | No — semantic judgment required |
| P2-A | Color contrast | Sitewide | No — needs ratio verification |
| P2-B | Live regions | Dynamic UI | No — JS behavior context needed |
| P2-C | New-tab warnings | Links | No — copy and UI judgment |
| P3-A | iframe titles | Embeds only | No — label wording is contextual |
| P3-B | Input labels | Forms | No — label wording is contextual |
| P3-C | Heading semantics | Alerts/layouts | No — document outline judgment |
| P4-A | Obsolete meta tags | `<head>` | Yes — mechanical removal |
