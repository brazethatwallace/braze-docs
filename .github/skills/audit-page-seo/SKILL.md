---
name: audit-page-seo
description: >
  Run in-house SEO/AEO page audits: score pilot candidates, generate verified link
  fix tables, and produce per-page recommendation packets split into no-approval
  and approval-needed tiers. Use when optimizing docs for search or answer engines,
  running the SEO pilot, or delivering page-level title/meta/FAQ/link recommendations.
---

# Audit page SEO

Invoke with `/audit-page-seo`.

## When to use

- Scoring `_docs/` pages for SEO/AEO pilot candidacy
- Generating verified link fix tables (section heading + sentence context)
- Producing per-page recommendation packets for editorial review

English canonical `_docs/` only unless the user explicitly requests locale work.

## Workflow

1. **Broken links (optional):** `./bdocs fblinks || true`
2. **Score pages:** `python3 scripts/seo_pilot/page_scorecard.py --out scripts/temp/seo-pilot-scorecard.csv --top 15 --write-pilot-list`
   - **Targeted set:** add `--pages-file scripts/temp/top-traffic-pages.txt` (and optional `--gsc` + `--sort-by gsc_clicks`)
3. **Link fix table:** `python3 scripts/seo_pilot/link_fix_table.py --pages-file scripts/temp/pilot-pages.txt --out scripts/temp/link-fix-table-pilot.csv --scan-all`
4. **Page audits:** `python3 scripts/seo_pilot/page_audit.py --pages-file scripts/temp/pilot-pages.txt --out-dir docs/seo_pilot/recommendations`
5. **Ship no-approval items** in a PR (titles, metas, verified link fixes). Route approval-needed copy to editorial.

## Template and tiers

Follow [docs/contributing/style_guide/seo_aeo_page_template.md](../../docs/contributing/style_guide/seo_aeo_page_template.md).

| Tier | Examples |
|------|----------|
| No-approval | `description`, verified link fixes, heading levels, `search_rank` |
| Approval-needed | Opening answer rewrites, new FAQ blocks, section reorganization |

## Input files

See [scripts/seo_pilot/README.md](../../scripts/seo_pilot/README.md) for GSC, Algolia, and support CSV formats.

## Pre-PR gates

- `./bdocs fblinks`
- spell-check / check-accessibility on changed markdown
- Style QA for prose diffs
