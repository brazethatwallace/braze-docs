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
  SUPPORT_ANALYZER_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA
                                (required in CI) Set to "1" when running in GitHub Actions
                                (GITHUB_ACTIONS=true) to confirm you accept writing raw Support
                                Case CSV (may contain consumer PII) to the configured output path.

The export is raw Looker CSV (with common credential patterns redacted so git push protection
does not block the data branch). Treat the file as sensitive; this repo should stay private and
access to the data branch limited to people who may handle support content.

Usage:
  export LOOKER_CLIENT_ID="..." LOOKER_CLIENT_SECRET="..."
  python scripts/export_support_cases_from_looker.py
"""

import os
import re
import sys
from datetime import datetime

# Redact credential-like strings that may appear in case text before git push (push protection).
# Not a substitute for PII handling; see SUPPORT_ANALYZER_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA.
_SECRET_REDACTIONS: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"\b(?:AKIA|ASIA|AIDA|AROA|AIPA|ANPA|ANVA|AGPA)[0-9A-Z]{16}\b"),
        "[REDACTED_AWS_ACCESS_KEY_ID]",
    ),
    (
        # Leading word boundary only — trailing boundary omitted for CSV punctuation after keys.
        re.compile(r"\bSG\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
        "[REDACTED_SENDGRID_API_KEY]",
    ),
    (re.compile(r"\bghp_[A-Za-z0-9]{36}\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"\bgithub_pat_[A-Za-z0-9_]{82,}\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"\bgho_[A-Za-z0-9]{36}\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"\bghu_[A-Za-z0-9]{36}\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"\bghs_[A-Za-z0-9]{36}\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"\bghr_[A-Za-z0-9]{36}\b"), "[REDACTED_GITHUB_TOKEN]"),
    # b/a/p/r/s bot-app tokens; e enterprise; o legacy OAuth (GitHub push protection scans all).
    (re.compile(r"\bxox[bapreso]-[A-Za-z0-9-]{10,}\b"), "[REDACTED_SLACK_TOKEN]"),
    (
        re.compile(r"\b(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{16,}\b"),
        "[REDACTED_STRIPE_KEY]",
    ),
    # Twilio Account SID (AC…) and API Key SID (SK…); 32 hex chars after prefix.
    (re.compile(r"\bAC[0-9a-fA-F]{32}"), "[REDACTED_TWILIO_ACCOUNT_SID]"),
    (re.compile(r"\bSK[0-9a-fA-F]{32}"), "[REDACTED_TWILIO_API_KEY_SID]"),
]


def _redact_embedded_secrets(text: str) -> tuple[str, int]:
    """Return scrubbed text and total number of replacements."""
    total = 0
    for pattern, replacement in _SECRET_REDACTIONS:
        text, n = pattern.subn(replacement, text)
        total += n
    return text, total


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

    if os.environ.get("GITHUB_ACTIONS") == "true":
        if os.environ.get("SUPPORT_ANALYZER_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA") != "1":
            print(
                "Error: In GitHub Actions, set SUPPORT_ANALYZER_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1 "
                "to confirm raw Support Cases CSV (may contain PII) may be written to the output path.",
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

    csv_text, redactions = _redact_embedded_secrets(csv_resp.text)
    if redactions:
        print(
            f"Redacted {redactions} embedded credential-like value(s) from export before write.",
            file=sys.stderr,
        )

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(csv_text)

    rows = max(0, len(csv_text.splitlines()) - 1)
    print(f"Exported {rows} data rows (plus header) to {output_path}")


if __name__ == "__main__":
    main()
