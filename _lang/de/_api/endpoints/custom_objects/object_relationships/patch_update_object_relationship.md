---
nav_title: "PATCH: Objektbeziehung aktualisieren"
article_title: "PATCH: Objektbeziehung aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Aktualisieren von Objektbeziehungen."
---
{% api %}
# Objektbeziehung aktualisieren {#update-object-relationship}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Attribute in eine bestehende Objektbeziehung zusammenzuführen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.object_relationships.update`.

## Rate-Limit

Dieser Endpunkt befindet sich im Custom-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | URL-Objekttyp |
| `external_id` | Erforderlich | String | URL-Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Objektbeziehung aktualisieren" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `related_type_name` | Erforderlich | String | Verwandter Objekttyp |
| `related_external_id` | Erforderlich | String | Verwandter Objektbezeichner |
| `anchor` | Optional | String | `source` (Standard) oder `target` |
| `attributes` | Optional | Object | Zusammenzuführende Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für Objektbeziehung aktualisieren" }

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

Dieses Beispiel führt Attribute in die bestehende `subaccount`-Beziehung zwischen `acct-123` und `acct-456` zusammen, wobei alle Attribute, die Sie weglassen, unverändert bleiben.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

Dieser Abschnitt enthält eine Beispielantwort bei Erfolg und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortbody zurückgeben.

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
| `object_relationship` | Erforderlich | Object | Aktualisierter Beziehungsdatensatz |
| `object_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `object_relationship.to_custom_object` | Bedingt | Object | Verwandtes Objekt, wenn `anchor=source` |
| `object_relationship.from_custom_object` | Bedingt | Object | Verwandtes Objekt, wenn `anchor=target` |
| `object_relationship.attributes` | Erforderlich | Object | Beziehungsattribute nach der Zusammenführung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Objektbeziehung aktualisieren" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass `rel_kind`, `anchor` und `attributes` für den Beziehungstyp gültig sind. |
| `404` | Beziehung nicht gefunden (`custom-object-relationship-not-found`) | Stellen Sie sicher, dass das Quellobjekt, das verwandte Objekt und die Beziehungsschlüsselwerte alle existieren. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `custom_objects.object_relationships.update` besitzt und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler bei Objektbeziehung aktualisieren" }
{% endapi %}