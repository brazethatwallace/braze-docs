#!/usr/bin/env python3
"""
Sync the Docs team ownership spreadsheet Page Paths tab with `_docs/` markdown paths.

Compares eligible repo paths (see scripts/doc_ownership_sync_config.yml) against the
Google Sheet, adds new paths with inherited Writer/Team, removes stale paths, writes
`.github/support_analyzer_doc_assignees.csv`, and appends a row to the Auto-Assign Log tab.

Environment:
  GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON  Service account JSON (preferred in GitHub Actions).
  GOOGLE_APPLICATION_CREDENTIALS      Path to service account JSON file (local runs).

Usage:
  python3 scripts/sync_doc_page_paths.py --dry-run
  python3 scripts/sync_doc_page_paths.py --apply
  python3 scripts/sync_doc_page_paths.py --apply --github-output "$GITHUB_OUTPUT"
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "scripts" / "doc_ownership_sync_config.yml"
SHEETS_SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
REDIRECT_FM_RE = re.compile(r"layout:\s*redirect\b", re.MULTILINE)


@dataclass(frozen=True)
class OwnershipRow:
    page_path: str
    writer: str
    team: str
    github_username: str


@dataclass(frozen=True)
class SyncPlan:
    target_rows: list[OwnershipRow]
    added_paths: list[str]
    removed_paths: list[str]
    writer_config: dict[str, str]


def load_config(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Config must be a mapping: {path}")
    return data


def _normalize_repo_path(raw: str) -> str:
    return raw.strip().replace("\\", "/")


def is_redirect_only(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        return False
    front_matter = text[3:end]
    return "redirect_to:" in front_matter and bool(REDIRECT_FM_RE.search(front_matter))


def path_is_eligible(rel: str, config: dict[str, Any]) -> bool:
    rel = _normalize_repo_path(rel)
    include_prefixes = config.get("include_prefixes") or []
    if not any(rel.startswith(prefix) for prefix in include_prefixes):
        return False
    for prefix in config.get("exclude_prefixes") or []:
        if rel.startswith(prefix):
            return False
    segments = rel.split("/")
    excluded_segments = set(config.get("exclude_path_segments") or [])
    if any(segment in excluded_segments for segment in segments):
        return False
    return True


def enumerate_repo_paths(root: Path, config: dict[str, Any]) -> set[str]:
    docs_dir = root / "_docs"
    if not docs_dir.is_dir():
        raise FileNotFoundError(f"Missing _docs directory under {root}")
    paths: set[str] = set()
    exclude_redirect = bool(config.get("exclude_redirect_only", True))
    for md in docs_dir.rglob("*.md"):
        rel = md.relative_to(root).as_posix()
        if not path_is_eligible(rel, config):
            continue
        if exclude_redirect and is_redirect_only(md):
            continue
        paths.add(rel)
    return paths


def _inherit_row(page_path: str, existing: dict[str, OwnershipRow]) -> OwnershipRow | None:
    best_len = -1
    best: OwnershipRow | None = None
    for prefix, row in existing.items():
        if page_path == prefix or page_path.startswith(prefix + "/"):
            plen = len(prefix)
            if plen > best_len:
                best_len = plen
                best = row
    return best


def resolve_github_username(writer: str, writer_config: dict[str, str], fallback: str) -> str:
    key = writer.strip()
    if not key:
        return fallback
    return writer_config.get(key, fallback)


def build_sync_plan(
    *,
    repo_paths: set[str],
    existing_rows: dict[str, OwnershipRow],
    config: dict[str, Any],
    writer_config: dict[str, str],
) -> SyncPlan:
    default_writer = str(config.get("default_writer") or "Docs Team")
    default_team = str(config.get("default_team") or "")
    default_github = str(config.get("default_github_username") or "docs-team")

    added_paths = sorted(repo_paths - set(existing_rows))
    removed_paths = sorted(set(existing_rows) - repo_paths)

    merged: dict[str, OwnershipRow] = {}
    for path in sorted(repo_paths):
        if path in existing_rows:
            merged[path] = existing_rows[path]
            continue
        inherited = _inherit_row(path, existing_rows)
        if inherited:
            writer = inherited.writer
            team = inherited.team
            github = inherited.github_username or resolve_github_username(
                writer, writer_config, default_github
            )
        else:
            writer = default_writer
            team = default_team
            github = resolve_github_username(writer, writer_config, default_github)
        merged[path] = OwnershipRow(
            page_path=path,
            writer=writer,
            team=team,
            github_username=github,
        )

    target_rows = [merged[path] for path in sorted(merged)]
    return SyncPlan(
        target_rows=target_rows,
        added_paths=added_paths,
        removed_paths=removed_paths,
        writer_config=writer_config,
    )


def rows_to_csv(rows: list[OwnershipRow], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["Page Path", "Writer", "Team", "GitHub Username"])
        for row in rows:
            writer.writerow([row.page_path, row.writer, row.team, row.github_username])


def read_csv_rows(csv_path: Path) -> dict[str, OwnershipRow]:
    if not csv_path.is_file():
        return {}
    rows: dict[str, OwnershipRow] = {}
    with csv_path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return {}
        lower = {name.strip().lower(): name for name in reader.fieldnames}
        path_key = lower.get("page path") or lower.get("path") or lower.get("page_path")
        writer_key = lower.get("writer")
        team_key = lower.get("team")
        github_key = lower.get("github username") or lower.get("github_username")
        if not path_key:
            return {}
        for raw in reader:
            page_path = _normalize_repo_path(raw.get(path_key) or "")
            if not page_path:
                continue
            rows[page_path] = OwnershipRow(
                page_path=page_path,
                writer=(raw.get(writer_key or "") or "").strip(),
                team=(raw.get(team_key or "") or "").strip(),
                github_username=(raw.get(github_key or "") or "").strip(),
            )
    return rows


def csv_matches_plan(csv_path: Path, plan: SyncPlan) -> bool:
    if not csv_path.is_file():
        return False
    current = read_csv_rows(csv_path)
    if set(current) != {row.page_path for row in plan.target_rows}:
        return False
    for row in plan.target_rows:
        existing = current.get(row.page_path)
        if not existing:
            return False
        if (
            existing.writer != row.writer
            or existing.team != row.team
            or existing.github_username != row.github_username
        ):
            return False
    return True


def _load_service_account_credentials():
    try:
        from google.oauth2 import service_account
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependencies. Run: pip install -r scripts/requirements-doc-ownership-sync.txt"
        ) from exc

    raw_json = (os.environ.get("GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON") or "").strip()
    if raw_json:
        try:
            info = json.loads(raw_json)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON is not valid JSON. Re-save the "
                "GitHub secret with the full downloaded service account key file "
                "(standard JSON with double-quoted keys)."
            ) from exc
        if not isinstance(info, dict):
            raise RuntimeError("GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON must be a JSON object.")
        return service_account.Credentials.from_service_account_info(info, scopes=SHEETS_SCOPE)

    creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if creds_path and Path(creds_path).is_file():
        return service_account.Credentials.from_service_account_file(
            creds_path, scopes=SHEETS_SCOPE
        )

    raise RuntimeError(
        "Set GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON or GOOGLE_APPLICATION_CREDENTIALS to a "
        "service account JSON file with edit access to the ownership spreadsheet."
    )


def _get_sheets_service():
    try:
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependencies. Run: pip install -r scripts/requirements-doc-ownership-sync.txt"
        ) from exc

    credentials = _load_service_account_credentials()
    return build("sheets", "v4", credentials=credentials, cache_discovery=False)


def _sheet_values(
    service: Any,
    spreadsheet_id: str,
    sheet_name: str,
    range_a1: str,
    *,
    value_render_option: str = "FORMATTED_VALUE",
) -> list[list[str]]:
    quoted = sheet_name.replace("'", "''")
    result = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=spreadsheet_id,
            range=f"'{quoted}'!{range_a1}",
            valueRenderOption=value_render_option,
        )
        .execute()
    )
    values = result.get("values") or []
    return [[str(cell) for cell in row] for row in values]


def _sheet_id_by_name(service: Any, spreadsheet_id: str, sheet_name: str) -> int:
    meta = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    for sheet in meta.get("sheets") or []:
        props = sheet.get("properties") or {}
        if props.get("title") == sheet_name:
            return int(props["sheetId"])
    raise KeyError(f"Sheet tab not found: {sheet_name!r}")


def load_sheet_rows(service: Any, config: dict[str, Any]) -> tuple[dict[str, OwnershipRow], dict[str, str]]:
    spreadsheet_id = str(config["spreadsheet_id"])
    page_sheet = str(config["page_paths_sheet"])
    config_sheet = str(config["config_sheet"])

    raw_rows = _sheet_values(service, spreadsheet_id, page_sheet, "A2:D")
    existing: dict[str, OwnershipRow] = {}
    for row in raw_rows:
        if not row:
            continue
        page_path = _normalize_repo_path(row[0] if len(row) > 0 else "")
        if not page_path or page_path.lower() == "page path":
            continue
        existing[page_path] = OwnershipRow(
            page_path=page_path,
            writer=(row[1] if len(row) > 1 else "").strip(),
            team=(row[2] if len(row) > 2 else "").strip(),
            github_username=(row[3] if len(row) > 3 else "").strip(),
        )

    writer_config: dict[str, str] = {}
    for row in _sheet_values(service, spreadsheet_id, config_sheet, "A2:B"):
        if len(row) < 2:
            continue
        writer = row[0].strip()
        github = row[1].strip()
        if writer and github:
            writer_config[writer] = github

    return existing, writer_config


def apply_sheet_updates(
    service: Any,
    config: dict[str, Any],
    plan: SyncPlan,
    *,
    eastern_now: datetime | None = None,
) -> None:
    spreadsheet_id = str(config["spreadsheet_id"])
    page_sheet = str(config["page_paths_sheet"])
    log_sheet = str(config["log_sheet"])
    quoted_page = page_sheet.replace("'", "''")
    quoted_log = log_sheet.replace("'", "''")

    values = [[row.page_path, row.writer, row.team] for row in plan.target_rows]
    if values:
        end_row = 1 + len(values)
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"'{quoted_page}'!A2:C{end_row}",
            valueInputOption="USER_ENTERED",
            body={"values": values},
        ).execute()
    else:
        end_row = 1

    page_sheet_id = _sheet_id_by_name(service, spreadsheet_id, page_sheet)
    current_row_count = len(_sheet_values(service, spreadsheet_id, page_sheet, "A:A"))
    if current_row_count > end_row:
        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "requests": [
                    {
                        "deleteDimension": {
                            "range": {
                                "sheetId": page_sheet_id,
                                "dimension": "ROWS",
                                "startIndex": end_row,
                                "endIndex": current_row_count,
                            }
                        }
                    }
                ]
            },
        ).execute()

    eastern_now = eastern_now or datetime.now(ZoneInfo("America/New_York"))
    message = (
        f"monthly-sync | +{len(plan.added_paths)} / -{len(plan.removed_paths)} paths"
    )
    if plan.added_paths:
        message += f" | added: {', '.join(plan.added_paths[:5])}"
        if len(plan.added_paths) > 5:
            message += f" (+{len(plan.added_paths) - 5} more)"
    if plan.removed_paths:
        message += f" | removed: {', '.join(plan.removed_paths[:5])}"
        if len(plan.removed_paths) > 5:
            message += f" (+{len(plan.removed_paths) - 5} more)"

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"'{quoted_log}'!A:D",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body={
            "values": [
                [
                    f"{eastern_now.month}/{eastern_now.day}/{eastern_now.year}",
                    "doc-ownership-sync",
                    "synced",
                    message,
                ]
            ]
        },
    ).execute()


def write_github_output(path: Path | None, data: dict[str, str]) -> None:
    if not path:
        return
    with path.open("a", encoding="utf-8") as f:
        for key, value in data.items():
            f.write(f"{key}={value}\n")


def write_summary_json(path: Path, plan: SyncPlan, *, changed: bool, csv_changed: bool) -> None:
    payload = {
        "changed": changed,
        "csv_changed": csv_changed,
        "added_count": len(plan.added_paths),
        "removed_count": len(plan.removed_paths),
        "total_count": len(plan.target_rows),
        "added_paths": plan.added_paths,
        "removed_paths": plan.removed_paths,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Compute diff only; do not write.")
    mode.add_argument("--apply", action="store_true", help="Update Google Sheet and CSV.")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help=f"Sync config YAML (default: {DEFAULT_CONFIG.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root (default: parent of scripts/)",
    )
    parser.add_argument(
        "--github-output",
        type=Path,
        default=None,
        help="Append key=value lines for GitHub Actions ($GITHUB_OUTPUT).",
    )
    parser.add_argument(
        "--summary-json",
        type=Path,
        default=None,
        help="Write machine-readable sync summary JSON to this path.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_config(args.config.resolve())
    root = args.root.resolve()
    csv_path = root / str(config.get("csv_output") or ".github/support_analyzer_doc_assignees.csv")

    repo_paths = enumerate_repo_paths(root, config)

    if args.dry_run:
        existing_rows = read_csv_rows(csv_path)
        writer_config = {
            row.writer: row.github_username
            for row in existing_rows.values()
            if row.writer and row.github_username
        }
    else:
        service = _get_sheets_service()
        existing_rows, writer_config = load_sheet_rows(service, config)

    plan = build_sync_plan(
        repo_paths=repo_paths,
        existing_rows=existing_rows,
        config=config,
        writer_config=writer_config,
    )

    changed = bool(plan.added_paths or plan.removed_paths)
    csv_changed = not csv_matches_plan(csv_path, plan)

    print(
        f"Eligible repo paths: {len(repo_paths)} | "
        f"sheet rows: {len(existing_rows)} | "
        f"added: {len(plan.added_paths)} | removed: {len(plan.removed_paths)} | "
        f"csv_changed: {csv_changed}",
        file=sys.stderr,
    )
    if plan.added_paths:
        print("Added:", file=sys.stderr)
        for path in plan.added_paths[:20]:
            print(f"  + {path}", file=sys.stderr)
        if len(plan.added_paths) > 20:
            print(f"  ... +{len(plan.added_paths) - 20} more", file=sys.stderr)
    if plan.removed_paths:
        print("Removed:", file=sys.stderr)
        for path in plan.removed_paths[:20]:
            print(f"  - {path}", file=sys.stderr)
        if len(plan.removed_paths) > 20:
            print(f"  ... -{len(plan.removed_paths) - 20} more", file=sys.stderr)

    if args.summary_json:
        write_summary_json(args.summary_json.resolve(), plan, changed=changed, csv_changed=csv_changed)

    if args.apply:
        service = None
        if changed:
            service = _get_sheets_service()
            apply_sheet_updates(service, config, plan)
        if csv_changed:
            rows_to_csv(plan.target_rows, csv_path)

    write_github_output(
        args.github_output,
        {
            "changed": "true" if changed else "false",
            "csv_changed": "true" if csv_changed else "false",
            "added_count": str(len(plan.added_paths)),
            "removed_count": str(len(plan.removed_paths)),
            "total_count": str(len(plan.target_rows)),
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
