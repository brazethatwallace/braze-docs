---
nav_title: "GET: Canvas-Liste exportieren"
article_title: "GET: Canvas-Liste exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Canvas-Liste exportieren“."

---
{% api %}
# Canvas-Liste exportieren {#export-canvas-list}
{% apimethod get %}
/canvas/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste von Canvases zu exportieren, einschließlich des Namens, des Canvas-API-Bezeichners und der zugehörigen Tags.

Canvases werden in Gruppen von 100 zurückgegeben, sortiert nach dem Zeitpunkt der Erstellung (standardmäßig vom ältesten zum neuesten).

Archivierte Canvases werden nicht in die API-Antwort aufgenommen, es sei denn, das Feld `include_archived` ist angegeben. Canvases, die angehalten, aber nicht archiviert wurden, werden jedoch standardmäßig zurückgegeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `canvas.list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | Die Seite der Canvases, die zurückgegeben werden soll. Standard ist `0` (gibt den ersten Satz von bis zu 100 zurück). |
| `include_archived` | Optional | Boolescher Wert | Ob archivierte Canvases einbezogen werden sollen oder nicht. Standard ist `false`. |
| `sort_direction` | Optional | String | - Erstellungszeit vom neuesten zum ältesten sortieren: Geben Sie den Wert `desc` ein.<br> - Erstellungszeit vom ältesten zum neuesten sortieren: Geben Sie den Wert `asc` ein. <br><br>Wenn `sort_direction` nicht angegeben ist, ist die Standardreihenfolge vom ältesten zum neuesten. |
| `last_edit.time[gt]` | Optional | Zeit | Filtert die Ergebnisse und gibt nur Canvases zurück, die nach dem angegebenen Zeitpunkt bearbeitet wurden. Das Format ist `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

```json
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}