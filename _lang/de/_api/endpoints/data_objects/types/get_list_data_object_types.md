---
nav_title: "GET: Datenobjekttypen auflisten"
article_title: "GET: Datenobjekttypen auflisten"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Datenobjekttypen auflisten“."
---
{% api %}
# Datenobjekttypen auflisten {#list-data-object-types}
{% apimethod get %}
/data_objects/types
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Datenobjekttypen in einem Workspace aufzulisten.

{% alert important %}
Datenobjekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Datenobjekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.read`.

## Rate-Limit

Dieser Endpunkt befindet sich im Datenobjekte-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Abfrageparameter {#query-parameters}

Die folgende Tabelle listet und beschreibt die Abfrageparameter für den Endpunkt `/data_objects/types`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `search_term` | Optional | String | Groß-/Kleinschreibung-unabhängiger Präfixfilter für den Typnamen |
| `limit` | Optional | Integer | Seitengröße. Standard `100`. Begrenzt auf `1` bis `250` |
| `offset` | Optional | Integer | Offset. Standard `0`. Negative Werte werden auf `0` aufgerundet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter für Datenobjekttypen auflisten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für Abfrageparameter und eine cURL-Beispielanfrage.

### Beispiel-Anfragenutzlast {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für die Abfrageparameter in dieser Anfrage.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel listet die Datenobjekttypen auf, die dem Suchbegriff `acc` entsprechen, und gibt zwei Ergebnisse pro Seite zurück.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält eine erfolgreiche Beispielantwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben.

```json
{
  "items": [
    {
      "type_name": "account",
      "metadata": { "display_name_source": "name" }
    },
    {
      "type_name": "contact",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`metadata.display_name_source` ist vorhanden, wenn ein Anzeigename-Feld für den Typ konfiguriert ist.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Liste der Datenobjekttyp-Datensätze |
| `items[].type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `items[].metadata` | Erforderlich | Object | Metadatenobjekt des Typs |
| `total_count` | Erforderlich | Integer | Gesamtzahl der übereinstimmenden Datensätze |
| `has_more` | Erforderlich | Boolean | Ob eine weitere Ergebnisseite verfügbar ist |
| `next_offset` | Optional | Integer | Offset für die nächste Seite, wenn `has_more` `true` ist |
| `offset` | Erforderlich | Integer | Aktueller Seiten-Offset |
| `limit` | Erforderlich | Integer | Von der Anfrage verwendete Seitengröße |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Datenobjekttypen auflisten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `400` | Ungültiger Abfrageparametertyp oder -wert | Stellen Sie sicher, dass `limit` und `offset` Integer sind und alle Parameterwerte gültig sind. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `data_objects.read` hat und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie den Versuch nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Auflisten von Datenobjekttypen" }
{% endapi %}