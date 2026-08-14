---
nav_title: "Nutzer:innen-Attribute-Objekt"
article_title: "API-Nutzer:innen-Attribute-Objekt"
page_order: 11
page_type: reference
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Nutzer:innen-Attribute-Objekts."

---

# Nutzer:innen-Attribute-Objekt {#user-attributes-object}

> Eine API-Anfrage mit beliebigen Feldern im Attributobjekt erstellt oder aktualisiert ein Attribut mit diesem Namen und dem angegebenen Wert im angegebenen Nutzerprofil.

Verwenden Sie die Feldnamen des Braze-Nutzerprofils (wie nachfolgend aufgelistet oder alle im Abschnitt für [Braze-Nutzerprofilfelder](#braze-user-profile-fields) aufgeführten), um diese speziellen Werte im Nutzerprofil im Dashboard zu aktualisieren, oder fügen Sie Ihre eigenen angepassten Attributdaten für die Nutzer:innen hinzu.

## Objektkörper {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
  // Braze User Profile Fields
  "first_name" : "Alex",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
  // Array of objects custom attribute
  "my_array_of_objects_attribute": [{"key": "value"}, {"key": "value"}],
  // Adding to an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$add": [{"key": "value"}] },
  // Removing from an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$remove": [{"$identifier_key": "key", "$identifier_value": "value"}] },
}
```

- [Externe Nutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Nutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases)

{% alert note %}
Verwenden Sie für reguläre angepasste Array-Attribute `add` und `remove` (ohne `$`).

Verwenden Sie für Arrays von Objekten (verschachtelte angepasste Attribute) `$add`, `$remove` und `$update` in `/users/track`-Anfrage-Payloads. Diese Operatoren wenden Änderungen auf Objektebene an, indem sie Bezeichner (`$identifier_key` und `$identifier_value`) abgleichen, und unterstützen In-Place-Aktualisierungen mit `$new_object`.

Verwenden Sie dieses Format, wenn Sie Objekte innerhalb eines bestehenden Arrays anhängen, entfernen oder aktualisieren müssen, während der restliche Array-Zustand erhalten bleibt. Vollständige Anfrage-Beispiele finden Sie unter [Array von Objekten – API-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) und [Array von Objekten – SDK-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).
{% endalert %}

Um ein Profilattribut zu entfernen, setzen Sie es auf `null`. Einige Felder, wie `external_id` und `user_alias`, können nicht entfernt werden, nachdem sie einem Nutzerprofil hinzugefügt wurden.

### Bezeichner-Auflösung {#identifier-resolution}

Sofern Sie keinen [anonymen Push-Token-Import](#push-token-import) durchführen, muss jedes Nutzerattribut-Objekt mindestens einen Bezeichner enthalten: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`. Verwenden Sie nach Möglichkeit nur einen Bezeichner pro Objekt, um Mehrdeutigkeiten darüber zu vermeiden, welches Nutzerprofil aktualisiert oder erstellt wird.

Beachten Sie Folgendes bei der Verwendung von Bezeichnern:

- **`external_id` und `user_alias` schließen sich gegenseitig aus.** Wenn beide im selben Nutzerattribut-Objekt enthalten sind, wird ein Fehler zurückgegeben. Um einem Nutzer, der bereits eine `external_id` hat, einen Alias hinzuzufügen, verwenden Sie den [`/users/alias/new`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_alias).
- **`email` hat Vorrang vor `phone`.** Wenn sowohl `email` als auch `phone` im selben Objekt enthalten sind, verwendet Braze `email` als Bezeichner. Das bedeutet, dass die Attribute auf das mit dieser E-Mail-Adresse verknüpfte Nutzerprofil angewendet werden, auch wenn die Telefonnummer zu einem anderen Profil gehört.

{% alert important %}
Um unerwartetes Verhalten zu vermeiden, verwenden Sie einen einzelnen Bezeichner pro Nutzerattribut-Objekt. Die Angabe mehrerer Bezeichner, die auf verschiedene Nutzerprofile verweisen, kann dazu führen, dass Attribute dem falschen Profil zugewiesen werden.
{% endalert %}

#### Nur bestehende Profile aktualisieren {#update-existing-profiles-only}

Wenn Sie nur bestehende Nutzerprofile in Braze aktualisieren möchten, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Body Ihrer Anfrage übergeben. Wird dieser Wert weggelassen, erstellt Braze ein neues Nutzerprofil, falls die `external_id` noch nicht existiert.

{% alert note %}
Wenn Sie ein Alias-only-Nutzerprofil über den `/users/track`-Endpunkt erstellen, müssen Sie `_update_existing_only` auf `false` setzen. Wenn Sie diesen Wert weglassen, erstellt Braze das Alias-only-Profil nicht.
{% endalert %}

#### Push-Token-Import {#push-token-import}

Bevor Sie Push-Token in Braze importieren, prüfen Sie, ob dies tatsächlich erforderlich ist. Wenn die Braze SDKs eingebunden sind, verwalten sie Push-Token automatisch, ohne dass ein Upload über die API nötig ist.

Falls Sie sie dennoch über die API hochladen müssen, können sie entweder für identifizierte oder anonyme Nutzer:innen hochgeladen werden. Das bedeutet, dass entweder eine `external_id` vorhanden sein muss oder bei anonymen Nutzer:innen das Flag `push_token_import` auf `true` gesetzt sein muss.

{% alert note %}
Beim Import von Push-Token aus anderen Systemen ist eine `external_id` nicht immer verfügbar. Um die Kommunikation mit diesen Nutzer:innen während Ihres Übergangs zu Braze aufrechtzuerhalten, können Sie die Legacy-Token für anonyme Nutzer:innen ohne Angabe einer `external_id` importieren, indem Sie `push_token_import` auf `true` setzen.
{% endalert %}

Wenn `push_token_import` auf `true` gesetzt ist:

* `external_id` und `braze_id` sollten **nicht** angegeben werden
* Das Attribut-Objekt **muss** ein Push-Token enthalten
* Wenn das Token bereits in Braze existiert, wird die Anfrage ignoriert; andernfalls erstellt Braze ein temporäres, anonymes Nutzerprofil für jedes Token, damit Sie diese Personen weiterhin kontaktieren können

Nach dem Import verschiebt Braze automatisch das importierte Push-Token in das Braze-Nutzerprofil, sobald die jeweilige Person die Braze-fähige Version Ihrer App startet, und bereinigt das temporäre Profil.

Braze prüft einmal im Monat, ob anonyme Profile mit dem Flag `push_token_import` vorhanden sind, die kein Push-Token mehr haben. Wenn das anonyme Profil kein Push-Token mehr hat, löscht Braze das Profil. Hat das anonyme Profil jedoch noch ein Push-Token – was darauf hindeutet, dass sich die tatsächliche Person noch nicht auf dem Gerät mit dem betreffenden Push-Token angemeldet hat – unternimmt Braze nichts.

Weitere Informationen finden Sie unter [Push-Token migrieren](#migrate-push-tokens).

#### Datentypen für angepasste Attribute {#custom-attribute-data-types}

Die folgenden Datentypen können als angepasstes Attribut gespeichert werden:

| Datentyp | Hinweise |
| --- | --- |
| Arrays | Angepasste Attribut-Arrays werden unterstützt. Wenn Sie ein Element hinzufügen, wird es am Ende des Arrays angehängt. Wenn das Element bereits existiert, wird es von seiner aktuellen Position an das Ende verschoben.<br><br>Es werden nur eindeutige Werte gespeichert. Beispielsweise ergibt der Import von `['hotdog','hotdog','hotdog','pizza']` das Ergebnis `['hotdog', 'pizza']`.<br><br>Sie können ein Array direkt setzen (z. B. `"my_array_custom_attribute":[ "Value1", "Value2" ]`), mit `"my_array_custom_attribute" : { "add" : ["Value3"] }` zu einem bestehenden Array hinzufügen oder mit `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}` Werte entfernen.<br><br>Die Standard- und Höchstzahl an Elementen in einem Array beträgt 500. Sie können die Höchstzahl der Arrays im Braze-Dashboard unter **Data Settings** > **Custom Attributes** aktualisieren. Weitere Informationen finden Sie unter [Arrays]({{site.baseurl}}/developer_guide/analytics#arrays). |
| Array von Objekten | Verwenden Sie ein Array von Objekten, um eine Liste von Objekten zu definieren, wobei jedes Objekt eine Reihe von Attributen enthält. Verwenden Sie diesen Typ, um mehrere Sätze zusammengehöriger Daten für eine:n Nutzer:in zu speichern, z. B. Hotelaufenthalte, Kaufhistorie oder Präferenzen.<br><br>Definieren Sie beispielsweise ein angepasstes Attribut namens `hotel_stays` in einem Nutzerprofil als Array, wobei jedes Objekt einen separaten Aufenthalt darstellt, mit Attributen wie `hotel_name`, `check_in_date` und `nights_stayed`.<br><br>Arrays von Objekten haben keine Begrenzung der Artikelanzahl, aber eine maximale Größe von 100&nbsp;KB. Wenn eine Aktualisierung dazu führt, dass das Array dieses Limit überschreitet, verwirft Braze die Aktualisierung, und das Attribut bleibt unverändert.<br><br>Verwenden Sie für `/users/track`- und SDK-Payloads `$add`, `$remove` und `$update` für Array-von-Objekten-Operationen. Verwenden Sie `add` und `remove` (ohne `$`) für reguläre angepasste Array-Attribute, die skalare Werte enthalten. Details finden Sie unter [Array von Objekten – API-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example), [Array von Objekten – SDK-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example) und [Array-von-Objekten-Beispiel](#array-of-objects-example). |
| Booleans | `true` oder `false` |
| Datumsangaben | Speichern Sie Datumsangaben im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format (empfohlen) oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Beachten Sie, dass „T“ ein Zeitkennzeichen ist, kein Platzhalter, und nicht geändert oder entfernt werden sollte. <br><br>Datumswerte, die keinem der aufgeführten Formate entsprechen, werden als Strings im Nutzerprofil gespeichert, nicht als Datentyp „Time“. Das bedeutet, dass zeitbasierte Segmentierungsfilter (wie „vor“, „nach“ oder „in den letzten X Tagen“) für diese Attribute nicht funktionieren. Beispielsweise wird `Mar 26 2026 06:12 PM +00:00` als String gespeichert, da es keinem unterstützten Format entspricht. Um dies zu vermeiden, verwenden Sie das ISO-8601-Format (z. B. `2026-03-26T18:12:00Z`). <br><br>Zeitattribute ohne Zeitzone werden standardmäßig auf Mitternacht UTC gesetzt (und im Dashboard als Äquivalent von Mitternacht UTC in der Zeitzone des Unternehmens formatiert). Um eine Zeitzone anzugeben, hängen Sie einen UTC-Offset an den Zeitstempel an (z. B. `2024-11-10T18:00:00-05:00` für EST). Wenn der Zeitzonen-Offset fehlt oder falsch formatiert ist, wird der Wert standardmäßig auf UTC gesetzt. <br><br>Zeiten werden im Dashboard in der Zeitzone Ihres Unternehmens angezeigt. Beispielsweise würde `2024-11-10T18:00:00-05:00` (18:00 Uhr EST) als die entsprechende Zeit in der konfigurierten Zeitzone Ihres Unternehmens angezeigt. <br><br>Ereignisse mit Zeitstempeln in der Zukunft werden standardmäßig auf die aktuelle Zeit gesetzt. <br><br>Bei regulären angepassten Attributen wird der Wert als String im Nutzerprofil gespeichert, wenn das Jahr kleiner als 0 oder größer als 3000 ist. |
| Gleitkommazahlen | Angepasste Gleitkomma-Attribute sind positive oder negative Zahlen mit einem Dezimalpunkt. Sie können Gleitkommazahlen beispielsweise verwenden, um Kontostände oder Nutzerbewertungen für Produkte oder Dienste zu speichern. |
| Ganzzahlen | Sie können ganzzahlige angepasste Attribute inkrementieren, indem Sie ein Objekt mit dem Feld „inc“ und dem hinzuzufügenden Betrag zuweisen. <br><br>Beispiel: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Verschachtelte angepasste Attribute | Verschachtelte angepasste Attribute definieren eine Reihe von Attributen als Eigenschaft eines anderen Attributs. Wenn Sie ein angepasstes Attribut-Objekt definieren, fügen Sie diesem Objekt eine Reihe von Attributen hinzu. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). |
| Strings | Angepasste String-Attribute sind Zeichenfolgen, die zum Speichern von Textdaten verwendet werden. Sie können Strings beispielsweise verwenden, um Vor- und Nachnamen, E-Mail-Adressen oder Präferenzen zu speichern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datentypen für angepasste Attribute" }

{% alert tip %}
Hinweise dazu, wann ein angepasstes Event im Vergleich zu einem angepassten Attribut verwendet werden sollte, finden Sie unter [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) und [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).
{% endalert %}

##### Array-von-Objekten-Beispiel {#array-of-objects-example}

Dieses Array von Objekten ermöglicht es Ihnen, Segmente basierend auf bestimmten Kriterien innerhalb der Aufenthalte zu erstellen und Ihre Nachrichten mithilfe der Daten aus jedem Aufenthalt mit Liquid-Templates zu personalisieren.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

Beispiele für Arrays von Objekten mit `$add`, `$remove` und `$update` finden Sie unter [Array von Objekten – API-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) und [Array von Objekten – SDK-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).

#### Braze-Nutzerprofilfelder {#braze-user-profile-fields}

{% alert important %}
Die folgenden Nutzerprofilfelder sind case-sensitiv. Stellen Sie daher sicher, dass Sie diese Felder in Kleinbuchstaben referenzieren.
{% endalert %}

{% alert tip %}
Eine kundenorientierte Referenz der Standardattribute, die nach Kategorie organisiert ist und Hinweise für SDK, API, CSV und Cloud Data Ingestion enthält, finden Sie unter [Standardattribute]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes).
{% endalert %}

| Nutzerprofilfeld | Datentyp-Spezifikation |
| ---| --- |
| alias_name | (String) |
| alias_label | (String) |
| braze_id | (String, optional) Wenn ein Nutzerprofil vom SDK erkannt wird, wird ein anonymes Nutzerprofil mit einer zugehörigen `braze_id` erstellt. Die `braze_id` wird automatisch von Braze zugewiesen, kann nicht bearbeitet werden und ist gerätespezifisch. |
| country | (String) Wir verlangen, dass Ländercodes im [ISO-3166-1 Alpha-2-Standard](http://en.wikipedia.org/wiki/ISO_3166-1) an Braze übergeben werden. Unsere API versucht nach bestem Wissen, Länder in verschiedenen Formaten zuzuordnen. Beispielsweise kann „Australia“ auf „AU“ abgebildet werden. Wenn die Eingabe jedoch keinem [ISO-3166-1 Alpha-2-Standard](http://en.wikipedia.org/wiki/ISO_3166-1) entspricht, wird der Länderwert auf `NULL` gesetzt. <br><br>Das Setzen von `country` für eine:n Nutzer:in per CSV-Import oder API verhindert, dass Braze diese Information automatisch über das SDK erfasst. |
| current_location | (Objekt) In der Form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (Datum der ersten App-Nutzung) String im ISO-8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (Datum der letzten App-Nutzung) String im ISO-8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (Geburtsdatum) String im Format „YYYY-MM-DD“, z. B. 1980-12-21. |
| email | (String) |
| email_subscribe | (String) Verfügbare Werte sind „opted_in“ (explizit für den Empfang von E-Mail-Nachrichten registriert), „unsubscribed“ (explizit vom Empfang von E-Mail-Nachrichten abgemeldet) und „subscribed“ (weder angemeldet noch abgemeldet).  |
| email_open_tracking_disabled | (Boolean) `true` oder `false` akzeptiert. Setzen Sie den Wert auf `true`, um zu verhindern, dass das Öffnungs-Tracking-Pixel zu allen zukünftigen E-Mails hinzugefügt wird, die an diese:n Nutzer:in gesendet werden.|
| email_click_tracking_disabled | (Boolean) `true` oder `false` akzeptiert. Setzen Sie den Wert auf `true`, um das Klick-Tracking für alle Links in zukünftigen E-Mails zu deaktivieren, die an diese:n Nutzer:in gesendet werden.|
| external_id | (String) Ein eindeutiger Bezeichner für ein Nutzerprofil. Nach der Zuweisung einer `external_id` identifiziert Braze das Nutzerprofil über alle Geräte hinweg. Bei der erstmaligen Zuweisung einer external_id zu einem unbekannten Nutzerprofil migriert Braze alle vorhandenen Nutzerprofildaten in das neue Nutzerprofil. |
| facebook | Hash, der beliebige der folgenden Werte enthält: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| first_name | (String) |
| gender | (String) „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (möchte nicht angeben) oder null (unbekannt). |
| home_city | (String) |
| language | (String) Wir verlangen, dass die Sprache im [ISO-639-1-Standard](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) an Braze übergeben wird. Unterstützte Sprachen finden Sie in unserer [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes).<br><br>Das Setzen von `language` für eine:n Nutzer:in per CSV-Import oder API verhindert, dass Braze diese Information automatisch über das SDK erfasst. |
| last_name | (String) |
| marked_email_as_spam_at | (String) Datum, an dem die E-Mail der/des Nutzers/Nutzerin als Spam markiert wurde. Erscheint im ISO-8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (String) Wir empfehlen, Telefonnummern im [E.164](https://en.wikipedia.org/wiki/E.164)-Format anzugeben. Details finden Sie unter [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format).|
| push_subscribe | (String) Verfügbare Werte sind „opted_in“ (explizit für den Empfang von Push-Nachrichten registriert), „unsubscribed“ (explizit vom Empfang von Push-Nachrichten abgemeldet) und „subscribed“ (weder angemeldet noch abgemeldet).  |
| push_tokens | Array von Objekten mit `app_id` und `token`-String. Sie können optional eine `device_id` für das Gerät angeben, dem dieses Token zugeordnet ist, z. B. `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Wenn keine `device_id` angegeben wird, wird eine zufällig generiert. |
| subscription_groups | Array von Objekten mit `subscription_group_id` und `subscription_state`-String, z. B. `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Verfügbare Werte für `subscription_state` sind „subscribed“ und „unsubscribed“.|
| time_zone | (String) Zeitzonenname aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (z. B. „America/New_York“ oder „Eastern Time (US & Canada)“). Es werden nur gültige Zeitzonenwerte gesetzt. |
| twitter | Hash, der beliebige der folgenden Werte enthält: `id` (Ganzzahl), `screen_name` (String, X (ehemals Twitter)-Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze-Nutzerprofilfelder" }

Sprachwerte, die explizit über diese API gesetzt werden, haben Vorrang vor den Gebietsschema-Informationen, die Braze automatisch vom Gerät erhält.

####  Beispielanfrage für Nutzerattribute {#user-attribute-example-request}

Dieses Beispiel enthält vier Nutzerattribut-Objekte von insgesamt 75 zulässigen Attribut-Objekten pro API-Aufruf.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Alex",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Lee",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Yuri",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## Push-Token migrieren {#migrate-push-tokens}

Wenn Sie vor der Integration von Braze bereits Push-Benachrichtigungen versendet haben – entweder eigenständig oder über einen anderen Anbieter –, können Sie mit der Push-Token-Migration weiterhin Push-Benachrichtigungen an Ihre Nutzer:innen mit registrierten Push-Token senden.

### Automatische Migration über das SDK {#automatic-migration-through-sdk}

Nachdem Sie das [Braze SDK integriert]({{site.baseurl}}/developer_guide/sdk_integration) haben, werden Push-Token für Ihre Nutzer:innen mit Opt-in automatisch migriert, sobald diese Ihre App das nächste Mal öffnen. Bis dahin können Sie diesen Nutzer:innen keine Push-Benachrichtigungen über Braze senden.

Alternativ können Sie [Ihre Push-Token manuell migrieren](#manual-migration-through-api), um Ihre Nutzer:innen schneller wieder zu erreichen.

#### Überlegungen zu Web-Token {#web-token-considerations}

Aufgrund der Besonderheiten von Web-Push-Token sollten Sie bei der Implementierung von Push für das Web Folgendes beachten:

|Überlegung|Details|
|----------------------|------------|
| **Service Worker**  | Standardmäßig sucht das Web SDK nach einem Service Worker unter `./service-worker`, sofern keine andere Option angegeben ist, wie z. B. `manageServiceWorkerExternally` oder `serviceWorkerLocation`. Wenn Ihr Service Worker nicht korrekt eingerichtet ist, kann dies zu abgelaufenen Push-Token für Ihre Nutzer:innen führen. |
| **Abgelaufene Token**   | Wenn Nutzer:innen innerhalb von 60 Tagen keine Web-Sitzung gestartet haben, läuft ihr Push-Token ab. Da Braze abgelaufene Push-Token nicht migrieren kann, müssen Sie einen [Push-Primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) senden, um sie erneut zu erreichen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Überlegungen zu Web-Token" }

### Manuelle Migration über die API {#manual-migration-through-api}

Die manuelle Push-Token-Migration ist der Prozess, bei dem diese zuvor erstellten Schlüssel über die API in Ihre Braze-Plattform importiert werden.

Migrieren Sie iOS- (APNs) und Android-Token (FCM) programmatisch auf Ihre Plattform, indem Sie den [`users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden. Sie können sowohl identifizierte Nutzer:innen (Nutzer:innen mit einer zugeordneten externen ID) als auch anonyme Nutzer:innen (Nutzer:innen ohne externe ID) migrieren.

Geben Sie die `app_id` Ihrer App während der Push-Token-Migration an, um das entsprechende Push-Token der richtigen App zuzuordnen. Jede App (iOS, Android usw.) hat eine eigene `app_id`, die im Abschnitt **Identifikation** auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) zu finden ist. Stellen Sie sicher, dass Sie die `app_id` der richtigen Plattform verwenden.

{% alert important %}
Es ist nicht möglich, Web-Push-Token über die API zu migrieren. Dies liegt daran, dass Web-Push-Token nicht demselben Schema wie andere Plattformen entsprechen.

<br>Wenn Sie versuchen, Web-Push-Token programmatisch zu migrieren, erhalten Sie möglicherweise einen Fehler wie den folgenden: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Als Alternative zur API-Migration empfehlen wir, das SDK zu integrieren und Ihre Token-Basis auf natürliche Weise wieder aufzubauen.
{% endalert %}

{% tabs local %}
{% tab Externe ID vorhanden %}
Setzen Sie für identifizierte Nutzer:innen das Flag `push_token_import` auf `false` (oder lassen Sie den Parameter weg) und geben Sie die Werte `external_id`, `app_id` und `token` im `attributes`-Objekt der Nutzer:innen an.

Zum Beispiel:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab Externe ID fehlt %}
Beim Import von Push-Token aus anderen Systemen ist eine `external_id` nicht immer verfügbar. Setzen Sie in diesem Fall das Flag `push_token_import` auf `true` und geben Sie die Werte `app_id` und `token` an. Braze erstellt für jedes Token ein temporäres, anonymes Nutzerprofil, damit Sie diese Personen weiterhin kontaktieren können. Wenn das Token bereits in Braze vorhanden ist, wird die Anfrage ignoriert.

Zum Beispiel:

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

Nach dem Import verschiebt Braze automatisch das importierte Push-Token in das Braze-Nutzerprofil, sobald die anonymen Nutzer:innen die Braze-fähige Version Ihrer App starten, und bereinigt das temporäre Profil.

Braze prüft einmal im Monat, ob anonyme Profile mit dem Flag `push_token_import` vorhanden sind, die kein Push-Token besitzen. Wenn das anonyme Profil kein Push-Token mehr hat, löscht Braze das Profil. Hat das anonyme Profil jedoch noch ein Push-Token – was darauf hindeutet, dass sich die tatsächlichen Nutzer:innen noch nicht auf dem Gerät mit dem betreffenden Push-Token angemeldet haben –, unternimmt Braze nichts.
{% endtab %}
{% endtabs %}

### iOS-Push-Token importieren {#import-ios-push-tokens}

Beim Migrieren von iOS-Push-Token mit `/users/track` wird das Feld `gateway` am Push-Token nicht gesetzt. Braze geht davon aus, dass über die API importierte Token gültige Vordergrund-Push-Token sind, kann jedoch nicht bestimmen, zu welcher APNs-Umgebung das Token gehört.

Ohne das Gateway-Feld verwendet Braze die konfigurierte Fallback-Umgebungseinstellung Ihrer App beim Senden von Push-Benachrichtigungen. Dies kann zu `BadDeviceToken`-Fehlern führen, wenn die tatsächliche Umgebung des Tokens von der konfigurierten Fallback-Einstellung abweicht. Beispielsweise schlägt ein Entwicklungs-Token fehl, das über das Produktions-Gateway gesendet wird.

Um Zustellungsprobleme zu vermeiden:

- Stellen Sie sicher, dass die Umgebungseinstellung Ihrer App im Braze-Dashboard mit den Token übereinstimmt, die Sie importieren.
- Importieren Sie für Produktions-Apps nur Produktions-Token.
- Überprüfen Sie bei Testumgebungen, dass sowohl Ihre App-Konfiguration als auch die importierten Token die Entwicklungsumgebung verwenden.

{% alert note %}
Token, die über das Braze SDK registriert werden, enthalten das Gateway-Feld automatisch, da das SDK die Umgebung aus den Berechtigungen Ihrer App erkennt.
{% endalert %}

### Android-Push-Token importieren {#import-android-push-tokens}

{% alert important %}
Die folgende Überlegung gilt nur für Android-Apps. iOS-Apps erfordern diese Schritte nicht, da diese Plattform nur ein Framework zur Anzeige von Push hat und Push-Benachrichtigungen sofort dargestellt werden, solange Braze über die erforderlichen Push-Token und Zertifikate verfügt.
{% endalert %}

Wenn Sie Android-Push-Benachrichtigungen an Ihre Nutzer:innen senden müssen, bevor die Braze-SDK-Integration abgeschlossen ist, verwenden Sie Schlüssel-Wert-Paare zur Validierung von Push-Benachrichtigungen.

Sie benötigen einen Receiver, der Push-Payloads verarbeitet und anzeigt. Um den Receiver über das Push-Payload zu informieren, fügen Sie die erforderlichen Schlüssel-Wert-Paare zur Push-Campaign hinzu. Die Werte dieser Paare hängen vom jeweiligen Push-Partner ab, den Sie vor Braze verwendet haben.

{% alert note %}
Bei einigen Push-Benachrichtigungsanbietern muss Braze die Schlüssel-Wert-Paare vereinfachen, damit sie korrekt interpretiert werden können. Um Schlüssel-Wert-Paare für eine bestimmte Android-App zu vereinfachen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie finde ich Nutzer:innen, die als Spam behandelt oder vom Messaging ausgeschlossen wurden? {#how-do-i-find-users-treated-as-spam-or-blocked-from-messaging}

Braze stellt im Dashboard keine dedizierte Spam-Liste bereit. Braze blockiert einzelne Nutzerprofile („Dummy-Nutzer:innen“) mit mehr als fünf Millionen Sessions, mehr als 20.000 unterschiedlichen angepassten Event-Namen oder mehr als 20.000 unterschiedlichen Produktnamen in Käufen und stoppt die Aufnahme aller eingehenden Daten für dieses Profil – sowohl von den SDKs als auch von der REST API. Wenn ein Bezeichner blockiert ist, kann [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) den Fehler `"provided external_id is blacklisted and disallowed"` zurückgeben. Dieser Wortlaut stammt wörtlich aus der API-Antwort. Um Profile zu finden, die wegen übermäßiger Sessions blockiert wurden, erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mit dem Filter **Session Count**, der auf **more than 5,000,000** eingestellt ist, exportieren Sie das Segment als CSV und gleichen Sie die Profilfelder unter **Engagement** > **Search users** oder mit dem Endpunkt [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) ab. Für unterschiedliche angepasste Event-Namen oder Produktnamen gibt es keinen entsprechenden Filter. Wenden Sie sich daher an Ihren Braze Account Manager, um Profile zu identifizieren, die aus diesen Gründen blockiert wurden. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_archival).