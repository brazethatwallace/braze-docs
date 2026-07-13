---
nav_title: "GET: Umsatzdaten exportieren"
article_title: "GET: Umsatzdaten exportieren"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Exportieren von Umsatzdaten."

---
{% api %}
# Umsatzdaten nach Zeit exportieren {#export-revenue-data-by-time}
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Gesamtausgaben in Ihrer App über einen bestimmten Zeitraum abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `purchases.revenue_series`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `ending_at` | Optional | Datetime ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Datum, an dem der Datenexport enden soll. Standardmäßig wird der Zeitpunkt der Anfrage verwendet. |
| `length` | Erforderlich | Integer | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Serie enthalten sein sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann Tag oder Stunde sein, Standardeinstellung ist Tag. |
| `app_id` | Optional | String | API-Bezeichner der App, abgerufen von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Wenn nicht angegeben, werden die Ergebnisse für alle Apps in einem Workspace zurückgegeben. |
| `product` | Optional | String | Name des Produkts, nach dem die Antwort gefiltert werden soll. Wenn nicht angegeben, werden die Ergebnisse für alle Apps zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/revenue_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

```json
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "revenue" : (int) amount of revenue for the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}