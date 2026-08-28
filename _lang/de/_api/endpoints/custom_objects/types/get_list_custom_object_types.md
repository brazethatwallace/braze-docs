---
nav_title: "GET: Angepasste Objekttypen auflisten"
article_title: "GET: Angepasste Objekttypen auflisten"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Auflisten angepasster Objekttypen."
---
{% api %}
# Angepasste Objekttypen auflisten {#list-custom-object-types}
{% apimethod get %}
/custom_objects/types
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um angepasste Objekttypen in einem Workspace aufzulisten.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.read`.

## Rate-Limit

Dieser Endpunkt gehört zum Custom-Objects-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Abfrageparameter {#query-parameters}

Die folgende Tabelle listet und beschreibt die Abfrageparameter für den `/custom_objects/types`-Endpunkt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `search_term` | Optional | String | Groß-/kleinschreibungsunabhängiger Präfixfilter für den Typnamen |
| `limit` | Optional | Integer | Seitengröße. Standard `100`. Eingegrenzt auf `1` bis `250` |
| `offset` | Optional | Integer | Offset. Standard `0`. Negative Werte werden auf `0` gerundet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter für angepasste Objekttypen auflisten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für Abfrageparameter und eine cURL-Beispielanfrage.

### Beispiel-Anfragenutzlast {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für die Abfrageparameter dieser Anfrage.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel listet die angepassten Objekttypen auf, die dem Suchbegriff `acc` entsprechen, und gibt zwei Ergebnisse pro Seite zurück.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält eine erfolgreiche Beispielantwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben.

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

`metadata.display_name_source` ist vorhanden, wenn ein Anzeigenamenfeld für den Typ konfiguriert ist.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Liste der Datensätze für angepasste Objekttypen |
| `items[].type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `items[].metadata` | Erforderlich | Object | Metadatenobjekt des Typs |
| `total_count` | Erforderlich | Integer | Gesamtzahl der übereinstimmenden Datensätze |
| `has_more` | Erforderlich | Boolean | Ob eine weitere Ergebnisseite verfügbar ist |
| `next_offset` | Optional | Integer | Offset für die nächste Seite, wenn `has_more` `true` ist |
| `offset` | Erforderlich | Integer | Aktueller Seiten-Offset |
| `limit` | Erforderlich | Integer | Von der Anfrage verwendete Seitengröße |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für angepasste Objekttypen auflisten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `400` | Ungültiger Typ oder Wert des Abfrageparameters | Stellen Sie sicher, dass `limit` und `offset` Integer sind und alle Parameterwerte gültig sind. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder Anfrage wird durch die Allowlist blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `custom_objects.read` hat und Ihre Quell-IP auf der Allowlist des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Auflisten angepasster Objekttypen" }
{% endapi %}