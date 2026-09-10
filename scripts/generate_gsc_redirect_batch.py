#!/usr/bin/env python3
"""
Generate locale mirrors, liquid-leak fixes, and double-locale redirects from a
GSC 404 drilldown export, then optionally fill remaining Vercel bulk budget with
legacy-IA locale mirrors.

Usage:
  python3 scripts/generate_gsc_redirect_batch.py --gsc-csv /path/to/Table.csv
  python3 scripts/generate_gsc_redirect_batch.py --gsc-csv /path/to/Table-failed-only.csv --failed-only --path-regex custom_objects --apply --marker "// GSC ..."
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

from locale_redirect_utils import (
    LOCALES,
    LOCALE_IN_PATH,
    add_locale_prefix,
    format_validurl_line,
    is_bulk_eligible_source,
    is_en_bulk_source,
    parse_validurls,
    strip_locale_prefix,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REDIRECT_JS = PROJECT_ROOT / "assets/js/broken_redirect_list.js"
BULK_JSON = PROJECT_ROOT / "assets/redirects/bulk-redirects.json"

LOCALE_SEGMENT = r"(?:ko|es|fr|pt-br|ja|de)"
DOUBLE_LOCALE_RE = re.compile(rf"^/docs/({LOCALE_SEGMENT})/\1(/.*)$")

LEGACY_IA_MARKERS = (
    "engagement_tools",
    "message_building_by_channel",
    "platform_integration_guides",
    "data_and_analytics",
    "personalization_and_dynamic_content",
    "administrative",
    "platform_wide",
    "data_and_infrastructure_agility",
    "message_orchestration",
)


def normalize_gsc_path(url: str) -> str:
    return url.replace("https://www.braze.com", "").rstrip("/")


def split_path_query(path: str) -> tuple[str, str]:
    if "?" not in path:
        return path.rstrip("/"), ""
    base, query = path.split("?", 1)
    return base.rstrip("/"), f"?{query}"


def join_path_query(path: str, query: str) -> str:
    if not query or "?" in path:
        return path
    return path.rstrip("/") + query


def is_legacy_ia(path: str) -> bool:
    return any(marker in path for marker in LEGACY_IA_MARKERS)


def liquid_leak_destination(path: str) -> str | None:
    parts = re.split(r"\{\{site\.baseurl\}\}/?", path, maxsplit=1)
    if len(parts) != 2 or not parts[1]:
        return None
    dest = parts[1]
    if not dest.startswith("/docs/"):
        dest = f"/docs/{dest.lstrip('/')}"
    locale, _ = strip_locale_prefix(path)
    if locale and not LOCALE_IN_PATH.match(dest):
        dest = add_locale_prefix(locale, dest)
    return dest


def count_bulk_export(validurls: dict[str, str]) -> int:
    seen: set[str] = set()
    count = 0
    for source, destination in validurls.items():
        if "#" in source.split("?", 1)[0] or "?" in source:
            continue
        norm_source = source.rstrip("/").lower()
        norm_dest = destination.rstrip("/").lower()
        if not norm_source.startswith("/"):
            continue
        if norm_source == norm_dest:
            continue
        if norm_source in seen:
            continue
        seen.add(norm_source)
        count += 1
    return count


def build_entries(
    gsc_paths: list[str],
    validurls: dict[str, str],
    fill_legacy_mirrors: bool,
    max_bulk: int,
) -> tuple[dict[str, str], dict[str, int]]:
    existing = dict(validurls)
    entries: dict[str, str] = {}
    stats = Counter()

    def add(source: str, dest: str, kind: str) -> None:
        dest_base, dest_query = split_path_query(dest)
        if source == dest or source == dest_base:
            stats[f"skip_identity_{kind}"] += 1
            return
        if source in existing:
            stats[f"skip_exists_{kind}"] += 1
            return
        if source in entries:
            if entries[source] != dest and entries[source] != dest_base:
                entries[source] = dest_base
                stats[f"merge_query_conflict_{kind}"] += 1
            return
        entries[source] = join_path_query(dest_base, dest_query)
        stats[kind] += 1

    locale_freq = Counter()
    for path in gsc_paths:
        locale, en_path = strip_locale_prefix(path)
        if locale:
            locale_freq[en_path] += 1

    for path in gsc_paths:
        path_only, query = split_path_query(path)

        if "{{site.baseurl}}" in path_only:
            dest = liquid_leak_destination(path_only)
            if dest:
                add(path_only, join_path_query(dest, query), "liquid_leak")
            continue

        double = DOUBLE_LOCALE_RE.match(path_only)
        if double:
            fixed = f"/docs/{double.group(1)}{double.group(2)}".rstrip("/")
            add(path_only, join_path_query(fixed, query), "double_locale")
            continue

        locale, en_path = strip_locale_prefix(path_only)
        if locale and en_path in existing:
            ldest = add_locale_prefix(locale, existing[en_path])
            add(path_only, join_path_query(ldest, query), "gsc_mirror")

    if fill_legacy_mirrors:
        current_bulk = count_bulk_export(existing)
        projected = current_bulk + sum(
            1 for source in entries if is_bulk_eligible_source(source)
        )
        candidates: list[tuple[int, str, str]] = []
        for src, dest in existing.items():
            if not is_en_bulk_source(src) or not is_legacy_ia(src):
                continue
            score = locale_freq.get(src, 0)
            for locale in LOCALES:
                lsrc = add_locale_prefix(locale, src)
                ldest = add_locale_prefix(locale, dest)
                if lsrc in existing or lsrc in entries or lsrc == ldest:
                    continue
                candidates.append((score, lsrc, ldest))

        candidates.sort(key=lambda row: (-row[0], row[1]))
        for _, lsrc, ldest in candidates:
            if is_bulk_eligible_source(lsrc):
                projected += 1
                if projected > max_bulk:
                    break
            add(lsrc, ldest, "legacy_mirror")

    stats["total"] = len(entries)
    return entries, dict(stats)


def filter_entries(
    entries: dict[str, str],
    include_regex: re.Pattern[str] | None,
    exclude_regex: re.Pattern[str] | None,
) -> dict[str, str]:
    filtered: dict[str, str] = {}
    for source, dest in entries.items():
        if include_regex and not include_regex.search(source):
            continue
        if exclude_regex and exclude_regex.search(source):
            continue
        filtered[source] = dest
    return filtered


def apply_entries(js_path: Path, entries: dict[str, str], marker: str) -> None:
    text = js_path.read_text(encoding="utf-8")
    if marker in text:
        raise SystemExit(f"Marker already present in {js_path}; remove block before re-applying")

    block_lines = [
        marker,
        *sorted(format_validurl_line(source, dest) for source, dest in entries.items()),
        "",
    ]
    block = "\n".join(block_lines)
    placeholder = "// validurls['OLD'] = 'NEW';"
    if placeholder not in text:
        raise SystemExit(f"Placeholder not found in {js_path}")

    js_path.write_text(text.replace(placeholder, f"{block}\n{placeholder}", 1), encoding="utf-8")


def load_gsc_paths(csv_path: Path, failed_only: bool) -> list[str]:
    paths: set[str] = set()
    with csv_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if failed_only and row.get("Status", "").lower() != "failed":
                continue
            url = row.get("URL", "").strip()
            if url:
                paths.add(normalize_gsc_path(url))
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gsc-csv", type=Path, required=True)
    parser.add_argument(
        "--failed-only",
        action="store_true",
        help="Only read rows with Status=Failed from the GSC export",
    )
    parser.add_argument(
        "--path-regex",
        type=str,
        default="",
        help="Only apply generated entries whose source matches this regex",
    )
    parser.add_argument(
        "--exclude-regex",
        type=str,
        default="",
        help="Drop generated entries whose source matches this regex",
    )
    parser.add_argument(
        "--fill-legacy-mirrors",
        action="store_true",
        help="Add legacy-IA locale mirrors until --max-bulk is reached",
    )
    parser.add_argument("--max-bulk", type=int, default=9500)
    parser.add_argument(
        "--marker",
        type=str,
        default="",
        help="Comment marker for the inserted block (required with --apply)",
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if not args.gsc_csv.is_file():
        print(f"CSV not found: {args.gsc_csv}", file=sys.stderr)
        return 1

    gsc_paths = load_gsc_paths(args.gsc_csv, args.failed_only)
    js_text = REDIRECT_JS.read_text(encoding="utf-8")
    validurls = parse_validurls(js_text)
    entries, stats = build_entries(
        gsc_paths, validurls, args.fill_legacy_mirrors, args.max_bulk
    )

    include_re = re.compile(args.path_regex) if args.path_regex else None
    exclude_re = re.compile(args.exclude_regex) if args.exclude_regex else None
    entries = filter_entries(entries, include_re, exclude_re)

    current_bulk = len(json.loads(BULK_JSON.read_text())) if BULK_JSON.is_file() else 0
    merged = dict(validurls)
    merged.update(entries)
    projected_bulk = count_bulk_export(merged)

    print(f"GSC paths: {len(gsc_paths)}")
    for key in sorted(stats):
        if key != "total":
            print(f"  {key}: {stats[key]}")
    print(f"New entries after filter: {len(entries)}")
    print(f"Current bulk redirects: {current_bulk}")
    print(f"Projected bulk redirects: {projected_bulk}")

    if not args.apply:
        print("\nDry run. Re-run with --apply to write broken_redirect_list.js")
        return 0

    marker = args.marker or (
        f"// GSC {args.gsc_csv.stem}: locale mirrors, liquid leaks, "
        "and legacy-IA fill"
    )
    if not entries:
        print("No entries to apply after filtering.", file=sys.stderr)
        return 1

    apply_entries(REDIRECT_JS, entries, marker)
    print(f"\nWrote {len(entries)} entries to {REDIRECT_JS.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
