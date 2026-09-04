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
- [Nutzer-Aliase]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

{% alert note %}
Verwenden Sie für reguläre Array-basierte angepasste Attribute `add` und `remove` (ohne `$`).

Für Arrays von Objekten (verschachtelte angepasste Attribute) verwenden Sie `$add`, `$remove` und `$update` in `/users/track`-Anfrage-Payloads. Diese Operatoren wenden Änderungen auf Objektebene an, indem sie Bezeichner (`$identifier_key` und `$identifier_value`) abgleichen und In-Place-Aktualisierungen mit `$new_object` unterstützen.

Verwenden Sie dieses Format, wenn Sie Objekte innerhalb eines bestehenden Arrays anhängen, entfernen oder aktualisieren müssen, während der restliche Array-Zustand erhalten bleibt. Vollständige Anfrage-Beispiele finden Sie unter [Array von Objekten – API-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) und [Array von Objekten – SDK-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).
{% endalert %}

Um ein Profilattribut zu entfernen, setzen Sie es auf `null`. Einige Felder, wie `external_id` und `user_alias`, können nicht entfernt werden, nachdem sie einem Nutzerprofil hinzugefügt wurden.

### Bezeichner-Auflösung {#identifier-resolution}

Sofern Sie keinen [anonymen Push-Token-Import](#push-token-import) durchführen, muss jedes Nutzerattribut-Objekt mindestens einen Bezeichner enthalten: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`. Verwenden Sie nach Möglichkeit nur einen Bezeichner pro Objekt, um Mehrdeutigkeiten darüber zu vermeiden, welches Nutzerprofil aktualisiert oder erstellt wird.

Beachten Sie Folgendes bei der Verwendung von Bezeichnern:

- **`external_id` und `user_alias` schließen sich gegenseitig aus.** Wenn beide im selben Nutzerattribut-Objekt enthalten sind, wird ein Fehler zurückgegeben. Um einem Nutzer, der bereits eine `external_id` hat, einen Alias hinzuzufügen, verwenden Sie den [`/users/alias/new`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_alias).
- **`email` hat Vorrang vor `phone`.** Wenn sowohl `email` als auch `phone` im selben Objekt enthalten sind, verwendet Braze `email` als Bezeichner. Das bedeutet, dass die Attribute auf das Nutzerprofil angewendet werden, das mit dieser E-Mail-Adresse verknüpft ist, selbst wenn die Telefonnummer zu einem anderen Profil gehört.

{% alert important %}
Um unerwartetes Verhalten zu vermeiden, verwenden Sie einen einzelnen Bezeichner pro Nutzerattribut-Objekt. Die Angabe mehrerer Bezeichner, die auf verschiedene Nutzerprofile verweisen, kann dazu führen, dass Attribute dem falschen Profil zugewiesen werden.
{% endalert %}

#### Nur bestehende Profile aktualisieren {#update-existing-profiles-only}

Wenn Sie nur bestehende Nutzerprofile in Braze aktualisieren möchten, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Anfragekörper übergeben. Wenn dieser Wert ausgelassen wird, erstellt Braze ein neues Nutzerprofil, falls die `external_id` noch nicht existiert.

{% alert note %}
Wenn Sie ein reines Alias-Nutzerprofil über den `/users/track`-Endpunkt erstellen, müssen Sie `_update_existing_only` auf `false` setzen. Wenn Sie diesen Wert auslassen, erstellt Braze das reine Alias-Profil nicht.
{% endalert %}

#### Push-Token-Import {#push-token-import}

Bevor Sie Push-Token in Braze importieren, prüfen Sie, ob dies erforderlich ist. Wenn die Braze SDKs eingebunden sind, verwalten sie Push-Token automatisch, ohne dass diese über die API hochgeladen werden müssen.

Falls Sie sie dennoch über die API hochladen müssen, können sie entweder für identifizierte oder anonyme Nutzer:innen hochgeladen werden. Das bedeutet, dass entweder eine `external_id` vorhanden sein muss oder bei anonymen Nutzer:innen das Flag `push_token_import` auf `true` gesetzt sein muss.

{% alert note %}
Beim Import von Push-Token aus anderen Systemen ist eine `external_id` nicht immer verfügbar. Um die Kommunikation mit diesen Nutzer:innen während Ihrer Umstellung auf Braze aufrechtzuerhalten, können Sie die Legacy-Token für anonyme Nutzer:innen ohne Angabe einer `external_id` importieren, indem Sie `push_token_import` auf `true` setzen.
{% endalert %}

Wenn `push_token_import` auf `true` gesetzt ist:

* `external_id` und `braze_id` sollten **nicht** angegeben werden
* Das Attribut-Objekt **muss** ein Push-Token enthalten
* Wenn das Token bereits in Braze existiert, wird die Anfrage ignoriert; andernfalls erstellt Braze ein temporäres, anonymes Nutzerprofil für jedes Token, damit Sie diesen Personen weiterhin Nachrichten senden können

Nach dem Import verschiebt Braze automatisch das importierte Push-Token in das Braze-Nutzerprofil, sobald der jeweilige Nutzer die Braze-fähige Version Ihrer App startet, und bereinigt das temporäre Profil.

Braze prüft einmal im Monat, ob ein anonymes Profil mit dem Flag `push_token_import` existiert, das kein Push-Token mehr besitzt. Wenn das anonyme Profil kein Push-Token mehr hat, löscht Braze das Profil. Hat das anonyme Profil jedoch noch ein Push-Token – was darauf hindeutet, dass sich der tatsächliche Nutzer noch nicht auf dem Gerät mit diesem Push-Token angemeldet hat –, unternimmt Braze nichts.

Weitere Informationen finden Sie unter [Push-Token migrieren](#migrate-push-tokens).

#### Datentypen angepasster Attribute {#custom-attribute-data-types}

Die folgenden Datentypen können als angepasstes Attribut gespeichert werden:

| Datentyp | Hinweise |
| --- | --- |
| Arrays | Arrays angepasster Attribute werden unterstützt. Wenn Sie ein Element hinzufügen, wird es am Ende des Arrays angehängt. Existiert das Element bereits, wird es von seiner aktuellen Position an das Ende verschoben.<br><br>Es werden nur eindeutige Werte gespeichert. Beispielsweise ergibt der Import von `['hotdog','hotdog','hotdog','pizza']` das Ergebnis `['hotdog', 'pizza']`.<br><br>Sie können ein Array direkt setzen (zum Beispiel `"my_array_custom_attribute":[ "Value1", "Value2" ]`), einem bestehenden Array mit `"my_array_custom_attribute" : { "add" : ["Value3"] }` Elemente hinzufügen oder Werte mit `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}` entfernen.<br><br>Die Standard- und Höchstzahl an Elementen in einem Array beträgt 500. Sie können die Höchstzahl an Arrays im Braze-Dashboard unter **Data Settings** > **Custom Attributes** aktualisieren. Weitere Informationen finden Sie unter [Arrays]({{site.baseurl}}/developer_guide/analytics#arrays). |
| Array von Objekten | Verwenden Sie ein Array von Objekten, um eine Liste von Objekten zu definieren, wobei jedes Objekt einen Satz von Attributen enthält. Verwenden Sie diesen Typ, um mehrere Sätze zusammenhängender Daten für eine:n Nutzer:in zu speichern, wie Hotelaufenthalte, Kaufhistorie oder Präferenzen.<br><br>Definieren Sie zum Beispiel ein angepasstes Attribut namens `hotel_stays` auf einem Nutzerprofil als Array, wobei jedes Objekt einen separaten Aufenthalt repräsentiert, mit Attributen wie `hotel_name`, `check_in_date` und `nights_stayed`.<br><br>Arrays von Objekten haben keine Beschränkung der Elementanzahl, aber eine maximale Größe von 100&nbsp;KB. Wenn eine Aktualisierung dazu führt, dass das Array diese Grenze überschreitet, verwirft Braze die Aktualisierung, und das Attribut bleibt unverändert.<br><br>Verwenden Sie für `/users/track`- und SDK-Payloads `$add`, `$remove` und `$update` für Array-von-Objekten-Operationen. Verwenden Sie `add` und `remove` (ohne `$`) für reguläre Array-basierte angepasste Attribute, die skalare Werte enthalten. Details finden Sie unter [Array von Objekten – API-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example), [Array von Objekten – SDK-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example) und [Array-von-Objekten-Beispiel](#array-of-objects-example). |
| Booleans | `true` oder `false` |
| Datumsangaben | Speichern Sie Datumsangaben im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format (empfohlen) oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Beachten Sie, dass „T“ ein Zeittrennzeichen ist, kein Platzhalter, und nicht geändert oder entfernt werden sollte. <br><br>Datumswerte, die keinem der aufgeführten Formate entsprechen, werden als Strings im Nutzerprofil gespeichert und nicht als Time-Datentyp. Das bedeutet, dass zeitbasierte Segmentierungsfilter (wie „vor“, „nach“ oder „in den letzten X Tagen“) für diese Attribute nicht funktionieren. Beispielsweise wird `Mar 26 2026 06:12 PM +00:00` als String gespeichert, da es keinem unterstützten Format entspricht. Um dies zu vermeiden, verwenden Sie das ISO-8601-Format (wie `2026-03-26T18:12:00Z`). <br><br>Zeitattribute ohne Zeitzone werden standardmäßig auf Mitternacht UTC gesetzt (und auf dem Dashboard als das Äquivalent von Mitternacht UTC in der Zeitzone des Unternehmens angezeigt). Um eine Zeitzone anzugeben, hängen Sie einen UTC-Offset an den Zeitstempel an (zum Beispiel `2024-11-10T18:00:00-05:00` für EST). Wenn der Zeitzonen-Offset fehlt oder falsch formatiert ist, wird der Wert standardmäßig auf UTC gesetzt. <br><br>Zeiten werden auf dem Dashboard in der Zeitzone Ihres Unternehmens angezeigt. Beispielsweise würde `2024-11-10T18:00:00-05:00` (18:00 Uhr EST) als die entsprechende Zeit in der konfigurierten Zeitzone Ihres Unternehmens erscheinen. <br><br>Ereignisse mit Zeitstempeln in der Zukunft werden standardmäßig auf die aktuelle Zeit gesetzt. <br><br>Bei regulären angepassten Attributen wird der Wert als String im Nutzerprofil gespeichert, wenn das Jahr kleiner als 0 oder größer als 3000 ist. |
| Gleitkommazahlen | Angepasste Attribute vom Typ Gleitkommazahl sind positive oder negative Zahlen mit einem Dezimalpunkt. Sie können Gleitkommazahlen zum Beispiel verwenden, um Kontostände oder Nutzerbewertungen für Produkte oder Dienste zu speichern. |
| Ganzzahlen | Sie können ganzzahlige angepasste Attribute inkrementieren, indem Sie ein Objekt mit dem Feld „inc“ und dem zu addierenden Betrag zuweisen. <br><br>Beispiel: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Verschachtelte angepasste Attribute | Verschachtelte angepasste Attribute definieren einen Satz von Attributen als Eigenschaft eines anderen Attributs. Wenn Sie ein angepasstes Attribut-Objekt definieren, fügen Sie diesem Objekt einen Satz von Attributen hinzu. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). |
| Strings | Angepasste Attribute vom Typ String sind Zeichenfolgen, die zur Speicherung von Textdaten verwendet werden. Sie können Strings zum Beispiel verwenden, um Vor- und Nachnamen, E-Mail-Adressen oder Präferenzen zu speichern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datentypen angepasster Attribute" }

{% alert tip %}
Hinweise dazu, wann Sie ein angepasstes Event statt eines angepassten Attributs verwenden sollten, finden Sie unter [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) und [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).
{% endalert %}

##### Array-von-Objekten-Beispiel {#array-of-objects-example}

Dieses Array von Objekten ermöglicht es Ihnen, Segmente basierend auf bestimmten Kriterien innerhalb der Aufenthalte zu erstellen und Ihre Nachrichten mithilfe der Daten jedes Aufenthalts mit Liquid-Templates zu personalisieren.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

Beispiele für Arrays von Objekten, die `$add`, `$remove` und `$update` verwenden, finden Sie unter [Array von Objekten – API-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) und [Array von Objekten – SDK-Beispiel]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).

#### Braze-Nutzerprofilfelder {#braze-user-profile-fields}

{% alert important %}
Die folgenden Nutzerprofilfelder unterscheiden zwischen Groß- und Kleinschreibung. Stellen Sie daher sicher, dass Sie diese Felder in Kleinbuchstaben referenzieren.
{% endalert %}

{% alert tip %}
Eine kundenorientierte Referenz der Standardattribute, die nach Kategorie organisiert ist und Hinweise für SDK, API, CSV und Cloud Data Ingestion enthält, finden Sie unter [Standardattribute]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes).
{% endalert %}

| Nutzerprofilfeld | Datentyp-Spezifikation |
| ---| --- |
| alias_name | (String) |
| alias_label | (String) |
| braze_id | (String, optional) Wenn ein Nutzerprofil vom SDK erkannt wird, wird ein anonymes Nutzerprofil mit einer zugehörigen `braze_id` erstellt. Die `braze_id` wird automatisch von Braze zugewiesen, kann nicht bearbeitet werden und ist gerätespezifisch. |
| country | (String) Wir erfordern, dass Ländercodes im [ISO-3166-1 Alpha-2-Standard](http://en.wikipedia.org/wiki/ISO_3166-1) an Braze übergeben werden. Unsere API versucht nach besten Kräften, Länder zuzuordnen, die in verschiedenen Formaten empfangen werden. Zum Beispiel kann „Australia“ auf „AU“ abgebildet werden. Wenn die Eingabe jedoch keinem gegebenen [ISO-3166-1 Alpha-2-Standard](http://en.wikipedia.org/wiki/ISO_3166-1) entspricht, wird der Länderwert auf `NULL` gesetzt. <br><br>Das Setzen von `country` bei einer:m Nutzer:in per CSV-Import oder API verhindert, dass Braze diese Information automatisch über das SDK erfasst. |
| current_location | (Objekt) In der Form {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (Datum, an dem der Nutzer die App zum ersten Mal verwendet hat) String im ISO-8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (Datum, an dem der Nutzer die App zum letzten Mal verwendet hat) String im ISO-8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (Geburtsdatum) String im Format „YYYY-MM-DD“, zum Beispiel 1980-12-21. |
| email | (String) |
| email_subscribe | (String) Verfügbare Werte sind „opted_in“ (explizit für den Empfang von E-Mail-Nachrichten registriert), „unsubscribed“ (explizit vom Empfang von E-Mail-Nachrichten abgemeldet) und „subscribed“ (weder angemeldet noch abgemeldet). |
| email_open_tracking_disabled | (Boolean) `true` oder `false` werden akzeptiert. Setzen Sie den Wert auf `true`, um zu verhindern, dass das Öffnungs-Tracking-Pixel allen zukünftigen E-Mails an diese:n Nutzer:in hinzugefügt wird. |
| email_click_tracking_disabled | (Boolean) `true` oder `false` werden akzeptiert. Setzen Sie den Wert auf `true`, um das Klick-Tracking für alle Links in zukünftigen E-Mails an diese:n Nutzer:in zu deaktivieren. |
| external_id | (String) Ein eindeutiger Bezeichner für ein Nutzerprofil. Nach der Zuweisung einer `external_id` identifiziert Braze das Nutzerprofil über die Geräte einer:s Nutzers:in hinweg. Beim erstmaligen Zuweisen einer external_id zu einem unbekannten Nutzerprofil migriert Braze alle bestehenden Nutzerprofildaten in das neue Nutzerprofil. |
| facebook | Hash, der eines der folgenden Felder enthalten kann: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| first_name | (String) |
| gender | (String) „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (keine Angabe) oder null (unbekannt). |
| home_city | (String) |
| language | (String) Wir erfordern, dass die Sprache im [ISO-639-1-Standard](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) an Braze übergeben wird. Eine Liste der unterstützten Sprachen finden Sie in unserer [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes).<br><br>Das Setzen von `language` bei einer:m Nutzer:in per CSV-Import oder API verhindert, dass Braze diese Information automatisch über das SDK erfasst. |
| last_name | (String) |
| marked_email_as_spam_at | (String) Datum, an dem die E-Mail der:des Nutzers:in als Spam markiert wurde. Erscheint im ISO-8601-Format oder in einem der folgenden Formate: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (String) Wir empfehlen, Telefonnummern im [E.164](https://en.wikipedia.org/wiki/E.164)-Format anzugeben. Details finden Sie unter [Telefonnummern von Nutzer:innen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format). |
| push_subscribe | (String) Verfügbare Werte sind „opted_in“ (explizit für den Empfang von Push-Nachrichten registriert), „unsubscribed“ (explizit vom Empfang von Push-Nachrichten abgemeldet) und „subscribed“ (weder angemeldet noch abgemeldet). |
| push_tokens | Array von Objekten mit `app_id` und `token`-String. Sie können optional eine `device_id` für das Gerät angeben, dem dieses Token zugeordnet ist, zum Beispiel `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Wenn keine `device_id` angegeben wird, wird eine zufällig generiert. |
| subscription_groups | Array von Objekten mit `subscription_group_id` und `subscription_state`-String, zum Beispiel `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Verfügbare Werte für `subscription_state` sind „subscribed“ und „unsubscribed“. |
| time_zone | (String) Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (zum Beispiel „America/New_York“ oder „Eastern Time (US & Canada)“). Es werden nur gültige Zeitzonenwerte gesetzt. |
| twitter | Hash, der eines der folgenden Felder enthalten kann: `id` (Ganzzahl), `screen_name` (String, X-Handle (ehemals Twitter)), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count` (Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze-Nutzerprofilfelder" }

Sprachwerte, die explizit über diese API gesetzt werden, haben Vorrang vor den Gebietsschema-Informationen, die Braze automatisch vom Gerät erhält.

#### Beispielanfrage für Nutzerattribute {#user-attribute-example-request}

Dieses Beispiel enthält vier Nutzerattribut-Objekte, von insgesamt 75 zulässigen Attribut-Objekten pro API-Aufruf.

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

Wenn Sie bereits vor der Integration von Braze Push-Benachrichtigungen versendet haben – entweder eigenständig oder über einen anderen Anbieter – ermöglicht Ihnen die Push-Token-Migration, weiterhin Push-Benachrichtigungen an Ihre Nutzer:innen mit registrierten Push-Token zu senden.

### Automatische Migration über das SDK {#automatic-migration-through-sdk}

Nachdem Sie das [Braze SDK integriert]({{site.baseurl}}/developer_guide/sdk_integration) haben, werden die Push-Token Ihrer angemeldeten Nutzer:innen automatisch beim nächsten Öffnen Ihrer App migriert. Bis dahin können Sie diesen Nutzer:innen keine Push-Benachrichtigungen über Braze senden.

Alternativ können Sie [Ihre Push-Token manuell migrieren](#manual-migration-through-api), um Ihre Nutzer:innen schneller wieder anzusprechen.

#### Hinweise zu Web-Token {#web-token-considerations}

Aufgrund der Beschaffenheit von Web-Push-Token sollten Sie bei der Implementierung von Push für das Web Folgendes beachten:

|Hinweis|Details|
|----------------------|------------|
| **Service Worker**  | Standardmäßig sucht das Web SDK nach einem Service Worker unter `./service-worker`, sofern keine andere Option angegeben wird, wie z. B. `manageServiceWorkerExternally` oder `serviceWorkerLocation`. Wenn Ihr Service Worker nicht richtig eingerichtet ist, kann dies zu abgelaufenen Push-Token für Ihre Nutzer:innen führen. |
| **Abgelaufene Token**   | Wenn Nutzer:innen innerhalb von 60 Tagen keine Web-Sitzung gestartet haben, läuft ihr Push-Token ab. Da Braze abgelaufene Push-Token nicht migrieren kann, müssen Sie einen [Push-Primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) senden, um sie erneut anzusprechen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hinweise zu Web-Token" }

### Manuelle Migration über die API {#manual-migration-through-api}

Die manuelle Push-Token-Migration ist der Prozess, bei dem diese zuvor erstellten Schlüssel über die API in Ihre Braze-Plattform importiert werden.

Migrieren Sie iOS- (APNs) und Android-Token (FCM) programmatisch auf Ihre Plattform, indem Sie den [`users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden. Sie können sowohl identifizierte Nutzer:innen (Nutzer:innen mit einer zugehörigen externen ID) als auch anonyme Nutzer:innen (Nutzer:innen ohne externe ID) migrieren.

Geben Sie die `app_id` Ihrer App während der Push-Token-Migration an, um das entsprechende Push-Token der entsprechenden App zuzuordnen. Jede App (iOS, Android usw.) hat eine eigene `app_id`, die im Bereich **Identification** auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) zu finden ist. Achten Sie darauf, die korrekte `app_id` der jeweiligen Plattform zu verwenden.

{% alert important %}
Es ist nicht möglich, Web-Push-Token über die API zu migrieren. Der Grund dafür ist, dass Web-Push-Token nicht dem gleichen Schema wie andere Plattformen entsprechen.

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

{% tab Externe ID nicht vorhanden %}
Beim Import von Push-Token aus anderen Systemen ist eine `external_id` nicht immer verfügbar. Setzen Sie in diesem Fall das Flag `push_token_import` auf `true` und geben Sie die Werte `app_id` und `token` an. Braze erstellt für jedes Token ein temporäres, anonymes Nutzerprofil, damit Sie diese Personen weiterhin kontaktieren können. Wenn das Token bereits in Braze existiert, wird die Anfrage ignoriert.

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

Wenn anonyme Nutzer:innen nach dem Import die Braze-fähige Version Ihrer App starten, verschiebt Braze ihr importiertes Push-Token automatisch in ihr Braze-Nutzerprofil und bereinigt das temporäre Profil.

Braze überprüft einmal im Monat, ob ein anonymes Profil mit dem Flag `push_token_import` existiert, das kein Push-Token besitzt. Wenn das anonyme Profil kein Push-Token mehr hat, löscht Braze das Profil. Hat das anonyme Profil jedoch noch ein Push-Token – was darauf hindeutet, dass sich die tatsächlichen Nutzer:innen noch nicht auf dem Gerät mit diesem Push-Token angemeldet haben –, unternimmt Braze nichts.
{% endtab %}
{% endtabs %}

### iOS-Push-Token importieren {#import-ios-push-tokens}

Beim Migrieren von iOS-Push-Token mit `/users/track` wird das Feld `gateway` nicht am Push-Token gesetzt. Braze geht davon aus, dass über die API importierte Token gültige Vordergrund-Push-Token sind, kann jedoch nicht bestimmen, zu welcher APNs-Umgebung das Token gehört.

Ohne das Gateway-Feld verwendet Braze beim Versenden von Push-Benachrichtigungen die konfigurierte Fallback-Umgebungseinstellung Ihrer App. Dies kann zu `BadDeviceToken`-Fehlern führen, wenn die tatsächliche Umgebung des Tokens von der konfigurierten Fallback-Umgebung abweicht. Beispielsweise wird ein Entwicklungs-Token, das über das Produktions-Gateway gesendet wird, fehlschlagen.

Um Zustellungsprobleme zu vermeiden:

- Stellen Sie sicher, dass die Umgebungseinstellung Ihrer App im Braze-Dashboard mit den Token übereinstimmt, die Sie importieren.
- Importieren Sie für Produktions-Apps nur Produktions-Token.
- Überprüfen Sie für Testumgebungen, dass sowohl Ihre App-Konfiguration als auch die importierten Token die Entwicklungsumgebung verwenden.

{% alert note %}
Token, die über das Braze SDK registriert werden, enthalten das Gateway-Feld automatisch, da das SDK die Umgebung aus den Berechtigungen Ihrer App erkennt.
{% endalert %}

### Android-Push-Token importieren {#import-android-push-tokens}

{% alert important %}
Der folgende Hinweis gilt nur für Android-Apps. iOS-Apps benötigen diese Schritte nicht, da diese Plattform nur ein Framework zur Anzeige von Push hat und Push-Benachrichtigungen sofort dargestellt werden, solange Braze über die erforderlichen Push-Token und Zertifikate verfügt.
{% endalert %}

Wenn Sie Android-Push-Benachrichtigungen an Ihre Nutzer:innen senden müssen, bevor die Integration des Braze SDK abgeschlossen ist, verwenden Sie Schlüssel-Wert-Paare zur Validierung von Push-Benachrichtigungen.

Sie benötigen einen Empfänger, der Push-Payloads verarbeitet und anzeigt. Um den Empfänger über den Push-Payload zu informieren, fügen Sie die erforderlichen Schlüssel-Wert-Paare zur Push-Campaign hinzu. Die Werte dieser Paare hängen vom jeweiligen Push-Partner ab, den Sie vor Braze verwendet haben.

{% alert note %}
Bei einigen Push-Benachrichtigungsanbietern muss Braze die Schlüssel-Wert-Paare vereinfachen, damit sie korrekt interpretiert werden können. Um Schlüssel-Wert-Paare für eine bestimmte Android-App zu vereinfachen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie finde ich Nutzer:innen, die als Spam behandelt oder von Nachrichten ausgeschlossen werden? {#how-do-i-find-users-treated-as-spam-or-blocked-from-messaging}

Braze stellt im Dashboard keine eigene Spamliste bereit. Braze blockiert einzelne Nutzerprofile („Dummy-Nutzer:innen“) mit mehr als fünf Millionen Sitzungen, mehr als 20.000 unterschiedlichen angepassten Event-Namen oder mehr als 20.000 unterschiedlichen Produktnamen in Käufen und stoppt die Aufnahme aller eingehenden Daten für dieses Profil – sowohl über die SDKs als auch über die REST API. Wenn ein Bezeichner blockiert ist, gibt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) möglicherweise den Fehler `"provided external_id is blacklisted and disallowed"` zurück. Dieser Wortlaut stammt wortwörtlich aus der API-Antwort. Um Profile zu finden, die wegen übermäßiger Sitzungen blockiert wurden, erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mit dem Filter **Session Count**, der auf **more than 5,000,000** eingestellt ist, exportieren Sie das Segment als CSV und gleichen Sie die Profilfelder unter **Engagement** > **Search users** oder mit dem Endpunkt [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) ab. Es gibt keinen entsprechenden Filter für unterschiedliche angepasste Event-Namen oder Produktnamen. Wenden Sie sich daher an Ihren Braze Account Manager, um Profile zu identifizieren, die aus diesen Gründen blockiert wurden. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_archival).