---
nav_title: "GET: View source translations for webhook template"
article_title: "GET: View source translations for webhook template"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "This article outlines details about the endpoint for viewing source translations for a webhook template."
---

{% api %}
# View source translations for a webhook template
{% apimethod get %}
/templates/webhook/translations/source
{% endapimethod %}

> Use this endpoint to view the default source translations for a [webhook template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). For more information about translation features, see [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with the `templates.translations.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Query parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `template_id` | Required | String | The ID of your webhook template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Query parameters" }

## Example request

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Replace *`TEMPLATE_ID`* with the ID of your webhook template.

## Response

There are five status code responses for this endpoint: `200`, `400`, `403`, `404`, and `429`.

### Example success response

The status code `200` could return the following response body.

```json
{
  "translations": {
    "translation_map": {
      "id_0": "Hello!",
      "id_1": "Would you like to buy this?"
    }
  }
}
```

### Example error response

The status code `400` could return the following response body.

```json
{
  "message": "This template does not have multi-language setup"
}
```

{% endapi %}
