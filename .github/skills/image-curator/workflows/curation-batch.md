# Curation batch workflow

For manual `@image-curator` runs and CI draft PR review. Criteria: [removal-criteria.md](../removal-criteria.md).

## Checklist

```
- [ ] 1. Scan candidates
- [ ] 2. Review CSV (high → medium)
- [ ] 3. Apply edits (≤15 per PR, delete-image-only)
- [ ] 4. Delete dereferenced binaries
- [ ] 5. Verify links
- [ ] 6. Open draft PR
```

## Step 1: Scan

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py \
  --csv scripts/image-curator/redundant_image_candidates.csv \
  --min-confidence medium
```

Add `--no-ocr` for a faster scan. CI uses `--min-confidence high` only.

## Step 2: Review

For each CSV row (high first):

1. Open `source_file` at `line_number`.
2. Read `image_path` with vision; compare alt and OCR snippet to prose.
3. Apply [removal-criteria.md](../removal-criteria.md).
4. **High** — OK for CI batch after spot-check (check `reasons` for corroboration).
5. **Medium** — vision review required; skip non-obvious placement, builder UI, table icons.
6. **Low** — skip (see skip-reason table in removal-criteria).

Also skip when an open PR touches the same file, `_lang/` still references the binary, or a page has multiple images and the candidate path does not match exactly.

## Step 3: Apply edits

1. **Delete-image-only** — remove the image line (and inline `{: style=...}` on the same line). Drop a trailing `<br>` when the step is complete without the image.
2. Do **not** append alt text unless the [alt merge gate](../removal-criteria.md#alt-merge-gate-required-before-any-merge) passes on the **same** step.
3. Do **not** mix heading-level or unrelated prose edits in the same `[IC]` PR.
4. Re-read the block; confirm numbered steps are intact.

Reject CI hunks that violate [anti-patterns](../removal-criteria.md#anti-patterns).

## Step 4: Delete binaries

```bash
rg -F 'assets/img/path/to/file.png' _docs _includes _lang docs _layouts _plugins assets/css assets/js
```

Delete under `assets/img/` only when the search returns no hits. Do not delete `assets/img_archive/` unless explicitly requested.

## Step 5: Verify

```bash
./bdocs fblinks
```

Spot-check partner pages, landing-page builder docs, Administer settings pages, and multi-image steps.

## Step 6: Open draft PR

| Field | Value |
|-------|-------|
| Title | `[IC] Remove N redundant image references from English docs` — `N` from `git diff develop` |
| Label | `image pruning` |
| Body | **Image Pruning** section: delete-image-only; scan command; reference count; binaries deleted; English-only |

```bash
gh pr create --draft \
  --title "[IC] Remove 12 redundant image references from English docs" \
  --label "image pruning" \
  --body "$(cat <<'EOF'
## Image Pruning

Removes 12 redundant image references from English docs (delete-image-only).

- Scan: `python3 scripts/image-curator/find_redundant_image_candidates.py --min-confidence high`
- References removed: 12
- Image files deleted: 0
- Scope: `_docs/`, `_includes/` only
EOF
)"
```

Assign per `CODEOWNERS`; if none, `@braze-inc/docs-team`.
