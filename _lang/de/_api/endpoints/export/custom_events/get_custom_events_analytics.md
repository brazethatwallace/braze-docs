---
nav_title: "GET: Analytics angepasster Events exportieren"
article_title: "GET: Analytics angepasster Events exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Analytics angepasster Events exportieren“."

---
{% api %}
# Analytics angepasster Events exportieren {#export-custom-events-analytics}
{% apimethod get %}
/events/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Reihe der Anzahl von Vorkommen eines angepassten Events in Ihrer App über einen bestimmten Zeitraum abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `events.data_series`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `event` | Erforderlich | String | Der Name des angepassten Events, für das Analytics zurückgegeben werden sollen. |
| `length` | Erforderlich | Integer | Maximale Anzahl der Einheiten (Tage oder Stunden) vor `ending_at`, die in die zurückgegebene Reihe aufgenommen werden sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann `day` oder `hour` sein, Standard ist `day`. |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird der Zeitpunkt der Anfrage verwendet. |
| `app_id` | Optional | String | App-API-Bezeichner, der von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) abgerufen wird, um Analytics auf eine bestimmte App zu beschränken. |
| `segment_id` | Optional | String | Siehe [Segment-API-Bezeichner]({{site.baseurl}}/api/identifier_types). Segment-ID, die das Analytics-aktivierte Segment angibt, für das Event-Analytics zurückgegeben werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }


## Beispielanfrage {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "data" : [
        {
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int) the number of occurrences of provided custom event
        },
        ...
    ]
}
```

### Antwortcodes bei schwerwiegenden Fehlern {#fatal-export}

Statuscodes und zugehörige Fehlermeldungen, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors#fatal-errors).

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}