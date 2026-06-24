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

When removing an image:

1. Read the image (vision), alt text, and 3–5 lines before/after the reference.
2. If prose already covers the image, delete the reference only.
3. If alt or OCR adds navigation or labels missing from prose, add one short sentence to the nearest paragraph or step list item.
4. Follow [`braze-docs`](../braze-docs/SKILL.md) voice: imperative steps, sentence case, no “screenshot of”.
5. Do not leave empty paragraphs or broken list numbering.
6. Run `./bdocs fblinks` on touched files.

## Relationship to image-pruner

| Skill | Removes |
|-------|---------|
| **image-pruner** | Unreferenced binaries under `assets/img/` (all locales) |
| **image-curator** (this skill) | Referenced but redundant images in English docs; may delete binaries after dereferencing |

Run **image-curator** before or between **image-pruner** batches so prose is updated before orphan scans.
