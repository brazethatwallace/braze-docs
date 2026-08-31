"""Markdown heading anchor helpers for SEO pilot link fixes."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = REPO_ROOT / "_docs"

HEADING_RE = re.compile(
    r"^(#{1,6})\s+(.+?)(?:\s+\{#([^}]+)\})?\s*$",
    re.MULTILINE,
)


def normalize_fragment(fragment: str) -> str:
    return fragment.strip().strip("/")


def kramdown_slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_`]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def extract_heading_ids(text: str) -> list[str]:
    ids: list[str] = []
    for match in HEADING_RE.finditer(text):
        explicit = match.group(3)
        if explicit:
            ids.append(explicit)
            continue
        slug = kramdown_slug(match.group(2))
        if slug:
            ids.append(slug)
    return ids


def url_tail_to_markdown_path(tail: str) -> Path | None:
    tail = tail.lstrip("/")
    if not tail:
        candidate = DOCS_ROOT / "_home.md"
        return candidate if candidate.is_file() else None
    parts = tail.split("/")
    collection = parts[0]
    sub = "/".join(parts[1:])
    if sub:
        candidate = DOCS_ROOT / f"_{collection}" / f"{sub}.md"
    else:
        candidate = DOCS_ROOT / f"_{collection}.md"
    return candidate if candidate.is_file() else None


def sanitize_fragment_for_target(target_tail: str, fragment: str) -> str:
    """Return a valid fragment for the target page, or empty string."""
    fragment = normalize_fragment(fragment)
    if not fragment:
        return ""

    md_path = url_tail_to_markdown_path(target_tail)
    if not md_path:
        return ""

    heading_ids = extract_heading_ids(md_path.read_text(encoding="utf-8"))
    if not heading_ids or fragment not in heading_ids:
        return ""

    if heading_ids[0] == fragment:
        return ""

    return fragment
