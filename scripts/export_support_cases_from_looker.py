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
does not block the data branch). Patterns live in `_data/pii_patterns.yml` — edit that file to
add or change redactions without touching this script. Treat the CSV as sensitive; this repo
should stay private and access to the data branch limited to people who may handle support content.

Usage:
  export LOOKER_CLIENT_ID="..." LOOKER_CLIENT_SECRET="..."
  pip install requests pyyaml
  python scripts/export_support_cases_from_looker.py
"""

from __future__ import annotations

import os
import re
import sys
from datetime import datetime
from functools import lru_cache
from pathlib import Path

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise SystemExit("PyYAML is required: pip install pyyaml") from e

_REPO_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_PII_PATTERNS_PATH = _REPO_ROOT / "_data" / "pii_patterns.yml"


@lru_cache(maxsize=1)
def _load_secret_redactions(
    patterns_path: str | None = None,
) -> list[tuple[re.Pattern[str], str]]:
    """Load and compile redaction patterns from `_data/pii_patterns.yml`."""
    path = Path(patterns_path) if patterns_path else _DEFAULT_PII_PATTERNS_PATH
    if not path.is_file():
        raise FileNotFoundError(
            f"PII redaction patterns file not found: {path}. "
            "Expected `_data/pii_patterns.yml` (copied from the workflow ref in CI)."
        )

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("patterns"), list):
        raise ValueError(
            f"Invalid PII patterns file {path}: expected a mapping with a `patterns` list."
        )

    compiled: list[tuple[re.Pattern[str], str]] = []
    for i, entry in enumerate(data["patterns"]):
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid pattern entry at index {i} in {path}: expected a mapping.")
        pattern = entry.get("pattern")
        replacement = entry.get("replacement")
        if not isinstance(pattern, str) or not pattern:
            raise ValueError(f"Invalid or missing `pattern` at index {i} in {path}.")
        if not isinstance(replacement, str) or not replacement:
            raise ValueError(f"Invalid or missing `replacement` at index {i} in {path}.")
        try:
            compiled.append((re.compile(pattern), replacement))
        except re.error as exc:
            raise ValueError(f"Invalid regex at index {i} in {path}: {exc}") from exc

    if not compiled:
        raise ValueError(f"No redaction patterns found in {path}.")
    return compiled


def _redact_embedded_secrets(
    text: str,
    *,
    patterns_path: str | None = None,
) -> tuple[str, int]:
    """Return scrubbed text and total number of replacements."""
    total = 0
    for pattern, replacement in _load_secret_redactions(patterns_path):
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

    try:
        csv_text, redactions = _redact_embedded_secrets(csv_resp.text)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
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
