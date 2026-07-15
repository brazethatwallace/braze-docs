# Workflow: Spell-check changed Markdown

## Overview

Run [cspell](https://cspell.org/) on changed English markdown under `_docs/` and `_includes/`, matching the PR CI workflow in `.github/workflows/cspell.yml`. Fix only **very high-confidence** typos automatically. Present everything else to the contributor before editing prose or the project dictionary.

---

## Step 1: Collect changed files

Build the file list from the context in `SKILL.md`, or run:

```bash
BASE="origin/develop"
if ! git rev-parse --verify "$BASE" >/dev/null 2>&1; then
  BASE="develop"
fi
mapfile -t FILES < <(
  git diff --name-only --diff-filter=ACMRT "$BASE"...HEAD -- _docs _includes \
    | grep -E '\.md$' \
    | grep -v '^_docs/_hidden/' || true
)
```

Exclude `_lang/**` (out of scope).

If `FILES` is empty, report:
> No changed Markdown under `_docs/` or `_includes/` (excluding `_docs/_hidden/`). Nothing to spell-check.

Stop here.

Confirm `node_modules/.bin/cspell` exists. If missing, run `npm ci --ignore-scripts` once, then retry.

---

## Step 2: Run cspell

```bash
npm exec -- cspell lint --no-progress "${FILES[@]}"
```

Capture full stdout/stderr. Exit code `0` = clean.

Optional — group hits by unknown word for review:

```bash
npm exec -- cspell lint --no-progress "${FILES[@]}" 2>&1 \
  | python3 scripts/cspell_group_report.py
```

If cspell exits `0`, report success and stop.

---

## Step 3: Classify each unknown word

Parse lines in cspell's default format:

```text
path/to/file.md:42:10 - Unknown word (token) [optional fix: (suggestion)]
```

### Very high confidence — auto-fix

Apply the fix in source **only when all** of the following are true:

1. cspell reports **exactly one** `fix: (suggestion)` for that occurrence
2. The suggestion differs from the flagged token by a **common, unambiguous typo** — for example:
   - transposed letters (`recieve` → `receive`, `occured` → `occurred`)
   - omitted or duplicated letter in a common English word (`teh` → `the`, `adress` → `address`)
   - a well-known misspelling with a single standard correction
3. The flagged token is **not** a plausible Braze product name, API field, partner name, or glossary term (check [`writing_style_guide.md`](../../../../docs/contributing/style_guide/writing_style_guide.md) #glossary and [`config/cspell/braze-dictionary.txt`](../../../../config/cspell/braze-dictionary.txt))
4. The token is **not** inside a fenced code block, URL, Liquid tag, or file path (cspell usually skips these; if not, do not auto-fix)

When in doubt, **do not** auto-fix. Treat as ask-first.

### Ask first — do not auto-fix

Stop and present options when **any** of the following apply:

- No `fix:` suggestion, or multiple plausible corrections
- The word may be intentional (product/feature name, partner, acronym, API identifier)
- Capitalization or branding matters (`Canvas` vs `canvas`, `Segment` vs `segment`)
- The hit is in a heading, link text, or table cell where meaning is unclear
- Adding to the dictionary vs changing prose is ambiguous

For each ask-first item, offer:

1. **Fix typo** — apply a specific correction the contributor confirms
2. **Add to dictionary** — add the token to `config/cspell/braze-dictionary.txt` (see Step 4)
3. **Skip** — leave unchanged (contributor accepts CI risk or will handle separately)

Collect answers in one batch when there are multiple hits.

---

## Step 4: Dictionary vs typo

**Fix the Markdown** when the word is simply misspelled English or does not match Braze editorial spelling.

**Add to [`config/cspell/braze-dictionary.txt`](../../../../config/cspell/braze-dictionary.txt)** when the word is **correct** but unknown to cspell:

- Braze product/feature names and approved glossary terms
- Partner names, SDK symbols, and industry terms used intentionally in docs
- Multi-word tokens that appear as a single line in the dictionary

Dictionary rules (see file header):

- One entry per line, keep the file **sorted alphabetically**
- Do **not** add misspellings to silence the checker
- Do **not** duplicate common `en_US` words already recognized by cspell
- Prefer the style guide glossary over ad-hoc additions

Do **not** add routine English words to `cspell.json` overrides unless there is a rare per-file exception (for example `_docs/_contributing/styling_examples.md`).

---

## Step 5: Re-run until clean

After auto-fixes and confirmed contributor choices:

1. Re-run Step 2 on the same `FILES` list (or the subset that still has open hits)
2. Repeat until cspell exits `0` or only explicit skips remain

Final summary format:

```markdown
## Spell-check summary

- Files checked: N
- Auto-fixed: [list or "none"]
- Dictionary additions: [list or "none"]
- Contributor decisions: [list or "none"]
- Skipped (explicit): [list or "none"]
- Result: clean | N issue(s) remaining
```

If issues remain after explicit skips, warn that CI **Spellcheck** will fail on the PR.

---

## Core principles

1. **Match CI scope** — same paths and excludes as `cspell.yml` (`_docs/`, `_includes/`, `.md` only, skip `_docs/_hidden/`).
2. **Very high bar for auto-fix** — when uncertain, ask. A false correction in prose is worse than a dictionary question.
3. **Dictionary is for valid terms, not typos** — never add a misspelling to `braze-dictionary.txt`.
4. **One stop for ambiguous hits** — batch ask-first items; do not interleave silent prose edits with dictionary changes.
