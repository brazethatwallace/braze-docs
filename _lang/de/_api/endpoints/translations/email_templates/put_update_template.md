---
nav_title: "PUT: Update der Übersetzungen für ein E-Mail-Template"
article_title: "PUT: Übersetzungen für ein E-Mail-Template aktualisieren"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts „Übersetzungen für ein E-Mail-Template aktualisieren“."
---

{% api %}
# Übersetzungen für ein E-Mail-Template aktualisieren {#update-translations-for-an-email-template}
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Übersetzungen für ein [E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates) zu aktualisieren. Weitere Informationen zu den Übersetzungsfeatures finden Sie unter [Locales in Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `templates.translations.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Pfadparameter {#path-parameters}

Für diesen Endpunkt gibt es keine Pfadparameter.

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `template_id` | Erforderlich | String | Die ID Ihres E-Mail-Templates. |
| `locale_id` | Erforderlich | String | Die ID des Gebietsschemas. |
| `translations_map` | Erforderlich | String | Die Zuordnung der Übersetzungen für Ihr E-Mail-Template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universelle eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispielanfrage {#example-request}

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
    }
}
```

## Antwort {#response}

Es gibt vier Statuscode-Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

```json
{
    "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
	"errors": [
		{
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}