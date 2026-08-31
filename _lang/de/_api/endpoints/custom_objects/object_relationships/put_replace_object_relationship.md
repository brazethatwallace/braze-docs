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
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Objektbeziehung zu erstellen oder zu ersetzen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.object_relationships.update`.

## Rate-Limit

Dieser Endpunkt gehört zum Custom-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | URL-Objekttyp |
| `external_id` | Erforderlich | String | URL-Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für das Ersetzen von Objektbeziehungen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `related_type_name` | Erforderlich | String | Verwandter Objekttyp |
| `related_external_id` | Erforderlich | String | Verwandter Objektbezeichner |
| `anchor` | Optional | String | `source` (Standard) oder `target` |
| `attributes` | Optional | Objekt | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für das Ersetzen von Objektbeziehungen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispiel-Payload und eine cURL-Beispielanfrage.

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

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel ersetzt die `subaccount`-Beziehung zwischen `acct-123` und `acct-456` und überschreibt dabei alle zuvor gespeicherten Attribute.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortinhalt zurückgeben.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_custom_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `object_relationship` | Erforderlich | Objekt | Erstellter oder ersetzter Beziehungsdatensatz |
| `object_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `object_relationship.to_custom_object` | Bedingt | Objekt | Verwandtes Objekt, wenn `anchor=source` |
| `object_relationship.from_custom_object` | Bedingt | Objekt | Verwandtes Objekt, wenn `anchor=target` |
| `object_relationship.attributes` | Erforderlich | Objekt | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für das Ersetzen von Objektbeziehungen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Empfehlung |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass `rel_kind`, `anchor` und `attributes` für den Beziehungstyp gültig sind. |
| `404` | Beziehung oder Endpunktobjekte nicht gefunden (`custom-object-relationship-not-found`) | Stellen Sie sicher, dass beide Objekte und die verwandten Typnamen im Workspace vorhanden sind. |
| `422` | Beziehungslimit pro Objekt erreicht (`custom-object-relationship-limit-exceeded`) | Reduzieren Sie die Anzahl der Beziehungen für das Objekt oder kontaktieren Sie den Braze-Support bezüglich Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `custom_objects.object_relationships.update` hat und dass Ihre Quell-IP auf der Allowlist des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie den Versuch nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Ersetzen von Objektbeziehungen" }
{% endapi %}