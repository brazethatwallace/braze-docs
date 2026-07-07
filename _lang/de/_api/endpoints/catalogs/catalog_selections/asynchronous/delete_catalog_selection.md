---
nav_title: "DELETE: Katalogauswahl löschen"
article_title: "DELETE: Katalogauswahl löschen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Katalogauswahl löschen“."

---
{% api %}
# Katalogauswahl löschen {#delete-catalog-selection}
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Katalogauswahl zu löschen.

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `catalogs.delete_selection`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Pfadparameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| ---------------- | -------- | --------- | ------------------------------ |
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
| `selection_name` | Erforderlich | String | Name der Katalogauswahl. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter" }

## Beispielanfrage {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Antwort {#response}

Für diesen Endpunkt gibt es zwei Statuscode-Antworten: `202` und `404`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `202` könnte folgenden Antworttext zurückgeben:

```json
{
  "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `404` könnte folgenden Antworttext zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

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
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `invalid-selection` | Prüfen Sie, ob der Auswahlname gültig ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

{% endapi %}