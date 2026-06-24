# Curation batch workflow

Use this workflow for manual `@image-curator` runs and when reviewing CI draft PRs.

## Progress checklist

```
Task progress:
- [ ] 1. Scan candidates
- [ ] 2. Review CSV (high → medium)
- [ ] 3. Apply edits in batches (≤25 per PR)
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

## Step 2: Review candidates

Sort CSV by `confidence` (high first). For each row:

1. Open `source_file` at `line_number`.
2. Read the image file (`image_path`) with vision; compare to alt text and OCR snippet.
3. Apply rules in [removal-criteria.md](removal-criteria.md).
4. **High** — safe for automated batch or agent removal after quick spot-check.
5. **Medium** — agent must read image + prose; skip if the screenshot shows a non-obvious control location.
6. **Low** — skip unless user asked for aggressive cleanup.

Skip when:

- Open PR touches the same file or image path.
- Image is under `assets/img/contributing/style_guide/`.
- `_lang/` still needs the binary (do not edit locales; binary may remain referenced there).

## Step 3: Apply edits

For each approved candidate:

1. Run the [alt merge gate](../removal-criteria.md#alt-merge-gate-required-before-any-merge) if you plan to edit prose (most removals skip this).
2. Remove the markdown/HTML/Liquid image line (and optional `{: style=...}` suffix on the same line). Remove a trailing `<br>` on the same line when the step text is complete without the image.
3. **Do not append alt text** unless the gate passes on the **same** step or paragraph.
4. Follow [`braze-docs`](../braze-docs/SKILL.md) for lists, alerts, and UI labels (`**bold**` for controls).
5. Re-read the edited block and confirm numbered steps are sequential and no step lost its instruction.

**Batch size:** ≤ **25** image removals per PR (prose edits need human review).

### CI / automated batch review

The maintenance script removes image references **only** — it does not merge alt text. When reviewing draft `[IC]` PRs, reject any hunk that:

- Appends alt text or image captions to prose (`Stensul Save Options.`, `Home dashboard in Braze.`, `Expand.`)
- Merges alt into a **different** numbered step, list item, or paragraph than the image was on
- Collapses or skips step numbers

Revert those hunks to **delete-image-only** per [removal-criteria.md](../removal-criteria.md#anti-pattern-alt-appended-to-wrong-line).

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

Spot-check 3–5 edited pages in preview if available.

## Step 6: Open draft PR

- **Title:** `[IC] Remove N redundant image references from English docs` — adjust `N` and add a short qualifier when helpful (for example `…from email channel docs`).
- **Label:** `image pruning` (required — same as image-pruner).
- **Body:** Must include an **Image Pruning** section stating this PR removes redundant **references** and updates prose; list scan command, count of references removed, count of binaries deleted, and note English-only scope.
- **Draft:** Yes for scheduled/CI batches; manual runs may be draft or ready for review per user preference.
- Do not mix image curation with script/skill changes in one PR.

```bash
gh pr create --draft \
  --title "[IC] Remove 12 redundant image references from English docs" \
  --label "image pruning" \
  --body "$(cat <<'EOF'
## Image Pruning

This PR is for **Image Pruning**: removes 12 redundant image references from English docs and merges alt text into surrounding prose where needed.

## Scan

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py --min-confidence medium
```

- References removed: 12
- Image files deleted (unreferenced after edit): 8
- Scope: `_docs/`, `_includes/` only
EOF
)"
```

Assign per `CODEOWNERS`; if none, `@braze-inc/docs-team`.
