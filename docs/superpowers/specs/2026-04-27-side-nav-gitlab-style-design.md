# Side Navigation: GitLab-Style Visual Refresh

**Date:** 2026-04-27
**Branch:** `bf/side-nav-ui-improvements`
**Approach:** Option B — GitLab-inspired, Braze-adjusted

---

## Goal

Make the Braze Docs side navigation feel more visually similar to GitLab Docs's side navigation, while retaining Braze design tokens, preserving the existing expand/collapse behavior, and keeping all WCAG 2.2 accessibility improvements already on the branch.

**Reference:** https://docs.gitlab.com/user/ — reverse-engineered from live CSS at `https://docs.gitlab.com/vite/main.css` and `https://docs.gitlab.com/gitlab_ui/ui/index.css`.

---

## What Is Not Changing

- Expand/collapse behavior (Bootstrap collapse, `documents.js`)
- Sidebar toggle (collapse to icon-only rail)
- Caret icon swap (`fa-chevron-right` ↔ `fa-chevron-down`) — left as-is to avoid touching three files for a subtle animation gain
- Ruby plugin HTML structure (`urlnavmenu_generator.rb`)
- `aria-current="page"` fix (already on branch)
- `button.nav_toggle` 24px min target size (already on branch)
- `$nav-nesting-border: #b0b0b7` accessible nesting line (already on branch)
- Nesting indent geometry (already equivalent to GitLab at ~20px effective indent)

---

## Section 1: Color & Tokens

**File:** `assets/css/_navigation_menu.scss`

### Token changes

| Token | Before | After | Rationale |
|---|---|---|---|
| `$nav-hover-bg` | `$grey-athens` (#f4f4f7) | `$grey-ghost` (#dddde2) | Closer to GitLab's `neutral-50` (#ececef); visibly distinct from white |
| `$nav-active-bg` | `$grey-athens` (#f4f4f7) | `$grey-athens` (#f4f4f7) | Kept lighter than hover; purple bar carries active weight. More GitLab-like than making both the same. |

**Contrast impact:**
- `$black-shark` (#212123) on `$grey-ghost` (#dddde2): ~11.9:1 — passes all thresholds
- `$braze-purple` (#801ED7) on `$grey-ghost`: ~5.0:1 — passes AA text (4.5:1)
- `$grey-ghost` on white for the nesting border is **not** used — `$nav-nesting-border: #b0b0b7` (3.1:1) is already the value

### Active Bar Color

`$braze-purple` — unchanged, replaces GitLab's blue with Braze brand color.

### Cascade note

`$nav-hover-bg` is also used by `#sidebar_toggle:hover` (the collapsed-sidebar toggle button background) and `button.nav_toggle:hover` background inherits from the token. Both pick up the updated `$grey-ghost` value automatically — no separate selector changes needed.

---

## Section 2: Spacing & Geometry

**File:** `assets/css/_navigation_menu.scss`

### Row height

All nav rows unified to `min-height: 40px` (GitLab: `2.5rem` = 40px).

| Selector | Before | After |
|---|---|---|
| `.nav_item_row` | `min-height: 32px` | `min-height: 40px` |
| `.nav div.nav-item > .nav_reg` | `min-height: 28px` | `min-height: 40px` |
| `.nav div.nav-item > .nav_block` | `min-height: 28px` | `min-height: 40px` |
| `a.nav_link` | `min-height: 28px` | `min-height: 40px` |

Row padding stays `6px 8px` — height is now driven by `min-height`, not padding inflation.

### Border radius

All hover/active highlight containers: `4px` → `8px`.

| Selector | Before | After |
|---|---|---|
| `.nav_item_row` | `border-radius: 4px` | `border-radius: 8px` |
| `.nav div.nav-item > .nav_reg` | `border-radius: 4px` | `border-radius: 8px` |
| `.nav div.nav-item > .nav_block` | `border-radius: 4px` | `border-radius: 8px` |
| `a.nav_link` focus ring | `border-radius: 6px` | `border-radius: 8px` |
| Active `.nav_item_row`, `.nav_reg`, `.nav_block` | `border-radius: 4px` | `border-radius: 8px` |
| Active bar `::before` | `border-radius: 2px` | `border-radius: 2px` (unchanged — bar is narrow) |

### Active bar inset

The active `::before` bar is height-relative (adapts to text reflow at zoom). Adjusted inset for taller 40px rows:

| Property | Before | After |
|---|---|---|
| `top` | `4px` | `6px` |
| `bottom` | `4px` | `6px` |
| `width` | `3px` | `3px` (unchanged) |

This keeps the bar proportionally similar to GitLab's centered 20px bar in a 40px row, while remaining adaptive.

---

## Section 3: Motion

**File:** `assets/css/_navigation_menu.scss`

### Transition easing

Replace `ease` with GitLab's easing curve everywhere `background-color` is transitioned. Duration stays `0.2s`.

**Before:** `background-color 0.2s ease`
**After:** `background-color 0.2s cubic-bezier(0.22, 0.61, 0.36, 1)`

GitLab's curve is ease-out (fast start, decelerates), making hover responses feel snappier. All `@media (prefers-reduced-motion: no-preference)` guards remain in place.

**Selectors affected:**
- `.nav_item_row`
- `.nav div.nav-item > .nav_reg`
- `.nav div.nav-item > .nav_block`
- `button.nav_toggle`

---

## Files Changed

| File | Change type |
|---|---|
| `assets/css/_navigation_menu.scss` | Token values, min-height, border-radius, easing curve, active bar inset |

No changes to JS, Ruby plugin, HTML templates, or other SCSS files.

---

## GitLab Reference Values (for audit)

Reverse-engineered from live CSS:

| Property | GitLab value | Our equivalent |
|---|---|---|
| Sidebar width | `17rem` (272px) | `$nav_width: 280px` |
| Row min-height | `2.5rem` (40px) | `40px` (after this change) |
| Font size | `0.875rem` (14px) | `14px` ✓ |
| Border radius | `0.5rem` (8px) | `8px` (after this change) |
| Hover/active bg | `#ececef` (neutral-50) | `$grey-ghost` (#dddde2) — slightly darker |
| Nesting indent | `1rem` + `0.25rem` = ~20px | `12px` margin + `8px` padding = 20px ✓ |
| Nesting border | `#ececef` (neutral-50, 1.35:1) | `#b0b0b7` (3.1:1) — more accessible |
| Active bar width | `3px` | `3px` ✓ |
| Active bar height | `20px` fixed, centered | Height-relative (`top/bottom: 6px`) — more accessible |
| Transition easing | `cubic-bezier(0.22, 0.61, 0.36, 1)` | Same (after this change) |
| Transition duration | `0.2s` | `0.2s` ✓ |
