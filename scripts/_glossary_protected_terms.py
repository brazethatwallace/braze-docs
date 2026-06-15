"""Shared constants for protected Braze product terminology.

Both ``scripts/auto_translate.py`` (runtime glossary override during
translation) and ``scripts/audit_glossaries.py`` (upstream-sync guard
against future dashboard/SDK auto-fix regressions) need to agree on
which English product names must stay in English across every locale.

The two scripts previously kept parallel copies of this table with a
"keep in sync" comment, which drifted in practice. Copilot flagged the
duplication on PR #13303 as a long-term drift risk; extracting the
constant into this tiny module makes the single source of truth
explicit and keeps the import fast (no ``anthropic`` / API client
pulls into ``audit_glossaries``).

The mapping key is the canonical English form of the product name (the
form that must surface in translated docs), and the value maps a
locale key to a per-locale override when one differs from English.
Most locales render each term identically to English — the empty
``{}`` dict means "use the English term in every locale".

The ``Canvases`` override for ``es``/``fr``/``pt-br`` intentionally
collapses the plural to singular: those locales do not pluralize
English loanwords with an added ``s`` in docs prose, so the canonical
plural is the same word as the singular. ``de``/``ja``/``ko`` keep
the English plural.
"""

PROTECTED_PRODUCT_TERMS = {
    "Braze":            {},
    "BrazeAI":          {},
    "Canvas":           {},
    "Canvases":         {"es": "Canvas", "fr": "Canvas", "pt-br": "Canvas"},
    "Currents":         {},
    "Content Cards":    {},
    "Content Blocks":   {},
    "News Feed":        {},
    "Liquid":           {},
    "SDK":              {},
    "API":              {},
    "REST API":         {},
    "Segment":          {},
    "Segments":         {},
    "Campaign":         {},
    "Campaigns":        {},
    "Push Stories":     {},
    "In-App Messages":  {},
}
