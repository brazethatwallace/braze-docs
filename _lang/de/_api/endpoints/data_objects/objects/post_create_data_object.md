---
nav_title: "POST: Datenobjekt erstellen"
article_title: "POST: Datenobjekt erstellen"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Datenobjekt erstellen“."
---
{% api %}
# Datenobjekt erstellen {#create-data-object}
{% apimethod post %}
/data_objects/objects/{type_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein Datenobjekt für einen Typ zu erstellen.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Data Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.create`.

## Rate-Limit

Dieser Endpunkt gehört zum Data-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Datenobjekt erstellen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/data_objects/objects/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `external_id` | Erforderlich | String | Objektbezeichner, eindeutig innerhalb des Typs |
| `attributes` | Erforderlich | Objekt | Durch Feldnamen referenzierte Werte, die gegen das Typschema validiert werden |
| `display_name` | Optional | String | Anzeigelabel für das Objekt. Wenn der Typ ein Quellfeld für den Anzeigenamen hat, hat der Wert dieses Feldes Vorrang. Standardmäßig `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für Datenobjekt erstellen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispielpayload und eine cURL-Beispielanfrage.

### Beispiel-Anfragepayload {#sample-request-payload}

```json
{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel erstellt einen `account`-Datensatz mit dem Bezeichner `acct-new` und setzt dessen Attribute `name` und `industry`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `201` könnte den folgenden Antwortbody zurückgeben.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `data_object` | Erforderlich | Objekt | Erstellter Datenobjekt-Datensatz |
| `data_object.type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `data_object.external_id` | Erforderlich | String | Bezeichner des Datenobjekts |
| `data_object.attributes` | Erforderlich | Objekt | Gespeicherte Objektattribute, referenziert nach Feldname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Datenobjekt erstellen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Unbekanntes Attributfeld oder ungültiger Attributtyp | Stellen Sie sicher, dass jedes Feld in `attributes` im Typschema existiert und den korrekten Datentyp verwendet. |
| `404` | Typ nicht gefunden (`data-object-type-not-found`) | Stellen Sie sicher, dass `type_name` im Workspace existiert und exakt dem Maschinennamen entspricht. |
| `409` | Doppeltes Objekt (`duplicate-data-object`) | Verwenden Sie eine andere `external_id` oder nutzen Sie `PUT`, um das bestehende Objekt zu ersetzen. |
| `422` | Datensatzlimit erreicht (`data-object-record-limit-exceeded`) | Reduzieren Sie die Objektanzahl für den Typ oder kontaktieren Sie den Braze-Support bezüglich Ihrer Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel über `data_objects.create` verfügt und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es erneut nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Erstellen von Datenobjekten" }
{% endapi %}