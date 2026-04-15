#!/usr/bin/env python3
"""
Braze Docs PR Triage Checker
Checks braze-inc/braze-docs for PRs that newly meet notification criteria.

State is persisted in state.json so each PR is only notified once per threshold
crossing. If a PR is updated after being notified, its state resets — it can
trigger again if it goes stale a second time.

Scenario 1 — Needs review setup:
  PR is missing the "In Review" label OR has no non-docs-team reviewers tagged.
  Notify once when the PR first hits this state. Reset if the PR is fixed
  (label added / reviewer tagged), so it can re-notify if it breaks again.

Scenario 2 — Approved but stale:
  A non-docs-team member approved the PR, but no changes have been made in
  STALE_DAYS days. Notify once. If the PR author pushes an update, the stale
  clock resets — re-notify if it goes stale again after that update.

Subcommand:
  python3 check_prs.py save-thread <s1|s2> <pr_number> <slack_thread_ts>
    Persists the Slack thread timestamp for a PR notification into state.json.
    Call this after posting a notification to Slack so future runs can reply
    to the same thread when the PR is resolved.
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")
STATE_PATH  = os.path.join(SCRIPT_DIR, "state.json")

# ── Subcommand: save-thread ───────────────────────────────────────────────────

if len(sys.argv) == 5 and sys.argv[1] == "save-thread":
    _, _, scenario, pr_num_str, thread_ts = sys.argv
    if scenario not in ("s1", "s2"):
        print(json.dumps({"error": "scenario must be 's1' or 's2'"}))
        sys.exit(1)
    try:
        pr_num = int(pr_num_str)
    except ValueError:
        print(json.dumps({"error": f"invalid pr_number: {pr_num_str!r}"}))
        sys.exit(1)

    state = {}
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH) as f:
                state = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    state.setdefault("thread_ts", {})
    key = f"{scenario}_{pr_num}"
    state["thread_ts"][key] = thread_ts

    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

    print(json.dumps({"saved": key, "thread_ts": thread_ts}))
    sys.exit(0)

# ── Load config ───────────────────────────────────────────────────────────────

with open(CONFIG_PATH) as f:
    cfg = json.load(f)

TOKEN = cfg.get("github_token", "").strip()
if not TOKEN or TOKEN == "ghp_YOUR_GITHUB_TOKEN_HERE":
    print(json.dumps({"error": "GitHub token not set. Edit pr-notifier/config.json and add your token."}))
    sys.exit(1)

REPO        = cfg.get("repo", "braze-inc/braze-docs")
STALE_DAYS  = cfg.get("stale_days", 7)
GH_TO_SLACK = cfg.get("github_to_slack", {})
EXTRA_DOCS  = set(cfg.get("extra_docs_team_members", []))

# ── State ─────────────────────────────────────────────────────────────────────

def load_state():
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {
        "scenario1_notified": [],
        "scenario2_notified": {},
        "thread_ts": {},
    }

def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

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
    team_fetch_error = (
        "Could not fetch braze-inc/docs-team members from GitHub API "
        "(token may need read:org scope). Using extra_docs_team_members list from config instead."
    )

# ── Fetch all open PRs ─────────────────────────────────────────────────────────

all_prs = gh_paginate(f"/repos/{REPO}/pulls", state="open")
open_pr_numbers = {pr["number"] for pr in all_prs}

now   = datetime.now(timezone.utc)
state = load_state()

state.setdefault("scenario1_notified", [])
state.setdefault("scenario2_notified", {})
state.setdefault("thread_ts", {})

s1_notified = set(state["scenario1_notified"])
s2_notified = dict(state["scenario2_notified"])
thread_ts   = dict(state["thread_ts"])

new_scenario1      = []
new_scenario2      = []
resolved_scenario1 = []
resolved_scenario2 = []

# ── Slack mention helper ───────────────────────────────────────────────────────

def slack_mention(github_login):
    import re
    slack_val = GH_TO_SLACK.get(github_login)
    if slack_val and re.match(r'^[UW][A-Z0-9]{6,}$', slack_val):
        return f"<@{slack_val}>"
    if slack_val:
        return f"@{slack_val}"
    return f"`@{github_login}`"

# ── Evaluate each open PR ──────────────────────────────────────────────────────

for pr in all_prs:
    num        = pr["number"]
    title      = pr["title"]
    author     = pr["user"]["login"]
    url        = pr["html_url"]
    labels     = {l["name"] for l in pr.get("labels", [])}
    created_at = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))
    updated_at = datetime.fromisoformat(pr["updated_at"].replace("Z", "+00:00"))
    days_open         = (now - created_at).days
    days_since_update = (now - updated_at).days
    updated_at_str    = pr["updated_at"]

    requested_non_docs = [
        r["login"] for r in pr.get("requested_reviewers", [])
        if r["login"] not in docs_team
    ]

    reviews_raw = gh_get(f"/repos/{REPO}/pulls/{num}/reviews")
    reviews = reviews_raw if isinstance(reviews_raw, list) else []

    reviewed_non_docs = [r["user"]["login"] for r in reviews if r["user"]["login"] not in docs_team]
    approved_non_docs = [r["user"]["login"] for r in reviews
                         if r["user"]["login"] not in docs_team and r["state"] == "APPROVED"]

    has_non_docs_involvement = bool(requested_non_docs or reviewed_non_docs)

    # ── Scenario 1 ──────────────────────────────────────────────────────────
    no_label    = "In Review" not in labels
    no_non_docs = not has_non_docs_involvement
    meets_s1    = no_label or no_non_docs

    if meets_s1:
        if num not in s1_notified:
            reasons = []
            if no_label:
                reasons.append('missing "In Review" label')
            if no_non_docs:
                reasons.append("no stakeholder reviewers tagged")
            new_scenario1.append({
                "number":         num,
                "title":          title,
                "author":         author,
                "author_mention": slack_mention(author),
                "url":            url,
                "days_open":      days_open,
                "labels":         sorted(labels),
                "reason":         " & ".join(reasons),
            })
            s1_notified.add(num)
    else:
        if num in s1_notified:
            # PR just resolved — capture thread_ts so we can reply to the original message
            resolved_scenario1.append({
                "number":    num,
                "title":     title,
                "url":       url,
                "thread_ts": thread_ts.get(f"s1_{num}"),
            })
            s1_notified.discard(num)
            thread_ts.pop(f"s1_{num}", None)

    # ── Scenario 2 ──────────────────────────────────────────────────────────
    meets_s2 = bool(approved_non_docs) and days_since_update >= STALE_DAYS
    num_str  = str(num)

    if meets_s2:
        prev_updated_at = s2_notified.get(num_str)
        if prev_updated_at is None:
            unique_approvers = sorted(set(approved_non_docs))
            new_scenario2.append({
                "number":            num,
                "title":             title,
                "author":            author,
                "author_mention":    slack_mention(author),
                "url":               url,
                "days_since_update": days_since_update,
                "approvers":         unique_approvers,
                "approver_mentions": [slack_mention(a) for a in unique_approvers],
            })
            s2_notified[num_str] = updated_at_str
        elif prev_updated_at != updated_at_str:
            # Updated since last notification — stale clock reset, re-notify
            unique_approvers = sorted(set(approved_non_docs))
            new_scenario2.append({
                "number":            num,
                "title":             title,
                "author":            author,
                "author_mention":    slack_mention(author),
                "url":               url,
                "days_since_update": days_since_update,
                "approvers":         unique_approvers,
                "approver_mentions": [slack_mention(a) for a in unique_approvers],
            })
            s2_notified[num_str] = updated_at_str
    else:
        if num_str in s2_notified:
            prev_updated_at = s2_notified[num_str]
            if prev_updated_at != updated_at_str or not approved_non_docs or days_since_update < STALE_DAYS:
                resolved_scenario2.append({
                    "number":    num,
                    "title":     title,
                    "url":       url,
                    "thread_ts": thread_ts.get(f"s2_{num}"),
                })
                del s2_notified[num_str]
                thread_ts.pop(f"s2_{num}", None)

# ── Clean up state for closed PRs ─────────────────────────────────────────────

# Emit resolved entries for any PRs in state that are now closed
for num in list(s1_notified):
    if num not in open_pr_numbers:
        resolved_scenario1.append({
            "number":    num,
            "title":     f"PR #{num} (closed)",
            "url":       f"https://github.com/{REPO}/pull/{num}",
            "thread_ts": thread_ts.get(f"s1_{num}"),
        })
        s1_notified.discard(num)
        thread_ts.pop(f"s1_{num}", None)

for num_str in list(s2_notified):
    num = int(num_str)
    if num not in open_pr_numbers:
        resolved_scenario2.append({
            "number":    num,
            "title":     f"PR #{num} (closed/merged)",
            "url":       f"https://github.com/{REPO}/pull/{num}",
            "thread_ts": thread_ts.get(f"s2_{num}"),
        })
        del s2_notified[num_str]
        thread_ts.pop(f"s2_{num}", None)

# ── Persist state ──────────────────────────────────────────────────────────────

state["scenario1_notified"] = sorted(s1_notified)
state["scenario2_notified"] = s2_notified
state["thread_ts"]           = thread_ts
save_state(state)

# ── Output ─────────────────────────────────────────────────────────────────────

output = {
    "new_scenario1":      new_scenario1,
    "new_scenario2":      new_scenario2,
    "resolved_scenario1": resolved_scenario1,
    "resolved_scenario2": resolved_scenario2,
    "total_open_prs":     len(all_prs),
    "checked_at":         now.isoformat(),
    "repo":               REPO,
    "stale_days":         STALE_DAYS,
}
if team_fetch_error:
    output["warning"] = team_fetch_error

print(json.dumps(output, indent=2))
