---
nav_title: "PATCH: Datenobjekt Update or aktualisieren or aktualisieren"
article_title: "PATCH: Datenobjekt Update or aktualisieren or aktualisieren"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Update or aktualisieren or aktualisieren von Datenobjekten."
---
{% api %}
# Datenobjekt Update or aktualisieren or aktualisieren {#update-data-object}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Attribute in ein bestehendes Datenobjekt zusammenzuführen.

{% alert important %}
Datenobjekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Datenobjekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.update`.

## Rate-Limit

Dieser Endpunkt gehört zum Datenobjekte-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Datenobjekt Update or aktualisieren or aktualisieren" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragekörperparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `attributes` | Erforderlich | Objekt | Felder der obersten Ebene, die zusammengeführt werden sollen |
| `display_name` | Optional | String | Anzeigename für das Objekt. Wenn der Typ ein Quellfeld für den Anzeigenamen hat, hat der Wert dieses Feldes Vorrang. Wenn nicht angegeben, wird der bestehende Anzeigename beibehalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für Datenobjekt Update or aktualisieren or aktualisieren" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel-JSON-Payload und eine Beispiel-cURL-Anfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### Beispiel-cURL-Anfrage {#sample-curl-request}

Dieses Beispiel aktualisiert das Attribut `credits` für `acct-123` und lässt die übrigen Attribute des Datensatzes unverändert.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben. Das Objekt `attributes` spiegelt das Ergebnis der Zusammenführung wider.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `data_object` | Erforderlich | Objekt | Aktualisierter Datenobjekt-Datensatz |
| `data_object.type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `data_object.external_id` | Erforderlich | String | Datenobjektbezeichner |
| `data_object.attributes` | Erforderlich | Objekt | Objektattribute nach der Zusammenführung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Datenobjekt Update or aktualisieren or aktualisieren" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass jedes Feld in `attributes` im Typ-Schema existiert und den korrekten Datentyp verwendet. |
| `404` | Typ nicht gefunden oder Objekt nicht gefunden | Stellen Sie sicher, dass sowohl `type_name` als auch `external_id` im Workspace existieren. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und ob der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel über die Berechtigung `data_objects.update` verfügt und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Update or aktualisieren or aktualisieren von Datenobjekten" }
{% endapi %}