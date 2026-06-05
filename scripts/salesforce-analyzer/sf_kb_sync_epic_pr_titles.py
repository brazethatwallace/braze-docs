#!/usr/bin/env python3
"""
Rename braze-docs PRs for Epic BD-6308 children to ``[BD-####](SF) TICKET_NAME``.

Reads each task under parent epic BD-6308, finds the linked GitHub PR (Jira description
or ``gh pr list`` search), and runs ``gh pr edit --title`` when the title is not already
in the required format. Works for open and merged PRs.

Requires JIRA_USER_EMAIL, JIRA_API_TOKEN, and ``gh`` authenticated for braze-inc/braze-docs.

Usage (repo root):
  python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py
  python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py --dry-run
  python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py --issue BD-6402
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from typing import Any

from sf_kb_jira_ticket import (
    EPIC_KEY,
    GITHUB_PR_URL_RE,
    JiraTicketError,
    SF_KB_PR_TITLE_KEY_RE,
    _jira_base_url,
    _jira_request,
    format_sf_kb_pr_title,
    gh_pr_edit_title,
    strip_legacy_sf_kb_title_prefixes,
)

DEFAULT_REPO = "braze-inc/braze-docs"
JIRA_KEY_IN_TEXT_RE = re.compile(r"\b(BD-\d+)\b", re.I)


def _walk_adf_links(node: Any, out: list[str]) -> None:
    if isinstance(node, dict):
        if node.get("type") == "text":
            marks = node.get("marks") or []
            for mark in marks:
                if mark.get("type") == "link":
                    href = (mark.get("attrs") or {}).get("href")
                    if href:
                        out.append(str(href))
        for value in node.values():
            _walk_adf_links(value, out)
    elif isinstance(node, list):
        for item in node:
            _walk_adf_links(item, out)


def pr_url_from_jira_description(description: Any) -> str | None:
    if not description:
        return None
    if isinstance(description, str):
        m = GITHUB_PR_URL_RE.search(description)
        if m and "braze-docs" in m.group(0):
            return m.group(0)
        return None
    links: list[str] = []
    if isinstance(description, dict):
        _walk_adf_links(description, links)
    for href in links:
        if GITHUB_PR_URL_RE.search(href) and "braze-docs" in href:
            return href
    return None


def ticket_name_from_jira_summary(summary: str) -> str:
    return strip_legacy_sf_kb_title_prefixes(summary)


def search_gh_pr_by_issue_key(issue_key: str, *, repo: str) -> str | None:
    """Find a PR whose title contains ``[BD-####]`` via GitHub CLI."""
    proc = subprocess.run(
        [
            "gh",
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "all",
            "--search",
            f"[{issue_key}] in:title",
            "--limit",
            "5",
            "--json",
            "url,title",
        ],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return None
    try:
        rows = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        return None
    key_upper = issue_key.upper()
    for row in rows:
        title = row.get("title") or ""
        if SF_KB_PR_TITLE_KEY_RE.match(title) and f"[{key_upper}]" in title.upper():
            return row.get("url")
    if rows:
        return rows[0].get("url")
    return None


def gh_pr_title(pr_url: str, *, repo: str) -> str | None:
    m = GITHUB_PR_URL_RE.search(pr_url)
    if not m:
        return None
    number = m.group("number")
    proc = subprocess.run(
        ["gh", "pr", "view", number, "--repo", repo, "--json", "title"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return None
    try:
        return json.loads(proc.stdout or "{}").get("title")
    except json.JSONDecodeError:
        return None


def list_epic_child_issues(
    *,
    epic_key: str,
    single_issue: str | None = None,
) -> list[dict[str, Any]]:
    if single_issue:
        body = _jira_request(
            "GET",
            f"/rest/api/3/issue/{single_issue.strip().upper()}?fields=summary,description",
        )
        if not isinstance(body, dict):
            return []
        return [body]

    jql = f'parent = {epic_key} ORDER BY key ASC'
    issues: list[dict[str, Any]] = []
    start_at = 0
    page_size = 100
    while True:
        body = _jira_request(
            "POST",
            "/rest/api/3/search/jql",
            payload={
                "jql": jql,
                "maxResults": page_size,
                "startAt": start_at,
                "fields": ["summary", "description"],
            },
        )
        if not isinstance(body, dict):
            break
        batch = body.get("issues") or []
        issues.extend(batch)
        if body.get("isLast", True) or len(batch) < page_size:
            break
        start_at += len(batch)
    return issues


def sync_issue(
    issue: dict[str, Any],
    *,
    repo: str,
    dry_run: bool,
) -> str:
    key = str(issue.get("key") or "").upper()
    fields = issue.get("fields") or {}
    summary = str(fields.get("summary") or "")
    ticket_name = ticket_name_from_jira_summary(summary)
    if not ticket_name:
        return f"{key}: skip (empty ticket name from summary)"

    expected_title = format_sf_kb_pr_title(key, ticket_name)
    pr_url = pr_url_from_jira_description(fields.get("description"))
    if not pr_url:
        pr_url = search_gh_pr_by_issue_key(key, repo=repo)
    if not pr_url:
        return f"{key}: skip (no GitHub PR found)"

    current = gh_pr_title(pr_url, repo=repo) or ""
    if current.strip() == expected_title:
        return f"{key}: ok `{expected_title}` (#{GITHUB_PR_URL_RE.search(pr_url).group('number')})"

    if dry_run:
        return f"{key}: would rename #{GITHUB_PR_URL_RE.search(pr_url).group('number')}\n  from: {current}\n  to:   {expected_title}"

    gh_pr_edit_title(pr_url, expected_title, repo=repo, dry_run=False)
    return (
        f"{key}: renamed #{GITHUB_PR_URL_RE.search(pr_url).group('number')}\n"
        f"  from: {current}\n"
        f"  to:   {expected_title}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--issue", help="Sync one issue key (for example BD-6402)")
    args = parser.parse_args()

    try:
        issues = list_epic_child_issues(epic_key=EPIC_KEY, single_issue=args.issue)
    except JiraTicketError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    if not issues:
        print("No issues found.", file=sys.stderr)
        sys.exit(1)

    print(f"Epic {EPIC_KEY}: {len(issues)} issue(s) @ {_jira_base_url()}/browse/{EPIC_KEY}\n")
    changed = 0
    for issue in issues:
        line = sync_issue(issue, repo=args.repo, dry_run=args.dry_run)
        print(line)
        print()
        if "renamed" in line or "would rename" in line:
            changed += 1
    print(f"Done. {changed} PR title(s) {'would be ' if args.dry_run else ''}updated.")


if __name__ == "__main__":
    main()
