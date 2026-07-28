#!/usr/bin/env python3
"""
Generate locale-prefixed validurls entries by mirroring English redirects.

For each English validurls mapping OLD -> NEW, creates locale variants:
  /docs/{locale}/path -> /docs/{locale}/dest

Skips entries that already exist, use fragment/query sources (client-side only),
or point to external URLs without a /docs/ destination.

Usage:
  python3 scripts/generate_locale_mirror_validurls.py --gsc-csv /path/to/Table.csv
  python3 scripts/generate_locale_mirror_validurls.py --gsc-csv /path/to/Table.csv --apply
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REDIRECT_JS = PROJECT_ROOT / "assets/js/broken_redirect_list.js"

LOCALES = ("ko", "es", "fr", "pt-br", "ja", "de")
LOCALE_SEGMENT = r"(?:ko|es|fr|pt-br|ja|de)"
LOCALE_IN_PATH = re.compile(rf"^/docs/{LOCALE_SEGMENT}(/|$)")

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


def strip_locale_prefix(path: str) -> tuple[str | None, str]:
    """Return (locale, en_path) or (None, path) when no locale prefix."""
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


def source_eligible_for_bulk(source: str) -> bool:
    path = source.split("?", 1)[0]
    return "#" not in path and "?" not in source


def load_gsc_locale_404_urls(csv_path: Path) -> list[str]:
    urls: list[str] = []
    with csv_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("Status", "").lower() != "failed":
                continue
            url = row.get("URL", "").strip()
            if not url or "{{site.baseurl}}" in url:
                continue
            if not re.search(rf"/docs/{LOCALE_SEGMENT}/", url):
                continue
            result = subprocess.run(
                [
                    "curl",
                    "-sgI",
                    "-o",
                    "/dev/null",
                    "-w",
                    "%{http_code}",
                    "-A",
                    "Googlebot",
                    "--max-time",
                    "12",
                    url,
                ],
                capture_output=True,
                text=True,
            )
            if result.stdout.strip() == "404":
                path = url.replace("https://www.braze.com", "").rstrip("/")
                urls.append(path)
    return sorted(set(urls))


def mirror_entries(
    locale_paths: list[str], validurls: dict[str, str]
) -> tuple[list[tuple[str, str]], list[str]]:
    """Return (new_entries, skipped_reasons)."""
    new_entries: list[tuple[str, str]] = []
    skipped: list[str] = []

    for locale_path in locale_paths:
        if locale_path in validurls:
            skipped.append(f"exists: {locale_path}")
            continue

        locale, en_path = strip_locale_prefix(locale_path)
        if not locale:
            skipped.append(f"not locale: {locale_path}")
            continue

        en_dest = validurls.get(en_path)
        if not en_dest:
            skipped.append(f"no EN redirect: {locale_path} (EN {en_path})")
            continue

        locale_dest = add_locale_prefix(locale, en_dest)
        if locale_path == locale_dest:
            skipped.append(f"identity: {locale_path}")
            continue

        if not source_eligible_for_bulk(locale_path):
            skipped.append(f"fragment/query source: {locale_path}")
            continue

        new_entries.append((locale_path, locale_dest))

    return new_entries, skipped


def format_validurl_line(source: str, dest: str) -> str:
    return (
        f"validurls['{escape_js_string(source)}'] = "
        f"'{escape_js_string(dest)}';"
    )


def apply_entries(js_path: Path, entries: list[tuple[str, str]], marker: str) -> None:
    text = js_path.read_text(encoding="utf-8")
    block_lines = [marker, *sorted(format_validurl_line(s, d) for s, d in entries), ""]
    block = "\n".join(block_lines)

    placeholder = "// validurls['OLD'] = 'NEW';"
    if placeholder not in text:
        raise SystemExit(f"Placeholder not found in {js_path}")

    if marker in text:
        raise SystemExit(f"Marker already present in {js_path}; remove block before re-applying")

    updated = text.replace(placeholder, f"{block}\n{placeholder}", 1)
    js_path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--gsc-csv",
        type=Path,
        required=True,
        help="GSC validation export Table.csv (failed locale 404 URLs)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Append generated entries to broken_redirect_list.js",
    )
    args = parser.parse_args()

    if not args.gsc_csv.is_file():
        print(f"CSV not found: {args.gsc_csv}", file=sys.stderr)
        return 1

    js_text = REDIRECT_JS.read_text(encoding="utf-8")
    validurls = parse_validurls(js_text)
    locale_paths = load_gsc_locale_404_urls(args.gsc_csv)
    entries, skipped = mirror_entries(locale_paths, validurls)

    print(f"Locale 404 URLs in GSC export: {len(locale_paths)}")
    print(f"New mirror entries: {len(entries)}")
    print(f"Skipped: {len(skipped)}")

    if skipped:
        print("\nSkipped (first 15):")
        for line in skipped[:15]:
            print(f"  {line}")
        if len(skipped) > 15:
            print(f"  ... and {len(skipped) - 15} more")

    for source, dest in entries[:10]:
        print(f"  {source}")
        print(f"    -> {dest}")
    if len(entries) > 10:
        print(f"  ... and {len(entries) - 10} more")

    if not args.apply:
        print("\nDry run. Re-run with --apply to write broken_redirect_list.js")
        return 0

    marker = "// GSC 2026-07-28: locale mirrors for legacy IA paths (failed validation export)"
    apply_entries(REDIRECT_JS, entries, marker)
    print(f"\nWrote {len(entries)} entries to {REDIRECT_JS.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
