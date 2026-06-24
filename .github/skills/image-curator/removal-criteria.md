# Redundant image removal criteria

Canonical sources (defer to these over this summary):

| Source | Use for |
|--------|---------|
| [`writing_style_guide.md`](../../../docs/contributing/style_guide/writing_style_guide.md) | Alt text, redundant visuals, media formatting |
| [`image_style_guide.md`](../../../docs/contributing/style_guide/image_style_guide.md) | Cropping, placement, embedded text |
| [`images.md`](../../../docs/contributing/content_management/images.md) | Authoring policy |

## Remove (high confidence)

Images that add little or no information beyond what prose should carry:

| Category | Examples | Why remove |
|----------|----------|------------|
| **Action buttons only** | Save, Cancel, Submit, Done, OK, Close | Describe the action in a step; no unique UI to show |
| **Home / landing pages** | Dashboard home, channel overview with no highlighted control | Navigation can be one sentence (`Go to **Messaging** > **Email**`) |
| **Full-page chrome** | Entire dashboard, header + sidebar, browser frame, URL bar | Style guide: crop tightly; explain nav in text |
| **Redundant with prose** | Alt duplicates the previous paragraph; decorative screenshot after numbered steps | Style guide: blank alt when redundant; prefer prose for screen-reader users |
| **Terminal / code as image** | Screenshot of terminal output or code | Use fenced code blocks instead |
| **Outdated UI** | Deprecated feature, removed nav item, old branding with no instructional value | Replace with updated copy or delete if steps are obsolete |

## Keep (do not remove)

| Category | Why keep |
|----------|----------|
| **Unique UI placement** | Shows where a control lives when prose alone is ambiguous |
| **Complex workflows** | Multi-step builder states, drag-and-drop layouts, comparison do/don't pairs |
| **Diagrams and architecture** | Concepts that are hard to describe in text alone |
| **Style guide examples** | `assets/img/contributing/style_guide/**` — teaching images |
| **Protected paths** | `logos/`, `braze_icons/`, `icons/` |
| **Partner co-marketing** | Unless explicitly deprecated; flag for human review |

## Filename and alt signals

Flag for review when **filename** or **alt text** suggests:

- `save`, `cancel`, `submit`, `home_page`, `homepage`, `landing`, `overview`, `full_page`, `entire_dashboard`, `browser_frame`, `left_nav`, `sidebar`, `header_only`
- Alt starts with “A screenshot of…” and the body already states the same navigation
- Alt describes only a standard button with no surrounding instructional value

## OCR signals

When Tesseract is available (`scripts/check_screenshot_pii.py` uses the same binary):

- Very short OCR text that is only a button label → candidate for removal
- OCR shows mostly nav chrome with no highlighted feature → candidate for removal
- OCR reveals steps or field labels not in prose → **keep** and merge missing detail into text instead of deleting

## Prose absorption rules

**Default: delete the image reference only.** Merging alt text into prose is the exception, not the rule. When the image is redundant, its alt text is usually redundant too.

### Alt merge gate (required before any merge)

Evaluate alt text **before** editing. Merge only when **all** of the following are true:

1. **New information** — Alt or OCR states a navigation path, control label, or setting name that does **not** already appear in the same step, the previous step, or the surrounding paragraph.
2. **Same step** — The image sits on the step or paragraph you are editing. **Never** append alt text to a *different* numbered step (for example, do not merge step 3’s alt into step 2).
3. **Not a visual echo** — Alt does not merely restate what the prose already tells the reader to do (for example, prose says “select **Account Overview**” and alt says “navigation with Account Overview selected”).
4. **List integrity** — Numbered and bulleted lists keep correct sequence and one instruction per step after the edit.

If any check fails → **remove the image line only**; leave prose unchanged.

### Redundant alt patterns (delete image, do not merge)

| Alt pattern | Prose already says | Action |
|-------------|-------------------|--------|
| “The navigation with **Account Overview** selected.” | “select your **Account Overview**” on the same step | Delete image; keep step text |
| “**Save** button highlighted” | “Select **Save**.” | Delete image only |
| “Screenshot of the dashboard home page” | “Open the dashboard.” | Delete image only |
| “A screenshot of…” + rest duplicates nearby text | Same facts in steps above | Delete image only |

### Anti-pattern

**Before (step 3 has redundant nav screenshot):**

```markdown
2. Select the ad account you are having issues with.
3. In the navigation, select your **Account Overview**. <br> ![The navigation with Account Overview selected.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
```

**Wrong** — alt merged into step 2:

```markdown
2. Select the ad account you are having issues with. The navigation with Account Overview selected.
```

**Correct** — image removed; step 3 prose unchanged:

```markdown
2. Select the ad account you are having issues with.
3. In the navigation, select your **Account Overview**.
```

### When merge is appropriate

Merge only when alt/OCR adds facts **missing** from prose — for example, a field label visible in the screenshot that is not named in the step text, and removing the image would leave readers without that label.

### Edit checklist

1. Read the image (vision), alt text, and 3–5 lines before/after the reference.
2. Run the [alt merge gate](#alt-merge-gate-required-before-any-merge).
3. Remove the image line (and inline `<br>` before it when the step text is complete without the image).
4. If the gate passes, add **one** short sentence to the **same** step or paragraph — never to a prior step.
5. Follow [`braze-docs`](../braze-docs/SKILL.md) voice: imperative steps, sentence case, no “screenshot of”.
6. Confirm list numbering is intact; renumber if a step becomes empty.
7. Run `./bdocs fblinks` on touched files.

## Relationship to image-pruner

| Skill | Removes |
|-------|---------|
| **image-pruner** | Unreferenced binaries under `assets/img/` (all locales) |
| **image-curator** (this skill) | Referenced but redundant images in English docs; may delete binaries after dereferencing |

Run **image-curator** before or between **image-pruner** batches so prose is updated before orphan scans.
