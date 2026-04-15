#!/usr/bin/env python3
"""
Braze Docs PR Triage Checker
Checks braze-inc/braze-docs for PRs needing attention and outputs JSON.

Scenario 1 — Needs review setup:
  PR is missing the "In Review" label OR has no non-docs-team reviewers tagged.

Scenario 2 — Approved but stale:
  A non-docs-team member approved the PR, but no changes have been made in STALE_DAYS days.
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")

with open(CONFIG_PATH) as f:
    cfg = json.load(f)

TOKEN = cfg.get("github_token", "").strip()
if not TOKEN or TOKEN == "ghp_YOUR_GITHUB_TOKEN_HERE":
    print(json.dumps({"error": "GitHub token not set. Edit pr-notifier/config.json and add your token."}))
    sys.exit(1)

REPO         = cfg.get("repo", "braze-inc/braze-docs")
STALE_DAYS   = cfg.get("stale_days", 7)
GH_TO_SLACK  = cfg.get("github_to_slack", {})   # { "github_handle": "slack_user_id" }
EXTRA_DOCS   = set(cfg.get("extra_docs_team_members", []))  # fallback list

# ── GitHub helpers ─────────────────────────────────────────────────────────────

BASE = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "braze-docs-pr-triage-bot/1.0",
}

def gh_get(path, **params):
    url = f"{BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"_error": str(e), "_status": e.code, "_body": body}

def gh_paginate(path, **params):
    """Fetch all pages of a list endpoint."""
    results = []
    page = 1
    while True:
        batch = gh_get(path, per_page=100, page=page, **params)
        if not isinstance(batch, list):
            break
        results.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return results

# ── Fetch docs team members ────────────────────────────────────────────────────

docs_team = set(EXTRA_DOCS)
team_fetch_error = None

team_members = gh_paginate("/orgs/braze-inc/teams/docs-team/members")
if team_members and isinstance(team_members[0], dict) and "_error" not in team_members[0]:
    docs_team.update(m["login"] for m in team_members)
else:
    team_fetch_error = "Could not fetch braze-inc/docs-team members from GitHub API (token may need read:org scope). Using extra_docs_team_members list from config instead."

# ── Fetch all open PRs ─────────────────────────────────────────────────────────

all_prs = gh_paginate(f"/repos/{REPO}/pulls", state="open")

now = datetime.now(timezone.utc)
scenario1 = []
scenario2 = []

def slack_mention(github_login):
    """Return a Slack mention string for a GitHub user.

    - If the mapped value looks like a Slack user ID (e.g. U0A1B2C3D) → <@USERID> (real ping)
    - If it's a display name → @display-name (visible but won't ping)
    - If no mapping → shows the GitHub handle in backticks
    To enable real pings, replace display names in config.json with Slack user IDs
    (open someone's Slack profile → ⋮ → Copy member ID).
    """
    import re
    slack_val = GH_TO_SLACK.get(github_login)
    if slack_val and re.match(r'^[UW][A-Z0-9]{6,}$', slack_val):
        return f"<@{slack_val}>"          # Real Slack user ID — will ping
    if slack_val:
        return f"@{slack_val}"            # Display name — visible but no ping
    return f"`@{github_login}`"           # No mapping — show GitHub handle

for pr in all_prs:
    num        = pr["number"]
    title      = pr["title"]
    author     = pr["user"]["login"]
    url        = pr["html_url"]
    labels     = {l["name"] for l in pr.get("labels", [])}
    created_at = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))
    updated_at = datetime.fromisoformat(pr["updated_at"].replace("Z", "+00:00"))
    days_open          = (now - created_at).days
    days_since_update  = (now - updated_at).days

    # Reviewers explicitly requested (non-docs-team)
    requested_non_docs = [
        r["login"] for r in pr.get("requested_reviewers", [])
        if r["login"] not in docs_team
    ]

    # All reviews submitted
    reviews_raw = gh_get(f"/repos/{REPO}/pulls/{num}/reviews")
    reviews = reviews_raw if isinstance(reviews_raw, list) else []

    reviewed_non_docs  = [r["user"]["login"] for r in reviews if r["user"]["login"] not in docs_team]
    approved_non_docs  = [r["user"]["login"] for r in reviews
                          if r["user"]["login"] not in docs_team and r["state"] == "APPROVED"]

    has_non_docs_involvement = bool(requested_non_docs or reviewed_non_docs)

    # ── Scenario 1 ──────────────────────────────────────────────────────────
    no_label    = "In Review" not in labels
    no_non_docs = not has_non_docs_involvement

    if no_label or no_non_docs:
        reasons = []
        if no_label:
            reasons.append("missing \"In Review\" label")
        if no_non_docs:
            reasons.append("no stakeholder reviewers tagged")

        scenario1.append({
            "number":   num,
            "title":    title,
            "author":   author,
            "author_mention": slack_mention(author),
            "url":      url,
            "days_open": days_open,
            "labels":   sorted(labels),
            "reason":   " & ".join(reasons),
        })

    # ── Scenario 2 ──────────────────────────────────────────────────────────
    if approved_non_docs and days_since_update >= STALE_DAYS:
        unique_approvers = sorted(set(approved_non_docs))
        scenario2.append({
            "number":   num,
            "title":    title,
            "author":   author,
            "author_mention": slack_mention(author),
            "url":      url,
            "days_since_update": days_since_update,
            "approvers": unique_approvers,
            "approver_mentions": [slack_mention(a) for a in unique_approvers],
        })

# ── Output ─────────────────────────────────────────────────────────────────────

output = {
    "scenario1":        scenario1,
    "scenario2":        scenario2,
    "docs_team_count":  len(docs_team),
    "total_open_prs":   len(all_prs),
    "checked_at":       now.isoformat(),
    "repo":             REPO,
    "stale_days":       STALE_DAYS,
}
if team_fetch_error:
    output["warning"] = team_fetch_error

print(json.dumps(output, indent=2))
