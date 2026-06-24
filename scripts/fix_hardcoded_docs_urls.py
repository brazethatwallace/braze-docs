#!/usr/bin/env python3
"""Replace hardcoded braze.com/docs URLs in English canonical sources with site.baseurl.

Only touches ``_docs/`` and root ``_includes/``. Skips ``_lang/``.

- ``redirect_to:`` front matter → ``/docs/...`` path (for multi_lang redirect layout)
- ``{% apimethod ...|URL %}`` → ``/docs/...`` root-relative path
- JSON-LD / JS needing absolute URLs → ``{{ site.homeurl }}{{ site.baseurl }}/...``
- Everything else → ``{{site.baseurl}}/...``
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOTS = [REPO / "_docs", REPO / "_includes"]

DOCS_URL_RE = re.compile(
    r"https?://(?:www\.)?braze\.com(/docs/?[^\s\"'<>]*)",
    re.IGNORECASE,
)

REDIRECT_TO_RE = re.compile(r"^(\s*redirect_to:\s*)", re.IGNORECASE)
YAML_LINK_RE = re.compile(r"^(\s*link:\s*)", re.IGNORECASE)
APIMETHOD_RE = re.compile(r"(\{%\s*apimethod\s+\S+\|)", re.IGNORECASE)
ABSOLUTE_CONTEXT_RE = re.compile(
    r"(urlTemplate|\"url\"\s*:|placeholder\s*=\s*['\"])",
    re.IGNORECASE,
)


def _subpath(docs_path: str) -> str:
    """``/docs/user_guide/foo/`` → ``/user_guide/foo/``."""
    if docs_path.startswith("/docs/"):
        return docs_path[len("/docs") :]
    if docs_path == "/docs":
        return "/"
    return docs_path


def _replace_url(url_match: str, line: str) -> str:
    m = DOCS_URL_RE.match(url_match)
    if not m:
        return url_match
    path_part = m.group(1)
    if path_part.endswith("/") and path_part != "/docs/":
        path_part = path_part.rstrip("/")

    if REDIRECT_TO_RE.search(line) or YAML_LINK_RE.search(line):
        return path_part

    if APIMETHOD_RE.search(line):
        return path_part

    if ABSOLUTE_CONTEXT_RE.search(line):
        sub = _subpath(path_part)
        if sub == "/":
            return "{{ site.homeurl }}{{ site.baseurl }}"
        return f"{{{{ site.homeurl }}}}{{{{ site.baseurl }}}}{sub}"

    sub = _subpath(path_part)
    if sub == "/":
        return "{{site.baseurl}}/"
    return f"{{{{site.baseurl}}}}{sub}"


def fix_line(line: str) -> tuple[str, int]:
    count = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        return _replace_url(match.group(0), line)

    return DOCS_URL_RE.sub(replacer, line), count


def fix_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    total = 0
    lines = []
    for line in original.splitlines(keepends=True):
        new_line, n = fix_line(line)
        total += n
        lines.append(new_line)
    if total:
        path.write_text("".join(lines), encoding="utf-8")
    return total


def main() -> int:
    grand_total = 0
    changed_files = []
    for root in ROOTS:
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix not in {".md", ".html", ".yml", ".yaml", ".xml"}:
                continue
            n = fix_file(path)
            if n:
                changed_files.append((path.relative_to(REPO), n))
                grand_total += n
    print(f"Replaced {grand_total} URL(s) in {len(changed_files)} file(s)")
    for rel, n in changed_files[:50]:
        print(f"  {rel}: {n}")
    if len(changed_files) > 50:
        print(f"  ... and {len(changed_files) - 50} more files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
