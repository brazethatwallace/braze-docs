# Curation batch workflow

Use this workflow for manual `@image-curator` runs and when reviewing CI draft PRs.

## Progress checklist

```
Task progress:
- [ ] 1. Scan candidates
- [ ] 2. Review CSV (high → medium)
- [ ] 3. Apply edits in batches (≤15 per PR)
- [ ] 4. Delete dereferenced binaries
- [ ] 5. Verify links and prose
- [ ] 6. Open draft PR
```

## Step 1: Scan

From repo root on `develop` (or a branch that includes latest English docs):

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py \
  --csv scripts/image-curator/redundant_image_candidates.csv \
  --min-confidence medium
```

Optional faster scan (no Tesseract):

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py --no-ocr --min-confidence medium
```

CI processes **high** confidence only. Manual runs should review **medium** candidates with vision before removal.

## Step 2: Review candidates

Sort CSV by `confidence` (high first). For each row:

1. Open `source_file` at `line_number`.
2. Read the image file (`image_path`) with vision; compare to alt text and OCR snippet.
3. Apply rules in [removal-criteria.md](removal-criteria.md).
4. **High** — safe for automated batch after spot-check (requires corroborating signals in CSV `reasons` column).
5. **Medium** — agent must read image + prose; skip if the screenshot shows a non-obvious control location, builder UI, or table icon.
6. **Low** — skip unless user asked for aggressive cleanup.

Skip when `reasons` includes:

| Reason | Meaning |
|--------|---------|
| `partner_page_skip` | Technology Partner page |
| `diagram_or_workflow` | Diagram, data flow, or process graphic |
| `builder_editor_ui` | Landing page / editor instructional UI |
| `reference_table_icon` | Icon in a markdown table (for example `deep_links.md`) |
| `third_party_console` | GCP / AWS / Infobip navigation screenshot |
| `metric_chart_example` | Metric tile or chart layout |
| `instructional_placement` | Pencil icon, permissions panel, or similar placement shot |

Also skip when:

- Open PR touches the same file or image path.
- Image is under `assets/img/contributing/style_guide/`.
- `_lang/` still needs the binary (do not edit locales; binary may remain referenced there).
- The page has **multiple images** and the candidate path does not exactly match the intended removal.

## Step 3: Apply edits

For each approved candidate:

1. Run the [alt merge gate](../removal-criteria.md#alt-merge-gate-required-before-any-merge) if you plan to edit prose (most removals skip this).
2. Remove the markdown/HTML/Liquid image line (and optional `{: style=...}` suffix on the same line). Remove a trailing `<br>` on the same line when the step text is complete without the image.
3. **Do not append alt text** unless the gate passes on the **same** step or paragraph.
4. Follow [`braze-docs`](../braze-docs/SKILL.md) for lists, alerts, and UI labels (`**bold**` for controls).
5. Re-read the edited block and confirm numbered steps are sequential and no step lost its instruction.
6. **Do not mix unrelated edits** (heading level changes, prose rewrites) in the same `[IC]` PR.

**Batch size:** ≤ **15** image removals per PR (CI default; prose edits need human review).

### CI / automated batch review

The maintenance script removes image references **only** — it does not merge alt text. When reviewing draft `[IC]` PRs, reject any hunk that:

- Appends alt text or image captions to prose (`Stensul Save Options.`, `Home dashboard in Braze.`, `Expand.`)
- Merges alt into a **different** numbered step, list item, or paragraph than the image was on
- Collapses or skips step numbers
- Removes the **wrong image** on a step that has multiple `image_buster` references
- Changes heading levels or unrelated prose

Revert those hunks to **delete-image-only** per [removal-criteria.md](../removal-criteria.md#anti-pattern-alt-appended-to-wrong-line).

### Lessons from test PR #14293

Before merge, confirm:

1. **Partner pages** (`_docs/_partners/`) — no image removals unless explicitly approved
2. **Landing page builder docs** — only `*-homepage.png`-style list shots removed; editor/workflow images kept
3. **`braze_pilot/deep_links.md`** — icon table intact
4. **Diagrams** — `user_profile_process3.png`, `churn_overview.png`, `tealium_overview.png`, and similar kept
5. **GCP / third-party console** navigation screenshots kept; save/cancel-only shots reviewed individually
6. **PR title count** matches `git diff develop` image removals, not batch script output

## Step 4: Delete binaries

After removing English references, check whether the image is still referenced anywhere:

```bash
rg -F 'assets/img/path/to/file.png' _docs _includes _lang docs _layouts _plugins assets/css assets/js
```

Delete the file under `assets/img/` only when the search returns no hits. Do **not** delete `assets/img_archive/` files from this workflow unless the user explicitly requests archive cleanup.

## Step 5: Verify

```bash
./bdocs fblinks
```

Spot-check 3–5 edited pages in preview if available. Pay extra attention to partner pages, landing page builder docs, and multi-image steps.

## Step 6: Open draft PR

- **Title:** `[IC] Remove N redundant image references from English docs` — set `N` from `git diff develop` (count removed `image_buster` lines), not from the batch script alone.
- **Label:** `image pruning` (required — same as image-pruner).
- **Body:** Must include an **Image Pruning** section stating this PR removes redundant **references** (delete-image-only); list scan command, count of references removed, count of binaries deleted, and note English-only scope.
- **Draft:** Yes for scheduled/CI batches; manual runs may be draft or ready for review per user preference.
- Do not mix image curation with script/skill changes in one PR.

```bash
gh pr create --draft \
  --title "[IC] Remove 12 redundant image references from English docs" \
  --label "image pruning" \
  --body "$(cat <<'EOF'
## Image Pruning

This PR removes 12 redundant image references from English docs (delete-image-only; no alt merged into prose).

## Scan

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py --min-confidence high
```

- References removed: 12
- Image files deleted (unreferenced after edit): 0
- Scope: `_docs/`, `_includes/` only
EOF
)"
```

Assign per `CODEOWNERS`; if none, `@braze-inc/docs-team`.
