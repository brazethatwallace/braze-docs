---
nav_title: "GET: Nutzer:innen-Beziehungen auflisten"
article_title: "GET: Nutzer:innen-Beziehungen auflisten"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Nutzer:innen-Beziehungen auflisten“."
---
{% api %}
# Nutzer:innen-Beziehungen auflisten {#list-user-relationships}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/user_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Nutzer:innen aufzulisten, die mit einem Data Object verknüpft sind.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Data-Objects-API-Schlüssel-Berechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.user_relationships.read`.

## Rate-Limits {#rate-limit}

Dieser Endpunkt gehört zum Data-Objects-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/user_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Objekttyp |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Nutzer:innen-Beziehungen auflisten" }

## Abfrageparameter {#query-parameters}

Die folgende Tabelle listet und beschreibt die Abfrageparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/user_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `rel_kind` | Optional | String | Nach Beziehungsart filtern |
| `limit` | Optional | Integer | Seitengröße. Standard `100`. Wird auf `1` bis `250` begrenzt |
| `offset` | Optional | Integer | Offset. Standard `0`. Negative Werte werden auf `0` gesetzt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter für Nutzer:innen-Beziehungen auflisten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel-Payload und eine Beispiel-cURL-Anfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für Anfrageparameter.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "rel_kind": "account_user",
  "limit": 100,
  "offset": 0
}
```

### Beispiel-cURL-Anfrage {#sample-curl-request}

Dieses Beispiel listet die Nutzer:innen auf, die über die Beziehung `account_user` mit `acct-123` verknüpft sind.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/user_relationships?rel_kind=account_user&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält eine Beispielantwort bei Erfolg und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "items": [
    {
      "type_name": "account",
      "external_id": "acct-123",
      "rel_kind": "account_user",
      "user": { "braze_id": "507f1f77bcf86cd799439011" },
      "attributes": { "role": "admin" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

Das `user`-Payload enthält nur `braze_id`.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Liste der Nutzer:innen-Beziehungsdatensätze |
| `items[].type_name` | Erforderlich | String | Maschinenname des Data-Object-Typs |
| `items[].external_id` | Erforderlich | String | Data-Object-Bezeichner |
| `items[].rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `items[].user` | Erforderlich | Object | Verknüpftes Nutzer:innen-Objekt |
| `items[].user.braze_id` | Erforderlich | String | Braze-Nutzer:innen-Bezeichner |
| `items[].attributes` | Erforderlich | Object | Beziehungsattribute |
| `total_count` | Erforderlich | Integer | Gesamtanzahl übereinstimmender Datensätze |
| `has_more` | Erforderlich | Boolean | Ob eine weitere Ergebnisseite verfügbar ist |
| `next_offset` | Optional | Integer | Offset für die nächste Seite, wenn `has_more` den Wert `true` hat |
| `offset` | Erforderlich | Integer | Aktueller Seiten-Offset |
| `limit` | Erforderlich | Integer | Von der Anfrage verwendete Seitengröße |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Nutzer:innen-Beziehungen auflisten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `404` | Typ oder Objekt nicht gefunden | Stellen Sie sicher, dass `type_name` und `external_id` beide im Workspace vorhanden sind. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Zulassungsliste blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `data_objects.user_relationships.read` hat und dass Ihre Quell-IP auf der Schlüssel-Zulassungsliste steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler bei Nutzer:innen-Beziehungen auflisten" }
{% endapi %}