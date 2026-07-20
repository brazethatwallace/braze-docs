---
nav_title: "DELETE: Mehrere Katalogartikel löschen"
article_title: "DELETE: Mehrere Katalogartikel löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Mehrere Katalogartikel löschen“."

---
{% api %}
# Mehrere Katalogartikel löschen {#delete-multiple-catalog-items}
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Artikel in Ihrem Katalog zu löschen.

Jede Anfrage kann bis zu 50 Artikel enthalten. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `catalogs.delete_items`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Pfad-Parameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfad-Parameter" }

## Anfrage-Parameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Ein Array, das Artikel-Objekte enthält. Die Artikel-Objekte sollten eine `id` enthalten, die auf die Artikel verweist, die Braze löschen soll. Es sind bis zu 50 Artikel-Objekte pro Anfrage zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrage-Parameter" }

## Beispielanfrage {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

## Antwort {#response}

Es gibt drei Statuscode-Antworten für diesen Endpunkt: `202`, `400` und `404`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `202` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
  "errors": [
    {
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request"
}
```

## Fehlerbehebung {#troubleshooting}

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlerbehebung |
| --- | --- |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `ids-too-large` | Artikel-IDs dürfen nicht mehr als 250 Zeichen lang sein. |
| `ids-not-unique` | Prüfen Sie, ob die Artikel-IDs in der Anfrage eindeutig sind. |
| `ids-not-strings` | Artikel-IDs müssen vom Typ String sein. |
| `items-missing-ids` | Einige Artikel haben keine Artikel-IDs. Prüfen Sie, ob jeder Artikel eine ID hat. |
| `invalid-ids` | Artikel-IDs dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| `request-includes-too-many-items` | Ihre Anfrage enthält zu viele Artikel. Die Anzahl der Artikel pro Anfrage ist auf 50 begrenzt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

{% endapi %}