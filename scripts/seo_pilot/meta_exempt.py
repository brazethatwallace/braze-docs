"""Frontmatter checks for pages that should not receive SEO meta recommendations."""

from __future__ import annotations

import re

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Layouts that do not render description/article_title for search snippets.
SKIP_META_LAYOUTS = frozenset({"redirect", "bare", "blank_config", "broken_page"})

# Unpublished archived content under _hidden/archive_docs/ (not in public sitemap).
ARCHIVE_DOCS_MARKER = "/archive_docs/"


def normalize_doc_path(rel: str) -> str:
    return rel.replace("\\", "/")


def is_archive_doc_path(rel: str) -> bool:
    return ARCHIVE_DOCS_MARKER in normalize_doc_path(rel)


def skips_seo_audit(rel: str) -> bool:
    """True when a page should be excluded from SEO pilot audits entirely."""
    return is_archive_doc_path(rel)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out


def is_truthy(value: str) -> bool:
    return value.strip().lower() in ("true", "yes", "1")


def skips_seo_meta(fm: dict[str, str]) -> bool:
    """True when description/article_title SEO fixes should not apply."""
    layout = fm.get("layout", "").strip().lower()
    if layout in SKIP_META_LAYOUTS:
        return True
    if is_truthy(fm.get("config_only", "")):
        return True
    return False


def skip_meta_reason(fm: dict[str, str]) -> str:
    layout = fm.get("layout", "").strip().lower()
    if layout in SKIP_META_LAYOUTS:
        return f"`layout: {layout}` does not render SEO meta"
    if is_truthy(fm.get("config_only", "")):
        return "`config_only: true` stub page"
    return ""
