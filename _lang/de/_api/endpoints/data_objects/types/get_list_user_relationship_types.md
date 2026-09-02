---
nav_title: "GET: Nutzer:innen-Beziehungstypen auflisten"
article_title: "GET: Nutzer:innen-Beziehungstypen auflisten"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Nutzer:innen-Beziehungstypen auflisten“."
---
{% api %}
# Nutzer:innen-Beziehungstypen auflisten {#list-user-relationship-types}
{% apimethod get %}
/data_objects/types/{type_name}/user_relationship_types
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um gültige `rel_kind`-Werte für Nutzer:innen-Beziehungen eines Datenobjekttyps aufzulisten.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Data-Objects-API-Schlüssel-Berechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.read`.

## Rate-Limit

Dieser Endpunkt befindet sich im Data-Objects-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/types/{type_name}/user_relationship_types`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Nutzer:innen-Beziehungstypen auflisten" }

## Abfrageparameter {#query-parameters}

Die folgende Tabelle listet und beschreibt die Abfrageparameter für den Endpunkt `/data_objects/types/{type_name}/user_relationship_types`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `limit` | Optional | Integer | Seitengröße. Standard `100`. Auf `1` bis `250` begrenzt |
| `offset` | Optional | Integer | Offset. Standard `0`. Negative Werte werden auf `0` gerundet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter für Nutzer:innen-Beziehungstypen auflisten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für die Parameter-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für Anfrageparameter.

```json
{
  "type_name": "account",
  "limit": 100,
  "offset": 0
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel listet die Nutzer:innen-Beziehungstypen auf, die Sie verwenden können, um Nutzer:innen mit `account`-Datensätzen zu verknüpfen.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account/user_relationship_types?limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "items": [
    { "rel_kind": "account_user", "display_name": "account_user" }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`display_name` entspricht derzeit `rel_kind`.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `items` | Erforderlich | Array | Liste der verfügbaren Nutzer:innen-Beziehungstypen |
| `items[].rel_kind` | Erforderlich | String | Wert des Nutzer:innen-Beziehungstyps |
| `items[].display_name` | Erforderlich | String | Anzeigename für den Beziehungstyp |
| `total_count` | Erforderlich | Integer | Gesamtanzahl der übereinstimmenden Datensätze |
| `has_more` | Erforderlich | Boolean | Ob eine weitere Ergebnisseite verfügbar ist |
| `next_offset` | Optional | Integer | Offset für die nächste Seite, wenn `has_more` den Wert `true` hat |
| `offset` | Erforderlich | Integer | Aktueller Seiten-Offset |
| `limit` | Erforderlich | Integer | Von der Anfrage verwendete Seitengröße |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Nutzer:innen-Beziehungstypen auflisten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `404` | Typ nicht gefunden (`data-object-type-not-found`) | Bestätigen Sie, dass `type_name` im Workspace existiert und exakt dem Maschinennamen entspricht. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `data_objects.read` hat und dass Ihre Quell-IP in der Zulassungsliste des Schlüssels enthalten ist, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler für Nutzer:innen-Beziehungstypen auflisten" }
{% endapi %}