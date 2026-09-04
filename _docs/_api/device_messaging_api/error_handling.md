---
nav_title: Error handling and retries
article_title: Device Messaging API error handling and retries
page_order: 2
page_type: reference
description: "Learn how to handle Device Messaging API responses, errors, and retries."
hidden: true
---

# Device Messaging API error handling and retries

Device Messaging API response bodies and success semantics vary by endpoint. Use each endpoint's response schema and status-code table as the authoritative contract.

{% alert important %}
This page is in beta. Features and documentation for the Device Messaging API are subject to change. Contact your Braze account manager to request access.
{% endalert %}

## Success responses

The Banner endpoints use different success responses:

- `POST /v1/device-messaging/banners/sync` returns a `200` status code with a `banners` object.
- `POST /v1/device-messaging/banners/track` returns a `202` status code with `events_processed` and `message`. If Braze skips individual events, the response also includes an `errors` array.

A `202` response from the tracking endpoint means Braze accepted at least one valid event. Review the `errors` array to identify skipped events.

## Error responses

Error response fields also vary:

- Banner retrieval errors use an `error` field.
- Banner tracking errors use a `message` field and can include an indexed `errors` array.

Don't parse error-message text to determine application behavior. Use the HTTP status code and endpoint-specific fields instead.

## Retry guidance

Use the following guidance when deciding whether to retry:

| Status code | Retry guidance |
|---|---|
| `400` | Correct the request before retrying. For Banner tracking, correct skipped events before retrying them. |
| `401` or `403` | Verify the client-side REST API key and its permissions before retrying. |
| `404` | Confirm that the Device Messaging API is enabled for the workspace and that the endpoint URL is correct. |
| `429` | Reduce the request rate and retry with exponential backoff. Use rate-limit response headers when available. |
| `5XX` | Retry with exponential backoff and a maximum number of attempts. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Device Messaging API retry guidance" }

For the exact response body and supported status codes, refer to the relevant endpoint:

- [Retrieve Banners for a user]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)
- [Track Banner analytics events]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)
