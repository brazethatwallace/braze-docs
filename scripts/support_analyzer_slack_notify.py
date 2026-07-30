#!/usr/bin/env python3
"""
Post Support analyzer (Looker) workflow results to Slack (#docs_request).

Used by .github/workflows/export-support-cases-from-looker.yml notify job.
Requires SLACK_BOT_TOKEN and SLACK_DOCS_REQUEST_CHANNEL (channel ID), with optional
fallback to SLACK_DEPLOY_NOTIFY_CHANNEL.

Optional SUPPORT_ANALYZER_GITHUB_TO_SLACK: JSON object mapping GitHub login → Slack
member ID (U…), same shape as pr-notifier github_to_slack entries.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


def _slack_api(token: str, method: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    url = f"https://slack.com/api/{method}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}"},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _load_github_to_slack() -> dict[str, str]:
    raw = (os.environ.get("SUPPORT_ANALYZER_GITHUB_TO_SLACK") or "").strip()
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid SUPPORT_ANALYZER_GITHUB_TO_SLACK JSON: {e}", file=sys.stderr)
        return {}
    if not isinstance(data, dict):
        return {}
    out: dict[str, str] = {}
    for k, v in data.items():
        if isinstance(k, str) and isinstance(v, str) and v.strip():
            out[k.lower()] = v.strip()
    return out


def _build_slack_user_index(token: str) -> dict[str, str]:
    """Map lowercase GitHub-like handles to Slack member IDs."""
    index: dict[str, str] = {}
    cursor = ""
    for _ in range(50):
        params: dict[str, str] = {"limit": "200"}
        if cursor:
            params["cursor"] = cursor
        data = _slack_api(token, "users.list", params)
        if not data.get("ok"):
            print(f"users.list failed: {data.get('error')}", file=sys.stderr)
            break
        for member in data.get("members") or []:
            if member.get("deleted") or member.get("is_bot"):
                continue
            mid = member.get("id") or ""
            if not mid.startswith("U"):
                continue
            name = (member.get("name") or "").strip().lower()
            profile = member.get("profile") or {}
            display = (profile.get("display_name") or "").strip().lower()
            if name:
                index.setdefault(name, mid)
            if display:
                index.setdefault(display, mid)
        cursor = (data.get("response_metadata") or {}).get("next_cursor") or ""
        if not cursor:
            break
    return index


def _mention(login: str, *, explicit: dict[str, str], slack_index: dict[str, str]) -> str:
    key = login.strip().lower()
    if not key:
        return ""
    sid = explicit.get(key) or slack_index.get(key)
    if sid and sid.startswith("U"):
        return f"<@{sid}>"
    return f"@{login}"


def _mentions_for_logins(
    logins: list[str],
    *,
    explicit: dict[str, str],
    slack_index: dict[str, str],
) -> str:
    seen: set[str] = set()
    parts: list[str] = []
    for login in logins:
        lk = login.strip().lower()
        if not lk or lk in seen:
            continue
        seen.add(lk)
        parts.append(_mention(login, explicit=explicit, slack_index=slack_index))
    return " ".join(parts)


def _post_message(token: str, channel: str, text: str) -> None:
    payload = json.dumps(
        {
            "channel": channel,
            "unfurl_links": False,
            "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": text}}],
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(data, indent=2))
    if not data.get("ok"):
        raise SystemExit(f"chat.postMessage failed: {data.get('error')}")


def _job_failed(result: str) -> bool:
    return result in ("failure", "cancelled")


def main() -> None:
    token = (os.environ.get("SLACK_BOT_TOKEN") or "").strip()
    channel = (
        (os.environ.get("SLACK_DOCS_REQUEST_CHANNEL") or "").strip()
        or (os.environ.get("SLACK_DEPLOY_NOTIFY_CHANNEL") or "").strip()
    )
    if not token or not channel:
        print(
            "Slack not configured (set SLACK_BOT_TOKEN and SLACK_DOCS_REQUEST_CHANNEL); skipping.",
            file=sys.stderr,
        )
        return

    run_url = (os.environ.get("RUN_URL") or "").strip()
    export_result = os.environ.get("NEEDS_EXPORT_RESULT", "")
    digest_result = os.environ.get("NEEDS_DIGEST_RESULT", "")
    phase2_result = os.environ.get("NEEDS_PHASE2_RESULT", "")
    skip_phase2 = (os.environ.get("SKIP_PHASE2") or "").lower() in ("1", "true", "yes")

    summary_path = Path(
        os.environ.get("PHASE2_SUMMARY_PATH", ".github/support_analyzer_phase2_run_summary.json")
    )
    opened: list[dict[str, Any]] = []
    if summary_path.is_file():
        try:
            doc = json.loads(summary_path.read_text(encoding="utf-8"))
            opened = list(doc.get("opened") or [])
        except (json.JSONDecodeError, OSError) as e:
            print(f"Could not read run summary: {e}", file=sys.stderr)

    failed_jobs: list[str] = []
    if _job_failed(export_result):
        failed_jobs.append("export")
    if _job_failed(digest_result):
        failed_jobs.append("digest")
    if not skip_phase2 and _job_failed(phase2_result):
        failed_jobs.append("phase 2")

    explicit = _load_github_to_slack()
    slack_index: dict[str, str] = {}
    if opened or failed_jobs:
        try:
            slack_index = _build_slack_user_index(token)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"Slack users.list failed: {e}", file=sys.stderr)

    if failed_jobs:
        jobs = ", ".join(failed_jobs)
        text = f":x: *Support analyzer (Looker)* failed ({jobs})\n{run_url}"
        _post_message(token, channel, text)
        return

    lines: list[str] = []

    if opened:
        n_opened = len(opened)
        pr_label = "PR" if n_opened == 1 else "PRs"
        lines.append(
            f":white_check_mark: *Support analyzer (Looker)* — opened {n_opened} support-analyzer {pr_label}"
        )
        if run_url:
            lines.append(run_url)
        for item in opened:
            pr_url = (item.get("pr_url") or "").strip()
            rule_id = (item.get("rule_id") or "").strip()
            title = (item.get("title") or rule_id).strip()
            assignees = [str(a) for a in (item.get("assignees") or []) if str(a).strip()]
            mention = _mentions_for_logins(assignees, explicit=explicit, slack_index=slack_index)
            if pr_url:
                line = f"• <{pr_url}|{title}>"
            else:
                line = f"• {title}"
            if mention:
                line += f" — {mention}"
            lines.append(line)
        _post_message(token, channel, "\n".join(lines))
        return

    print("Nothing to post to Slack for this run.", file=sys.stderr)


if __name__ == "__main__":
    main()
