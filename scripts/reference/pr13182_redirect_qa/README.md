# PR 13182 — redirect list normalization QA artifacts

CSV triage files for `assets/js/broken_redirect_list.js` on this branch vs parent `develop` at merge base **a42f956983** (single commit **dbf36917b8**).

| File | Purpose |
|------|---------|
| `redirect_pr_lhs_summary_review.csv` | One row per **non-unchanged** normalized LHS key (at-a-glance triage). |
| `redirect_pr_develop_duplicate_norm_lhs.csv` | The **five** LHS keys that appeared twice on `develop` under the same normalized key (dedupe explains net −5 lines). |
| `redirect_pr_lhs_modified_or_semicolon.csv` | LHS/RHS or semicolon differences where both sides still have a row. |
| `redirect_pr_lhs_removed.csv` | Normalized keys present on `develop` but with **no** PR row (superseded by canonical LHS / merge). |
| `redirect_pr_lhs_added.csv` | Normalized keys that appear only on the PR side. |

**Regenerate** (from repo root), optionally writing a full 4k-row summary to `scripts/temp/`:

```bash
ruby scripts/reference/pr13182_redirect_qa/regenerate_report.rb a42f956983 dbf36917b8
```

Normalization was applied with `normalize_broken_redirect_list.rb --apply` (full pass: semicolons, slash-before-`?`/`#`, dedupe by normalized LHS, casing/path cleanup). That script is not on this branch; use `redirect_tooling_improvements` or a local copy to re-run.

**Normalized LHS key** here means: lowercase + strip trailing slashes on the redirect-from path (used to group duplicates), not the full Jekyll compare logic.
