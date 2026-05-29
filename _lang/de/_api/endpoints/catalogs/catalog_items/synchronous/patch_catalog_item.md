---
nav_title: "PATCH: Katalogartikel bearbeiten"
article_title: "PATCH: Katalogartikel bearbeiten"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Katalogartikel bearbeiten“."

---
{% api %}
# Katalogartikel bearbeiten {#edit-catalog-item}
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen bestehenden Artikel in Ihrem Katalog zu bearbeiten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.update_item`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Pfad-Parameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `catalog_name` | Erforderlich | String | Name des Katalogs. |
| `item_id` | Erforderlich | String | Die ID des Katalogartikels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Anfrage-Parameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Ein Array, das Artikel-Objekte enthält. Die Artikel-Objekte sollten Felder enthalten, die im Katalog vorhanden sind, mit Ausnahme des Feldes `id`. Pro Anfrage ist nur ein Artikel-Objekt zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Beispielanfrage {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
- Das Feld `Location` verwendet den Datentyp `geo`, der ein Array im Format `[longitude, latitude]` erwartet.
- Die Operatoren `$add` und `$remove` sind nur auf Felder vom Typ Array anwendbar und werden nur von PATCH-Endpunkten unterstützt.
{% endalert %}

## Antwort {#response}

Es gibt drei Statuscode-Antworten für diesen Endpunkt: `200`, `400` und `404`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antworttext zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `arbitrary-error` | Es ist ein unerwarteter Fehler aufgetreten. Bitte versuchen Sie es erneut oder kontaktieren Sie den [Support]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `filtered-set-field-too-long` | Der Feldwert wird in einer gefilterten Menge verwendet, die die Zeichengrenze für einen Artikel überschreitet. |
| `id-in-body` | Eine Artikel-ID existiert bereits im Katalog. |
| `ids-too-large` | Die Zeichenbegrenzung für jede Artikel-ID beträgt 250 Zeichen. |
| `invalid-ids` | Unterstützte Zeichen für Artikel-ID-Namen sind Buchstaben, Zahlen, Bindestriche und Unterstriche. |
| `invalid-fields` | Bestätigen Sie, dass die Felder in der Anfrage im Katalog vorhanden sind. |
| `invalid-keys-in-value-object` | Artikel-Objektschlüssel dürfen weder `.` noch `$` enthalten. |
| `item-not-found` | Prüfen Sie, ob der Artikel im Katalog enthalten ist. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-too-large` | Das Zeichenlimit für jeden Artikel beträgt 5.000 Zeichen. |
| `request-includes-too-many-items` | Sie können pro Anfrage nur einen Katalogartikel bearbeiten. |
| `too-deep-nesting-in-value-object` | Artikel-Objekte dürfen nicht mehr als 50 Verschachtelungsebenen haben. |
| `unable-to-coerce-value` | Artikeltypen können nicht konvertiert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}