#!/usr/bin/env python3
"""
PR Triage Notifier for Braze Docs
Scenarios:
  1: Non-docs-team member approved 24h+ ago, no docs reviewer, no "do not merge"
  2: Approved by non-docs-team, no activity for 5+ days, no "do not merge"
  3: External PR author, no docs reviewer, older than 24h
  4: Docs-team tagged as reviewer, no other reviewers, no approval, older than 24h
  5: Any PR with no activity for 20+ days — fires once as a final catch-all
  6: Docs-team tagged + non-docs approval exists + no docs-team review yet, 24h+ since tagged

Scenarios 1–4 and 6 fire once, then remind every 2 days up to 5 reminders.
Scenario 5 fires once only.
"""

import json
import sys
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")
STATE_PATH  = os.path.join(SCRIPT_DIR, "state.json")

REMINDER_INTERVAL_DAYS = 2
MAX_REMINDERS          = 5


def load_json(path):
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def slack_react(token, channel, timestamp, emoji="white_check_mark"):
    """Add an emoji reaction to a Slack message."""
    payload = {"channel": channel, "timestamp": timestamp, "name": emoji}
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://slack.com/api/reactions.add",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            if not result.get("ok"):
                print(f"[slack] React error: {result.get('error')}", file=sys.stderr)
    except Exception as e:
        print(f"[slack] React failed: {e}", file=sys.stderr)

def slack_post(token, channel, text, thread_ts=None):
    """Post a message to Slack. Returns the message ts, or None on failure."""
    payload = {"channel": channel, "text": text, "mrkdwn": True}
    if thread_ts:
        payload["thread_ts"] = thread_ts
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            if result.get("ok"):
                return result.get("ts")
            else:
                print(f"[slack] Error: {result.get('error')}", file=sys.stderr)
                return None
    except Exception as e:
        print(f"[slack] Request failed: {e}", file=sys.stderr)
        return None

def gh_request(url, token):
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "braze-docs-pr-notifier")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def gh_paginate(url, token):
    results = []
    page = 1
    while True:
        sep = "&" if "?" in url else "?"
        data = gh_request(f"{url}{sep}per_page=100&page={page}", token)
        if not data:
            break
        results.extend(data)
        if len(data) < 100:
            break
        page += 1
    return results

def get_docs_team_members(token, org="braze-inc", team_slug="docs-team"):
    try:
        url = f"https://api.github.com/orgs/{org}/teams/{team_slug}/members"
        members = gh_paginate(url, token)
        return {m["login"].lower() for m in members}
    except Exception:
        return set()

def days_since(dt_str):
    if not dt_str:
        return 0
    dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - dt).days

def get_pr_reviews(repo, pr_number, token):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/reviews"
    try:
        return gh_paginate(url, token)
    except Exception:
        return []

def get_docs_team_tagged_time(repo, pr_number, token):
    """Return the most recent datetime docs-team was requested as a reviewer, or None."""
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/timeline"
    try:
        events = gh_paginate(url, token)
        last_request = None
        for event in events:
            if event.get("event") == "review_requested":
                team = event.get("requested_team")
                if team and team.get("slug", "").lower() == "docs-team":
                    ts = event.get("created_at")
                    if ts:
                        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                        if last_request is None or dt > last_request:
                            last_request = dt
        return last_request
    except Exception:
        return None

def get_pr_requested_reviewers(repo, pr_number, token):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/requested_reviewers"
    try:
        return gh_request(url, token)
    except Exception:
        return {"users": [], "teams": []}

def should_remind(last_reminded_str, reminder_count):
    """Return True if 2 days have passed since last reminder and cap not reached."""
    if reminder_count >= MAX_REMINDERS:
        return False
    if not last_reminded_str:
        return False
    last_dt = datetime.fromisoformat(last_reminded_str)
    return (datetime.now(timezone.utc) - last_dt) >= timedelta(days=REMINDER_INTERVAL_DAYS)

def resolve_mention(login, github_to_slack, oncall_docs_mention):
    """Convert a GitHub login to a Slack mention string."""
    slack_id = github_to_slack.get(login.lower()) or github_to_slack.get(login)
    if slack_id and slack_id.startswith("U"):
        return f"<@{slack_id}>"
    elif slack_id:
        return f"@{slack_id}"
    else:
        return oncall_docs_mention

def build_author_mention(author, author_lower, pr, docs_team, github_to_slack,
                         oncall_docs_mention, svc_accounts):
    """
    Determine the best Slack mention for a PR's responsible owner.
    Priority:
      1. Service account → use docs-team assignee if present, else oncall-docs
      2. Docs team author with a different docs-team assignee → use assignee
      3. Everyone else → use author
    """
    assignees = pr.get("assignees", [])

    if author_lower in svc_accounts:
        docs_assignee = next(
            (a for a in assignees if a["login"].lower() in docs_team), None
        )
        if docs_assignee:
            return resolve_mention(docs_assignee["login"], github_to_slack, oncall_docs_mention)
        return oncall_docs_mention

    # If author is docs team and there's a different docs-team assignee, prefer assignee
    docs_assignee = next(
        (a for a in assignees
         if a["login"].lower() in docs_team and a["login"].lower() != author_lower),
        None
    )
    if docs_assignee:
        return resolve_mention(docs_assignee["login"], github_to_slack, oncall_docs_mention)

    return resolve_mention(author, github_to_slack, oncall_docs_mention)


def main():
    # Handle save-thread subcommand
    if len(sys.argv) >= 5 and sys.argv[1] == "save-thread":
        scenario   = sys.argv[2]
        pr_number  = int(sys.argv[3])
        thread_ts  = sys.argv[4]
        state = load_json(STATE_PATH)
        state.setdefault("thread_ts", {})[f"{scenario}_{pr_number}"] = thread_ts
        save_json(STATE_PATH, state)
        print(f"Saved thread_ts for {scenario}_{pr_number}: {thread_ts}")
        return

    try:
        config = load_json(CONFIG_PATH)
    except Exception as e:
        print(json.dumps({"error": f"Could not load config.json: {e}"}))
        return

    token              = config.get("github_token", "")
    repo               = config.get("repo", "")
    stale_days         = config.get("stale_days", 5)
    github_to_slack    = config.get("github_to_slack", {})
    extra_docs         = set(m.lower() for m in config.get("extra_docs_team_members", [])
                             if not m.startswith("_"))
    slack_token        = config.get("slack_bot_token", "")
    slack_channel      = config.get("slack_channel", "")
    oncall_docs_mention = config.get("oncall_docs_mention", "<!subteam^S096J5PE2TB|oncall-docs>")
    ignored_reviewers  = {r.lower() for r in config.get("ignored_reviewers", [])}
    svc_accounts       = {"brazedocs-svc"}

    if not token or not repo:
        print(json.dumps({"error": "Missing github_token or repo in config.json"}))
        return

    # ── Load state ──────────────────────────────────────────────────────────────
    try:
        state = load_json(STATE_PATH)
    except Exception:
        state = {}

    scenario1_notified      = set(state.get("scenario1_notified", []))
    scenario1_last_reminded = state.get("scenario1_last_reminded", {})
    scenario1_reminder_count = state.get("scenario1_reminder_count", {})

    scenario2_notified      = state.get("scenario2_notified", {})
    scenario2_last_reminded = state.get("scenario2_last_reminded", {})
    scenario2_reminder_count = state.get("scenario2_reminder_count", {})

    scenario3_notified      = set(state.get("scenario3_notified", []))
    scenario3_last_reminded = state.get("scenario3_last_reminded", {})
    scenario3_reminder_count = state.get("scenario3_reminder_count", {})

    scenario4_notified      = set(state.get("scenario4_notified", []))
    scenario4_last_reminded = state.get("scenario4_last_reminded", {})
    scenario4_reminder_count = state.get("scenario4_reminder_count", {})

    scenario5_notified = set(state.get("scenario5_notified", []))

    scenario6_notified       = set(state.get("scenario6_notified", []))
    scenario6_last_reminded  = state.get("scenario6_last_reminded", {})
    scenario6_reminder_count = state.get("scenario6_reminder_count", {})

    thread_ts_map = state.get("thread_ts", {})

    # ── Build docs team set ──────────────────────────────────────────────────────
    docs_team = get_docs_team_members(token)
    docs_team.update(extra_docs)
    docs_team.update(k.lower() for k in github_to_slack.keys() if not k.startswith("_"))

    warning = None

    # ── Fetch open PRs ───────────────────────────────────────────────────────────
    try:
        prs = gh_paginate(f"https://api.github.com/repos/{repo}/pulls?state=open", token)
    except urllib.error.HTTPError as e:
        print(json.dumps({"error": f"GitHub API error: {e}"}))
        return
    except Exception as e:
        print(json.dumps({"error": f"Failed to fetch PRs: {e}"}))
        return

    total_open_prs = len(prs)

    # New notifications and reminders
    new_s1 = []; remind_s1 = []
    new_s2 = []; remind_s2 = []
    new_s3 = []; remind_s3 = []
    new_s4 = []; remind_s4 = []
    new_s5 = []
    new_s6 = []; remind_s6 = []

    # Resolved notifications
    resolved_s1 = []; resolved_s2 = []; resolved_s3 = []; resolved_s4 = []; resolved_s5 = []; resolved_s6 = []

    # Currently active PRs per scenario
    current_s1 = set(); current_s2 = set(); current_s3 = set(); current_s4 = set(); current_s5 = set(); current_s6 = set()

    for pr in prs:
        pr_number  = pr["number"]
        pr_title   = pr["title"]
        pr_url     = pr["html_url"]
        author     = pr["user"]["login"]
        author_lower = author.lower()
        created_at = pr.get("created_at", "")
        updated_at = pr.get("updated_at", "")
        labels     = [l["name"] for l in pr.get("labels", [])]
        open_days  = days_since(created_at)
        pr_num_str = str(pr_number)

        author_mention = build_author_mention(
            author, author_lower, pr, docs_team, github_to_slack,
            oncall_docs_mention, svc_accounts
        )

        reviews             = get_pr_reviews(repo, pr_number, token)
        requested_reviewers = get_pr_requested_reviewers(repo, pr_number, token)

        requested_team_slugs  = {t["slug"].lower() for t in requested_reviewers.get("teams", [])}
        requested_user_logins = {u["login"].lower() for u in requested_reviewers.get("users", [])}
        docs_team_individuals = {k.lower() for k in github_to_slack.keys() if not k.startswith("_")}
        reviewed_logins       = {r["user"]["login"].lower() for r in reviews
                                  if r.get("user") and r["state"] != "DISMISSED"}

        team_tagged      = "docs-team" in requested_team_slugs
        individual_tagged = bool(docs_team_individuals & (requested_user_logins | reviewed_logins))
        no_docs_reviewer = not team_tagged and not individual_tagged

        created_dt     = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        pr_age         = datetime.now(timezone.utc) - created_dt
        older_than_24h = pr_age >= timedelta(hours=24)

        has_do_not_merge = any(l.lower() == "do not merge" for l in labels)

        # ── Scenario 1 ────────────────────────────────────────────────────────
        non_docs_approved_24h = any(
            r["state"] == "APPROVED"
            and r.get("user")
            and r["user"].get("type", "User") != "Bot"
            and r["user"]["login"].lower() not in docs_team
            and r["user"]["login"].lower() not in ignored_reviewers
            and (datetime.now(timezone.utc) - datetime.fromisoformat(
                r["submitted_at"].replace("Z", "+00:00"))) >= timedelta(hours=24)
            for r in reviews
        )

        if no_docs_reviewer and not has_do_not_merge and non_docs_approved_24h:
            current_s1.add(pr_number)
            pr_data = {"pr_number": pr_number, "title": pr_title, "url": pr_url,
                       "author_mention": author_mention, "open_days": open_days,
                       "reason": "no docs-team reviewer tagged"}
            if pr_number not in scenario1_notified:
                new_s1.append(pr_data)
            elif should_remind(scenario1_last_reminded.get(pr_num_str),
                               scenario1_reminder_count.get(pr_num_str, 0)):
                remind_s1.append(pr_data)

        # ── Scenario 2 ────────────────────────────────────────────────────────
        approvals = [r for r in reviews
                     if r["state"] == "APPROVED"
                     and r.get("user")
                     and r["user"].get("type", "User") != "Bot"
                     and r["user"]["login"].lower() not in docs_team
                     and r["user"]["login"].lower() not in ignored_reviewers]

        stale = days_since(updated_at) >= stale_days

        if approvals and stale and not has_do_not_merge:
            current_s2.add(pr_number)

            approver_mentions = []
            for appr in approvals:
                appr_login = appr["user"]["login"].lower()
                appr_slack = github_to_slack.get(appr_login) or github_to_slack.get(appr["user"]["login"])
                if appr_slack and appr_slack.startswith("U"):
                    approver_mentions.append(f"<@{appr_slack}>")
                elif appr_slack:
                    approver_mentions.append(f"@{appr_slack}")
                else:
                    approver_mentions.append(f"@{appr['user']['login']}")

            assignees = pr.get("assignees", [])
            assignee_is_docs = any(a["login"].lower() in docs_team for a in assignees)

            pr_data = {"pr_number": pr_number, "title": pr_title, "url": pr_url,
                       "author_mention": author_mention, "open_days": open_days,
                       "stale_days": days_since(updated_at),
                       "approver_mentions": approver_mentions,
                       "assignee_is_docs": assignee_is_docs}

            if pr_num_str not in scenario2_notified:
                new_s2.append(pr_data)
            elif should_remind(scenario2_last_reminded.get(pr_num_str) or scenario2_notified.get(pr_num_str),
                               scenario2_reminder_count.get(pr_num_str, 0)):
                remind_s2.append(pr_data)

        # ── Scenario 3 ────────────────────────────────────────────────────────
        author_is_external = author_lower not in docs_team

        # Also consider a docs-team assignee as "covered" — not just reviewers
        assignees = pr.get("assignees", [])
        docs_team_assigned = any(a["login"].lower() in docs_team for a in assignees)
        no_docs_owner = no_docs_reviewer and not docs_team_assigned

        if author_is_external and older_than_24h and no_docs_owner:
            current_s3.add(pr_number)
            pr_data = {"pr_number": pr_number, "title": pr_title, "url": pr_url,
                       "author_mention": author_mention, "open_days": open_days}
            if pr_number not in scenario3_notified:
                new_s3.append(pr_data)
            elif should_remind(scenario3_last_reminded.get(pr_num_str),
                               scenario3_reminder_count.get(pr_num_str, 0)):
                remind_s3.append(pr_data)

        # ── Scenario 4 ────────────────────────────────────────────────────────
        docs_team_is_requested = "docs-team" in requested_team_slugs

        other_human_requested = [
            u["login"].lower() for u in requested_reviewers.get("users", [])
            if u.get("type", "User") != "Bot"
            and u["login"].lower() not in docs_team
            and u["login"].lower() not in ignored_reviewers
        ]
        other_human_reviewed = [
            r["user"]["login"].lower() for r in reviews
            if r.get("user")
            and r["user"].get("type", "User") != "Bot"
            and r["user"]["login"].lower() not in docs_team
            and r["user"]["login"].lower() not in ignored_reviewers
            and r["state"] != "DISMISSED"
        ]
        no_other_human_reviewers = not other_human_requested and not other_human_reviewed

        no_human_approvals = not any(
            r["state"] == "APPROVED"
            and r.get("user")
            and r["user"].get("type", "User") != "Bot"
            and r["user"]["login"].lower() not in ignored_reviewers
            for r in reviews
        )

        # Look up when docs-team was tagged (shared by Scenarios 4 and 6)
        docs_team_tagged_dt = None

        if docs_team_is_requested and no_other_human_reviewers and no_human_approvals \
                and not has_do_not_merge:
            docs_team_tagged_dt = get_docs_team_tagged_time(repo, pr_number, token)
            if docs_team_tagged_dt is None:
                # Fall back to PR age if timeline lookup fails
                docs_team_tagged_dt = created_dt
            tagged_age = datetime.now(timezone.utc) - docs_team_tagged_dt
            tagged_days = tagged_age.days
            tagged_24h = tagged_age >= timedelta(hours=24)

            if tagged_24h:
                current_s4.add(pr_number)
                pr_data = {"pr_number": pr_number, "title": pr_title, "url": pr_url,
                           "author_mention": author_mention, "open_days": open_days,
                           "tagged_days": tagged_days}
                if pr_number not in scenario4_notified:
                    new_s4.append(pr_data)
                elif should_remind(scenario4_last_reminded.get(pr_num_str),
                                   scenario4_reminder_count.get(pr_num_str, 0)):
                    remind_s4.append(pr_data)

        # ── Scenario 5 ────────────────────────────────────────────────────────
        # Any PR with no activity for 20+ days — fires once as a final catch-all
        ancient = days_since(updated_at) >= 20

        if ancient and not has_do_not_merge:
            current_s5.add(pr_number)
            if pr_number not in scenario5_notified:
                new_s5.append({
                    "pr_number": pr_number,
                    "title": pr_title,
                    "url": pr_url,
                    "author_mention": author_mention,
                    "open_days": open_days,
                    "stale_days": days_since(updated_at),
                })

        # ── Scenario 6 ────────────────────────────────────────────────────────
        # Docs-team tagged + non-docs approval + no docs-team review yet, 24h+ since tagged
        non_docs_approved = any(
            r["state"] == "APPROVED"
            and r.get("user")
            and r["user"].get("type", "User") != "Bot"
            and r["user"]["login"].lower() not in docs_team
            and r["user"]["login"].lower() not in ignored_reviewers
            for r in reviews
        )
        docs_has_reviewed = bool(docs_team_individuals & reviewed_logins)

        if docs_team_is_requested and non_docs_approved and not docs_has_reviewed and not has_do_not_merge:
            # Use when docs-team was tagged, not PR creation date
            if docs_team_tagged_dt is None:
                docs_team_tagged_dt = get_docs_team_tagged_time(repo, pr_number, token)
            tagged_age_s6 = datetime.now(timezone.utc) - (docs_team_tagged_dt or created_dt)
            tagged_days_s6 = tagged_age_s6.days

            if tagged_age_s6 >= timedelta(hours=24):
                current_s6.add(pr_number)
                pr_data = {"pr_number": pr_number, "title": pr_title, "url": pr_url,
                           "author_mention": author_mention, "open_days": open_days,
                           "tagged_days": tagged_days_s6}
                if pr_number not in scenario6_notified:
                    new_s6.append(pr_data)
                elif should_remind(scenario6_last_reminded.get(pr_num_str),
                                   scenario6_reminder_count.get(pr_num_str, 0)):
                    remind_s6.append(pr_data)

    # ── Find resolved PRs ────────────────────────────────────────────────────────
    for pr_number in list(scenario1_notified):
        if pr_number not in current_s1:
            resolved_s1.append({"pr_number": pr_number,
                                 "thread_ts": thread_ts_map.get(f"s1_{pr_number}")})

    for pr_num_str in list(scenario2_notified.keys()):
        pr_number = int(pr_num_str)
        if pr_number not in current_s2:
            resolved_s2.append({"pr_number": pr_number,
                                 "thread_ts": thread_ts_map.get(f"s2_{pr_number}")})

    for pr_number in list(scenario3_notified):
        if pr_number not in current_s3:
            resolved_s3.append({"pr_number": pr_number,
                                 "thread_ts": thread_ts_map.get(f"s3_{pr_number}")})

    for pr_number in list(scenario4_notified):
        if pr_number not in current_s4:
            resolved_s4.append({"pr_number": pr_number,
                                 "thread_ts": thread_ts_map.get(f"s4_{pr_number}")})

    for pr_number in list(scenario5_notified):
        if pr_number not in current_s5:
            resolved_s5.append({"pr_number": pr_number,
                                 "thread_ts": thread_ts_map.get(f"s5_{pr_number}")})

    for pr_number in list(scenario6_notified):
        if pr_number not in current_s6:
            resolved_s6.append({"pr_number": pr_number,
                                 "thread_ts": thread_ts_map.get(f"s6_{pr_number}")})

    # ── Remove resolved from state ───────────────────────────────────────────────
    new_s1_set  = scenario1_notified.copy()
    new_s2_dict = scenario2_notified.copy()
    new_s3_set  = scenario3_notified.copy()
    new_s4_set  = scenario4_notified.copy()
    new_s5_set  = scenario5_notified.copy()

    for r in resolved_s1:
        n = r["pr_number"]
        new_s1_set.discard(n)
        scenario1_last_reminded.pop(str(n), None)
        scenario1_reminder_count.pop(str(n), None)

    for r in resolved_s2:
        n = r["pr_number"]
        new_s2_dict.pop(str(n), None)
        scenario2_last_reminded.pop(str(n), None)
        scenario2_reminder_count.pop(str(n), None)

    for r in resolved_s3:
        n = r["pr_number"]
        new_s3_set.discard(n)
        scenario3_last_reminded.pop(str(n), None)
        scenario3_reminder_count.pop(str(n), None)

    for r in resolved_s4:
        n = r["pr_number"]
        new_s4_set.discard(n)
        scenario4_last_reminded.pop(str(n), None)
        scenario4_reminder_count.pop(str(n), None)

    for r in resolved_s5:
        new_s5_set.discard(r["pr_number"])

    new_s6_set = scenario6_notified.copy()
    for r in resolved_s6:
        n = r["pr_number"]
        new_s6_set.discard(n)
        scenario6_last_reminded.pop(str(n), None)
        scenario6_reminder_count.pop(str(n), None)

    warning_footer = f"\n_⚠️ Note: {warning}_" if warning else ""

    # ── Post resolved reactions ──────────────────────────────────────────────────
    for r in resolved_s1 + resolved_s2 + resolved_s3 + resolved_s4 + resolved_s5 + resolved_s6:
        ts = r.get("thread_ts")
        if ts and slack_token and slack_channel:
            slack_react(slack_token, slack_channel, ts)

    # ── Helper to post and record ────────────────────────────────────────────────
    def post_and_record(text, pr_number, notified_set=None, notified_dict=None,
                        last_reminded_dict=None, reminder_count_dict=None,
                        scenario_key=None):
        """Post a Slack message and update the relevant state dicts."""
        pr_num_str = str(pr_number)
        if slack_token and slack_channel:
            ts = slack_post(slack_token, slack_channel, text)
            if ts:
                now_iso = datetime.now(timezone.utc).isoformat()
                if notified_set is not None:
                    notified_set.add(pr_number)
                if notified_dict is not None:
                    notified_dict[pr_num_str] = now_iso
                if last_reminded_dict is not None:
                    last_reminded_dict[pr_num_str] = now_iso
                if reminder_count_dict is not None:
                    reminder_count_dict[pr_num_str] = reminder_count_dict.get(pr_num_str, 0) + 1
                if scenario_key:
                    thread_ts_map[f"{scenario_key}_{pr_number}"] = ts
        else:
            print(text)

    # ── Post Scenario 1 ──────────────────────────────────────────────────────────
    for pr in new_s1:
        text = (
            f"🔴 *Action needed: PR missing reviewer*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Open {pr['open_days']} days  |  {pr['reason']}"
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        notified_set=new_s1_set,
                        last_reminded_dict=scenario1_last_reminded,
                        scenario_key="s1")

    for pr in remind_s1:
        text = (
            f"🔴 *Reminder: PR still missing reviewer*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Open {pr['open_days']} days  |  {pr['reason']}"
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        last_reminded_dict=scenario1_last_reminded,
                        reminder_count_dict=scenario1_reminder_count,
                        scenario_key="s1")

    # ── Post Scenario 2 ──────────────────────────────────────────────────────────
    for pr in new_s2:
        approvers  = ", ".join(pr["approver_mentions"]) if pr["approver_mentions"] else "unknown"
        oncall_tag = f"\n{oncall_docs_mention} please follow up on this PR." if not pr["assignee_is_docs"] else ""
        text = (
            f"⏰ *Action needed: Approved PR has gone stale*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Approved by: {approvers}  |  No updates for {pr['stale_days']} days"
            f"{oncall_tag}"
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        notified_dict=new_s2_dict,
                        last_reminded_dict=scenario2_last_reminded,
                        scenario_key="s2")

    for pr in remind_s2:
        approvers  = ", ".join(pr["approver_mentions"]) if pr["approver_mentions"] else "unknown"
        oncall_tag = f"\n{oncall_docs_mention} please follow up on this PR." if not pr["assignee_is_docs"] else ""
        text = (
            f"⏰ *Reminder: Approved PR still waiting*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Approved by: {approvers}  |  No updates for {pr['stale_days']} days"
            f"{oncall_tag}"
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        last_reminded_dict=scenario2_last_reminded,
                        reminder_count_dict=scenario2_reminder_count,
                        scenario_key="s2")

    # ── Post Scenario 3 ──────────────────────────────────────────────────────────
    for pr in new_s3:
        text = (
            f"👋 *External PR needs a docs team owner*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Opened by: {pr['author_mention']}  |  Open {pr['open_days']} days\n"
            f"{oncall_docs_mention} please assign this PR to the appropriate docs team owner."
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        notified_set=new_s3_set,
                        last_reminded_dict=scenario3_last_reminded,
                        scenario_key="s3")

    for pr in remind_s3:
        text = (
            f"👋 *Reminder: External PR still needs an owner*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Opened by: {pr['author_mention']}  |  Open {pr['open_days']} days\n"
            f"{oncall_docs_mention} please assign this PR to the appropriate docs team owner."
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        last_reminded_dict=scenario3_last_reminded,
                        reminder_count_dict=scenario3_reminder_count,
                        scenario_key="s3")

    # ── Post Scenario 4 ──────────────────────────────────────────────────────────
    for pr in new_s4:
        text = (
            f"🔔 *Docs-team PR ready for review*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Tagged for review {pr['tagged_days']} days ago\n"
            f"{oncall_docs_mention} this PR is waiting on a docs-team review — please take a look, leave feedback, or approve and merge."
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        notified_set=new_s4_set,
                        last_reminded_dict=scenario4_last_reminded,
                        scenario_key="s4")

    for pr in remind_s4:
        text = (
            f"🔔 *Reminder: Docs-team PR still waiting for review*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Tagged for review {pr['tagged_days']} days ago\n"
            f"{oncall_docs_mention} this PR is still waiting on a docs-team review."
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        last_reminded_dict=scenario4_last_reminded,
                        reminder_count_dict=scenario4_reminder_count,
                        scenario_key="s4")

    # ── Post Scenario 5 ──────────────────────────────────────────────────────────
    for pr in new_s5:
        text = (
            f"😬 *Wowza, this PR hasn't been touched in {pr['stale_days']} days*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Open {pr['open_days']} days\n"
            f"Is this still relevant? Time to merge, close, or give it some love."
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        notified_set=new_s5_set,
                        scenario_key="s5")

    # ── Post Scenario 6 ──────────────────────────────────────────────────────────
    for pr in new_s6:
        text = (
            f"🔔 *Docs-team review needed: PR has stakeholder approval*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Tagged for review {pr['tagged_days']} days ago\n"
            f"{oncall_docs_mention} this PR has been approved by stakeholders and is waiting on a docs-team review."
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        notified_set=new_s6_set,
                        last_reminded_dict=scenario6_last_reminded,
                        scenario_key="s6")

    for pr in remind_s6:
        text = (
            f"🔔 *Reminder: Docs-team review still needed*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Tagged for review {pr['tagged_days']} days ago\n"
            f"{oncall_docs_mention} this PR still needs a docs-team review — stakeholders have already approved."
            f"{warning_footer}"
        )
        post_and_record(text, pr["pr_number"],
                        last_reminded_dict=scenario6_last_reminded,
                        reminder_count_dict=scenario6_reminder_count,
                        scenario_key="s6")

    # ── Save state ───────────────────────────────────────────────────────────────
    state["scenario1_notified"]       = sorted(new_s1_set)
    state["scenario1_last_reminded"]  = scenario1_last_reminded
    state["scenario1_reminder_count"] = scenario1_reminder_count

    state["scenario2_notified"]       = new_s2_dict
    state["scenario2_last_reminded"]  = scenario2_last_reminded
    state["scenario2_reminder_count"] = scenario2_reminder_count

    state["scenario3_notified"]       = sorted(new_s3_set)
    state["scenario3_last_reminded"]  = scenario3_last_reminded
    state["scenario3_reminder_count"] = scenario3_reminder_count

    state["scenario4_notified"]       = sorted(new_s4_set)
    state["scenario4_last_reminded"]  = scenario4_last_reminded
    state["scenario4_reminder_count"] = scenario4_reminder_count

    state["scenario5_notified"] = sorted(new_s5_set)

    state["scenario6_notified"]       = sorted(new_s6_set)
    state["scenario6_last_reminded"]  = scenario6_last_reminded
    state["scenario6_reminder_count"] = scenario6_reminder_count

    state["thread_ts"] = thread_ts_map
    save_json(STATE_PATH, state)

    output = {
        "new_scenario1": new_s1, "reminders_scenario1": remind_s1,
        "new_scenario2": new_s2, "reminders_scenario2": remind_s2,
        "new_scenario3": new_s3, "reminders_scenario3": remind_s3,
        "new_scenario4": new_s4, "reminders_scenario4": remind_s4,
        "new_scenario5": new_s5,
        "new_scenario6": new_s6, "reminders_scenario6": remind_s6,
        "resolved_scenario1": resolved_s1,
        "resolved_scenario2": resolved_s2,
        "resolved_scenario3": resolved_s3,
        "resolved_scenario4": resolved_s4,
        "resolved_scenario5": resolved_s5,
        "resolved_scenario6": resolved_s6,
        "total_open_prs": total_open_prs,
    }
    if warning:
        output["warning"] = warning

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
