---
nav_title: "GET: Objektbeziehungen auflisten"
article_title: "GET: Objektbeziehungen auflisten"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Objektbeziehungen auflisten“."
---
{% api %}
# Objektbeziehungen auflisten {#list-object-relationships}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um verwandte Datenobjekte von einem Objektanker aus aufzulisten.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Data-Objects-API-Schlüssel-Berechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.read`.

## Rate-Limit

Dieser Endpunkt befindet sich im Data-Objects-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Quellobjekttyp |
| `external_id` | Erforderlich | String | Bezeichner des Quellobjekts |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Objektbeziehungen auflisten" }

## Abfrageparameter {#query-parameters}

Die folgende Tabelle listet und beschreibt die Abfrageparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `anchor` | Optional | String | `source` (Standard) oder `target` |
| `rel_kind` | Optional | String | Nach einer Beziehungsart filtern |
| `limit` | Optional | Integer | Seitengröße. Standard `100`. Begrenzt auf `1` bis `250` |
| `offset` | Optional | Integer | Offset. Standard `0`. Negative Werte werden auf `0` gesetzt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter für Objektbeziehungen auflisten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für die Parameter-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für Anfrageparameter.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "anchor": "source",
  "rel_kind": "subaccount",
  "limit": 100,
  "offset": 0
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel listet die `subaccount`-Datensätze auf, auf die `acct-123` verweist, und gibt die erste Ergebnisseite zurück.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antworttext zurückgeben.

```json
{
  "items": [
    {
      "rel_kind": "subaccount",
      "to_data_object": {
        "type_name": "account",
        "external_id": "acct-456",
        "attributes": { "name": "Child Account" }
      },
      "attributes": {}
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

Mit `anchor=target` werden verwandte Objekte als `from_data_object` zurückgegeben.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Liste der Objektbeziehungsdatensätze |
| `items[].rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `items[].to_data_object` | Bedingt | Object | Verwandtes Objekt bei `anchor=source` |
| `items[].from_data_object` | Bedingt | Object | Verwandtes Objekt bei `anchor=target` |
| `items[].to_data_object.type_name` | Bedingt | String | Typname des verwandten Objekts |
| `items[].to_data_object.external_id` | Bedingt | String | Externe ID des verwandten Objekts |
| `items[].to_data_object.attributes` | Bedingt | Object | Attribute des verwandten Objekts |
| `items[].from_data_object.type_name` | Bedingt | String | Typname des verwandten Objekts |
| `items[].from_data_object.external_id` | Bedingt | String | Externe ID des verwandten Objekts |
| `items[].from_data_object.attributes` | Bedingt | Object | Attribute des verwandten Objekts |
| `items[].attributes` | Erforderlich | Object | Beziehungsattribute |
| `total_count` | Erforderlich | Integer | Gesamtzahl der übereinstimmenden Datensätze |
| `has_more` | Erforderlich | Boolean | Ob eine weitere Ergebnisseite verfügbar ist |
| `next_offset` | Optional | Integer | Offset für die nächste Seite, wenn `has_more` den Wert `true` hat |
| `offset` | Erforderlich | Integer | Aktueller Seiten-Offset |
| `limit` | Erforderlich | Integer | Von der Anfrage verwendete Seitengröße |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Objektbeziehungen auflisten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Ungültiger `anchor` | Verwenden Sie `source` oder `target` für `anchor`. |
| `404` | Typ oder Objekt nicht gefunden | Stellen Sie sicher, dass `type_name` und `external_id` beide im Workspace vorhanden sind. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `data_objects.read` hat und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler bei Objektbeziehungen auflisten" }
{% endapi %}