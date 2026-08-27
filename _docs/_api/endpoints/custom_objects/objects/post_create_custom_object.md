---
nav_title: "POST: Create custom object"
article_title: "POST: Create Custom Object"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about the Create custom object endpoint."
---
{% api %}
# Create custom object
{% apimethod post %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> Use this endpoint to create one custom object for a type.

{% alert important %}
Custom Objects is currently in early access. Your workspace must be enabled before the Custom Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `custom_objects.create`.

## Rate limit

This endpoint is in the Custom Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/custom_objects/objects/{type_name}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Custom object type machine name |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create custom object path parameters" }

## Request parameters

The following table lists and describes the JSON request body parameters for the `/custom_objects/objects/{type_name}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `external_id` | Required | String | Object identifier, unique within the type |
| `attributes` | Required | Object | Field-name keyed values validated against the type schema |
| `display_name` | Optional | String | Display label for the object. When the type has a display-name source field, the value of that field takes precedence. Defaults to `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create custom object request parameters" }

## Example request

This section includes a sample JSON payload and a sample cURL request.

### Sample request payload

```json
{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}
```

### Sample cURL request

This example creates an `account` record with the identifier `acct-new` and sets its `name` and `industry` attributes.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `201` could return the following response body.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `custom_object` | Required | Object | Created custom object record |
| `custom_object.type_name` | Required | String | Custom object type machine name |
| `custom_object.external_id` | Required | String | Custom object identifier |
| `custom_object.attributes` | Required | Object | Stored object attributes keyed by field name |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create custom object response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Unknown attribute field or invalid attribute type | Confirm every field in `attributes` exists in the type schema and uses the correct data type. |
| `404` | Type not found (`custom-object-type-not-found`) | Confirm `type_name` exists in the workspace and matches the machine name exactly. |
| `409` | Duplicate object (`duplicate-custom-object`) | Use a different `external_id`, or use `PUT` to replace the existing object. |
| `422` | Record limit reached (`custom-object-record-limit-exceeded`) | Reduce object count for the type, or contact Braze support about your workspace limits. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `custom_objects.create` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Create custom object errors" }
{% endapi %}
