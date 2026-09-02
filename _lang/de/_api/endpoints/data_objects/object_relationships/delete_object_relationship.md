---
nav_title: "DELETE: Objektbeziehung löschen"
article_title: "DELETE: Objektbeziehung löschen"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Objektbeziehung löschen“."
---
{% api %}
# Objektbeziehung löschen {#delete-object-relationship}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Objekt-zu-Objekt-Beziehungskante zu löschen.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Data-Objects-API-Schlüsselberechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.object_relationships.delete`.

## Rate-Limit

Dieser Endpunkt befindet sich im Data-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | URL-Objekttyp |
| `external_id` | Erforderlich | String | URL-Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter zum Löschen von Objektbeziehungen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `related_type_name` | Erforderlich | String | Verknüpfter Objekttyp |
| `related_external_id` | Erforderlich | String | Verknüpfter Objektbezeichner |
| `anchor` | Optional | String | `source` (Standard) oder `target` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter zum Löschen von Objektbeziehungen" }

{% alert note %}
Dieser `DELETE`-Endpunkt erwartet einen JSON-Anfragebody. Stellen Sie sicher, dass Ihr HTTP-Client Anfragebodies bei `DELETE`-Aufrufen sendet.
{% endalert %}

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispiel-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel entfernt die `subaccount`-Beziehung zwischen `acct-123` und `acct-456`. Beide Kontodatensätze bleiben erhalten.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}'
```

## Antwort {#response}

Dieser Abschnitt enthält ein Beispiel für eine erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` kann den folgenden Antwortbody zurückgeben.

```json
{ "deleted": true }
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `deleted` | Erforderlich | Boolean | Ob das Löschen der Beziehung erfolgreich war |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter zum Löschen von Objektbeziehungen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass der Anfragebody gültige Werte für `rel_kind`, `related_type_name`, `related_external_id` und `anchor` enthält. |
| `404` | Beziehung oder Endpunktobjekt nicht gefunden | Stellen Sie sicher, dass beide Objekte existieren und die Beziehungsschlüsselwerte mit einer vorhandenen Kante übereinstimmen. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Zulassungsliste blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `data_objects.object_relationships.delete` hat und Ihre Quell-IP auf der Schlüssel-Zulassungsliste steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragefrequenz. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Löschen von Objektbeziehungen" }
{% endapi %}