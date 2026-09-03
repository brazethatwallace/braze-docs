---
nav_title: "GET: View translations for webhook template"
article_title: "GET: View translations for webhook template"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "This article outlines details about the endpoint for viewing translations for a webhook template."
---

{% api %}
# View translations for a webhook template
{% apimethod get %}
/templates/webhook/translations
{% endapimethod %}

> Use this endpoint to view translations for a [webhook template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). You can return all configured locales or filter the response by locale. For more information about translation features, see [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Prerequisites

To use this endpoint, you'll need an [API key]({{site.baseurl}}/api/basics#rest-api-key-permissions) with the `templates.translations.get` permission.

## Rate limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Query parameters

| Parameter | Required | Data Type | Description |
| --- | --- | --- | --- |
| `template_id` | Required | String | The ID of your webhook template. |
| `locale_id` | Optional | String | The locale UUID to return. If omitted, the response includes all locales configured for the webhook template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Query parameters" }

## Example request

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Replace *`TEMPLATE_ID`* with the ID of your webhook template and *`LOCALE_ID`* with the UUID of the locale you want to return. Omit `locale_id` to return all configured locales.

## Response

There are five status code responses for this endpoint: `200`, `400`, `403`, `404`, and `429`.

### Example success response

The status code `200` could return the following response body.

```json
{
  "translations": [
    {
      "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "¿Te gustaría comprar esto?"
      },
      "locale": {
        "uuid": "c7c12345-de35-1234-5678-abcdefa99a3f",
        "name": "es-MX",
        "country": "MX",
        "language": "es",
        "locale_key": "es-mx"
      }
    },
    {
      "translation_map": {
        "id_0": "你好！",
        "id_1": "你想買這個嗎？"
      },
      "locale": {
        "uuid": "a1b12345-cd35-1234-5678-abcdefa99a3f",
        "name": "zh-HK",
        "country": "HK",
        "language": "zh",
        "locale_key": "zh-hk"
      }
    }
  ]
}
```

### Example error response

The status code `400` could return the following response body.

```json
{
  "message": "Invalid locale ID"
}
```

{% endapi %}
