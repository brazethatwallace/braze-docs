---
nav_title: "DELETE: Katalog löschen"
article_title: "DELETE: Katalog löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Katalog löschen“."

---
{% api %}
# Katalog löschen {#delete-catalog}
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Katalog zu löschen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.delete`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Pfadparameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter" }

## Beispielanfrage {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Antwort {#response}

Für diesen Endpunkt gibt es zwei Statuscode-Antworten: `200` und `404`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antworttext zurückgeben:

```json
{
  "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `404` könnte den folgenden Antworttext zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

{% endapi %}