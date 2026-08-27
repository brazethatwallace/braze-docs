---
nav_title: Nutzerdaten und CSV-Events importieren
article_title: Nutzerdaten und CSV-Events importieren
permalink: "/csv_events/"
description: "Dieser Referenzartikel beschreibt, wie Sie Nutzerdaten importieren und wie Sie angepasste Events mithilfe von CSV-Dateien importieren."
page_type: reference
---

# Nutzerdaten importieren (CSV-Events – Early Access) {#importing-user-data-csv-events-early-access}

> Braze bietet verschiedene Möglichkeiten, Nutzerdaten in die Plattform zu importieren: SDKs, APIs, Cloud-Datenaufnahme, Partnerintegrationen und CSV-Dateien. Dieser Artikel enthält detaillierte Anleitungen zum Import von Nutzerdaten, einschließlich des [Imports angepasster Events über CSV-Dateien (Early Access)](#importing-custom-events).

{% alert important %}
Senden Sie keine rechtlich vorgeschriebenen Transaktions-E-Mails an SMS-Gateways, da eine hohe Wahrscheinlichkeit besteht, dass diese E-Mails nicht zugestellt werden.

Obwohl E-Mails, die Sie über eine Telefonnummer und die E-Mail-zu-SMS-Gateway-Domain des Anbieters (MM3) senden, dazu führen können, dass die E-Mail als SMS (Textnachricht) empfangen wird, unterstützen einige E-Mail-Anbieter dieses Verhalten nicht. Wenn Sie beispielsweise eine E-Mail an eine T-Mobile-Telefonnummer senden (z. B. „9999999999@tmomail.net“), würde Ihre SMS-Nachricht an die Person gesendet, die diese Telefonnummer im T-Mobile-Netz besitzt.

Auch wenn diese E-Mails möglicherweise nicht an das SMS-Gateway zugestellt werden, zählen sie dennoch für Ihre E-Mail-Abrechnung. Um das Senden von E-Mails an nicht unterstützte Gateways zu vermeiden, überprüfen Sie die [Liste der nicht unterstützten Gateway-Domainnamen](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}


Beachten Sie vor dem Fortfahren, dass Braze HTML-Daten beim Import nicht bereinigt (validiert oder korrekt formatiert). Das bedeutet, dass Script-Tags aus allen Importdaten entfernt werden müssen, die für die Web-Personalisierung vorgesehen sind.

## REST API

Sie können den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden, um angepasste Events, Nutzerattribute und Käufe für Nutzer:innen aufzuzeichnen.

## CSV-Import

Sie können Nutzerprofile über CSV-Dateien hochladen und aktualisieren, indem Sie zu **Audience** > **Import Users** navigieren.

Der Import von Nutzerdaten mithilfe von CSV-Dateien unterstützt das Erfassen und Aktualisieren von Nutzerattributen wie Vorname und E-Mail sowie angepasste Attribute wie Schuhgröße. Sie können eine CSV-Datei importieren, indem Sie einen von zwei eindeutigen Nutzerbezeichnern angeben: eine `external_id` oder einen Nutzer-Alias.

{% alert important %}
Der Nutzerimport unterstützt auch das Erfassen und Aktualisieren angepasster Events von Nutzer:innen. Ähnlich wie bei Nutzerattributen können Sie mit einer `external_id`, `braze_id` oder mit `user_alias_name` und `user_alias_label` importieren. Weitere Details finden Sie unter [Angepasste Events importieren](#importing-custom-events).
{% endalert %}

{% alert note %}
Wenn Sie eine Mischung aus Nutzer:innen mit einer `external_id` und Nutzer:innen ohne hochladen, müssen Sie für jeden Import eine separate CSV-Datei erstellen. Eine CSV-Datei kann nicht sowohl `external_ids` als auch Nutzer-Aliasse enthalten.
{% endalert %}

### Import mit externer ID {#importing-with-external-id}

Beim Import Ihrer Kundendaten müssen Sie den eindeutigen Bezeichner jeder Kund:in angeben, auch bekannt als `external_id`. Bevor Sie mit Ihrem CSV-Import beginnen, ist es wichtig, von Ihrem Entwicklerteam zu erfahren, wie Nutzer:innen in Braze identifiziert werden. Typischerweise handelt es sich um eine interne Datenbank-ID. Diese sollte mit der Art übereinstimmen, wie Nutzer:innen vom Braze SDK auf Mobilgeräten und im Internet identifiziert werden, und ist so konzipiert, dass jede Kund:in ein einzelnes Nutzerprofil in Braze über alle Geräte hinweg hat. Lesen Sie mehr über den [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle) von Braze.

Wenn Sie in Ihrem Import eine `external_id` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit derselben `external_id` oder erstellt eine:n neu identifizierte:n Nutzer:in mit dieser `external_id`, falls keine:r gefunden wird.

- **Download:** [CSV-Attribut-Import-Template][import_template]
- **Download:** [CSV-Event-Import-Template][events_template]

### Import mit Nutzer-Alias {#importing-with-user-alias}

Um Nutzer:innen anzusprechen, die keine `external_id` haben, können Sie eine Liste von Nutzer:innen mit Nutzer-Aliassen importieren. Ein Alias dient als alternativer eindeutiger Nutzerbezeichner und kann hilfreich sein, wenn Sie versuchen, anonyme Nutzer:innen zu erreichen, die sich nicht registriert oder kein Konto in Ihrer App erstellt haben.

Wenn Sie Nutzerprofile hochladen oder aktualisieren, die nur Aliasse haben, müssen die folgenden zwei Spalten in Ihrer CSV-Datei enthalten sein:

- `user_alias_name`: Ein eindeutiger Nutzerbezeichner; eine Alternative zur `external_id`
- `user_alias_label`: Ein gemeinsames Label, mit dem Nutzer-Aliasse gruppiert werden

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Wenn Sie in Ihrem Import sowohl einen `user_alias_name` als auch ein `user_alias_label` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `user_alias_name` und `user_alias_label`. Falls keine:r gefunden wird, erstellt Braze eine:n neu identifizierte:n Nutzer:in mit diesem `user_alias_name`.

{% alert important %}
Sie können keinen CSV-Import verwenden, um eine:n vorhandene:n Nutzer:in mit einem `user_alias_name` zu aktualisieren, wenn diese:r bereits eine `external_id` hat. Stattdessen wird ein neues Nutzerprofil mit dem zugehörigen `user_alias_name` erstellt. Um eine:n Nutzer:in, die:der nur einen Alias hat, mit einer `external_id` zu verknüpfen, verwenden Sie den [Endpunkt „Nutzer:innen identifizieren“]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).
{% endalert %}

- **Download:** [CSV-Alias-Attribut-Import-Template][template_alias_attributes]
- **Download:** [CSV-Alias-Event-Import-Template][template_alias_events]

### Import mit Braze-ID {#importing-with-braze-id}

Um vorhandene Nutzerprofile in Braze über einen internen Braze-ID-Wert anstelle einer `external_id` oder eines `user_alias_name` und `user_alias_label` zu aktualisieren, geben Sie `braze_id` als Spaltenüberschrift an.

Dies kann hilfreich sein, wenn Sie Nutzerdaten aus Braze über unsere CSV-Exportoption innerhalb der Segmentierung exportiert haben und diesen vorhandenen Nutzer:innen ein neues angepasstes Attribut hinzufügen möchten.

{% alert important %}
Sie können keinen CSV-Import verwenden, um eine:n neue:n Nutzer:in mit `braze_id` zu erstellen. Diese Methode kann nur zum Aktualisieren bereits vorhandener Nutzer:innen innerhalb der Braze-Plattform verwendet werden.
{% endalert %}

{% alert tip %}
Der `braze_id`-Wert kann in CSV-Exporten aus dem Braze-Dashboard als `Appboy ID` bezeichnet sein. Diese ID ist identisch mit der `braze_id` einer Nutzer:in, sodass Sie diese Spalte beim erneuten Import der CSV-Datei in `braze_id` umbenennen können.
{% endalert %}

### Standardattribute importieren {#importing-default-attributes}

Um Standardattribute für Nutzer:innen zu importieren, navigieren Sie zu **Import Users** > **Attributes**. Standardmäßige Nutzerattribute sind reservierte Schlüssel in Braze. Zum Beispiel `first_name` oder `email`. Angepasste Attribute sind individuell für Ihr Unternehmen. Beispielsweise könnte eine Reisebuchungs-App ein angepasstes Attribut namens `last_destination_searched` haben.

{% alert important %}
Beim Import von Kundendaten als Attribute müssen die verwendeten Spaltenüberschriften exakt der Schreibweise und Groß-/Kleinschreibung der Standardnutzerattribute entsprechen. Andernfalls erstellt Braze automatisch ein angepasstes Attribut im Profil dieser Nutzer:in.
{% endalert %}

#### Standard-Nutzerdaten-Spaltenüberschriften {#default-user-data-column-headers}

| NUTZERPROFIL-FELD | DATENTYP | INFORMATION | ERFORDERLICH |
|---|---|---|---|
| `external_id` | String | Ein eindeutiger Nutzerbezeichner für Ihre Kund:in. | Ja, siehe den [folgenden Hinweis](#about-external-ids). |
| `user_alias_name` | String | Ein eindeutiger Nutzerbezeichner für anonyme Nutzer:innen. Eine Alternative zur `external_id`. | Nein, siehe den [folgenden Hinweis](#about-external-ids). |
| `user_alias_label` | String | Ein gemeinsames Label, mit dem Nutzer-Aliasse gruppiert werden. | Ja, wenn `user_alias_name` verwendet wird. |
| `first_name` | String | Der Vorname Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `Jane`). | Nein |
| `last_name` | String | Der Nachname Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `Doe`). | Nein |
| `email` | String | Die E-Mail-Adresse Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `jane.doe@braze.com`). | Nein |
| `country` | String | Ländercodes müssen im ISO-3166-1 Alpha-2-Standard an Braze übergeben werden (z. B. `GB`). | Nein |
| `dob` | String | Muss im Format „YYYY-MM-DD“ übergeben werden (z. B. `1980-12-21`). Dadurch wird das Geburtsdatum Ihrer Nutzer:innen importiert und Sie können Nutzer:innen ansprechen, deren Geburtstag „heute“ ist. | Nein |
| `gender` | String | „M“, „F“, „O“ (andere), „N“ (nicht zutreffend), „P“ (keine Angabe erwünscht) oder nil (unbekannt). | Nein |
| `home_city` | String | Der Wohnort Ihrer Nutzer:innen, wie von ihnen angegeben (z. B. `London`). | Nein |
| `language` | String | Die Sprache muss im ISO-639-1-Standard an Braze übergeben werden (z. B. `en`). <br>Siehe unsere [Liste der akzeptierten Sprachen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes). | Nein |
| `phone` | String | Eine Telefonnummer, wie von Ihren Nutzer:innen angegeben, im `E.164`-Format (z. B. `+442071838750`). <br> Siehe [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers) für Formatierungshinweise. | Nein |
| `email_open_tracking_disabled` | Boolean | true oder false akzeptiert. Auf true setzen, um das Open-Tracking-Pixel nicht mehr zu allen zukünftigen E-Mails hinzuzufügen, die an diese:n Nutzer:in gesendet werden. | Nein |
| `email_click_tracking_disabled` | Boolean | true oder false akzeptiert. Auf true setzen, um das Klick-Tracking für alle Links in zukünftigen E-Mails zu deaktivieren, die an diese:n Nutzer:in gesendet werden. | Nein |
| `email_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von E-Mail-Nachrichten registriert), `unsubscribed` (explizit vom Empfang von E-Mail-Nachrichten abgemeldet) und `subscribed` (weder angemeldet noch abgemeldet). | Nein |
| `push_subscribe` | String | Verfügbare Werte sind `opted_in` (explizit für den Empfang von Push-Nachrichten registriert), `unsubscribed` (explizit vom Empfang von Push-Nachrichten abgemeldet) und `subscribed` (weder angemeldet noch abgemeldet). | Nein |
| `time_zone` | String | Die Zeitzone muss im selben Format wie die IANA-Zeitzonen-Datenbank an Braze übergeben werden (z. B. `America/New_York` oder `Eastern Time (US & Canada)`). | Nein |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Kann in einem der folgenden ISO-8601-Formate übergeben werden: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (z. B. 2019-11-20T18:38:57) </li> </ul> {:/} | Nein |
| `subscription_group_id` | String | Die `id` Ihrer Abo-Gruppe. Dieser Bezeichner ist auf der Seite der Abo-Gruppen in Ihrem Dashboard zu finden. | Nein |
| `subscription_state` | String | Der Abo-Status für die durch `subscription_group_id` angegebene Abo-Gruppe. Zulässige Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe). | Nein, aber dringend empfohlen, wenn `subscription_group_id` verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### Über externe IDs {#about-external-ids}

Obwohl `external_id` nicht zwingend erforderlich ist, **müssen** Sie eines dieser Felder angeben:
- `external_id`: Ein eindeutiger Nutzerbezeichner für Ihre Kund:in, **oder**
- `braze_id`: Ein eindeutiger, von Braze zugewiesener Nutzerbezeichner für vorhandene Braze-Nutzer:innen, **oder**
- `user_alias_name` und `user_alias_label`: Ein eindeutiger Nutzerbezeichner für eine:n anonyme:n Nutzer:in

### Angepasste Attribute importieren {#importing-custom-attributes}

Sie können angepasste Attribute für Nutzer:innen importieren, indem Sie zu **Import Users** > **Attributes** navigieren. Alle Überschriften, die nicht exakt mit Standardattributen übereinstimmen, erstellen ein angepasstes Attribut in Braze.

Die folgenden Datentypen werden beim Nutzerimport akzeptiert:

| Datentyp | Beschreibung |
|-----------|-------------|
| Datetime | Muss im ISO-8601-Format gespeichert werden |
| Boolean | TRUE oder FALSE |
| Number | Ganzzahl oder Gleitkommazahl ohne Leerzeichen oder Kommas; Gleitkommazahlen müssen einen Punkt (.) als Dezimaltrennzeichen verwenden |
| String | Kann Kommas enthalten, solange der Spaltenwert in doppelte Anführungszeichen eingeschlossen ist |
| Leer | Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und Sie müssen nicht alle vorhandenen Nutzerattribute in Ihre CSV-Datei aufnehmen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Arrays und Push-Token werden beim Nutzerimport nicht unterstützt. Insbesondere bei Arrays werden Kommas in Ihrer CSV-Datei als Spaltentrennzeichen interpretiert, sodass Kommas in Werten zu Fehlern beim Parsen der Datei führen. <br>Um solche Werte hochzuladen, verwenden Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion).
{% endalert %}

### Abo-Gruppenstatus aktualisieren {#updating-subscription-group-status}

Sie können Nutzer:innen über den Nutzerimport zu E-Mail- oder SMS-Abo-Gruppen hinzufügen. Dies ist besonders für SMS nützlich, da Nutzer:innen in eine SMS-Abo-Gruppe aufgenommen werden müssen, um über den SMS-Kanal kontaktiert werden zu können. Weitere Informationen finden Sie unter [SMS-Abo-Gruppen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#subscription-group-mms-enablement).

Wenn Sie den Abo-Gruppenstatus aktualisieren, müssen die folgenden zwei Spalten in Ihrer CSV-Datei enthalten sein:

- `subscription_group_id`: Die `id` der [Abo-Gruppe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups).
- `subscription_state`: Verfügbare Werte sind `unsubscribed` (nicht in der Abo-Gruppe) oder `subscribed` (in der Abo-Gruppe).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Abo-Gruppenstatus aktualisieren">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
Pro Zeile im Nutzerimport kann nur eine einzige `subscription_group_id` festgelegt werden. Verschiedene Zeilen können unterschiedliche `subscription_group_id`-Werte haben. Wenn Sie jedoch dieselben Nutzer:innen in mehrere Abo-Gruppen aufnehmen möchten, müssen Sie mehrere Importe durchführen.
{% endalert %}

### Angepasste Events importieren (Early Access) {#importing-custom-events}

{% alert important %}
Der Import angepasster Events befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Teilnahme am Early Access interessiert sind.
{% endalert %}

Um angepasste Events für Ihre Nutzer:innen zu importieren, navigieren Sie zu **Import Users** > **Events**.

Angepasste Events sind individuell für Ihr Unternehmen. Beispielsweise könnte eine Streaming-App ein angepasstes Event namens rented_movie haben. Ihre CSV-Datei muss Spaltenüberschriften für Folgendes enthalten:

- Eines der folgenden:
  - `external_id`, **oder**
  - `braze_id`, **oder**
  - `user_alias_name` und `user_alias_label`
- Name
- Time

Angepasste Events können Event-Eigenschaften haben. Beispielsweise könnte das angepasste Event rented_movie die Eigenschaften title und genre haben. Diese Event-Eigenschaften sollten eine Spaltenüberschrift im Format `<event_name>.properties.<property name>` haben. Ein Beispiel ist `rented_movie.properties.title`.

| NUTZERPROFIL-FELD                       | DATENTYP  | INFORMATION                                                                                                                                                                                                             | ERFORDERLICH                                                                                    |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | String    | Ein eindeutiger Nutzerbezeichner für Ihre:n Nutzer:in.                                                                                                                                                                  | Ja, eines von `external_id`, `braze_id` oder `user_alias_name` und `user_alias_label` ist erforderlich. |
| `braze_id`                              | String    | Ein von Braze zugewiesener Bezeichner für Ihre:n Nutzer:in.                                                                                                                                                             | Ja, eines von `external_id`, `braze_id` oder `user_alias_name` und `user_alias_label` ist erforderlich. |
| `user_alias_name`                       | String    | Ein eindeutiger Nutzerbezeichner für anonyme Nutzer:innen. Eine Alternative zur external_id.                                                                                                                            | Ja, eines von `external_id`, `braze_id` oder `user_alias_name` und `user_alias_label` ist erforderlich. |
| `user_alias_label`                      | String    | Ein gemeinsames Label, mit dem Nutzer-Aliasse gruppiert werden.                                                                                                                                                         | Ja, eines von `external_id`, `braze_id` oder `user_alias_name` und `user_alias_label` ist erforderlich. |
| `name`                                  | String    | Ein angepasstes Event Ihrer Nutzer:innen.                                                                                                                                                                               | Ja                                                                                              |
| `time`                                  | String    | Die Uhrzeit des Events. Kann in einem der folgenden ISO-8601-Formate übergeben werden: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (z. B. 2019-11-20T18:38:57) </li> </ul> {:/} | Ja                                                                                              |
| `<event name>.properties.<property name>` | Mehrere   | Eine Event-Eigenschaft, die mit einem angepassten Event verknüpft ist. Ein Beispiel ist `rented_movie.properties.title`                                                                                                 | Nein                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Obwohl external_id selbst nicht zwingend erforderlich ist, müssen Sie eines der folgenden Felder angeben: <br>- `external_id`: Ein eindeutiger Nutzerbezeichner für Ihre Kund:in <br>- `braze_id`: Ein eindeutiger, von Braze zugewiesener Nutzerbezeichner für vorhandene Braze-Nutzer:innen <br>- `user_alias_name`: Ein eindeutiger Nutzerbezeichner für eine:n anonyme:n Nutzer:in
{% endalert %}

#### CSV-Größe {#csv-size}

Braze akzeptiert Nutzerdaten im Standard-CSV-Format aus Dateien mit einer Größe von bis zu 500 MB. Um eines unserer CSV-Datei-Templates herunterzuladen, lesen Sie die Abschnitte [Import mit externer ID](#importing-with-external-id) oder [Import mit Nutzer-Alias](#importing-with-user-alias).

#### Überlegungen zu Datenpunkten {#data-point-considerations}

Jedes über CSV importierte Kundendatum überschreibt den vorhandenen Wert in Nutzerprofilen und zählt als Datenpunkt, mit Ausnahme von externen IDs und leeren Werten.

- Über CSV-Import hochgeladene externe IDs verbrauchen keine Datenpunkte. Wenn Sie eine CSV-Datei hochladen, um vorhandene Braze-Nutzer:innen zu segmentieren, indem Sie nur externe IDs hochladen, ist dies ohne Verbrauch von Datenpunkten möglich. Wenn Sie in Ihrem Import zusätzliche Daten wie die E-Mail-Adresse oder Telefonnummer hinzufügen würden, würde dies vorhandene Nutzerdaten überschreiben und Ihre Datenpunkte verbrauchen.
    - CSV-Importe zu Segmentierungszwecken (Importe, bei denen `external_id`, `braze_id` oder `user_alias_name` das einzige Feld ist) verbrauchen keine Datenpunkte.
- Leere Werte überschreiben keine vorhandenen Werte im Nutzerprofil, und Sie müssen nicht alle vorhandenen Nutzerattribute oder angepassten Events in Ihre CSV-Datei aufnehmen.
- Das Aktualisieren von `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` wird nicht auf den Datenpunktverbrauch angerechnet.

{% alert important %}
Das Festlegen von Sprache oder Land für eine:n Nutzer:in über CSV-Import oder API verhindert, dass Braze diese Informationen automatisch über das SDK erfasst.
{% endalert %}

## CSV-Import {#importing-a-csv}

So importieren Sie Ihre CSV-Datei:
1. Gehen Sie zu **Audience** > **Import Users**.
2. Wählen Sie **Browse Files** aus, wählen Sie die gewünschte Datei und dann **Start import**. Braze lädt Ihre Datei hoch und überprüft die Spaltenüberschriften sowie die Datentypen jeder Spalte.

{% alert important %}
CSV-Importe unterscheiden zwischen Groß- und Kleinschreibung. Das bedeutet, dass Großbuchstaben in CSV-Importen das Feld als angepasstes Attribut statt als Standardattribut schreiben. Zum Beispiel ist „email“ korrekt, aber „Email“ würde als angepasstes Attribut geschrieben.
{% endalert %}

![Die Option „Events“ ist als Typ der zu importierenden Nutzerinformationen ausgewählt.][5]

Nach Abschluss des Uploads können Sie eine Vorschau der Inhalte Ihrer Datei anzeigen. Die Informationen in der Tabelle basieren auf den Werten in den obersten Zeilen Ihrer CSV-Datei.

Sie können den Fortschritt auf der Seite **Import Users** verfolgen, die alle fünf Sekunden aktualisiert wird, oder wenn Sie **Refresh table** auswählen. Sie können den Rest des Braze-Dashboards während des Imports weiterhin nutzen und erhalten Benachrichtigungen, wenn der Import beginnt und endet.

Sie können auch Ihre letzten Importe, deren Dateinamen, CSV-Typ, Anzahl der Zeilen in der Datei, Anzahl der erfolgreich importierten Zeilen, die Gesamtzahl der Zeilen in jeder Datei und den Status jedes Imports einsehen.

Sie können mehr als eine CSV-Datei gleichzeitig importieren. CSV-Importe werden gleichzeitig ausgeführt, was bedeutet, dass die Reihenfolge der Aktualisierungen nicht garantiert seriell ist. Wenn Sie CSV-Importe nacheinander ausführen möchten, sollten Sie warten, bis ein CSV-Import abgeschlossen ist, bevor Sie einen zweiten hochladen.

Wenn der Importprozess auf einen Fehler stößt, erscheint ein Warnsymbol neben der Gesamtzahl der Zeilen in der Datei. Sie können mit dem Mauszeiger über das Symbol fahren, um Details darüber zu erfahren, warum bestimmte Zeilen fehlgeschlagen sind. Nach Abschluss des Imports werden alle Daten zu bestehenden Profilen hinzugefügt oder neue Profile erstellt.

![CSV-Datei-Upload mit Fehlern aufgrund gemischter Datentypen in einer einzelnen Spalte abgeschlossen][4]{: style="max-width:70%"}

### Hinweise {#considerations}

Wenn Braze beim Upload in den obersten Zeilen Ihrer Datei etwas Fehlerhaftes bemerkt, werden diese Fehler zusammen mit der Zusammenfassung angezeigt. Wenn Ihre Datei beispielsweise eine fehlerhafte Zeile enthält, wird dieser Fehler in der Vorschau beim Import der Datei angezeigt. Obwohl eine Datei mit Fehlern importiert werden kann, wird empfohlen, solche Fehler in Ihrer Datei zu beheben, bevor Sie mit dem Import fortfahren.

Darüber hinaus ist es wichtig, die gesamte CSV-Datei vor dem Upload zu prüfen, da Braze für die Vorschau nicht jede Zeile der Eingabedatei scannt. Das bedeutet, dass Fehler existieren können, die Braze beim Erstellen dieser Vorschau nicht erkennt.

Fehlerhafte Zeilen und Zeilen ohne externe ID werden nicht importiert. Alle anderen Fehler können importiert werden, können aber das Filtern beim Erstellen eines Segments beeinträchtigen. Weitere Informationen finden Sie im Abschnitt [Fehlerbehebung](#troubleshooting).

{% alert warning %}
Fehler basieren ausschließlich auf dem Datentyp und der Dateistruktur. Beispielsweise würde eine schlecht formatierte E-Mail-Adresse trotzdem importiert, da sie weiterhin als String geparst werden kann.
{% endalert %}

### Lambda-Nutzer-CSV-Import {#lambda-user-csv-import}

Sie können unser serverloses S3-Lambda-CSV-Import-Skript verwenden, um Nutzerattribute in die Plattform hochzuladen. Diese Lösung funktioniert als CSV-Uploader, bei dem Sie Ihre CSV-Dateien in einen S3-Bucket ablegen und die Skripte sie über unsere API hochladen.

Die geschätzte Ausführungszeit für eine Datei mit einer Million Zeilen beträgt etwa fünf Minuten. Weitere Informationen finden Sie unter [Nutzerattribut-CSV-zu-Braze-Import]({{site.baseurl}}/user_csv_lambda).

## Segmentierung {#segmenting}

Der Nutzerimport erstellt und aktualisiert Nutzerprofile und kann auch zur Erstellung von Segmenten verwendet werden. Um ein Segment zu erstellen, wählen Sie **Automatically generate a segment from the users who are imported from this CSV** aus, bevor Sie den Import starten.

Sie können den Namen des Segments festlegen oder den Standardnamen übernehmen, der dem Namen Ihrer Datei entspricht. Dateien, die zur Erstellung eines Segments verwendet wurden, enthalten nach Abschluss des Imports einen Link zur Anzeige des Segments.

Der Filter, der zur Erstellung des Segments verwendet wird, wählt Nutzer:innen aus, die in einem ausgewählten Import erstellt oder aktualisiert wurden, und ist zusammen mit allen anderen Filtern auf der Seite zum Bearbeiten des Segments verfügbar.

## Fehlerbehebung {#troubleshooting}

### Fehlende Zeilen {#missing-rows}

Es gibt einige Gründe, warum die Anzahl der importierten Nutzer:innen möglicherweise nicht mit der Gesamtzahl der Zeilen in Ihrer CSV-Datei übereinstimmt:

- **Doppelte externe IDs:** Wenn es doppelte externe ID-Spalten gibt, kann dies zu fehlerhaften oder nicht importierten Zeilen führen, selbst wenn die Zeilen korrekt formatiert sind. In einigen Fällen wird möglicherweise kein spezifischer Fehler gemeldet. Überprüfen Sie, ob es doppelte externe IDs in Ihrer CSV-Datei gibt. Falls ja, entfernen Sie die Duplikate und versuchen Sie den Upload erneut.
- **Zeichen mit Akzenten:** Ihre CSV-Datei kann Namen oder Attribute enthalten, die Akzente beinhalten. Stellen Sie sicher, dass Ihre Datei UTF-8-kodiert ist, um Probleme zu vermeiden.

### Fehlerhafte Zeile {#malformed-row}

Sie müssen eine Kopfzeile in Ihre CSV-Datei aufnehmen, um Ihre Daten korrekt zu importieren. Jede Zeile muss die gleiche Anzahl von Zellen wie die Kopfzeile haben. Zeilen mit mehr oder weniger Werten als die Kopfzeile werden vom Import ausgeschlossen. Kommas in einem Wert werden als Trennzeichen interpretiert und können zu diesem Fehler führen. Außerdem müssen alle Daten UTF-8-kodiert sein.

Wenn Ihre CSV-Datei leere Zeilen enthält und weniger Zeilen importiert als die Gesamtzahl der Zeilen in der CSV-Datei, muss dies nicht unbedingt auf ein Problem mit dem Import hindeuten, da die leeren Zeilen nicht importiert werden müssen. Überprüfen Sie die Anzahl der korrekt importierten Zeilen und stellen Sie sicher, dass sie mit der Anzahl der Nutzer:innen übereinstimmt, die Sie importieren möchten.

### Mehrere Datentypen {#multiple-data-types}

Braze erwartet, dass jeder Wert in einer Spalte denselben Datentyp hat. Werte, die nicht mit dem Datentyp ihres Attributs übereinstimmen, verursachen Fehler bei der Segmentierung.

### Falsch formatierte Daten {#incorrectly-formatted-dates}

Daten, die nicht im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format vorliegen, werden beim Import nicht als Datetime-Werte gelesen.

### String-Anführungszeichen {#string-quotation}

Werte, die in einfache ('') oder doppelte ("") Anführungszeichen eingeschlossen sind, werden beim Import als Strings gelesen.

### Als angepasstes Attribut importierte Daten {#data-imported-as-custom-attribute}

Wenn Sie feststellen, dass Standard-Nutzerdaten (zum Beispiel `email` oder `first_name`) als angepasstes Attribut importiert werden, überprüfen Sie die Groß-/Kleinschreibung und die Abstände in Ihrer CSV-Datei. Zum Beispiel würde `First_name` als angepasstes Attribut importiert, während `first_name` korrekt in das Feld „Vorname“ im Profil einer:eines Nutzerin:Nutzers importiert würde.

[import_template]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/unlisted_docs/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/unlisted_docs/download_file/braze-events-csv-example-user-alias.csv %}
[3]: {% image_buster /assets/unlisted_docs/img/importcsv5.png %}
[4]: {% image_buster /assets/unlisted_docs/img/importcsv2.png %}
[5]: {% image_buster /assets/unlisted_docs/img/importcsv3.png %}
[7]: {% image_buster /assets/unlisted_docs/img/segment-imported-users.png %}
[8]: {% image_buster /assets/unlisted_docs/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/unlisted_docs/img/subscription_group_import.png %}