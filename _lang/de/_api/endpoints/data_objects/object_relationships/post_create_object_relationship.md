---
nav_title: "POST: Objektbeziehung erstellen"
article_title: "POST: Objektbeziehung erstellen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Objektbeziehung erstellen“."
---
{% api %}
# Objektbeziehung erstellen {#create-object-relationship}
{% apimethod post %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine gerichtete Beziehungskante zwischen zwei Datenobjekten zu erstellen.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert werden, bevor die API-Schlüsselberechtigungen für Data Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.object_relationships.create`.

## Rate-Limit

Dieser Endpunkt gehört zum Data-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | URL-Objekttyp |
| `external_id` | Erforderlich | String | URL-Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Objektbeziehung erstellen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfrageparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `related_type_name` | Erforderlich | String | Typ des verknüpften Objekts |
| `related_external_id` | Erforderlich | String | Bezeichner des verknüpften Objekts |
| `anchor` | Optional | String | `source` (Standard) oder `target` |
| `attributes` | Optional | Object | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für Objektbeziehung erstellen" }

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

Dieses Beispiel verknüpft `acct-123` mit `acct-456` als `subaccount`, wobei `acct-123` die Quelle der Beziehung ist.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
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

Dieser Abschnitt enthält eine erfolgreiche Beispielantwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `201` könnte den folgenden Antwortkörper zurückgeben.

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
| `object_relationship` | Erforderlich | Object | Erstellter Beziehungsdatensatz |
| `object_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `object_relationship.to_data_object` | Bedingt | Object | Verknüpftes Objekt bei `anchor=source` |
| `object_relationship.from_data_object` | Bedingt | Object | Verknüpftes Objekt bei `anchor=target` |
| `object_relationship.to_data_object.type_name` | Bedingt | String | Typname des verknüpften Objekts |
| `object_relationship.to_data_object.external_id` | Bedingt | String | Externe ID des verknüpften Objekts |
| `object_relationship.to_data_object.attributes` | Bedingt | Object | Attribute des verknüpften Objekts |
| `object_relationship.from_data_object.type_name` | Bedingt | String | Typname des verknüpften Objekts |
| `object_relationship.from_data_object.external_id` | Bedingt | String | Externe ID des verknüpften Objekts |
| `object_relationship.from_data_object.attributes` | Bedingt | Object | Attribute des verknüpften Objekts |
| `object_relationship.attributes` | Erforderlich | Object | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Objektbeziehung erstellen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Unbekannter `rel_kind`, ungültiger `anchor`, ungültiger verknüpfter Typ für die Beziehungsart oder Schemaverstoß | Bestätigen Sie, dass `rel_kind` für das Typpaar gültig ist, verwenden Sie einen gültigen `anchor` und stellen Sie sicher, dass `attributes` dem Beziehungsschema entsprechen. |
| `404` | URL-Objekt, verknüpftes Objekt, URL-Typ oder verknüpfter Typ nicht gefunden | Bestätigen Sie, dass beide Objekte und beide Typnamen im Workspace vorhanden sind. |
| `409` | Doppelte Kante (`duplicate-object-relationship`) | Verwenden Sie `PUT`, um die vorhandene Beziehung zu ersetzen, oder löschen Sie sie, bevor Sie sie erneut erstellen. |
| `422` | Beziehungslimit pro Objekt erreicht (`data-object-relationship-limit-exceeded`) | Reduzieren Sie die Anzahl der Beziehungen für das Objekt oder kontaktieren Sie den Braze-Support bezüglich der Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Allowlist blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `data_objects.object_relationships.create` hat und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler bei Objektbeziehung erstellen" }
{% endapi %}