---
nav_title: "POST: Duplicate campaigns"
article_title: "POST: Duplicate Campaigns"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "This article outlines details about the Duplicate campaigns endpoint."

---
{% api %}
# Duplicate campaigns using the API
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Use this endpoint to duplicate campaigns. This API endpoint is similar to [duplicating campaigns in the Braze dashboard]({{site.baseurl}}/user_guide/messaging/governance/duplicating).

## Prerequisites

To use this endpoint, you'll need to generate an API key with the `campaigns.duplicate` permission.

## Rate limit

This endpoint is limited to 100 API calls per minute.

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
  "tag_names": (optional, array of strings) The tags of the resulting campaign,
}
```

## Request parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Required | String | See [campaign identifier]({{site.baseurl}}/api/identifier_types). |
|`name`| Required | String | The name of the resulting campaign. |
|`description`| Optional | String | The description field for the resulting campaign. |
|`tag_names` | Optional | Array of strings | The tags for the resulting campaign. These must be existing tags. If you add new tags in the request, they overwrite any tags that were on the original campaign. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }


## Response

This endpoint returns a `202` status code, and the campaign creation occurs asynchronously. You can use the [security event download]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report) to see records of when campaigns were duplicated and by which API key.

{% endapi %}
