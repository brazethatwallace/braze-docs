---
nav_title: "GET: Angepasstes Objekt abrufen"
article_title: "GET: Angepasstes Objekt abrufen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Abrufen eines angepassten Objekts."
---
{% api %}
# Angepasstes Objekt abrufen {#get-custom-object}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein angepasstes Objekt zurückzugeben.

{% alert important %}
Angepasste Objekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für angepasste Objekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.read`.

## Rate-Limit

Dieser Endpunkt befindet sich im Lese-Bucket für angepasste Objekte mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für das Abrufen angepasster Objekte" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für Pfadparameter und eine cURL-Beispielanfrage.

### Beispiel-Anfragenutzlast {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für die Pfadparameter in dieser Anfrage.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel ruft den Kontodatensatz `acct-123` und seine gespeicherten Attribute ab.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "industry": "software" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `custom_object` | Erforderlich | Objekt | Zurückgegebener Datensatz des angepassten Objekts |
| `custom_object.type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `custom_object.external_id` | Erforderlich | String | Bezeichner des angepassten Objekts |
| `custom_object.attributes` | Erforderlich | Objekt | Objektattribute, nach Feldname geordnet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für das Abrufen angepasster Objekte" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `404` | Typ nicht gefunden (`custom-object-type-not-found`) oder Objekt nicht gefunden (`custom-object-not-found`) | Bestätigen Sie, dass `type_name` und `external_id` beide im Workspace existieren. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder Anfrage wird durch die Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel über die Berechtigung `custom_objects.read` verfügt und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Abrufen angepasster Objekte" }
{% endapi %}