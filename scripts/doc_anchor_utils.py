"""Markdown heading anchor helpers for ulinks and redirect tooling."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "_docs"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(
    r"^(#{1,6})\s+(.+?)(?:\s+\{#([^}]+)\})?\s*$",
    re.MULTILINE,
)
IAL_RE = re.compile(r"\{#([^}]+)\}")
GLOSSARY_LAYOUTS = frozenset({"glossary_page", "api_glossary"})


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


def load_frontmatter_yaml(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def local_redirect_keys(fm: dict) -> list[str]:
    value = fm.get("local_redirect")
    if isinstance(value, dict):
        return [str(key) for key in value]
    if isinstance(value, list):
        keys: list[str] = []
        for item in value:
            if isinstance(item, dict):
                keys.extend(str(key) for key in item)
        return keys
    return []


def uses_rendered_includes(text: str, fm: dict) -> bool:
    layout = str(fm.get("layout", "")).lower()
    if layout in GLOSSARY_LAYOUTS:
        return True
    return "{% sdktab" in text or "{% multi_lang_include" in text


def docs_tail_from_url(url: str) -> str:
    tail = url.strip().lstrip("/")
    if tail.startswith("docs/"):
        tail = tail[len("docs/") :]
    tail, _, _query = tail.partition("?")
    tail, _, _frag = tail.partition("#")
    return tail.rstrip("/")


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


def valid_anchor_ids(text: str, fm: dict) -> set[str]:
    ids = set(extract_heading_ids(text))
    ids.update(local_redirect_keys(fm))
    ids.update(match.group(1) for match in IAL_RE.finditer(text))
    return ids


def sanitize_fragment_for_target(target_url: str, fragment: str) -> str:
    """Return a valid fragment for the target page, or empty string."""
    fragment = normalize_fragment(fragment)
    if not fragment:
        return ""

    tail = docs_tail_from_url(target_url)
    md_path = url_tail_to_markdown_path(tail)
    if not md_path:
        return fragment

    text = md_path.read_text(encoding="utf-8")
    fm = load_frontmatter_yaml(text)
    if uses_rendered_includes(text, fm):
        return fragment

    heading_ids = extract_heading_ids(text)
    valid_ids = valid_anchor_ids(text, fm)
    if not valid_ids:
        return fragment

    if fragment not in valid_ids:
        return ""

    if heading_ids and heading_ids[0] == fragment:
        return ""

    return fragment
