---
name: image-pruner
description: >
  Finds and removes stale image files under assets/img/ that are not referenced in
  documentation articles (_docs/, _includes/, _lang/), contributing guides (docs/),
  or site chrome (layouts, CSS, plugins). Never touches logos/, braze_icons/, or icons/.
  Use when cleaning up unused screenshots, reducing repo size, image pruning, or when
  the user mentions unreferenced images or image-pruner.
---

# Image pruning

Remove image files under `assets/img/` that no documentation article, contributing guide, or site layout references anymore. This reduces repository size and can improve docs site build and deploy times.

**Canonical scanner:** [`scripts/image-pruner/find_unreferenced_images.py`](../../../scripts/image-pruner/find_unreferenced_images.py)

**Scope:** References in `_docs/`, root `_includes/`, `_lang/`, `docs/` (contributing), plus site chrome (`_layouts/`, `_plugins/`, `assets/css/`, `assets/js/`, root config) keep an image from deletion.

**Never deleted** regardless of references: `assets/img/logos/`, `assets/img/braze_icons/`, and `assets/img/icons/`.

> **Policy note:** [`docs/contributing/content_management/images.md`](../../../docs/contributing/content_management/images.md) tells authors not to delete image files when updating a single page. This workflow is for **intentional repo-wide cleanup** after verifying an image is unreferenced in **all** locales—not for routine article edits.

---

## Scheduled maintenance (CI)

Skills do not run on a schedule. **Twice-yearly maintenance** is handled by GitHub Actions:

| Item | Detail |
|------|--------|
| Workflow | [`.github/workflows/image-pruner-maintenance.yml`](../../../.github/workflows/image-pruner-maintenance.yml) |
| Batch script | [`scripts/image-pruner/run_maintenance_batch.py`](../../../scripts/image-pruner/run_maintenance_batch.py) |
| Schedule | **June 1** and **December 1** at 10:00 America/New_York |
| Branch | `develop` |
| What CI does | Scan; delete up to **100** unreferenced files (secondary verify, open-PR exclusions); open a **draft** `[IP]` PR |
| Human review | **Merge the draft PR** after reviewing the image deletions in the diff |

Each run always executes a delete batch (up to 100 files). CI opens a **draft PR whenever at least one file is deleted**—there is no minimum count. If every candidate is skipped (secondary verify) or the scan finds zero unreferenced images, no PR is opened.

CI skips opening a new batch when another open `[IP] Remove …` PR already exists (merge or close it first, then re-run).

**Maintenance phase** (after bulk cleanup): expect few or no deletable files per run. Known primary-scan false positives (for example `assets/img/Braze Komo Images v2/`) are skipped by secondary verification and never appear in the PR diff. If more than 100 files remain after a PR merges, re-run the workflow or invoke this skill (`braze-docs:image-pruner`) for the next batch.

### Manual runs

- **GitHub Actions:** *Actions → Image pruner (maintenance) → Run workflow* (`workflow_dispatch`).
- **Cursor / agents:** Invoke `braze-docs:image-pruner` for ad-hoc scans and extra `[IP]` batch PRs any time.

### Division of labor

| Trigger | Who acts |
|---------|----------|
| Scheduled run (Jun/Dec) | CI runs batch and opens a draft `[IP]` PR when deletions exist |
| Draft PR opened by CI | Docs team reviews diff and merges (or closes without merging) |
| Spike after a large IA move | Run workflow manually or invoke this skill (`braze-docs:image-pruner`); do not wait for the next scheduled run |
| More than 100 files remain | Merge current PR, then re-run workflow for the next batch |

---

## What counts as a reference

The scanner walks article trees, contributing guides, and site chrome, extracting paths under `assets/img/`:

| Area | Examples |
|------|----------|
| `_docs/`, `_includes/`, `_lang/` | `{% image_buster /assets/img/... %}`, `![alt]({% image_buster ... %})`, relative `../../../assets/img/...`, YAML frontmatter `image:` on landing pages |
| `docs/` | Contributing guides: `![alt](../../../assets/img/contributing/...)` |
| `_layouts/`, `_plugins/` | `<img src="{{site.baseurl}}/assets/img/...">`, alert icons in Liquid plugins |
| `assets/css/`, `assets/js/` | `url(.../assets/img/...)`, copy-button icons in `highlight.js` |
| `_config.yml`, `vercel.json`, `package.json` | Root config references |

**Not scanned:** `_data/`, `.github/` (PR/issue templates), `scripts/`, and agent skill files. Add paths to the allowlist if those trees reference an image.

**Never deleted** regardless of references: anything under `assets/img/logos/`, `assets/img/braze_icons/`, or `assets/img/icons/`.

Supported extensions: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`.

---

## Workflow

### 1. Scan (report only)

From the repo root:

```bash
python3 scripts/image-pruner/find_unreferenced_images.py \
  --csv scripts/image-pruner/unreferenced_images.csv
```

Review the CSV. Sort by directory and use the [high-risk patterns](#high-risk-path-patterns) below. Paths under `logos/`, `braze_icons/`, and `icons/` never appear in the delete list.

### 2. Allowlist exceptions

If an image is required but not detected (dynamic path, external tooling), add one path per line to [`_data/unreferenced_images_allowlist.txt`](../../../_data/unreferenced_images_allowlist.txt):

```text
# Hotlinked from support macros; no static repo reference
assets/img/example_keep_me.svg
```

Re-run the scan after updating the allowlist.

### 3. Delete (explicit force flag)

Only after human review and the [guardrails](#guardrails-before-deleting) below:

```bash
UNREFERENCED_IMAGE_DELETE_FORCE=1 python3 scripts/image-pruner/find_unreferenced_images.py --delete
```

By default, each `--delete` run removes **at most 100** unreferenced files and runs a **secondary reference check** on every candidate before unlinking. Re-run scan + delete until the report shows zero (or an acceptable remainder).

```bash
# Optional: smaller batch for one run (default is 100)
UNREFERENCED_IMAGE_DELETE_FORCE=1 python3 scripts/image-pruner/find_unreferenced_images.py --delete --limit 25
```

Safety defaults:

| Variable | Default | Purpose |
|----------|---------|---------|
| `UNREFERENCED_IMAGE_DELETE_FORCE` | unset | Must be `1` to delete anything |
| `UNREFERENCED_IMAGE_MAX_DELETES` | `100` | Max files deleted per `--delete` run (override with `--limit`) |

For large cleanups, delete in batches of **up to 100 files per PR** rather than one enormous commit.

**Do not use `--no-verify`** unless you have manually confirmed every path in the batch; it skips the secondary text search.

### 4. Verify

After each delete batch:

```bash
python3 scripts/image-pruner/find_unreferenced_images.py
./bdocs fblinks
```

Re-run the scan until `Unreferenced` count stops decreasing or you have reviewed what remains. Optional: local Jekyll build or CI preview to spot-check pages that used heavy imagery.

### 5. Open a PR

Image deletion batches use the **Image Pruning** PR template. Skill/tooling-only changes (script, skill doc) belong on a separate branch—do not mix with image binaries in one PR.

**REQUIRED SUB-SKILL:** Use [create-pr](../create-pr/SKILL.md) (`braze-docs:create-pr`) for Steps 0–1, 3–4, quality checklist, and anti-patterns. **Override Step 2 only** as follows.

#### Step 2 override (image-pruner)

| Field | Value |
|-------|--------|
| **Title** | `[IP] Remove N unreferenced images from assets/img` (prefix is required) |
| **Label** | `image pruning` — `gh pr edit --add-label "image pruning"` after create |
| **Reviewers** | Per `CODEOWNERS`; if none, `braze-inc/docs-team` |

**Body** — use the create-pr template and include:

````markdown
### Why are you making this change? (required)

Remove unreferenced image files to reduce repo size and maintenance burden.

### Image Pruning

This PR is for **Image Pruning**: removes N unreferenced image files (~X MB).

### Scan

```bash
python3 scripts/image-pruner/find_unreferenced_images.py --csv scripts/image-pruner/unreferenced_images.csv
UNREFERENCED_IMAGE_DELETE_FORCE=1 python3 scripts/image-pruner/find_unreferenced_images.py --delete
```

Reference pass included `_lang/`, `docs/`, and site chrome. Excluded: `logos/`, `braze_icons/`, `icons/`.

### Verification

- [ ] Spot-check pages that previously referenced removed images (if any edge cases)
- [ ] Confirm scan commands above reproduce the deletion set

### Contributor checklist

<Copy from create-pr Step 2 — redirects and image-replacement rules usually N/A for pure deletions.>
````

After `--delete`, the script may print a suggested title and body — adapt them into this format when opening the PR.

---

## Guardrails before deleting

Use these in addition to the script’s built-in checks. None alone is sufficient; combine several for safe cleanup.

### Built into the script

1. **Report-only by default** — No files are removed without `--delete` and `UNREFERENCED_IMAGE_DELETE_FORCE=1`.
2. **Article + contributing + site-chrome reference pass** — Regex scan across `_docs/`, `_includes/`, `_lang/`, `docs/`, `_layouts/`, `_plugins/`, `assets/css/`, `assets/js/`, and root config files.
3. **Protected directories** — `assets/img/logos/`, `assets/img/braze_icons/`, and `assets/img/icons/` are never eligible for deletion.
4. **Secondary verification (default on `--delete`)** — Before each unlink, the script searches all reference files again for path fragments. Candidates with any hit are **skipped** and reported.
5. **Allowlist** — Paths in `_data/unreferenced_images_allowlist.txt` are never deleted.
6. **Batch cap** — At most **100** deletions per run unless you pass `--limit` or raise `UNREFERENCED_IMAGE_MAX_DELETES`.

### Human review (required)

7. **Review the CSV before approving delete** — Sort by directory. Be extra cautious with the [high-risk patterns](#high-risk-path-patterns) below.
8. **Spot-check with ripgrep** for paths you are unsure about:

   ```bash
   rg -F 'assets/img/path/to/file.png' \
     _docs _includes _lang docs _layouts _plugins assets/css assets/js
   ```

9. **Check open PRs and in-flight work** — An image may be uploaded in one branch while the article reference lands in another, or screenshots may be staged for an upcoming release note before the markdown merges.
10. **Do not run cleanup in the same PR as a large IA move** (renames, help → user guide migrations). Run scan on a branch that includes those merges first so references are current.
11. **Confirm locale coverage** — English may have dropped a reference while `_lang/` still uses the file (the scanner checks locales; verify manually for partial migrations).
12. **Watch for `img/` vs `img_archive/`** — Live pages may reference `assets/img_archive/...`. Deleting a duplicate or migration leftover under `assets/img/` can still break a page if you remove the wrong copy.
13. **Consider external hotlinks** — Support macros, Slack pins, Loom decks, bookmarks, and other Braze repos may embed `braze.com/docs/assets/img/...` URLs with zero in-repo references. Confirm with docs platform owners before deleting widely shared assets.
14. **Attach the scan CSV to the PR** so reviewers can see what was considered unreferenced.

### High-risk path patterns

Be skeptical when the CSV shows:

| Pattern | Why |
|---------|-----|
| `assets/img/new-icons/**` | Legacy landing/card icons (not auto-protected; review manually) |
| `assets/img/contributing/**` | Should be kept when referenced in `docs/`; if still listed, verify path spelling |
| Partner folders (`assets/img/komo/`, `assets/img/ada/`, etc.) | May be referenced only in archived partner pages or hardcoded layout JS |
| Root-level `assets/img/*.png` | Often layout, brand, or 404 assets (`docs_404.png` vs unused `404.png`) |
| `_docs/_hidden/**` references | Archived pages are scanned but easy to overlook in review |
| Generic names (`dashboard.png`, `settings.png`) | Historically reused across many pages |
| Paths with spaces (`Braze Komo Images v2/`) | Alternate URL encodings may not match secondary verify |
| Recently touched in `git log` but “unreferenced” | Likely in-flight PR |

### After delete

15. **Re-run the scanner** — Confirm deleted paths are gone and no new false “unreferenced” spike appeared.
16. **CI / preview** — Open a draft PR and use the Vercel preview; spot-check a few pages that historically used images from the deleted folders.
17. **Investigate skips** — If the secondary check skipped files, add them to the allowlist (if still needed) or fix a scanner gap before retrying.

### Known blind spots (use allowlist or skip)

**Scanner gaps (no static `assets/img/...` substring in scanned files):**

- Liquid paths built from variables (`{% assign dir = 'assets/img/foo/' %}{{ dir }}bar.png`) or loops without a full path in source.
- Liquid `append:` chains that omit the filename as a contiguous path (fragile; most current templates still include the filename substring).
- Commented-out CSS/SCSS `background-image` references (image may be kept intentionally for a future re-enable).
- Filename-only references (bare `filename.png` without `assets/img/`).
- Absolute CDN URLs (`https://www.braze.com/docs/assets/img/...`) with no relative path in repo.
- URL-encoded path variants (spaces, special characters).
- Case mismatches (`Foo.png` referenced, `foo.png` on disk — macOS may hide the gap until Linux CI).
- `_data/`, `.github/`, `scripts/`, and skill/rule files that mention paths but are not scanned.

**External or out-of-band use (zero in-repo refs, still in use):**

- Images referenced only from **another repository** (marketing site, email templates, in-app help).
- **Hotlinked or bookmarked** production URLs after an article removed the reference.
- **Search index / CDN cache** lag after reference removal.
- **Internal training assets** (Loom, Notion, slide decks) that embed docs image URLs.

**Workflow timing:**

- **In-flight PRs** — image and reference in separate branches.
- **Draft / upcoming release** screenshots added before article text merges.
- **Intentional orphans** per authoring policy — reference removed in a page edit, binary left for a later cleanup pass.

**Other:**

- Very short filenames (for example `1.png`) — noisy in secondary search; verify manually.
- Duplicate or alternate renditions (original vs optimized) where only one path is referenced.

---

## Agent rules

1. **Always scan before deleting.** Never delete image files by guessing from `git status` or a single article change.
2. **Include `_lang/` and `docs/` in reasoning** — the scanner already does; do not delete because English dropped a reference if locales or contributing guides still use the file.
3. **Prefer batch PRs** of up to **100 files**; reviewers need a CSV summary, not a 4k-file diff blind review.
4. **Do not pass `--no-verify`** unless the user explicitly accepts the risk after manual ripgrep on every candidate.
5. **Do not edit `_lang/` prose** as part of this workflow unless the user explicitly asked for locale work; deleting unreferenced binaries is fine when the scanner confirms zero references.
6. **Update the allowlist** instead of skipping deletion ad hoc when a false positive is found—keeps the next run clean.
7. **Never raise `--limit` or `UNREFERENCED_IMAGE_MAX_DELETES` above 100** without user approval and documented review of the CSV.
8. **Image Pruning PRs** — Title must start with `[IP]`; body must say the PR is for **Image Pruning**; apply label `image pruning`. Do not mix image deletions with script/skill changes in one PR.

---

## Limitations

- References built only at runtime from non-static strings may not be detected; use the allowlist.
- Images referenced exclusively from another repository (marketing site, CDN) but still stored here will look unreferenced—confirm with docs platform owners before deleting.
- The script does not remove empty directories under `assets/img/`.
- `assets/img/new-icons/` is not auto-protected; review manually or allowlist if still required.

---

## Example prompts

Natural-language example requests:

```
Run a scan and summarize how many MB we can reclaim.
```

```
Delete unreferenced images after I approve the CSV.
```

```
The maintenance workflow opened a draft PR — help review the deletion batch.
```
