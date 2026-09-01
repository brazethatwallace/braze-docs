"""Frontmatter checks for pages that should not receive SEO meta recommendations."""

from __future__ import annotations

import re

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Layouts that do not render description/article_title for search snippets.
SKIP_META_LAYOUTS = frozenset({"redirect", "bare", "blank_config", "broken_page"})

# Unpublished archived hidden content (not in public sitemap).
UNPUBLISHED_PATH_MARKERS = ("/archive_docs/", "/archived_layouts/", "/_unlisted_docs/")

# Functional pages excluded from automated SEO edits (see style-qa / create-pr skills).
PROTECTED_DOC_PATHS = frozenset(
    {
        "_docs/_hidden/other/support_contact.md",
        "_docs/_hidden/other/feedback.md",
        "_docs/_hidden/other/documentation_request.md",
    }
)


def normalize_doc_path(rel: str) -> str:
    return rel.replace("\\", "/")


def is_protected_doc_path(rel: str) -> bool:
    return normalize_doc_path(rel) in PROTECTED_DOC_PATHS


def is_unpublished_doc_path(rel: str) -> bool:
    path = normalize_doc_path(rel)
    return any(marker in path for marker in UNPUBLISHED_PATH_MARKERS)


def is_archive_doc_path(rel: str) -> bool:
    """Backward-compatible alias."""
    return is_unpublished_doc_path(rel)


def skips_seo_audit(rel: str) -> bool:
    """True when a page should be excluded from SEO pilot audits entirely."""
    return is_protected_doc_path(rel) or is_unpublished_doc_path(rel)


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


def is_release_doc_path(rel: str) -> bool:
    return "/_releases/" in normalize_doc_path(rel)


def skips_seo_meta(fm: dict[str, str], rel: str = "") -> bool:
    """True when description/article_title SEO fixes should not apply."""
    if rel and is_release_doc_path(rel):
        return True
    layout = fm.get("layout", "").strip().lower()
    if layout in SKIP_META_LAYOUTS:
        return True
    if is_truthy(fm.get("config_only", "")):
        return True
    if is_truthy(fm.get("noindex", "")):
        return True
    return False


def skip_meta_reason(fm: dict[str, str], rel: str = "") -> str:
    if rel and is_release_doc_path(rel):
        return "release notes are historical content"
    layout = fm.get("layout", "").strip().lower()
    if layout in SKIP_META_LAYOUTS:
        return f"`layout: {layout}` does not render SEO meta"
    if is_truthy(fm.get("config_only", "")):
        return "`config_only: true` stub page"
    if is_truthy(fm.get("noindex", "")):
        return "`noindex: true` page"
    return ""
