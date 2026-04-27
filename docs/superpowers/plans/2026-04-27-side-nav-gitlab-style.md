# Side Nav GitLab-Style Visual Refresh — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update `_navigation_menu.scss` so the Braze Docs side nav matches the GitLab Docs visual language — row height 40px, border-radius 8px, darker hover fill, and snappier easing — while retaining Braze tokens and all existing accessibility fixes.

**Architecture:** All changes are confined to a single SCSS file. The plan is three independent variable/property groups: (1) color tokens, (2) geometry (height + radius + active bar), (3) motion. Each group gets its own task and commit so diffs are reviewable in isolation. RSpec tests cover the Ruby plugin (already on branch) and are unaffected; no JS or HTML changes.

**Tech Stack:** SCSS (compiled by Jekyll/sassc), RSpec 3.13 for existing plugin tests.

---

## File Map

| File | Role |
|---|---|
| `assets/css/_navigation_menu.scss` | Only file changed. All token, geometry, and motion edits live here. |
| `spec/plugins/urlnavmenu_generator_spec.rb` | Existing tests — run after each task to confirm no regressions. |

---

## Task 1: Update Color Tokens

**Spec section:** Section 1 — Color & Tokens

**Files:**
- Modify: `assets/css/_navigation_menu.scss:24-25`

### What you're doing

Change `$nav-hover-bg` from `$grey-athens` (#f4f4f7) to `$grey-ghost` (#dddde2). Leave `$nav-active-bg` at `$grey-athens`. This creates a visible hover/active distinction — hover is darker, active is lighter with the purple bar carrying weight.

`$grey-ghost` is already defined in `assets/css/main.scss:142` as `#dddde2`. It's used elsewhere in the codebase for borders, so it is a known Braze token.

The change cascades automatically to all selectors that reference `$nav-hover-bg`:
- `.nav_item_row:hover` (line 229)
- `.nav div.nav-item > .nav_reg:hover` and `.nav_block:hover` (line 300–302)
- `#sidebar_toggle:hover` (line 68)
- collapsed `#sidebar_toggle` background (line 143)

No additional selector edits needed.

- [ ] **Step 1: Change `$nav-hover-bg`**

Open `assets/css/_navigation_menu.scss`. Find lines 23–25:

```scss
// Nav highlight colors (neutral gray, GitLab-style)
$nav-hover-bg: $grey-athens;
$nav-active-bg: $grey-athens;
```

Change to:

```scss
// Nav highlight colors (neutral gray, GitLab-style)
$nav-hover-bg: $grey-ghost;
$nav-active-bg: $grey-athens;
```

- [ ] **Step 2: Run existing RSpec tests**

```bash
bundle exec rspec spec/plugins/urlnavmenu_generator_spec.rb --format documentation
```

Expected output:
```
Jekyll::UrlNavMenu#build_menu_html
  active leaf page (no children)
    renders aria-current='page' on the active span
  active section page (has children, is current page)
    renders aria-current='page' on the active span inside the nav_item_row
  non-active page
    does not render aria-current on a regular link

3 examples, 0 failures
```

If any test fails, stop — do not continue to Step 3.

- [ ] **Step 3: Commit**

```bash
git add assets/css/_navigation_menu.scss
git commit -m "Update nav hover token to grey-ghost for GitLab-style fill"
```

---

## Task 2: Update Geometry — Row Height, Border Radius, Active Bar

**Spec section:** Section 2 — Spacing & Geometry

**Files:**
- Modify: `assets/css/_navigation_menu.scss` (multiple locations, detailed below)

### What you're doing

Four geometry changes, all in `_navigation_menu.scss`:

1. `.nav_item_row`: `min-height: 32px` → `40px`, `border-radius: 4px` → `8px`
2. `.nav div.nav-item > .nav_reg` and `.nav_block`: `min-height: 28px` → `40px`, `border-radius: 4px` → `8px`
3. `a.nav_link`: `min-height: 28px` → `40px`, `border-radius: 6px` → `8px`
4. Active `::before` bar on `.nav_item_row`, `.nav_reg`, `.nav_block`: `top: 4px; bottom: 4px` → `top: 6px; bottom: 6px`, `border-radius: 4px` → `8px` on the active highlight container

Work through each change individually below. Exact current line numbers are noted for reference — verify before editing since prior tasks may have shifted lines by ±1.

- [ ] **Step 1: Update `.nav_item_row` min-height and border-radius**

Find the `.nav_item_row` block (currently around line 207). It looks like:

```scss
.nav_item_row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    min-width: 0;
    padding: 4px 8px;
    border-radius: 4px;
    min-height: 32px;
    box-sizing: border-box;
    position: relative;
```

Change `border-radius: 4px` → `border-radius: 8px` and `min-height: 32px` → `min-height: 40px`:

```scss
.nav_item_row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    min-width: 0;
    padding: 4px 8px;
    border-radius: 8px;
    min-height: 40px;
    box-sizing: border-box;
    position: relative;
```

- [ ] **Step 2: Update `a.nav_link` min-height and border-radius**

Find the `a.nav_link` block (currently around line 268):

```scss
a.nav_link {
    display: inline-flex;
    align-items: center;
    min-height: 28px;
    width: 100%;
    padding: 0;
    border-radius: 6px;
```

Change `min-height: 28px` → `min-height: 40px` and `border-radius: 6px` → `border-radius: 8px`:

```scss
a.nav_link {
    display: inline-flex;
    align-items: center;
    min-height: 40px;
    width: 100%;
    padding: 0;
    border-radius: 8px;
```

- [ ] **Step 3: Update `.nav_reg` / `.nav_block` min-height and border-radius**

Find the leaf-item rule (currently around line 288):

```scss
.nav div.nav-item > .nav_reg,
.nav div.nav-item > .nav_block {
    display: flex;
    align-items: center;
    min-height: 28px;
    padding: 4px 8px;
    border-radius: 4px;
    position: relative;
    box-sizing: border-box;
```

Change `min-height: 28px` → `min-height: 40px` and `border-radius: 4px` → `border-radius: 8px`:

```scss
.nav div.nav-item > .nav_reg,
.nav div.nav-item > .nav_block {
    display: flex;
    align-items: center;
    min-height: 40px;
    padding: 4px 8px;
    border-radius: 8px;
    position: relative;
    box-sizing: border-box;
```

- [ ] **Step 4: Update active highlight container border-radius and active bar inset**

Find the `.active` block inside `.nav div.nav-item` (currently around line 379). It contains:

```scss
&.active {
    width: 100%;
    color: $black-shark;
    > .nav_item_row,
    > .nav_reg,
    > .nav_block {
        background-color: $nav-active-bg;
        border-radius: 4px;
        &::before {
            content: '';
            position: absolute;
            left: 0;
            top: 4px;
            bottom: 4px;
            width: 3px;
            background-color: $braze-purple;
            border-radius: 2px;
        }
    }
```

Change `border-radius: 4px` on the active container → `border-radius: 8px`, and the bar inset `top: 4px; bottom: 4px` → `top: 6px; bottom: 6px`:

```scss
&.active {
    width: 100%;
    color: $black-shark;
    > .nav_item_row,
    > .nav_reg,
    > .nav_block {
        background-color: $nav-active-bg;
        border-radius: 8px;
        &::before {
            content: '';
            position: absolute;
            left: 0;
            top: 6px;
            bottom: 6px;
            width: 3px;
            background-color: $braze-purple;
            border-radius: 2px;
        }
    }
```

- [ ] **Step 5: Run existing RSpec tests**

```bash
bundle exec rspec spec/plugins/urlnavmenu_generator_spec.rb --format documentation
```

Expected: `3 examples, 0 failures`. If any test fails, stop.

- [ ] **Step 6: Commit**

```bash
git add assets/css/_navigation_menu.scss
git commit -m "Update nav row height to 40px and border-radius to 8px (GitLab geometry)"
```

---

## Task 3: Update Transition Easing

**Spec section:** Section 3 — Motion

**Files:**
- Modify: `assets/css/_navigation_menu.scss` (4 locations)

### What you're doing

Replace `ease` with `cubic-bezier(0.22, 0.61, 0.36, 1)` (GitLab's easing curve) in every `background-color` transition. This is ease-out: starts fast, decelerates. All transitions are already inside `@media (prefers-reduced-motion: no-preference)` guards — do not remove those guards.

Four locations to update:

1. `#sidebar_toggle` transition (currently ~line 65)
2. `.nav_item_row` transition (currently ~line 218)
3. `button.nav_toggle` transition (currently ~line 248)
4. `.nav div.nav-item > .nav_reg, .nav_block` transition (currently ~line 297)

- [ ] **Step 1: Update `#sidebar_toggle` transition**

Find inside `#nav_col > @media > #sidebar_toggle`:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s ease, color 0.2s ease;
}
```

Change to:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s cubic-bezier(0.22, 0.61, 0.36, 1), color 0.2s cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

- [ ] **Step 2: Update `.nav_item_row` transition**

Find inside `.nav_item_row`:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s ease;
}
```

Change to:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

- [ ] **Step 3: Update `button.nav_toggle` transition**

Find inside `button.nav_toggle`:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s ease, color 0.2s ease;
}
```

Change to:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s cubic-bezier(0.22, 0.61, 0.36, 1), color 0.2s cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

- [ ] **Step 4: Update `.nav_reg` / `.nav_block` transition**

Find inside `.nav div.nav-item > .nav_reg, .nav div.nav-item > .nav_block`:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s ease;
}
```

Change to:

```scss
@media (prefers-reduced-motion: no-preference) {
    transition: background-color 0.2s cubic-bezier(0.22, 0.61, 0.36, 1);
}
```

- [ ] **Step 5: Run existing RSpec tests**

```bash
bundle exec rspec spec/plugins/urlnavmenu_generator_spec.rb --format documentation
```

Expected: `3 examples, 0 failures`. If any test fails, stop.

- [ ] **Step 6: Commit**

```bash
git add assets/css/_navigation_menu.scss
git commit -m "Update nav transitions to GitLab ease-out cubic-bezier curve"
```

---

## Final Verification

- [ ] **Confirm no conflict markers remain**

```bash
grep -n "<<<<<<\|=======\|>>>>>>>" assets/css/_navigation_menu.scss
```

Expected: no output.

- [ ] **Confirm all four easing instances updated**

```bash
grep -n "0.2s ease" assets/css/_navigation_menu.scss
```

Expected: no output (all instances replaced).

- [ ] **Confirm geometry values**

```bash
grep -n "min-height: 28px\|min-height: 32px\|border-radius: 4px\|border-radius: 6px" assets/css/_navigation_menu.scss
```

Expected: no output from any of those old values in nav row selectors. (The `border-radius: 4px` on `button.nav_toggle` and `#dev_select` are intentionally unchanged — this grep may surface those. Verify manually they are not nav row selectors.)

- [ ] **Run full test suite one final time**

```bash
bundle exec rspec spec/ --format documentation
```

Expected: `3 examples, 0 failures`.
