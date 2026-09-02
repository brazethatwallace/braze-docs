---
nav_title: "PUT: Übersetzung in einem Content-Block Update or aktualisieren or aktualisieren"
article_title: "PUT: Übersetzung in einem Content-Block Update or aktualisieren or aktualisieren"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt „Übersetzung in einem Content-Block Update or aktualisieren or aktualisieren“."
---

{% api %}
# Übersetzung in einem Content-Block Update or aktualisieren or aktualisieren {#update-translation-in-a-content-block}
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Übersetzungen für einen [Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) zu Update or aktualisieren or aktualisieren. Weitere Informationen zu den Übersetzungsfeatures finden Sie unter [Locales in Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `content_blocks.translations.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Pfadparameter {#path-parameters}

Für diesen Endpunkt gibt es keine Pfadparameter.

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Erforderlich | String | Die ID Ihres Content-Blocks. |
| `locale_id` | Erforderlich | String | Die ID (UUID) der Locale. |
| `translation_map` | Erforderlich | Objekt | Objekt, das die neuen Übersetzungen enthält. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universelle eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispielanfrage {#example-request}

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
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
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}