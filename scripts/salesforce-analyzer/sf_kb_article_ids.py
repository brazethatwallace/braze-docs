"""Shared helpers for Salesforce Knowledge article id columns in `kb_articles.csv`."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

# CSV headers that may store Salesforce Knowledge article ids (first match wins).
ARTICLE_ID_HEADER_ALIASES = ("article_id", "xt")


def article_id_column(fieldnames: Sequence[str] | None) -> str | None:
    """Return the CSV header that stores Salesforce Knowledge article ids."""
    if not fieldnames:
        return None
    available = list(fieldnames)
    lower_to_original = {header.lower(): header for header in available}
    for alias in ARTICLE_ID_HEADER_ALIASES:
        if alias in available:
            return alias
        original = lower_to_original.get(alias.lower())
        if original:
            return original
    return None


def article_id_from_row(
    row: Mapping[str, str],
    *,
    id_column: str | None = None,
) -> str:
    """Read a Salesforce Knowledge article id from a CSV row."""
    columns: list[str] = []
    if id_column:
        columns.append(id_column)
    for alias in ARTICLE_ID_HEADER_ALIASES:
        if id_column and id_column.lower() == alias.lower():
            continue
        columns.append(alias)
    for column in columns:
        value = (row.get(column) or "").strip()
        if value:
            return value
    return ""
