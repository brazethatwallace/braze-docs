# TAM solutions — Google Drive export

Exports native **Google Docs** from the [TAM Assets Drive folder](https://drive.google.com/drive/folders/1APchTnf3UWN6MGpGkeBfryGMn73LBUM0) to JSON for the [`tam-solutions`](../.github/skills/tam-solutions/SKILL.md) Cursor workflow.

## What it does

- Recursively walks a shared Drive folder
- Exports each Google Doc as plain text (`text/plain`)
- Writes one JSON file with metadata (`title`, `path`, `category`, `web_view_link`, `text`, …)
- Skips non–Google Doc files (PDF, Word uploads, Sheets, etc.) with reasons in `skipped`

## Setup

### 1. Google Cloud project

1. Create or use a GCP project with the **Google Drive API** enabled.
2. Choose one auth mode:

| Mode | When to use |
|------|-------------|
| **Service account** (recommended for automation) | Shared folder is visible to a robot account |
| **OAuth** (`--oauth`) | Personal Drive access; no service account |

### 2. Service account (recommended)

1. Create a service account and download its JSON key.
2. Share the TAM Assets folder (or parent) with the service account email as **Viewer**.
3. Export:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
export TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1
pip install google-api-python-client google-auth
python3 scripts/tam-solutions/export_drive_solutions.py
```

### 3. OAuth (alternative)

1. Create an OAuth **Desktop** client in GCP and save JSON as `scripts/tam-solutions/oauth_client_secret.json` (do not commit).
2. Run:

```bash
export TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1
pip install google-api-python-client google-auth google-auth-oauthlib
python3 scripts/tam-solutions/export_drive_solutions.py --oauth
```

Token is stored in `scripts/tam-solutions/.oauth_token.json` (gitignored).

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TAM_SOLUTIONS_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA` | Yes | Must be `1` — exports may contain customer-specific content |
| `GOOGLE_APPLICATION_CREDENTIALS` | Service account mode | Path to service account JSON |
| `TAM_DRIVE_FOLDER_ID` | No | Root folder ID (default: TAM Assets folder) |
| `TAM_SOLUTIONS_OUTPUT` | No | Output path (default: `_data/tam_solutions/export_<YYYYMMDD>.json`) |

## Output shape

```json
{
  "export_version": 1,
  "exported_at": "2026-06-12T12:00:00+00:00",
  "source_folder_id": "...",
  "source_folder_url": "https://drive.google.com/drive/folders/...",
  "solution_count": 2,
  "skipped_count": 1,
  "solutions": [
    {
      "file_id": "...",
      "title": "Filtering Catalog items by date range",
      "path": "Catalog/date_range_selection",
      "category": "Catalog",
      "mime_type": "application/vnd.google-apps.document",
      "modified_time": "...",
      "web_view_link": "https://docs.google.com/document/d/.../edit",
      "export_mime": "text/plain",
      "text": "..."
    }
  ],
  "skipped": []
}
```

`category` is the top-level folder name under the export root—useful for audit counts per vertical.

## Security

- Treat exports as **sensitive** until generalized. Default output path is gitignored.
- Do not commit raw JSON to `develop`. Use local export or a private data branch (similar to `support-analyzer-data`).
- The skill generalizes and scrubs PII before any public docs PR.

## Limitations

- **Google Docs only** — PDFs in Drive (common for TAM whitepapers) are not exported. Convert to Google Docs, paste into chat, or extend the script to download PDF bytes.
- **Plain text export** — section structure is not preserved; audit completeness from headings in `text` or parse heuristically later.
- **Connected Content / live URLs** in docs are exported as-is in `text`.
