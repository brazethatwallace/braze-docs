---
name: image-curator
description: >
  Finds redundant, outdated, or unneeded images still referenced in English docs
  (_docs/, _includes/). Removes image references, absorbs alt/OCR content into
  prose per the style guide, and deletes dereferenced binaries. Targets Save
  buttons, home pages, full dashboards, and other low-value screenshots. Use for
  image curation, redundant screenshot cleanup, or @image-curator. Complements
  @image-pruner (unreferenced files). Scheduled twice yearly via CI; also runs manually.
---

# Image curator

Remove **referenced but redundant** images from English canonical docs. Unlike [`image-pruner`](../image-pruner/SKILL.md), which deletes **unreferenced** binaries, this skill edits markdown, updates surrounding prose, and may delete image files only after dereferencing.

**Canonical scanner:** [`scripts/image-curator/find_redundant_image_candidates.py`](../../../scripts/image-curator/find_redundant_image_candidates.py)

**Removal criteria:** [removal-criteria.md](removal-criteria.md) (from [`writing_style_guide.md`](../../../docs/contributing/style_guide/writing_style_guide.md) and [`image_style_guide.md`](../../../docs/contributing/style_guide/image_style_guide.md))

**Scope:** `_docs/` and root `_includes/` only. Do **not** edit `_lang/` unless the user explicitly requests locale work.

**Never curate:** `assets/img/logos/`, `assets/img/braze_icons/`, `assets/img/icons/`, `assets/img/contributing/style_guide/**`.

---

## Scheduled maintenance (CI)

Skills do not run on a schedule. **Twice-yearly maintenance** is handled by GitHub Actions:

| Item | Detail |
|------|--------|
| Workflow | [`.github/workflows/image-curator-maintenance.yml`](../../../.github/workflows/image-curator-maintenance.yml) |
| Batch script | [`scripts/image-curator/run_curation_batch.py`](../../../scripts/image-curator/run_curation_batch.py) |
| Schedule | **June 1** and **December 1** at 14:00 America/New_York (4 hours after image-pruner) |
| Branch | `develop` |
| What CI does | Scan high-confidence candidates; remove up to **25** references per run; open a **draft** `[IC]` PR |
| Human review | **Merge the draft PR** after reviewing prose edits and deletions |

CI applies rule-based prose merge (alt text → sentence). Medium/low confidence candidates stay for manual `@image-curator` runs.

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

See [removal-criteria.md](removal-criteria.md) for the full matrix.

---

## Workflow

Load and follow [workflows/curation-batch.md](workflows/curation-batch.md).

### Quick start (agent)

1. **Scan** — Run the candidate finder; read the CSV.
2. **Review** — Open each high/medium candidate; read the image file (vision), alt text, and surrounding markdown.
3. **Edit** — Remove the reference; merge missing facts from alt/OCR into prose ([`braze-docs`](../braze-docs/SKILL.md) style).
4. **Delete** — Remove binaries only when `rg` shows zero references repo-wide.
5. **Verify** — `./bdocs fblinks`
6. **PR** — Draft `[IC]` PR with label `image pruning`.

### Automated high-confidence batch (CI or local)

```bash
python3 scripts/image-curator/find_redundant_image_candidates.py \
  --csv scripts/image-curator/redundant_image_candidates.csv \
  --min-confidence high

IMAGE_CURATION_DELETE_FORCE=1 python3 scripts/image-curator/run_curation_batch.py --limit 25
```

Requires `IMAGE_CURATION_DELETE_FORCE=1`. Default cap: **25** edits per run.

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
2. **Read every image** you remove (vision + alt + OCR). Absorb non-redundant facts into prose.
3. **English only** — `_docs/`, `_includes/`. Leave `_lang/` alone; binaries may remain referenced there.
4. **Batch ≤ 25** removals per PR.
5. **Do not curate style-guide teaching images** under `assets/img/contributing/style_guide/`.
6. **Run `./bdocs fblinks`** after edits.
7. **Label `image pruning`** on every curation PR.
8. **Follow [`screenshot-pii-audit`](../screenshot-pii-audit/SKILL.md)** if you add replacement screenshots.

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
