---
nav_title: "POST: Duplicate Canvases"
article_title: "POST: Duplicate Canvases"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "This article outlines details about the Duplicate Canvases endpoint."
---

{% api %}
# Duplicate Canvases using the API
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Use this endpoint to duplicate Canvases. This API endpoint is similar to [duplicating Canvases in the Braze dashboard]({{site.baseurl}}/user_guide/messaging/governance/duplicating).

## Prerequisites

To use this endpoint, you must generate an API key with the `canvas.duplicate` permission.

## Rate limit

This endpoint is limited to 100 API calls per minute.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, array of strings) The tags of the resulting Canvas,
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Required | String | See [Canvas identifier]({{site.baseurl}}/api/identifier_types). |
|`name`| Required | String | The name of the resulting Canvas. |
|`description`| Optional | String | The description field for the resulting Canvas. |
|`tag_names` | Optional | Array of strings | The tags for the resulting Canvas. These must be existing tags. If you add new tags in the request, they overwrite any tags that were on the original Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## Response

This endpoint returns a `202` status code, and the Canvas creation occurs asynchronously. You can use the [security event download]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report) to see records of when Canvases were duplicated and by which API key.

{% endapi %}
