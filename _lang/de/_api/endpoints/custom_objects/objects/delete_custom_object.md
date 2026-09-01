---
nav_title: "DELETE: Angepasstes Objekt löschen"
article_title: "DELETE: Angepasstes Objekt löschen"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Angepasstes Objekt löschen“."
---
{% api %}
# Angepasstes Objekt löschen {#delete-custom-object}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein angepasstes Objekt zu löschen.

{% alert important %}
Angepasste Objekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für angepasste Objekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt verwenden zu können, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.delete`.

## Rate-Limit

Dieser Endpunkt befindet sich im Schreib-Bucket für angepasste Objekte mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter zum Löschen angepasster Objekte" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für die Pfadparameter sowie eine cURL-Beispielanfrage.

### Beispiel für den Anfrage-Payload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für die Pfadparameter in dieser Anfrage.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel löscht den Account-Datensatz `acct-123`.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort sowie die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben.

```json
{ "deleted": true }
```

Das Löschen erfolgt synchron. Das Löschen eines Objekts führt nicht zum Löschen verwandter Objekte.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `deleted` | Erforderlich | Boolean | Ob das Löschen des Objekts erfolgreich war |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter zum Löschen angepasster Objekte" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `404` | Typ nicht gefunden oder Objekt nicht gefunden | Bestätigen Sie, dass sowohl `type_name` als auch `external_id` im Workspace vorhanden sind. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und ob der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `custom_objects.delete` hat und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Löschen angepasster Objekte" }
{% endapi %}