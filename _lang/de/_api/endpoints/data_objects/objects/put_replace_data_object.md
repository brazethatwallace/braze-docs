---
nav_title: "PUT: Datenobjekt ersetzen"
article_title: "PUT: Datenobjekt ersetzen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Ersetzen von Datenobjekten."
---
{% api %}
# Datenobjekt ersetzen {#replace-data-object}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein Datenobjekt mit vollständiger Attributersetzungssemantik zu erstellen oder zu ersetzen.

{% alert important %}
Datenobjekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Datenobjekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.update`.

## Rate-Limit

Dieser Endpunkt befindet sich im Datenobjekte-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für das Ersetzen von Datenobjekten" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfrageparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `attributes` | Erforderlich | Objekt | Vollständige Objektattribute. Ausgelassene Felder werden gelöscht |
| `display_name` | Optional | String | Anzeigename für das Objekt. Wenn der Typ ein Quellfeld für den Anzeigenamen hat, hat der Wert dieses Feldes Vorrang. Standardwert ist `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für das Ersetzen von Datenobjekten" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispiel-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel ersetzt die gespeicherten Attribute von `acct-123` durch die im Payload enthaltenen. Wenn kein Datensatz mit diesem Bezeichner existiert, erstellt diese Anfrage einen neuen.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## Antwort {#response}

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben. Dieser Endpunkt gibt `200` zurück, unabhängig davon, ob die Anfrage das Objekt erstellt oder ersetzt hat.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `data_object` | Erforderlich | Objekt | Erstellter oder ersetzter Datenobjektdatensatz |
| `data_object.type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `data_object.external_id` | Erforderlich | String | Bezeichner des Datenobjekts |
| `data_object.attributes` | Erforderlich | Objekt | Gespeicherte Objektattribute, nach Feldnamen geordnet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für das Ersetzen von Datenobjekten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Lösungshinweis |
|---|---|---|
| `400` | Validierungsfehler | Überprüfen Sie, ob jedes Feld in `attributes` im Typschema existiert und den richtigen Datentyp verwendet. |
| `404` | Typ nicht gefunden (`data-object-type-not-found`) | Überprüfen Sie, ob `type_name` im Workspace existiert und exakt mit dem Maschinennamen übereinstimmt. |
| `422` | Datensatzlimit erreicht (`data-object-record-limit-exceeded`), wenn diese Anfrage ein neues Objekt erstellen würde | Reduzieren Sie die Anzahl der Objekte für den Typ oder kontaktieren Sie den Braze-Support bezüglich Ihrer Workspace-Limits. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Allowlist blockiert | Überprüfen Sie, ob der Schlüssel über die Berechtigung `data_objects.update` verfügt und ob Ihre Quell-IP auf der Schlüssel-Allowlist steht, sofern konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Ersetzen von Datenobjekten" }
{% endapi %}