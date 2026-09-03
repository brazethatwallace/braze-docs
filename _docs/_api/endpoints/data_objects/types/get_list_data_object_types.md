---
nav_title: "GET: List data object types"
article_title: "GET: List Data Object Types"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the List data object types endpoint."
---
{% api %}
# List data object types
{% apimethod get %}
/data_objects/types
{% endapimethod %}

> Use this endpoint to list data object types in a workspace.

{% alert important %}
Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `data_objects.read`.

## Rate limit

This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.

## Query parameters

The following table lists and describes the query parameters for the `/data_objects/types` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `search_term` | Optional | String | Case-insensitive prefix filter on type name |
| `limit` | Optional | Integer | Page size. Default `100`. Clamped to `1` through `250` |
| `offset` | Optional | Integer | Offset. Default `0`. Negative values are floored to `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List data object types query parameters" }

## Example request

This section includes a sample query-parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for the query parameters in this request.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### Sample cURL request

This example lists the data object types matching the search term `acc`, returning two results per page.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types?search_term=acc&limit=2&offset=0' \
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
      "metadata": { "display_name_source": "name" }
    },
    {
      "type_name": "contact",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`metadata.display_name_source` is present when a display-name field is configured for the type.

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | List of data object type records |
| `items[].type_name` | Required | String | Data object type machine name |
| `items[].metadata` | Required | Object | Type metadata object |
| `total_count` | Required | Integer | Total number of matching records |
| `has_more` | Required | Boolean | Whether another page of results is available |
| `next_offset` | Optional | Integer | Offset for the next page when `has_more` is `true` |
| `offset` | Required | Integer | Current page offset |
| `limit` | Required | Integer | Page size used by the request |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List data object types response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Invalid query parameter type or value | Ensure `limit` and `offset` are integers and that all parameter values are valid. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `data_objects.read` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="List data object types errors" }
{% endapi %}
