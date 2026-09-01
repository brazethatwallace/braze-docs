---
nav_title: "DELETE: Delete object relationship"
article_title: "DELETE: Delete Object Relationship"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines details about the Delete object relationship endpoint."
---
{% api %}
# Delete object relationship
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use this endpoint to delete one object-to-object relationship edge.

{% alert important %}
Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `data_objects.object_relationships.delete`.

## Rate limit

This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/data_objects/objects/{type_name}/{external_id}/object_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | URL object type |
| `external_id` | Required | String | URL object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Delete object relationship path parameters" }

## Request parameters

The following table lists and describes the JSON request body parameters for the `/data_objects/objects/{type_name}/{external_id}/object_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `rel_kind` | Required | String | Relationship kind |
| `related_type_name` | Required | String | Related object type |
| `related_external_id` | Required | String | Related object identifier |
| `anchor` | Optional | String | `source` (default) or `target` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Delete object relationship request parameters" }

{% alert note %}
This `DELETE` endpoint expects a JSON request body. Validate that your HTTP client sends request bodies on `DELETE` calls.
{% endalert %}

## Example request

This section includes a sample JSON payload and a sample cURL request.

### Sample request payload

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}
```

### Sample cURL request

This example removes the `subaccount` relationship between `acct-123` and `acct-456`. Both account records remain.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `200` could return the following response body.

```json
{ "deleted": true }
```

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `deleted` | Required | Boolean | Whether the relationship deletion succeeded |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Delete object relationship response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Validation error | Confirm the request body includes valid `rel_kind`, `related_type_name`, `related_external_id`, and `anchor` values. |
| `404` | Relationship or endpoint object not found | Confirm both objects exist and the relationship key values match an existing edge. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `data_objects.object_relationships.delete` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Delete object relationship errors" }
{% endapi %}
