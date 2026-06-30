---
nav_title: "POST: Katalogauswahl erstellen"
article_title: "POST: Katalogauswahl erstellen"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Katalogauswahl erstellen“."

---
{% api %}
# Katalogauswahl erstellen {#create-catalog-selection}
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Auswahl in Ihrem Katalog zu erstellen.

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `catalogs.create_selection`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Pfad-Parameter {#path-parameters}

| Parameter      | Erforderlich | Datentyp | Beschreibung          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Erforderlich | String    | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Anfrage-Parameter {#request-parameters}

| Parameter   | Erforderlich | Datentyp | Beschreibung                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Erforderlich | Objekt    | Ein Objekt, das Auswahlkriterien enthält. Eine vollständige Aufschlüsselung des Objekts und seiner Felder finden Sie unter [Katalogauswahl-Objekt]({{site.baseurl}}/api/objects_filters/catalog_selection_object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Parameter des Auswahlobjekts {#selection-object-parameters}

| Parameter        | Erforderlich | Datentyp | Beschreibung                                                                                                                                                        |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`           | Erforderlich | String    | Der Name der Katalogauswahl. |
| `description`    | Optional | String    | Eine Beschreibung der Katalogauswahl. |
| `external_id`    | Erforderlich | String    | Ein eindeutiger Bezeichner für die Auswahl. |
| `source`         | Erforderlich | String    | Die Quelle der Katalogdaten. Für Shopify-Kataloge verwenden Sie `"Shopify"`. Für angepasste Kataloge verwenden Sie `"custom"`. |
| `filters`        | Optional | Array    | Ein Array von Filterobjekten, die auf die Katalogartikel angewendet werden sollen. Sie können bis zu vier Filter pro Anfrage angeben. Wenn keine Filter angegeben werden, werden alle Artikel aus dem Katalog einbezogen. |
| `results_limit`  | Optional | Integer   | Die maximale Anzahl der zurückzugebenden Ergebnisse. Es muss sich um eine Zahl zwischen 1 und 50 handeln. |
| `sort_field`     | Optional | String    | Das Feld, nach dem die Ergebnisse sortiert werden sollen. Dies muss zusammen mit `sort_order` verwendet werden. Wenn weder `sort_field` noch `sort_order` vorhanden sind, werden die Ergebnisse in zufälliger Reihenfolge zurückgegeben. |
| `sort_order`     | Optional | String    | Die Reihenfolge, in der die Ergebnisse sortiert werden sollen. Zulässige Werte sind `"asc"` (aufsteigend) oder `"desc"` (absteigend). Dies muss zusammen mit `sort_field` verwendet werden. Wenn weder `sort_field` noch `sort_order` vorhanden sind, werden die Ergebnisse in zufälliger Reihenfolge zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Die Parameter `sort_field` und `sort_order` müssen zusammen verwendet werden. Wenn Sie nur einen der beiden Parameter angeben oder beide Parameter weglassen, werden die Auswahlergebnisse in zufälliger Reihenfolge zurückgegeben.
{% endalert %}

## Beispielanfrage {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "custom",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
  }
}'
```

### Filteroperatoren {#filter-operators}

| Feldtyp | Unterstützte Operatoren                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
| `geo`      | `geo within`, `geo outside`                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Die API unterstützt maximal vier Filter pro Auswahlanfrage. Im Braze-Dashboard können Sie bis zu 10 Filter pro Auswahl hinzufügen. Filter werden in der Reihenfolge angewendet, in der sie im Array erscheinen.
{% endalert %}

{% alert note %}
Wenn Sie einen `geo`-Filter anwenden, sortiert das System die Ergebnisse automatisch nach Entfernung, wobei das nächstgelegene Element zuerst angezeigt wird – unabhängig von den Parametern `sort_field` und `sort_order`.
{% endalert %}

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

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die auftreten können.

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

In der folgenden Tabelle finden Sie mögliche zurückgegebene Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler                                | Fehlerbehebung                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Prüfen Sie, ob der Katalogname gültig ist.                                                         |
| `company-size-limit-already-reached` | Das Limit für die Katalogspeichergröße ist erreicht.                                                    |
| `selection-limit-reached`            | Das Limit für die Katalogauswahl ist erreicht.                                                      |
| `invalid-selection`                  | Prüfen Sie, ob die Auswahl gültig ist.                                                            |
| `too-many-filters`                   | Prüfen Sie, ob die Auswahl zu viele Filter enthält.                                                  |
| `selection-name-already-exists`      | Prüfen Sie, ob der Name der Auswahl bereits im Katalog vorhanden ist.                                    |
| `selection-has-invalid-filter`       | Prüfen Sie, ob der Auswahlfilter gültig ist.                                                       |
| `selection-invalid-results-limit`    | Prüfen Sie, ob das Ergebnislimit der Auswahl gültig ist.                                                |
| `invalid-sorting`                    | Prüfen Sie, ob die Auswahlsortierung gültig ist.                                                      |
| `invalid-sort-field`                 | Prüfen Sie, ob das Sortierfeld der Auswahl gültig ist.                                                   |
| `invalid-sort-order`                 | Prüfen Sie, ob die Sortierreihenfolge der Auswahl gültig ist.                                                   |
| `selection-contains-too-many-arrays` | Prüfen Sie, ob die Auswahl mehr als ein Feld mit dem Typ `array` enthält. Es wird nur eines unterstützt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}