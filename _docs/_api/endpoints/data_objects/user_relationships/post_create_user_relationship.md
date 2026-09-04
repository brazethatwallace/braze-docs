---
nav_title: "POST: Create user relationship"
article_title: "POST: Create User Relationship"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the Create user relationship endpoint."
---
{% api %}
# Create user relationship
{% apimethod post %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Use this endpoint to link one Braze user to one data object.

{% alert important %}
Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `data_objects.user_relationships.create`.

## Rate limit

This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/data_objects/objects/{type_name}/{external_id}/users` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Object type |
| `external_id` | Required | String | Object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create user relationship path parameters" }

## Request parameters

The following table lists and describes the JSON request body parameters for the `/data_objects/objects/{type_name}/{external_id}/users` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `braze_id` | Required | String | Braze user ID |
| `rel_kind` | Required | String | Relationship kind |
| `attributes` | Optional | Object | Relationship attributes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create user relationship request parameters" }

## Example request

This section includes a sample JSON payload and a sample cURL request.

### Sample request payload

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}
```

### Sample cURL request

This example links a user to `acct-123` as an `account_user` and records their `role` as `owner`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `201` could return the following response body.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "owner" }
  }
}
```

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `user_relationship` | Required | Object | Created user relationship record |
| `user_relationship.type_name` | Required | String | Data object type machine name |
| `user_relationship.external_id` | Required | String | Data object identifier |
| `user_relationship.rel_kind` | Required | String | Relationship kind value |
| `user_relationship.user` | Required | Object | Linked user object |
| `user_relationship.user.braze_id` | Required | String | Braze user identifier |
| `user_relationship.attributes` | Required | Object | Relationship attributes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Create user relationship response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `400` | Unknown `rel_kind` for the type or schema validation error | Confirm `rel_kind` is valid for the object type and `attributes` match the relationship schema. |
| `404` | Type or object not found | Confirm `type_name` and `external_id` both exist in the workspace. |
| `409` | Duplicate relationship (`duplicate-user-relationship`) | Use `PUT` to replace the existing relationship, or delete it before creating again. |
| `422` | Objects-per-user limit reached (`data-objects-per-user-limit-exceeded`) or users-per-object limit reached (`users-per-data-object-limit-exceeded`) | Reduce the relationship count for the user or the object, or contact Braze support about your workspace limits. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `data_objects.user_relationships.create` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Create user relationship errors" }
{% endapi %}
