# Translation glossaries

`scripts/glossaries/{locale}.json` files power automated translation and glossary
compliance checks (`scripts/auto_translate.py`, `scripts/audit_glossaries.py`).

## Source of truth: Phrase TMS

Glossary entries are **synced from Phrase term bases**, not edited directly in
this repo for routine updates. Term-base UIDs and locale language codes live in
[`../phrase_term_bases.json`](../phrase_term_bases.json).

### Local sync

1. Copy [`.phrase-tms.env.example`](../../.phrase-tms.env.example) to
   `.phrase-tms.env` at the repo root and add your Phrase Platform API token.
2. Install dependencies: `pip install -r scripts/requirements-glossaries.txt`
3. Run:

```bash
python scripts/sync_glossaries_from_phrase.py
```

Options:

- `--dry-run` — fetch and diff without writing files
- `--locale ja` — sync one locale (repeatable)
- `--report path.md` — markdown summary for PRs
- `--skip-locale-propagation` — update glossaries only (no `_lang/` edits)

### CI

[`.github/workflows/sync-glossaries-from-phrase.yml`](../../.github/workflows/sync-glossaries-from-phrase.yml)
runs weekly (and on demand), opens a PR when Phrase entries change, and
propagates added or updated terms into matching `_lang/` markdown files.
Requires the
`PHRASE_TMS_TOKEN` repository secret (Phrase Platform API token).

### Locale propagation exclusions

[`../phrase_glossary_locale_propagation_exclusions.json`](../phrase_glossary_locale_propagation_exclusions.json)
lists English glossary keys that are too generic for blind `_lang/` substring
replacement during sync (for example `monitoring`, which would corrupt
`{#monitoring-...}` heading anchor IDs).

Propagation uses only the **first** Phrase synonym when a glossary value contains
` or ` (for example `SDK or Software-Development-Kit` → `SDK`). Files under
`_lang/*/_api/` are skipped entirely so API reference pages keep English acronyms
and endpoint literals intact.

If a sync PR still contains known corruption patterns (for example `Taxi for Email`
in rideshare examples or `On-Klick, der` from the `click` glossary key), run
`python scripts/repair_glossary_propagation_corruption.py` before merging.

### Sync exclusions

[`../phrase_glossary_sync_exclusions.json`](../phrase_glossary_sync_exclusions.json)
lists per-locale English keys dropped after Phrase import when a term is too
generic for docs glossary substring matching (for example Spanish `data`).

[`../phrase_glossary_sync_overrides.json`](../phrase_glossary_sync_overrides.json)
adds or replaces keys when Phrase has a bad English source term (for example
German `lokal time` → `local time`, or excluding bare `gear` so `gear icon`
matches correctly).

### Protected product terms

[`../_glossary_protected_terms.py`](../_glossary_protected_terms.py) still
overrides a small set of Braze product names at **translation runtime** (for
example Japanese `Campaign` → `キャンペーン`). Those overrides apply on top of the
synced JSON. When product terminology should change in docs, update the Phrase
term base and/or the protected-terms module together.

### Drift audit

[`.github/workflows/audit-glossaries.yml`](../../.github/workflows/audit-glossaries.yml)
compares Phrase-synced glossaries against platform and SDK locale files and
opens a **report-only** PR when mismatches are found. Resolve drift by updating
Phrase (preferred) or the upstream product locale files.
