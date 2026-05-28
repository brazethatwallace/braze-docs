#!/usr/bin/env python3
"""Phase 2: one branch/PR per Salesforce KB article_id. Run from repo root."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

ARTICLES: list[tuple[str, str, str]] = [
    # (article_id, short_title_for_pr, relative_path from repo root)
    ("ka0VP0000001IkTYAU", "API segment export incremental S3 Azure", "_docs/_user_guide/data/distribution/export_braze_data/export_troubleshooting.md"),
    ("ka03o000001N9RKAA0", "Canvas branching distribution within a variant", "_docs/_user_guide/messaging/canvas/create_a_canvas.md"),
    ("ka0VP00000017STYAY", "Exclude users in active Canvas from campaigns", "_docs/_user_guide/messaging/canvas/faqs.md"),
    ("ka0VP0000001y6zYAA", "Currents timely session end events", "_docs/_user_guide/data/distribution/braze_currents/faq.md"),
    ("ka0VP0000001yBpYAI", "Intelligent Selection re-eligibility Canvas vs campaigns", "_docs/_user_guide/brazeai/intelligence_suite/intelligent_selection.md"),
    ("ka0VP0000003WUnYAM", "Quiet hours segment membership evaluation", "_docs/_user_guide/messaging/messaging_fundamentals/quiet_hours.md"),
    ("ka0VP0000004WSjYAM", "Canvas error Too Many Canvas Branches", "_docs/_user_guide/messaging/canvas/troubleshooting.md"),
    ("ka0VP0000006vq1YAA", "Unity AndroidX gradleTemplate.properties", "_includes/developer_guide/unity/sdk_integration.md"),
    ("ka0VP0000008kk1YAA", "Liquid European currency formatting", "_docs/_user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases.md"),
    ("ka0VP0000002QsrYAE", "Home dashboard New Users stat retroactive decrease", "_docs/_user_guide/analytics/dashboards/home.md"),
    ("ka0VP0000002S0DYAU", "Report Builder unique recipients vs impressions", "_docs/_user_guide/analytics/reports/report_builder.md"),
    ("ka0VP0000007EnpYAE", "Gmail Unsubscribe vs list-unsubscribe header", "_docs/_user_guide/administer/global/workspace_settings/email_preferences.md"),
    ("ka0VP0000007XYjYAM", "Restrict dashboard access without deleting user", "_docs/_user_guide/administer/global/user_management/teams.md"),
    ("ka0VP0000008HtJYAU", "Dashboard key-value pair data types", "_docs/_user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs.md"),
    ("ka0VP0000008f9FYAQ", "Content Cards dismissals higher than impressions", "_docs/_developer_guide/content_cards/logging_analytics.md"),
]


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=REPO, text=True, capture_output=True, check=False, **kw)


def apply_edit(path: Path) -> bool:
    rel = path.relative_to(REPO).as_posix()
    text = path.read_text(encoding="utf-8")
    original = text

    if rel.endswith("export_troubleshooting.md"):
        needle = "## API exports  \nWhen you export data through the APIs with a storage partner connected"
        insert = (
            "## API exports  \n"
            "When you export data through the APIs with a storage partner connected, the export files are written to your bucket. "
            "For **Amazon S3** and **Microsoft Azure Blob Storage**, files typically appear in your bucket **as the export runs**—you do not need to wait for the entire job to finish before accessing partial results. "
            "Each worker uploads completed batches incrementally rather than holding everything until the end.\n\n"
            "When you export data through the APIs with a storage partner connected"
        )
        if needle in text and "as the export runs" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("create_a_canvas.md"):
        needle = "You can adjust the distribution between your messages by double-clicking the **Variant Name** headers.\n"
        insert = (
            "You can adjust the distribution between your messages by double-clicking the **Variant Name** headers.\n\n"
            "If a single variant has multiple branches with the same audience and send time, Braze does not guarantee an even split across those branches. "
            "Distribution may favor the branch that was created first. "
            "For an even split, use [Random Bucket Number]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) filters on each branch. "
            "For more detail, see [What happens if the audience and send time are identical for a Canvas that has one variant, but multiple branches?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches).\n\n"
        )
        if needle in text and "does not guarantee an even split" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("canvas/faqs.md"):
        needle = "## Segmentation\n"
        insert = (
            "### Can I exclude users who are currently in a Canvas journey from a campaign or segment?\n\n"
            "No. Braze does not provide a segment or campaign filter for \"currently in a Canvas journey.\" "
            "To target or suppress users based on Canvas entry, use webhooks at Canvas entry and exit to set custom attributes, then filter on those attributes in campaigns or segments.\n\n"
            "## Segmentation\n"
        )
        if needle in text and "currently in a Canvas journey" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("braze_currents/faq.md"):
        needle = "### What happens if my storage bucket is unavailable when Currents tries to write data?\n"
        insert = (
            "### Why are session end events delayed or missing in Currents?\n\n"
            "Session end events are flushed on the SDK's normal upload schedule (typically about every 10 seconds when the network is available). "
            "If a user force-quits the app or goes offline before that flush, the session end may arrive late or not at all in Currents.\n\n"
            "To improve timeliness for session end in Currents, call your platform's immediate flush after session start when you need near-real-time session boundaries—for example, `requestImmediateDataFlush()` on supported SDKs. "
            "For general flush behavior, see [SDK overview]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/#data-upload-and-download).\n\n"
            "### What happens if my storage bucket is unavailable when Currents tries to write data?\n"
        )
        if needle in text and "requestImmediateDataFlush" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("intelligent_selection.md"):
        needle = "Intelligent Selection will not be available if you haven't yet added conversion events to your Canvas or if your campaign is composed of a solo variant.\n{% endtab %}"
        insert = (
            "Intelligent Selection will not be available if you haven't yet added conversion events to your Canvas or if your campaign is composed of a solo variant.\n\n"
            "{% alert note %}\n"
            "**Canvas and campaigns handle re-eligibility differently.** Campaigns cannot enable re-eligibility when Intelligent Selection is on. "
            "Canvases can use Intelligent Selection with re-eligibility enabled, but Braze cannot guarantee that a user receives the same variant on re-entry because optimum allocation shifts over time.\n"
            "{% endalert %}\n"
            "{% endtab %}"
        )
        if needle in text and "Canvas and campaigns handle re-eligibility" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("quiet_hours.md"):
        needle = "## Things to consider\n"
        insert = (
            "## Segment membership and quiet hours\n\n"
            "Segment and audience filters are evaluated when a user is scheduled to receive a message, not again when quiet hours end. "
            "If a user qualifies during quiet hours, Braze holds the send until the quiet window closes and delivers the message without re-checking segment membership. "
            "A user who left the segment while the message was held can still receive it after quiet hours.\n\n"
            "## Things to consider\n"
        )
        if needle in text and "Segment membership and quiet hours" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("canvas/troubleshooting.md"):
        needle = "## Why did a user not receive a triggered Canvas step?\n"
        insert = (
            "## \"Too Many Canvas Branches\" error\n\n"
            "If you see a **Too Many Canvas Branches** error when saving or launching a Canvas, the journey exceeds Braze limits for full-step branches on that Canvas.\n\n"
            "- Prefer **Audience Path** steps instead of many parallel full-step branches when you need large fan-out.\n"
            "- Reconfigure or relaunch the Canvas so the branch count stays within supported limits.\n\n"
            "## Why did a user not receive a triggered Canvas step?\n"
        )
        if needle in text and "Too Many Canvas Branches" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("unity/sdk_integration.md"):
        needle = "{% alert note %}\nAs of Unity 2.6.0, the bundled Braze Android SDK artifact requires"
        insert = (
            "{% alert note %}\n"
            "If Android builds fail with **This project uses AndroidX dependencies, but the 'android.useAndroidX' property is not enabled**, "
            "open `Assets/Plugins/Android/gradleTemplate.properties` in your Unity project and set `android.useAndroidX=true`. "
            "See the [Braze Unity sample app](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples) for a working template.\n"
            "{% endalert %}\n\n"
            "{% alert note %}\nAs of Unity 2.6.0, the bundled Braze Android SDK artifact requires"
        )
        if "android.useAndroidX=true" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("liquid_use_cases.md"):
        needle = "### Subtract two custom attributes to display the difference as a monetary value {#attribute-monetary-difference}\n"
        insert = (
            "### Format currency for European number conventions {#european-currency-format}\n\n"
            "Use the [`money` filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#money-filter) with `number_with_delimiter` and `replace` to swap decimal and thousands separators for locales that use comma as the decimal separator (for example, Italy or Germany).\n\n"
            "{% raw %}\n"
            "```liquid\n"
            "{{ 1234.56 | money | replace: '.', '#' | replace: ',', '.' | replace: '#', ',' }}\n"
            "```\n"
            "{% endraw %}\n\n"
            "### Subtract two custom attributes to display the difference as a monetary value {#attribute-monetary-difference}\n"
        )
        if "european-currency-format" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("dashboards/home.md"):
        needle = "{% alert important %}\nUsers associated with more than one app are counted separately"
        insert = (
            "The *New Users* count can **decrease retroactively** when an anonymous profile is linked to an identified user and the anonymous profile is orphaned. "
            "Braze removes the orphaned profile from the app usage totals, which can lower *New Users* for a period you already viewed. "
            "For profile linking behavior, see [User profile lifecycle]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/).\n\n"
            "{% alert important %}\nUsers associated with more than one app are counted separately"
        )
        if "decrease retroactively" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("report_builder.md"):
        needle = "Statistics for deleted message variants are not displayed when you break down your report by campaigns or Canvases. However, channel-level totals include all statistics regardless of whether the variant was deleted. For example, _Sends_ for email include all email sends, but if you break down those statistics by campaign, the numbers may be lower because sends for deleted message variants are filtered out.\n"
        insert = (
            "Statistics for deleted message variants are not displayed when you break down your report by campaigns or Canvases. However, channel-level totals include all statistics regardless of whether the variant was deleted. For example, _Sends_ for email include all email sends, but if you break down those statistics by campaign, the numbers may be lower because sends for deleted message variants are filtered out.\n\n"
            "*Unique Recipients* can be higher than *Unique Impressions* in the same report when a message variant was deleted after send. "
            "Impressions tied to deleted variants may no longer appear in variant-level breakdowns, while recipient counts can still reflect users who received the message.\n"
        )
        if "Unique Recipients* can be higher than *Unique Impressions" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("email_preferences.md"):
        needle = "### Mailbox provider support\n"
        insert = (
            "### Does turning off the list-unsubscribe header remove the Gmail Unsubscribe button?\n\n"
            "No. Disabling Braze's list-unsubscribe header does not give you control over whether Gmail shows its **Unsubscribe** control in the mailbox UI. "
            "Gmail may still surface an unsubscribe option from the message body or other provider logic. "
            "Whether the header appears in the raw message is separate from whether Gmail displays it to recipients.\n\n"
            "### Mailbox provider support\n"
        )
        if "turning off the list-unsubscribe header" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("user_management/teams.md"):
        needle = "## Assign users to Teams\n"
        insert = (
            "## Restrict dashboard access without deleting a user\n\n"
            "To prevent a company user from accessing the dashboard without deleting their account, assign them to a Team with only minimal permissions—for example, **Access Media Library**—and no permissions for campaigns, Canvases, or user data. "
            "They remain in the workspace but cannot perform most messaging or audience actions.\n\n"
            "## Assign users to Teams\n"
        )
        if "Restrict dashboard access without deleting" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("key_value_pairs.md"):
        needle = "In the message composer, select the **Settings** tab, select **Add New Pair**, and specify your key-value pairs.\n"
        insert = (
            "In the message composer, select the **Settings** tab, select **Add New Pair**, and specify your key-value pairs.\n\n"
            "When you add key-value pairs in the dashboard composer, values are sent as strings. "
            "Reserved Apple Push Notification service keys (such as `loc-key` for localized alert text) still use the correct types on the device. "
            "For custom keys, your app receives string values unless you parse them in your integration.\n\n"
        )
        if "values are sent as strings" not in text:
            text = text.replace(needle, insert, 1)

    elif rel.endswith("content_cards/logging_analytics.md"):
        needle = "## Missing Content Cards analytics\n"
        insert = (
            "## Unique dismissals higher than unique impressions\n\n"
            "If dashboard analytics show *Unique Dismissals* higher than *Unique Impressions* for Content Cards, review your logging integration:\n\n"
            "- Confirm whether you use Braze's default Content Card UI or a fully custom UI. Custom UI requires you to log impressions and dismissals explicitly.\n"
            "- Verify you call the correct logging methods when a card is shown and when a user dismisses it.\n"
            "- Dismissals logged without matching impressions usually indicate a bug in custom logging code, not expected Braze behavior.\n\n"
            "For method details, see the platform sections in this article and [Log analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) for your SDK.\n\n"
            "## Missing Content Cards analytics\n"
        )
        if "Unique dismissals higher than unique impressions" not in text:
            text = text.replace(needle, insert, 1)

    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def branch_name(article_id: str) -> str:
    return f"sf-cursor-kb-{article_id.lower()}"


def process_article(article_id: str, title: str, rel_path: str, push: bool) -> str | None:
    path = REPO / rel_path
    if not path.is_file():
        print(f"SKIP {article_id}: missing {rel_path}", file=sys.stderr)
        return None

    run(["git", "checkout", "develop"])
    run(["git", "pull", "origin", "develop"])
    br = branch_name(article_id)
    run(["git", "checkout", "-B", br, "develop"])

    if not apply_edit(path):
        print(f"SKIP {article_id}: no edit applied (already present?)", file=sys.stderr)
        run(["git", "checkout", "develop"])
        run(["git", "branch", "-D", br])
        return None

    run(["git", "add", rel_path])
    commit_msg = f"SF KB: {title}\n\nSalesforce Knowledge article_id: {article_id}"
    c = run(["git", "commit", "-m", commit_msg])
    if c.returncode != 0:
        print(c.stderr, file=sys.stderr)
        return None

    if not push:
        print(f"LOCAL OK {article_id} on {br}")
        return br

    p = run(["git", "push", "-u", "origin", br])
    if p.returncode != 0:
        print(p.stderr, file=sys.stderr)
        return None

    body = f"""## Summary
- Document Salesforce Knowledge gap for `{article_id}`.
- **Salesforce Knowledge article:** `{article_id}`

## Test plan
- [ ] Review prose against Braze Docs style guide
- [ ] Confirm technical accuracy on the target page
"""
    pr = run(
        [
            "gh",
            "pr",
            "create",
            "--base",
            "develop",
            "--title",
            f"SF KB: {title}",
            "--label",
            "salesforce migration",
            "--body",
            body,
        ]
    )
    if pr.returncode != 0:
        print(pr.stderr, file=sys.stderr)
        return br
    url = pr.stdout.strip().splitlines()[-1] if pr.stdout else br
    print(f"OK {article_id} -> {url}")
    return url


def main() -> None:
    push = "--push" in sys.argv
    results: list[str] = []
    for aid, title, rel in ARTICLES:
        url = process_article(aid, title, rel, push=push)
        if url:
            results.append(f"| `{aid}` | {title} | {url} |")
    print("\n".join(results))


if __name__ == "__main__":
    main()
