#!/usr/bin/env python3
"""Normalize GA4 page-path export into a deduped, pilot-excluded pages file."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import importlib.util

REPO_ROOT = Path(__file__).resolve().parents[2]
_SCORECARD = REPO_ROOT / "scripts" / "seo_pilot" / "page_scorecard.py"
_spec = importlib.util.spec_from_file_location("page_scorecard", _SCORECARD)
_scorecard = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_scorecard)
docs_url_to_doc_path = _scorecard.docs_url_to_doc_path
page_skip_reason = _scorecard.page_skip_reason

# Round-1 SEO pilot pages (normalized /docs paths, no trailing slash).
PILOT_ROUND1 = {
    "/docs/partners/home",
    "/docs/user_guide/brazeai",
    "/docs/user_guide/data/distribution/braze_currents",
    "/docs/user_guide/messaging/canvas",
    "/docs/api/home",
    "/docs/user_guide/channels/sms_mms_and_rcs",
    "/docs/developer_guide/home",
    "/docs/user_guide/analytics",
    "/docs/user_guide/audience/subscription_preferences/preference_center",
    "/docs/user_guide/channels/whatsapp",
    "/docs/user_guide/messaging/design_and_edit/personalize/liquid",
    "/docs/user_guide/channels/email",
    "/docs/user_guide/channels/in_app_messages",
    "/docs/user_guide/channels/push",
    "/docs/developer_guide/push_notifications/soft_push_prompts",
}

# Non-article utility paths (search, locale home, support widget, bare /docs).
SKIP_PATHS = {
    "/docs",
    "/docs/en",
    "/docs/search",
    "/docs/en/search",
    "/docs/en/support_contact",
}


def normalize_ga_path(raw: str) -> str | None:
    path = raw.strip().split("?")[0].split("#")[0]
    if not path.startswith("/docs"):
        return None
    path = re.sub(r"/+", "/", path).rstrip("/") or "/docs"
    if path.startswith("/docs/en/"):
        path = "/docs/" + path[len("/docs/en/") :]
    elif path == "/docs/en":
        path = "/docs"
    return path


def load_ga_views(csv_path: Path) -> dict[str, int]:
    aggregated: dict[str, int] = {}
    lines = [
        line
        for line in csv_path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    reader = csv.DictReader(lines)
    if not reader.fieldnames:
        return aggregated
    fields = {c.lower().strip(): c for c in reader.fieldnames}
    path_col = fields.get("page path and screen class") or fields.get("page")
    views_col = fields.get("views")
    if not path_col or not views_col:
        raise SystemExit(f"Expected GA columns in {csv_path}")
    for row in reader:
        norm = normalize_ga_path(row[path_col])
        if not norm:
            continue
        try:
            views = int(float(row[views_col] or 0))
        except ValueError:
            continue
        aggregated[norm] = aggregated.get(norm, 0) + views
    return aggregated


def main() -> int:
    parser = argparse.ArgumentParser(description="GA4 export → SEO pilot pages file")
    parser.add_argument("ga_csv", type=Path)
    parser.add_argument("--top", type=int, default=100)
    parser.add_argument(
        "--out-pages",
        type=Path,
        default=REPO_ROOT / "scripts/temp/ga-top-traffic-pages.txt",
    )
    parser.add_argument(
        "--out-gsc",
        type=Path,
        default=REPO_ROOT / "scripts/temp/ga-traffic-as-gsc.csv",
        help="GSC-shaped CSV (views → clicks) for scorecard",
    )
    parser.add_argument(
        "--out-report",
        type=Path,
        default=REPO_ROOT / "scripts/temp/ga-top-traffic-report.csv",
    )
    args = parser.parse_args()

    views_by_path = load_ga_views(args.ga_csv)
    ranked = sorted(views_by_path.items(), key=lambda kv: kv[1], reverse=True)

    selected: list[tuple[str, str, int]] = []
    skipped: list[tuple[str, int, str]] = []

    for path, views in ranked:
        if path in SKIP_PATHS:
            skipped.append((path, views, "utility_page"))
            continue
        if path in PILOT_ROUND1:
            skipped.append((path, views, "pilot_round1"))
            continue
        doc_path = docs_url_to_doc_path(path)
        if not doc_path:
            skipped.append((path, views, "unmapped_url"))
            continue
        md = REPO_ROOT / doc_path
        reason = page_skip_reason(md)
        if reason:
            skipped.append((path, views, reason))
            continue
        if any(p == path for p, _, _ in selected):
            continue
        selected.append((path, doc_path, views))
        if len(selected) >= args.top:
            break

    args.out_pages.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# GA top {args.top} by views (YTD), deduped, pilot round-1 excluded"]
    for path, doc_path, views in selected:
        lines.append(f"# {views:,} views — {path}")
        lines.append(doc_path)
    args.out_pages.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with args.out_gsc.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["page", "clicks", "impressions", "ctr", "position"])
        writer.writeheader()
        for path, _, views in selected:
            writer.writerow(
                {"page": path, "clicks": views, "impressions": views, "ctr": 0, "position": 0}
            )

    with args.out_report.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["rank", "ga_views", "docs_path", "doc_path", "skip_reason"]
        )
        writer.writeheader()
        for i, (path, doc_path, views) in enumerate(selected, start=1):
            writer.writerow(
                {"rank": i, "ga_views": views, "docs_path": path, "doc_path": doc_path, "skip_reason": ""}
            )
        for path, views, reason in skipped[:200]:
            writer.writerow(
                {
                    "rank": "",
                    "ga_views": views,
                    "docs_path": path,
                    "doc_path": docs_url_to_doc_path(path) or "",
                    "skip_reason": reason,
                }
            )

    print(f"Selected {len(selected)} pages → {args.out_pages}")
    print(f"Wrote GSC-shaped traffic file → {args.out_gsc}")
    print(f"Wrote selection report → {args.out_report}")
    if len(selected) < args.top:
        print(f"Warning: only {len(selected)} scoreable pages found (requested {args.top})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
