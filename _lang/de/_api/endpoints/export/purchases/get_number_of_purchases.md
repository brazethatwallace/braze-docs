---
nav_title: "GET: Anzahl der Käufe exportieren"
article_title: "GET: Anzahl der Käufe exportieren"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Exportieren der Anzahl von Käufen."

---
{% api %}
# Anzahl der Käufe exportieren {#export-number-of-purchases}
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Gesamtzahl der Käufe in Ihrer App über einen bestimmten Zeitraum zurückzugeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `purchases.quantity_series`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `ending_at` | Optional | Datetime ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Datum, an dem der Datenexport enden soll. Standardmäßig wird der Zeitpunkt der Anfrage verwendet. |
| `length` | Erforderlich | Integer | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Serie enthalten sein sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann Tag oder Stunde sein, Standardeinstellung ist Tag. |
| `app_id` | Optional | String | App-API-Bezeichner, der auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) abgerufen wird. Wenn nicht angegeben, werden die Ergebnisse für alle Apps in einem Workspace zurückgegeben. |
| `product` | Optional | String | Name des Produkts, nach dem die Antwort gefiltert werden soll. Wenn nicht angegeben, werden die Ergebnisse für alle Apps zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

```json
{
  "message": (string) returns 'success' when the request completes without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}