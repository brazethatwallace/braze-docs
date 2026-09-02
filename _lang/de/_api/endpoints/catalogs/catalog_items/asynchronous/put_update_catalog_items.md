---
nav_title: "PUT: Mehrere Katalogartikel ersetzen"
article_title: "PUT: Mehrere Katalogartikel ersetzen"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Mehrere Katalogartikel ersetzen“."

---
{% api %}
# Katalogartikel ersetzen {#replace-catalog-items}
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Artikel in Ihrem Katalog zu ersetzen.

Wenn ein Katalogartikel nicht vorhanden ist, erstellt dieser Endpunkt den Artikel in Ihrem Katalog. Jede Anfrage kann bis zu 50 Katalogartikel unterstützen. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `catalogs.replace_items`.

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
| `items` | Erforderlich | Array | Ein Array, das Artikelobjekte enthält. Jedes Objekt muss eine ID haben. Die Artikelobjekte sollten Felder enthalten, die im Katalog vorhanden sind. Pro Anfrage sind bis zu 50 Artikelobjekte zulässig. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrage-Parameter" }

## Beispielanfrage {#example-request}

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

{% alert note %}
Das Feld `Location` verwendet den Datentyp `geo`, der ein Array im Format `[longitude, latitude]` erwartet.
{% endalert %}

## Antwort {#response}

Es gibt drei Statuscode-Antworten für diesen Endpunkt: `202`, `400` und `404`.

{% alert note %}
Das System kann auch eine `400`-Antwort zurückgeben, wenn Ihr Unternehmen das Speicherlimit für Kataloge erreicht hat. Die kostenlose Version der Kataloge ist auf 500&nbsp;MB begrenzt. Weitere Informationen zu Speicherstufen und zum Upgrade finden Sie unter [Datenspeicherbeschränkungen]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations).
{% endalert %}

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

In der folgenden Tabelle finden Sie mögliche zurückgegebene Fehler und die zugehörigen Schritte zur Fehlerbehebung.

| Fehler | Fehlerbehebung |
| --- | --- |
| `catalog-not-found` | Prüfen Sie, ob der Katalogname gültig ist. |
| `company-size-limit-already-reached` | Das Speicherlimit für Kataloge ist erreicht. Weitere Informationen zu Speicherstufen finden Sie unter [Datenspeicherbeschränkungen]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `company-size-limit-surge` | Die Anfrage überschreitet den verbleibenden Katalogspeicher Ihres Unternehmens. Versuchen Sie es erneut mit einem kleineren Update. Weitere Informationen zu Speicherstufen finden Sie unter [Datenspeicherbeschränkungen]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `ids-not-string` | Bestätigen Sie, dass jede Artikel-ID ein String ist. |
| `ids-not-unique` | Prüfen Sie, ob jede Artikel-ID eindeutig ist. |
| `ids-too-large` | Die Zeichenbegrenzung für jede Artikel-ID beträgt 250 Zeichen. |
| `item-array-invalid` | `items` muss ein Array von Objekten sein. |
| `items-missing-ids` | Einige Artikel haben keine Artikel-IDs. Bestätigen Sie, dass jeder Artikel eine ID hat. |
| `items-too-large` | Artikelwerte dürfen 5.000 Zeichen nicht überschreiten. |
| `invalid-ids` | Unterstützte Zeichen für Artikel-ID-Namen sind Buchstaben, Zahlen, Bindestriche und Unterstriche. |
| `invalid-fields` | Stellen Sie sicher, dass alle Felder, die Sie in der API-Anfrage senden, bereits im Katalog vorhanden sind. Dies bezieht sich nicht auf das in der Fehlermeldung erwähnte ID-Feld. |
| `invalid-keys-in-value-object` | Artikelobjekt-Schlüssel dürfen nicht `.` oder `$` enthalten. |
| `too-deep-nesting-in-value-object` | Artikelobjekte dürfen nicht mehr als 50 Verschachtelungsebenen haben. |
| `request-includes-too-many-items` | Ihre Anfrage enthält zu viele Artikel. Das Limit pro Anfrage beträgt 50 Artikel. |
| `unable-to-coerce-value` | Artikeltypen können nicht konvertiert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

{% endapi %}