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

Dieser Endpunkt legt eine neue (primäre) `external_id` für die Nutzer:innen fest und markiert die bestehende `external_id` als veraltet. Das bedeutet, dass Nutzer:innen über beide `external_id` identifiziert werden können, bis die veraltete ID entfernt wird. Mehrere externe IDs ermöglichen einen Migrationszeitraum, sodass ältere Versionen Ihrer Apps, die das frühere Namensschema für externe IDs verwenden, nicht beeinträchtigt werden. Das Profil bleibt unter beiden Bezeichnern während des Migrationszeitraums voll funktionsfähig – das Braze SDK or Software-Development-Kit, die Representational State Transfer API und die Messaging-Pipelines können die Nutzer:innen weiterhin über beide IDs referenzieren, bis die veraltete ID explizit entfernt wird.

Nachdem Ihr altes Namensschema nicht mehr verwendet wird, empfehlen wir dringend, veraltete externe IDs über den [Endpunkt `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) zu entfernen.

{% alert warning %}
Stellen Sie sicher, dass Sie veraltete externe IDs mit dem Endpunkt `/users/external_ids/remove` anstelle von `/users/delete` entfernen. Wenn Sie eine Anfrage an `/users/delete` mit der veralteten externen ID senden, wird das Kundenprofil or Nutzerprofil vollständig gelöscht und kann nicht rückgängig gemacht werden.
{% endalert %}

## Funktionsweise der Umbenennung {#how-renaming-works}

Wenn Sie diesen Endpunkt aufrufen, weist er einem Kundenprofil or Nutzerprofil eine neue primäre `external_id` zu und konvertiert gleichzeitig die bisherige primäre `external_id` in eine veraltete externe ID. Nach einer erfolgreichen Umbenennung enthält das Kundenprofil or Nutzerprofil genau eine primäre `external_id` (den neuen Wert) und eine veraltete externe ID (den alten Wert).

Nachfolgende Umbenennungsaufrufe für dasselbe Profil sind zulässig: Jede Umbenennung erzeugt eine zusätzliche veraltete externe ID, sodass ein Profil im Laufe der Zeit eine primäre `external_id` und mehrere veraltete externe IDs ansammeln kann. Der Wert von `new_external_id` darf jedoch nicht bereits in einem Braze-Profil vorhanden sein – weder als primäre noch als veraltete externe ID.

Der Endpunkt protokolliert keine Datenpunkte und hat keinen Einfluss auf MAU or monatlich aktive:r Nutzer:in-Zählungen. Alle historischen Nutzerdaten – Ereignisse, Käufe, Attribute, Campaign-Engagement – bleiben mit demselben Profil verknüpft.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics) mit der Berechtigung `users.external_ids.rename`.

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

- Die `current_external_id` muss die primäre ID der Nutzer:innen sein und darf keine veraltete ID sein. Wenn der als `current_external_id` übergebene Wert selbst eine veraltete ID im Profil ist, schlägt der Aufruf fehl. Verwenden Sie vor einem erneuten Versuch den [Endpunkt `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier), um zu bestätigen, welche ID derzeit die primäre ist.
- Die `new_external_id` darf nicht bereits als primäre ID oder als veraltete ID verwendet werden. Der Versuch, auf eine ID umzubenennen, die bereits als veraltete ID gespeichert ist, gibt den Fehler „new_external_id is already in use“ zurück.
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

## Massenmigrationen {#bulk-migrations}

Für Migrationen mit großen Nutzerpopulationen fassen Sie Nutzer:innen in Gruppen von bis zu 50 zusammen und senden jede Gruppe als separaten API-Aufruf. Der Endpunkt unterliegt einem Rate-Limit von 1.000 Anfragen pro Minute. Bei maximaler Gruppengröße (50 Objekte pro Anfrage) ermöglicht dies bis zu 50.000 Umbenennungen von Nutzer:innen pro Minute.

Jedes Umbenennungsobjekt in der Gruppe wird unabhängig verarbeitet. Ein Fehler bei einem Objekt blockiert nicht die anderen in derselben Anfrage. Der Antworttext unterscheidet erfolgreiche Umbenennungen (aufgelistet im Array `external_ids`) von fehlgeschlagenen (aufgelistet im Array `rename_errors` mit einem Indexverweis auf die Position des fehlgeschlagenen Objekts im Anfrage-Array).

Bei der Durchführung von Massenmigrationen:

1. Iterieren Sie durch die gesamte Nutzerpopulation in Gruppen von bis zu 50 Paaren.
2. Prüfen Sie bei jeder Antwort sowohl `external_ids` (Erfolg) als auch `rename_errors` (Fehler), um Nutzer:innen zu identifizieren, für die ein erneuter Versuch erforderlich ist.
3. Sammeln Sie fehlgeschlagene Objekte und planen Sie separate Wiederholungsgruppen. Häufige Fehlerursachen sind, dass die `new_external_id` bereits verwendet wird oder die `current_external_id` eine veraltete ID statt einer primären ID ist.
4. Protokollieren Sie Erfolge und Fehler in Ihren eigenen Aufzeichnungen, damit der Migrationsstatus außerhalb von Braze nachverfolgt wird.

## Aktuelle externe ID überprüfen {#verifying-the-current-external-id}

Während einer Migration müssen Sie möglicherweise bestätigen, welche externe ID der aktive primäre Bezeichner eines bestimmten Profils ist – zum Beispiel, um festzustellen, ob bestimmte Nutzer:innen bereits migriert wurden, oder bei der Fehlerbehebung einer fehlgeschlagenen Umbenennung. Verwenden Sie dazu den [Endpunkt `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier).

Der Export-Endpunkt löst sowohl primäre als auch veraltete externe IDs zum selben zugrunde liegenden Profil auf und gibt in der Antwort immer die aktuelle primäre `external_id` zurück. Das bedeutet, dass Sie jeden bekannten Bezeichner für Nutzer:innen abfragen können – alt oder neu – und die Antwort die kanonische primäre ID enthält. Dies ist eine zuverlässige Methode, um den Migrationsstatus zu ermitteln.

Um nur die externe ID zu prüfen (anstatt das vollständige Profil abzurufen), übergeben Sie `fields_to_export` nur mit dem Feld `external_id`.

## Empfohlener Migrations-Workflow {#recommended-migration-workflow}

Für die meisten Migrationsszenarien ist die empfohlene Reihenfolge:

1. **In Staging testen** – Führen Sie den vollständigen Umbenennungs- und Überprüfungsablauf in einem Entwicklungs- oder Staging-Workspace durch, bevor Sie die Produktionsumgebung bearbeiten.
2. **In Gruppen umbenennen** – Verwenden Sie den Endpunkt `/users/external_ids/rename` in Gruppen von bis zu 50, behandeln Sie `rename_errors` bei jeder Antwort und stellen Sie fehlgeschlagene Paare für einen erneuten Versuch in die Warteschlange.
3. **Überprüfen** – Prüfen Sie nach jeder Gruppe (oder am Ende der Migration) stichprobenartig Profile über `/users/export/ids`, um zu bestätigen, dass die erwartete primäre `external_id` gesetzt ist.
4. **Deprecation-Zeitraum beibehalten** – Halten Sie veraltete externe IDs so lange aktiv, wie ein System (einschließlich älterer App-Versionen im Feld) möglicherweise noch die alten IDs referenziert. Überstürzen Sie diesen Schritt nicht.
5. **Veraltete IDs entfernen** – Sobald bestätigt ist, dass alle Systeme die neuen IDs verwenden, nutzen Sie [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) in Gruppen von bis zu 50 zur Bereinigung.

Wenn Sie auch Ihre SDK or Software-Development-Kit-Integration migrieren (zum Beispiel den an `changeUser` übergebenen Wert ändern), koordinieren Sie die API-seitige Umbenennung mit dem App-Release-Zeitplan, sodass die neue externe ID sowohl auf dem Server als auch auf dem Client verwendet wird, bevor veraltete IDs entfernt werden.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Hat dies Auswirkungen auf MAU or monatlich aktive:r Nutzer:in? {#does-this-impact-mau}
Nein, da die Anzahl der Nutzer:innen gleich bleibt – sie haben lediglich eine neue `external_id`.

### Ändert sich das historische Verhalten der Nutzer:innen? {#does-user-behavior-change-historically}
Nein, da es sich weiterhin um dieselben Nutzer:innen handelt und ihr gesamtes historisches Verhalten nach wie vor mit ihnen verknüpft ist.

### Kann dies in Entwicklungs- oder Staging-Workspaces ausgeführt werden? {#can-it-be-run-on-development-or-staging-workspaces}
Ja. Wir empfehlen sogar dringend, eine Testmigration in einem Staging- oder Entwicklungs-Workspace durchzuführen und sicherzustellen, dass alles reibungslos funktioniert, bevor Sie die Migration mit Produktionsdaten ausführen.

### Werden dabei Datenpunkte protokolliert? {#does-this-log-data-points}
Dieses Feature protokolliert keine Datenpunkte.

### Welcher Zeitraum wird für die Deprecation empfohlen? {#what-is-the-recommended-deprecation-period}
Es gibt keine feste Grenze, wie lange Sie veraltete externe IDs beibehalten können. Wir empfehlen jedoch dringend, sie zu entfernen, sobald es nicht mehr notwendig ist, Nutzer:innen über die veraltete ID zu referenzieren.

### Wie viele veraltete externe IDs kann ein Profil haben? {#how-many-deprecated-external-ids-can-a-profile-have}
Ein Kundenprofil or Nutzerprofil kann eine primäre `external_id` und eine beliebige Anzahl veralteter externer IDs enthalten, die durch aufeinanderfolgende Umbenennungsvorgänge angesammelt wurden. Es gibt keine dokumentierte Obergrenze für die Anzahl veralteter IDs, die ein einzelnes Profil haben kann, aber Braze empfiehlt, sie zu entfernen, sobald sie nicht mehr benötigt werden.

{% endapi %}