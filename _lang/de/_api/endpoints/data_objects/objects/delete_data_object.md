---
nav_title: "DELETE: Datenobjekt löschen"
article_title: "DELETE: Datenobjekt löschen"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Datenobjekt löschen“."
---
{% api %}
# Datenobjekt löschen {#delete-data-object}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein Datenobjekt zu löschen.

{% alert important %}
Datenobjekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Datenobjekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.delete`.

## Rate-Limit

Dieser Endpunkt befindet sich im Schreib-Bucket für Datenobjekte mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für das Löschen von Datenobjekten" }

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

Dieses Beispiel löscht den Kontodatensatz `acct-123`.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben.

```json
{ "deleted": true }
```

Das Löschen erfolgt synchron. Das Löschen eines Objekts löscht keine verwandten Objekte.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `deleted` | Erforderlich | Boolean | Ob das Löschen des Objekts erfolgreich war |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für das Löschen von Datenobjekten" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Hinweis |
|---|---|---|
| `404` | Typ nicht gefunden oder Objekt nicht gefunden | Bestätigen Sie, dass sowohl `type_name` als auch `external_id` im Workspace vorhanden sind. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und ob der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `data_objects.delete` hat und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Löschen von Datenobjekten" }
{% endapi %}