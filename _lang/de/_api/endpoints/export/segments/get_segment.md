---
nav_title: "GET: Liste der Segmente exportieren"
article_title: "GET: Liste der Segmente exportieren"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Liste der Segmente exportieren“."

---
{% api %}
# Liste der Segmente exportieren {#export-segment-list}
{% apimethod get %}
/segments/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste von Segmenten zu exportieren, die jeweils den Namen, den Segment-API-Bezeichner und die Angabe, ob Analytics-Tracking aktiviert ist, enthalten.

Die Segmente werden in Gruppen von 100 zurückgegeben, sortiert nach dem Zeitpunkt der Erstellung (standardmäßig vom ältesten zum neuesten). Archivierte Segmente sind nicht enthalten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `segments.list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | Die Seite der zurückzugebenden Segmente, Standardwert ist 0 (gibt den ersten Satz von bis zu 100 zurück). |
| `sort_direction` | Optional | String | - Erstellungszeit vom neuesten zum ältesten sortieren: Geben Sie den Wert `desc` an.<br> - Erstellungszeit vom ältesten zum neuesten sortieren: Geben Sie den Wert `asc` an. <br><br>Wenn `sort_direction` nicht angegeben ist, ist die Standardreihenfolge vom ältesten zum neuesten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}