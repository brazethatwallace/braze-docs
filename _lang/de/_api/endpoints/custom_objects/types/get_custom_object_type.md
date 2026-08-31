---
nav_title: "GET: Angepassten Objekttyp abrufen"
article_title: "GET: Angepassten Objekttyp abrufen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Angepassten Objekttyp abrufen“."
---
{% api %}
# Angepassten Objekttyp abrufen {#get-custom-object-type}
{% apimethod get %}
/custom_objects/types/{type_name}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen angepassten Objekttyp und seine Schemadefinition zurückzugeben.

{% alert important %}
Angepasste Objekte befinden sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für angepasste Objekte unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.read`.

## Rate-Limit

Dieser Endpunkt gehört zum Lese-Bucket für angepasste Objekte mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/types/{type_name}`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für „Angepassten Objekttyp abrufen“" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für den Pfadparameter und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

Verwenden Sie dieses JSON-Objekt als Referenz für den Pfadparameter in dieser Anfrage.

```json
{
  "type_name": "account"
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel ruft die Definition des angepassten Objekttyps `account` ab.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortkörper zurückgeben.

```json
{
  "custom_object_type": {
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

`schema_def` beschreibt die zulässigen Objektfelder. Schreibvorgänge lehnen nicht deklarierte Felder weiterhin ab, auch wenn dieses Antwortschema beschreibender Natur ist.

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `custom_object_type` | Erforderlich | Objekt | Zurückgegebener Datensatz des angepassten Objekttyps |
| `custom_object_type.type_name` | Erforderlich | String | Maschinenname des angepassten Objekttyps |
| `custom_object_type.metadata` | Erforderlich | Objekt | Metadaten-Objekt des Typs |
| `custom_object_type.schema_def` | Erforderlich | Objekt | JSON-Schemadefinition für Objektattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für „Angepassten Objekttyp abrufen“" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Hinweis |
|---|---|---|
| `404` | Typ nicht gefunden (`custom-object-type-not-found`) | Bestätigen Sie, dass `type_name` im Workspace vorhanden ist und exakt mit dem Maschinennamen übereinstimmt. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel über die Berechtigung `custom_objects.read` verfügt und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler für „Angepassten Objekttyp abrufen“" }
{% endapi %}