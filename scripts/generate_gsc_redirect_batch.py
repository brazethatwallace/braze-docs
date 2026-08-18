#!/usr/bin/env python3
"""
Generate locale mirrors, liquid-leak fixes, and double-locale redirects from a
GSC 404 drilldown export, then optionally fill remaining Vercel bulk budget with
legacy-IA locale mirrors.

Usage:
  python3 scripts/generate_gsc_redirect_batch.py --gsc-csv /path/to/Table.csv
  python3 scripts/generate_gsc_redirect_batch.py --gsc-csv /path/to/Table.csv --fill-legacy-mirrors --max-bulk 9500 --apply
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REDIRECT_JS = PROJECT_ROOT / "assets/js/broken_redirect_list.js"
BULK_JSON = PROJECT_ROOT / "assets/redirects/bulk-redirects.json"

LOCALES = ("ko", "es", "fr", "pt-br", "ja", "de")
LOCALE_SEGMENT = r"(?:ko|es|fr|pt-br|ja|de)"
LOCALE_IN_PATH = re.compile(rf"^/docs/{LOCALE_SEGMENT}(/|$)")
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

VALIDURLS_RE = re.compile(
    r"validurls\['((?:\\'|[^'])*)'\]\s*=\s*'((?:\\'|[^'])*)'\s*;"
)


def unescape_js_string(value: str) -> str:
    return value.replace("\\'", "'")


def escape_js_string(value: str) -> str:
    return value.replace("'", "\\'")


def parse_validurls(js_text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in js_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("//"):
            continue
        match = VALIDURLS_RE.search(stripped)
        if not match:
            continue
        source = unescape_js_string(match.group(1))
        dest = unescape_js_string(match.group(2))
        entries[source] = dest
    return entries


def normalize_gsc_path(url: str) -> str:
    return url.replace("https://www.braze.com", "").rstrip("/")


def split_path_query(path: str) -> tuple[str, str]:
    """Return (path_without_query, ?query_suffix)."""
    if "?" not in path:
        return path.rstrip("/"), ""
    base, query = path.split("?", 1)
    return base.rstrip("/"), f"?{query}"


def join_path_query(path: str, query: str) -> str:
    if not query or "?" in path:
        return path
    return path.rstrip("/") + query


def strip_locale_prefix(path: str) -> tuple[str | None, str]:
    match = re.match(rf"^/docs/({LOCALE_SEGMENT})(/.*)$", path)
    if not match:
        return None, path
    return match.group(1), f"/docs{match.group(2)}"


def add_locale_prefix(locale: str, path: str) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        return path
    if LOCALE_IN_PATH.match(path):
        return path
    if path.startswith("/docs/"):
        return f"/docs/{locale}{path[5:]}"
    return path


def is_en_bulk_source(path: str) -> bool:
    if not path.startswith("/docs/"):
        return False
    if LOCALE_IN_PATH.match(path):
        return False
    if "#" in path.split("?", 1)[0]:
        return False
    if "?" in path:
        return False
    return True


def is_bulk_eligible_source(path: str) -> bool:
    base = path.split("?", 1)[0]
    return "#" not in base and "?" not in path


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


def format_validurl_line(source: str, dest: str) -> str:
    return (
        f"validurls['{escape_js_string(source)}'] = "
        f"'{escape_js_string(dest)}';"
    )


def count_bulk_export(validurls: dict[str, str]) -> int:
  # lightweight mirror of generate_bulk_redirects rules
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
                # Same pathname, different tab query — use generic destination.
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
            # Prefer mirrored EN destination; only append GSC query when EN dest has none.
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gsc-csv", type=Path, required=True)
    parser.add_argument(
        "--fill-legacy-mirrors",
        action="store_true",
        help="Add legacy-IA locale mirrors until --max-bulk is reached",
    )
    parser.add_argument("--max-bulk", type=int, default=9500)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if not args.gsc_csv.is_file():
        print(f"CSV not found: {args.gsc_csv}", file=sys.stderr)
        return 1

    gsc_paths = sorted(
        {
            normalize_gsc_path(row["URL"].strip())
            for row in csv.DictReader(args.gsc_csv.open(encoding="utf-8"))
            if row.get("URL", "").strip()
        }
    )

    js_text = REDIRECT_JS.read_text(encoding="utf-8")
    validurls = parse_validurls(js_text)
    entries, stats = build_entries(
        gsc_paths, validurls, args.fill_legacy_mirrors, args.max_bulk
    )

    current_bulk = len(json.loads(BULK_JSON.read_text())) if BULK_JSON.is_file() else 0
    merged = dict(validurls)
    merged.update(entries)
    projected_bulk = count_bulk_export(merged)

    print(f"GSC paths: {len(gsc_paths)}")
    for key in sorted(stats):
        if key != "total":
            print(f"  {key}: {stats[key]}")
    print(f"New entries: {stats.get('total', 0)}")
    print(f"Current bulk redirects: {current_bulk}")
    print(f"Projected bulk redirects: {projected_bulk}")

    if not args.apply:
        print("\nDry run. Re-run with --apply to write broken_redirect_list.js")
        return 0

    marker = (
        f"// GSC {args.gsc_csv.stem}: locale mirrors, liquid leaks, "
        "and legacy-IA fill"
    )
    apply_entries(REDIRECT_JS, entries, marker)
    print(f"\nWrote {len(entries)} entries to {REDIRECT_JS.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
