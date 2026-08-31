#!/usr/bin/env python3
"""Apply no-approval SEO fixes from audit outputs."""

from __future__ import annotations

import argparse
import csv
import html
import re
import sys
from pathlib import Path

from anchor_utils import normalize_fragment, sanitize_fragment_for_target
from meta_exempt import parse_frontmatter, skips_seo_audit, skips_seo_meta

REPO_ROOT = Path(__file__).resolve().parents[2]
FRONTMATTER_RE = re.compile(r"^(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)
META_ROW_RE = re.compile(
    r"^\| `(article_title|description)` \| (.+?) \| `([^`]+)` \| (.+) \|$",
    re.MULTILINE,
)


def unescape_table(value: str) -> str:
    return html.unescape(value.replace("&#58;", ":"))


def format_frontmatter_value(value: str) -> str:
    if value.startswith('"') and value.endswith('"'):
        return value
    return f'"{value}"'


def apply_frontmatter_fixes(text: str, fixes: dict[str, str]) -> tuple[str, list[str]]:
    applied: list[str] = []
    m = FRONTMATTER_RE.match(text)
    if not m or not fixes:
        return text, applied
    prefix, body, suffix = m.group(1), m.group(2), m.group(3)
    lines = body.splitlines()
    out_lines: list[str] = []
    present_keys: set[str] = set()
    for line in lines:
        if ":" not in line:
            out_lines.append(line)
            continue
        key, _, _val = line.partition(":")
        key = key.strip()
        present_keys.add(key)
        if key not in fixes:
            out_lines.append(line)
            continue
        new_val = fixes[key]
        out_lines.append(f"{key}: {format_frontmatter_value(new_val)}")
        applied.append(key)

    missing = {k: v for k, v in fixes.items() if k not in present_keys}
    if missing:
        insert_at = len(out_lines)
        for i, line in enumerate(out_lines):
            if line.partition(":")[0].strip() == "article_title":
                insert_at = i + 1
                break
        for key in ("description", "article_title"):
            if key in missing:
                out_lines.insert(insert_at, f"{key}: {format_frontmatter_value(missing[key])}")
                applied.append(key)
                insert_at += 1

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
                if recommended.strip().startswith("<"):
                    continue
                if "(missing)" in current_raw:
                    if recommended.startswith(("Content Cards >", "Learn about")):
                        recommended = recommended.split(">", 1)[-1].strip()
                    page_fixes[field] = recommended
                elif "chars)" in current_raw:
                    page_fixes[field] = recommended
            elif field == "article_title":
                current = unescape_table(current_raw.strip("`"))
                if current != recommended:
                    page_fixes[field] = recommended
        if page_fixes:
            md_path = REPO_ROOT / rel
            if md_path.is_file() and skips_seo_meta(parse_frontmatter(md_path.read_text(encoding="utf-8")), rel):
                page_fixes = {
                    k: v for k, v in page_fixes.items() if k not in ("description", "article_title")
                }
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


def build_link_replacements(rows: list[dict]) -> list[tuple[re.Pattern[str], object]]:
    """Return regex replacements sorted longest-path-first to avoid prefix collisions."""
    specs: list[tuple[str, str, str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        if row.get("status") != "redirect_resolved":
            continue
        old = row.get("current_url", "").strip()
        new = row.get("verified_replacement", "").strip()
        if not old or not new:
            continue
        pair = (old, new)
        if pair in seen:
            continue
        seen.add(pair)
        old_base, _old_query, _old_frag = split_url(old)
        _new_base, new_query, new_frag = split_url(new)
        old_tail = docs_tail(old_base)
        new_tail = docs_tail(_new_base)
        if not old_tail or old_tail == new_tail:
            continue
        specs.append((old, old_tail, new_tail, new_query, new_frag))

    specs.sort(key=lambda s: len(s[1]), reverse=True)

    replacements: list[tuple[re.Pattern[str], object]] = []
    suffix_pat = r"(?P<query>\?[^)#\s\"]*)?(?P<frag>#[^)\s\"]*)?"
    for old, old_tail, new_tail, new_query, new_frag in specs:
        tail_escaped = re.escape(old_tail.rstrip("/"))

        def liquid_replacer(
            match: re.Match[str],
            *,
            tail: str = new_tail,
            csv_query: str = new_query,
            csv_frag: str = new_frag,
        ) -> str:
            query = f"?{csv_query}" if csv_query else (match.group("query") or "")
            raw_frag = csv_frag or (match.group("frag") or "")
            frag_value = normalize_fragment(raw_frag.lstrip("#")) if raw_frag else ""
            if frag_value:
                frag_value = sanitize_fragment_for_target(tail, frag_value)
            frag = f"#{frag_value}" if frag_value else ""
            return f"{{{{site.baseurl}}}}/{tail}{query}{frag}"

        def docs_replacer(
            match: re.Match[str],
            *,
            tail: str = new_tail,
            csv_query: str = new_query,
            csv_frag: str = new_frag,
        ) -> str:
            query = f"?{csv_query}" if csv_query else (match.group("query") or "")
            raw_frag = csv_frag or (match.group("frag") or "")
            frag_value = normalize_fragment(raw_frag.lstrip("#")) if raw_frag else ""
            if frag_value:
                frag_value = sanitize_fragment_for_target(tail, frag_value)
            frag = f"#{frag_value}" if frag_value else ""
            return f"/docs/{tail}{query}{frag}"

        liquid_pat = re.compile(
            r"\{\{site\.baseurl\}\}/" + tail_escaped + suffix_pat + r"(?!/)"
        )
        replacements.append((liquid_pat, liquid_replacer))

        if old.startswith("/docs"):
            docs_pat = re.compile(r"/docs/" + tail_escaped + suffix_pat + r"(?!/)")
            replacements.append((docs_pat, docs_replacer))

        replacements.append((re.compile(re.escape(old)), new))
    return replacements


def apply_link_fixes(text: str, rows: list[dict]) -> tuple[str, int]:
    count = 0
    for pattern, repl in build_link_replacements(rows):
        if callable(repl):
            text, n = pattern.subn(repl, text)
        else:
            text, n = pattern.subn(str(repl), text)
        count += n
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
        default=REPO_ROOT / "scripts/temp/link-fix-table-pilot.csv",
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
    else:
        print(f"Warning: link fix CSV not found: {args.link_fix_csv}", file=sys.stderr)

    changed_files: list[str] = []
    for rel, fixes in sorted(meta_fixes.items()):
        if skips_seo_audit(rel):
            continue
        md = REPO_ROOT / rel
        if not md.is_file():
            print(f"Skip missing {rel}", file=sys.stderr)
            continue
        text = md.read_text(encoding="utf-8")
        if skips_seo_meta(parse_frontmatter(text), rel):
            fixes = {k: v for k, v in fixes.items() if k not in ("description", "article_title")}
            if not fixes:
                continue
        new_text, applied_meta = apply_frontmatter_fixes(text, fixes)
        new_text, link_count = apply_link_fixes(new_text, link_by_file.get(rel, []))
        if new_text != text:
            md.write_text(new_text, encoding="utf-8")
            changed_files.append(f"{rel} (meta: {applied_meta}, links: {link_count})")

    for rel, rows in sorted(link_by_file.items()):
        if skips_seo_audit(rel):
            continue
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
