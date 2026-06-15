---
nav_title: "GET: Liste angepasster Events exportieren"
article_title: "GET: Liste angepasster Events exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Liste angepasster Events exportieren“."

---
{% api %}
# Liste angepasster Events exportieren {#export-custom-events-list}
{% apimethod get %}
/events/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der angepassten Events zu exportieren, die für Ihre App aufgezeichnet wurden. Die Event-Namen werden in Gruppen von 250 zurückgegeben, alphabetisch sortiert.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `events.list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='events list' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | Die Seite der Event-Namen, die zurückgegeben werden soll. Standard ist 0 (gibt den ersten Satz von bis zu 250 zurück). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### Antwortcodes bei schwerwiegenden Fehlern {#fatal-export}

Informationen zu Statuscodes und zugehörigen Fehlermeldungen, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}