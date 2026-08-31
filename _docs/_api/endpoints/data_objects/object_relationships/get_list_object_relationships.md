---
nav_title: "GET: List object relationships"
article_title: "GET: List Object Relationships"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the List object relationships endpoint."
---
{% api %}
# List object relationships
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use this endpoint to list related data objects from one object anchor.

{% alert important %}
Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `data_objects.read`.

## Rate limit

This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/data_objects/objects/{type_name}/{external_id}/object_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Source object type |
| `external_id` | Required | String | Source object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List object relationships path parameters" }

## Query parameters

The following table lists and describes the query parameters for the `/data_objects/objects/{type_name}/{external_id}/object_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `anchor` | Optional | String | `source` (default) or `target` |
| `rel_kind` | Optional | String | Filter by one relationship kind |
| `limit` | Optional | Integer | Page size. Default `100`. Clamped to `1` through `250` |
| `offset` | Optional | Integer | Offset. Default `0`. Negative values are floored to `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List object relationships query parameters" }

## Example request

This section includes a sample parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for request parameters.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "anchor": "source",
  "rel_kind": "subaccount",
  "limit": 100,
  "offset": 0
}
```

### Sample cURL request

This example lists the `subaccount` records that `acct-123` links out to, returning the first page of results.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
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
      "rel_kind": "subaccount",
      "to_data_object": {
        "type_name": "account",
        "external_id": "acct-456",
        "attributes": { "name": "Child Account" }
      },
      "attributes": {}
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

With `anchor=target`, related objects are returned as `from_data_object`.

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | List of object relationship records |
| `items[].rel_kind` | Required | String | Relationship kind value |
| `items[].to_data_object` | Conditional | Object | Related object when `anchor=source` |
| `items[].from_data_object` | Conditional | Object | Related object when `anchor=target` |
| `items[].to_data_object.type_name` | Conditional | String | Related object type name |
| `items[].to_data_object.external_id` | Conditional | String | Related object external ID |
| `items[].to_data_object.attributes` | Conditional | Object | Related object attributes |
| `items[].from_data_object.type_name` | Conditional | String | Related object type name |
| `items[].from_data_object.external_id` | Conditional | String | Related object external ID |
| `items[].from_data_object.attributes` | Conditional | Object | Related object attributes |
| `items[].attributes` | Required | Object | Relationship attributes |
| `total_count` | Required | Integer | Total number of matching records |
| `has_more` | Required | Boolean | Whether another page of results is available |
| `next_offset` | Optional | Integer | Offset for the next page when `has_more` is `true` |
| `offset` | Required | Integer | Current page offset |
| `limit` | Required | Integer | Page size used by the request |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List object relationships response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Invalid `anchor` | Use `source` or `target` for `anchor`. |
| `404` | Type or object not found | Confirm `type_name` and `external_id` both exist in the workspace. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `data_objects.read` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="List object relationships errors" }
{% endapi %}
