---
nav_title: "PUT: Nutzer:innen-Beziehung ersetzen"
article_title: "PUT: Nutzer:innen-Beziehung ersetzen"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Ersetzen von Nutzer:innen-Beziehungen."
---
{% api %}
# Nutzer:innen-Beziehung ersetzen {#replace-user-relationship}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Nutzer:innen-Beziehung zu erstellen oder zu ersetzen.

{% alert important %}
Data Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Data-Objects-API-Schlüssel-Berechtigungen unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `data_objects.user_relationships.update`.

## Rate-Limit

Dieser Endpunkt befindet sich im Data-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Objekttyp |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter zum Ersetzen von Nutzer:innen-Beziehungen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Request-Body-Parameter für den Endpunkt `/data_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `braze_id` | Erforderlich | String | Braze-Nutzer:innen-ID |
| `rel_kind` | Erforderlich | String | Beziehungstyp |
| `attributes` | Optional | Objekt | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter zum Ersetzen von Nutzer:innen-Beziehungen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispiel-Payload und eine cURL-Beispielanfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel ersetzt die Attribute der `account_user`-Beziehung zwischen dem/der Nutzer:in und `acct-123` und überschreibt dabei alle zuvor gespeicherten Attribute.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}'
```

## Antwort {#response}

Dieser Abschnitt enthält eine erfolgreiche Beispielantwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "admin" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `user_relationship` | Erforderlich | Objekt | Erstellter oder ersetzter Nutzer:innen-Beziehungsdatensatz |
| `user_relationship.type_name` | Erforderlich | String | Maschinenname des Data-Object-Typs |
| `user_relationship.external_id` | Erforderlich | String | Data-Object-Bezeichner |
| `user_relationship.rel_kind` | Erforderlich | String | Wert des Beziehungstyps |
| `user_relationship.user` | Erforderlich | Objekt | Verknüpftes Nutzer:innen-Objekt |
| `user_relationship.user.braze_id` | Erforderlich | String | Braze-Nutzer:innen-Bezeichner |
| `user_relationship.attributes` | Erforderlich | Objekt | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter zum Ersetzen von Nutzer:innen-Beziehungen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und deren Behebung auf.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass `rel_kind` für den Objekttyp gültig ist und `attributes` dem Beziehungsschema entsprechen. |
| `404` | Beziehung oder Objekt nicht gefunden (`data-object-relationship-not-found`) | Stellen Sie sicher, dass das Objekt, der/die Nutzer:in und die Beziehungsschlüsselwerte alle existieren. |
| `422` | Objekte-pro-Nutzer:in-Limit erreicht (`data-objects-per-user-limit-exceeded`) oder Nutzer:innen-pro-Objekt-Limit erreicht (`users-per-data-object-limit-exceeded`) | Reduzieren Sie die Anzahl der Beziehungen für den/die Nutzer:in oder das Objekt, oder kontaktieren Sie den Braze-Support bezüglich Ihrer Workspace-Limits. |
| `401` | Fehlender oder ungültiger Representational State Transfer-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und ob der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder Anfrage wird durch Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel die Berechtigung `data_objects.user_relationships.update` hat und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, sofern konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Ersetzen von Nutzer:innen-Beziehungen" }
{% endapi %}