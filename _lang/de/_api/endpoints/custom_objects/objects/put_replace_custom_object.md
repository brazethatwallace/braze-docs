---
nav_title: "PUT: Angepasstes Objekt ersetzen"
article_title: "PUT: Angepasstes Objekt ersetzen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt „Angepasstes Objekt ersetzen“."
---
{% api %}
# Angepasstes Objekt ersetzen {#replace-custom-object}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein angepasstes Objekt mit vollständiger Attributersetzungssemantik zu erstellen oder zu ersetzen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.update`.

## Rate-Limit

Dieser Endpunkt befindet sich im Custom-Objects-Write-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für angepasstes Objekt ersetzen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `attributes` | Erforderlich | Objekt | Vollständige Objektattribute. Ausgelassene Felder werden gelöscht. |
| `display_name` | Optional | String | Anzeigename für das Objekt. Wenn der Typ ein Quellenfeld für den Anzeigenamen hat, hat der Wert dieses Feldes Vorrang. Standardmäßig `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für angepasstes Objekt ersetzen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel-JSON-Payload und eine Beispiel-cURL-Anfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### Beispiel-cURL-Anfrage {#sample-curl-request}

Dieses Beispiel ersetzt die gespeicherten Attribute von `acct-123` durch die im Payload enthaltenen. Wenn kein Datensatz mit diesem Bezeichner existiert, erstellt diese Anfrage einen neuen.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## Antwort {#response}

Dieser Abschnitt enthält eine Beispielantwort für den Erfolgsfall und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortbody zurückgeben. Dieser Endpunkt gibt `200` zurück, unabhängig davon, ob die Anfrage das Objekt erstellt oder ersetzt hat.

```json
{
  "custom_object": {
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
| `custom_object` | Erforderlich | Objekt | Erstellter oder ersetzter Datensatz des angepassten Objekts |
| `custom_object.type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `custom_object.external_id` | Erforderlich | String | Bezeichner des angepassten Objekts |
| `custom_object.attributes` | Erforderlich | Objekt | Gespeicherte Objektattribute, nach Feldname indiziert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für angepasstes Objekt ersetzen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Lösung |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass jedes Feld in `attributes` im Typschema existiert und den korrekten Datentyp verwendet. |
| `404` | Typ nicht gefunden (`custom-object-type-not-found`) | Stellen Sie sicher, dass `type_name` im Workspace existiert und exakt dem Maschinennamen entspricht. |
| `422` | Datensatzlimit erreicht (`custom-object-record-limit-exceeded`), wenn diese Anfrage ein neues Objekt erstellen würde | Reduzieren Sie die Objektanzahl für den Typ oder wenden Sie sich an den Braze-Support bezüglich Ihrer Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Zulassungsliste blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `custom_objects.update` hat und dass Ihre Quell-IP in der Schlüssel-Zulassungsliste enthalten ist, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Ersetzen angepasster Objekte" }
{% endapi %}