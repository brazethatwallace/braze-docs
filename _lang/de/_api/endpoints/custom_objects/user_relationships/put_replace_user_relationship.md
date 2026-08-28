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
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Nutzer:innen-Beziehung zu erstellen oder zu ersetzen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die Berechtigungen für den Custom-Objects-API-Schlüssel unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.user_relationships.update`.

## Rate-Limit

Dieser Endpunkt befindet sich im Custom-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Objekttyp |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter zum Ersetzen von Nutzer:innen-Beziehungen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragekörperparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `braze_id` | Erforderlich | String | Braze-Nutzer:innen-ID |
| `rel_kind` | Erforderlich | String | Art der Beziehung |
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

Dieses Beispiel ersetzt die Attribute der `account_user`-Beziehung zwischen dem/der Nutzer:in und `acct-123` und überschreibt alle zuvor darauf gespeicherten Attribute.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
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

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

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

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `user_relationship` | Erforderlich | Objekt | Erstellter oder ersetzter Nutzer:innen-Beziehungsdatensatz |
| `user_relationship.type_name` | Erforderlich | String | Maschinenname des Custom-Object-Typs |
| `user_relationship.external_id` | Erforderlich | String | Custom-Object-Bezeichner |
| `user_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `user_relationship.user` | Erforderlich | Objekt | Verknüpftes Nutzer:innen-Objekt |
| `user_relationship.user.braze_id` | Erforderlich | String | Braze-Nutzer:innen-Bezeichner |
| `user_relationship.attributes` | Erforderlich | Objekt | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter zum Ersetzen von Nutzer:innen-Beziehungen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Validierungsfehler | Bestätigen Sie, dass `rel_kind` für den Objekttyp gültig ist und `attributes` dem Beziehungsschema entsprechen. |
| `404` | Beziehung oder Objekt nicht gefunden (`custom-object-relationship-not-found`) | Bestätigen Sie, dass das Objekt, der/die Nutzer:in und die Beziehungsschlüsselwerte alle existieren. |
| `422` | Limit für Objekte pro Nutzer:in erreicht (`custom-objects-per-user-limit-exceeded`) oder Limit für Nutzer:innen pro Objekt erreicht (`users-per-custom-object-limit-exceeded`) | Reduzieren Sie die Anzahl der Beziehungen für den/die Nutzer:in oder das Objekt, oder kontaktieren Sie den Braze-Support bezüglich Ihrer Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Allowlist blockiert | Bestätigen Sie, dass der Schlüssel die Berechtigung `custom_objects.user_relationships.update` hat und dass Ihre Quell-IP auf der Schlüssel-Allowlist steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler beim Ersetzen von Nutzer:innen-Beziehungen" }
{% endapi %}