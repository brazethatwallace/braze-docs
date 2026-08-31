#!/usr/bin/env python3
"""
Build verified link fix tables with section heading and sentence context.

Joins broken-links.csv (from ./bdocs fblinks) with redirect map resolution.

Usage:
  python3 scripts/seo_pilot/link_fix_table.py --out scripts/temp/link-fix-table.csv
  python3 scripts/seo_pilot/link_fix_table.py --pages-file scripts/temp/pilot-pages.txt
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from meta_exempt import skips_seo_audit

REPO_ROOT = Path(__file__).resolve().parents[2]
REDIRECT_JS = REPO_ROOT / "assets" / "js" / "broken_redirect_list.js"
DOCS_ROOT = REPO_ROOT / "_docs"

REDIRECT_RE = re.compile(
    r"validurls\['/docs([^']*)'\]\s*=\s*'/docs([^']*)';"
)
LINK_INLINE_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")


def is_braze_host(hostname: str | None) -> bool:
    if not hostname:
        return False
    host = hostname.lower()
    return host == "braze.com" or host.endswith(".braze.com")


def extract_docs_path(url: str) -> str | None:
    url = url.strip()
    if url.startswith("/docs"):
        return url
    parsed = urlparse(url)
    if is_braze_host(parsed.hostname) and parsed.path.startswith("/docs"):
        path = parsed.path
        if parsed.query:
            path += f"?{parsed.query}"
        if parsed.fragment:
            path += f"#{parsed.fragment}"
        return path
    return None


def ensure_docs_path(path: str) -> str:
    path = path.strip()
    if not path.startswith("/docs"):
        path = "/docs" + path if path.startswith("/") else "/docs/" + path
    return path


def path_only(url: str) -> str:
    """Strip query and fragment for filesystem / path-only redirect lookups."""
    url = ensure_docs_path(url)
    url = url.split("?")[0].split("#")[0]
    return url.rstrip("/") or "/docs"


def url_fragment(url: str) -> str | None:
    return url.split("#", 1)[1] if "#" in url else None


def load_redirect_map() -> dict[str, str]:
    """Load redirect map preserving query strings and fragments in keys/values."""
    text = REDIRECT_JS.read_text(encoding="utf-8")
    mapping: dict[str, str] = {}
    for m in REDIRECT_RE.finditer(text):
        old_full = ensure_docs_path(f"/docs{m.group(1)}")
        new_full = ensure_docs_path(f"/docs{m.group(2)}")
        mapping[old_full] = new_full
    return mapping


def resolve_redirect(url: str, redirects: dict[str, str], max_hops: int = 10) -> tuple[str, str]:
    """Return (final_url, status)."""
    current = ensure_docs_path(url)
    seen: set[str] = set()
    redirected = False
    for _ in range(max_hops):
        if current in seen:
            return current, "redirect_loop"
        seen.add(current)
        if current in redirects:
            current = redirects[current]
            redirected = True
            continue
        # Path-only fallback for redirects without matching query/fragment
        path_key = path_only(current)
        if path_key in redirects:
            current = redirects[path_key]
            redirected = True
            continue
        fragment = url_fragment(current)
        if fragment is not None:
            exact_frag = [
                k
                for k in redirects
                if path_only(k) == path_key and url_fragment(k) == fragment
            ]
            if exact_frag:
                current = redirects[exact_frag[0]]
                redirected = True
                continue
        else:
            path_matches = [
                k for k in redirects if path_only(k) == path_key and k != current and "#" not in k
            ]
            if path_matches:
                current = redirects[sorted(path_matches, key=len)[0]]
                redirected = True
                continue
        doc = url_to_markdown(current)
        if doc and doc.is_file():
            return current, "redirect_resolved" if redirected else "canonical_exists"
        return current, "manual_required"
    return current, "redirect_loop"


def url_to_markdown(url: str) -> Path | None:
    url = path_only(url)
    if not url.startswith("/docs/"):
        return None
    rest = url[len("/docs/") :]
    if not rest:
        return DOCS_ROOT / "_home.md" if (DOCS_ROOT / "_home.md").exists() else None
    parts = rest.split("/")
    collection = parts[0]
    sub = "/".join(parts[1:])
    if sub:
        return DOCS_ROOT / f"_{collection}" / f"{sub}.md"
    return DOCS_ROOT / f"_{collection}.md"


def nearest_heading_and_sentence(content: str, link_substring: str) -> tuple[str, str]:
    """Find section heading and sentence containing the link."""
    lines = content.splitlines()
    current_heading = "(top of page)"
    best_sentence = ""
    for i, line in enumerate(lines):
        hm = HEADING_RE.match(line)
        if hm and int(hm.group(1).count("#")) <= 4:
            current_heading = hm.group(2).strip()
        if link_substring in line or path_only(link_substring) in line:
            # extract sentence around link
            chunk = line
            if len(chunk) < 20 and i + 1 < len(lines):
                chunk = line + " " + lines[i + 1]
            # strip markdown noise for display
            chunk = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", chunk)
            chunk = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", chunk)
            chunk = re.sub(r"\{\{[^}]+\}\}", "", chunk)
            chunk = re.sub(r"\s+", " ", chunk).strip()
            if len(chunk) > 200:
                idx = chunk.find(link_substring.split("/")[-1])
                if idx < 0:
                    idx = 0
                start = max(0, idx - 80)
                chunk = ("..." if start > 0 else "") + chunk[start : start + 180] + "..."
            best_sentence = chunk
            break
    return current_heading, best_sentence or "(link not found in source scan)"


def scan_file_links(md_path: Path) -> list[tuple[str, str]]:
    """Return list of (link_url, link_text) from markdown."""
    content = md_path.read_text(encoding="utf-8", errors="replace")
    # strip code blocks
    content = re.sub(r"``````[\s\S]*?``````|```[\s\S]*?```", "", content)
    found: list[tuple[str, str]] = []
    for m in LINK_INLINE_RE.finditer(content):
        raw = m.group(2).strip()
        raw = raw.replace("{{site.baseurl}}", "").replace("{{ site.baseurl }}", "")
        raw = raw.split("#")[0].split("?")[0].strip()
        if raw.startswith("/") and "." not in raw.split("/")[-1]:
            found.append((raw, m.group(1)))
    return found


def load_broken_csv(path: Path) -> list[dict]:
    rows = []
    if not path.is_file():
        return rows
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def load_pages_filter(path: Path | None) -> set[str] | None:
    if not path or not path.is_file():
        return None
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description="Verified link fix table generator")
    parser.add_argument(
        "--broken-links",
        type=Path,
        default=REPO_ROOT / "scripts/temp/broken-links.csv",
    )
    parser.add_argument("--pages-file", type=Path, help="Limit to these doc paths")
    parser.add_argument("--out", type=Path, default=REPO_ROOT / "scripts/temp/link-fix-table.csv")
    parser.add_argument("--scan-all", action="store_true", help="Scan all links, not only broken CSV")
    args = parser.parse_args()

    redirects = load_redirect_map()
    page_filter = load_pages_filter(args.pages_file)
    out_rows: list[dict] = []

    if args.scan_all or not args.broken_links.is_file():
        md_files = sorted(DOCS_ROOT.rglob("*.md"))
        if page_filter:
            md_files = [p for p in md_files if str(p.relative_to(REPO_ROOT)) in page_filter]
        for md_path in md_files:
            rel = str(md_path.relative_to(REPO_ROOT))
            if skips_seo_audit(rel):
                continue
            content = md_path.read_text(encoding="utf-8", errors="replace")
            for link, text in scan_file_links(md_path):
                full = ensure_docs_path(link)
                source_doc = url_to_markdown(full)
                if source_doc and source_doc.is_file():
                    continue
                final, status = resolve_redirect(full, redirects)
                if status == "canonical_exists":
                    continue
                if status in ("redirect_resolved", "manual_required", "redirect_loop"):
                    heading, sentence = nearest_heading_and_sentence(content, link)
                    out_rows.append(
                        {
                            "source_file": rel,
                            "section_heading": heading,
                            "surrounding_sentence": sentence,
                            "link_text": text,
                            "current_url": full,
                            "verified_replacement": final if status != "manual_required" else "",
                            "status": status,
                        }
                    )
    else:
        broken = load_broken_csv(args.broken_links)
        for row in broken:
            source = row.get("File", "").strip()
            if skips_seo_audit(source):
                continue
            if page_filter and source not in page_filter:
                continue
            current = row.get("Broken Link", "").strip()
            md_path = REPO_ROOT / source
            content = md_path.read_text(encoding="utf-8", errors="replace") if md_path.is_file() else ""
            link_path = current.replace("https://www.braze.com", "")
            if not link_path.startswith("/docs"):
                link_path = extract_docs_path(current) or link_path
            final, status = resolve_redirect(link_path, redirects)
            heading, sentence = nearest_heading_and_sentence(content, current)
            out_rows.append(
                {
                    "source_file": source,
                    "section_heading": heading,
                    "surrounding_sentence": sentence,
                    "link_text": "",
                    "current_url": ensure_docs_path(link_path),
                    "verified_replacement": final if status != "manual_required" else "",
                    "status": status,
                }
            )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "source_file",
        "section_heading",
        "surrounding_sentence",
        "link_text",
        "current_url",
        "verified_replacement",
        "status",
    ]
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out_rows)

    print(f"Wrote {len(out_rows)} link fix rows to {args.out}")
    # only show fixable
    fixable = [r for r in out_rows if r["verified_replacement"] and r["status"] != "manual_required"]
    print(f"  {len(fixable)} with verified replacements")
    return 0


if __name__ == "__main__":
    sys.exit(main())
