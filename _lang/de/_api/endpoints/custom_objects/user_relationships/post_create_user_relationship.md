---
nav_title: "POST: Nutzer:innen-Beziehung erstellen"
article_title: "POST: Nutzer:innen-Beziehung erstellen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Nutzer:innen-Beziehung erstellen“."
---
{% api %}
# Nutzer:innen-Beziehung erstellen {#create-user-relationship}
{% apimethod post %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine:n Braze-Nutzer:in mit einem Custom Object zu verknüpfen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüsselberechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `custom_objects.user_relationships.create`.

## Rate-Limits {#rate-limit}

Dieser Endpunkt befindet sich im Custom-Objects-Schreib-Bucket mit einem Standardlimit von 50 Anfragen pro Minute.

## Pfadparameter {#path-parameters}

Die folgende Tabelle listet und beschreibt die Pfadparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `type_name` | Erforderlich | String | Objekttyp |
| `external_id` | Erforderlich | String | Objektbezeichner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für Nutzer:innen-Beziehung erstellen" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfrageparameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `braze_id` | Erforderlich | String | Braze-Nutzer:innen-ID |
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `attributes` | Optional | Objekt | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für Nutzer:innen-Beziehung erstellen" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein Beispiel-JSON-Payload und eine Beispiel-cURL-Anfrage.

### Beispiel-Anfrage-Payload {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}
```

### Beispiel-cURL-Anfrage {#sample-curl-request}

Dieses Beispiel verknüpft eine:n Nutzer:in mit `acct-123` als `account_user` und erfasst die `role` als `owner`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}'
```

## Antwort {#response}

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `201` könnte den folgenden Antworttext zurückgeben.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "owner" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `user_relationship` | Erforderlich | Objekt | Erstellter Nutzer:innen-Beziehungsdatensatz |
| `user_relationship.type_name` | Erforderlich | String | Maschinenname des Custom-Object-Typs |
| `user_relationship.external_id` | Erforderlich | String | Custom-Object-Bezeichner |
| `user_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `user_relationship.user` | Erforderlich | Objekt | Verknüpftes Nutzer:innen-Objekt |
| `user_relationship.user.braze_id` | Erforderlich | String | Braze-Nutzer:innen-Bezeichner |
| `user_relationship.attributes` | Erforderlich | Objekt | Beziehungsattribute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für Nutzer:innen-Beziehung erstellen" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie diese behoben werden können.

| Status | Ursache | Anleitung |
|---|---|---|
| `400` | Unbekannter `rel_kind` für den Typ oder Schema-Validierungsfehler | Stellen Sie sicher, dass `rel_kind` für den Objekttyp gültig ist und die `attributes` dem Beziehungsschema entsprechen. |
| `404` | Typ oder Objekt nicht gefunden | Stellen Sie sicher, dass sowohl `type_name` als auch `external_id` im Workspace vorhanden sind. |
| `409` | Doppelte Beziehung (`duplicate-user-relationship`) | Verwenden Sie `PUT`, um die bestehende Beziehung zu ersetzen, oder löschen Sie sie, bevor Sie sie erneut erstellen. |
| `422` | Limit für Objekte pro Nutzer:in erreicht (`custom-objects-per-user-limit-exceeded`) oder Limit für Nutzer:innen pro Objekt erreicht (`users-per-custom-object-limit-exceeded`) | Reduzieren Sie die Anzahl der Beziehungen für die:den Nutzer:in oder das Objekt, oder wenden Sie sich an den Braze-Support bezüglich Ihrer Workspace-Limits. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Zulassungsliste blockiert | Stellen Sie sicher, dass der Schlüssel über `custom_objects.user_relationships.create` verfügt und dass Ihre Quell-IP auf der Zulassungsliste des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Versuchen Sie es nach `X-RateLimit-Reset` erneut und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler bei Nutzer:innen-Beziehung erstellen" }
{% endapi %}