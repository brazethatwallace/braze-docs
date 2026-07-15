#!/usr/bin/env python3
"""
Sync `kb_articles.csv` with migration PRs (optional).

Collects ``article_id``s from open + merged `salesforce migration` PR bodies, drops matching CSV
rows, runs `generate_kb_phase1_outputs.py --no-prune`. Commit `_data/` outside migration PRs.

Usage: `python3 scripts/salesforce-analyzer/sf_kb_sync_tracker.py [--dry-run]`
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


def pr_article_ids() -> tuple[set[str], int, int]:
    """PR body ``article_id``s and open/merged PR counts."""
    nums: set[int] = set()
    open_count = 0
    merged_count = 0
    for state in ("open", "merged"):
        prs = gh_json(
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
        )
        if state == "open":
            open_count = len(prs)
        else:
            merged_count = len(prs)
        for pr in prs:
            nums.add(pr["number"])

    ids: set[str] = set()
    for num in sorted(nums):
        detail = gh_json(["pr", "view", str(num), "--json", "body"])
        ids |= set(ARTICLE_ID_RE.findall(detail.get("body") or ""))

    return ids, open_count, merged_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        csv_rows = list(reader)

    csv_ids_before = {r["article_id"].strip() for r in csv_rows if r.get("article_id", "").strip()}
    pr_ids, open_prs, merged_prs = pr_article_ids()

    to_remove = csv_ids_before & pr_ids
    new_csv_rows = [r for r in csv_rows if r.get("article_id", "").strip() not in pr_ids]

    print(
        f"tracker: {len(pr_ids)} id(s) from PRs ({open_prs} open + {merged_prs} merged) | "
        f"CSV {len(csv_rows)} -> {len(new_csv_rows)} (-{len(to_remove)})"
    )

    if args.dry_run:
        print("(dry-run, no writes)")
        return

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

    print("Regenerated actioned/skipped markdown.")


if __name__ == "__main__":
    main()
