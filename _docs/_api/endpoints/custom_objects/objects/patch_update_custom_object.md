---
nav_title: "PATCH: Update custom object"
article_title: "PATCH: Update Custom Object"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines details about the Update custom object endpoint."
---
{% api %}
# Update custom object
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use this endpoint to merge attributes into an existing custom object.

{% alert important %}
Custom Objects is currently in early access. Your workspace must be enabled before the Custom Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `custom_objects.update`.

## Rate limit

This endpoint is in the Custom Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/custom_objects/objects/{type_name}/{external_id}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Custom object type machine name |
| `external_id` | Required | String | Object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update custom object path parameters" }

## Request parameters

The following table lists and describes the JSON request body parameters for the `/custom_objects/objects/{type_name}/{external_id}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `attributes` | Required | Object | Top-level fields to merge |
| `display_name` | Optional | String | Display label for the object. When the type has a display-name source field, the value of that field takes precedence. When omitted, the existing display name is preserved |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update custom object request parameters" }

## Example request

This section includes a sample JSON payload and a sample cURL request.

### Sample request payload

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### Sample cURL request

This example updates the `credits` attribute on `acct-123` and leaves the record's other attributes unchanged.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `200` could return the following response body. The `attributes` object reflects the result of the merge.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `custom_object` | Required | Object | Updated custom object record |
| `custom_object.type_name` | Required | String | Custom object type machine name |
| `custom_object.external_id` | Required | String | Custom object identifier |
| `custom_object.attributes` | Required | Object | Object attributes after merge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update custom object response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Validation error | Confirm every field in `attributes` exists in the type schema and uses the correct data type. |
| `404` | Type not found or object not found | Confirm `type_name` and `external_id` both exist in the workspace. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `custom_objects.update` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Update custom object errors" }
{% endapi %}
