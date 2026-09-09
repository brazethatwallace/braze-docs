---
nav_title: "PUT: Objektbeziehung ersetzen"
article_title: "PUT: Objektbeziehung ersetzen"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Ersetzen von Objektbeziehungen."
---
{% api %}
# Objektbeziehung ersetzen {#replace-object-relationship}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Objektbeziehung zu erstellen oder zu ersetzen.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Data-Objects-API-Schlüssel-Berechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.object_relationships.update`.

## Rate-Limit

Dieser Endpunkt gehört zum Data-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | URL-Objekttyp |
| `external_id` | Erforderlich | String | URL-Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter zum Ersetzen von Objektbeziehungen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfrageparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `related_type_name` | Erforderlich | String | Zugehöriger Objekttyp |
| `related_external_id` | Erforderlich | String | Zugehöriger Objektbezeichner |
| `anchor` | Optional | String | `source` (Standard) oder `target` |
| `attributes` | Optional | Object | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter zum Ersetzen von Objektbeziehungen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel-JSON-Payload und eine Beispiel-cURL-Anfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### Beispiel-cURL-Anfrage {#sample-curl-request}

Dieses Beispiel ersetzt die `subaccount`-Beziehung zwischen `acct-123` und `acct-456` und überschreibt dabei alle zuvor gespeicherten Attribute.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}'
```

## Antwort {#response}

Dieser Abschnitt enthält eine Beispielantwort bei Erfolg sowie die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` kann die folgende Antwort zurückgeben.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_data_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `object_relationship` | Erforderlich | Object | Erstellter oder ersetzter Beziehungsdatensatz |
| `object_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `object_relationship.to_data_object` | Bedingt | Object | Zugehöriges Objekt, wenn `anchor=source` |
| `object_relationship.from_data_object` | Bedingt | Object | Zugehöriges Objekt, wenn `anchor=target` |
| `object_relationship.attributes` | Erforderlich | Object | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter zum Ersetzen von Objektbeziehungen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Empfehlung |
|---|---|---|
| `400` | Validierungsfehler | Überprüfen Sie, ob `rel_kind`, `anchor` und `attributes` für den Beziehungstyp gültig sind. |
| `404` | Beziehung oder Endpunktobjekte nicht gefunden (`data-object-relationship-not-found`) | Überprüfen Sie, ob beide Objekte und die zugehörigen Typnamen im Workspace existieren. |
| `422` | Beziehungslimit pro Objekt erreicht (`data-object-relationship-limit-exceeded`) | Reduzieren Sie die Anzahl der Beziehungen für das Objekt oder kontaktieren Sie den Braze-Support bezüglich der Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Zulassungsliste blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `data_objects.object_relationships.update` hat und Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Ersetzen von Objektbeziehungen" }
{% endapi %}