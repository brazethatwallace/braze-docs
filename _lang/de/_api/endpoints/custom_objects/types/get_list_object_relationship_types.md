---
nav_title: "GET: Objekt-Beziehungstypen auflisten"
article_title: "GET: Objekt-Beziehungstypen auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Objekt-Beziehungstypen auflisten“."
---
{% api %}
# Objekt-Beziehungstypen auflisten {#list-object-relationship-types}
{% apimethod get %}
/custom_objects/types/{type_name}/object_relationship_types
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die verfügbaren Beziehungsarten für Objekt-zu-Objekt-Verknüpfungen für eine bestimmte Ankerrichtung aufzulisten.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.read`.

## Rate-Limits {#rate-limit}

Dieser Endpunkt gehört zum Custom-Objects-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/types/{type_name}/object_relationship_types`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Objekt-Beziehungstypen auflisten" }

## Abfrageparameter {#query-parameters}

Die folgende Tabelle listet und beschreibt die Abfrageparameter für den Endpunkt `/custom_objects/types/{type_name}/object_relationship_types`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `anchor` | Optional | String | `source` (Standard) oder `target` |
| `limit` | Optional | Integer | Seitengröße. Standard `100`. Begrenzt auf `1` bis `250` |
| `offset` | Optional | Integer | Offset. Standard `0`. Negative Werte werden auf `0` gerundet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter für Objekt-Beziehungstypen auflisten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für den Parameter-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für Anfrageparameter.

```json
{
  "type_name": "account",
  "anchor": "source",
  "limit": 10,
  "offset": 0
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel listet die Objektbeziehungsarten auf, die für den Typ `account` verfügbar sind, wenn `account` die Quelle der Beziehung ist.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account/object_relationship_types?anchor=source&limit=10&offset=0' \
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
      "from_type_name": "account",
      "to_type_name": "account",
      "rel_kind": "subaccount",
      "display_name": "subaccount",
      "related_type_name": "account"
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 10
}
```

`related_type_name` ist der Typ auf der anderen Seite der Beziehung für den ausgewählten `anchor`.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Liste der verfügbaren Objekt-Beziehungstypen |
| `items[].from_type_name` | Erforderlich | String | Name des Quell-Objekttyps |
| `items[].to_type_name` | Erforderlich | String | Name des Ziel-Objekttyps |
| `items[].rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `items[].display_name` | Erforderlich | String | Anzeigename für die Beziehungsart |
| `items[].related_type_name` | Erforderlich | String | Typ auf der gegenüberliegenden Seite für den angeforderten `anchor` |
| `total_count` | Erforderlich | Integer | Gesamtanzahl der übereinstimmenden Datensätze |
| `has_more` | Erforderlich | Boolean | Ob eine weitere Ergebnisseite verfügbar ist |
| `next_offset` | Optional | Integer | Offset für die nächste Seite, wenn `has_more` den Wert `true` hat |
| `offset` | Erforderlich | Integer | Aktueller Seiten-Offset |
| `limit` | Erforderlich | Integer | Von der Anfrage verwendete Seitengröße |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Objekt-Beziehungstypen auflisten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Ungültiger `anchor` | Verwenden Sie `source` oder `target` für `anchor`. |
| `404` | Typ nicht gefunden (`custom-object-type-not-found`) | Stellen Sie sicher, dass `type_name` im Workspace existiert und exakt dem Maschinennamen entspricht. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `custom_objects.read` hat und Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler für Objekt-Beziehungstypen auflisten" }
{% endapi %}