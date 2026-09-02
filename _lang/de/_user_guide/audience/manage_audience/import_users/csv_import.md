---
nav_title: CSV-Import
article_title: CSV-Import
description: "Erfahren Sie, wie Sie Nutzerattribute und angepasste Events mithilfe des CSV-Imports erfassen und Update or aktualisieren or aktualisieren können."
page_order: 1.2
---

# CSV-Import {#csv-import}

> Erfahren Sie, wie Sie Nutzerattribute und angepasste Events mithilfe des CSV-Imports erfassen und Update or aktualisieren or aktualisieren können.

## Über den CSV-Import {#about-csv-import}

Sie können den CSV-Import verwenden, um die folgenden Nutzerattribute und angepassten Events zu erfassen und zu Update or aktualisieren or aktualisieren. Braze akzeptiert diese Daten als Standard-CSV-Dateien innerhalb der maximalen Größen in der folgenden Tabelle.

|Typ|Definition|Beispiel|Maximale Dateigröße|
|---|---|---|---|
|Standardattribute|Reservierte Nutzerattribute, die von Braze erkannt werden.| `first_name`, `email`|500 MB|
|Angepasste Attribute|Nutzerattribute, die speziell für Ihr Unternehmen sind.| `last_destination_searched`|500 MB|
|Angepasste Events|Events, die speziell für Ihr Unternehmen sind und Nutzeraktionen darstellen.| `trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Über den CSV-Import" }

## CSV-Import verwenden {#using-csv-import}

### Schritt 1: CSV-Vorlage herunterladen {#step-1-download-a-csv-template}

Um den CSV-Import zu öffnen, gehen Sie zu **Audiences** > **Import Users**. Hier finden Sie eine Tabelle mit Details zu den letzten Importen, wie z. B. das Upload-Datum, den Namen der hochladenden Person, den Dateinamen, die Targeting-Verfügbarkeit, die Anzahl der importierten Zeilen und den Status des Imports.

Wählen Sie zunächst **Attributes** oder **Events** und laden Sie dann die entsprechende Vorlage herunter, die Ihnen beim Erstellen Ihrer CSV-Datei für den Upload hilft.

![Die Seite „Import Users“ im Braze-Dashboard.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Schritt 2: Einen Bezeichner auswählen {#choose-an-identifier}

Die CSV-Datei, die Sie importieren, benötigt einen dedizierten Bezeichner. Wählen Sie einen der folgenden Bezeichnertypen für Ihren Import:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
Beim Import Ihrer Kundendaten können Sie eine `external_id` als eindeutigen Bezeichner für jede:n Kund:in verwenden. Wenn Sie eine `external_id` in Ihrem Import angeben, aktualisiert Braze alle bestehenden Nutzer:innen mit derselben `external_id` oder erstellt eine:n neu identifizierte:n Nutzer:in mit dieser `external_id`, falls keine Übereinstimmung gefunden wird.

- Download: [CSV-Attribut-Importvorlage: Externe ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Download: [CSV-Event-Importvorlage: Externe ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Wenn Sie eine Mischung aus Nutzer:innen mit einer `external_id` und Nutzer:innen ohne `external_id` hochladen, müssen Sie für jeden Import eine separate CSV-Datei erstellen. Eine CSV-Datei kann nicht gleichzeitig `external_id` und Nutzer-Aliase enthalten.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
Um Nutzer:innen ohne `external_id` anzusprechen, können Sie eine Liste von Nutzer:innen mit Nutzer-Aliasen importieren. Ein Alias dient als alternativer eindeutiger Nutzerbezeichner und kann hilfreich sein, wenn Sie anonyme Nutzer:innen ansprechen möchten, die sich noch nicht registriert oder ein Konto in Ihrer App erstellt haben.

Wenn Sie Nutzerprofile hochladen oder Update or aktualisieren or aktualisieren, die nur einen Alias haben, müssen die folgenden zwei Spalten in Ihrer CSV-Datei enthalten sein:

- `user_alias_name`: Ein eindeutiger Nutzerbezeichner; eine Alternative zur `external_id`
- `user_alias_label`: Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@example.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@example.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Schritt 2: Einen Bezeichner auswählen" }

Wenn Sie in Ihrem Import sowohl einen `user_alias_name` als auch ein `user_alias_label` angeben, aktualisiert Braze alle bestehenden Nutzer:innen mit demselben `user_alias_name` und `user_alias_label`. Wird kein:e Nutzer:in gefunden, erstellt Braze eine:n neu identifizierte:n Nutzer:in mit diesem `user_alias_name`.

{% alert important %}
Sie können einen CSV-Import nicht verwenden, um eine:n bestehende:n Nutzer:in mit einem `user_alias_name` zu Update or aktualisieren or aktualisieren, wenn diese:r bereits eine `external_id` hat. Stattdessen wird ein neues Kundenprofil or Nutzerprofil mit dem zugehörigen `user_alias_name` erstellt. Um eine:n Nutzer:in nur mit Alias einer `external_id` zuzuordnen, verwenden Sie den [Endpunkt „Nutzer:innen identifizieren“]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).
{% endalert %}

Download: [CSV-Attribut-Importvorlage: Nutzer-Alias]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab braze id %}
Um bestehende Nutzerprofile in Braze mithilfe eines internen Braze-ID-Werts anstelle einer `external_id` oder eines `user_alias_name`- und `user_alias_label`-Werts zu Update or aktualisieren or aktualisieren, geben Sie `braze_id` als Spaltenüberschrift an.

Dies kann hilfreich sein, wenn Sie Nutzerdaten aus Braze über unsere CSV-Export-Option innerhalb der Segmentierung exportiert haben und diesen bestehenden Nutzer:innen ein neues angepasstes Attribut hinzufügen möchten.

{% alert important %}
Sie können einen CSV-Import nicht verwenden, um eine:n neue:n Nutzer:in mit `braze_id` zu erstellen. Diese Methode kann nur verwendet werden, um bereits bestehende Nutzer:innen innerhalb der Braze-Plattform zu Update or aktualisieren or aktualisieren.
{% endalert %}

{% alert tip %}
Der `braze_id`-Wert kann in CSV-Exporten aus dem Braze-Dashboard als `Appboy ID` bezeichnet werden. Diese ID ist identisch mit der `braze_id` einer Person, sodass Sie diese Spalte beim erneuten Import der CSV-Datei in `braze_id` umbenennen können.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab E-Mail-Adressen und Telefonnummern %}
Sie können auf eine externe ID oder einen Nutzer-Alias verzichten und stattdessen eine E-Mail-Adresse oder Telefonnummer verwenden, um Nutzer:innen zu importieren. Bevor Sie eine CSV-Datei mit E-Mail-Adressen oder Telefonnummern importieren, prüfen Sie Folgendes:

- Stellen Sie sicher, dass in Ihrer CSV-Datei keine externen IDs oder Nutzer-Aliase für diese Profile vorhanden sind. Falls doch, priorisiert Braze die externe ID oder den Nutzer-Alias vor der E-Mail-Adresse zur Identifizierung von Profilen.
- Bestätigen Sie, dass Ihre CSV-Datei korrekt formatiert ist.

{% alert note %}
Wenn Sie sowohl E-Mail-Adressen als auch Telefonnummern in Ihrer CSV-Datei angeben, wird die E-Mail-Adresse bei der Suche nach Profilen gegenüber der Telefonnummer priorisiert.
{% endalert %}

Wenn ein bestehendes Profil diese E-Mail-Adresse oder Telefonnummer hat, wird dieses Profil aktualisiert, und Braze erstellt kein neues Profil. Wenn es mehrere Profile mit derselben E-Mail-Adresse gibt, verwendet Braze dieselbe Logik wie der [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), wobei das zuletzt aktualisierte Profil aktualisiert wird.

Wenn kein Profil mit dieser E-Mail-Adresse oder Telefonnummer existiert, erstellt Braze ein neues Profil mit diesem Bezeichner. Sie können den [`/users/identify`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) verwenden, um dieses Profil später zu identifizieren. Um ein Kundenprofil or Nutzerprofil zu löschen, können Sie auch den [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)-Endpunkt verwenden.
{% endtab %}
{% endtabs %}

### Schritt 3: Ihre CSV-Datei erstellen {#step-3-build-your-csv-file}

Sie können einen der folgenden Datentypen als einzelne CSV-Datei hochladen. Um mehr als einen Datentyp hochzuladen, laden Sie mehrere CSV-Dateien hoch.

- **Nutzerattribute:** Dies umfasst sowohl Standard- als auch angepasste Nutzerattribute. Standardnutzerattribute sind reservierte Schlüssel in Braze (wie `first_name` oder `email`), und angepasste Attribute sind für Ihr Unternehmen spezifische Nutzerattribute (wie `last_destination_searched`).
- **Angepasste Events:** Diese sind für Ihr Unternehmen spezifisch und spiegeln Aktionen wider, die Nutzer:innen durchgeführt haben, wie z. B. `trip_booked` für eine Reisebuchungs-App.

Wenn Sie bereit sind, mit dem Erstellen Ihrer CSV-Datei zu beginnen, beachten Sie die folgenden Informationen:

{% tabs local %}
<!-- TAB -->
{% tab Nutzerattribute %}
#### Erforderliche Bezeichner {#required-identifiers-attributes}

Die `external_id` ist zwar nicht erforderlich, aber Ihre CSV-Datei muss einen Nutzerbezeichner enthalten, der **einem** der folgenden Bezeichner zugeordnet werden kann. Weitere Details zu jedem einzelnen finden Sie unter [Einen Bezeichner auswählen](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **und** `user_alias_label`
- `email`
- `phone`

#### Angepasste Attribute {#custom-attributes}

Die folgenden Datentypen können als angepasste Attribute für den CSV-Import verwendet werden. Spaltenüberschriften, die nicht exakt einem [Standardattribut](#default-attributes) entsprechen, werden als angepasste Attribute in Braze importiert, sofern sie nicht während des Zuordnungsschritts geändert werden.

| Datentyp | Beschreibung |
|---|---|
| Datetime | Muss im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format gespeichert werden. |
| Boolean | Akzeptiert `true` oder `false`. |
| Zahl | Muss eine Ganzzahl oder Gleitkommazahl ohne Leerzeichen oder Kommata sein. Gleitkommazahlen müssen einen Punkt (`.`) als Dezimaltrennzeichen verwenden. |
| String | Kann Kommata enthalten, wenn der Wert in doppelte Anführungszeichen (`""`) eingeschlossen ist. |
| Leer | Leere Werte überschreiben keine vorhandenen Werte im Kundenprofil or Nutzerprofil, und Sie müssen nicht alle vorhandenen Nutzerattribute in Ihrer CSV-Datei angeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Attribute" }

{% alert important %}
Arrays, Push-Token / Textbaustein und angepasste Event-Datentypen werden beim Nutzerimport nicht unterstützt, da Kommata in Ihrer CSV-Datei als Spaltentrennzeichen interpretiert werden und Fehler beim Parsen der Datei verursachen.<br><br>Verwenden Sie stattdessen den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), um diese Arten von Werten hochzuladen.
{% endalert %}

#### Standardattribute {#default-attributes}

{% alert important %}
Beim Import von Standardattributen müssen die verwendeten Spaltenüberschriften exakt der Schreibweise und Groß-/Kleinschreibung der Standardnutzerattribute entsprechen. Andernfalls erkennt Braze diese stattdessen als [angepasste Attribute](#custom-attributes).
{% endalert %}

{% alert tip %}
Eine vollständige Liste der von Braze erkannten Standardattribute (über SDK or Software-Development-Kit, API, CSV und Cloud-Datenaufnahme) finden Sie unter [Standardattribute]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes). Die folgende Tabelle enthält nur die Teilmenge, die über den CSV-Import festgelegt werden kann.
{% endalert %}

Die folgenden Standardattribute sind für den Nutzerimport verfügbar.

| Nutzerprofilfeld | Datentyp | Beschreibung | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Nutzerbezeichner für Ihre Kund:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_name` | String | Ein eindeutiger Nutzerbezeichner für anonyme Nutzer:innen, als Alternative zur `external_id`. Muss zusammen mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_label` | String | Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren. Muss zusammen mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `first_name` | String | Der Vorname Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `Jane`). | Nein |
| `last_name` | String | Der Nachname Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `Doe`). | Nein |
| `email` | String | Die E-Mail-Adresse Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `jane.doe@example.com`). | Nein |
| `country` | String | Ländercodes müssen im ISO-3166-1-Alpha-2-Standard an Braze übergeben werden (z. B. `GB`). | Nein |
| `dob` | String | Muss im Format „JJJJ-MM-TT“ übergeben werden (z. B. `1980-12-21`). Importiert das Geburtsdatum Ihrer Nutzer:innen und ermöglicht es Ihnen, Nutzer:innen anzusprechen, deren Geburtstag „heute“ ist. | Nein |
| `gender` | String | „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (keine Angabe erwünscht) oder nil (unbekannt). | Nein |
| `home_city` | String | Der Wohnort Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `London`). | Nein |
| `language` | String | Die Sprache muss im ISO-639-1-Standard an Braze übergeben werden (z. B. `en`). Siehe unsere [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes). | Nein |
| `phone` | String | Eine von Ihren Nutzer:innen angegebene Telefonnummer im `E.164`-Format (z. B. `+442071838750`). Weitere Informationen zur Formatierung finden Sie unter [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers). | Nein |
| `email_open_tracking_disabled` | Boolean | Akzeptiert true oder false. Setzen Sie den Wert auf true, um zu verhindern, dass das Open-Tracking-Pixel zu allen zukünftigen E-Mails an diese:n Nutzer:in hinzugefügt wird. | Nein |
| `email_click_tracking_disabled` | Boolean | Akzeptiert true oder false. Setzen Sie den Wert auf true, um das Klick-Tracking für alle Links in zukünftigen E-Mails an diese:n Nutzer:in zu deaktivieren. | Nein |
| `email_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von E-Mail-Nachrichten registriert), `unsubscribed` (explizit vom Empfang von E-Mail-Nachrichten abgemeldet) und `subscribed` (weder angemeldet noch abgemeldet). | Nein |
| `push_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von Push-Nachrichten registriert), `unsubscribed` (explizit vom Empfang von Push-Nachrichten abgemeldet) und `subscribed` (weder angemeldet noch abgemeldet). | Nein |
| `time_zone` | String | Die Zeitzone muss im selben Format wie die IANA-Zeitzonendatenbank an Braze übergeben werden (z. B. `America/New_York` oder `Eastern Time (US & Canada)`). | Nein |
| `date_of_first_session`  `date_of_last_session` | String | Kann in einem der folgenden ISO-8601-Formate übergeben werden: „JJJJ-MM-TT“ „JJJJ-MM-TTTHH:MM:SS+00:00“ „JJJJ-MM-TTTHH:MM:SSZ“ „JJJJ-MM-TTTHH:MM:SS“ (z. B. 2019-11-20T18:38:57) | Nein |
| `subscription_group_id` | String | Die `id` Ihrer Abo-Gruppe. Dieser Bezeichner ist auf der Abo-Gruppenseite Ihres Dashboards zu finden. | Nein |
| `subscription_state` | String | Der Abo-Status für die durch `subscription_group_id` angegebene Abo-Gruppe. Zulässige Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe). | Nein, aber dringend empfohlen, wenn `subscription_group_id` verwendet wird |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Standardattribute" }

#### Abo-Gruppenstatus Update or aktualisieren or aktualisieren (optional) {#updating-subscription-group-status-optional}

Darüber hinaus können Sie Nutzer:innen über den Nutzerimport zu E-Mail- oder Kurzmitteilungsdienst or SMS-Abo-Gruppen hinzufügen. Dies ist besonders nützlich für Kurzmitteilungsdienst or SMS, da Nutzer:innen in einer Kurzmitteilungsdienst or SMS-Abo-Gruppe registriert sein müssen, um über den Kurzmitteilungsdienst or SMS-Kanal angeschrieben werden zu können. Weitere Informationen finden Sie unter [Kurzmitteilungsdienst or SMS-Abo-Gruppen]({{site.baseurl}}/sms_rcs_subscription_groups#subscription-group-mms-enablement).

Wenn Sie Abo-Gruppenstatus Update or aktualisieren or aktualisieren, müssen die folgenden zwei Spalten in Ihrer CSV-Datei enthalten sein:

- `subscription_group_id`: Die `id` der [Abo-Gruppe]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).
- `subscription_state`: Verfügbare Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abo-Gruppenstatus Update or aktualisieren or aktualisieren (optional)" }

{% alert note %}
Pro Zeile im Nutzerimport kann nur eine einzelne `subscription_group_id` gesetzt werden. Verschiedene Zeilen können unterschiedliche `subscription_group_id`-Werte haben. Wenn Sie jedoch dieselben Nutzer:innen in mehrere Abo-Gruppen aufnehmen möchten, müssen Sie mehrere Importe durchführen.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Angepasste Events %}
#### Erforderliche Bezeichner {#required-identifiers-custom-events}

Die `external_id` ist zwar nicht erforderlich, aber Ihre CSV-Datei muss einen Nutzerbezeichner enthalten, der **einem** der folgenden Bezeichner zugeordnet werden kann. Weitere Details zu jedem einzelnen finden Sie unter [Einen Bezeichner auswählen](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **und** `user_alias_label`
- `email`
- `phone`

#### Felder für angepasste Events {#custom-event-fields}

Zusätzlich zu den in der folgenden Tabelle aufgeführten Standardfeldern kann Ihre CSV-Datei auch zusätzliche Spaltenüberschriften für Event-Eigenschaften enthalten. Diese Eigenschaften sollten eine Spaltenüberschrift im Format `<event_name>.properties.<property name>` oder `<property name>` haben.

Beispielsweise könnte das angepasste Event `trip_booked` die Eigenschaften `destination` und `duration` haben. Sie können diese mit den Spaltenüberschriften `trip_booked.properties.destination` und `trip_booked.properties.duration` importieren. Sie können Eigenschaften in den Überschriften auch als `<property name>` darstellen. Braze erkennt die relevanten Eigenschaften für jedes Event anhand dessen, ob ein Wert in der entsprechenden CSV-Zelle vorhanden ist.

| Nutzerprofilfeld | Datentyp | Information | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Nutzerbezeichner für Ihre Nutzer:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `braze_id` | String | Ein von Braze zugewiesener Bezeichner für Ihre Nutzer:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_name` | String | Ein eindeutiger Nutzerbezeichner für anonyme Nutzer:innen, als Alternative zur `external_id`. Muss zusammen mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_label` | String | Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren. Muss zusammen mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `email` | String | Die E-Mail-Adresse Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `jane.doe@example.com`). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Siehe den folgenden Hinweis. |
| `phone` | String | Eine von Ihren Nutzer:innen angegebene Telefonnummer im `E.164`-Format (z. B. `+442071838750`). Weitere Informationen zur Formatierung finden Sie unter [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Siehe den folgenden Hinweis. |
| `name` | String | Ein angepasstes Event Ihrer Nutzer:innen. | Ja |
| `time` | String | Der Zeitpunkt des Events. Kann in einem der folgenden ISO-8601-Formate übergeben werden: „JJJJ-MM-TT“ „JJJJ-MM-TTTHH:MM:SS+00:00“ „JJJJ-MM-TTTHH:MM:SSZ“ „JJJJ-MM-TTTHH:MM:SS“ (z. B. 2019-11-20T18:38:57) | Ja |
| `<event name>.properties.<property name>` | Mehrere | Eine Event-Eigenschaft, die mit einem angepassten Event verknüpft ist. Ein Beispiel ist `trip_booked.properties.destination` | Nein |
| `<property name>` | Mehrere | Eine Event-Eigenschaft, die Sie über mehrere Event-Typen hinweg verwenden können. Ein Beispiel ist `destination`. Diese Eigenschaft wird einem Event zugeordnet, wenn ein nicht-leerer Wert in der entsprechenden CSV-Zelle vorhanden ist. | Nein |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Felder für angepasste Events" }

#### Formatierungsanforderungen für angepasste Events {#format-requirements-for-custom-events}

Beim Import von angepassten Events per CSV müssen Sie Ihre Datei gemäß den folgenden Anforderungen formatieren, damit der Datenimport erfolgreich ist.

##### Formatierung von angepassten Events verstehen {#understanding-custom-event-formatting}

Formatieren Sie Ihre CSV-Datei für angepasste Events korrekt mit Punkt-Notation oder mit einem nicht-leeren Wert in der entsprechenden Zelle, damit Braze jede Eigenschaft dem endgültigen Event zuordnet. Bei fehlerhafter Formatierung können Eigenschaften verworfen werden oder der Import kann fehlschlagen, insbesondere wenn mehrere Event-Typen in einer Datei enthalten sind.

##### Punkt-Notation für Event-Eigenschaften verwenden {#use-dot-notation-for-event-properties}

Verwenden Sie Punkt-Notation, um die hierarchische Beziehung zwischen einem angepassten Event und seinen Eigenschaften zu definieren. Diese Formatierungskonvention ermöglicht es Ihnen, strukturierte Event-Daten zu importieren, die spezifische Attribute für jedes Event enthalten.

Das Format der Punkt-Notation folgt dieser Struktur: `event_name.properties.property_name`

Die Punkt-Notation funktioniert in der folgenden Reihenfolge:

1. Zuerst kommt der Event-Name
2. Gefolgt von `.properties.`, um anzuzeigen, dass das Folgende eine Event-Eigenschaft ist
3. Zuletzt der spezifische Eigenschaftsname

**Beispiel:**

Für ein angepasstes Event namens `rented_movie` mit den Eigenschaften `movie_name` und `genre` wären Ihre CSV-Spaltenüberschriften:

- `rented_movie.properties.movie_name`
- `rented_movie.properties.genre`

Diese Notation weist Braze an, ein angepasstes Event namens `rented_movie` zu erstellen und die Eigenschaften `movie_name` und `genre` an diese spezifische Event-Instanz anzuhängen.

Wenn Sie eine Kombination aus Punkt-Notation und Nicht-Punkt-Notation für den Import von Eigenschaften verwenden, kann Ihr CSV-Upload fehlschlagen, weil Braze doppelte Überschriften erkennt. Dies tritt auf, wenn Sie die Überschriften `rented_movie.properties.movie_name` und `movie_name` in derselben Datei haben. Um dies zu vermeiden, verwenden Sie nur ein Eigenschaftsformat für Ihre Überschriften.

##### Ein Event pro Zeile {#one-event-per-row}

Jede Zeile in Ihrer CSV-Datei repräsentiert ein einzelnes angepasstes Event für eine:n einzelne:n Nutzer:in. Wenn eine Person mehrere Events hat, müssen Sie für jedes Event eine separate Zeile einfügen, auch wenn sie denselben Nutzerbezeichner verwenden.

{% alert important %}
Wenn eine Zeile Daten für ein bestimmtes Event enthält, füllen Sie nur die Spalten für die Eigenschaften dieses Events aus. Lassen Sie die Spalten für andere Events leer.
{% endalert %}

##### Beispiel einer CSV-Struktur {#example-csv-structure}

Die folgende Tabelle zeigt die korrekte Formatierung für den Import von angepassten Events mit Eigenschaften. Dieses Beispiel zeigt zwei Nutzer:innen, die jeweils verschiedene Events durchgeführt haben: eine Person hat einen Film ausgeliehen und eine andere hat einen Film gekauft.

| external_id | name | time | rented_movie.properties.movie_name | rented_movie.properties.genre | bought_movie.properties.movie_name | bought_movie.properties.genre |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 123 | rented_movie | 2024-06-10T12:00:00Z | Ghostbusters | Action | | |
| 456 | bought_movie | 2024-06-12T12:00:00Z | | | Ghostbusters | Action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Beispiel einer CSV-Struktur" }

In diesem Beispiel:

- Nutzer:in `123` hat das Event `rented_movie` mit den Eigenschaften `movie_name` (Ghostbusters) und `genre` (Action) ausgelöst
- Nutzer:in `456` hat das Event `bought_movie` mit den Eigenschaften `movie_name` (Ghostbusters) und `genre` (Action) ausgelöst
- Jedes Event füllt nur seine relevanten Eigenschaftsspalten aus und lässt die Eigenschaftsspalten anderer Events leer

{% endtab %}
{% endtabs %}

### Schritt 4: Ihre Datei hochladen {#step-4-upload-your-file}

Um Ihre Datei hochzuladen, wählen Sie **Attributes** oder **Events**, klicken Sie auf **Browse Files** und laden Sie Ihre CSV-Datei hoch. Braze zeigt eine Vorschau der ersten Zeilen und eine Zusammenfassung der erkannten Felder an.

Bei großen Dateien (bis zu 500 MB für Standardattribute und angepasste Attribute oder 50 MB für angepasste Events) kann das Dashboard während des Uploads und der Berechnung durch Braze vorübergehend nicht reagieren. Diese Uploads und Berechnungen können länger dauern als bei kleineren Dateien. Lassen Sie diesen Schritt abschließen. Weitere Informationen zu Dateigrößenbeschränkungen und Zeitrahmen finden Sie unter [Ihre CSV-Datei erstellen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

Benennen Sie Ihre CSV-Datei vor dem Upload mit dem Importnamen um, den Sie in Braze sehen möchten. Der Importname kann nach dem Upload nicht mehr geändert werden.

{% alert note %}
Die Dateivorschau zeigt nur die ersten Zeilen Ihrer Datei an. Um jede Zeile vor dem Import zu überprüfen, verwenden Sie die [Dateivalidierung](#file-validation).
{% endalert %}

{% alert important %}
CSV-Nutzerimporte stehen im Dashboard 14 Tage nach dem Upload zum Download bereit. Nach diesem Zeitraum wird die Datei aus dem Speicher gelöscht und ist nicht mehr zugänglich.
{% endalert %}

### Schritt 5: Ihre Felder zuordnen {#csv-data-mapping}

Nach der Vorschau können Sie Ihre CSV-Überschriften Braze-Attributen, Events oder Event-Eigenschaften zuordnen. Braze ordnet automatisch Felder in Ihrer CSV-Datei Attributen, Events oder Event-Eigenschaften mit identischem Namen zu und erstellt bei Bedarf neue Felder. Sie haben außerdem die Flexibilität, Vorschläge manuell anzupassen oder andere Attribute, Events oder Eigenschaften auszuwählen.

Für Event-Eigenschaften erkennt Braze Eigenschaften und verknüpft sie mit relevanten Events basierend darauf, ob eine CSV-Zelle einen nicht-leeren Wert enthält, oder anhand von Überschriften, die Punkt-Notation im Format `<event name>.properties.<property name>` verwenden.

![Die Seite für die Spaltenzuordnung.]({% image_buster /assets/img/csv_import/column_mapping_mapped.png %})

#### Zuordnungsstatus {#mapping-statuses}

Die Spalte für den Zuordnungsstatus zeigt die Aktion an, die beim Import Ihrer CSV-Datei ausgeführt wird, und kann einen der folgenden Werte haben.

| Zuordnungsstatus | Bedeutung |
|:---|:---|
| **Zugeordnet** | Feld wurde einem bestehenden Attribut, Event oder Bezeichner zugeordnet. |
| **Neues Attribut**, **Neues Event** oder **Neue Event-Eigenschaft** | Braze erstellt beim Import ein neues Attribut oder Event. Sie können es bearbeiten, indem Sie den Button **Edit new attribute**, **Edit new event** oder **Edit new property** auswählen. |
| **Datentypkonflikt** | Der erkannte Datentyp der CSV-Spalte stimmt nicht mit dem Datentyp des bestehenden Attributs, Events oder Bezeichners überein. Braze versucht, den Datentyp beim Import zu konvertieren, um ihn dem bestehenden Attribut anzupassen. Braze verwirft den Wert, wenn dies nicht möglich ist. |
| **Blocklistenattribut** oder **Blocklisten-Event** | Das CSV-Feld stimmt mit dem Namen eines blockierten Attributs oder Events überein. Wählen Sie ein anderes Attribut oder Event zur Zuordnung aus, oder es wird nicht importiert. |
| **Doppeltes Attribut** | Es gibt ein oder mehrere Felder mit demselben Namen in Ihrer CSV-Datei. Ordnen Sie die gleichnamigen Spalten verschiedenen Attributen zu, andernfalls wird nur die erste Spalte importiert. |
| **Reservierter Event-Schlüssel** | Der Name Ihrer Event-Eigenschaft entspricht einem in Braze reservierten Event-Schlüssel, wie `time` oder `event_name`. Geben Sie einen anderen Namen ein oder wählen Sie eine andere Eigenschaft zur Zuordnung aus, andernfalls wird sie verworfen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zuordnungsstatus" }


#### Neue Attribute, Events und Eigenschaften bearbeiten {#editing-new-attributes-events-and-properties}

Wenn ein passendes Attribut, Event oder eine Event-Eigenschaft in Ihrem Workspace nicht existiert, versucht Braze, beim Import ein neues Attribut, Event oder eine neue Eigenschaft zu erstellen, wobei der Name des CSV-Felds und der erkannte Datentyp verwendet werden. Sie können dieses neue Feld vor dem Import bearbeiten, indem Sie den Button **Edit new attribute**, **Edit new event** oder **Edit new property** neben dem Zuordnungsstatus auswählen.

![Der Button „Edit new attribute“ auf der Seite für die Spaltenzuordnung.]({% image_buster /assets/img/csv_import/column_mapping_edit_attribute_button.png %})


{% alert note %}
Sie können den Zuordnungsschritt nicht fortsetzen, bis ein Bezeichner zugeordnet ist. Braze ordnet nach Möglichkeit automatisch einen Bezeichner zu. Für angepasste Events müssen Sie außerdem die Spalten `name` und `time` zuordnen. Weitere Informationen finden Sie im Abschnitt **Erforderliche Felder**.
{% endalert %}

### Schritt 6: Targeting-Einstellungen wählen {#targeting-preferences}

Nach der Zuordnung können Sie auf der Seite „Importeinstellungen“ aus den folgenden Targeting-Einstellungen wählen. Wenn Sie keinen neuen Targeting-Filter oder kein neues Segment aus Ihrem Import erstellen müssen, wählen Sie **Do not make this list available as a targeting filter**.

| Option | Beschreibung |
|---|---|
| Targeting-Filter | Um Ihre CSV-Datei in eine Retargeting-Option beim Erstellen von Nutzersegmenten umzuwandeln, wählen Sie Ihre Datei aus dem Dropdown **Updated/Imported from CSV** und dann **Create targeting filter**. |
| Neue Segmente | Um zusätzlich ein neues Segment aus Ihrem neuen Targeting-Filter zu erstellen, wählen Sie **Create targeting filter and add to new segment**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 6: Targeting-Einstellungen wählen" }

![Eine Filtergruppe mit dem Filter „Updated/Imported from CSV“, der eine CSV-Datei mit dem Titel „Halloween season fun“ enthält.]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Schritt 7: Ihre Datei validieren (optional) {#file-validation}

Bevor Sie Ihren Import starten, können Sie eine Dateivalidierung ausführen, um jede Zeile auf Fehler und Warnungen zu prüfen. Um Ihre Datei zu validieren, wählen Sie auf der Seite „Importeinstellungen“ **Validate file before importing** und dann **Next**.

Die Validierung kann bei Dateien mit maximaler Größe bis zu 2 Minuten dauern. Während die Validierung läuft, können Sie **Skip validation** auswählen, um sie zu überspringen und sofort fortzufahren.

#### Validierungsergebnisse {#validation-results}

Wenn die Validierung abgeschlossen ist, wird eines der folgenden Ergebnisse angezeigt.

| Ergebnis | Bedeutung | Nächster Schritt |
|---|---|---|
| **Validierung abgeschlossen** | Keine Probleme gefunden. | Wählen Sie **Import data**. |
| **Probleme gefunden** | Einige Zeilen haben Fehler oder Warnungen. | Laden Sie den Fehlerbericht herunter, um die Probleme zu überprüfen, und wählen Sie dann **Import anyway**, um fortzufahren, oder **Cancel**, um Ihre Datei zuerst zu korrigieren. |
| **Validierung hat das Zeitlimit überschritten** | Die Validierung wurde nicht rechtzeitig abgeschlossen. Die überprüften Zeilen hatten keine Probleme. | Wählen Sie **Import data**. Ein vollständiger Bericht wird in wenigen Minuten verfügbar sein. |
| **Zeitlimit mit Problemen überschritten** | Die Validierung wurde nicht rechtzeitig abgeschlossen und hat in einigen der überprüften Zeilen Fehler gefunden. | Laden Sie den Teilbericht herunter, um die gefundenen Probleme zu überprüfen, und wählen Sie dann **Import anyway** oder **Cancel**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Validierungsergebnisse" }

![Die Zusammenfassungsseite mit dem Abschnitt „Gefundene Probleme“, der die Anzahl der Zeilen mit Fehlern und Warnungen anzeigt, mit Optionen zum Zurückgehen, Herunterladen des Fehlerberichts oder Starten des Imports.]({% image_buster /assets/img/csv_import/summary_page_validation_results.png %})

#### Den Fehlerbericht verstehen {#understanding-the-error-report}

Der Fehlerbericht ist eine CSV-Datei, die jede markierte Zeile zusammen mit ihren Originaldaten und einer Beschreibung des Problems enthält.

| Problemtyp | Beschreibung |
|---|---|
| **Fehler** | Die Zeile wird beim Import vollständig übersprungen. |
| **Warnung** | Die Zeile wird importiert, aber einige Werte werden verworfen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Den Fehlerbericht verstehen" }

Nach der Überprüfung des Berichts können Sie die Probleme in Ihrer Originaldatei korrigieren und erneut hochladen, oder den Import fortsetzen und die Teilergebnisse akzeptieren.



### Schritt 8: Ihren CSV-Import starten {#step-8-start-your-csv-import}

Wenn Sie bereit sind, wählen Sie **Start Import**. Sie können den aktuellen Fortschritt auf der Seite **Import Users** verfolgen, die sich automatisch alle 5 Sekunden aktualisiert.
Die Verarbeitung kann je nach Größe Ihrer CSV-Datei von einigen Minuten bis zu mehreren Stunden dauern. Während dieser Zeit kann das Dashboard nicht reagieren oder langsam sein, aber der Import läuft weiterhin.

{% alert note %}
Sie können mehr als eine CSV-Datei gleichzeitig importieren. CSV-Importe werden parallel ausgeführt, sodass die Reihenfolge der Aktualisierungen nicht garantiert seriell ist. Wenn Sie CSV-Importe nacheinander ausführen möchten, warten Sie, bis ein CSV-Import abgeschlossen ist, bevor Sie einen zweiten hochladen.
{% endalert %}

#### Importstatus {#import-statuses}

Nach dem Start Ihres Imports können Sie den Status auf der Seite **Import Users** überprüfen.

| Status | Beschreibung |
|---|---|
| **Abgeschlossen** | Alle Zeilen wurden erfolgreich importiert. |
| **Teilerfolg** | Einige Zeilen sind fehlgeschlagen. Wählen Sie das Drei-Punkte-Menü neben dem Import, um einen Fehlerbericht oder die ursprünglich hochgeladene CSV-Datei herunterzuladen. |
| **In Bearbeitung** | Der Import läuft gerade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Importstatus" }

![Die Seite „Import Users“ mit dem Status „Teilerfolg“ und geöffnetem Kontextmenü, das die Optionen „Fehlerbericht herunterladen“ und „Hochgeladene CSV herunterladen“ anzeigt.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

Der Fehlerbericht nach dem Import enthält Zeilen, die aus Gründen fehlgeschlagen sind, die die Validierung nicht abdeckt, z. B. wenn eine Person in Braze nicht existiert.

{% alert important %}
Zuvor hochgeladene CSV-Dateien stehen auf der Seite **Import Users** 14 Tage nach dem Upload-Datum zum Download bereit. Nach 14 Tagen wird die Datei endgültig gelöscht und kann nicht mehr abgerufen werden.
{% endalert %}

## Datenpunkt-Überlegungen {#data-point-considerations}

Jede über eine CSV-Datei importierte Kundendateninformation überschreibt den vorhandenen Wert in Nutzerprofilen und protokolliert einen Datenpunkt, mit Ausnahme von externen IDs und leeren Werten. Wenn Sie Fragen zu den Feinheiten der Braze-Datenpunkte haben, kann Ihr Account Manager:in bei Braze diese beantworten.

| Überlegung | Details |
|---|---|
| Externe IDs | Das Hochladen einer CSV-Datei, die nur `external_id` enthält, protokolliert keine Datenpunkte. So können Sie bestehende Braze-Nutzer:innen segmentieren, ohne die Datenlimits zu beeinflussen. Das Einbeziehen von Feldern wie `email` oder `phone` überschreibt jedoch vorhandene Nutzerdaten und protokolliert Datenpunkte. <br><br>CSV-Importe, die nur zur Segmentierung verwendet werden, protokollieren keine Datenpunkte, z. B. solche, die nur `external_id`, `braze_id` oder `user_alias_name` enthalten. |
| Leere Werte | Leere Werte in Ihrer CSV-Datei überschreiben keine vorhandenen Nutzerprofildaten. Sie müssen beim Import nicht alle Nutzerattribute oder angepassten Events angeben. |
| Abo-Status | Das Update or aktualisieren or aktualisieren von `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` wird **nicht** auf die Datenpunkt-Nutzung angerechnet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datenpunkt-Überlegungen" }

{% alert important %}
Wenn Sie `language` oder `country` für Nutzer:innen über einen CSV-Import oder die API festlegen, wird Braze daran gehindert, diese Informationen automatisch über das SDK or Software-Development-Kit zu erfassen.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Wenn Sie die [Dateivalidierung](#file-validation) verwendet haben, beginnen Sie mit dem Fehlerbericht, da er das spezifische Problem für jede markierte Zeile und eine Beschreibung zur Behebung enthält. Für Zeilen, die beim Import statt bei der Validierung fehlgeschlagen sind, laden Sie den Fehlerbericht herunter, indem Sie auf der Seite **Nutzer:innen importieren** mit der Maus über die Zeile fahren und den <i class="fas fa-download" title="Herunterladen"></i>-Button auswählen.

Zur Fehlerbehebung beim CSV-Import überprüfen Sie die folgenden häufigen Probleme in den nachstehenden Abschnitten.

### CSV-Import bleibt bei „Calculating“ stehen {#csv-import-stuck-on-calculating}

Unter **Nutzer:innen importieren** bedeutet `Calculating`, dass Braze die Datei noch für die Verarbeitung vorbereitet. Während dieses Schritts kann die Zeilenanzahl als `0 / Calculating` angezeigt werden, bis die Vorbereitung abgeschlossen ist.

Wenn Ihr Import bei „Calculating“ stehen zu bleiben scheint:

- Lassen Sie den Import weiterlaufen. Brechen Sie ihn nicht ab und laden Sie die Datei nicht erneut hoch, es sei denn, der Braze-Support empfiehlt es.
- Bestätigen Sie, dass Ihre Datei innerhalb der unterstützten Grenzen liegt, die unter [CSV erstellen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#import-options) beschrieben sind.
- Überprüfen Sie [Schritt 4: Datei hochladen](#step-4-upload-your-file) und [Schritt 8: CSV-Import starten](#step-8-start-your-csv-import) für das erwartete Dashboard-Verhalten und die Verarbeitungszeiten.
- Kontaktieren Sie den Braze-Support, wenn `Calculating` deutlich länger als für Ihre Dateigröße erwartet dauert, nachdem Sie diese Prüfungen durchgeführt haben.

### E-Mail als `external_id` verwenden {#use-email-as-external_id}

Braze empfiehlt nicht, eine E-Mail-Adresse als `external_id` zu verwenden. Wenn Sie eine E-Mail als `external_id` verwenden, fügen Sie sowohl die Spalte `external_id` als auch die Spalte `email` in Ihre CSV-Datei ein, damit Nutzer:innen weiterhin über den E-Mail-Kanal ansprechbar bleiben. Verwenden Sie ein Komma (`,`) als Spaltentrennzeichen – kein Doppelpunkt (`:`).

### Anführungszeichen in `external_id`-Werten {#quote-characters-in-external_id-values}

Wenn eine `external_id`-Zelle ein doppeltes Anführungszeichen enthält, maskieren Sie es durch Verdopplung des Zeichens (`""`), wie unter [Nicht maskierte oder unausgeglichene doppelte Anführungszeichen](#missing-row) beschrieben. Der CSV-Import verwendet keine Backslash-Maskierung.

### CSV-Import ist nicht als Segment-Filter verfügbar {#csv-import-isnt-available-as-a-segment-filter}

Sie können einen CSV-Import nur dann als Segment-Filter verwenden, wenn Sie beim Hochladen eine Targeting-Einstellung aktiviert haben.

So prüfen Sie, ob die Targeting-Verfügbarkeit für einen bestehenden Import aktiviert ist:

1. Suchen Sie auf der Seite **Nutzer:innen importieren** Ihren CSV-Import.
2. Prüfen Sie, ob **Zu Segment wechseln** für diesen Import angezeigt wird.
3. Wenn **Zu Segment wechseln** angezeigt wird, ist Ihre CSV-Datei im Segment-Filter `Updated/Imported from CSV` verfügbar.
4. Wenn **Zu Segment wechseln** nicht angezeigt wird, wurde die Targeting-Verfügbarkeit für diesen Import nicht aktiviert.

Sie können die Targeting-Verfügbarkeit nach Abschluss eines CSV-Uploads nicht mehr aktivieren. Um diese CSV-Datei als Segment-Filter zu verwenden, laden Sie die Datei erneut hoch und wählen Sie in [Schritt 6: Targeting-Einstellungen auswählen](#step-6-choose-targeting-preferences) die Option **Targeting-Filter erstellen** oder **Targeting-Filter erstellen und zu neuem Segment hinzufügen**.

Wenn Ihr Ziel darin besteht, ein Segment zu erstellen, ohne Profildaten zu Update or aktualisieren or aktualisieren, laden Sie eine CSV-Datei hoch, die nur Bezeichner-Spalten enthält (zum Beispiel `external_id` oder Alias-Bezeichner-Spalten), und wählen Sie dann **Targeting-Filter erstellen und zu neuem Segment hinzufügen**.

### Probleme mit der Dateiformatierung {#file-formatting-issues}

#### Fehlerhafte Zeile {#malformed-row}

Wenn Ihr Upload mit Fehlern abgeschlossen wurde, enthält Ihre CSV-Datei möglicherweise eine fehlerhafte Zeile.

Für den korrekten Datenimport muss eine Kopfzeile vorhanden sein. Jede Zeile muss die gleiche Anzahl an Zellen wie die Kopfzeile haben. Zeilen mit mehr oder weniger Werten als die Kopfzeile werden vom Import ausgeschlossen. Kommas in einem Wert werden als Trennzeichen interpretiert und können zu diesem Fehler führen.

Darüber hinaus müssen alle Daten UTF-8-kodiert sein. Wenn die Datei mit einer veralteten Kodierung gespeichert ist (zum Beispiel bei einigen Excel-Standardeinstellungen), können Sonderzeichen und URLs in Zellen beschädigt werden und als Fragezeichen (`?`) in Braze oder in gesendeten Nachrichten erscheinen.

Wenn Ihre CSV-Datei leere Zeilen enthält und weniger Zeilen als die Gesamtzahl der Zeilen in der CSV-Datei importiert werden, weist dies möglicherweise nicht auf ein Problem mit dem Import hin, da die leeren Zeilen nicht importiert werden müssen. Überprüfen Sie die Anzahl der korrekt importierten Zeilen und stellen Sie sicher, dass sie mit der Anzahl der Nutzer:innen übereinstimmt, die Sie importieren möchten.

#### Fehlende Zeile {#missing-row}

Es gibt mehrere Gründe, warum die Anzahl der importierten Nutzer:innen nicht mit der Gesamtzahl der Zeilen in Ihrer CSV-Datei übereinstimmen kann:

| Problem | Lösung |
|---|---|
| Doppelte externe IDs, Nutzer-Aliase, Braze-IDs, E-Mail-Adressen oder Telefonnummern | Wenn es doppelte Spalten für externe IDs gibt, kann dies zu fehlerhaften oder nicht importierten Zeilen führen, auch wenn die Zeilen korrekt formatiert sind. In einigen Fällen wird kein spezifischer Fehler gemeldet. Prüfen Sie auf Duplikate und entfernen Sie diese vor dem erneuten Hochladen. |
| Akzentzeichen | Ihre CSV-Datei kann Namen oder Attribute mit Akzenten enthalten. Stellen Sie sicher, dass die Datei UTF-8-kodiert ist, um Import-Probleme zu vermeiden. |
| Braze-ID gehört zu verwaisten Nutzer:innen | Wenn Nutzer:innen mit anderen zusammengeführt wurden und Braze die Braze-ID nicht dem verbleibenden Profil zuordnen kann, wird die Zeile nicht importiert. |
| Leere Zeile | Leere Zeilen in der CSV-Datei können fehlerhafte Datenfehler verursachen. Überprüfen Sie die Datei mit einem Nur-Text-Editor, nicht mit Excel oder Sheets. |
| Nicht maskierte oder unausgeglichene doppelte Anführungszeichen (`"`) | Doppelte Anführungszeichen umschließen String-Werte, die Kommas enthalten. Wenn ein Wert selbst ein doppeltes Anführungszeichen enthält, maskieren Sie es durch Verdopplung (`""`). Nicht maskierte oder unausgeglichene doppelte Anführungszeichen verursachen eine fehlerhafte Zeile. |
| Inkonsistente Zeilenumbrüche | Gemischte Zeilenumbrüche (z. B. `\n` und `\r\n`) können dazu führen, dass die erste Datenzeile als Teil der Kopfzeile behandelt wird. Verwenden Sie einen Hex- oder erweiterten Texteditor zum Überprüfen und Beheben. |
| Falsch kodierte Datei | Auch wenn Akzente zulässig sind, muss die Datei UTF-8-kodiert sein. Andere Kodierungen funktionieren möglicherweise teilweise, werden aber nicht vollständig unterstützt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlende Zeile" }

#### String-Anführungszeichen {#string-quotation}

Werte, die in einfache (`''`) oder doppelte (`""`) Anführungszeichen eingeschlossen sind, werden beim Import als Strings gelesen.

#### Falsch formatierte Daten {#incorrectly-formatted-dates}

Daten, die nicht im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format vorliegen, werden beim Import nicht als `datetimes` gelesen.

### Probleme mit der Datenstruktur {#data-structure-issues}

#### Ungültige E-Mail-Adressen {#invalid-email-addresses}

Wenn Ihr Upload mit Fehlern abgeschlossen wurde, enthält er möglicherweise eine oder mehrere ungültige verschlüsselte E-Mail-Adressen. Stellen Sie sicher, dass alle E-Mail-Adressen vor dem Import in Braze korrekt verschlüsselt sind.

- **Beim [Update or aktualisieren or aktualisieren oder Importieren von E-Mail-Adressen]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption#step-3-import-and-update-users)** in Braze verwenden Sie den gehashten E-Mail-Wert, wo immer eine E-Mail-Adresse enthalten ist. Diese gehashten E-Mail-Werte werden von Ihrem internen Team bereitgestellt.
- **Beim Erstellen neuer Nutzer:innen** müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail-Wert der Nutzer:innen hinzufügen. Andernfalls erstellt Braze die Nutzer:innen nicht. Wenn Sie einer bestehenden Person, die keine E-Mail-Adresse hat, eine E-Mail-Adresse hinzufügen, müssen Sie ebenfalls `email_encrypted` hinzufügen. Andernfalls aktualisiert Braze die Nutzer:innen nicht.

#### Daten werden als angepasstes Attribut importiert {#data-imported-as-custom-attribute}

Wenn Standardnutzerdaten (wie `email` oder `first_name`) als angepasstes Attribut importiert werden, überprüfen Sie die Groß-/Kleinschreibung und Leerzeichen in Ihrer CSV-Datei. Beispielsweise wird `First_name` als angepasstes Attribut importiert, während `first_name` korrekt in das Feld „Vorname“ im Kundenprofil or Nutzerprofil importiert wird.

#### Datentyp eines angepassten Attributs ändern {#change-a-custom-attributes-data-type}

Wenn Sie den Datentyp eines bestehenden angepassten Attributs ändern müssen (zum Beispiel von String zu Boolean), Update or aktualisieren or aktualisieren Sie den Datentyp auf der Seite [**Angepasste Attribute**]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) im Dashboard, bevor Sie Ihre CSV-Datei importieren. Wenn der Datentyp in Ihrer CSV-Datei nicht mit dem aktuell definierten Datentyp des Attributs übereinstimmt, schlägt der Import mit einem Fehler fehl.

#### Mehrere Datentypen {#multiple-data-types}

Braze erwartet, dass jeder Wert in einer Spalte den gleichen Datentyp hat. Werte, die nicht zum Datentyp ihres Attributs passen, verursachen Fehler bei der Segmentierung.

Zusätzlich verursacht es Probleme, wenn ein Zahlenattribut mit einer Null beginnt, da Zahlen mit führender Null als Strings betrachtet werden. Wenn Braze diesen String konvertiert, wird er möglicherweise als Oktalwert behandelt (der Ziffern von null bis sieben verwendet), was bedeutet, dass er in den entsprechenden Dezimalwert konvertiert wird. Wenn der Wert in der CSV-Datei beispielsweise 0130 ist, zeigt das Braze-Profil 88 an. Um dieses Problem zu vermeiden, verwenden Sie Attribute mit String-Datentypen. Dieser Datentyp ist jedoch nicht im Zahlenvergleich bei der Segmentierung verfügbar.

#### Standardattribut-Typen {#default-attribute-types}

Einige Standardattribute akzeptieren möglicherweise nur bestimmte Werte als gültig für Nutzeraktualisierungen. Weitere Hinweise finden Sie unter [CSV erstellen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

Nachgestellte Leerzeichen und Unterschiede in der Groß-/Kleinschreibung können dazu führen, dass ein Wert als ungültig interpretiert wird. Zum Beispiel wird in der folgenden CSV-Datei nur bei der Person in der ersten Zeile (`brazetest1`) der E-Mail- und Push-Status erfolgreich aktualisiert, da die akzeptierten Werte `unsubscribed`, `subscribed` und `opted_in` sind.

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@example.com,unsubscribed,unsubscribed
brazetest2,test2@example.com,Unsubscribed,Unsubscribed
```

### „CSV-Datei auswählen“ funktioniert nicht {#select-csv-file-is-not-working}

Es gibt mehrere Gründe, warum der Button **CSV-Datei auswählen** möglicherweise nicht funktioniert:

| Problem | Lösung |
|---|---|
| Pop-up-Blocker | Dies kann verhindern, dass die Seite angezeigt wird. Bestätigen Sie, dass Ihr Browser Pop-ups auf der Braze-Dashboard-Website zulässt. |
| Veralteter Browser | Stellen Sie sicher, dass Ihr Browser auf dem neuesten Stand ist; falls nicht, Update or aktualisieren or aktualisieren Sie ihn auf die neueste Version. |
| Hintergrundprozesse | Schließen Sie jede Browser-Instanz und starten Sie dann Ihren Computer neu. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="„CSV-Datei auswählen“ funktioniert nicht" }