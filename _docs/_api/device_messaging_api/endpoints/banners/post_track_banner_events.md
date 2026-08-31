---
nav_title: "POST: Track Banner analytics events"
article_title: "POST: Track Banner analytics events"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Use this endpoint to track impression, click, and dismissal events for Banners."
hidden: true
---

{% api %}
# Track Banner analytics events
{% apimethod post %}
/v1/device-messaging/banners/track
{% endapimethod %}

> Use this endpoint to record impression, click, and dismissal events for Banners.

Braze validates each event separately. When a request contains both valid and invalid events, Braze processes the valid events and returns details about skipped events in the `errors` array. If no events are valid, Braze returns a `400` status code.

{% alert important %}
This page is in beta. Features and documentation for the Device Messaging API are subject to change. Contact your Braze account manager to request access.
{% endalert %}

## Prerequisites

To use this endpoint, you need the following:

- A workspace with Banners enabled
- A [client-side REST API key]({{site.baseurl}}/api/device_messaging_api/authentication) with the `banners.track` permission
- The [REST endpoint]({{site.baseurl}}/api/basics#endpoints) for your Braze instance
- A Banner `id` returned by the [Retrieve Banners for a user endpoint]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)

Include the client-side REST API key in the `Authorization` header as a bearer token.

## Rate limit

Rate limits apply per workspace. If you exceed the rate limit, Braze returns a `429` status code. When available, use the `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and `X-RateLimit-Retry-After` response headers to monitor your usage and determine when to retry.

For more information, see [Device Messaging API rate limits]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Dismissing Banners

Tracking a `dismiss` event dismisses the Banner for the given user. Subsequent Banner syncs for that user won't include previously dismissed Banners, unless re-eligibility is configured in the campaign.

{% alert note %}
Dismissal events are processed asynchronously and aren't reflected immediately. In rare cases, processing can take a few minutes. Avoid calling the [Retrieve Banners for a user endpoint]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) immediately after a dismissal, because the Banner may still be returned during this window.
{% endalert %}

Braze doesn't reconcile the Banner's state in your UI. Hiding the Banner after a dismissal, and keeping it hidden until Braze processes the event, is up to your app.

## Request body

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "{BANNER_ID}",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    }
  ]
}
```

## Request parameters

| Parameter | Required | Data type | Description | Example |
|---|---|---|---|---|
| `external_user_id` | Required | String | The external ID of the user associated with all events in the request. The UTF-8 encoded value must be fewer than 987 bytes. | `user_abc123` |
| `app_id` | Required | String | The [app API identifier]({{site.baseurl}}/api/identifier_types#app-identifier). It must identify an app in the authenticated workspace. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Required | String | The version of the host app. It must not exceed 255 characters. | `1.0.0` |
| `events` | Required | Array of objects | One or more Banner analytics events to record. | `[{"id":"bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E","event_type":"impression","timestamp":"2026-04-09T12:00:00Z"}]` |
| `events[].id` | Required | String | The Banner `id` returned by the Retrieve Banners for a user endpoint. Use the Banner ID, not the `placement_id`, so Braze attributes the event to the correct campaign and variant. | `bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E` |
| `events[].event_type` | Required | String | The event type. Possible values are `impression`, `click`, and `dismiss`. | `impression` |
| `events[].timestamp` | Required | String | The date and time when the event occurred, formatted as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string. | `2026-04-09T12:00:00Z` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Request parameters" }

## Example request

Replace *`YOUR_REST_API_URL`* with the [REST endpoint]({{site.baseurl}}/api/basics#endpoints) for your Braze instance.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/track' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    },
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "click",
      "timestamp": "2026-04-09T12:00:05Z"
    }
  ]
}'
```

## Response parameters

| Parameter | Data type | Description |
|---|---|---|
| `events_processed` | Integer | The number of events that Braze validated and queued. |
| `message` | String | The status of the accepted event batch. |
| `errors` | Array of objects | Details about events that Braze skipped. This array is absent when Braze processes all events. |
| `errors[].type` | String | The validation error for the skipped event. |
| `errors[].index` | Integer | The zero-based index of the skipped event in the request's `events` array. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response parameters" }

## Example responses

### All events processed

When Braze accepts all events, it returns a `202` status code.

```json
{
  "events_processed": 2,
  "message": "success"
}
```

### Some events skipped

Braze also returns a `202` status code when it accepts at least one valid event. The response identifies any skipped events.

```json
{
  "events_processed": 2,
  "message": "success",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 2
    }
  ]
}
```

### No valid events

If Braze can't process any events, it returns a `400` status code.

```json
{
  "message": "No valid events provided.",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 0
    },
    {
      "type": "'timestamp' is required",
      "index": 1
    }
  ]
}
```

## Status codes

| Status code | Description |
|---|---|
| `202` | Braze accepted at least one event. The response lists any skipped events. |
| `400` | The request is malformed, required fields are invalid, or no events are valid. |
| `401` | The client-side REST API key is missing or invalid. |
| `403` | The client-side REST API key doesn't have the `banners.track` permission. |
| `404` | The Banners feature isn't enabled for the workspace. |
| `429` | The workspace exceeded its rate limit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status codes" }

For more information, see [Device Messaging API error handling and retries]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}
