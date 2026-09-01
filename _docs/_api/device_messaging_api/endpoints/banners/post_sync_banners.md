---
nav_title: "POST: Retrieve Banners for a user"
article_title: "POST: Retrieve Banners for a user"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Use this endpoint to retrieve eligible Banners for a user."
hidden: true
---

{% api %}
# Retrieve Banners for a user
{% apimethod post %}
/v1/device-messaging/banners/sync
{% endapimethod %}

> Use this endpoint to retrieve the eligible Banner for each requested placement for a user.

The response contains structured Banner properties that you can use to build a custom interface. It doesn't contain rendered HTML.

{% alert important %}
This page is in beta. Features and documentation for the Device Messaging API are subject to change. Contact your Braze account manager to request access.
{% endalert %}

## Prerequisites

To use this endpoint, you need the following:

- A workspace with Banners enabled
- A [client-side REST API key]({{site.baseurl}}/api/device_messaging_api/authentication) with the `banners.sync` permission
- The [REST endpoint]({{site.baseurl}}/api/basics#endpoints) for your Braze instance

Include the client-side REST API key in the `Authorization` header as a bearer token.

## Rate limit

Rate limits apply per workspace. If you exceed the rate limit, Braze returns a `429` status code. When available, use the `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` response headers to monitor your usage.

For more information, see [Device Messaging API rate limits]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Request body

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "device_id": "{DEVICE_ID}",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}
```

## Request parameters

| Parameter | Required | Data type | Description | Example |
|---|---|---|---|---|
| `external_user_id` | Required | String | The external ID of the user. | `user_abc123` |
| `app_id` | Required | String | The [app API identifier]({{site.baseurl}}/api/identifier_types#app-identifier). It must identify an app in the authenticated workspace. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Required | String | The version of the host app. It must not exceed 255 characters. | `1.0.0` |
| `placements` | Required | Array of strings | One or more placement IDs to retrieve Banners for. Include at least one placement ID. | `["home_hero", "sidebar_promo"]` |
| `device_id` | Optional | String | The Braze device identifier for the device this request targets. It must not exceed 1,011 bytes. | `7bb8ac35-0a3f-4b8c-96ad-2e2e0dd1a4c9` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Request parameters" }

### Personalizing with device attributes

When you include `device_id` and that device exists on the user's profile, Braze populates the {% raw %}`{{targeted_device.${...}}}`{% endraw %} Liquid namespace while rendering the Banner. This lets you personalize Banner properties by the device's platform, model, or operating system. For more information, see [Targeted device information]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information).

If you omit `device_id`, send an empty value, or send an identifier that isn't on the user's profile, Braze still returns a `200` status code and renders the Banner with those tags unresolved, so they fall back to any Liquid `default` filter values. Braze doesn't create a device or return an error in these cases.

## Example request

Replace *`YOUR_REST_API_URL`* with the [REST endpoint]({{site.baseurl}}/api/basics#endpoints) for your Braze instance.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/sync' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "device_id": "7bb8ac35-0a3f-4b8c-96ad-2e2e0dd1a4c9",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}'
```

## Response parameters

| Parameter | Data type | Description |
|---|---|---|
| `banners` | Object | A map of each requested placement ID to its resolved Banner. The value is `null` when no Banner is eligible for a placement. |
| `banners.{placement_id}.id` | String | The unique Banner identifier. Use this value to report impression and click events. |
| `banners.{placement_id}.placement_id` | String | The placement ID matched to the Banner. |
| `banners.{placement_id}.is_control` | Boolean | Whether the Banner is a control-group variant. |
| `banners.{placement_id}.is_test_send` | Boolean | Whether the Banner is from a test send. Defaults to `false`. |
| `banners.{placement_id}.expires_at` | Integer | The Unix timestamp, in seconds, after which you shouldn't display the Banner. A value of `-1` means the Banner doesn't expire. |
| `banners.{placement_id}.properties` | Object or null | Marketer-defined properties for the Banner. Each property contains a `type` and `value`. |
| `banners.{placement_id}.properties.{property}.type` | String | The property's type. Possible values are `number`, `string`, `boolean`, `image`, `jsonobject`, and `datetime`. |
| `banners.{placement_id}.properties.{property}.value` | Number, string, Boolean, or object | The property's value. Its JSON type corresponds to `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response parameters" }

## Example response

A successful request returns a `200` status code and the resolved Banner for each requested placement.

```json
{
  "banners": {
    "home_hero": {
      "id": "this_banner_is_a_stub_01",
      "placement_id": "home_hero",
      "is_control": false,
      "is_test_send": false,
      "expires_at": 1735689600,
      "properties": {
        "headline": {
          "type": "string",
          "value": "Level Up Your Game"
        },
        "cta_label": {
          "type": "string",
          "value": "Shop Now"
        }
      }
    },
    "sidebar_promo": null
  }
}
```

## Status codes

| Status code | Description |
|---|---|
| `200` | Braze resolved Banner data for each requested placement. |
| `400` | The request contains missing or invalid parameters. |
| `401` | The client-side REST API key is missing, invalid, or doesn't have the `banners.sync` permission. |
| `404` | The endpoint is unavailable. This response doesn't distinguish a missing or invalid API key from a disabled Banners feature. |
| `429` | The workspace exceeded its rate limit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status codes" }

For more information, see [Device Messaging API error handling and retries]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}
