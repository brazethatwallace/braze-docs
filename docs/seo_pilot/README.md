# SEO/AEO pilot

In-house SEO and answer-engine optimization pilot for English canonical docs (`_docs/`).

## Deliverables

| Asset | Location |
|-------|----------|
| Page structure template | [docs/contributing/style_guide/seo_aeo_page_template.md](../contributing/style_guide/seo_aeo_page_template.md) |
| Pilot tooling | [scripts/seo_pilot/](../../scripts/seo_pilot/) |
| Agent skill | [.github/skills/page-seo-audit/](../../.github/skills/page-seo-audit/SKILL.md) |
| Pilot page selection | [pilot-selection.md](pilot-selection.md) |
| Per-page recommendations | [recommendations/](recommendations/) |

## Regenerate

```bash
./bdocs fblinks || true
python3 scripts/seo_pilot/page_scorecard.py \
  --out scripts/temp/seo-pilot-scorecard.csv \
  --top 15 \
  --write-pilot-list
python3 scripts/seo_pilot/link_fix_table.py \
  --pages-file scripts/temp/pilot-pages.txt \
  --out scripts/temp/link-fix-table-pilot.csv \
  --scan-all
python3 scripts/seo_pilot/page_audit.py \
  --pages-file scripts/temp/pilot-pages.txt \
  --out-dir docs/seo_pilot/recommendations
```

Optional inputs: GSC pages export, Algolia zero-result CSV, support cases CSV. See [scripts/seo_pilot/README.md](../../scripts/seo_pilot/README.md).

## Recommendation tiers

- **No-approval:** titles, metas, verified link fixes, heading levels — ship in PRs without copy review
- **Approval-needed:** opening answer rewrites, new FAQ blocks, reorganization — editorial sign-off first
