---
nav_title: "GET: List user relationships"
article_title: "GET: List User Relationships"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "This article outlines details about the List user relationships endpoint."
---
{% api %}
# List user relationships
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}/user_relationships
{% endapimethod %}

> Use this endpoint to list users linked to one custom object.

{% alert important %}
Custom Objects is currently in early access. Your workspace must be enabled before the Custom Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `custom_objects.user_relationships.read`.

## Rate limit

This endpoint is in the Custom Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/custom_objects/objects/{type_name}/{external_id}/user_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Object type |
| `external_id` | Required | String | Object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List user relationships path parameters" }

## Query parameters

The following table lists and describes the query parameters for the `/custom_objects/objects/{type_name}/{external_id}/user_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `rel_kind` | Optional | String | Filter by relationship kind |
| `limit` | Optional | Integer | Page size. Default `100`. Clamped to `1` through `250` |
| `offset` | Optional | Integer | Offset. Default `0`. Negative values are floored to `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List user relationships query parameters" }

## Example request

This section includes a sample parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for request parameters.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "rel_kind": "account_user",
  "limit": 100,
  "offset": 0
}
```

### Sample cURL request

This example lists the users linked to `acct-123` through the `account_user` relationship.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/user_relationships?rel_kind=account_user&limit=100&offset=0' \
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
      "rel_kind": "account_user",
      "user": { "braze_id": "507f1f77bcf86cd799439011" },
      "attributes": { "role": "admin" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

The `user` payload contains only `braze_id`.

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `items` | Required | Array | List of user relationship records |
| `items[].type_name` | Required | String | Custom object type machine name |
| `items[].external_id` | Required | String | Custom object identifier |
| `items[].rel_kind` | Required | String | Relationship kind value |
| `items[].user` | Required | Object | Linked user object |
| `items[].user.braze_id` | Required | String | Braze user identifier |
| `items[].attributes` | Required | Object | Relationship attributes |
| `total_count` | Required | Integer | Total number of matching records |
| `has_more` | Required | Boolean | Whether another page of results is available |
| `next_offset` | Optional | Integer | Offset for the next page when `has_more` is `true` |
| `offset` | Required | Integer | Current page offset |
| `limit` | Required | Integer | Page size used by the request |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="List user relationships response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `404` | Type or object not found | Confirm `type_name` and `external_id` both exist in the workspace. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `custom_objects.user_relationships.read` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="List user relationships errors" }
{% endapi %}
