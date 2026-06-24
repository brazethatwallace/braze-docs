---
name: image-curator
description: >
  Finds redundant, outdated, or unneeded images still referenced in English docs
  (_docs/, _includes/). Removes image references (delete-image-only by default),
  and deletes dereferenced binaries when safe. Targets home/list-page chrome,
  save/cancel-only shots, and other low-value screenshots. Use for image
  curation, redundant screenshot cleanup, or @image-curator. Complements
  @image-pruner (unreferenced files). Scheduled twice yearly via CI; also runs manually.
---

# Image curator

Remove **referenced but redundant** images from English canonical docs. Unlike [`image-pruner`](../image-pruner/SKILL.md), which deletes **unreferenced** binaries, this skill edits markdown, updates surrounding prose, and may delete image files only after dereferencing.

**Canonical scanner:** [`scripts/image-curator/find_redundant_image_candidates.py`](../../../scripts/image-curator/find_redundant_image_candidates.py)

**Removal criteria:** [removal-criteria.md](removal-criteria.md) (from [`writing_style_guide.md`](../../../docs/contributing/style_guide/writing_style_guide.md) and [`image_style_guide.md`](../../../docs/contributing/style_guide/image_style_guide.md))

**Scope:** `_docs/` and root `_includes/` only. Do **not** edit `_lang/` unless the user explicitly requests locale work.

**Never curate:** `assets/img/logos/`, `assets/img/braze_icons/`, `assets/img/icons/`, `assets/img/contributing/style_guide/**`, **`_docs/_partners/**`** (Technology Partner pages — manual review only).

---

## Scheduled maintenance (CI)

Skills do not run on a schedule. **Twice-yearly maintenance** is handled by GitHub Actions:

| Item | Detail |
|------|--------|
| Workflow | [`.github/workflows/image-curator-maintenance.yml`](../../../.github/workflows/image-curator-maintenance.yml) |
| Batch script | [`scripts/image-curator/run_curation_batch.py`](../../../scripts/image-curator/run_curation_batch.py) |
| Schedule | **June 1** and **December 1** at 14:00 America/New_York (4 hours after image-pruner) |
| Branch | `develop` |
| What CI does | Scan high-confidence candidates; remove up to **15** references per run; open a **draft** `[IC]` PR |
| Human review | **Merge the draft PR** after reviewing prose edits and deletions |

CI opens draft `[IC]` PRs with **delete-image-only** edits. The batch script does not merge alt text. Review diffs for any prose change beyond image removal; revert hunks that append alt fragments.

CI skips opening a new batch when another open `[IC]` PR already exists (merge or close it first).

### Manual runs

- **GitHub Actions:** *Actions → Image curator (maintenance) → Run workflow* (`workflow_dispatch`).
- **Cursor / agents:** `@image-curator` for full vision review, medium-confidence batches, or ad-hoc cleanup.

### Division of labor

| Trigger | Who acts |
|---------|----------|
| Scheduled run (Jun/Dec) | CI opens draft `[IC]` PR for high-confidence batch |
| Draft PR opened by CI | Docs team reviews prose + diff, then merges |
| Nuanced screenshots | `@image-curator` manual run with vision on each image |
| Orphan binaries after curation | `@image-pruner` on a follow-up PR |

---

## What to remove

Per the style guide, prefer prose over images when the screenshot shows:

- **Save / Cancel / Submit** buttons with no unique UI context
- **Home, landing, or overview** pages explainable in one navigation sentence
- **Full dashboard, header, sidebar, or browser chrome**
- **Terminal output or code** (use code fences)
- **Redundant visuals** where alt text duplicates existing steps

**Do not remove** from automated batches:

- **Technology Partner screenshots** (`_docs/_partners/`) — partner UIs are usually instructional
- **Diagrams and workflows** — integration graphics, data flows, architecture overviews, process diagrams
- **Builder / editor UI** — landing page drag-and-drop panels, form blocks, toggles, personalization dialogs
- **Reference table icons** — markdown tables where images illustrate constants (for example `braze_pilot/deep_links.md`)
- **Third-party admin consoles** — GCP, AWS, Azure, Infobip navigation (save/cancel-only shots on those pages may still be removable)
- **Metric and chart examples** — metric tiles, trend lines, and chart layouts on dashboard pages

See [removal-criteria.md](removal-criteria.md) for the full matrix.

---

## Workflow

Load and follow [workflows/curation-batch.md](workflows/curation-batch.md).

### Quick start (agent)

1. **Scan** — Run the candidate finder; read the CSV.
2. **Review** — Open each high/medium candidate; read the image file (vision), alt text, and surrounding markdown.
3. **Edit** — Remove the reference only. Do **not** append alt text unless you manually pass the [alt merge gate](removal-criteria.md#alt-merge-gate-required-before-any-merge) ([`braze-docs`](../braze-docs/SKILL.md) style).
4. **Delete** — Remove binaries only when `rg` shows zero references repo-wide.
5. **Verify** — `./bdocs fblinks`
6. **PR** — Draft `[IC]` PR with label `image pruning`.

### Automated high-confidence batch (CI or local)

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py \
  --csv scripts/image-curator/redundant_image_candidates.csv \
  --min-confidence high

IMAGE_CURATION_DELETE_FORCE=1 python3 scripts/image-curator/run_curation_batch.py --limit 15
```

Requires `IMAGE_CURATION_DELETE_FORCE=1`. Default cap: **15** edits per run (raised only after human review of batch precision).

---

## Pull request conventions

Same program as image-pruner; different title prefix to avoid collision with `[IP] Remove N unreferenced images` PRs.

| Field | Value |
|-------|-------|
| Title prefix | `[IC]` |
| Title example | `[IC] Remove 12 redundant image references from English docs` |
| Label | `image pruning` (required) |
| Body | **Image Pruning** section; state reference removal + prose updates; English-only scope |

Do not mix curation edits with script/skill changes in one PR.

---

## Agent rules

1. **Always scan before editing.** Use the candidate script; do not delete images from a single page in isolation without checking repo-wide references.
2. **Read every image** you remove (vision + alt + OCR). **Delete the image only** by default. Never append alt text to a prior step, list item, or paragraph. Merge alt only when you manually pass the [alt merge gate](removal-criteria.md#alt-merge-gate-required-before-any-merge) on the **same** line or step.
3. **English only** — `_docs/`, `_includes/`. Leave `_lang/` alone; binaries may remain referenced there.
4. **Batch ≤ 15** removals per PR (CI default; increase only when batch precision is verified).
5. **Do not curate style-guide teaching images** under `assets/img/contributing/style_guide/`.
6. **Skip `_docs/_partners/`** in automated batches; partner screenshots need human review before removal.
7. **Never auto-remove diagrams, workflows, builder UI, table icons, or third-party console navigation** — see [removal-criteria.md](removal-criteria.md).
8. **High confidence requires corroboration** — two signals (filename + alt, filename + OCR, and so on). Filename-only `save`/`landing` hits are medium at most.
9. **Run `./bdocs fblinks`** after edits.
10. **Label `image pruning`** on every curation PR.
11. **Follow [`screenshot-pii-audit`](../screenshot-pii-audit/SKILL.md)** if you add replacement screenshots.
12. **Review CI draft PRs** for bad alt merges, wrong-image removal on multi-image steps, and unrelated prose/heading edits. Revert to delete-image-only per [anti-pattern](removal-criteria.md#anti-pattern). Reject partner-page, diagram, or builder removals.
13. **Count PR removals from `git diff develop`** for the title — not from the batch script output alone.

---

## Example prompts

```
@image-curator Scan for redundant Save button and home page screenshots in _docs/.
```

```
@image-curator The maintenance workflow opened a draft [IC] PR — help review the prose edits.
```

```
@image-curator Remove medium-confidence candidates from the latest CSV after I approve the list.
```
