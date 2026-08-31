---
nav_title: "PATCH: Update object relationship"
article_title: "PATCH: Update Object Relationship"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Update object relationship endpoint."
---
{% api %}
# Update object relationship
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use this endpoint to merge attributes onto an existing object relationship.

{% alert important %}
Custom Objects is currently in early access. Your workspace must be enabled before the Custom Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `custom_objects.object_relationships.update`.

## Rate limit

This endpoint is in the Custom Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/custom_objects/objects/{type_name}/{external_id}/object_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | URL object type |
| `external_id` | Required | String | URL object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update object relationship path parameters" }

## Request parameters

The following table lists and describes the JSON request body parameters for the `/custom_objects/objects/{type_name}/{external_id}/object_relationships` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `rel_kind` | Required | String | Relationship kind |
| `related_type_name` | Required | String | Related object type |
| `related_external_id` | Required | String | Related object identifier |
| `anchor` | Optional | String | `source` (default) or `target` |
| `attributes` | Optional | Object | Relationship attributes to merge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update object relationship request parameters" }

## Example request

This section includes a sample JSON payload and a sample cURL request.

### Sample request payload

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### Sample cURL request

This example merges attributes into the existing `subaccount` relationship between `acct-123` and `acct-456`, leaving any attributes you omit unchanged.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `200` could return the following response body.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_custom_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `object_relationship` | Required | Object | Updated relationship record |
| `object_relationship.rel_kind` | Required | String | Relationship kind value |
| `object_relationship.to_custom_object` | Conditional | Object | Related object when `anchor=source` |
| `object_relationship.from_custom_object` | Conditional | Object | Related object when `anchor=target` |
| `object_relationship.attributes` | Required | Object | Relationship attributes after merge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update object relationship response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Validation error | Confirm `rel_kind`, `anchor`, and `attributes` are valid for the relationship type. |
| `404` | Relationship not found (`custom-object-relationship-not-found`) | Confirm the source object, related object, and relationship key values all exist. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `custom_objects.object_relationships.update` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Update object relationship errors" }
{% endapi %}
