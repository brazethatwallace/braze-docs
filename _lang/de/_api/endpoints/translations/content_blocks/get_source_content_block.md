---
nav_title: "GET: Standard-Quellwerte für Übersetzungs-Tags von Content-Blöcken anzeigen"
article_title: "GET: Standard-Quellwerte für Übersetzungs-Tags von Content-Blöcken anzeigen"
search_tag: Endpoint
page_order: 0

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt für Übersetzungsquellen von Content-Blöcken."
---

{% api %}
# Standard-Quellwerte für Übersetzungs-Tags eines Content-Blocks anzeigen {#view-default-source-values-for-a-content-blocks-translation-tags}
{% apimethod get %}
/content_blocks/translations/source
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Standard-Übersetzungsquellen für die Übersetzungs-Tags eines Content-Blocks anzuzeigen. Dies sind die Werte innerhalb von {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Weitere Informationen zu Übersetzungsfunktionen finden Sie unter [Lokalisierungen in Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `content_blocks.translations.get`.

## Rate-Limits {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter {#query-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Erforderlich | String | Die ID Ihres Content-Blocks. |
| `locale_id` | Optional | String | Eine Locale-UUID zum Filtern der Antworten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universell eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations/source?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

Für diesen Endpunkt gibt es vier Statuscode-Antworten: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwort-Header und -Body zurückgeben.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Welcome!",
           "id_1": "Thank you for joining our program"
       }
   },
   "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antwort-Body zurückgeben. Weitere Informationen zu möglichen Fehlern finden Sie unter [Fehlerbehebung](#troubleshooting).

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}