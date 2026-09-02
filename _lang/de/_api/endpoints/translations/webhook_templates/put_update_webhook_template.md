---
nav_title: "PUT: Übersetzungen für Webhook-Template aktualisieren"
article_title: "PUT: Übersetzungen für Webhook-Template aktualisieren"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Aktualisieren von Übersetzungen für ein Webhook-Template."
---

{% api %}
# Übersetzungen für ein Webhook-Template aktualisieren {#update-translations-for-a-webhook-template}
{% apimethod put %}
/templates/webhook/translations
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Übersetzungen für ein [Webhook-Template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) zu aktualisieren. Weitere Informationen zu Übersetzungs-Features finden Sie unter [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `templates.translations.update`.

## Rate-Limits {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Pfadparameter {#path-parameters}

Für diesen Endpunkt gibt es keine Pfadparameter.

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `template_id` | Erforderlich | String | Die ID Ihres Webhook-Templates. |
| `locale_id` | Erforderlich | String | Die UUID der zu aktualisierenden Locale. Die Locale muss für das Webhook-Template konfiguriert sein. |
| `translation_map` | Erforderlich | Objekt | Ein Objekt, das die aktualisierten Übersetzungen enthält. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

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

## Antwort {#response}

Es gibt fünf Statuscode-Antworten für diesen Endpunkt: `200`, `400`, `403`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` gibt den folgenden leeren Antwortkörper zurück.

```json
{}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "Locale not found"
}
```

{% endapi %}