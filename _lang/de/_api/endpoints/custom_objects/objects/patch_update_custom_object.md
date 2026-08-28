---
nav_title: "PATCH: Benutzerdefiniertes Objekt aktualisieren"
article_title: "PATCH: Benutzerdefiniertes Objekt aktualisieren"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Benutzerdefiniertes Objekt aktualisieren“."
---
{% api %}
# Benutzerdefiniertes Objekt aktualisieren {#update-custom-object}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Attribute in ein bestehendes benutzerdefiniertes Objekt zusammenzuführen.

{% alert important %}
Benutzerdefinierte Objekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für benutzerdefinierte Objekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.update`.

## Rate-Limit

Dieser Endpunkt befindet sich im Schreib-Bucket für benutzerdefinierte Objekte mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des benutzerdefinierten Objekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für benutzerdefiniertes Objekt aktualisieren" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `attributes` | Erforderlich | Objekt | Felder der obersten Ebene zum Zusammenführen |
| `display_name` | Optional | String | Anzeigename für das Objekt. Wenn der Typ ein Quellfeld für den Anzeigenamen hat, hat der Wert dieses Feldes Vorrang. Wird er weggelassen, bleibt der bestehende Anzeigename erhalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für benutzerdefiniertes Objekt aktualisieren" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispiel-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel aktualisiert das Attribut `credits` bei `acct-123` und lässt die übrigen Attribute des Datensatzes unverändert.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## Antwort {#response}

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antworttext zurückgeben. Das `attributes`-Objekt spiegelt das Ergebnis der Zusammenführung wider.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `custom_object` | Erforderlich | Objekt | Aktualisierter Datensatz des benutzerdefinierten Objekts |
| `custom_object.type_name` | Erforderlich | String | Maschinenname des benutzerdefinierten Objekttyps |
| `custom_object.external_id` | Erforderlich | String | Bezeichner des benutzerdefinierten Objekts |
| `custom_object.attributes` | Erforderlich | Objekt | Objektattribute nach der Zusammenführung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für benutzerdefiniertes Objekt aktualisieren" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass jedes Feld in `attributes` im Typschema existiert und den korrekten Datentyp verwendet. |
| `404` | Typ nicht gefunden oder Objekt nicht gefunden | Bestätigen Sie, dass `type_name` und `external_id` beide im Workspace existieren. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel über `custom_objects.update` verfügt und dass Ihre Quell-IP auf der Allowlist des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Aktualisieren benutzerdefinierter Objekte" }
{% endapi %}