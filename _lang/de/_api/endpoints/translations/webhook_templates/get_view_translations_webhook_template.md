---
nav_title: "GET: Übersetzungen für Webhook-Template anzeigen"
article_title: "GET: Übersetzungen für Webhook-Template anzeigen"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Anzeigen von Übersetzungen für ein Webhook-Template."
---

{% api %}
# Übersetzungen für ein Webhook-Template anzeigen {#view-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Übersetzungen für ein [Webhook-Template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) anzuzeigen. Sie können alle konfigurierten Sprachen zurückgeben oder die Antwort nach Sprache filtern. Weitere Informationen zu Übersetzungsfunktionen finden Sie unter [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `templates.translations.get`.

## Rate-Limits {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter {#query-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `template_id` | Erforderlich | String | Die ID Ihres Webhook-Templates. |
| `locale_id` | Optional | String | Die UUID der Sprache, die zurückgegeben werden soll. Wenn dieser Parameter weggelassen wird, enthält die Antwort alle für das Webhook-Template konfigurierten Sprachen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

## Beispielanfrage {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Ersetzen Sie *`TEMPLATE_ID`* durch die ID Ihres Webhook-Templates und *`LOCALE_ID`* durch die UUID der Sprache, die Sie zurückgeben möchten. Lassen Sie `locale_id` weg, um alle konfigurierten Sprachen zurückzugeben.

## Antwort {#response}

Für diesen Endpunkt gibt es fünf Statuscode-Antworten: `200`, `400`, `403`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antworttext zurückgeben.

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

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben.

```json
{
  "message": "Invalid locale ID"
}
```

{% endapi %}