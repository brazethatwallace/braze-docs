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

REPO_ROOT = Path(__file__).resolve().parents[2]
REDIRECT_JS = REPO_ROOT / "assets" / "js" / "broken_redirect_list.js"
DOCS_ROOT = REPO_ROOT / "_docs"

REDIRECT_RE = re.compile(
    r"validurls\['/docs([^']*)'\]\s*=\s*'/docs([^']*)';"
)
LINK_INLINE_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")


def normalize_path(path: str) -> str:
    path = path.strip()
    if not path.startswith("/docs"):
        path = "/docs" + path if path.startswith("/") else "/docs/" + path
    # strip query/fragment for redirect lookup
    path = path.split("?")[0].split("#")[0]
    return path.rstrip("/") or "/docs"


def load_redirect_map() -> dict[str, str]:
    text = REDIRECT_JS.read_text(encoding="utf-8")
    mapping: dict[str, str] = {}
    for m in REDIRECT_RE.finditer(text):
        old_p, new_p = m.group(1), m.group(2)
        old_key = normalize_path(f"/docs{old_p}")
        new_val = normalize_path(f"/docs{new_p}")
        mapping[old_key] = new_val
        mapping[old_key + "/"] = new_val
    return mapping


def resolve_redirect(url: str, redirects: dict[str, str], max_hops: int = 10) -> tuple[str, str]:
    """Return (final_url, status)."""
    current = normalize_path(url)
    seen = set()
    for _ in range(max_hops):
        if current in seen:
            return current, "redirect_loop"
        seen.add(current)
        if current in redirects:
            current = redirects[current]
            continue
        # file exists check
        doc = url_to_markdown(current)
        if doc and doc.is_file():
            return current, "redirect_resolved" if len(seen) > 1 else "canonical_exists"
        return current, "manual_required"
    return current, "redirect_loop"


def url_to_markdown(url: str) -> Path | None:
    url = normalize_path(url)
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
        if link_substring in line or normalize_path(link_substring) in line:
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
            content = md_path.read_text(encoding="utf-8", errors="replace")
            for link, text in scan_file_links(md_path):
                full = normalize_path(link)
                final, status = resolve_redirect(full, redirects)
                doc = url_to_markdown(final)
                if doc and doc.is_file() and normalize_path(full) == normalize_path(final):
                    continue
                if status == "manual_required" or normalize_path(full) != normalize_path(final):
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
            if page_filter and source not in page_filter:
                continue
            current = row.get("Broken Link", "").strip()
            md_path = REPO_ROOT / source
            content = md_path.read_text(encoding="utf-8", errors="replace") if md_path.is_file() else ""
            link_path = current.replace("https://www.braze.com", "").split("?")[0]
            final, status = resolve_redirect(link_path, redirects)
            heading, sentence = nearest_heading_and_sentence(content, current)
            out_rows.append(
                {
                    "source_file": source,
                    "section_heading": heading,
                    "surrounding_sentence": sentence,
                    "link_text": "",
                    "current_url": normalize_path(link_path),
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
