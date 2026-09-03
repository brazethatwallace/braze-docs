---
nav_title: "POST: Create data object"
article_title: "POST: Create Data Object"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "This article outlines details about the Create data object endpoint."
---
{% api %}
# Create data object
{% apimethod post %}
/data_objects/objects/{type_name}
{% endapimethod %}

> Use this endpoint to create one data object for a type.

{% alert important %}
Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `data_objects.create`.

## Rate limit

This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/data_objects/objects/{type_name}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Data object type machine name |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create data object path parameters" }

## Request parameters

The following table lists and describes the JSON request body parameters for the `/data_objects/objects/{type_name}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `external_id` | Required | String | Object identifier, unique within the type |
| `attributes` | Required | Object | Field-name keyed values validated against the type schema |
| `display_name` | Optional | String | Display label for the object. When the type has a display-name source field, the value of that field takes precedence. Defaults to `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create data object request parameters" }

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
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account' \
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
  "data_object": {
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
| `data_object` | Required | Object | Created data object record |
| `data_object.type_name` | Required | String | Data object type machine name |
| `data_object.external_id` | Required | String | Data object identifier |
| `data_object.attributes` | Required | Object | Stored object attributes keyed by field name |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create data object response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Unknown attribute field or invalid attribute type | Confirm every field in `attributes` exists in the type schema and uses the correct data type. |
| `404` | Type not found (`data-object-type-not-found`) | Confirm `type_name` exists in the workspace and matches the machine name exactly. |
| `409` | Duplicate object (`duplicate-data-object`) | Use a different `external_id`, or use `PUT` to replace the existing object. |
| `422` | Record limit reached (`data-object-record-limit-exceeded`) | Reduce object count for the type, or contact Braze support about your workspace limits. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `data_objects.create` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Create data object errors" }
{% endapi %}
