#!/usr/bin/env python3
"""
Safely remove stale generated files under _data/.

Usage (from repo root):
  python3 scripts/prune_data_files.py --dry-run
  python3 scripts/prune_data_files.py --dry-run --group support-csv
  python3 scripts/prune_data_files.py --dry-run --group kb-generated
  python3 scripts/prune_data_files.py --confirm
  python3 scripts/prune_data_files.py --confirm --group kb-generated

Always run --dry-run first, review the list, then run --confirm to delete.

Groups:
  support-csv   Dated local Looker exports (_data/support_cases_YYYYMMDD.csv).
                Keeps _data/support_cases_latest.csv (CI + manual canonical file).
  kb-generated  Phase 1 markdown queues (_data/kb_articles_actioned.md,
                _data/kb_articles_skipped.md). Run only after Phase 2 PRs merge
                and Phase 3 write-back to kb_articles.csv (salesforce-migration).
  all           Every prunable group above (default when --group is omitted).

Safety:
  - Only deletes files inside _data/.
  - Never deletes live Jekyll config, sitemaps, allowlists, or *_latest.* audit pointers.
  - Refuses paths outside _data/ even if passed explicitly.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_ROOT = REPO_ROOT / "_data"

# Live site / CI data — never pruned.
PROTECTED_REL_PATHS = {
    "_data/alerts.yml",
    "_data/i18n.yml",
    "_data/language_map.yml",
    "_data/pii_patterns.yml",
    "_data/unreferenced_images_allowlist.txt",
    "_data/support_cases_latest.csv",
}

PROTECTED_GLOBS = (
    "_data/sitemap_*.json",
    "_data/snippet_pii_audit/snippet_pii_report_latest.json",
    "_data/snippet_pii_audit/snippet_pii_report_latest.md",
)

PRUNE_GROUPS: dict[str, tuple[str, ...]] = {
    "support-csv": (
        "_data/support_cases_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].csv",
    ),
    "kb-generated": (
        "_data/kb_articles_actioned.md",
        "_data/kb_articles_skipped.md",
    ),
}

GROUP_DESCRIPTIONS = {
    "support-csv": "dated local support case CSV exports (keeps support_cases_latest.csv)",
    "kb-generated": "Phase 1 KB markdown queues (after Phase 2 merge + Phase 3 write-back)",
}


@dataclass(frozen=True)
class PruneCandidate:
    rel_path: str
    group: str


def rel_under_data(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def is_under_data(path: Path) -> bool:
    try:
        path.resolve().relative_to(DATA_ROOT.resolve())
    except ValueError:
        return False
    return True


def matches_glob(rel_path: str, pattern: str) -> bool:
    return fnmatch.fnmatch(rel_path, pattern)


def is_protected(rel_path: str) -> bool:
    if rel_path in PROTECTED_REL_PATHS:
        return True
    if matches_any_glob(rel_path, PROTECTED_GLOBS):
        return True
    name = Path(rel_path).name
    return fnmatch.fnmatch(name, "*_latest.*")


def matches_any_glob(rel_path: str, patterns: tuple[str, ...]) -> bool:
    return any(matches_glob(rel_path, pattern) for pattern in patterns)


def iter_data_files() -> list[Path]:
    if not DATA_ROOT.is_dir():
        return []
    files: list[Path] = []
    for dirpath, _, filenames in os.walk(DATA_ROOT):
        for name in filenames:
            if name in {".DS_Store", ".gitkeep"}:
                continue
            files.append(Path(dirpath) / name)
    return sorted(files)


def groups_to_run(group_arg: str | None) -> list[str]:
    if group_arg is None or group_arg == "all":
        return list(PRUNE_GROUPS)
    if group_arg not in PRUNE_GROUPS:
        raise ValueError(f"Unknown group {group_arg!r}; choose from: all, {', '.join(PRUNE_GROUPS)}")
    return [group_arg]


def find_candidates(groups: list[str]) -> list[PruneCandidate]:
    patterns: list[tuple[str, str]] = []
    for group in groups:
        for pattern in PRUNE_GROUPS[group]:
            patterns.append((group, pattern))

    candidates: list[PruneCandidate] = []
    for path in iter_data_files():
        rel = rel_under_data(path)
        if is_protected(rel):
            continue
        for group, pattern in patterns:
            if matches_glob(rel, pattern) and path.is_file():
                candidates.append(PruneCandidate(rel, group))
                break
    return candidates


def print_candidates(candidates: list[PruneCandidate], *, dry_run: bool) -> None:
    if not candidates:
        print("No stale _data/ files matched the selected prune groups.")
        return

    by_group: dict[str, list[PruneCandidate]] = {}
    for row in candidates:
        by_group.setdefault(row.group, []).append(row)

    action = "Would delete" if dry_run else "Deleting"
    print(f"{action} {len(candidates)} file(s) under _data/:\n")
    for group in sorted(by_group):
        print(f"## {group} — {GROUP_DESCRIPTIONS.get(group, group)}")
        for row in by_group[group]:
            print(f"  {row.rel_path}")
        print()


def delete_candidates(candidates: list[PruneCandidate]) -> int:
    removed = 0
    for row in candidates:
        target = REPO_ROOT / row.rel_path
        if not target.is_file():
            print(f"Skip (missing): {row.rel_path}", file=sys.stderr)
            continue
        if not is_under_data(target):
            print(f"Refusing to delete outside _data/: {row.rel_path}", file=sys.stderr)
            return 1
        if is_protected(row.rel_path):
            print(f"Refusing to delete protected file: {row.rel_path}", file=sys.stderr)
            return 1
        target.unlink()
        print(f"Deleted {row.rel_path}")
        removed += 1
    print(f"\nRemoved {removed} file(s).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="List files that would be deleted")
    mode.add_argument("--confirm", action="store_true", help="Delete files after reviewing --dry-run")
    parser.add_argument(
        "--group",
        choices=[*PRUNE_GROUPS, "all"],
        default="all",
        help="Prune only one category (default: all)",
    )
    args = parser.parse_args()

    try:
        groups = groups_to_run(None if args.group == "all" else args.group)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    candidates = find_candidates(groups)
    print_candidates(candidates, dry_run=args.dry_run)

    if args.dry_run:
        if candidates:
            print("Review the list above, then run again with --confirm to delete.")
        return 0

    if not candidates:
        return 0
    return delete_candidates(candidates)


if __name__ == "__main__":
    raise SystemExit(main())
