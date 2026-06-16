#!/usr/bin/env python3
"""
Export Google Docs from a shared Drive folder (recursive) to JSON for @tam-solutions.

Uses the Google Drive API to list folders and export native Google Docs as plain text.
Output is intended for local Cursor triage—not for committing raw TAM content to develop.

Environment variables:
  GOOGLE_APPLICATION_CREDENTIALS   Path to a Google Cloud service account JSON key with
                                   Drive read access. The TAM Assets folder must be shared
                                   with the service account email (Viewer).
  TAM_DRIVE_FOLDER_ID              (optional) Root folder ID. Default: TAM Assets folder.
  TAM_SOLUTIONS_OUTPUT             (optional) Output JSON path. Default:
                                   _data/tam_solutions/export_<YYYYMMDD>.json
  TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA
                                   Set to "1" when you accept that exports may contain
                                   customer-specific content until generalized.

Dependencies (install once):
  pip install google-api-python-client google-auth

Usage:
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
  export TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1
  python3 scripts/tam-solutions/export_drive_solutions.py

OAuth alternative (no service account):
  python3 scripts/tam-solutions/export_drive_solutions.py --oauth
  First run opens a browser; token is saved to scripts/tam-solutions/.oauth_token.json
  (gitignored).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Default TAM Assets folder: https://drive.google.com/drive/folders/1APchTnf3UWN6MGpGkeBfryGMn73LBUM0
DEFAULT_FOLDER_ID = "1APchTnf3UWN6MGpGkeBfryGMn73LBUM0"

GOOGLE_DOC_MIME = "application/vnd.google-apps.document"
GOOGLE_FOLDER_MIME = "application/vnd.google-apps.folder"
EXPORT_MIME_PLAIN = "text/plain"

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "_data" / "tam_solutions"
OAUTH_TOKEN_PATH = SCRIPT_DIR / ".oauth_token.json"
OAUTH_CLIENT_SECRETS = SCRIPT_DIR / "oauth_client_secret.json"

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def _require_acknowledgement() -> None:
    if os.environ.get("TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA") != "1":
        print(
            "Set TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1 to confirm exports may "
            "contain sensitive TAM content. Do not commit raw exports to public branches.",
            file=sys.stderr,
        )
        sys.exit(1)


def _get_drive_service(use_oauth: bool) -> Any:
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        from google.auth.transport.requests import Request
    except ImportError:
        print(
            "Missing dependencies. Run: pip install google-api-python-client google-auth",
            file=sys.stderr,
        )
        sys.exit(1)

    if use_oauth:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow

        creds = None
        if OAUTH_TOKEN_PATH.exists():
            creds = Credentials.from_authorized_user_file(str(OAUTH_TOKEN_PATH), SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not OAUTH_CLIENT_SECRETS.exists():
                    print(
                        f"OAuth mode requires {OAUTH_CLIENT_SECRETS}. "
                        "Download OAuth client JSON from Google Cloud Console (Desktop app) "
                        "or use service account mode with GOOGLE_APPLICATION_CREDENTIALS.",
                        file=sys.stderr,
                    )
                    sys.exit(1)
                flow = InstalledAppFlow.from_client_secrets_file(str(OAUTH_CLIENT_SECRETS), SCOPES)
                creds = flow.run_local_server(port=0)
            OAUTH_TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
            OAUTH_TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
        return build("drive", "v3", credentials=creds, cache_discovery=False)

    creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds_path or not Path(creds_path).is_file():
        print(
            "Set GOOGLE_APPLICATION_CREDENTIALS to a service account JSON file, "
            "or pass --oauth for user credentials.",
            file=sys.stderr,
        )
        sys.exit(1)
    credentials = service_account.Credentials.from_service_account_file(creds_path, scopes=SCOPES)
    return build("drive", "v3", credentials=credentials, cache_discovery=False)


def _list_children(service: Any, folder_id: str) -> list[dict[str, str]]:
    files: list[dict[str, str]] = []
    page_token = None
    query = f"'{folder_id}' in parents and trashed = false"
    while True:
        response = (
            service.files()
            .list(
                q=query,
                fields="nextPageToken, files(id, name, mimeType, modifiedTime, webViewLink)",
                pageSize=200,
                pageToken=page_token,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            .execute()
        )
        files.extend(response.get("files", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return files


def _export_google_doc_text(service: Any, file_id: str) -> str:
    import io
    from googleapiclient.http import MediaIoBaseDownload

    request = service.files().export_media(fileId=file_id, mimeType=EXPORT_MIME_PLAIN)
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buffer.getvalue().decode("utf-8")


def _walk_folder(
    service: Any,
    folder_id: str,
    relative_path: str,
    solutions: list[dict[str, Any]],
    skipped: list[dict[str, str]],
) -> None:
    for item in _list_children(service, folder_id):
        name = item.get("name", "")
        mime = item.get("mimeType", "")
        item_path = f"{relative_path}/{name}" if relative_path else name

        if mime == GOOGLE_FOLDER_MIME:
            _walk_folder(service, item["id"], item_path, solutions, skipped)
            continue

        if mime == GOOGLE_DOC_MIME:
            try:
                text = _export_google_doc_text(service, item["id"])
            except Exception as exc:  # noqa: BLE001 — surface API errors per file
                skipped.append(
                    {
                        "path": item_path,
                        "file_id": item["id"],
                        "mime_type": mime,
                        "reason": f"export failed: {exc}",
                    }
                )
                continue

            category = relative_path.split("/")[0] if relative_path else "uncategorized"
            solutions.append(
                {
                    "file_id": item["id"],
                    "title": name,
                    "path": item_path,
                    "category": category,
                    "mime_type": mime,
                    "modified_time": item.get("modifiedTime"),
                    "web_view_link": item.get("webViewLink"),
                    "export_mime": EXPORT_MIME_PLAIN,
                    "text": text,
                }
            )
            continue

        skipped.append(
            {
                "path": item_path,
                "file_id": item["id"],
                "mime_type": mime,
                "reason": "not a native Google Doc (export only supports Google Docs)",
            }
        )


def _default_output_path() -> Path:
    env = os.environ.get("TAM_SOLUTIONS_OUTPUT")
    if env:
        return Path(env)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    return DEFAULT_OUTPUT_DIR / f"export_{stamp}.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Export TAM Google Docs to JSON")
    parser.add_argument(
        "--folder-id",
        default=os.environ.get("TAM_DRIVE_FOLDER_ID", DEFAULT_FOLDER_ID),
        help="Google Drive folder ID to export recursively",
    )
    parser.add_argument(
        "--oauth",
        action="store_true",
        help="Use OAuth user credentials instead of a service account",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output JSON file path",
    )
    args = parser.parse_args()

    _require_acknowledgement()

    output_path = args.output or _default_output_path()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    service = _get_drive_service(use_oauth=args.oauth)
    solutions: list[dict[str, Any]] = []
    skipped: list[dict[str, str]] = []

    _walk_folder(service, args.folder_id, "", solutions, skipped)

    payload = {
        "export_version": 1,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "source_folder_id": args.folder_id,
        "source_folder_url": f"https://drive.google.com/drive/folders/{args.folder_id}",
        "solution_count": len(solutions),
        "skipped_count": len(skipped),
        "solutions": solutions,
        "skipped": skipped,
    }

    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Exported {len(solutions)} Google Doc(s) to {output_path}")
    if skipped:
        print(f"Skipped {len(skipped)} file(s) (see 'skipped' in JSON).")


if __name__ == "__main__":
    main()
