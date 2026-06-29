#!/usr/bin/env python3
"""Strip trailing slashes from internal Braze docs links in Markdown.

Production serves extensionless doc URLs without a trailing slash (Vercel
``trailingSlash: false``). This script normalizes internal link targets in
``_docs/`` so they point at 200 URLs instead of paths that 308-redirect.

Handles:
  - Markdown ``[text]({{site.baseurl}}/path/)``
  - Markdown ``[text](/docs/path/)``
  - HTML ``href="/docs/path/"`` and ``href='/docs/path/'``
  - YAML ``link: /docs/path/`` frontmatter values

Skips external URLs, asset paths with known file extensions, and paths whose
last segment looks like a file (contains a dot).

Usage:
  python3 scripts/strip_internal_doc_link_trailing_slashes.py --dry-run \\
    _docs/_user_guide _docs/_developer_guide _docs/_api
  python3 scripts/strip_internal_doc_link_trailing_slashes.py --apply \\
    _docs/_user_guide _docs/_developer_guide _docs/_api
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

_SKIP_EXTS = (
    ".md",
    ".html",
    ".htm",
    ".json",
    ".xml",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".pdf",
    ".txt",
    ".yaml",
    ".yml",
    ".csv",
    ".zip",
    ".ico",
)

_MARKDOWN_LINK_URL = re.compile(r"\]\(([^)]+)\)")
_HREF_ATTR = re.compile(r"""href=(['"])([^'"]+)\1""")
_YAML_LINK_LINE = re.compile(r"^(\s*link:\s*)(/docs/\S+?)/?\s*$", re.MULTILINE)


def _split_url(url: str) -> tuple[str, str, str]:
    frag = ""
    query = ""
    body = url
    if "#" in body:
        body, rest = body.split("#", 1)
        frag = f"#{rest}"
    if "?" in body:
        body, rest = body.split("?", 1)
        query = f"?{rest}"
    return body, query, frag


def _is_internal_doc_url(url: str) -> bool:
    u = url.strip()
    if not u or u.startswith(("http://", "https://", "mailto:", "tel:")):
        return False
    if "{{site.baseurl}}" in u:
        return True
    return u.startswith("/docs/")


def _path_looks_like_file(path: str) -> bool:
    last_seg = path.rstrip("/").rsplit("/", 1)[-1]
    if not last_seg:
        return False
    lower = last_seg.lower()
    if any(lower.endswith(ext) for ext in _SKIP_EXTS):
        return True
    return "." in last_seg


def normalize_internal_doc_url(url: str) -> tuple[str, bool]:
    """Return (normalized_url, changed)."""
    if not _is_internal_doc_url(url):
        return url, False

    body, query, frag = _split_url(url)

    if body.endswith("/") and body not in {"/", "/docs"}:
        if _path_looks_like_file(body):
            return url, False
        body = body.rstrip("/")

    if frag and frag.endswith("/"):
        frag = frag.rstrip("/")

    new_url = f"{body}{query}{frag}"
    return new_url, new_url != url


def _rewrite_markdown_links(content: str) -> tuple[str, int]:
    changes = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal changes
        url = match.group(1)
        new_url, changed = normalize_internal_doc_url(url)
        if changed:
            changes += 1
        return f"]({new_url})"

    return _MARKDOWN_LINK_URL.sub(repl, content), changes


def _rewrite_href_attrs(content: str) -> tuple[str, int]:
    changes = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal changes
        quote, url = match.group(1), match.group(2)
        new_url, changed = normalize_internal_doc_url(url)
        if changed:
            changes += 1
        return f"href={quote}{new_url}{quote}"

    return _HREF_ATTR.sub(repl, content), changes


def _rewrite_yaml_links(content: str) -> tuple[str, int]:
    changes = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal changes
        prefix, path = match.group(1), match.group(2)
        new_url, changed = normalize_internal_doc_url(path)
        if changed:
            changes += 1
        return f"{prefix}{new_url}"

    return _YAML_LINK_LINE.sub(repl, content), changes


def process_file(path: Path, apply: bool) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    updated = text
    stats = {"markdown": 0, "href": 0, "yaml_link": 0}

    updated, n = _rewrite_markdown_links(updated)
    stats["markdown"] += n
    updated, n = _rewrite_href_attrs(updated)
    stats["href"] += n
    updated, n = _rewrite_yaml_links(updated)
    stats["yaml_link"] += n

    if updated != text and apply:
        path.write_text(updated, encoding="utf-8")

    stats["changed"] = int(updated != text)
    return stats


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for root in paths:
        if root.is_file() and root.suffix == ".md":
            files.append(root)
            continue
        if not root.is_dir():
            continue
        files.extend(sorted(root.rglob("*.md")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        default=[
            "_docs/_user_guide",
            "_docs/_developer_guide",
            "_docs/_api",
        ],
        help="Markdown files or directories to process (default: user_guide, developer_guide, api)",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--apply", action="store_true", help="Write changes to disk")
    group.add_argument("--dry-run", action="store_true", help="Report only (default)")
    args = parser.parse_args()

    apply = args.apply
    targets = [(REPO_ROOT / p).resolve() for p in args.paths]
    files = iter_markdown_files(targets)

    totals = {"files": 0, "markdown": 0, "href": 0, "yaml_link": 0}
    changed_files: list[str] = []

    for md_path in files:
        rel = md_path.relative_to(REPO_ROOT)
        stats = process_file(md_path, apply=apply)
        if not stats["changed"]:
            continue
        changed_files.append(str(rel))
        totals["files"] += 1
        totals["markdown"] += stats["markdown"]
        totals["href"] += stats["href"]
        totals["yaml_link"] += stats["yaml_link"]

    mode = "APPLY" if apply else "DRY-RUN"
    print(f"{mode}: scanned {len(files)} markdown file(s)")
    print(
        f"  {totals['files']} file(s) with changes; "
        f"{totals['markdown']} markdown link(s), "
        f"{totals['href']} href attr(s), "
        f"{totals['yaml_link']} yaml link: line(s)"
    )
    for rel in changed_files[:40]:
        print(f"    {rel}")
    if len(changed_files) > 40:
        print(f"    … and {len(changed_files) - 40} more")

    if not apply and totals["files"]:
        print("Run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
