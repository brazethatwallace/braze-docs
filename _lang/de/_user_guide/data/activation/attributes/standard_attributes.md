---
nav_title: Standardattribute
article_title: Standardattribute
page_order: 0.5
page_type: reference
description: "Dieser Referenzartikel listet die Standardnutzerattribute (reservierte Schlüssel) von Braze sowie die Syntaxanforderungen für jedes Attribut auf."
---

# Standardattribute {#standard-attributes}

> Standardattribute sind vordefinierte Felder, die Braze in jedem Nutzerprofil erkennt. Verwenden Sie diese Seite als Kurzreferenz für den Feldnamen, den Datentyp und das erwartete Format jedes Standardattributs.

Standardattribute (manchmal auch *Standardattribute* oder *reservierte Schlüssel* genannt) unterscheiden sich von [angepassten Attributen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), die speziell für Ihr Unternehmen gelten. Wenn Sie Daten mit einem der auf dieser Seite aufgeführten Feldnamen an Braze senden, speichert Braze diese im vordefinierten Profilfeld, anstatt ein neues angepasstes Attribut zu erstellen.

Sie können Standardattribute über eine der folgenden Methoden festlegen:

- Das [Braze SDK]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)
- Das [User-Attributes-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object) am [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)

{% alert important %}
Standardattributnamen sind case-sensitiv. Verwenden Sie immer Kleinbuchstaben (zum Beispiel `first_name`, nicht `First_Name`). Wenn Schreibweise oder Groß-/Kleinschreibung nicht exakt übereinstimmen, speichert Braze den Wert stattdessen als [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).
{% endalert %}

## Bezeichner {#identifiers}

Bezeichner teilen Braze mit, welches Nutzerprofil aktualisiert oder erstellt werden soll. Jede API-Anfrage und CSV-Zeile muss mindestens einen Bezeichner enthalten. Einzelheiten zur Auswahl des richtigen Bezeichners finden Sie unter [Bezeichner-Auflösung]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).

| Feld | Datentyp | Format und Hinweise |
|---|---|---|
| `external_id` | String | Ein eindeutiger Nutzerbezeichner, den Sie zuweisen. Nachdem er in einem Profil festgelegt wurde, verwendet Braze ihn, um die Nutzer:innen geräteübergreifend zu erkennen. Kann nach dem Hinzufügen nicht entfernt werden. |
| `braze_id` | String | Ein von Braze zugewiesener Bezeichner, der erstellt wird, wenn das SDK ein Gerät zum ersten Mal erkennt. Schreibgeschützt. Kann nicht bearbeitet werden. |
| `user_alias` | Objekt | Ein Objekt mit `alias_name` (String) und `alias_label` (String), das zur Identifizierung von Nutzer:innen ohne `external_id` verwendet wird. Schließt sich mit `external_id` in derselben Anfrage gegenseitig aus. |
| `email` | String | Kann als Bezeichner verwendet werden, wenn `external_id` und `user_alias` fehlen. Hat Vorrang vor `phone`, wenn beide gesendet werden. |
| `phone` | String | Kann als Bezeichner verwendet werden, wenn `external_id`, `user_alias` und `email` fehlen. Verwenden Sie das [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format)-Format (zum Beispiel `+14155552671`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Profilfelder {#profile-fields}

Diese Felder erfassen demografische, Kontakt- und Standortdaten Ihrer Nutzer:innen.

| Feld | Datentyp | Format und Hinweise |
|---|---|---|
| `first_name` | String | Der Vorname der Nutzer:innen (zum Beispiel `Jane`). |
| `last_name` | String | Der Nachname der Nutzer:innen (zum Beispiel `Doe`). |
| `email` | String | Die E-Mail-Adresse der Nutzer:innen (zum Beispiel `jane.doe@braze.com`). |
| `phone` | String | Die Telefonnummer der Nutzer:innen. Verwenden Sie das [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format)-Format (zum Beispiel `+14155552671`). |
| `dob` | String | Geburtsdatum im Format `YYYY-MM-DD` (zum Beispiel `1988-02-14`). Ermöglicht Targeting nach Geburtstagen. |
| `gender` | String | Einer der Werte `M`, `F`, `O` (andere), `N` (nicht zutreffend), `P` (möchte nicht angeben) oder `null` (unbekannt). |
| `country` | String | Ein Ländercode im [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1)-Format (zum Beispiel `US`, `GB`). Das Setzen von `country` über CSV-Import oder API verhindert, dass das SDK es automatisch erfasst. |
| `home_city` | String | Der Wohnort der Nutzer:innen (zum Beispiel `London`). |
| `language` | String | Ein Sprachcode im [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)-Format (zum Beispiel `en`). Siehe die [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes). Das Setzen von `language` über CSV-Import oder API verhindert, dass das SDK es automatisch erfasst. |
| `time_zone` | String | Ein Zeitzonenname aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (zum Beispiel `America/New_York` oder `Eastern Time (US & Canada)`). |
| `current_location` | Objekt | Ein Objekt mit `longitude` und `latitude` (zum Beispiel `{"longitude": -73.991443, "latitude": 40.753824}`). |
| `image_url` | String | Eine URL zum Profilbild der Nutzer:innen. Maximal 1.024 Zeichen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Abo und Einwilligung {#subscription-and-consent}

Diese Felder steuern, wie Nutzer:innen Nachrichten über verschiedene Kanäle erhalten. Das Aktualisieren dieser Felder zählt nicht zur Datenpunkt-Nutzung.

| Feld | Datentyp | Format und Hinweise |
|---|---|---|
| `email_subscribe` | String | Einer der Werte `opted_in` (hat sich ausdrücklich für den E-Mail-Empfang angemeldet), `unsubscribed` (hat sich ausdrücklich von E-Mails abgemeldet) oder `subscribed` (weder angemeldet noch abgemeldet). |
| `push_subscribe` | String | Einer der Werte `opted_in`, `unsubscribed` oder `subscribed`. Gleiche Definitionen wie bei `email_subscribe`. |
| `subscription_groups` | Array von Objekten | Ein Array, in dem jedes Objekt eine `subscription_group_id` (String) und einen `subscription_state` (`subscribed` oder `unsubscribed`) enthält. Zum Beispiel: `[{"subscription_group_id": "abc-123", "subscription_state": "subscribed"}]`. |
| `email_open_tracking_disabled` | Boolescher Wert | `true` oder `false`. Setzen Sie den Wert auf `true`, um das E-Mail-Öffnungs-Tracking-Pixel für diese:n Nutzer:in zu deaktivieren. Nur für SparkPost und SendGrid verfügbar. |
| `email_click_tracking_disabled` | Boolescher Wert | `true` oder `false`. Setzen Sie den Wert auf `true`, um das E-Mail-Klick-Tracking für diese:n Nutzer:in zu deaktivieren. Nur für SparkPost und SendGrid verfügbar. |
| `marked_email_as_spam_at` | String | Zeitstempel, zu dem die E-Mail der Nutzer:innen als Spam markiert wurde. Verwenden Sie das [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-Format. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Einzelheiten zur Einrichtung von Abo-Gruppen finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups).

## Sitzungen und Engagement {#sessions-and-engagement}

Diese Felder erfassen, wann Nutzer:innen zum ersten oder letzten Mal mit Ihrer App interagiert haben. Das SDK zeichnet sie automatisch auf; Sie legen sie in der Regel nur über API oder CSV fest, wenn Sie von einer anderen Plattform migrieren.

| Feld | Datentyp | Format und Hinweise |
|---|---|---|
| `date_of_first_session` | String | Das Datum, an dem die Nutzer:innen die App zum ersten Mal verwendet haben. Verwenden Sie das [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-Format oder eines der folgenden: `yyyy-MM-ddTHH:mm:ss:SSSZ`, `yyyy-MM-ddTHH:mm:ss`, `yyyy-MM-dd HH:mm:ss`, `yyyy-MM-dd`, `MM/dd/yyyy` oder `ddd MM dd HH:mm:ss.TZD YYYY`. |
| `date_of_last_session` | String | Das Datum, an dem die Nutzer:innen die App zuletzt verwendet haben. Gleiche akzeptierte Formate wie bei `date_of_first_session`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Push-Token {#push-tokens}

Verwenden Sie diese Felder, wenn Sie Push-Token von einer anderen Plattform migrieren. Nach der Integration des Braze SDK werden Push-Token automatisch erfasst. Eine Migrationsanleitung finden Sie unter [Push-Token migrieren]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens).

| Feld | Datentyp | Format und Hinweise |
|---|---|---|
| `push_tokens` | Array von Objekten | Ein Array, in dem jedes Objekt eine `app_id` (String) und ein `token` (String) enthält. Optional kann eine `device_id` (String) angegeben werden. Zum Beispiel: `[{"app_id": "YOUR_APP_ID", "token": "abcd", "device_id": "optional_device_id"}]`. |
| `push_token_import` | Boolescher Wert | Top-Level-Flag (nicht in `attributes` verschachtelt). Setzen Sie den Wert auf `true`, um ältere Push-Token für anonyme Nutzer:innen ohne `external_id` zu importieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Social-Media-Profil {#social-profile}

Diese Felder speichern Daten aus Social-Media-Integrationen.

| Feld | Datentyp | Format und Hinweise |
|---|---|---|
| `facebook` | Objekt | Ein Objekt, das `id` (String), `likes` (String-Array) oder `num_friends` (Integer) enthalten kann. |
| `twitter` | Objekt | Ein Objekt, das `id` (Integer), `screen_name` (String, X-Handle), `followers_count` (Integer), `friends_count` (Integer) oder `statuses_count` (Integer) enthalten kann. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## API-Beispiel {#api-example}

Die folgende Anfrage setzt Standardattribute für zwei Nutzer:innen über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
    {
      "external_id": "user1",
      "first_name": "Alex",
      "last_name": "Doe",
      "email": "jane.doe@example.com",
      "country": "US",
      "language": "en",
      "time_zone": "America/New_York",
      "dob": "1988-02-14",
      "email_subscribe": "opted_in"
    },
    {
      "external_id": "user2",
      "first_name": "Alex",
      "phone": "+14155552671",
      "current_location": {
        "longitude": -73.991443,
        "latitude": 40.753824
      },
      "subscription_groups": [
        {
          "subscription_group_id": "abc-123",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```

Den vollständigen API-Vertrag finden Sie unter [User-Attributes-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## CSV-Beispiel {#csv-example}

Die folgende CSV-Datei aktualisiert Standardattribute für zwei Nutzer:innen. Spaltenüberschriften müssen exakt mit den Feldnamen in diesem Artikel übereinstimmen. Überschriften, die nicht übereinstimmen (zum Beispiel `First_name` statt `first_name`), werden als angepasste Attribute importiert.

```plaintext
external_id,first_name,last_name,email,country,language,dob,email_subscribe
user1,Jane,Doe,jane.doe@example.com,US,en,1988-02-14,opted_in
user2,Alex,Smith,alex.smith@example.com,GB,en,1992-09-30,subscribed
```

Einige Standardattribute können nicht über CSV-Import festgelegt werden. Arrays, Push-Token und verschachtelte Objekte müssen stattdessen über die API oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) gesendet werden. Die vollständige Liste der CSV-unterstützten Felder und Importschritte finden Sie unter [Standardattribute]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#default-attributes).

## Hinweise {#considerations}

Beachten Sie die folgenden Punkte bei der Arbeit mit Standardattributen:

- **Feldnamen sind case-sensitiv.** Verwenden Sie immer Kleinbuchstaben. Eine Überschrift oder ein Schlüssel, der nicht exakt mit einem Standardattributnamen übereinstimmt, wird als angepasstes Attribut behandelt.
- **Die automatische SDK-Erfassung wird unterdrückt, wenn Sie Werte über API oder CSV festlegen.** Wenn Sie `country` oder `language` über API oder CSV festlegen, stoppt Braze die automatische Erfassung dieser Felder durch das SDK für diese:n Nutzer:in.
- **`null` entfernt einen Wert.** Setzen Sie ein Standardattribut auf `null`, um es aus dem Profil zu entfernen. Einige Felder, darunter `external_id` und `user_alias`, können nach dem Festlegen nicht entfernt werden.
- **Leere CSV-Werte überschreiben nicht.** Eine leere Zelle in einem CSV-Import behält den bestehenden Wert im Profil bei. Um einen Wert zu löschen, verwenden Sie die API.
- **Zeitzonen sind standardmäßig UTC.** Datumsstrings ohne Offset werden als Mitternacht UTC interpretiert und in der Zeitzone Ihres Workspace angezeigt. Um eine Zeitzone anzugeben, fügen Sie einen UTC-Offset hinzu (zum Beispiel `2024-11-10T18:00:00-05:00`).

## Verwandte Seiten {#related-pages}

- [User-Attributes-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object) — Vollständiger API-Vertrag für das Attributes-Objekt.
- [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) — REST-Endpunkt zum Erstellen und Aktualisieren von Nutzerprofilen.
- [Nutzerattribute festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes) — SDK-Methoden zum Festlegen von Standard- und angepassten Attributen.
- [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) — Standardattribute über eine CSV-Datei hochladen.
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) — Attribute definieren, die speziell für Ihr Unternehmen gelten.
- [Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types) — Referenz für unterstützte Datentypen.