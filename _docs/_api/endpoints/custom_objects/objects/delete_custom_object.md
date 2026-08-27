---
nav_title: "DELETE: Delete custom object"
article_title: "DELETE: Delete Custom Object"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "This article outlines details about the Delete custom object endpoint."
---
{% api %}
# Delete custom object
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use this endpoint to delete one custom object.

{% alert important %}
Custom Objects is currently in early access. Your workspace must be enabled before the Custom Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `custom_objects.delete`.

## Rate limit

This endpoint is in the Custom Objects write bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/custom_objects/objects/{type_name}/{external_id}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Custom object type machine name |
| `external_id` | Required | String | Object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Delete custom object path parameters" }

## Example request

This section includes a sample path-parameter payload and a sample cURL request.

### Sample request payload

Use this JSON object as a reference for the path parameters in this request.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### Sample cURL request

This example deletes the `acct-123` account record.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `200` could return the following response body.

```json
{ "deleted": true }
```

The delete is synchronous. Deleting one object does not delete related objects.

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `deleted` | Required | Boolean | Whether the object deletion succeeded |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Delete custom object response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `404` | Type not found or object not found | Confirm `type_name` and `external_id` both exist in the workspace. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `custom_objects.delete` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Delete custom object errors" }
{% endapi %}
