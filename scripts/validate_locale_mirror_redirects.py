#!/usr/bin/env python3
"""
Verify locale-prefixed mirrors exist for English bulk-eligible redirects.

Usage:
  python3 scripts/validate_locale_mirror_redirects.py
  python3 scripts/validate_locale_mirror_redirects.py --check
  python3 scripts/validate_locale_mirror_redirects.py --check-added --base origin/develop
  python3 scripts/validate_locale_mirror_redirects.py --path-regex custom_objects
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from locale_redirect_utils import (
    missing_mirrors_for_en_sources,
    mirror_en_redirect_to_locales,
    parse_added_validurl_sources,
    parse_validurls,
    is_en_bulk_source,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REDIRECT_JS = PROJECT_ROOT / "assets/js/broken_redirect_list.js"


def git_diff_redirect_file(base_ref: str) -> str:
    result = subprocess.run(
        ["git", "diff", "--unified=0", f"{base_ref}...HEAD", "--", str(REDIRECT_JS)],
        capture_output=True,
        text=True,
        check=False,
        cwd=PROJECT_ROOT,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr or f"git diff failed against {base_ref}")
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 when locale mirrors are missing (CI mode)",
    )
    parser.add_argument(
        "--check-added",
        action="store_true",
        help="Only check EN redirects added in the current branch diff",
    )
    parser.add_argument(
        "--base",
        type=str,
        default="origin/develop",
        help="Base ref for --check-added (default: origin/develop)",
    )
    parser.add_argument(
        "--path-regex",
        type=str,
        default="",
        help="Only check EN sources matching this regex",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Max missing entries to print",
    )
    args = parser.parse_args()

    validurls = parse_validurls(REDIRECT_JS.read_text(encoding="utf-8"))

    if args.check_added:
        diff_text = git_diff_redirect_file(args.base)
        added_sources = parse_added_validurl_sources(diff_text)
        if args.path_regex:
            pattern = re.compile(args.path_regex)
            added_sources = [src for src in added_sources if pattern.search(src)]
        missing = missing_mirrors_for_en_sources(added_sources, validurls)
        scope = f"{len(added_sources)} EN redirect(s) added in diff"
    else:
        pattern = re.compile(args.path_regex) if args.path_regex else None
        missing = []
        for en_source, en_dest in validurls.items():
            if not is_en_bulk_source(en_source):
                continue
            if pattern and not pattern.search(en_source):
                continue
            for locale_source, locale_dest in mirror_en_redirect_to_locales(
                en_source, en_dest, validurls
            ):
                missing.append((locale_source, locale_dest))
        missing.sort(key=lambda pair: pair[0])
        scope = "all EN bulk-eligible redirects"
        if pattern:
            scope = f'EN sources matching "{args.path_regex}"'

    if not missing:
        print(f"OK: locale mirrors present for checked EN redirects ({scope})")
        return 0

    print(f"Missing {len(missing)} locale mirror redirect(s) ({scope}):")
    for source, destination in missing[: args.limit]:
        print(f"  {source}")
        print(f"    -> {destination}")
    if len(missing) > args.limit:
        print(f"  ... and {len(missing) - args.limit} more")

    if args.check or args.check_added:
        print(
            "\nAdd locale mirrors alongside new EN redirects, or run "
            "python3 scripts/generate_gsc_redirect_batch.py for backfill batches.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
