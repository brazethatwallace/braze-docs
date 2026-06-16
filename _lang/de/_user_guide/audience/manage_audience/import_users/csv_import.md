---
nav_title: CSV-Import
article_title: CSV-Import
description: "Erfahren Sie, wie Sie Nutzerattribute und angepasste Events mithilfe des CSV-Imports erfassen und aktualisieren können."
page_order: 1.2
---

# CSV-Import {#csv-import}

> Erfahren Sie, wie Sie Nutzerattribute und angepasste Events mithilfe des CSV-Imports erfassen und aktualisieren können.

## Über den CSV-Import {#about-csv-import}

Sie können den CSV-Import verwenden, um die folgenden Nutzerattribute und angepassten Events zu erfassen und zu aktualisieren. Braze akzeptiert diese Daten als Standard-CSV-Dateien innerhalb der in der folgenden Tabelle angegebenen maximalen Dateigrößen.

| Typ | Definition | Beispiel | Maximale Dateigröße |
|---|---|---|---|
| Standardattribute | Reservierte Nutzerattribute, die von Braze erkannt werden. | `first_name`, `email` | 500 MB |
| Angepasste Attribute | Nutzerattribute, die für Ihr Unternehmen spezifisch sind. | `last_destination_searched` | 500 MB |
| Angepasste Events | Events, die für Ihr Unternehmen spezifisch sind und Nutzeraktionen darstellen. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Über den CSV-Import" }

## CSV-Import verwenden {#using-csv-import}

### 1. Schritt: CSV-Template herunterladen {#step-1-download-a-csv-template}

Um den CSV-Import zu öffnen, gehen Sie zu **Audiences** > **Import Users**. Dort finden Sie eine Tabelle mit Details zu den letzten Importen, wie z. B. das Upload-Datum, den Namen der hochladenden Person, den Dateinamen, die Targeting-Verfügbarkeit, die Anzahl der importierten Zeilen und den Status des Imports.

Um zu beginnen, wählen Sie **Attributes** oder **Events** und laden Sie dann das entsprechende Template herunter, das Ihnen beim Erstellen Ihrer CSV-Datei für den Upload hilft.

![Die Seite „Import Users“ im Braze-Dashboard.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### 2. Schritt: Bezeichner auswählen {#choose-an-identifier}

Die CSV-Datei, die Sie importieren, benötigt einen dedizierten Bezeichner. Wählen Sie einen der folgenden Bezeichnertypen für Ihren Import:

{% tabs local %}
<!-- TAB -->
{% tab Externe ID %}
Beim Import Ihrer Kundendaten können Sie eine `external_id` als eindeutigen Bezeichner für jede:n Kund:in verwenden. Wenn Sie in Ihrem Import eine `external_id` angeben, aktualisiert Braze alle bestehenden Nutzer:innen mit derselben `external_id` oder erstellt eine:n neu identifizierte:n Nutzer:in mit dieser `external_id`, falls keine Übereinstimmung gefunden wird.

- Download: [CSV-Attribut-Import-Template: Externe ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Download: [CSV-Event-Import-Template: Externe ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Wenn Sie eine Mischung aus Nutzer:innen mit einer `external_id` und Nutzer:innen ohne hochladen, müssen Sie für jeden Import eine separate CSV-Datei erstellen. Eine CSV-Datei kann nicht gleichzeitig `external_ids` und Nutzer-Aliase enthalten.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Nutzer-Alias %}
Um Nutzer:innen anzusprechen, die keine `external_id` haben, können Sie eine Liste von Nutzer:innen mit Nutzer-Aliasen importieren. Ein Alias dient als alternativer eindeutiger Nutzerbezeichner und kann hilfreich sein, wenn Sie versuchen, anonyme Nutzer:innen anzusprechen, die sich noch nicht registriert oder ein Konto in Ihrer App erstellt haben.

Wenn Sie Nutzerprofile hochladen oder aktualisieren, die nur einen Alias haben, müssen die folgenden zwei Spalten in Ihrer CSV-Datei vorhanden sein:

- `user_alias_name`: Ein eindeutiger Nutzerbezeichner; eine Alternative zur `external_id`
- `user_alias_label`: Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Schritt 2: Bezeichner auswählen" }

Wenn Sie sowohl einen `user_alias_name` als auch ein `user_alias_label` in Ihrem Import angeben, aktualisiert Braze alle bestehenden Nutzer:innen mit demselben `user_alias_name` und `user_alias_label`. Wenn keine Übereinstimmung gefunden wird, erstellt Braze eine:n neu identifizierte:n Nutzer:in mit diesem `user_alias_name`.

{% alert important %}
Sie können keinen CSV-Import verwenden, um bestehende Nutzer:innen mit einem `user_alias_name` zu aktualisieren, wenn diese bereits eine `external_id` haben. Stattdessen wird ein neues Nutzerprofil mit dem zugehörigen `user_alias_name` erstellt. Um eine:n Nutzer:in, die/der nur einen Alias hat, mit einer `external_id` zu verknüpfen, verwenden Sie den [Endpunkt „Nutzer:innen identifizieren“]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Download: [CSV-Attribut-Import-Template: Nutzer-Alias]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab Braze-ID %}
Um bestehende Nutzerprofile in Braze mithilfe eines internen Braze-ID-Werts anstelle einer `external_id` oder eines `user_alias_name`- und `user_alias_label`-Werts zu aktualisieren, geben Sie `braze_id` als Spaltenüberschrift an.

Dies kann hilfreich sein, wenn Sie Nutzerdaten über unsere CSV-Exportoption innerhalb der Segmentierung aus Braze exportiert haben und diesen bestehenden Nutzer:innen ein neues angepasstes Attribut hinzufügen möchten.

{% alert important %}
Sie können keinen CSV-Import verwenden, um neue Nutzer:innen mit einer `braze_id` zu erstellen. Diese Methode kann nur verwendet werden, um bereits bestehende Nutzer:innen innerhalb der Braze-Plattform zu aktualisieren.
{% endalert %}

{% alert tip %}
Der `braze_id`-Wert kann in CSV-Exporten aus dem Braze-Dashboard als `Appboy ID` bezeichnet sein. Diese ID ist identisch mit der `braze_id` einer/eines Nutzers/Nutzerin, sodass Sie diese Spalte beim erneuten Import der CSV-Datei in `braze_id` umbenennen können.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab E-Mail-Adresse und Telefonnummern %}
Sie können auf eine externe ID oder einen Nutzer-Alias verzichten und stattdessen entweder eine E-Mail-Adresse oder eine Telefonnummer verwenden, um Nutzer:innen zu importieren. Bevor Sie eine CSV-Datei mit E-Mail-Adressen oder Telefonnummern importieren, prüfen Sie Folgendes:

- Stellen Sie sicher, dass in Ihrer CSV-Datei keine externen IDs oder Nutzer-Aliase für diese Profile vorhanden sind. Falls doch, priorisiert Braze die externe ID oder den Nutzer-Alias vor der E-Mail-Adresse zur Identifizierung von Profilen.
- Bestätigen Sie, dass Ihre CSV-Datei korrekt formatiert ist.

{% alert note %}
Wenn Sie sowohl E-Mail-Adressen als auch Telefonnummern in Ihrer CSV-Datei angeben, wird die E-Mail-Adresse bei der Profilsuche gegenüber der Telefonnummer priorisiert.
{% endalert %}

Wenn ein bestehendes Profil diese E-Mail-Adresse oder Telefonnummer hat, wird dieses Profil aktualisiert, und Braze erstellt kein neues Profil. Wenn es mehrere Profile mit derselben E-Mail-Adresse gibt, verwendet Braze dieselbe Logik wie der [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), wobei das zuletzt aktualisierte Profil aktualisiert wird.

Wenn kein Profil mit dieser E-Mail-Adresse oder Telefonnummer existiert, erstellt Braze ein neues Profil mit diesem Bezeichner. Sie können den [`/users/identify`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) verwenden, um dieses Profil später zu identifizieren. Um ein Nutzerprofil zu löschen, können Sie auch den [`/users/delete`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) verwenden.
{% endtab %}
{% endtabs %}

### 3. Schritt: CSV-Datei erstellen {#step-3-build-your-csv-file}

Sie können einen der folgenden Datentypen als einzelne CSV-Datei hochladen. Um mehr als einen Datentyp hochzuladen, laden Sie mehrere CSV-Dateien hoch.

- **Nutzerattribute:** Dies umfasst sowohl Standard- als auch angepasste Nutzerattribute. Standardattribute sind reservierte Schlüssel in Braze (wie `first_name` oder `email`), und angepasste Attribute sind Nutzerattribute, die für Ihr Unternehmen spezifisch sind (wie `last_destination_searched`).
- **Angepasste Events:** Diese sind für Ihr Unternehmen spezifisch und spiegeln Aktionen wider, die Nutzer:innen durchgeführt haben, wie z. B. `trip_booked` für eine Reisebuchungs-App.

Wenn Sie bereit sind, Ihre CSV-Datei zu erstellen, beachten Sie die folgenden Informationen:

{% tabs local %}
<!-- TAB -->
{% tab Nutzerattribute %}
#### Erforderliche Bezeichner {#required-identifiers-attributes}

Obwohl `external_id` nicht erforderlich ist, muss Ihre CSV-Datei einen Nutzerbezeichner enthalten, der **einem** der folgenden Bezeichner zugeordnet werden kann. Details zu jedem einzelnen finden Sie unter [Bezeichner auswählen](#choose-an-identifier).

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
| Boolescher Wert | Akzeptiert `true` oder `false`. |
| Zahl | Muss eine Ganzzahl oder Gleitkommazahl ohne Leerzeichen oder Kommas sein. Gleitkommazahlen müssen einen Punkt (`.`) als Dezimaltrennzeichen verwenden. |
| String | Kann Kommas enthalten, wenn der Wert in doppelte Anführungszeichen (`""`) eingeschlossen ist. |
| Leer | Leere Werte überschreiben keine bestehenden Werte im Nutzerprofil, und Sie müssen nicht alle bestehenden Nutzerattribute in Ihrer CSV-Datei angeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Attribute" }

{% alert important %}
Arrays, Push-Token und angepasste Event-Datentypen werden beim Nutzerimport nicht unterstützt, da Kommas in Ihrer CSV-Datei als Spaltentrennzeichen interpretiert werden und beim Parsen Ihrer Datei Fehler verursachen.<br><br>Um diese Art von Werten hochzuladen, verwenden Sie stattdessen den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder die [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/).
{% endalert %}

#### Standardattribute {#default-attributes}

{% alert important %}
Beim Import von Standardattributen müssen die verwendeten Spaltenüberschriften exakt der Schreibweise und Groß-/Kleinschreibung der Standard-Nutzerattribute entsprechen. Andernfalls erkennt Braze diese als [angepasste Attribute](#custom-attributes).
{% endalert %}

{% alert tip %}
Die vollständige Liste der von Braze erkannten Standardattribute (über SDK, API, CSV und Cloud-Datenaufnahme) finden Sie unter [Standardattribute]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes/). Die folgende Tabelle enthält nur die Teilmenge, die über den CSV-Import festgelegt werden kann.
{% endalert %}

Die folgenden Standardattribute stehen für den Nutzerimport zur Verfügung.

| Nutzerprofilfeld | Datentyp | Beschreibung | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Nutzerbezeichner für Ihre Kund:innen. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_name` | String | Ein eindeutiger Nutzerbezeichner für anonyme Nutzer:innen als Alternative zur `external_id`. Muss zusammen mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `user_alias_label` | String | Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren. Muss zusammen mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-attributes). |
| `first_name` | String | Der Vorname Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `Jane`). | Nein |
| `last_name` | String | Der Nachname Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `Doe`). | Nein |
| `email` | String | Die E-Mail-Adresse Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `jane.doe@braze.com`). | Nein |
| `country` | String | Ländercodes müssen im ISO-3166-1-Alpha-2-Standard an Braze übergeben werden (z. B. `GB`). | Nein |
| `dob` | String | Muss im Format „YYYY-MM-DD“ übergeben werden (z. B. `1980-12-21`). Damit wird das Geburtsdatum Ihrer Nutzer:innen importiert und Sie können Nutzer:innen ansprechen, deren Geburtstag „heute“ ist. | Nein |
| `gender` | String | „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (möchte nicht angeben) oder nil (unbekannt). | Nein |
| `home_city` | String | Der Wohnort Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `London`). | Nein |
| `language` | String | Die Sprache muss im ISO-639-1-Standard an Braze übergeben werden (z. B. `en`). Weitere Informationen finden Sie in unserer [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes/). | Nein |
| `phone` | String | Eine Telefonnummer, wie von Ihren Nutzer:innen angegeben, im `E.164`-Format (z. B. `+442071838750`). Formatierungshinweise finden Sie unter [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/). | Nein |
| `email_open_tracking_disabled` | Boolescher Wert | Akzeptiert true oder false. Setzen Sie den Wert auf true, um zu verhindern, dass das Öffnungs-Tracking-Pixel zu allen zukünftigen E-Mails an diese:n Nutzer:in hinzugefügt wird. Nur für SparkPost und SendGrid verfügbar. | Nein |
| `email_click_tracking_disabled` | Boolescher Wert | Akzeptiert true oder false. Setzen Sie den Wert auf true, um das Klick-Tracking für alle Links in zukünftigen E-Mails an diese:n Nutzer:in zu deaktivieren. Nur für SparkPost und SendGrid verfügbar. | Nein |
| `email_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von E-Mail-Nachrichten registriert), `unsubscribed` (explizit vom Empfang von E-Mail-Nachrichten abgemeldet) und `subscribed` (weder angemeldet noch abgemeldet). | Nein |
| `push_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von Push-Nachrichten registriert), `unsubscribed` (explizit vom Empfang von Push-Nachrichten abgemeldet) und `subscribed` (weder angemeldet noch abgemeldet). | Nein |
| `time_zone` | String | Die Zeitzone muss im selben Format wie die IANA-Zeitzonendatenbank an Braze übergeben werden (z. B. `America/New_York` oder `Eastern Time (US & Canada)`). | Nein |
| `date_of_first_session`  `date_of_last_session` | String | Kann in einem der folgenden ISO-8601-Formate übergeben werden: „YYYY-MM-DD“ „YYYY-MM-DDTHH:MM:SS+00:00“ „YYYY-MM-DDTHH:MM:SSZ“ „YYYY-MM-DDTHH:MM:SS“ (z. B. 2019-11-20T18:38:57) | Nein |
| `subscription_group_id` | String | Die `id` Ihrer Abo-Gruppe. Dieser Bezeichner ist auf der Abo-Gruppenseite Ihres Dashboards zu finden. | Nein |
| `subscription_state` | String | Der Abo-Status für die durch `subscription_group_id` angegebene Abo-Gruppe. Zulässige Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe). | Nein, aber dringend empfohlen, wenn `subscription_group_id` verwendet wird |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Standardattribute" }

#### Abo-Gruppenstatus aktualisieren (optional) {#updating-subscription-group-status-optional}

Zusätzlich können Sie Nutzer:innen über den Nutzerimport zu E-Mail- oder SMS-Abo-Gruppen hinzufügen. Dies ist besonders für SMS nützlich, da Nutzer:innen in eine SMS-Abo-Gruppe eingetragen sein müssen, um über den SMS-Kanal Nachrichten zu erhalten. Weitere Informationen finden Sie unter [SMS-Abo-Gruppen](https://www.braze.com/docs/sms_rcs_subscription_groups#subscription-group-mms-enablement).

Wenn Sie Abo-Gruppenstatus aktualisieren, müssen die folgenden zwei Spalten in Ihrer CSV-Datei vorhanden sein:

- `subscription_group_id`: Die `id` der [Abo-Gruppe](https://www.braze.com/docs/user_guide/channels/email/subscriptions#subscription-groups).
- `subscription_state`: Verfügbare Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abo-Gruppenstatus aktualisieren (optional)" }

{% alert note %}
Pro Zeile im Nutzerimport kann nur eine einzige `subscription_group_id` festgelegt werden. Verschiedene Zeilen können unterschiedliche `subscription_group_id`-Werte haben. Wenn Sie jedoch dieselben Nutzer:innen in mehrere Abo-Gruppen eintragen müssen, sind mehrere Importe erforderlich.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Angepasste Events %}
#### Erforderliche Bezeichner {#required-identifiers-custom-events}

Obwohl `external_id` nicht erforderlich ist, **müssen** Sie **einen** der folgenden Bezeichner als Überschrift in Ihrer CSV-Datei angeben. Details zu jedem einzelnen finden Sie unter [Bezeichner auswählen](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **und** `user_alias_label`
- `email`
- `phone`

#### Felder für angepasste Events {#custom-event-fields}

Zusätzlich zu den folgenden Feldern kann Ihre CSV-Datei auch weitere Spaltenüberschriften für Event-Eigenschaften enthalten. Diese Eigenschaften sollten eine Spaltenüberschrift im Format `<event_name>.properties.<property name>.` haben.

Zum Beispiel könnte das angepasste Event `trip_booked` die Eigenschaften `destination` und `duration` haben. Diese können importiert werden, indem die Spaltenüberschriften `trip_booked.properties.destination` und `trip_booked.properties.duration` verwendet werden.

| Nutzerprofilfeld | Datentyp | Information | Erforderlich? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | Ein eindeutiger Nutzerbezeichner für Ihre:n Nutzer:in. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `braze_id` | String | Ein von Braze zugewiesener Bezeichner für Ihre:n Nutzer:in. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_name` | String | Ein eindeutiger Nutzerbezeichner für anonyme Nutzer:innen als Alternative zur `external_id`. Muss zusammen mit `user_alias_label` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `user_alias_label` | String | Ein gemeinsames Label, um Nutzer-Aliase zu gruppieren. Muss zusammen mit `user_alias_name` verwendet werden. | Bedingt. Siehe [Erforderliche Bezeichner](#required-identifiers-custom-events). |
| `email` | String | Die E-Mail-Adresse Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `jane.doe@braze.com`). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Siehe den folgenden Hinweis. |
| `phone` | String | Eine Telefonnummer, wie von Ihren Nutzer:innen angegeben, im `E.164`-Format (z. B. `+442071838750`). Formatierungshinweise finden Sie unter [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/). | Nein, und kann nur verwendet werden, wenn keine anderen Bezeichner vorhanden sind. Siehe den folgenden Hinweis. |
| `name` | String | Ein angepasstes Event Ihrer Nutzer:innen. | Ja |
| `time` | String | Der Zeitpunkt des Events. Kann in einem der folgenden ISO-8601-Formate übergeben werden: „YYYY-MM-DD“ „YYYY-MM-DDTHH:MM:SS+00:00“ „YYYY-MM-DDTHH:MM:SSZ“ „YYYY-MM-DDTHH:MM:SS“ (z. B. 2019-11-20T18:38:57) | Ja |
| `<event name>.properties.<property name>` | Mehrere | Eine Event-Eigenschaft, die mit einem angepassten Event verknüpft ist. Ein Beispiel ist `trip_booked.properties.destination` | Nein |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Felder für angepasste Events" }

#### Formatierungsanforderungen für angepasste Events {#format-requirements-for-custom-events}

Beim Import angepasster Events über CSV müssen Sie Ihre Datei gemäß den folgenden Anforderungen formatieren, um einen erfolgreichen Datenimport zu gewährleisten.

##### Formatierung angepasster Events verstehen {#understanding-custom-event-formatting}

Es ist wichtig, Ihre CSV-Datei für angepasste Events korrekt mit Punktnotation zu formatieren, damit jede Eigenschaft dem richtigen Event zugeordnet wird. Wenn das Format nicht korrekt ist, können Eigenschaften verworfen werden oder der Import kann fehlschlagen, insbesondere wenn mehrere Event-Typen in einer Datei enthalten sind.

##### Punktnotation für Event-Eigenschaften verwenden {#use-dot-notation-for-event-properties}

Die Punktnotation wird verwendet, um die hierarchische Beziehung zwischen einem angepassten Event und seinen Eigenschaften zu definieren. Diese Formatierungskonvention ermöglicht es Ihnen, strukturierte Event-Daten zu importieren, die spezifische Attribute für jedes Event enthalten.

Das Format der Punktnotation folgt dieser Struktur: `event_name.properties.property_name`

Die Punktnotation funktioniert in der folgenden Reihenfolge:

1. Zuerst kommt der Event-Name
2. Gefolgt von `.properties.`, um anzuzeigen, dass das Folgende eine Event-Eigenschaft ist
3. Schließlich der spezifische Eigenschaftsname

**Beispiel:**

Für ein angepasstes Event namens `rented_movie` mit den Eigenschaften `movie_name` und `genre` wären Ihre CSV-Spaltenüberschriften:

- `rented_movie.properties.movie_name`
- `rented_movie.properties.genre`

Diese Notation weist Braze an, ein angepasstes Event namens `rented_movie` zu erstellen und die Eigenschaften `movie_name` und `genre` dieser spezifischen Event-Instanz zuzuordnen.

##### Ein Event pro Zeile {#one-event-per-row}

Jede Zeile in Ihrer CSV-Datei repräsentiert ein einzelnes angepasstes Event für eine:n einzelne:n Nutzer:in. Wenn eine:r Nutzer:in mehrere Events hat, müssen Sie für jedes Event eine separate Zeile einfügen, auch wenn sie denselben Nutzerbezeichner teilen.

{% alert important %}
Wenn eine Zeile Daten für ein bestimmtes Event enthält, füllen Sie nur die Spalten für die Eigenschaften dieses Events aus. Lassen Sie die Spalten für andere Events leer.
{% endalert %}

##### Beispiel-CSV-Struktur {#example-csv-structure}

Die folgende Tabelle zeigt die korrekte Formatierung für den Import angepasster Events mit Eigenschaften. Dieses Beispiel zeigt zwei Nutzer:innen, die jeweils unterschiedliche Events durchgeführt haben: Eine:r hat einen Film ausgeliehen und eine:r hat einen Film gekauft.

| external_id | name | time | rented_movie.properties.movie_name | rented_movie.properties.genre | bought_movie.properties.movie_name | bought_movie.properties.genre |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 123 | rented_movie | 2024-06-10T12:00:00Z | Ghostbusters | Action | | |
| 456 | bought_movie | 2024-06-12T12:00:00Z | | | Ghostbusters | Action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Beispiel-CSV-Struktur" }

In diesem Beispiel:

- Nutzer:in `123` hat das Event `rented_movie` mit den Eigenschaften `movie_name` (Ghostbusters) und `genre` (Action) ausgelöst
- Nutzer:in `456` hat das Event `bought_movie` mit den Eigenschaften `movie_name` (Ghostbusters) und `genre` (Action) ausgelöst
- Jedes Event füllt nur seine relevanten Eigenschaftsspalten aus, während die Eigenschaftsspalten anderer Events leer bleiben

{% endtab %}
{% endtabs %}

### 4. Schritt: Datei hochladen {#step-4-upload-your-file}

Um Ihre Datei hochzuladen, wählen Sie **Attributes** oder **Events**, klicken Sie auf **Browse Files** und laden Sie Ihre CSV-Datei hoch. Braze zeigt eine Vorschau der ersten Zeilen und eine Zusammenfassung der erkannten Felder an.

Bei großen Dateien (bis zu 500 MB für Standardattribute und angepasste Attribute oder 50 MB für angepasste Events) kann das Dashboard vorübergehend nicht reagieren, während die Datei hochgeladen wird und Braze den Import berechnet. Diese Uploads und Berechnungen können länger dauern als bei kleineren Dateien. Lassen Sie diesen Schritt abschließen. Weitere Informationen zu Dateigrößenlimits und Zeitangaben finden Sie unter [CSV-Datei erstellen]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Im Feld **Import name** können Sie Ihren Import umbenennen. Standardmäßig wird der Dateiname verwendet.

{% alert note %}
Die Dateivorschau zeigt nur die ersten Zeilen Ihrer Datei. Um jede Zeile vor dem Import zu prüfen, verwenden Sie die [Dateivalidierung](#file-validation).
{% endalert %}

### 5. Schritt: Felder zuordnen (für Attribute) {#csv-data-mapping}

Nach der Vorschau können Sie Ihre CSV-Überschriften Braze-Attributen zuordnen. Braze ordnet Felder in Ihrer CSV-Datei automatisch Attributen mit identischen Namen zu und erstellt bei Bedarf neue Attribute. Sie haben außerdem die Möglichkeit, Vorschläge manuell anzupassen oder andere Attribute für beliebige Spalten auszuwählen.

![Die Spaltenzuordnungsseite.]({% image_buster /assets/img/csv_import/column_mapping_mapped.png %})

#### Zuordnungsstatus {#mapping-statuses}

Die Spalte „Zuordnungsstatus“ zeigt die Aktion an, die beim Import Ihrer CSV-Datei ausgeführt wird, und kann einen der folgenden Werte haben.

| Zuordnungsstatus | Bedeutung |
|:---|:---|
| **Zugeordnet** | Feld wurde einem bestehenden Attribut oder Bezeichner zugeordnet. |
| **Neues Attribut** | Braze erstellt beim Import ein neues Attribut. Sie können dieses Attribut bearbeiten, indem Sie den Button **Edit new attribute** auswählen. |
| **Datentyp-Konflikt** | Der erkannte Datentyp der CSV-Spalte stimmt nicht mit dem Datentyp des bestehenden Attributs oder Bezeichners überein. Braze versucht, den Datentyp beim Import zu konvertieren, um ihn an das bestehende Attribut anzupassen. Der Wert wird verworfen, wenn dies nicht möglich ist. |
| **Blocklist-Attribut** | Das CSV-Feld stimmt mit dem Namen eines blockierten Attributs überein. Wählen Sie ein anderes Attribut für die Zuordnung aus, oder die Spalte wird nicht importiert. |
| **Doppeltes Attribut** | Es gibt ein oder mehrere Felder mit demselben Namen in Ihrer CSV-Datei. Ordnen Sie die gleichnamigen Spalten verschiedenen Attributen zu, oder es wird nur die erste Spalte importiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zuordnungsstatus" }


#### Neue Attribute bearbeiten {#editing-new-attributes}

Wenn ein passendes Attribut in Ihrem Workspace nicht existiert, versucht Braze, beim Import ein neues Attribut mit dem Namen des CSV-Felds und dem erkannten Datentyp zu erstellen. Sie können dieses neue Attribut vor dem Import bearbeiten, indem Sie den Button **Edit new attribute** neben dem Zuordnungsstatus auswählen.

![Der Button „Edit new attribute“ auf der Spaltenzuordnungsseite.]({% image_buster /assets/img/csv_import/column_mapping_edit_attribute_button.png %})


{% alert note %}
Sie können den Zuordnungsschritt erst fortsetzen, wenn ein Bezeichner zugeordnet ist. Braze ordnet nach Möglichkeit automatisch einen Bezeichner zu. Im Abschnitt **Required fields** können Sie prüfen, ob ein Bezeichner zugeordnet ist.
{% endalert %}

### 6. Schritt: Targeting-Einstellungen wählen {#targeting-preferences}

Nach der Zuordnung können Sie auf der Seite „Import-Einstellungen“ aus den folgenden Targeting-Einstellungen wählen. Wenn Sie keinen neuen Targeting-Filter oder kein neues Segment aus Ihrem Import erstellen müssen, wählen Sie **Do not make this list available as a targeting filter**.

| Option | Beschreibung |
|---|---|
| Targeting-Filter | Um Ihre CSV-Datei in eine Retargeting-Option beim Erstellen von Nutzersegmenten umzuwandeln, wählen Sie Ihre Datei aus dem Dropdown **Updated/Imported from CSV** und dann **Create targeting filter**. |
| Neue Segmente | Um zusätzlich ein neues Segment aus Ihrem neuen Targeting-Filter zu erstellen, wählen Sie **Create targeting filter and add to new segment**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 6: Targeting-Einstellungen wählen" }

![Eine Filtergruppe mit dem Filter „Updated/Imported from CSV“, der eine CSV-Datei mit dem Titel „Halloween season fun“ enthält.]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### 7. Schritt: Datei validieren (optional) {#file-validation}

Bevor Sie Ihren Import starten, können Sie eine Dateivalidierung durchführen, um jede Zeile auf Fehler und Warnungen zu prüfen. Um Ihre Datei zu validieren, wählen Sie **Validate file before importing** auf der Seite „Import-Einstellungen“ und klicken Sie dann auf **Next**.

Die Validierung kann bei Dateien mit der maximal zulässigen Größe bis zu 2 Minuten dauern. Während die Validierung läuft, können Sie **Skip validation** auswählen, um sie zu überspringen und sofort fortzufahren.

#### Validierungsergebnisse {#validation-results}

Wenn die Validierung abgeschlossen ist, wird eines der folgenden Ergebnisse angezeigt.

| Ergebnis | Bedeutung | Nächster Schritt |
|---|---|---|
| **Validierung abgeschlossen** | Keine Probleme gefunden. | Wählen Sie **Import data**. |
| **Probleme gefunden** | Einige Zeilen haben Fehler oder Warnungen. | Laden Sie den Fehlerbericht herunter, um die Probleme zu prüfen, und wählen Sie dann **Import anyway**, um fortzufahren, oder **Cancel**, um Ihre Datei zuerst zu korrigieren. |
| **Validierung abgelaufen** | Die Validierung hat das Zeitlimit überschritten. Die geprüften Zeilen hatten keine Probleme. | Wählen Sie **Import data**. Ein vollständiger Bericht ist in wenigen Minuten verfügbar. |
| **Validierung abgelaufen mit Problemen** | Die Validierung hat das Zeitlimit überschritten und Fehler in einigen der geprüften Zeilen gefunden. | Laden Sie den Teilbericht herunter, um die gefundenen Probleme zu prüfen, und wählen Sie dann **Import anyway** oder **Cancel**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Validierungsergebnisse" }

![Die Zusammenfassungsseite mit dem Abschnitt „Probleme gefunden“, der die Anzahl der Zeilen mit Fehlern und Warnungen anzeigt, sowie Optionen zum Zurückgehen, Herunterladen des Fehlerberichts oder Starten des Imports.]({% image_buster /assets/img/csv_import/summary_page_validation_results.png %})

#### Den Fehlerbericht verstehen {#understanding-the-error-report}

Der Fehlerbericht ist eine CSV-Datei, die jede markierte Zeile zusammen mit ihren Originaldaten und einer Beschreibung des Problems enthält.

| Problemtyp | Beschreibung |
|---|---|
| **Fehler** | Die Zeile wird beim Import vollständig übersprungen. |
| **Warnung** | Die Zeile wird importiert, aber einige Werte werden verworfen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Den Fehlerbericht verstehen" }

Nach der Überprüfung des Berichts können Sie die Probleme in Ihrer Originaldatei korrigieren und erneut hochladen oder mit dem Import fortfahren und die Teilergebnisse akzeptieren.



### 8. Schritt: CSV-Import starten {#step-8-start-your-csv-import}

Wenn Sie bereit sind, wählen Sie **Start Import**. Sie können den aktuellen Fortschritt auf der Seite **Import Users** verfolgen, die sich automatisch alle 5 Sekunden aktualisiert.
Die Verarbeitung kann je nach Größe Ihrer CSV-Datei von wenigen Minuten bis zu mehreren Stunden dauern. Während dieser Zeit kann das Dashboard nicht reagieren oder langsam antworten, aber der Import läuft weiter.

{% alert note %}
Sie können mehr als eine CSV-Datei gleichzeitig importieren. CSV-Importe laufen parallel, sodass die Reihenfolge der Aktualisierungen nicht garantiert seriell ist. Wenn Sie CSV-Importe nacheinander ausführen müssen, warten Sie, bis ein CSV-Import abgeschlossen ist, bevor Sie einen zweiten hochladen.
{% endalert %}

#### Importstatus {#import-statuses}

Nach dem Start Ihres Imports können Sie den Status auf der Seite **Import Users** überprüfen.

| Status | Beschreibung |
|---|---|
| **Abgeschlossen** | Alle Zeilen wurden erfolgreich importiert. |
| **Teilerfolg** | Einige Zeilen sind fehlgeschlagen. Wählen Sie das Drei-Punkte-Menü neben dem Import, um einen Fehlerbericht oder die ursprünglich hochgeladene CSV-Datei herunterzuladen. |
| **In Bearbeitung** | Der Import läuft derzeit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Importstatus" }

![Die Seite „Import Users“ mit dem Status „Teilerfolg“ und geöffnetem Kontextmenü, das die Optionen „Fehlerbericht herunterladen“ und „Hochgeladene CSV herunterladen“ anzeigt.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

Der Fehlerbericht nach dem Import enthält Zeilen, die aus Gründen fehlgeschlagen sind, die die Validierung nicht abdeckt, z. B. wenn eine:r Nutzer:in in Braze nicht existiert.

{% alert important %}
Zuvor hochgeladene CSV-Dateien können 14 Tage nach dem Upload-Datum von der Seite **Import Users** heruntergeladen werden. Nach 14 Tagen wird die Datei dauerhaft gelöscht und ist nicht mehr zugänglich.
{% endalert %}

## Überlegungen zu Datenpunkten {#data-point-considerations}

Jedes importierte Kundendatum aus einer CSV-Datei überschreibt den bestehenden Wert in Nutzerprofilen und protokolliert einen Datenpunkt, mit Ausnahme von externen IDs und leeren Werten. Bei Fragen zu den Feinheiten der Braze-Datenpunkte kann Ihr Braze Account Manager diese beantworten.

| Überlegung | Details |
|---|---|
| Externe IDs | Das Hochladen einer CSV-Datei, die nur `external_id` enthält, protokolliert keine Datenpunkte. Dies ermöglicht es Ihnen, bestehende Braze-Nutzer:innen zu segmentieren, ohne Datenlimits zu beeinflussen. Das Hinzufügen von Feldern wie `email` oder `phone` überschreibt jedoch bestehende Nutzerdaten und protokolliert **Datenpunkte**. <br><br>CSV-Importe, die nur zur Segmentierung verwendet werden, protokollieren keine Datenpunkte, z. B. solche, die nur `external_id`, `braze_id` oder `user_alias_name` enthalten. |
| Leere Werte | Leere Werte in Ihrer CSV-Datei überschreiben keine bestehenden Nutzerprofildaten. Sie müssen nicht alle Nutzerattribute oder angepassten Events beim Import angeben. |
| Abo-Status | Das Aktualisieren von `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` wird **nicht** auf die Datenpunkt-Nutzung angerechnet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Überlegungen zu Datenpunkten" }

{% alert important %}
Das Setzen von `language` oder `country` für eine:n Nutzer:in über CSV-Import oder API verhindert, dass Braze diese Informationen automatisch über das SDK erfasst.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Wenn Sie die [Dateivalidierung](#file-validation) verwendet haben, beginnen Sie mit dem Fehlerbericht, da dieser das spezifische Problem für jede markierte Zeile und eine Beschreibung zur Behebung enthält. Für Zeilen, die während des Imports und nicht während der Validierung fehlgeschlagen sind, laden Sie den Fehlerbericht herunter, indem Sie auf der Seite **Import Users** mit der Maus über die Zeile fahren und den <i class="fas fa-download" aria-label="Herunterladen"></i>-Button auswählen.

Zur Fehlerbehebung beim CSV-Import lesen Sie die folgenden häufigen Probleme.

### E-Mail als `external_id` verwenden {#use-email-as-external_id}

Braze empfiehlt nicht, eine E-Mail-Adresse als `external_id` zu verwenden. Wenn Sie E-Mail als `external_id` verwenden, fügen Sie sowohl die Spalte `external_id` als auch die Spalte `email` in Ihre CSV-Datei ein, damit Nutzer:innen weiterhin über den E-Mail-Kanal ansprechbar bleiben. Verwenden Sie ein Komma (`,`) als Spaltentrennzeichen – keinen Doppelpunkt (`:`).

### Anführungszeichen in `external_id`-Werten {#quote-characters-in-external_id-values}

Wenn eine `external_id`-Zelle ein doppeltes Anführungszeichen enthält, escapen Sie es durch Verdopplung des Zeichens (`""`), wie unter [Nicht-escapte oder unausgeglichene doppelte Anführungszeichen](#missing-row) beschrieben. Der CSV-Import verwendet kein Backslash-Escaping.

### CSV-Import ist nicht als Segment-Filter verfügbar {#csv-import-isnt-available-as-a-segment-filter}

Sie können einen CSV-Import nur dann als Segment-Filter verwenden, wenn Sie während des Uploads eine Targeting-Einstellung aktiviert haben.

Um zu prüfen, ob die Targeting-Verfügbarkeit für einen bestehenden Import aktiviert ist:

1. Suchen Sie auf der Seite **Import Users** Ihren CSV-Import.
2. Prüfen Sie, ob **Go to Segment** für diesen Import angezeigt wird.
3. Wenn **Go to Segment** angezeigt wird, ist Ihre CSV-Datei im Segment-Filter `Updated/Imported from CSV` verfügbar.
4. Wenn **Go to Segment** nicht angezeigt wird, wurde die Targeting-Verfügbarkeit für diesen Import nicht aktiviert.

Sie können die Targeting-Verfügbarkeit nach Abschluss eines CSV-Uploads nicht mehr aktivieren. Um diese CSV-Datei als Segment-Filter zu verwenden, laden Sie die Datei erneut hoch und wählen Sie in [Schritt 6: Targeting-Einstellungen wählen](#step-6-choose-targeting-preferences) die Option **Create targeting filter** oder **Create targeting filter and add to new segment**.

Wenn Ihr Ziel darin besteht, ein Segment zu erstellen, ohne Profildaten zu aktualisieren, laden Sie eine CSV-Datei hoch, die nur Bezeichnerspalten enthält (z. B. `external_id` oder Alias-Bezeichnerspalten), und wählen Sie dann **Create targeting filter and add to new segment**.

### Probleme mit der Dateiformatierung {#file-formatting-issues}

#### Fehlerhafte Zeile {#malformed-row}

Wenn Ihr Upload mit Fehlern abgeschlossen wurde, kann es eine fehlerhafte Zeile in Ihrer CSV-Datei geben.

Für einen korrekten Datenimport muss eine Kopfzeile vorhanden sein. Jede Zeile muss die gleiche Anzahl an Zellen wie die Kopfzeile haben. Zeilen mit mehr oder weniger Werten als die Kopfzeile werden vom Import ausgeschlossen. Kommas in einem Wert werden als Trennzeichen interpretiert und können zu diesem Fehler führen.

Außerdem müssen alle Daten UTF-8-kodiert sein. Wenn die Datei mit einer veralteten Kodierung gespeichert wurde (z. B. einige Excel-Standardeinstellungen), können Sonderzeichen und URLs in Zellen beschädigt werden und als Fragezeichen (`?`) in Braze oder in gesendeten Nachrichten erscheinen.

Wenn Ihre CSV-Datei leere Zeilen enthält und weniger Zeilen importiert als die Gesamtzahl der Zeilen in der CSV-Datei, muss dies nicht unbedingt auf ein Problem mit dem Import hinweisen, da die leeren Zeilen nicht importiert werden müssen. Überprüfen Sie die Anzahl der korrekt importierten Zeilen und stellen Sie sicher, dass sie mit der Anzahl der Nutzer:innen übereinstimmt, die Sie importieren möchten.

#### Fehlende Zeile {#missing-row}

Es gibt einige Gründe, warum die Anzahl der importierten Nutzer:innen nicht mit der Gesamtzahl der Zeilen in Ihrer CSV-Datei übereinstimmen kann:

| Problem | Lösung |
|---|---|
| Doppelte externe IDs, Nutzer-Aliase, Braze-IDs, E-Mail-Adressen oder Telefonnummern | Wenn es doppelte Spalten für externe IDs gibt, kann dies zu fehlerhaften oder nicht importierten Zeilen führen, auch wenn die Zeilen korrekt formatiert sind. In einigen Fällen wird kein spezifischer Fehler gemeldet. Prüfen Sie auf Duplikate und entfernen Sie diese vor dem erneuten Hochladen. |
| Zeichen mit Akzenten | Ihre CSV-Datei kann Namen oder Attribute mit Akzenten enthalten. Stellen Sie sicher, dass die Datei UTF-8-kodiert ist, um Importprobleme zu vermeiden. |
| Braze-ID gehört zu einer/einem verwaisten Nutzer:in | Wenn eine:r Nutzer:in mit einer/einem anderen zusammengeführt wurde und Braze die Braze-ID nicht dem verbleibenden Profil zuordnen kann, wird die Zeile nicht importiert. |
| Leere Zeile | Leere Zeilen in der CSV-Datei können Fehler bei fehlerhaften Daten verursachen. Prüfen Sie dies mit einem Texteditor, nicht mit Excel oder Sheets. |
| Nicht-escapte oder unausgeglichene doppelte Anführungszeichen (`"`) | Doppelte Anführungszeichen umschließen String-Werte, die Kommas enthalten. Wenn ein Wert selbst ein doppeltes Anführungszeichen enthält, escapen Sie es durch Verdopplung (`""`). Nicht-escapte oder unausgeglichene doppelte Anführungszeichen verursachen eine fehlerhafte Zeile. |
| Inkonsistente Zeilenumbrüche | Gemischte Zeilenumbrüche (z. B. `\n` und `\r\n`) können dazu führen, dass die erste Datenzeile als Teil der Kopfzeile behandelt wird. Verwenden Sie einen Hex- oder erweiterten Texteditor, um dies zu prüfen und zu beheben. |
| Falsch kodierte Datei | Auch wenn Akzente zulässig sind, muss die Datei UTF-8-kodiert sein. Andere Kodierungen funktionieren möglicherweise teilweise, werden aber nicht vollständig unterstützt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlende Zeile" }

#### String-Anführungszeichen {#string-quotation}

Werte, die in einfache (`''`) oder doppelte (`""`) Anführungszeichen eingeschlossen sind, werden beim Import als Strings gelesen.

#### Falsch formatierte Datumsangaben {#incorrectly-formatted-dates}

Datumsangaben, die nicht im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format vorliegen, werden beim Import nicht als `datetimes` gelesen.

### Probleme mit der Datenstruktur {#data-structure-issues}

#### Ungültige E-Mail-Adressen {#invalid-email-addresses}

Wenn Ihr Upload mit Fehlern abgeschlossen wurde, kann es eine oder mehrere ungültige verschlüsselte E-Mail-Adressen geben. Bestätigen Sie, dass alle E-Mail-Adressen korrekt verschlüsselt sind, bevor Sie sie in Braze importieren.

- **Beim [Aktualisieren oder Importieren von E-Mail-Adressen]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/#step-3-import-and-update-users)** in Braze verwenden Sie den gehashten E-Mail-Wert überall dort, wo eine E-Mail enthalten ist. Diese gehashten E-Mail-Werte werden von Ihrem internen Team bereitgestellt.
- **Beim Erstellen neuer Nutzer:innen** müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail-Wert der/des Nutzers/Nutzerin hinzufügen. Andernfalls erstellt Braze die/den Nutzer:in nicht. Ebenso müssen Sie, wenn Sie einer/einem bestehenden Nutzer:in ohne E-Mail eine E-Mail-Adresse hinzufügen, `email_encrypted` hinzufügen. Andernfalls aktualisiert Braze die/den Nutzer:in nicht.

#### Daten als angepasstes Attribut importiert {#data-imported-as-custom-attribute}

Wenn ein Standard-Nutzerdatum (wie `email` oder `first_name`) als angepasstes Attribut importiert wird, überprüfen Sie die Groß-/Kleinschreibung und die Abstände in Ihrer CSV-Datei. Zum Beispiel wird `First_name` als angepasstes Attribut importiert, während `first_name` korrekt in das Feld „Vorname“ im Nutzerprofil importiert wird.

#### Datentyp eines angepassten Attributs ändern {#change-a-custom-attributes-data-type}

Wenn Sie den Datentyp eines bestehenden angepassten Attributs ändern müssen (z. B. von String zu Boolescher Wert), aktualisieren Sie den Datentyp auf der Seite [**Angepasste Attribute**]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/) im Dashboard, bevor Sie Ihre CSV-Datei importieren. Wenn der Datentyp in Ihrer CSV-Datei nicht mit dem aktuell definierten Datentyp des Attributs übereinstimmt, schlägt der Import mit einem Fehler fehl.

#### Mehrere Datentypen {#multiple-data-types}

Braze erwartet, dass jeder Wert in einer Spalte denselben Datentyp hat. Werte, die nicht dem Datentyp ihres Attributs entsprechen, verursachen Fehler bei der Segmentierung.

Außerdem kann das Beginnen eines Zahlenattributs mit einer Null Probleme verursachen, da Zahlen, die mit Nullen beginnen, als Strings betrachtet werden. Wenn Braze diesen String konvertiert, kann er als Oktalwert behandelt werden (der Ziffern von null bis sieben verwendet), was bedeutet, dass er in seinen entsprechenden Dezimalwert umgewandelt wird. Wenn der Wert in der CSV-Datei beispielsweise 0130 ist, zeigt das Braze-Profil 88 an. Um dieses Problem zu vermeiden, verwenden Sie Attribute mit String-Datentypen. Dieser Datentyp ist jedoch nicht im Segmentierungs-Zahlenvergleich verfügbar.

#### Standardattributtypen {#default-attribute-types}

Einige Standardattribute akzeptieren möglicherweise nur bestimmte Werte als gültig für Nutzeraktualisierungen. Hinweise finden Sie unter [CSV-Datei erstellen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/).

Nachgestellte Leerzeichen und Unterschiede in der Groß-/Kleinschreibung können dazu führen, dass ein Wert als ungültig interpretiert wird. In der folgenden CSV-Datei wird beispielsweise nur die/der Nutzer:in in der ersten Zeile (`brazetest1`) erfolgreich mit dem E-Mail- und Push-Status aktualisiert, da die akzeptierten Werte `unsubscribed`, `subscribed` und `opted_in` sind.

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### „CSV-Datei auswählen“ funktioniert nicht {#select-csv-file-is-not-working}

Es gibt mehrere Gründe, warum der Button **Select CSV File** möglicherweise nicht funktioniert:

| Problem | Lösung |
|---|---|
| Pop-up-Blocker | Dies kann verhindern, dass die Seite angezeigt wird. Bestätigen Sie, dass Ihr Browser Pop-ups auf der Braze-Dashboard-Website zulässt. |
| Veralteter Browser | Stellen Sie sicher, dass Ihr Browser auf dem neuesten Stand ist; falls nicht, aktualisieren Sie ihn auf die neueste Version. |
| Hintergrundprozesse | Schließen Sie alle Browser-Instanzen und starten Sie dann Ihren Computer neu. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="„CSV-Datei auswählen“ funktioniert nicht" }