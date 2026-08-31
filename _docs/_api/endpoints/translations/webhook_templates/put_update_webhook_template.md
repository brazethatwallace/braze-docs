---
nav_title: "PUT: Update translations for webhook template"
article_title: "PUT: Update translations for webhook template"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "This article outlines details about the endpoint for updating translations for a webhook template."
---

{% api %}
# Update translations for a webhook template
{% apimethod put %}
/templates/webhook/translations
{% endapimethod %}

> Use this endpoint to update translations for a [webhook template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). For more information about translation features, see [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with the `templates.translations.update` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Path parameters

There are no path parameters for this endpoint.

## Request parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `template_id` | Required | String | The ID of your webhook template. |
| `locale_id` | Required | String | The UUID of the locale to update. The locale must be configured for the webhook template. |
| `translation_map` | Required | Object | An object containing the updated translations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Example request

```bash
curl --location --request PUT 'https://rest.iad-03.braze.com/templates/webhook/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
  "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
  "translation_map": {
    "id_0": "¡Hola!",
    "id_1": "¿Te gustaría comprar esto?"
  }
}'
```

## Response

There are five status code responses for this endpoint: `200`, `400`, `403`, `404`, and `429`.

### Example success response

The status code `200` returns the following empty response body.

```json
{}
```

### Example error response

The status code `400` could return the following response body.

```json
{
  "message": "Locale not found"
}
```

{% endapi %}
