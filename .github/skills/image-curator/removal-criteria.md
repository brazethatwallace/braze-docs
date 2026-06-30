# Redundant image removal criteria

Defer to the style guide over this summary:

| Source | Use for |
|--------|---------|
| [`writing_style_guide.md`](../../../docs/contributing/style_guide/writing_style_guide.md) | Alt text, redundant visuals, media formatting |
| [`image_style_guide.md`](../../../docs/contributing/style_guide/image_style_guide.md) | Cropping, placement, embedded text |
| [`images.md`](../../../docs/contributing/content_management/images.md) | Authoring policy |

## Confidence tiers

The scanner assigns **high**, **medium**, or **low**. Filename-only hits are **medium** at most.

| Tier | Rule | Who acts |
|------|------|----------|
| **High** | Two or more corroborating removal signals (for example `filename_list_home_chrome` + `alt_describes_redundant_ui`) | CI batch after spot-check |
| **Medium** | One removal signal | Vision review before removal |
| **Low** | Skip reason below, or no removal signal | Do not auto-remove |

CI processes **high** only, capped at **15** references per run.

### Scanner skip reasons (low — do not auto-remove)

| Reason | Keep when |
|--------|-----------|
| `partner_page_skip` | Source is `_docs/_partners/` |
| `diagram_or_workflow` | Diagram, data flow, architecture, or process graphic |
| `builder_editor_ui` | Landing page / editor instructional UI (`dnd.png`, `form.png`, etc.) |
| `reference_table_icon` | Image in a markdown table (for example `braze_pilot/deep_links.md`) |
| `third_party_console` | GCP, AWS, Azure, or Infobip navigation screenshot |
| `metric_chart_example` | Metric tile, trend line, or chart layout |
| `settings_field_keep` | Administer modal, field dialog, test preview, or SAML tooling |
| `instructional_placement` | Pencil icon, permissions matrix, or non-obvious control placement |
| `protected_path` | `logos/`, `braze_icons/`, `icons/`, style-guide teaching images |

### Scanner removal signals (review for medium/high)

| Signal | Typical target |
|--------|----------------|
| `filename_list_home_chrome` | `*-homepage.png`, `home_dashboard*`, `export_logs.png`, admin list pages |
| `filename_save_cancel` | Save, cancel, or submit in filename |
| `filename_page_chrome` | Full dashboard, browser frame, sidebar-only shots |
| `alt_describes_redundant_ui` | Alt describes home page, toggle, login screen, or button prose already states |
| `alt_redundant_with_prose` | Alt duplicates surrounding paragraph |
| `alt_settings_overview` | Administer page/list overview (often with `image_before_settings_navigation`) |
| `image_before_settings_navigation` | Image sits above `Go to **Settings**` or `To access this page` |
| `ocr_button_only` / `ocr_mostly_action_button` | OCR is only a button label |

---

## Remove

**Scope:** Braze-owned pages — **not** `_docs/_partners/` without explicit approval.

| Category | Examples | Why |
|----------|----------|-----|
| **Settings / list overview** | Notification Preferences page, exports log list, tag management list | Prose gives **Settings** navigation; image is destination chrome |
| **Home / channel list pages** | `*-homepage.png`, reporting home, credits overview tab | One navigation sentence suffices |
| **Save / Cancel / Submit** | Save-as-template, cancel export, checkbox named in steps | Prose names the control; image adds no placement context |
| **Full-page chrome** | Entire dashboard, header + sidebar, browser frame | Crop tightly or describe in text |
| **Redundant with prose** | Alt duplicates the previous paragraph | Prefer prose for screen-reader users |
| **Terminal / code as image** | Screenshot of terminal output | Use fenced code blocks |
| **Outdated UI** | Deprecated nav or branding | Update copy or delete obsolete steps |

---

## Keep

| Category | Why |
|----------|-----|
| **Unique UI placement** | Prose alone does not show where a control lives |
| **Builder / editor UI** | DnD panels, form blocks, toggles, personalization dialogs |
| **Diagrams and workflows** | Layout and data flow prose cannot replace |
| **Reference table icons** | Image is the reference content in a table cell |
| **Third-party consoles** | External admin UI (GCP, AWS, Infobip) — except redundant save/cancel on those pages |
| **Metric and chart examples** | How data is displayed (for example metric tiles on Home) |
| **Administer field dialogs** | Multi-field modals, email setting fields, locale dialogs, SAML tracer tooling |
| **Technology Partner pages** | Partner product UI — default keep |

### Administer (`_docs/_user_guide/administer/`)

Calibrated from manual curation of the Administer folder.

**Remove:** settings page overviews; images above a Settings navigation sentence; login-screen chrome; toggles/checkboxes/export actions already named in steps; filtered list views when prose describes the filter.

**Keep:** field-level email settings; Edit-button placement (`single_edit_icon.png`); bulk-edit UI; locale dialog windows; test/seed previews; SAML settings toggle and tracer tooling; AWS S3 setup screenshots.

Acceptable non-image edit: reorganize duplicate intro prose into bullets (as in `tags.md`) — not alt appended to the wrong line.

---

## Filename and alt signals

Flag for review:

- `homepage`, `home_dashboard`, `landing-pages-homepage`, `reporting_home`, `export_logs`, `tags_view`
- `save`, `cancel`, `submit` — medium at most unless corroborated
- Alt starts with “A screenshot of…” and body already states the same navigation

Do **not** flag from filename alone: builder assets (`dnd.png`, `form.png`), `*_home_icon.png` in tables, architecture `*_overview.png` (treat as diagram).

## OCR signals

When Tesseract is available:

- Button-only OCR → removal candidate (corroborate before high)
- Nav chrome with no highlighted feature → removal candidate
- Field labels not in prose → **keep**; merge only via [alt merge gate](#alt-merge-gate-required-before-any-merge)

---

## Prose rules (delete-image-only default)

**Default: remove the image line only.** Alt text describes appearance, not action. If the step already instructs the reader, delete the image and leave prose unchanged.

Automated batches and agents **must not** append alt text to existing sentences.

### Alt merge gate (required before any prose edit)

Merge only when **all** are true:

1. **New information** — Alt or OCR names a path, label, or setting **not** already in the same step or adjacent paragraph.
2. **Same step** — Image is on the step or paragraph you edit.
3. **Not a visual echo** — Alt does not restate what prose already says.
4. **List integrity** — Numbered and bulleted lists stay sequential.

If any check fails → delete the image only.

### Anti-patterns

| Mistake | Fix |
|---------|-----|
| Alt merged into a **previous** step, list item, or paragraph | Revert; delete image only |
| Alt caption appended (`Stensul Save Options.`, `Home dashboard in Braze.`) | Delete image only |
| Alt echoes navigation prose on the **same** step (Facebook Account Overview) | Delete image only |
| Step numbers skipped or collapsed after removal | Restore numbering |
| Wrong `image_buster` removed on a multi-image step | Revert; match exact path from CSV |

**Wrong** — alt merged into step 2:

```markdown
2. Select the ad account. The navigation with Account Overview selected.
3. In the navigation, select your **Account Overview**.
```

**Correct:**

```markdown
2. Select the ad account.
3. In the navigation, select your **Account Overview**.
```

### Edit checklist

1. Read image (vision), alt, and 3–5 lines of context.
2. Run the [alt merge gate](#alt-merge-gate-required-before-any-merge) if editing prose.
3. Remove the image line (and trailing `<br>` when the step is complete without it).
4. Confirm list numbering; run `./bdocs fblinks`.

---

## Relationship to image-pruner

| Skill | Removes |
|-------|---------|
| **image-pruner** | Unreferenced binaries under `assets/img/` |
| **image-curator** | Referenced but redundant English references; may delete binaries after dereferencing |

Run **image-curator** before **image-pruner** so prose is updated before orphan scans.
