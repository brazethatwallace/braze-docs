---
nav_title: "GET: Datenobjekt abrufen"
article_title: "GET: Datenobjekt abrufen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Abrufen eines Datenobjekts."
---
{% api %}
# Datenobjekt abrufen {#get-data-object}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein einzelnes Datenobjekt zurückzugeben.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Data Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.read`.

## Rate-Limit

Dieser Endpunkt gehört zum Data-Objects-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Datenobjekt abrufen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für Pfadparameter und eine cURL-Beispielanfrage.

### Beispiel-Anfragepayload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für die Pfadparameter in dieser Anfrage.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel ruft den `acct-123`-Kontodatensatz und seine gespeicherten Attribute ab.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "industry": "software" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `data_object` | Erforderlich | Objekt | Zurückgegebener Datenobjekt-Datensatz |
| `data_object.type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `data_object.external_id` | Erforderlich | String | Bezeichner des Datenobjekts |
| `data_object.attributes` | Erforderlich | Objekt | Objektattribute, indiziert nach Feldname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Datenobjekt abrufen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `404` | Typ nicht gefunden (`data-object-type-not-found`) oder Objekt nicht gefunden (`data-object-not-found`) | Vergewissern Sie sich, dass sowohl `type_name` als auch `external_id` im Workspace vorhanden sind. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel besitzt keine Berechtigung oder die Anfrage wird durch die Zulassungsliste blockiert | Vergewissern Sie sich, dass der Schlüssel die Berechtigung `data_objects.read` hat und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Abrufen von Datenobjekten" }
{% endapi %}