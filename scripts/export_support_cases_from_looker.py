#!/usr/bin/env python3
"""
Export Support Cases from Looker to CSV for the support-analyzer workflow.

Uses the Looker API to run the Support Cases explore query and save results as CSV.

Environment variables:
  LOOKER_CLIENT_ID              (required) API3 client ID
  LOOKER_CLIENT_SECRET          (required) API3 client secret
  LOOKER_BASE_URL               (optional) Default https://braze.looker.com
  LOOKER_SUPPORT_CASES_QUERY_ID (optional) Saved Looker query ID to run as CSV. If unset, uses the
                                default Support Cases explore (same as the dashboard embed). Change
                                this to export a different saved Look; filters and date windows live
                                in Looker on that saved query—not in this script.
  SUPPORT_ANALYZER_OUTPUT       (optional) Output path; default _data/support_cases_<YYYYMMDD>.csv

Usage:
  export LOOKER_CLIENT_ID="..." LOOKER_CLIENT_SECRET="..."
  python scripts/export_support_cases_from_looker.py
"""

import os
import sys
from datetime import datetime


# Default Support Cases explore query ID (from Looker embed URL); override with LOOKER_SUPPORT_CASES_QUERY_ID.
_DEFAULT_SUPPORT_CASES_QUERY_ID = "OwFKj0j5nyA2o05QqF2bm4"


def main():
    base_url = (os.environ.get("LOOKER_BASE_URL") or "https://braze.looker.com").rstrip("/")
    query_id = (os.environ.get("LOOKER_SUPPORT_CASES_QUERY_ID") or "").strip() or _DEFAULT_SUPPORT_CASES_QUERY_ID
    client_id = os.environ.get("LOOKER_CLIENT_ID")
    client_secret = os.environ.get("LOOKER_CLIENT_SECRET")

    if not client_id or not client_secret:
        print(
            "Error: Set LOOKER_CLIENT_ID and LOOKER_CLIENT_SECRET.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        import requests
    except ImportError:
        print("Error: Run: pip install requests", file=sys.stderr)
        sys.exit(1)

    login_url = f"{base_url}/api/4.0/login"
    run_url = f"{base_url}/api/4.0/queries/{query_id}/run/csv"

    resp = requests.post(
        login_url,
        data={"client_id": client_id, "client_secret": client_secret},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    if not resp.ok:
        print(f"Error: Looker login failed ({resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    access_token = data.get("access_token")
    if not access_token:
        print("Error: No access_token in login response.", file=sys.stderr)
        sys.exit(1)

    csv_resp = requests.get(
        run_url,
        headers={"Authorization": f"token {access_token}"},
        timeout=300,
    )
    if not csv_resp.ok:
        print(f"Error: Query run failed ({csv_resp.status_code}): {csv_resp.text[:500]}", file=sys.stderr)
        sys.exit(1)

    default_name = f"support_cases_{datetime.now().strftime('%Y%m%d')}.csv"
    output_path = os.environ.get("SUPPORT_ANALYZER_OUTPUT")
    if not output_path:
        output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_data", default_name)
    else:
        output_path = os.path.expanduser(output_path)

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(csv_resp.text)

    rows = max(0, len(csv_resp.text.splitlines()) - 1)
    print(f"Exported {rows} data rows (plus header) to {output_path}")


if __name__ == "__main__":
    main()
