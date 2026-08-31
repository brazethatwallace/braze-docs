---
nav_title: "POST: Benutzerdefiniertes Objekt erstellen"
article_title: "POST: Benutzerdefiniertes Objekt erstellen"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Benutzerdefiniertes Objekt erstellen“."
---
{% api %}
# Benutzerdefiniertes Objekt erstellen {#create-custom-object}
{% apimethod post %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein benutzerdefiniertes Objekt für einen Typ zu erstellen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.create`.

## Rate-Limit

Dieser Endpunkt befindet sich im Custom-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des benutzerdefinierten Objekttyps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für benutzerdefiniertes Objekt erstellen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Request-Body-Parameter für den Endpunkt `/custom_objects/objects/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `external_id` | Erforderlich | String | Objektbezeichner, eindeutig innerhalb des Typs |
| `attributes` | Erforderlich | Objekt | Feldnamen-basierte Werte, die gegen das Typschema validiert werden |
| `display_name` | Optional | String | Anzeigename für das Objekt. Wenn der Typ ein Anzeigename-Quellfeld besitzt, hat der Wert dieses Felds Vorrang. Standardmäßig `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für benutzerdefiniertes Objekt erstellen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispiel-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

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

Dieses Beispiel erstellt einen `account`-Datensatz mit dem Bezeichner `acct-new` und setzt die Attribute `name` und `industry`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account' \
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

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `201` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `custom_object` | Erforderlich | Objekt | Erstellter benutzerdefinierter Objektdatensatz |
| `custom_object.type_name` | Erforderlich | String | Maschinenname des benutzerdefinierten Objekttyps |
| `custom_object.external_id` | Erforderlich | String | Bezeichner des benutzerdefinierten Objekts |
| `custom_object.attributes` | Erforderlich | Objekt | Gespeicherte Objektattribute, nach Feldnamen geordnet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für benutzerdefiniertes Objekt erstellen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Empfehlung |
|---|---|---|
| `400` | Unbekanntes Attributfeld oder ungültiger Attributtyp | Stellen Sie sicher, dass jedes Feld in `attributes` im Typschema existiert und den richtigen Datentyp verwendet. |
| `404` | Typ nicht gefunden (`custom-object-type-not-found`) | Stellen Sie sicher, dass `type_name` im Workspace existiert und exakt mit dem Maschinennamen übereinstimmt. |
| `409` | Doppeltes Objekt (`duplicate-custom-object`) | Verwenden Sie eine andere `external_id` oder nutzen Sie `PUT`, um das vorhandene Objekt zu ersetzen. |
| `422` | Datensatzlimit erreicht (`custom-object-record-limit-exceeded`) | Reduzieren Sie die Objektanzahl für den Typ oder kontaktieren Sie den Braze-Support bezüglich Ihrer Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel über `custom_objects.create` verfügt und Ihre Quell-IP in der Allowlist des Schlüssels enthalten ist, sofern konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Erstellen benutzerdefinierter Objekte" }
{% endapi %}