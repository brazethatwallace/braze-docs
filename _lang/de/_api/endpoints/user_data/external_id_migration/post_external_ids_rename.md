---
nav_title: "POST: Externe ID umbenennen"
article_title: "POST: Externe ID umbenennen"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Endpunkt „Externe IDs umbenennen“."

---
{% api %}
# Externe ID umbenennen {#rename-external-id}
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die externen IDs Ihrer Nutzer:innen umzubenennen.

Sie können bis zu 50 Umbenennungsobjekte pro Anfrage senden.

Dieser Endpunkt legt eine neue (primäre) `external_id` für die Nutzer:innen fest und markiert die bestehende `external_id` als veraltet. Das bedeutet, dass Nutzer:innen über beide `external_id` identifiziert werden können, bis die veraltete ID entfernt wird. Mehrere externe IDs ermöglichen einen Migrationszeitraum, sodass ältere Versionen Ihrer Apps, die das frühere Namensschema für externe IDs verwenden, nicht beeinträchtigt werden.

Nachdem Ihr altes Namensschema nicht mehr verwendet wird, empfehlen wir dringend, veraltete externe IDs über den [Endpunkt `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) zu entfernen.

{% alert warning %}
Stellen Sie sicher, dass Sie veraltete externe IDs mit dem Endpunkt `/users/external_ids/remove` anstelle von `/users/delete` entfernen. Wenn Sie eine Anfrage an `/users/delete` mit der veralteten externen ID senden, wird das Nutzerprofil vollständig gelöscht und kann nicht rückgängig gemacht werden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `users.external_ids.rename`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Erforderlich | Array von Objekten zum Umbenennen externer Bezeichner | Sehen Sie sich das Anfragebeispiel und die folgenden Einschränkungen für die Struktur des Objekts zum Umbenennen externer Bezeichner an. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

Beachten Sie Folgendes:

- Die `current_external_id` muss die primäre ID der Nutzer:innen sein und darf keine veraltete ID sein.
- Die `new_external_id` darf nicht bereits als primäre ID oder als veraltete ID verwendet werden.
- Die `current_external_id` und `new_external_id` dürfen nicht identisch sein.

## Anfragebeispiel {#request-example}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Antwort {#response}

Die Antwort bestätigt alle erfolgreichen Umbenennungen sowie erfolglose Umbenennungen mit den zugehörigen Fehlern. Fehlermeldungen im Feld `rename_errors` referenzieren den Index des Objekts im Array der ursprünglichen Anfrage.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

Das Feld `message` gibt `success` für jede gültige Anfrage zurück. Spezifischere Fehler werden im Array `rename_errors` erfasst. Das Feld `message` gibt einen Fehler zurück in folgenden Fällen:

- Ungültiger API-Schlüssel
- Leeres `external_id_renames`-Array
- `external_id_renames`-Array mit mehr als 50 Objekten
- Rate-Limit erreicht (mehr als 1.000 Anfragen pro Minute)

## Häufig gestellte Fragen {#frequently-asked-questions}

### Hat dies Auswirkungen auf MAU? {#does-this-impact-mau}
Nein, da die Anzahl der Nutzer:innen gleich bleibt – sie haben lediglich eine neue `external_id`.

### Ändert sich das historische Verhalten der Nutzer:innen? {#does-user-behavior-change-historically}
Nein, da es sich weiterhin um dieselben Nutzer:innen handelt und ihr gesamtes historisches Verhalten nach wie vor mit ihnen verknüpft ist.

### Kann dies in Entwicklungs- oder Staging-Workspaces ausgeführt werden? {#can-it-be-run-on-development-or-staging-workspaces}
Ja. Wir empfehlen sogar dringend, eine Testmigration in einem Staging- oder Entwicklungs-Workspace durchzuführen und sicherzustellen, dass alles reibungslos funktioniert, bevor Sie die Migration mit Produktionsdaten ausführen.

### Werden dabei Datenpunkte protokolliert? {#does-this-log-data-points}
Dieses Feature protokolliert keine Datenpunkte.

### Welcher Zeitraum wird für die Deprecation empfohlen? {#what-is-the-recommended-deprecation-period}
Es gibt keine feste Grenze, wie lange Sie veraltete externe IDs beibehalten können. Wir empfehlen jedoch dringend, sie zu entfernen, sobald es nicht mehr notwendig ist, Nutzer:innen über die veraltete ID zu referenzieren.

{% endapi %}