---
name: image-curator
description: >
  Finds redundant, outdated, or unneeded images still referenced in English docs
  (_docs/, _includes/). Removes image references (delete-image-only by default),
  and deletes dereferenced binaries when safe. Use for image curation,
  redundant screenshot cleanup, or /image-curator from chat. Complements
  braze-docs:image-pruner. Scheduled twice yearly via CI; also runs manually.
---

# Image curator

Remove **referenced but redundant** images from English canonical docs. Unlike [`image-pruner`](../image-pruner/SKILL.md), which deletes **unreferenced** binaries, this skill edits markdown and may delete image files only after dereferencing.

| Resource | Path |
|----------|------|
| Scanner | [`scripts/image-curator/find_redundant_image_candidates.py`](../../../scripts/image-curator/find_redundant_image_candidates.py) |
| Batch script | [`scripts/image-curator/run_curation_batch.py`](../../../scripts/image-curator/run_curation_batch.py) |
| Removal criteria | [removal-criteria.md](removal-criteria.md) |
| Workflow | [workflows/curation-batch.md](workflows/curation-batch.md) |
| Style sources | [`writing_style_guide.md`](../../../docs/contributing/style_guide/writing_style_guide.md), [`image_style_guide.md`](../../../docs/contributing/style_guide/image_style_guide.md) |

**Scope:** `_docs/` and root `_includes/` only. Do **not** edit `_lang/` unless the user explicitly requests locale work.

**Never curate:** `assets/img/logos/`, `assets/img/braze_icons/`, `assets/img/icons/`, `assets/img/contributing/style_guide/**`, **`_docs/_partners/**`** (manual review only).

---

## Scheduled maintenance (CI)

| Item | Detail |
|------|--------|
| Workflow | [`.github/workflows/image-curator-maintenance.yml`](../../../.github/workflows/image-curator-maintenance.yml) |
| Schedule | **June 1** and **December 1** at 14:00 America/New_York |
| Branch | `develop` |
| Batch | Up to **15** high-confidence removals per run; **delete-image-only**; opens a **draft** `[IC]` PR |
| Review | Merge the draft PR after diff review. Skips if another open `[IC]` PR exists. |

Manual runs: GitHub Actions *workflow_dispatch*, or `/image-curator` from chat for medium-confidence and vision review.

| After curation | Use |
|----------------|-----|
| Nuanced screenshots | `braze-docs:image-curator` with vision on each candidate |
| Orphan binaries | [`image-pruner`](../image-pruner/SKILL.md) on a follow-up PR |

---

## Workflow

Load [workflows/curation-batch.md](workflows/curation-batch.md). Summary:

1. **Scan** — `find_redundant_image_candidates.py`; read the CSV.
2. **Review** — Vision + alt + prose per [removal-criteria.md](removal-criteria.md). CI uses **high** only; manual runs review **medium**.
3. **Edit** — Remove the image reference only. Prose changes are rare; pass the [alt merge gate](removal-criteria.md#alt-merge-gate-required-before-any-merge) first.
4. **Delete** — Binaries only when `rg` shows zero references repo-wide.
5. **Verify** — `./bdocs fblinks`
6. **PR** — Draft `[IC]` with label `image pruning`. Count removals from `git diff develop`, not batch output.

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py \
  --csv scripts/image-curator/redundant_image_candidates.csv \
  --min-confidence high

IMAGE_CURATION_DELETE_FORCE=1 python3 scripts/image-curator/run_curation_batch.py --limit 15 --csv scripts/image-curator/redundant_image_candidates.csv
```

Do not mix curation doc edits with script/skill changes in one PR.

---

## Pull request conventions

| Field | Value |
|-------|-------|
| Title prefix | `[IC]` (not `[IP]` — that is [`image-pruner`](../image-pruner/SKILL.md)) |
| Title example | `[IC] Remove 12 redundant image references from English docs` |
| Label | `image pruning` (required) |
| Body | **Image Pruning** section: delete-image-only; scan command; reference count; binaries deleted; English-only scope |

---

## Agent rules

1. **Scan before editing.** Check repo-wide references; do not curate one page in isolation.
2. **Delete-image-only by default.** Read each image (vision + alt). Never append alt to a different step, list item, or paragraph.
3. **English only** — `_docs/`, `_includes/`. Leave `_lang/` alone.
4. **Batch ≤ 15** per PR unless batch precision is verified.
5. **Follow [removal-criteria.md](removal-criteria.md)** for keep/remove categories, confidence tiers, and scanner skip reasons.
6. **Reject CI hunks** that merge alt into prose, remove the wrong image on multi-image steps, or change unrelated headings.
7. **Follow [`screenshot-pii-audit`](../screenshot-pii-audit/SKILL.md)** if you add replacement screenshots.

---

## Example prompts

Contributor chat (Cursor):

```
/image-curator Scan for redundant settings and home-page screenshots in _docs/_user_guide/administer/.
```

```
/image-curator Review the draft [IC] PR from CI maintenance.
```

```
/image-curator Remove approved medium-confidence candidates from the latest CSV.
```
