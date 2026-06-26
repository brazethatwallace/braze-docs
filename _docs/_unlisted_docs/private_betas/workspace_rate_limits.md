---
article_title: Workspace rate limits
description: "Learn how to set workspace rate limits, so you can control how your company’s overall API rate limit is distributed across individual workspaces, preventing a single integration or team from making too many requests to a specific endpoint."
permalink: /workspace_rate_limits/
---

# Workspace rate limits

> Learn how to set workspace rate limits, so you can control how your company’s overall API rate limit is distributed across individual workspaces, preventing a single integration or team from making too many requests to a specific endpoint.

## Prerequisites

Workspace rate limits are only available for Braze contracts without data points. Additionally, you'll need [admin permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) manage rate limits.

## About workspace rate limits

By default, company-level rate limits are shared across your workspaces.

With workspace rate limits, you can set a maximum number of API requests a workspace can make to a specific ingestion endpoint, such as `/users/track` or SDK data. You can also apply rate limits to a group of workspaces, meaning the limit is shared across all the workspaces in that group.

For example, if your `/users/track` endpoint has a company-level rate limit of 500,000 requests per hour, you could set the following workspace rate limits:

- A rate limit of 10,000 requests per hour applied to _Workspace 1_
- A shared rate limit of 200,000 requests per hour applied to _Workspace 2_ and _Workspace 3_
- No rate limit applied to _Workspace 4_, meaning the default company-level rate limit is used

## Managing workspace rate limits

### Assigning a limit

To assign a new rate limit for one or more workspaces, go to **Settings** > **Admin Settings** > **Workspace rate limits**, then select **Assign rate limits**.

![The 'Workspace Rate Limits' page in the Braze dashboard.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

Next, choose an endpoint and one or more workspaces, then enter your rate limit. The limit can be any whole number that's greater than 1,000 and doesn't exceed your company-level rate limit.

When you're finished, select **Update Rate Limit**.

![The 'Rate Limit' popup window with options for choosing an endpoint, workspaces, and rate limit.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
If you choose more than one workspace, the rate limit will be shared across that group of workspaces.
{% endalert %}

### Editing a limit

To edit an existing workspace rate limit, go to **Settings** > **Admin Settings** > **Workspace Rate Limits**, then select the <i class="fas fa-ellipsis-vertical"></i> vertical ellipsis and choose **Edit**. Your new rate limit may take affect within a few minutes.

### Resetting a limit

To reset an existing rate limit so it's reverted to your company-level rate limit, go to **Settings** > **Admin Settings** > **Workspace Rate Limits**, then select the <i class="fas fa-ellipsis-vertical"></i> vertical ellipsis and choose **Reset**.

## Monitoring usage

### Response headers

By default, all ingestion responses include the following headers, which reflect your steady company-level rate limit.

We recommend using these headers in your integration logic to manage rate limits effectively. For example, you can reduce request volume as you approach these limits and use the `Retry-After` header to determine when to retry.

| Header Name | Description |
| ----- | ----- |
| `X-RateLimit-Limit` | The maximum number of requests allowed in the current rate limit window. |
| `X-RateLimit-Remaining` | The number of requests remaining in the current window. |
| `X-RateLimit-Reset` | When the current rate limit window resets (UTC epoch seconds). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Error codes

If a workspace rate limit is reached, your request will return a `429` response code and the headers will include a `Retry-After` value. This represents the number of seconds until the rate limit resets.

The `Retry-After` value reflects the number of seconds until the start of the next hour, when the workspace rate limit resets.

### API usage dashboard

To monitor request volume, response codes, and ingestion behavior across workspaces, you can also use the [API Usage Dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard).

You can filter the dashboard to show `429 Workspace Rate Limited` or `429 Company Rate Limited`, so you can quickly identify whether a request was limited by the company or workspace rate limit.