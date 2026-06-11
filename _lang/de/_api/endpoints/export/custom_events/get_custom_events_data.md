---
nav_title: "GET: Angepasste Events exportieren"
article_title: "GET: Angepasste Events exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Braze-Endpunkt „Angepasste Events exportieren“."

---
{% api %}
# Angepasste Events exportieren {#export-custom-events}
{% apimethod get %}
/events
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der angepassten Events zu exportieren, die für Ihre App aufgezeichnet wurden. Die Events werden in Gruppen von 50, alphabetisch sortiert, zurückgegeben.

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `events.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='events' %}

## Abfrageparameter {#query-parameters}

Beachten Sie, dass jeder Aufruf dieses Endpunkts 50 Events zurückgibt. Bei mehr als 50 Events verwenden Sie den `Link`-Header, um die Daten auf der nächsten Seite abzurufen, wie in der folgenden Beispielantwort gezeigt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung der angepassten Events. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

## Beispielanfragen {#example-requests}

### Ohne Cursor {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### Antwortcodes bei schwerwiegenden Fehlern {#fatal-export}

Statuscodes und zugehörige Fehlermeldungen, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Schwerwiegende Fehler]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}