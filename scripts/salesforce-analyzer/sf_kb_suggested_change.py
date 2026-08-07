"""Shared triage and ship-ready checks for Salesforce KB migration."""

from __future__ import annotations

PHASE2_BATCH_MARKER = "<!-- sf-kb-phase2-batch -->"
PHASE2_BATCH_END_MARKER = "<!-- /sf-kb-phase2-batch -->"

# First-line ``suggested_change`` starters treated as non-actionable author briefs.
VAGUE_STARTERS: tuple[str, ...] = (
    "add to ",
    "add documentation",
    "ensure ",
    "consider adding",
    "optional troubleshooting",
    "document ",
    "update ",
    "cross-link",
    "include the ",
    "kb can remain",
    "optional ",
    "might ",
    "may ",
    "consider reviewing",
    "review ",
    "tbd",
    "unclear",
    "needs investigation",
    "needs sme",
    "flag for",
)


def is_vague_suggested_change(raw: str | None) -> bool:
    if not raw or not str(raw).strip():
        return True
    first = str(raw).strip().split("\n", 1)[0].strip().lower()
    return any(first.startswith(s) for s in VAGUE_STARTERS)


def validate_ship_ready_markdown(text: str) -> list[str]:
    """Return human-readable errors when a doc still has unpolished Phase 2 inserts.

    Only checks for phase-2 batch markers. CSV triage heuristics apply to
    ``suggested_change`` in Phase 1, not to full target pages (which often
    contain legitimate instructional lines such as "Ensure ..." or "Update ...").
    """
    errors: list[str] = []
    if PHASE2_BATCH_MARKER in text:
        errors.append(
            "remove phase-2 batch markers and integrate ship-ready prose before opening a PR"
        )
    if PHASE2_BATCH_END_MARKER in text:
        errors.append(
            "remove the phase-2 batch end marker before opening a PR"
        )
    return errors
