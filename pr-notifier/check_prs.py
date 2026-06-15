#!/usr/bin/env python3
"""
PR Triage Notifier for Braze Docs
Checks open PRs for:
  Scenario 1: Missing "In Review" label OR no stakeholder reviewers tagged
  Scenario 2: Approved by non-docs-team member but no updates in stale_days+
"""

import json
import sys
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.json")
STATE_PATH = os.path.join(SCRIPT_DIR, "state.json")

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

def get_pr_requested_reviewers(repo, pr_number, token):
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/requested_reviewers"
    try:
        return gh_request(url, token)
    except Exception:
        return {"users": [], "teams": []}

def main():
    # Handle save-thread subcommand
    if len(sys.argv) >= 5 and sys.argv[1] == "save-thread":
        scenario = sys.argv[2]  # s1 or s2
        pr_number = int(sys.argv[3])
        thread_ts = sys.argv[4]
        state = load_json(STATE_PATH)
        if "thread_ts" not in state:
            state["thread_ts"] = {}
        key = f"{scenario}_{pr_number}"
        state["thread_ts"][key] = thread_ts
        save_json(STATE_PATH, state)
        print(f"Saved thread_ts for {key}: {thread_ts}")
        return

    try:
        config = load_json(CONFIG_PATH)
    except Exception as e:
        print(json.dumps({"error": f"Could not load config.json: {e}"}))
        return

    token = config.get("github_token", "")
    repo = config.get("repo", "")
    stale_days = config.get("stale_days", 7)
    github_to_slack = config.get("github_to_slack", {})
    extra_docs = set(m.lower() for m in config.get("extra_docs_team_members", [])
                     if not m.startswith("_"))
    slack_token = config.get("slack_bot_token", "")
    slack_channel = config.get("slack_channel", "")
    oncall_docs_mention = config.get("oncall_docs_mention", "<!subteam^S096J5PE2TB|oncall-docs>")
    ignored_reviewers = {r.lower() for r in config.get("ignored_reviewers", [])}

    if not token or not repo:
        print(json.dumps({"error": "Missing github_token or repo in config.json"}))
        return

    # Load state
    try:
        state = load_json(STATE_PATH)
    except Exception:
        state = {}

    scenario1_notified = set(state.get("scenario1_notified", []))
    scenario2_notified = state.get("scenario2_notified", {})
    scenario2_last_reminded = state.get("scenario2_last_reminded", {})
    scenario3_notified = set(state.get("scenario3_notified", []))
    scenario4_notified = set(state.get("scenario4_notified", []))
    thread_ts_map = state.get("thread_ts", {})

    # Get docs team members
    docs_team = get_docs_team_members(token)
    docs_team.update(extra_docs)
    # Add known docs team from github_to_slack keys
    docs_team.update(k.lower() for k in github_to_slack.keys())

    warning = None

    # Fetch open PRs
    try:
        url = f"https://api.github.com/repos/{repo}/pulls?state=open"
        prs = gh_paginate(url, token)
    except urllib.error.HTTPError as e:
        print(json.dumps({"error": f"GitHub API error fetching PRs: {e}"}))
        return
    except Exception as e:
        print(json.dumps({"error": f"Failed to fetch PRs: {e}"}))
        return

    total_open_prs = len(prs)

    new_scenario1 = []
    new_scenario2 = []
    new_scenario2_reminders = []
    new_scenario3 = []
    new_scenario4 = []
    resolved_scenario1 = []
    resolved_scenario2 = []
    resolved_scenario3 = []
    resolved_scenario4 = []

    current_s1_prs = set()
    current_s2_prs = set()
    current_s3_prs = set()
    current_s4_prs = set()

    for pr in prs:
        pr_number = pr["number"]
        pr_title = pr["title"]
        pr_url = pr["html_url"]
        author = pr["user"]["login"]
        author_lower = author.lower()
        created_at = pr.get("created_at", "")
        updated_at = pr.get("updated_at", "")
        labels = [l["name"] for l in pr.get("labels", [])]
        open_days = days_since(created_at)

        # Slack mention for author
        # If the author is a service account, fall back to the PR assignee
        svc_accounts = {"brazedocs-svc"}
        if author_lower in svc_accounts:
            assignees = pr.get("assignees", [])
            docs_assignee = next(
                (a for a in assignees if a["login"].lower() in docs_team),
                None
            )
            if docs_assignee:
                assignee_login = docs_assignee["login"].lower()
                assignee_slack = github_to_slack.get(assignee_login) or github_to_slack.get(docs_assignee["login"])
                if assignee_slack and assignee_slack.startswith("U"):
                    author_mention = f"<@{assignee_slack}>"
                elif assignee_slack:
                    author_mention = f"@{assignee_slack}"
                else:
                    author_mention = oncall_docs_mention
            else:
                # No docs team assignee — fall back to oncall-docs
                author_mention = oncall_docs_mention
        else:
            # If the author is a docs team member and there's a different docs team assignee,
            # tag the assignee instead (they're the responsible owner)
            assignees = pr.get("assignees", [])
            docs_assignee = next(
                (a for a in assignees
                 if a["login"].lower() in docs_team
                 and a["login"].lower() != author_lower),
                None
            )
            mention_login = docs_assignee["login"] if docs_assignee else author
            mention_login_lower = mention_login.lower()
            slack_id = github_to_slack.get(mention_login_lower) or github_to_slack.get(mention_login)
            if slack_id and slack_id.startswith("U"):
                author_mention = f"<@{slack_id}>"
            elif slack_id:
                author_mention = f"@{slack_id}"
            else:
                author_mention = f"@{mention_login}"

        # Get reviews and requested reviewers
        reviews = get_pr_reviews(repo, pr_number, token)
        requested_reviewers = get_pr_requested_reviewers(repo, pr_number, token)

        # --- Scenario 1: No docs-team reviewer, non-docs approval 24h+ ago, not "do not merge" ---

        requested_team_slugs = {t["slug"].lower() for t in requested_reviewers.get("teams", [])}
        requested_user_logins = {u["login"].lower() for u in requested_reviewers.get("users", [])}
        docs_team_individuals = {k.lower() for k in github_to_slack.keys()
                                 if not k.startswith("_")}

        # Also include people who have already submitted a review — GitHub removes them
        # from requested_reviewers once they've reviewed, so we need to check both lists.
        reviewed_logins   = {r["user"]["login"].lower() for r in reviews
                             if r.get("user") and r["state"] != "DISMISSED"}

        team_tagged       = "docs-team" in requested_team_slugs
        individual_tagged = bool(docs_team_individuals & (requested_user_logins | reviewed_logins))
        no_docs_reviewer  = not team_tagged and not individual_tagged

        # Age checks used across scenarios
        created_dt     = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        pr_age         = datetime.now(timezone.utc) - created_dt
        older_than_24h = pr_age >= timedelta(hours=24)

        # PR does not have a "do not merge" label (case-insensitive)
        has_do_not_merge = any(l.lower() == "do not merge" for l in labels)

        # A non-docs-team human member approved the PR 24+ hours ago
        # Excludes bots (e.g. Copilot) and ignored_reviewers from config
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
            current_s1_prs.add(pr_number)

            if pr_number not in scenario1_notified:
                new_scenario1.append({
                    "pr_number": pr_number,
                    "title": pr_title,
                    "url": pr_url,
                    "author": author,
                    "author_mention": author_mention,
                    "open_days": open_days,
                    "reason": "no docs-team reviewer tagged",
                })

        # --- Scenario 2: Approved by non-docs-team, no updates in stale_days ---
        approvals = [r for r in reviews
                     if r["state"] == "APPROVED"
                     and r.get("user")
                     and r["user"].get("type", "User") != "Bot"
                     and r["user"]["login"].lower() not in docs_team
                     and r["user"]["login"].lower() not in ignored_reviewers]

        stale = days_since(updated_at) >= stale_days

        if approvals and stale and not has_do_not_merge:
            current_s2_prs.add(pr_number)
            pr_num_str = str(pr_number)

            approver_mentions = []
            for appr in approvals:
                approver_login = appr["user"]["login"].lower()
                appr_slack = github_to_slack.get(approver_login) or github_to_slack.get(appr["user"]["login"])
                if appr_slack and appr_slack.startswith("U"):
                    approver_mentions.append(f"<@{appr_slack}>")
                elif appr_slack:
                    approver_mentions.append(f"@{appr_slack}")
                else:
                    approver_mentions.append(f"@{appr['user']['login']}")

            assignees = pr.get("assignees", [])
            assignee_is_docs = any(
                a["login"].lower() in docs_team for a in assignees
            )

            pr_data = {
                "pr_number": pr_number,
                "title": pr_title,
                "url": pr_url,
                "author": author,
                "author_mention": author_mention,
                "open_days": open_days,
                "stale_days": days_since(updated_at),
                "approver_mentions": approver_mentions,
                "assignee_is_docs": assignee_is_docs,
            }

            if pr_num_str not in scenario2_notified:
                # First notification
                new_scenario2.append(pr_data)
            else:
                # Already notified — check if 2 days have passed since last reminder
                last_reminded_str = scenario2_last_reminded.get(pr_num_str) or scenario2_notified.get(pr_num_str)
                if last_reminded_str:
                    last_reminded_dt = datetime.fromisoformat(last_reminded_str)
                    if (datetime.now(timezone.utc) - last_reminded_dt) >= timedelta(days=2):
                        new_scenario2_reminders.append(pr_data)

        # --- Scenario 3: External PR with no docs-team reviewer after 24h ---
        author_is_external = author_lower not in docs_team

        if author_is_external and older_than_24h and no_docs_reviewer:
            current_s3_prs.add(pr_number)
            if pr_number not in scenario3_notified:
                new_scenario3.append({
                    "pr_number": pr_number,
                    "title": pr_title,
                    "url": pr_url,
                    "author": author,
                    "author_mention": author_mention,
                    "open_days": open_days,
                })

        # --- Scenario 4: docs-team tagged, no other human reviewers, no approval after 24h ---
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

        if docs_team_is_requested and no_other_human_reviewers and no_human_approvals and older_than_24h and not has_do_not_merge:
            current_s4_prs.add(pr_number)
            if pr_number not in scenario4_notified:
                new_scenario4.append({
                    "pr_number": pr_number,
                    "title": pr_title,
                    "url": pr_url,
                    "author": author,
                    "author_mention": author_mention,
                    "open_days": open_days,
                })

    # Check for resolved scenarios
    for pr_number in list(scenario1_notified):
        if pr_number not in current_s1_prs:
            resolved_scenario1.append({"pr_number": pr_number, "thread_ts": thread_ts_map.get(f"s1_{pr_number}")})

    for pr_num_str in list(scenario2_notified.keys()):
        pr_number = int(pr_num_str)
        if pr_number not in current_s2_prs:
            resolved_scenario2.append({"pr_number": pr_number, "thread_ts": thread_ts_map.get(f"s2_{pr_number}")})

    for pr_number in list(scenario3_notified):
        if pr_number not in current_s3_prs:
            resolved_scenario3.append({"pr_number": pr_number, "thread_ts": thread_ts_map.get(f"s3_{pr_number}")})

    for pr_number in list(scenario4_notified):
        if pr_number not in current_s4_prs:
            resolved_scenario4.append({"pr_number": pr_number, "thread_ts": thread_ts_map.get(f"s4_{pr_number}")})

    # Remove resolved PRs from state
    new_s1_set = scenario1_notified.copy()
    for r in resolved_scenario1:
        new_s1_set.discard(r["pr_number"])

    new_s2_dict = scenario2_notified.copy()
    for r in resolved_scenario2:
        new_s2_dict.pop(str(r["pr_number"]), None)

    new_s3_set = scenario3_notified.copy()
    for r in resolved_scenario3:
        new_s3_set.discard(r["pr_number"])

    new_s4_set = scenario4_notified.copy()
    for r in resolved_scenario4:
        new_s4_set.discard(r["pr_number"])

    warning_footer = f"\n_⚠️ Note: {warning}_" if warning else ""

    # --- Post resolved reactions ---
    for r in resolved_scenario1 + resolved_scenario2 + resolved_scenario3 + resolved_scenario4:
        ts = r.get("thread_ts")
        if ts and slack_token and slack_channel:
            slack_react(slack_token, slack_channel, ts)

    # --- Post new Scenario 1 alerts ---
    for pr in new_scenario1:
        text = (
            f"🔴 *Action needed: PR missing reviewer*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Open {pr['open_days']} days  |  {pr['reason']}"
            f"{warning_footer}"
        )
        if slack_token and slack_channel:
            ts = slack_post(slack_token, slack_channel, text)
            if ts:
                new_s1_set.add(pr["pr_number"])
                thread_ts_map[f"s1_{pr['pr_number']}"] = ts
        else:
            print(text)

    # --- Post new Scenario 2 alerts ---
    for pr in new_scenario2:
        approvers = ", ".join(pr["approver_mentions"]) if pr["approver_mentions"] else "unknown"
        oncall_tag = f"\n{oncall_docs_mention} please follow up on this PR." if not pr["assignee_is_docs"] else ""
        text = (
            f"⏰ *Action needed: Approved PR has gone stale*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Approved by: {approvers}  |  No updates for {pr['stale_days']} days"
            f"{oncall_tag}"
            f"{warning_footer}"
        )
        if slack_token and slack_channel:
            ts = slack_post(slack_token, slack_channel, text)
            if ts:
                now_iso = datetime.now(timezone.utc).isoformat()
                new_s2_dict[str(pr["pr_number"])] = now_iso
                scenario2_last_reminded[str(pr["pr_number"])] = now_iso
                thread_ts_map[f"s2_{pr['pr_number']}"] = ts
        else:
            print(text)

    # --- Post Scenario 2 follow-up reminders (every 2 days after initial) ---
    for pr in new_scenario2_reminders:
        approvers = ", ".join(pr["approver_mentions"]) if pr["approver_mentions"] else "unknown"
        oncall_tag = f"\n{oncall_docs_mention} please follow up on this PR." if not pr["assignee_is_docs"] else ""
        text = (
            f"⏰ *Reminder: Approved PR still waiting*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Approved by: {approvers}  |  No updates for {pr['stale_days']} days"
            f"{oncall_tag}"
            f"{warning_footer}"
        )
        if slack_token and slack_channel:
            ts = slack_post(slack_token, slack_channel, text)
            if ts:
                scenario2_last_reminded[str(pr["pr_number"])] = datetime.now(timezone.utc).isoformat()
                thread_ts_map[f"s2_{pr['pr_number']}"] = ts
        else:
            print(text)

    # --- Post new Scenario 3 alerts ---
    for pr in new_scenario3:
        text = (
            f"👋 *External PR needs a docs team owner*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Opened by: {pr['author_mention']}  |  Open {pr['open_days']} days\n"
            f"{oncall_docs_mention} please assign this PR to the appropriate docs team owner."
            f"{warning_footer}"
        )
        if slack_token and slack_channel:
            ts = slack_post(slack_token, slack_channel, text)
            if ts:
                new_s3_set.add(pr["pr_number"])
                thread_ts_map[f"s3_{pr['pr_number']}"] = ts
        else:
            print(text)

    # --- Post new Scenario 4 alerts ---
    for pr in new_scenario4:
        text = (
            f"🔔 *Docs-team PR ready for review*\n"
            f"<{pr['url']}|#{pr['pr_number']}: {pr['title']}>\n"
            f"Owner: {pr['author_mention']}  |  Open {pr['open_days']} days\n"
            f"{oncall_docs_mention} this PR is waiting on a docs-team review — please take a look, leave feedback, or approve and merge."
            f"{warning_footer}"
        )
        if slack_token and slack_channel:
            ts = slack_post(slack_token, slack_channel, text)
            if ts:
                new_s4_set.add(pr["pr_number"])
                thread_ts_map[f"s4_{pr['pr_number']}"] = ts
        else:
            print(text)

    # Save final state
    state["scenario1_notified"] = sorted(new_s1_set)
    state["scenario2_notified"] = new_s2_dict
    state["scenario2_last_reminded"] = scenario2_last_reminded
    state["scenario3_notified"] = sorted(new_s3_set)
    state["scenario4_notified"] = sorted(new_s4_set)
    state["thread_ts"] = thread_ts_map
    save_json(STATE_PATH, state)

    output = {
        "new_scenario1": new_scenario1,
        "new_scenario2": new_scenario2,
        "new_scenario2_reminders": new_scenario2_reminders,
        "new_scenario3": new_scenario3,
        "new_scenario4": new_scenario4,
        "resolved_scenario1": resolved_scenario1,
        "resolved_scenario2": resolved_scenario2,
        "resolved_scenario3": resolved_scenario3,
        "resolved_scenario4": resolved_scenario4,
        "total_open_prs": total_open_prs,
    }
    if warning:
        output["warning"] = warning

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
