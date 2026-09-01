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
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine gerichtete Beziehungskante zwischen zwei angepassten Objekten zu erstellen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert werden, bevor die API-Schlüsselberechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.object_relationships.create`.

## Rate-Limit

Dieser Endpunkt gehört zum Custom-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | URL-Objekttyp |
| `external_id` | Erforderlich | String | URL-Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Objektbeziehung erstellen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragekörperparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `related_type_name` | Erforderlich | String | Verwandter Objekttyp |
| `related_external_id` | Erforderlich | String | Bezeichner des verwandten Objekts |
| `anchor` | Optional | String | `source` (Standard) oder `target` |
| `attributes` | Optional | Object | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für Objektbeziehung erstellen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel für eine JSON-Nutzlast und eine cURL-Beispielanfrage.

### Beispiel-Anfragenutzlast {#sample-request-payload}

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
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `object_relationship` | Erforderlich | Object | Erstellter Beziehungsdatensatz |
| `object_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `object_relationship.to_custom_object` | Bedingt | Object | Verwandtes Objekt bei `anchor=source` |
| `object_relationship.from_custom_object` | Bedingt | Object | Verwandtes Objekt bei `anchor=target` |
| `object_relationship.to_custom_object.type_name` | Bedingt | String | Typname des verwandten Objekts |
| `object_relationship.to_custom_object.external_id` | Bedingt | String | Externe ID des verwandten Objekts |
| `object_relationship.to_custom_object.attributes` | Bedingt | Object | Attribute des verwandten Objekts |
| `object_relationship.from_custom_object.type_name` | Bedingt | String | Typname des verwandten Objekts |
| `object_relationship.from_custom_object.external_id` | Bedingt | String | Externe ID des verwandten Objekts |
| `object_relationship.from_custom_object.attributes` | Bedingt | Object | Attribute des verwandten Objekts |
| `object_relationship.attributes` | Erforderlich | Object | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Objektbeziehung erstellen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Unbekannte `rel_kind`, ungültiger `anchor`, ungültiger verwandter Typ für die Beziehungsart oder Schema-Verstoß | Bestätigen Sie, dass `rel_kind` für das Typpaar gültig ist, verwenden Sie einen gültigen `anchor` und stellen Sie sicher, dass `attributes` dem Beziehungsschema entsprechen. |
| `404` | URL-Objekt, verwandtes Objekt, URL-Typ oder verwandter Typ nicht gefunden | Bestätigen Sie, dass beide Objekte und beide Typnamen im Workspace vorhanden sind. |
| `409` | Doppelte Kante (`duplicate-object-relationship`) | Verwenden Sie `PUT`, um die bestehende Beziehung zu ersetzen, oder löschen Sie sie, bevor Sie sie erneut erstellen. |
| `422` | Beziehungslimit pro Objekt erreicht (`custom-object-relationship-limit-exceeded`) | Reduzieren Sie die Anzahl der Beziehungen für das Objekt oder kontaktieren Sie den Braze-Support bezüglich der Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Zulassungsliste blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `custom_objects.object_relationships.create` hat und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, sofern konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler bei Objektbeziehung erstellen" }
{% endapi %}