---
nav_title: Rate limits
article_title: Device Messaging API rate limits
page_order: 3
page_type: reference
description: "Learn how Device Messaging API rate limits and response headers work."
hidden: true
---

# Device Messaging API rate limits

Braze applies Device Messaging API rate limits per workspace. If a workspace exceeds a limit, Braze returns a `429 Too Many Requests` status code.

Device Messaging API limits are separate from the default limits documented for other Braze REST API endpoints. Don't assume that a limit, time window, payload size, or reset schedule documented for another endpoint applies to the Device Messaging API.

{% alert important %}
This page is in beta. Features and documentation for the Device Messaging API are subject to change. Contact your Braze account manager to request access.
{% endalert %}

## Rate-limit headers

When rate-limit information is available, a response includes the following headers:

| Header | Description |
|---|---|
| `X-RateLimit-Limit` | The maximum number of requests allowed in the current interval. |
| `X-RateLimit-Remaining` | The number of requests remaining in the current rate-limit window. |
| `X-RateLimit-Reset` | The UTC epoch time when the current rate-limit window resets. |
| `X-RateLimit-Retry-After` | The number of seconds to wait before retrying a rate-limited request. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Device Messaging API rate-limit headers" }

Use these headers to reduce or pause requests before reaching a limit. Headers might not be present on every response.

## Handling rate limits

When you receive a `429` response:

1. Stop or reduce requests for the affected workspace.
2. Use `X-RateLimit-Retry-After` when it is present to determine how long to wait. Otherwise, use `X-RateLimit-Reset` when available to determine when to resume.
3. Retry with exponential backoff and a maximum number of attempts.
