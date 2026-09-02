---
nav_title: "GET: Datenobjekttyp abrufen"
article_title: "GET: Datenobjekttyp abrufen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Datenobjekttyp abrufen“."
---
{% api %}
# Datenobjekttyp abrufen {#get-data-object-type}
{% apimethod get %}
/data_objects/types/{type_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen Datenobjekttyp und seine Schemadefinition zurückzugeben.

{% alert important %}
Datenobjekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Datenobjekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.read`.

## Rate-Limit

Dieser Endpunkt befindet sich im Datenobjekte-Lese-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/types/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Datenobjekttyp abrufen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für die Pfadparameter-Payload und eine Beispiel-cURL-Anfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für den Pfadparameter in dieser Anfrage.

```json
{
  "type_name": "account"
}
```

### Beispiel-cURL-Anfrage {#sample-curl-request}

Dieses Beispiel ruft die Definition des Datenobjekttyps `account` ab.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält eine Beispielantwort bei Erfolg und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben.

```json
{
  "data_object_type": {
    "type_name": "account",
    "metadata": { "display_name_source": "name" },
    "schema_def": {
      "type": "object",
      "properties": {
        "name": { "type": "string", "title": "Name" },
        "industry": { "type": "string", "title": "Industry" },
        "renewal_date": { "type": "string", "format": "date-time", "title": "Renewal date" }
      },
      "required": ["name"]
    }
  }
}
```

`schema_def` beschreibt die zulässigen Objektfelder. Schreibvorgänge lehnen nicht deklarierte Felder weiterhin ab, auch wenn dieses Antwortschema deskriptiv ist.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `data_object_type` | Erforderlich | Objekt | Zurückgegebener Datenobjekttyp-Datensatz |
| `data_object_type.type_name` | Erforderlich | String | Maschinenname des Datenobjekttyps |
| `data_object_type.metadata` | Erforderlich | Objekt | Typ-Metadaten-Objekt |
| `data_object_type.schema_def` | Erforderlich | Objekt | JSON-Schemadefinition für Objektattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Datenobjekttyp abrufen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `404` | Typ nicht gefunden (`data-object-type-not-found`) | Bestätigen Sie, dass `type_name` im Workspace existiert und exakt mit dem Maschinennamen übereinstimmt. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `data_objects.read` besitzt und Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Abrufen des Datenobjekttyps" }
{% endapi %}