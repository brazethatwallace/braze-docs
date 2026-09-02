---
nav_title: Segmentdaten
article_title: Segmentdaten exportieren
page_order: 4
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Segmentdaten nach CSV exportieren, welche Berechtigungen für den Export von Nutzerdaten erforderlich sind, wie Canvas-Schritt-Exporte funktionieren und welche Felder im Export enthalten sind."
---

# Segmentdaten nach CSV exportieren {#export-segment-data-to-csv}

> Auf dieser Seite erfahren Sie, wie Sie einen CSV-Export von Nutzerdaten eines Segments anfragen können und welche Daten im Export enthalten sind.

{% alert note %}
CSV-Exportoptionen werden im Dropdown-Menü **User Data** nur für Unternehmensnutzer:innen angezeigt, die über die [Berechtigung „Nutzerdaten exportieren“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) für diesen Workspace verfügen.
{% endalert %}

Um Segmentdaten in eine CSV-Datei zu exportieren, wählen Sie bei der Bearbeitung eines Segments das Dropdown-Menü **User Data** aus und wählen Sie, ob Sie die Nutzerdaten oder die E-Mail-Adressen für das Segment exportieren möchten.

![Abschnitt „Segmentdetails“ mit dem Dropdown-Menü „User Data“ und Exportoptionen.]({% image_buster /assets/img_archive/csvexport.png %})

Sie können einen CSV-Export auch von der Hauptseite **Segments** aus anfragen, indem Sie das Dropdown-Menü <i class="fas fa-gear" aria-label="Einstellungen"></i> **Settings** für ein Segment auswählen:

![Dropdown-Menü „Settings“ auf der Hauptseite „Segments“.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Um Daten aus all Ihren Nutzerprofilen zu exportieren, erstellen Sie ein Segment ohne Filter und fragen dann einen CSV-Export an.
{% endalert %}

Die CSV-Ausgabe enthält die Daten der einzelnen Nutzerprofile, die zum Zeitpunkt des Exports im Segment erfasst wurden. Sie können jedes Segment exportieren, indem Sie das Zahnradsymbol und den CSV-Export auswählen. Braze erstellt den Bericht im Hintergrund und sendet ihn per E-Mail an die Person, die gerade angemeldet ist.

## Details zum Segment-CSV-Export {#segment-csv-export-details}

{% alert note %}
Dashboard-Nutzer:innen benötigen die Berechtigung **Nutzerdaten exportieren**, um CSV-Exportoptionen verwenden zu können. Ohne diese Berechtigung werden die CSV-Exportoptionen nicht angezeigt.
{% endalert %}

**CSV-Export – E-Mail-Adressen** enthält nur Zeilen für Nutzer:innen im Segment, die eine E-Mail-Adresse haben. Wenn Ihr Segment beispielsweise 100.000 Nutzer:innen umfasst, aber nur 50.000 eine E-Mail-Adresse haben, erzeugt **CSV-Export – E-Mail-Adressen** etwa 50.000 Zeilen. **CSV-Export – Nutzerdaten** exportiert alle Nutzerdaten für das Segment.

{% alert important %}
Aufgrund von Dateigrößenbeschränkungen kann Ihr Export fehlschlagen, wenn die geschätzte Größe Ihres Segments über 500.000 Nutzer:innen liegt. Beachten Sie, dass diese Beschränkung die geschätzte Größe Ihres Segments verwendet und nicht die exakte Berechnung. Weitere Informationen finden Sie unter [Export großer Segmente](#exporting-large-segments).
{% endalert %}

Wenn Sie Ihre [Amazon S3-Zugangsdaten]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration) mit Braze verknüpft haben, wird die CSV-Datei stattdessen in Ihrem S3-Bucket unter dem Schlüssel `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` hochgeladen. Sie müssen im Dashboard angemeldet sein, um auf den per E-Mail zugesendeten Download-Link zugreifen zu können.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Im Export enthaltene Daten {#data-included-in-export}

Die folgenden Daten sind je nach Ihrer Auswahl in Ihrem Export enthalten.

### CSV-Export – Nutzerdaten {#csv-export-user-data}

| Feldname                    | Beschreibung                                             |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | Interne ID (kann nicht geändert werden)                  |
| country                     | Land                                                     |
| created_at                  | Datum und Uhrzeit der Erstellung des Nutzerprofils       |
| created_from                | Methode, mit der das Nutzerprofil erstellt wurde (z. B. REST API, SDK oder CSV-Import) |
| devices                     | Geräteinformationen                                      |
| date_of_birth               | Geburtsdatum                                             |
| email                       | E-Mail-Adresse                                           |
| unsubscribed_from_emails_at | Datum der E-Mail-Abmeldung                               |
| user_id                     | Externe ID                                               |
| first_name                  | Vorname                                                  |
| first_session               | Datum und Uhrzeit der ersten Sitzung                     |
| gender                      | Geschlecht                                               |
| google_ad_ids               | Mit dem/der Nutzer:in verknüpfte Google-Werbe-IDs        |
| city                        | Ort                                                      |
| IDFAs                       | Identifier for Advertising (IDFA)-Werte                  |
| IDFVs                       | Identifier for Vendor (IDFV)-Werte                       |
| language                    | Sprache im ISO-639-1-Standard                            |
| last_app_version_used       | Zuletzt verwendete App-Version                           |
| last_name                   | Nachname                                                 |
| last_session                | Datum und Uhrzeit der letzten Sitzung                    |
| number_of_google_ad_ids     | Anzahl der verknüpften Google-Werbe-IDs                  |
| number_of_IDFAs             | Anzahl der verknüpften IDFAs                             |
| number_of_IDFVs             | Anzahl der verknüpften IDFVs                             |
| number_of_push_tokens       | Anzahl der verknüpften Push-Benachrichtigungs-Token      |
| number_of_roku_ad_ids       | Anzahl der verknüpften Roku-Werbe-IDs                    |
| number_of_windows_ad_ids    | Anzahl der verknüpften Windows-Werbe-IDs                 |
| phone_number                | Telefonnummer                                            |
| opted_into_push_at          | Datum des Push-Opt-ins                                   |
| unsubscribed_from_push_at   | Datum der Push-Abmeldung                                 |
| random_bucket               | Zufällige Bucket-Nummer                                  |
| roku_ad_ids                 | Roku-Werbe-IDs                                           |
| session_count               | Gesamtanzahl der Sitzungen                               |
| timezone                    | Zeitzone der/des Nutzer:in im gleichen Format wie die IANA-Zeitzonendatenbank |
| in_app_purchase_total       | Gesamtbetrag für In-App-Käufe                            |
| user_aliases                | Nutzer-Aliase, falls vorhanden                           |
| windows_ad_ids              | Windows-Werbe-IDs                                        |
| Custom events               | Basierend auf der Auswahl beim Export                    |
| Custom attributes           | Basierend auf der Auswahl beim Export                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV-Export – Nutzerdaten" }

{% alert note %}
Wenn Sie Nutzerdaten aus einem Canvas-Schritt exportieren, enthält die CSV-Datei alle Nutzer:innen, die sich über die gesamte Lebensdauer des Canvas-Schritts in diesem Schritt befanden. Sie können den Export nicht auf einen Datumsbereich oder ein anderes Zeitfenster einschränken. Informationen zur Durchführung dieser Exporte finden Sie unter [Canvas-Daten exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data).
{% endalert %}

### CSV-Export – E-Mail-Adressen {#csv-export-email-addresses}

| Feldname                    | Beschreibung                   |
| --------------------------- | ------------------------------ |
| user_id                     | Externe ID der/des Nutzer:in   |
| first_name                  | Vorname                        |
| last_name                   | Nachname                       |
| email                       | E-Mail                         |
| unsubscribed_from_emails_at | Datum der E-Mail-Abmeldung     |
| opted_in_to_emails_at       | Datum des E-Mail-Opt-ins       |
| user_aliases                | Nutzer-Aliase, falls vorhanden |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV-Export – E-Mail-Adressen" }

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie in unserem Artikel zur [Fehlerbehebung]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% alert note %}
Daten zu Abo-Gruppen sind über Segment-Exporte nicht verfügbar. Um Nutzer:innen nach Abo-Status zu identifizieren, erstellen Sie ein separates Segment basierend auf der Mitgliedschaft in einer Abo-Gruppe und exportieren Sie dieses Segment.
{% endalert %}

## Exportieren großer Segmente {#exporting-large-segments}

Es gibt mehrere Methoden, um ein großes Nutzer:innen-Segment mit mehr als 500.000 Nutzer:innen zu exportieren.

{% tabs %}
{% tab Mehrere Segmente %}

Sie können ein großes Segment in kleinere Segmente aufteilen und dann jedes der kleineren Segmente aus Braze exportieren.

{% endtab %}
{% tab Zufällige Bucket-Nummern %}

Sie können auch [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) verwenden, um Ihre Nutzerbasis in mehrere Segmente aufzuteilen und diese nach dem Export wieder zusammenzuführen. Wenn Sie beispielsweise Ihr Segment in zwei verschiedene Segmente aufteilen müssen, können Sie dies mit den folgenden Filtern tun:
- Segment 1: Zufällige Bucket-Nummer ist kleiner als 5000 (umfasst 0–4999)
- Segment 2: Zufällige Bucket-Nummer ist größer als 4999 (umfasst 5000–9999)

{% endtab %}
{% tab Endpunkte %}

Sie können auch die folgenden Endpunkte nutzen, um Nutzerdaten für ein bestimmtes Segment zu exportieren. Beachten Sie, dass für diese Endpunkte Datenlimits und [Rate-Limits]({{site.baseurl}}/api/basics) gelten.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)

Wenn Sie [Amazon S3-Zugangsdaten]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration) verbunden haben, können große Exporte zusätzlich zum per E-Mail versendeten Download-Link an Ihren Bucket geliefert werden, wie unter [Details zum Segment-CSV-Export](#segment-csv-export-details) beschrieben.

{% endtab %}
{% endtabs %}