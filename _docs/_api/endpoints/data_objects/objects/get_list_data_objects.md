---
nav_title: "GET: List data objects"
article_title: "GET: List Data Objects"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the List data objects endpoint."
---
{% api %}
# List data objects
{% apimethod get %}
/data_objects/objects/{type_name}
{% endapimethod %}

> Use this endpoint to list objects for a specific data object type.

{% alert important %}
Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `data_objects.read`.

## Rate limit

This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/data_objects/objects/{type_name}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Data object type machine name |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List data objects path parameters" }

## Query parameters

The following table lists and describes the query parameters for the `/data_objects/objects/{type_name}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `search_term` | Optional | String | Substring filter on object identifier |
| `limit` | Optional | Integer | Page size. Default `100`. Clamped to `1` through `250` |
| `offset` | Optional | Integer | Offset. Default `0`. Negative values are floored to `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List data objects query parameters" }

## Example request

This section includes a sample parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for request parameters.

```json
{
  "type_name": "account",
  "search_term": "acct",
  "limit": 100,
  "offset": 0
}
```

### Sample cURL request

This example lists the `account` records matching the search term `acct`, returning the first page of results.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account?search_term=acct&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `200` could return the following response body.

```json
{
  "items": [
    {
      "type_name": "account",
      "external_id": "acct-123",
      "attributes": { "name": "Acme", "industry": "software" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | List of data object records |
| `items[].type_name` | Required | String | Data object type machine name |
| `items[].external_id` | Required | String | Data object identifier |
| `items[].attributes` | Required | Object | Object attributes keyed by field name |
| `total_count` | Required | Integer | Total number of matching records |
| `has_more` | Required | Boolean | Whether another page of results is available |
| `next_offset` | Optional | Integer | Offset for the next page when `has_more` is `true` |
| `offset` | Required | Integer | Current page offset |
| `limit` | Required | Integer | Page size used by the request |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List data objects response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `404` | Type not found (`data-object-type-not-found`) | Confirm `type_name` exists in the workspace and matches the machine name exactly. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `data_objects.read` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="List data objects errors" }
{% endapi %}
