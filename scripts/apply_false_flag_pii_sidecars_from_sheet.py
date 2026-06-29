#!/usr/bin/env python3
"""
Create or merge ``*.pii-audit-dismiss.json`` sidecars from a ``sheets__get_sheet_data`` JSON export
of the **Current screenshots** tab.

Uses rows where **Status** is exactly ``False flag``: column A = image path (``assets/img/...``),
column B = finding id for ``dismiss_ids``.

Existing sidecars are merged (union of ``dismiss_ids``; ``reason`` is preserved when already set).

Usage (from repo root)::

  python3 scripts/apply_false_flag_pii_sidecars_from_sheet.py --sheet-json path/to/sheet.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

STATUS_COL = 9
IMAGE_COL = 0
FINDING_COL = 1
FALSE_FLAG = "False flag"
DEFAULT_REASON = (
    "Triaged as a false positive in the screenshot PII audit (Current screenshots tab)."
)


def cell_value(row: list[object], i: int) -> str:
    if i >= len(row):
        return ""
    c = row[i]
    if isinstance(c, dict):
        return (c.get("value") or "").strip()
    return str(c).strip()


def load_false_flag_findings(sheet_path: Path) -> dict[str, set[str]]:
    obj = json.loads(sheet_path.read_text(encoding="utf-8"))
    rows: list[list[object]] = obj.get("data") or []
    by_image: dict[str, set[str]] = defaultdict(set)
    for idx, row in enumerate(rows):
        if idx == 0:
            continue
        if cell_value(row, STATUS_COL) != FALSE_FLAG:
            continue
        img = cell_value(row, IMAGE_COL)
        fid = cell_value(row, FINDING_COL)
        if img and fid:
            by_image[img].add(fid)
    return by_image


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--sheet-json",
        type=Path,
        required=True,
        help="JSON from sheets__get_sheet_data (Current screenshots)",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions only; do not write files",
    )
    args = ap.parse_args()

    repo = Path(__file__).resolve().parent.parent
    by_image = load_false_flag_findings(args.sheet_json)
    if not by_image:
        print("No False flag rows found.", file=sys.stderr)
        sys.exit(1)

    created = 0
    updated = 0
    for rel in sorted(by_image):
        img_path = repo / rel
        if not img_path.is_file():
            print(f"skip (missing image): {rel}", file=sys.stderr)
            continue
        side = img_path.with_suffix(img_path.suffix + ".pii-audit-dismiss.json")
        new_ids = by_image[rel]
        if side.is_file():
            data = json.loads(side.read_text(encoding="utf-8"))
            old_ids = set(data.get("dismiss_ids") or [])
            merged = old_ids | new_ids
            if merged == old_ids:
                continue
            data["dismiss_ids"] = sorted(merged, key=str.lower)
            if not (data.get("reason") or "").strip():
                data["reason"] = DEFAULT_REASON
            data.setdefault("dismiss_all", False)
            payload = data
            action = "update"
            updated += 1
        else:
            payload = {
                "reason": DEFAULT_REASON,
                "dismiss_all": False,
                "dismiss_ids": sorted(new_ids, key=str.lower),
            }
            action = "create"
            created += 1

        if args.dry_run:
            print(f"{action}: {side.relative_to(repo)} ids={sorted(new_ids)}")
            continue
        side.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.dry_run:
        print(f"dry-run: would create {created}, update {updated}", file=sys.stderr)
        return

    print(
        f"Wrote sidecars under assets/img/ (created {created}, updated {updated}, "
        f"images {len(by_image)}).",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
