# Include hygiene (pre-PR advisory)

Advisory check for agents opening a PR that adds, removes, or renames root
`_includes/` files, or changes `{% multi_lang_include %}` usage in `_docs/` or
`_includes/`. Run when [create-pr](../../create-pr/SKILL.md) Step 0 applies —
not on every docs edit.

This is **not** a blocking CI gate yet (see [BD-6842](https://jira.atl.braze.com/browse/BD-6842)).
It helps catch orphans and unnecessary indirection before review.

## When to run

Run this workflow when the branch diff against `develop` includes any of:

- Added, deleted, or renamed files under root `_includes/`
- New or removed `{% multi_lang_include %}` / `{% include %}` lines in `_docs/`
  or root `_includes/`

Skip when the PR only edits prose inside existing includes with no reference or
path changes.

## Commands

```bash
# Regenerate the backlog report (writes scripts/temp/single_use_includes_report.md)
python3 scripts/find_single_use_includes.py

# Optional: list only small, safe inline candidates (BD-6840-style batches)
python3 scripts/find_single_use_includes.py --eligible

# Confirm site still builds after include moves
bundle exec jekyll build --config _config.yml
```

For duplicate-content campaigns (extract shared snippets), also run:

```bash
python3 scripts/find_reuse_opportunities.py
```

Output: `scripts/temp/reuse_report.md`.

## PR checklist

After running the scripts, verify:

- [ ] **No orphaned includes** — Every deleted caller page still has its content
      inlined elsewhere, or the include file was deleted too. `jekyll build`
      catches broken `multi_lang_include` paths.
- [ ] **New includes justify indirection** — Prefer inlining when content is
      referenced once. Shared snippets belong in `_includes/` when two or more
      callers need the same text (see [BD-6838](https://jira.atl.braze.com/browse/BD-6838)).
- [ ] **Structural Liquid stays with callers** — Do not move `{% endtab %}`, tab
      wrappers, or page-specific `{% if %}` blocks into includes unless every
      caller shares the same wrapper context.
- [ ] **Report counts in the PR body** (include-hygiene batches only) — Note
      remaining single-use include count from the script output when the PR is
      part of BD-6345 / BD-6840 cleanup.

## What to note in the PR

For include-focused PRs, add a line under **Approach** or **Verification**:

```markdown
- Include hygiene: `find_single_use_includes.py` reports N single-reference includes remaining (M eligible for inlining).
```

Omit this line for routine edits that only touch existing include bodies.

## Interpreting `--eligible`

The `--eligible` filter flags small, single-reference includes that are safe
batch inline candidates (no parameters, no Liquid branching, ≤300 words, not SDK
forwarder stubs). Many legitimate includes fail this filter — that is expected.

Do **not** treat `--eligible` count as a merge blocker.

## Related tickets

| Ticket | Scope |
|--------|-------|
| [BD-6345](https://jira.atl.braze.com/browse/BD-6345) | Parent epic — include hygiene |
| [BD-6838](https://jira.atl.braze.com/browse/BD-6838) | Exact duplicates → shared includes |
| [BD-6840](https://jira.atl.braze.com/browse/BD-6840) | Single-use includes → inline |
| [BD-6841](https://jira.atl.braze.com/browse/BD-6841) | Orphaned includes |
| [BD-6842](https://jira.atl.braze.com/browse/BD-6842) | CI guardrails (future) |
