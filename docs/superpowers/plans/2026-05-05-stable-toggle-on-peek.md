# Stable Sidebar Toggle on Flyout Peek — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Keep the sidebar expand/collapse button stationary in the rail while the flyout peek is open, so users can click it without chasing it across the screen.

**Architecture:** `syncSidebarToggleDock()` in `documents.js` currently treats "peek" (collapsed + flyout open) the same as "fully expanded" for button placement, moving the button from the 48px rail into the flyout panel. The fix simplifies the dock condition: when `hide_sidebar` is set (regardless of flyout state), always keep the button in `.left-nav-collapsed-slot`. A companion CSS change raises the slot's z-index above the flyout overlay (`z-index: 200`) so the button isn't hidden behind it.

**Tech Stack:** jQuery (existing), SCSS (existing), no new dependencies.

---

## File Map

| File | Change |
|---|---|
| `assets/js/documents.js` | Simplify `syncSidebarToggleDock()` — remove `peeking` branch, key only on `hide_sidebar` |
| `assets/css/_navigation_menu.scss` | Add `z-index: 201` + `position: relative` to `.left-nav-collapsed-slot` in the `hide_sidebar.doc-nav-flyout-open` state |

---

## Task 1: Simplify `syncSidebarToggleDock` in `documents.js`

**File:** `assets/js/documents.js`

### Background

The current function (around line 504) has a `peeking` variable that evaluates to `true` when `hide_sidebar` is set and the flyout is open. When `peeking` is true the function moves the button to after `#doc_nav_flyout` — that's what causes the position jump. The fix: remove `peeking` entirely and drive placement solely on whether `hide_sidebar` is present.

**Current code (lines ~504–527):**

```js
// Move rail toggle between the first nav row host (expanded / peek) and the collapsed strip.
function syncSidebarToggleDock() {
  var nav_bar = $('#nav_bar');
  var host = $('#sidebar_toggle_host');
  var slot = $('.left-nav-collapsed-slot');
  var btn = $('#sidebar_toggle');
  if (!btn.length) { return; }
  var peeking = nav_bar.hasClass('hide_sidebar') &&
    ($('#left_navmenu').is(':visible') || nav_bar.hasClass('doc-nav-flyout-open'));
  if (nav_bar.hasClass('hide_sidebar') && !peeking) {
    if (slot.length) { btn.appendTo(slot); }
  } else {
    if (host.length) {
      btn.appendTo(host);
    } else {
      var primary = $('.left-nav-primary');
      var flyout = $('#doc_nav_flyout');
      if (primary.length && flyout.length) {
        btn.insertAfter(flyout);
      } else if (slot.length) {
        btn.appendTo(slot);
      }
    }
  }
}
```

- [ ] **Step 1: Replace `syncSidebarToggleDock` with the simplified version**

Find the function block above in `assets/js/documents.js` and replace it with:

```js
// Move rail toggle between the collapsed rail slot and the expanded-nav position.
// During flyout peek (hide_sidebar + doc-nav-flyout-open), the button stays in the
// rail slot so it doesn't jump when the flyout opens.
function syncSidebarToggleDock() {
  var nav_bar = $('#nav_bar');
  var host = $('#sidebar_toggle_host');
  var slot = $('.left-nav-collapsed-slot');
  var btn = $('#sidebar_toggle');
  if (!btn.length) { return; }
  if (nav_bar.hasClass('hide_sidebar')) {
    // Collapsed (with or without flyout peek): button stays in the rail slot.
    if (slot.length && !$.contains(slot[0], btn[0])) { btn.appendTo(slot); }
  } else {
    // Fully expanded: move button to the designated host or below the flyout panel.
    if (host.length) {
      btn.appendTo(host);
    } else {
      var primary = $('.left-nav-primary');
      var flyout = $('#doc_nav_flyout');
      if (primary.length && flyout.length) {
        btn.insertAfter(flyout);
      } else if (slot.length) {
        btn.appendTo(slot);
      }
    }
  }
}
```

The key changes are:
- `peeking` variable removed entirely
- Condition is now simply `nav_bar.hasClass('hide_sidebar')` → rail slot
- Added `!$.contains(slot[0], btn[0])` guard to skip the DOM move when the button is already in the correct place (avoids unnecessary reflow)

- [ ] **Step 2: Manually verify in a browser**

Build the site locally (`bundle exec jekyll serve`) and test:

1. Collapse the sidebar (click the toggle button). Button should be in the 48px rail.
2. Hover over the rail. Flyout should open. **Button should NOT move** — it should remain visible at the top of the rail strip.
3. Click the button while the flyout is open. Sidebar should expand permanently. Button should move to its expanded position (below the nav list).
4. Hover off the sidebar when the flyout is open without clicking. Flyout should close. Button should remain in the rail.
5. Collapse again. Repeat to confirm no regressions.

- [ ] **Step 3: Commit**

```bash
git add assets/js/documents.js
git commit -m "fix: keep sidebar toggle in rail during flyout peek

syncSidebarToggleDock previously moved the button to the flyout panel
when peek mode opened, causing users to chase the icon after hover.
Now the button stays in the collapsed-slot rail for all hide_sidebar
states, and only moves to the expanded position after a permanent expand."
```

---

## Task 2: Raise `.left-nav-collapsed-slot` above the flyout overlay in `_navigation_menu.scss`

**File:** `assets/css/_navigation_menu.scss`

### Background

When `hide_sidebar.doc-nav-flyout-open` is active, the flyout renders as `position: fixed; z-index: 200`. The `.left-nav-collapsed-slot` has no explicit `z-index`, so it sits behind the flyout and the button is visually obscured. We need the slot (and the button inside it) to paint above the flyout so users can see and click it.

Find the `&.hide_sidebar.doc-nav-flyout-open` block (around line 210). It currently opens with `#doc_nav_flyout { ... }`. Add a new rule **inside** that block for `.left-nav-collapsed-slot`:

- [ ] **Step 1: Add the z-index rule to the peek state**

Locate this block in `_navigation_menu.scss`:

```scss
&.hide_sidebar.doc-nav-flyout-open {
  #doc_nav_flyout {
```

Add the following rule **before** the `#doc_nav_flyout` rule, inside `&.hide_sidebar.doc-nav-flyout-open`:

```scss
&.hide_sidebar.doc-nav-flyout-open {
  // Keep the rail slot (and toggle button inside it) above the flyout overlay
  // so the button remains clickable without the user having to chase it.
  #nav_col .left-nav-collapsed-slot:not(:empty) {
    position: relative;
    z-index: 201;
  }
  #doc_nav_flyout {
```

`position: relative` is required for `z-index` to take effect on a non-positioned element. `z-index: 201` beats the flyout's `z-index: 200` by one level.

- [ ] **Step 2: Manually verify in a browser**

1. With the sidebar collapsed, hover over the rail to open the flyout.
2. The toggle button (rail icon) should be **visible** at the top of the 48px strip, **not** hidden behind the flyout panel.
3. Confirm the button has a visible hover/focus state (background highlight) when you mouse over it.
4. Confirm no visual regression on the flyout content itself (nav links, escape hint).

- [ ] **Step 3: Commit**

```bash
git add assets/css/_navigation_menu.scss
git commit -m "fix: raise rail slot above flyout overlay during peek

Without position:relative + z-index:201, the fixed-position flyout
(z-index:200) was painting over the .left-nav-collapsed-slot, hiding
the toggle button the user needs to permanently expand the sidebar."
```

---

## Task 3: Push and open the PR

- [ ] **Step 1: Push the branch**

```bash
git push -u origin bf/side-nav-stable-toggle-on-peek
```

- [ ] **Step 2: Open the PR targeting `bf/side-nav-ui-improvements-v2`**

```bash
gh pr create \
  --base bf/side-nav-ui-improvements-v2 \
  --title "fix: stable sidebar toggle during flyout peek" \
  --body "$(cat <<'EOF'
## Summary

- Sidebar toggle button no longer jumps when the flyout peek opens
- `syncSidebarToggleDock` simplified: button stays in rail slot for all `hide_sidebar` states, only moves on permanent expand
- Rail slot given `z-index: 201` in peek state so button is visible above the flyout overlay

## Test plan

- [ ] Collapse sidebar, hover to open flyout — button stays in rail, no position jump
- [ ] Click button while flyout is open — sidebar expands permanently, button moves to expanded position
- [ ] Hover off flyout without clicking — flyout closes, button stays in rail
- [ ] Fully expand sidebar — button visible in expected position at bottom of nav
- [ ] Keyboard: focus button in rail (`Tab`), press `Enter` — should expand permanently (no flyout needed)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

---

## Self-Review

**Spec coverage:** The spec has one requirement — button should not jump on hover-peek. Task 1 implements it in JS, Task 2 ensures the button is visible after the JS fix. Task 3 ships it. ✓

**Placeholder scan:** No TBDs, no "add appropriate X" phrases, all code blocks are complete. ✓

**Type consistency:** `syncSidebarToggleDock` is referred to by the same name across JS and this doc. `hide_sidebar`, `doc-nav-flyout-open`, `.left-nav-collapsed-slot` match the class names in the actual codebase. ✓
