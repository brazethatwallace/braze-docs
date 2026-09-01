---
nav_title: "GET: Angepasste Objekte auflisten"
article_title: "GET: Angepasste Objekte auflisten"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Angepasste Objekte auflisten“."
---
{% api %}
# Angepasste Objekte auflisten {#list-custom-objects}
{% apimethod get %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Objekte für einen bestimmten angepassten Objekttyp aufzulisten.

{% alert important %}
Angepasste Objekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für angepasste Objekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.read`.

## Rate-Limit

Dieser Endpunkt gehört zum Lese-Bucket für angepasste Objekte mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für angepasste Objekte auflisten" }

## Abfrageparameter {#query-parameters}

Die folgende Tabelle listet und beschreibt die Abfrageparameter für den Endpunkt `/custom_objects/objects/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `search_term` | Optional | String | Teilstring-Filter für den Objektbezeichner |
| `limit` | Optional | Integer | Seitengröße. Standard `100`. Begrenzt auf `1` bis `250` |
| `offset` | Optional | Integer | Offset. Standard `0`. Negative Werte werden auf `0` gerundet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter für angepasste Objekte auflisten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für die Anfrageparameter und eine cURL-Beispielanfrage.

### Beispiel-Anfrageparameter {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für Anfrageparameter.

```json
{
  "type_name": "account",
  "search_term": "acct",
  "limit": 100,
  "offset": 0
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel listet die `account`-Datensätze auf, die dem Suchbegriff `acct` entsprechen, und gibt die erste Ergebnisseite zurück.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account?search_term=acct&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben.

```json
{
  "items": [
    {
      "type_name": "account",
      "external_id": "acct-123",
      "attributes": { "name": "Acme", "industry": "software" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Liste der angepassten Objektdatensätze |
| `items[].type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `items[].external_id` | Erforderlich | String | Bezeichner des angepassten Objekts |
| `items[].attributes` | Erforderlich | Object | Objektattribute, nach Feldname indiziert |
| `total_count` | Erforderlich | Integer | Gesamtanzahl der übereinstimmenden Datensätze |
| `has_more` | Erforderlich | Boolean | Ob eine weitere Ergebnisseite verfügbar ist |
| `next_offset` | Optional | Integer | Offset für die nächste Seite, wenn `has_more` den Wert `true` hat |
| `offset` | Erforderlich | Integer | Aktueller Seiten-Offset |
| `limit` | Erforderlich | Integer | Von der Anfrage verwendete Seitengröße |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für angepasste Objekte auflisten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `404` | Typ nicht gefunden (`custom-object-type-not-found`) | Bestätigen Sie, dass `type_name` im Workspace existiert und exakt mit dem Maschinennamen übereinstimmt. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `custom_objects.read` besitzt und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Auflisten angepasster Objekte" }
{% endapi %}