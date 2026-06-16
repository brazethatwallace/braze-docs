#!/usr/bin/env python3
"""
Sync `_data/kb_articles.csv` and `_data/kb_epic_bd6308.txt` with Salesforce migration PRs.

Optional manual sync for branch `run_sf` when you explicitly refresh tracker state
from GitHub PRs. Not part of Phase 2 — run only when requested.

Do not include `_data/` changes in SF migration PRs to `develop`.

1. Collect `article_id` values from open and merged PRs labeled `salesforce migration`.
2. Merge into `_data/kb_epic_bd6308.txt` (sorted, deduped header preserved).
3. Remove those IDs from `_data/kb_articles.csv`.
4. Regenerate `_data/kb_articles_actioned.md` and `_data/kb_articles_skipped.md`.

Usage (repo root):
  python3 scripts/salesforce-analyzer/sf_kb_sync_tracker.py
  python3 scripts/salesforce-analyzer/sf_kb_sync_tracker.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = "braze-inc/braze-docs"
REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = REPO_ROOT / "_data" / "kb_articles.csv"
EPIC_PATH = REPO_ROOT / "_data" / "kb_epic_bd6308.txt"
ARTICLE_ID_RE = re.compile(r"`(ka[^`]+)`")


def gh_json(args: list[str]) -> object:
    proc = subprocess.run(
        ["gh", *args, "--repo", REPO],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh failed: {' '.join(args)}\n{proc.stderr or proc.stdout}")
    return json.loads(proc.stdout or "null")


def load_epic_ids() -> tuple[list[str], set[str]]:
    header: list[str] = []
    body: set[str] = set()
    in_header = True
    for line in EPIC_PATH.read_text(encoding="utf-8").splitlines():
        if in_header and (line.startswith("#") or not line.strip()):
            header.append(line)
            continue
        in_header = False
        if line.strip():
            body.add(line.strip())
    return header, body


def write_epic_ids(header: list[str], ids: set[str]) -> None:
    EPIC_PATH.write_text("\n".join(header + [""] + sorted(ids)) + "\n", encoding="utf-8")


def pr_article_ids() -> tuple[set[str], int, int]:
    """Return (ids, open_pr_count, merged_pr_count) from PR bodies."""
    nums: set[int] = set()
    for state in ("open", "merged"):
        for pr in gh_json(
            [
                "pr",
                "list",
                "--label",
                "salesforce migration",
                "--state",
                state,
                "--limit",
                "1000",
                "--json",
                "number",
            ]
        ):
            nums.add(pr["number"])

    open_count = len(
        gh_json(
            [
                "pr",
                "list",
                "--label",
                "salesforce migration",
                "--state",
                "open",
                "--limit",
                "1000",
                "--json",
                "number",
            ]
        )
    )
    merged_count = len(
        gh_json(
            [
                "pr",
                "list",
                "--label",
                "salesforce migration",
                "--state",
                "merged",
                "--limit",
                "1000",
                "--json",
                "number",
            ]
        )
    )

    ids: set[str] = set()
    for num in sorted(nums):
        detail = gh_json(["pr", "view", str(num), "--json", "body"])
        ids |= set(ARTICLE_ID_RE.findall(detail.get("body") or ""))

    return ids, open_count, merged_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    header, epic_ids = load_epic_ids()
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        csv_rows = list(reader)

    csv_ids_before = {r["article_id"].strip() for r in csv_rows if r.get("article_id", "").strip()}
    pr_ids, open_prs, merged_prs = pr_article_ids()

    merged_epic = epic_ids | pr_ids
    to_remove = csv_ids_before & merged_epic
    new_csv_rows = [r for r in csv_rows if r.get("article_id", "").strip() not in merged_epic]

    print("=== SF KB tracker sync ===")
    print(f"Epic IDs before:     {len(epic_ids)}")
    print(f"PR body IDs (O+M):   {len(pr_ids)}  ({open_prs} open, {merged_prs} merged PRs scanned)")
    print(f"Epic IDs after:      {len(merged_epic)}")
    print(f"CSV rows before:     {len(csv_rows)}")
    print(f"Removed from CSV:    {len(to_remove)}")
    print(f"CSV rows after:      {len(new_csv_rows)}")

    if args.dry_run:
        print("\n(dry-run — no files written)")
        return

    write_epic_ids(header, merged_epic)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(new_csv_rows)

    proc = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts/salesforce-analyzer/generate_kb_phase1_outputs.py"),
            "--no-prune",
        ],
        cwd=REPO_ROOT,
    )
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)

    print("\nRegenerated kb_articles_actioned.md and kb_articles_skipped.md")


if __name__ == "__main__":
    main()
