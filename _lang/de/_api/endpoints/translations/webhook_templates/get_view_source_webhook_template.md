---
nav_title: "GET: Quellübersetzungen für Webhook-Template anzeigen"
article_title: "GET: Quellübersetzungen für Webhook-Template anzeigen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Anzeigen von Quellübersetzungen für ein Webhook-Template."
---

{% api %}
# Quellübersetzungen für ein Webhook-Template anzeigen {#view-source-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations/source
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die standardmäßigen Quellübersetzungen für ein [Webhook-Template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) anzuzeigen. Weitere Informationen zu Übersetzungsfunktionen finden Sie unter [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `templates.translations.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter {#query-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `template_id` | Erforderlich | String | Die ID Ihres Webhook-Templates. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

## Beispielanfrage {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Ersetzen Sie *`TEMPLATE_ID`* durch die ID Ihres Webhook-Templates.

## Antwort {#response}

Es gibt fünf Statuscode-Antworten für diesen Endpunkt: `200`, `400`, `403`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antworttext zurückgeben.

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

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben.

```json
{
  "message": "This template does not have multi-language setup"
}
```

{% endapi %}