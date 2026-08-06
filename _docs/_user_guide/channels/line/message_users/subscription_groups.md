---
nav_title: Subscription groups
article_title: Subscription Groups
page_order: 1
description: "This article covers LINE message subscription groups."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINE subscription groups

> There are two subscription states for LINE users: subscribed and unsubscribed. LINE can have up to 100 subscription groups per workspace, with each subscription group connected to its own LINE channel. For a cross-channel overview of subscription groups, see [Subscription groups]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

| State | Definition |
| --- | --- |
| Subscribed | The user followed the LINE channel from within their LINE app. Users are automatically subscribed when they follow after you've completed the integration steps. |
| Unsubscribed | The user didn't follow the LINE channel from within their LINE app, or the user explicitly unfollowed the LINE channel. <br><br> Users who unsubscribe from a LINE subscription group will no longer receive any LINE messages from sending channels that belong to the subscription group. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE subscription groups" }

## Set a user's LINE subscription group

LINE hosts the users' subscription status. Braze processes the follow and unfollow events that update the subscription status.

{% alert important %}
LINE subscription groups can't be moved between workspaces. If you re-integrate a LINE channel in another workspace after archiving its subscription group, Braze creates a new subscription group in the target workspace—the original stays in the first workspace.
{% endalert %}

## Archive behavior

- **Standard archive:** If you archive a LINE subscription group and don't re-integrate the channel in another workspace, you can unarchive the subscription group later.
- **Permanent archive:** If you re-integrate the LINE channel in a different workspace after archiving its subscription group, the original subscription group is permanently archived and can't be unarchived through the dashboard.

For channel re-integration steps, refer to [LINE setup]({{site.baseurl}}/user_guide/channels/line/line_setup/#re-integrate-a-line-channel-in-another-workspace).
