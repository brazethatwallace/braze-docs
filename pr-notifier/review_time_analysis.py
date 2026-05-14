#!/usr/bin/env python3
"""
Review Time Analysis
Calculates the average time from a non-docs-team member being requested as a reviewer
to when they submitted an approval, across PRs closed in the last 30 days.
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")

with open(CONFIG_PATH) as f:
    cfg = json.load(f)

TOKEN = cfg.get("github_token", "").strip()
REPO  = cfg.get("repo", "braze-inc/braze-docs")

github_to_slack = cfg.get("github_to_slack", {})
extra_docs      = set(m.lower() for m in cfg.get("extra_docs_team_members", [])
                      if not m.startswith("_"))
ignored         = {r.lower() for r in cfg.get("ignored_reviewers", [])}

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "braze-docs-review-time-analysis/1.0",
}

def gh_get(path, **params):
    url = f"https://api.github.com{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"_error": str(e)}

def gh_paginate(path, **params):
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

# Build docs team set
docs_team = set()
members = gh_paginate(f"/orgs/braze-inc/teams/docs-team/members")
if members and isinstance(members[0], dict) and "_error" not in members[0]:
    docs_team = {m["login"].lower() for m in members}
docs_team.update(extra_docs)
docs_team.update(k.lower() for k in github_to_slack.keys() if not k.startswith("_"))

def is_external_human(login, user_type="User"):
    l = login.lower()
    return (
        user_type != "Bot"
        and l not in docs_team
        and l not in ignored
    )

# Fetch PRs closed in the last 30 days
since = (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
print(f"Fetching PRs closed since {since[:10]}...", flush=True)

closed_prs = gh_paginate(f"/repos/{REPO}/pulls", state="closed", sort="updated", direction="desc")

cutoff = datetime.now(timezone.utc) - timedelta(days=30)
recent_prs = [
    pr for pr in closed_prs
    if pr.get("closed_at")
    and datetime.fromisoformat(pr["closed_at"].replace("Z", "+00:00")) >= cutoff
]

print(f"Found {len(recent_prs)} PRs closed in the last 30 days. Analyzing...", flush=True)

deltas = []  # list of hours between request and approval

for i, pr in enumerate(recent_prs):
    num = pr["number"]
    print(f"  [{i+1}/{len(recent_prs)}] PR #{num}", end="\r", flush=True)

    # Get timeline events to find when non-docs-team members were requested
    events = gh_paginate(f"/repos/{REPO}/issues/{num}/timeline")
    request_times = {}  # login → earliest request datetime

    for event in events:
        if event.get("event") == "review_requested":
            reviewer = event.get("requested_reviewer")
            if not reviewer:
                continue
            login = reviewer.get("login", "").lower()
            utype = reviewer.get("type", "User")
            if not is_external_human(login, utype):
                continue
            ts = event.get("created_at")
            if not ts:
                continue
            dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            # Keep the earliest request time per reviewer
            if login not in request_times or dt < request_times[login]:
                request_times[login] = dt

    if not request_times:
        continue

    # Get reviews to find approvals from those same people
    reviews = gh_paginate(f"/repos/{REPO}/pulls/{num}/reviews")

    for review in reviews:
        if review.get("state") != "APPROVED":
            continue
        user = review.get("user")
        if not user:
            continue
        login = user.get("login", "").lower()
        utype = user.get("type", "User")
        if not is_external_human(login, utype):
            continue
        if login not in request_times:
            continue
        approved_at = review.get("submitted_at")
        if not approved_at:
            continue
        approved_dt = datetime.fromisoformat(approved_at.replace("Z", "+00:00"))
        requested_dt = request_times[login]
        delta_hours = (approved_dt - requested_dt).total_seconds() / 3600
        # Only count positive deltas (approval after request)
        if delta_hours > 0:
            deltas.append(delta_hours)

print()  # clear the progress line

if not deltas:
    print("No matching reviewer→approval pairs found in the last 30 days.")
else:
    avg_hours = sum(deltas) / len(deltas)
    avg_days  = avg_hours / 24
    median    = sorted(deltas)[len(deltas) // 2]

    print(f"\n{'='*50}")
    print(f"  PRs analyzed:        {len(recent_prs)}")
    print(f"  Reviewer→approval pairs found: {len(deltas)}")
    print(f"  Average time:        {avg_hours:.1f} hours ({avg_days:.1f} days)")
    print(f"  Median time:         {median:.1f} hours ({median/24:.1f} days)")
    print(f"{'='*50}\n")
