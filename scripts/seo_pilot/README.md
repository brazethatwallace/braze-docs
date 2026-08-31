# SEO pilot tooling

Scripts for the in-house SEO/AEO pilot: page scoring, link fix tables, and per-page audits.

## Prerequisites

- Python 3.9+
- Repo root as working directory
- Optional: `./bdocs fblinks` output at `scripts/temp/broken-links.csv` (for link fix tables)

## Page scorecard

Ranks English `_docs/` pages by optimization headroom using combined signals.

```bash
python3 scripts/seo_pilot/page_scorecard.py \
  --gsc path/to/gsc-pages.csv \
  --algolia path/to/algolia-zero-results.csv \
  --support path/to/support_cases.csv \
  --out scripts/temp/seo-pilot-scorecard.csv \
  --top 15
```

### Target a specific page set

Pass a text file with one entry per line (`_docs/...md` path, `/docs/...` URL, or full `braze.com/docs` URL). Useful for top-traffic or editorially chosen pages:

```bash
python3 scripts/seo_pilot/page_scorecard.py \
  --pages-file scripts/temp/top-traffic-pages.txt \
  --gsc path/to/gsc-pages-ytd.csv \
  --sort-by gsc_clicks \
  --top 20 \
  --write-pilot-list
```

| `--sort-by` | Use when |
|-------------|----------|
| `headroom` | Default — prioritize metadata/link gaps within the set |
| `input` | Preserve the order in your pages file (e.g. traffic rank) |
| `gsc_clicks` | Sort by GSC clicks (requires `--gsc`) |
| `gsc_impressions` | Sort by GSC impressions (requires `--gsc`) |

Without external CSVs, the script still scores pages using:

- Editorial hub boosts (SMS, Canvas, Liquid, API, preference center, etc.)
- Metadata gaps (missing `description`, over-length description, H1/title mismatch)
- Broken internal links (from `scripts/temp/broken-links.csv` when present)

### GSC input CSV

Export from Google Search Console (Pages report). Expected columns (case-insensitive):

| Column | Aliases |
|--------|---------|
| `page` | `url`, `top pages` |
| `clicks` | |
| `impressions` | |
| `ctr` | |
| `position` | `avg position` |

### Algolia input CSV

| Column | Description |
|--------|-------------|
| `query` | Search query |
| `count` | Zero-result or low-click count |
| `doc_path` | Optional mapped `_docs/...` path |

### Support input CSV

Uses `_data/support_cases_latest.csv` format when available. Maps case text to doc paths via URL mentions and keyword heuristics.

## Link fix table

Produces vendor-style link fix tables: section heading, surrounding sentence, current URL, verified replacement.

```bash
# Generate broken-links.csv first (optional; script can scan inline)
./bdocs fblinks || true

python3 scripts/seo_pilot/link_fix_table.py \
  --broken-links scripts/temp/broken-links.csv \
  --out scripts/temp/link-fix-table.csv
```

Filter to pilot pages:

```bash
python3 scripts/seo_pilot/link_fix_table.py \
  --pages-file scripts/temp/pilot-pages.txt \
  --out scripts/temp/link-fix-table-pilot.csv
```

## Page audit

Audits meta, intro block, FAQ presence, and links for pilot pages.

```bash
python3 scripts/seo_pilot/page_audit.py \
  --pages-file scripts/temp/pilot-pages.txt \
  --out-dir docs/seo_pilot/recommendations
```

Outputs one markdown recommendation packet per page under `docs/seo_pilot/recommendations/`.

## GA4 traffic page list

Build a deduped pages file from a GA4 **Pages and screens** export (skips utility paths and pilot round-1 hubs):

```bash
python3 scripts/seo_pilot/ga_pages_to_list.py path/to/ga-export.csv --top 100
```

Writes:

| Output | Purpose |
|--------|---------|
| `scripts/temp/ga-top-traffic-pages.txt` | Doc paths for `--pages-file` (with view counts in comments) |
| `scripts/temp/ga-traffic-as-gsc.csv` | GSC-shaped CSV (`views` → `clicks`) for scorecard sorting |
| `scripts/temp/ga-top-traffic-report.csv` | Selection report with skip reasons |

## Apply no-approval fixes

After generating recommendation packets and a link fix table, apply shippable meta and link updates:

```bash
python3 scripts/seo_pilot/apply_wave2_no_approval.py \
  --recommendations docs/seo_pilot/recommendations \
  --link-fix-csv scripts/temp/link-fix-table-pilot.csv
```

Applies `article_title` / `description` changes from audit packets and `redirect_resolved` rows from the link fix CSV. Delete recommendation packets before opening the content PR.

**Meta-exempt pages** (`layout: redirect`, `bare`, `broken_page`, `blank_config`, or `config_only: true`) are skipped for description/title recommendations and fixes. See `meta_exempt.py`.

**Archived pages** under `_docs/**/archive_docs/` and `_docs/**/archived_layouts/` are excluded from all SEO pilot audits (unpublished content). **`_docs/_hidden/other/support_contact.md`** is also protected from automated edits.

## Typical workflow

```bash
./bdocs fblinks || true
python3 scripts/seo_pilot/page_scorecard.py --out scripts/temp/seo-pilot-scorecard.csv --top 15
# pilot-pages.txt is written by scorecard (--write-pilot-list)
python3 scripts/seo_pilot/link_fix_table.py --pages-file scripts/temp/pilot-pages.txt --out scripts/temp/link-fix-table-pilot.csv
python3 scripts/seo_pilot/page_audit.py --pages-file scripts/temp/pilot-pages.txt --out-dir docs/seo_pilot/recommendations
```

**Targeted set (e.g. top 20 traffic pages):**

```bash
./bdocs fblinks || true
python3 scripts/seo_pilot/page_scorecard.py \
  --pages-file scripts/temp/top-traffic-pages.txt \
  --gsc path/to/gsc-pages-ytd.csv \
  --sort-by gsc_clicks \
  --top 20 \
  --write-pilot-list
python3 scripts/seo_pilot/link_fix_table.py --pages-file scripts/temp/pilot-pages.txt --scan-all
python3 scripts/seo_pilot/page_audit.py --pages-file scripts/temp/pilot-pages.txt
```

**GA top-N traffic (deduped, pilot round-1 excluded):**

```bash
python3 scripts/seo_pilot/ga_pages_to_list.py path/to/ga-export.csv --top 100
./bdocs fblinks || true
python3 scripts/seo_pilot/page_scorecard.py \
  --pages-file scripts/temp/ga-top-traffic-pages.txt \
  --gsc scripts/temp/ga-traffic-as-gsc.csv \
  --sort-by input --top 100 --write-pilot-list \
  --out scripts/temp/ga-top-traffic-scorecard.csv
python3 scripts/seo_pilot/link_fix_table.py \
  --pages-file scripts/temp/pilot-pages.txt \
  --out scripts/temp/link-fix-table-ga-top100.csv --scan-all
python3 scripts/seo_pilot/page_audit.py \
  --pages-file scripts/temp/pilot-pages.txt \
  --link-fix-csv scripts/temp/link-fix-table-ga-top100.csv \
  --out-dir docs/seo_pilot/recommendations
python3 scripts/seo_pilot/apply_wave2_no_approval.py \
  --recommendations docs/seo_pilot/recommendations \
  --link-fix-csv scripts/temp/link-fix-table-ga-top100.csv
```

See [SEO and AEO page template](../../docs/contributing/style_guide/seo_aeo_page_template.md).
