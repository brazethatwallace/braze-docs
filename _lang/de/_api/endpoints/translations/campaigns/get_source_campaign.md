---
nav_title: "GET: Standardquellwerte für Campaign-Übersetzungs-Tags anzeigen"
article_title: "GET: Standardquellwerte für Campaign-Übersetzungs-Tags anzeigen"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel enthält detaillierte Informationen zum Endpunkt für die Übersetzungsquelle von Campaigns."
---

{% api %}
# Standardquellwerte für die Übersetzungs-Tags einer Campaign anzeigen {#view-default-source-values-for-a-campaigns-translation-tags}
{% apimethod get %}
/campaigns/translations/source
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Standardübersetzungsquellen für die Übersetzungs-Tags einer Campaign anzuzeigen. Dies sind die Werte innerhalb von {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Weitere Informationen zu den Übersetzungs-Features finden Sie unter [Locales in Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `campaigns.translations.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter {#query-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Die ID Ihrer Campaign. |
| `message_variation_id` | Erforderlich | String | Die ID Ihrer Nachrichtenvariante. |
| `locale_id` | Optional | String | Eine Locale-UUID zum Filtern der Antworten. |
| `post_launch_draft_version` | Optional | Boolescher Wert | Wenn `true`, wird die neueste Entwurfsversion anstelle der zuletzt veröffentlichten Live-Version zurückgegeben. Standardmäßig `false`, wodurch die aktuellste Live-Version zurückgegeben wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Abfrageparameter" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universelle eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

Es gibt vier Statuscode-Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwort-Header und -Body zurückgeben.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
       }
   },
   "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antwort-Body zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu möglichen Fehlern.

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