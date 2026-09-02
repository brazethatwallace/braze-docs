---
nav_title: "DELETE: Nutzer:innen-Beziehung löschen"
article_title: "DELETE: Nutzer:innen-Beziehung löschen"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Nutzer:innen-Beziehung löschen“."
---
{% api %}
# Nutzer:innen-Beziehung löschen {#delete-user-relationship}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Beziehung zwischen Nutzer:in und Objekt zu entfernen.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Data-Objects-API-Schlüsselberechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.user_relationships.delete`.

## Rate-Limit

Dieser Endpunkt gehört zum Data-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Objekttyp |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für das Löschen der Nutzer:innen-Beziehung" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `braze_id` | Erforderlich | String | Braze-Nutzer:innen-ID |
| `rel_kind` | Erforderlich | String | Beziehungstyp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für das Löschen der Nutzer:innen-Beziehung" }

{% alert note %}
Dieser `DELETE`-Endpunkt erwartet einen JSON-Anfragebody. Stellen Sie sicher, dass Ihr HTTP-Client Anfragebodys bei `DELETE`-Aufrufen sendet.
{% endalert %}

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält eine Beispiel-JSON-Payload und eine Beispiel-cURL-Anfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}
```

### Beispiel-cURL-Anfrage {#sample-curl-request}

Dieses Beispiel entfernt die `account_user`-Beziehung zwischen dem angegebenen Nutzer bzw. der angegebenen Nutzerin und `acct-123`. Das Nutzerprofil und der Account-Datensatz bleiben beide erhalten.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}'
```

## Antwort {#response}

Dieser Abschnitt enthält eine Beispielantwort bei Erfolg und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortbody zurückgeben.

```json
{ "deleted": true }
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `deleted` | Erforderlich | Boolean | Ob das Löschen der Beziehung erfolgreich war |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für das Löschen der Nutzer:innen-Beziehung" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Lösung |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass der Anfragebody gültige Werte für `braze_id` und `rel_kind` enthält. |
| `404` | Beziehung oder Objekt nicht gefunden | Stellen Sie sicher, dass das Objekt, der/die Nutzer:in und die Beziehungsschlüsselwerte alle existieren. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und ob der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch die Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `data_objects.user_relationships.delete` hat und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Löschen der Nutzer:innen-Beziehung" }
{% endapi %}