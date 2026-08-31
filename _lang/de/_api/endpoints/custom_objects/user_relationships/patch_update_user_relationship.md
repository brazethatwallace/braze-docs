---
nav_title: "PATCH: Nutzer:innen-Beziehung aktualisieren"
article_title: "PATCH: Nutzer:innen-Beziehung aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Nutzer:innen-Beziehung aktualisieren“."
---
{% api %}
# Nutzer:innen-Beziehung aktualisieren {#update-user-relationship}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Attribute in eine bestehende Nutzer:innen-Beziehung zusammenzuführen.

{% alert important %}
Custom Objects befindet sich derzeit im Early Access. Ihr Workspace muss aktiviert sein, bevor die API-Schlüssel-Berechtigungen für Custom Objects unter **Einstellungen** > **API-Schlüssel** angezeigt werden.
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter für die Aktualisierung der Nutzer:innen-Beziehung" }

## Anfrageparameter {#request-parameters}

Die folgende Tabelle listet und beschreibt die JSON-Anfragebody-Parameter für den Endpunkt `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `braze_id` | Erforderlich | String | Braze-Nutzer:innen-ID |
| `rel_kind` | Erforderlich | String | Art der Beziehung |
| `attributes` | Optional | Objekt | Beziehungsattribute zum Zusammenführen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter für die Aktualisierung der Nutzer:innen-Beziehung" }

## Beispielanfrage {#example-request}

Dieser Abschnitt enthält ein JSON-Beispielpayload und eine cURL-Beispielanfrage.

### Beispielpayload der Anfrage {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "billing_admin"
  }
}
```

### cURL-Beispielanfrage {#sample-curl-request}

Dieses Beispiel ändert das Attribut `role` der bestehenden `account_user`-Beziehung auf `billing_admin`, wobei die anderen Attribute der Beziehung unverändert bleiben.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "billing_admin"
  }
}'
```

## Antwort {#response}

Dieser Abschnitt enthält eine beispielhafte erfolgreiche Antwort und die Antwortfelder.

### Beispiel einer erfolgreichen Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortbody zurückgeben.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "billing_admin" }
  }
}
```

### Antwortparameter {#response-parameters}

Die folgende Tabelle listet und beschreibt die Felder in einer erfolgreichen Antwort.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `user_relationship` | Erforderlich | Objekt | Aktualisierter Datensatz der Nutzer:innen-Beziehung |
| `user_relationship.type_name` | Erforderlich | String | Maschinenname des Custom-Object-Typs |
| `user_relationship.external_id` | Erforderlich | String | Custom-Object-Bezeichner |
| `user_relationship.rel_kind` | Erforderlich | String | Wert der Beziehungsart |
| `user_relationship.user` | Erforderlich | Objekt | Verknüpftes Nutzer:innen-Objekt |
| `user_relationship.user.braze_id` | Erforderlich | String | Braze-Nutzer:innen-Bezeichner |
| `user_relationship.attributes` | Erforderlich | Objekt | Beziehungsattribute nach dem Zusammenführen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Antwortparameter für die Aktualisierung der Nutzer:innen-Beziehung" }

## Fehler {#errors}

Die folgende Tabelle listet häufige Fehler für diesen Endpunkt und wie Sie diese beheben können.

| Status | Ursache | Hinweis |
|---|---|---|
| `400` | Validierungsfehler | Stellen Sie sicher, dass `rel_kind` für den Objekttyp gültig ist und `attributes` dem Beziehungsschema entsprechen. |
| `404` | Beziehung nicht gefunden (`custom-object-relationship-not-found`) | Stellen Sie sicher, dass das Objekt, die Nutzer:in und die Beziehungsschlüsselwerte vorhanden sind. |
| `401` | Fehlender oder ungültiger REST-API-Schlüssel | Überprüfen Sie, ob der `Authorization`-Header `Bearer YOUR_REST_API_KEY` verwendet und der Schlüssel aktiv ist. |
| `403` | API-Schlüssel hat keine Berechtigung oder die Anfrage wird durch eine Allowlist blockiert | Stellen Sie sicher, dass der Schlüssel über die Berechtigung `custom_objects.user_relationships.update` verfügt und dass Ihre Quell-IP auf der Allowlist des Schlüssels steht, falls konfiguriert. |
| `429` | Rate-Limit überschritten | Wiederholen Sie die Anfrage nach `X-RateLimit-Reset` und reduzieren Sie die Anfragehäufigkeit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehler bei der Aktualisierung der Nutzer:innen-Beziehung" }
{% endapi %}