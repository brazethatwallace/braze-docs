#!/usr/bin/env python3
"""Apply no-approval SEO fixes from wave-2 audit outputs."""

from __future__ import annotations

import argparse
import csv
import html
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FRONTMATTER_RE = re.compile(r"^(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)
META_ROW_RE = re.compile(
    r"^\| `(article_title|description)` \| (.+?) \| `([^`]+)` \| (.+) \|$",
    re.MULTILINE,
)


def unescape_table(value: str) -> str:
    return html.unescape(value.replace("&#58;", ":"))


def apply_frontmatter_fixes(text: str, fixes: dict[str, str]) -> tuple[str, list[str]]:
    applied: list[str] = []
    m = FRONTMATTER_RE.match(text)
    if not m or not fixes:
        return text, applied
    prefix, body, suffix = m.group(1), m.group(2), m.group(3)
    lines = body.splitlines()
    out_lines: list[str] = []
    for line in lines:
        if ":" not in line:
            out_lines.append(line)
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        if key not in fixes:
            out_lines.append(line)
            continue
        new_val = fixes[key]
        if new_val.startswith('"') or new_val.endswith('"'):
            out_lines.append(f'{key}: {new_val}')
        else:
            out_lines.append(f'{key}: "{new_val}"')
        applied.append(key)
    if not applied:
        return text, applied
    return prefix + "\n".join(out_lines) + suffix + text[m.end() :], applied


def parse_recommendations(rec_dir: Path) -> dict[str, dict[str, str]]:
    fixes: dict[str, dict[str, str]] = {}
    for path in sorted(rec_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        source_m = re.search(r"\*\*Source:\*\* `([^`]+)`", content)
        if not source_m:
            continue
        rel = source_m.group(1)
        page_fixes: dict[str, str] = {}
        for m in META_ROW_RE.finditer(content):
            field, current_raw, recommended, _rationale = m.groups()
            current_raw = current_raw.strip()
            recommended = unescape_table(recommended)
            if field == "description":
                if "(missing)" in current_raw:
                    if recommended.startswith(("Content Cards >", "Learn about")):
                        recommended = recommended.split(">", 1)[-1].strip()
                    page_fixes[field] = recommended
                elif "chars)" in current_raw or len(recommended) <= 150:
                    page_fixes[field] = recommended
            elif field == "article_title":
                current = unescape_table(current_raw.strip("`"))
                if current != recommended:
                    page_fixes[field] = recommended
        if page_fixes:
            fixes[rel] = page_fixes
    return fixes


def docs_tail(path: str) -> str:
    path = path.strip()
    if path.startswith("/docs/"):
        path = path[len("/docs/") :]
    elif path.startswith("/docs"):
        path = path[len("/docs") :].lstrip("/")
    return path.lstrip("/")


def split_url(url: str) -> tuple[str, str, str]:
    base, _, frag = url.partition("#")
    base, _, query = base.partition("?")
    return base, query, frag


def apply_link_fixes(text: str, rows: list[dict]) -> tuple[str, int]:
    count = 0
    seen_pairs: set[tuple[str, str]] = set()
    for row in rows:
        if row.get("status") != "redirect_resolved":
            continue
        old = row.get("current_url", "").strip()
        new = row.get("verified_replacement", "").strip()
        if not old or not new:
            continue
        pair = (old, new)
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)

        old_base, old_query, old_frag = split_url(old)
        new_base, new_query, new_frag = split_url(new)
        old_tail = docs_tail(old_base)
        new_tail = docs_tail(new_base)
        if not old_tail or old_tail == new_tail:
            continue

        replacements: list[tuple[str, str]] = [
            (old, new),
            (old_base, new_base + (f"?{new_query}" if new_query else "") + (f"#{new_frag}" if new_frag else "")),
            (old_base.rstrip("/"), new_base.rstrip("/")),
        ]
        # site.baseurl links (with optional query/fragment on the old URL)
        old_liquid = re.escape(f"{{{{site.baseurl}}}}/{old_tail}")
        new_liquid_base = f"{{{{site.baseurl}}}}/{new_tail}"
        text, n = re.subn(
            old_liquid + r"(?:\?[^)#\s]*)?(?:#[^)\s]*)?",
            new_liquid_base
            + (f"?{new_query}" if new_query else "")
            + (f"#{new_frag or old_frag}" if (new_frag or old_frag) else ""),
            text,
        )
        count += n
        for a, b in replacements:
            if a and a in text:
                text = text.replace(a, b)
                count += 1
    return text, count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recommendations",
        type=Path,
        default=REPO_ROOT / "docs/seo_pilot/recommendations",
    )
    parser.add_argument(
        "--link-fix-csv",
        type=Path,
        default=REPO_ROOT / "scripts/temp/link-fix-table-ga-top100.csv",
    )
    args = parser.parse_args()

    meta_fixes = parse_recommendations(args.recommendations)
    link_by_file: dict[str, list[dict]] = {}
    if args.link_fix_csv.is_file():
        with args.link_fix_csv.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("status") != "redirect_resolved":
                    continue
                src = row.get("source_file", "")
                link_by_file.setdefault(src, []).append(row)

    changed_files: list[str] = []
    for rel, fixes in sorted(meta_fixes.items()):
        md = REPO_ROOT / rel
        if not md.is_file():
            print(f"Skip missing {rel}", file=sys.stderr)
            continue
        text = md.read_text(encoding="utf-8")
        new_text, applied_meta = apply_frontmatter_fixes(text, fixes)
        new_text, link_count = apply_link_fixes(new_text, link_by_file.get(rel, []))
        if new_text != text:
            md.write_text(new_text, encoding="utf-8")
            changed_files.append(f"{rel} (meta: {applied_meta}, links: {link_count})")

    # Files with link-only fixes
    for rel, rows in sorted(link_by_file.items()):
        if rel in meta_fixes:
            continue
        md = REPO_ROOT / rel
        if not md.is_file():
            continue
        text = md.read_text(encoding="utf-8")
        new_text, link_count = apply_link_fixes(text, rows)
        if new_text != text and link_count:
            md.write_text(new_text, encoding="utf-8")
            changed_files.append(f"{rel} (links: {link_count})")

    print(f"Updated {len(changed_files)} files:")
    for line in changed_files:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
