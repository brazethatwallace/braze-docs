#!/usr/bin/env python3
"""
Doc-path assignees for Salesforce KB Phase 2.

Resolves from `.github/support_analyzer_doc_assignees.csv` (longest path prefix):
GitHub username, product vertical (`Team`), and Jira `accountId` via
`.github/github_to_jira_assignees.json`.
"""

from __future__ import annotations

import csv
import json
import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ASSIGNEES_PATH = REPO_ROOT / ".github" / "support_analyzer_doc_assignees.csv"
GITHUB_TO_JIRA_PATH = REPO_ROOT / ".github" / "github_to_jira_assignees.json"

SKIP_GITHUB_USERNAMES = frozenset({"docs-team"})
# Spreadsheet placeholders in the Team column — not real product verticals.
SKIP_TEAM_VALUES = frozenset({"fix", "n/a", "na", "tbd", "none", "unknown"})


@dataclass(frozen=True)
class DocPathAssignees:
    github_username: str | None
    product_vertical: str | None
    jira_account_id: str | None


def _assignee_row_for_doc_path(doc_path: str) -> dict[str, str] | None:
    """Longest-prefix match row in support_analyzer_doc_assignees.csv."""
    if not ASSIGNEES_PATH.is_file():
        return None
    best_len = -1
    best_row: dict[str, str] | None = None
    with ASSIGNEES_PATH.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            page = (row.get("Page Path") or row.get("page path") or "").strip()
            if not page:
                continue
            if doc_path.startswith(page) and len(page) > best_len:
                best_len = len(page)
                best_row = row
    return best_row


def _valid_product_vertical(team: str | None) -> str | None:
    value = (team or "").strip()
    if not value or value.lower() in SKIP_TEAM_VALUES:
        return None
    return value


def product_vertical_for_doc_path(doc_path: str) -> str | None:
    """Product vertical from the CSV ``Team`` column (longest path prefix)."""
    row = _assignee_row_for_doc_path(doc_path)
    if not row:
        return None
    team = row.get("Team") or row.get("team")
    return _valid_product_vertical(team)


def lookup_github_assignee(doc_path: str) -> str | None:
    """Longest-prefix match in support_analyzer_doc_assignees.csv → GitHub username."""
    row = _assignee_row_for_doc_path(doc_path)
    if not row:
        return None
    user = (row.get("GitHub Username") or row.get("github username") or "").strip()
    if not user or user.startswith("@") or user in SKIP_GITHUB_USERNAMES:
        return None
    return user


@lru_cache(maxsize=1)
def _load_github_to_jira() -> dict[str, str]:
    if not GITHUB_TO_JIRA_PATH.is_file():
        return {}
    data = json.loads(GITHUB_TO_JIRA_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {}
    return {
        str(key).strip().lower(): str(value).strip()
        for key, value in data.items()
        if str(key).strip() and str(value).strip()
    }


def jira_account_id_for_github(github_username: str | None) -> str | None:
    """Map a GitHub username to a Jira Cloud accountId."""
    if not github_username:
        return None
    user = github_username.strip().lstrip("@")
    if not user or user in SKIP_GITHUB_USERNAMES:
        return None
    mapped = _load_github_to_jira().get(user.lower())
    if mapped:
        return mapped
    fallback = os.environ.get("JIRA_ASSIGNEE_ACCOUNT_ID", "").strip()
    return fallback or None


def assignees_for_doc_path(doc_path: str) -> DocPathAssignees:
    """Return GitHub assignee, product vertical, and Jira accountId for a doc path."""
    github = lookup_github_assignee(doc_path)
    return DocPathAssignees(
        github_username=github,
        product_vertical=product_vertical_for_doc_path(doc_path),
        jira_account_id=jira_account_id_for_github(github),
    )
