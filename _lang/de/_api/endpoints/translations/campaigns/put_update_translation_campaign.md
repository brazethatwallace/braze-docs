---
nav_title: "PUT: Übersetzung in einer Campaign aktualisieren"
article_title: "PUT: Übersetzung in einer Campaign aktualisieren"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "In diesem Artikel erfahren Sie mehr über den Endpunkt „Übersetzung in einer Campaign aktualisieren“."
---

{% api %}
# Übersetzung in einer Campaign aktualisieren {#update-translation-in-a-campaign}
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Übersetzungen für eine Campaign zu aktualisieren. Weitere Informationen zu den Übersetzungsfeatures finden Sie unter [Locales in Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

Wenn Sie Übersetzungen aktualisieren möchten, nachdem eine Campaign gestartet wurde, müssen Sie zunächst [Ihre Nachricht als Entwurf speichern]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `campaigns.translations.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Pfadparameter {#path-parameters}

Für diesen Endpunkt gibt es keine Pfadparameter.

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Die ID Ihrer Campaign. |
| `message_variation_id` | Erforderlich | String | Die ID Ihrer Nachrichtenvariante. |
| `locale_id` | Erforderlich | String | Die ID (UUID) des Locale. |
| `translation_map` | Erforderlich | Objekt | Objekt, das die neuen Übersetzungen enthält. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universelle eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispielanfrage {#example-request}

```json
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
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