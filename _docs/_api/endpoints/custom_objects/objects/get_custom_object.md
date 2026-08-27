---
nav_title: "GET: Get custom object"
article_title: "GET: Get Custom Object"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "This article outlines details about the Get custom object endpoint."
---
{% api %}
# Get custom object
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use this endpoint to return one custom object.

{% alert important %}
Custom Objects is currently in early access. Your workspace must be enabled before the Custom Objects API key permissions appear on **Settings** > **API Keys**.
{% endalert %}

## Prerequisites

To use this endpoint, you need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with `custom_objects.read`.

## Rate limit

This endpoint is in the Custom Objects read bucket with a default limit of 50 requests per minute.

## Path parameters

The following table lists and describes the path parameters for the `/custom_objects/objects/{type_name}/{external_id}` endpoint.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `type_name` | Required | String | Custom object type machine name |
| `external_id` | Required | String | Object identifier |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Get custom object path parameters" }

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

This example retrieves the `acct-123` account record and its stored attributes.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Response

This section includes a sample successful response and the response fields.

### Example success response

The status code `200` could return the following response body.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "industry": "software" }
  }
}
```

### Response parameters

The following table lists and describes the fields in a successful response.

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `custom_object` | Required | Object | Returned custom object record |
| `custom_object.type_name` | Required | String | Custom object type machine name |
| `custom_object.external_id` | Required | String | Custom object identifier |
| `custom_object.attributes` | Required | Object | Object attributes keyed by field name |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Get custom object response parameters" }

## Errors

The following table lists common errors for this endpoint and how to resolve them.

| Status | Cause | Guidance |
|---|---|---|
| `404` | Type not found (`custom-object-type-not-found`) or object not found (`custom-object-not-found`) | Confirm `type_name` and `external_id` both exist in the workspace. |
| `401` | Missing or invalid REST API key | Verify the `Authorization` header uses `Bearer YOUR_REST_API_KEY` and that the key is active. |
| `403` | API key lacks permission or request is blocked by allowlist | Confirm the key has `custom_objects.read` and that your source IP is on the key allowlist, if configured. |
| `429` | Rate limit exceeded | Retry after `X-RateLimit-Reset` and reduce request frequency. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Get custom object errors" }
{% endapi %}
