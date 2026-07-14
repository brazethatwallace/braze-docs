#!/usr/bin/env python3
"""
Export edge-eligible redirects from assets/js/broken_redirect_list.js for Vercel
Bulk Redirects (bulkRedirectsPath in vercel.json).

Client-side-only entries are skipped for bulk export:
- Source URLs with `#` fragments (not sent to the server)
- Source URLs with `?` query strings (bulk redirect sources are path-only)
- Comment lines such as `// validurls['OLD'] = 'NEW';`

Usage:
  python3 scripts/generate_bulk_redirects.py
  python3 scripts/generate_bulk_redirects.py --check   # exit 1 if JSON is stale
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REDIRECT_JS = PROJECT_ROOT / "assets/js/broken_redirect_list.js"
OUTPUT_JSON = PROJECT_ROOT / "assets/redirects/bulk-redirects.json"

VALIDURLS_RE = re.compile(
    r"validurls\['((?:\\'|[^'])*)'\]\s*=\s*'((?:\\'|[^'])*)'\s*;"
)


def unescape_js_string(value: str) -> str:
    return value.replace("\\'", "'")


def normalize_path(path: str) -> str:
    """Match redirect-management conventions: lowercase, no trailing slash."""
    if not path:
        return path
    if path.startswith("http://") or path.startswith("https://"):
        return path

    hash_part = ""
    query_part = ""
    base = path

    if "#" in base:
        base, hash_part = base.split("#", 1)
        hash_part = f"#{hash_part.lower()}"

    if "?" in base:
        base, query_part = base.split("?", 1)
        query_part = f"?{query_part.lower()}"

    base = base.rstrip("/").lower()
    return f"{base}{query_part}{hash_part}"


def source_has_fragment(source: str) -> bool:
    """Fragment in the request path is never sent to the edge; skip for bulk."""
    path = source.split("?", 1)[0]
    return "#" in path


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


def build_bulk_redirects(validurls: dict[str, str]) -> tuple[list[dict], dict[str, int]]:
    redirects: list[dict] = []
    stats = {
        "total_validurls": len(validurls),
        "skipped_fragment_source": 0,
        "skipped_query_source": 0,
        "skipped_invalid_source": 0,
        "skipped_identity": 0,
        "exported": 0,
    }

    seen_sources: set[str] = set()

    for source, destination in validurls.items():
        if source_has_fragment(source):
            stats["skipped_fragment_source"] += 1
            continue
        if "?" in source:
            stats["skipped_query_source"] += 1
            continue

        norm_source = normalize_path(source)
        norm_dest = normalize_path(destination)

        if not (
            norm_source.startswith("/")
            or norm_source.startswith("http://")
            or norm_source.startswith("https://")
        ):
            stats["skipped_invalid_source"] += 1
            continue

        if norm_source == norm_dest:
            stats["skipped_identity"] += 1
            continue

        if norm_source in seen_sources:
            continue
        seen_sources.add(norm_source)

        redirects.append(
            {
                "source": norm_source,
                "destination": norm_dest,
                "permanent": True,
            }
        )
        stats["exported"] += 1

    redirects.sort(key=lambda row: row["source"])
    return redirects, stats


def write_bulk_redirects(redirects: list[dict]) -> None:
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w", encoding="utf-8") as handle:
        json.dump(redirects, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify bulk-redirects.json matches broken_redirect_list.js (CI mode)",
    )
    args = parser.parse_args()

    js_text = REDIRECT_JS.read_text(encoding="utf-8")
    validurls = parse_validurls(js_text)
    redirects, stats = build_bulk_redirects(validurls)

    if args.check:
        if not OUTPUT_JSON.is_file():
            print(f"Missing {OUTPUT_JSON.relative_to(PROJECT_ROOT)}", file=sys.stderr)
            return 1
        existing = json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
        if existing != redirects:
            print(
                "bulk-redirects.json is out of date. Run: "
                "python3 scripts/generate_bulk_redirects.py",
                file=sys.stderr,
            )
            return 1
        print(f"OK: {stats['exported']} bulk redirects in sync")
        return 0

    write_bulk_redirects(redirects)
    print(f"Wrote {OUTPUT_JSON.relative_to(PROJECT_ROOT)}")
    print(
        f"  exported={stats['exported']} "
        f"skipped_fragment_source={stats['skipped_fragment_source']} "
        f"skipped_query_source={stats['skipped_query_source']} "
        f"skipped_invalid_source={stats['skipped_invalid_source']} "
        f"skipped_identity={stats['skipped_identity']} "
        f"total_validurls={stats['total_validurls']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
