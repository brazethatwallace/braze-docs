---
nav_title: FAQ
article_title: Currents FAQ
page_order: 4
page_type: reference
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von Braze-Currents auftreten."
tool: Currents
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu Currents.

## Kann ich Campaign- oder Canvas-Daten für ein bestimmtes Zeitfenster exportieren? {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

Um Campaign- oder Canvas-Metriken für einen definierten Zeitraum abzurufen, verwenden Sie einen der folgenden Ansätze:

- {% multi_lang_include product_feedback_cta.md context="gap" feature="date-aligned campaign or Canvas exports for dashboard-style reporting outside standard API windows" %}
- Rufen Sie die Endpunkte für [Campaign-Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) oder [Canvas-Analytics]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) mit den Parametern `ending_at` und `length` auf (oder verwenden Sie [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) und [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)) für Zeitreihendaten.
- Streamen Sie Events mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) in Ihr Data Warehouse, wenn Sie fortlaufend abfragbare Nachrichten-Engagement-Daten in Amazon S3, Azure Blob Storage oder einem anderen unterstützten Ziel benötigen.

## Wie bearbeite ich eine aktive Currents-Integration? {#how-do-i-edit-a-live-currents-integration}

Um einen aktiven Currents-Konnektor zu ändern, öffnen Sie die Integration und wählen Sie **Bearbeiten** aus. Ohne **Bearbeiten** bleibt die Integrations-UI schreibgeschützt, und Sie können die Konnektor-Einstellungen nicht allein über die Symbole ändern.

## Wie behandelt Braze Avro-Dateien in Azure Blob Storage nach dem Upload? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze modifiziert Avro-Dateien in [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) nach Abschluss des Uploads nicht. Azure kann das Löschen eines Blobs blockieren, solange ein Upload noch läuft.

## Wie erhalte ich historische Daten? {#how-do-i-get-historical-data}

Currents ist ein Echtzeit-Live-Datenstrom, d. h. Events können nicht erneut abgespielt werden. Sie können Currents-Daten jedoch in einem Data Warehouse wie [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) oder [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) speichern, um vergangene Events nach Bedarf zu verarbeiten. Daten werden 30 Tage lang aufbewahrt. Für weiter zurückreichende historische Daten können Sie [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake) abfragen.

## Warum gibt Currents Daten im Avro-Format aus und nicht in JSON? {#why-does-currents-output-data-in-the-avro-format-not-json}

Avro unterstützt im Gegensatz zu schemalosem JSON nativ die Schema-Evolution. Darüber hinaus profitieren Sie von der Möglichkeit, Avro-Dateien mit geringerer Bandbreite zu senden und Speicherplatz zu sparen, da Avro sehr gut komprimierbar ist.

## Wie geht Braze mit Datei-Overhead um? {#how-does-braze-handle-file-overhead}

Wir bauen einen ETL (ETL)-Prozess auf, mit dem Sie große Datenmengen aus einer Datenbank abrufen und in einer anderen ablegen und speichern können.

## Wo sollte ich diese Daten für Abfragen speichern? {#where-should-i-store-this-data-for-querying}

Braze arbeitet mit mehreren Data Warehouses zusammen, in denen Sie Ihre Daten für Abfragen speichern können. Wir empfehlen die Verwendung von:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents).

## Wie zuverlässig sind Currents-Daten? {#how-reliable-is-currents-data}

Currents garantiert eine „At-least-once“-Zustellung, was bedeutet, dass gelegentlich doppelte Events in Ihren Storage-Bucket geschrieben werden können. Wenn Ihr Anwendungsfall eine Exactly-once-Zustellung erfordert, können Sie Events mithilfe des eindeutigen Bezeichnerfelds (`id`) deduplizieren, das mit jedem Event gesendet wird. Weitere Informationen finden Sie unter [Event-Zustellungssemantik]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics).

## Wie oft werden Daten mit Currents synchronisiert? {#how-often-is-data-synced-to-currents}

Daten werden kontinuierlich gestreamt. Braze sendet einen Batch von Events, sobald ein vollständiger Batch vorliegt oder alle 5 Minuten – je nachdem, was zuerst eintritt. Bei Konnektoren mit hohem Datenvolumen treffen die Daten nahezu in Realtime ein. Bei Konnektoren mit niedrigem Datenvolumen ist mit einer Verzögerung von 5 bis 30 Minuten zu rechnen. Weitere Informationen finden Sie unter [Avro-Schreibschwellenwert]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics#avro-write-threshold).

{% alert note %}
Wenn ein Gerät nicht mit dem Internet verbunden ist, kann es zu einer Verzögerung bei der Erstellung des Events kommen. Dies tritt am häufigsten bei In-App-Nachrichten-Events auf, da In-App-Nachrichten auch offline ausgelöst werden können.
{% endalert %}

## Wie finde ich heraus, welche Events für Currents verfügbar sind? {#how-do-i-find-which-events-are-available-for-currents}

Eine vollständige Liste der Events, die Currents protokolliert, finden Sie in den Glossaren für [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) und [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). Sie können diese Glossare nach Event-Typ filtern (z. B. Sends, Zustellungen oder Öffnungen).

## Warum stimmen meine Currents-Event-Zahlen nicht mit meinen Dashboard- oder Engagement-Bericht-Metriken überein? {#why-do-my-currents-event-counts-not-match-my-dashboard-or-engagement-report-metrics}

Currents und das Braze-Dashboard berechnen bestimmte Metriken unterschiedlich, daher sind exakte Übereinstimmungen zwischen Currents-Events und Dashboard-Metriken nicht zu erwarten.

**Eindeutige Klicks:** Für E-Mails erfasst das Dashboard eindeutige Klicks über einen Zeitraum von sieben Tagen und misst sie anhand der `dispatch_id`. Currents zeichnet jedes einzelne Klick-Event auf. Um die auf Currents basierenden eindeutigen Klick-Zahlen mit den Dashboard-Metriken abzugleichen, filtern Sie nach Events, bei denen `is_unique` auf `true` gesetzt ist.

**Abmeldungen:** Die Dashboard-Metrik *Unsub* spiegelt Klicks auf den Standard-Abmeldelink von Braze wider. Angepasste Abmeldeseiten erhöhen diese Metrik nicht, es sei denn, Sie aktualisieren die Nutzer:innen über die API. Das Currents-Event `users.messages.email.Unsubscribe` ist ein spezielles Klick-Event, das ausgelöst wird, wenn Nutzer:innen auf einen Abmeldelink im E-Mail-Text oder in der Fußzeile klicken oder den List-Unsubscribe-Header verwenden. Es repräsentiert nicht jede Änderung des E-Mail-Abostatus.

**Zeitstempel und Zeitzonen:** Alle Currents-Zeitstempel sind in UTC. Dashboard-Metriken richten sich nach der Zeitzone Ihres Unternehmens. Wenn Sie Currents-Daten nach Kalendertag aggregieren, ohne sie in die Zeitzone Ihres Unternehmens umzurechnen, können Zählwerte in andere Datums-Buckets fallen als im Dashboard angezeigt.

**Doppelte Events:** Currents bietet eine At-Least-Once-Zustellung, was bedeutet, dass gelegentlich doppelte Events geschrieben werden können. Deduplizieren Sie anhand des eindeutigen `id`-Feldes jedes Events, bevor Sie Gesamtzahlen mit Dashboard-Metriken vergleichen.

## Warum weicht die `external_user_id` (Braze-Schema: `external_id`) in meinem Currents-E-Mail-Öffnungs- oder Klick-Event vom Kundenprofil im Braze-Dashboard ab? {#why-does-the-external_user_id-braze-schema-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Im Braze-Dashboard:** Wenn eine mit einer E-Mail-Adresse verknüpfte Person eine E-Mail öffnet oder anklickt, werden alle Nutzerprofile, die diese E-Mail-Adresse teilen, als geöffnet bzw. angeklickt markiert. Weitere Informationen finden Sie unter [Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben?]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **In Currents:** Derselbe Öffnungs- oder Klick-Vorgang wird nur in einem Profil gespeichert. Braze ordnet ihn dem Profil zu, das ursprünglich für den Versand ausgewählt wurde, sofern dieses Profil die E-Mail-Adresse noch teilt. Andernfalls ordnet Braze ihn einem zufällig ausgewählten Profil unter denjenigen zu, die die E-Mail-Adresse gemeinsam nutzen.

Aus diesem Grund stimmt der `external_user_id`-Wert (in der Braze-Schema-Zuordnungstabelle als `external_id` bezeichnet) eines Currents-E-Mail-Öffnungs- oder Klick-Events möglicherweise nicht mit dem Kundenprofil überein, das Sie erwarten, wenn Sie Currents mit dem Braze-Dashboard vergleichen.

## Werden alle Sende-Events in Currents protokolliert? {#are-all-send-events-logged-to-currents}

Alle Events werden in Currents protokolliert. Es gibt keine Szenarien, in denen ein Event absichtlich aus dem Currents-Stream unterdrückt wird.

## Können Daten in Currents beschädigt werden? {#can-data-be-corrupted-in-currents}

Unter normalen Umständen werden Currents-Daten nicht beschädigt. Auch wenn die Möglichkeit eines seltenen Problems immer besteht, gibt es keine bekannten Bedingungen, unter denen Daten systematisch beschädigt würden.

## Warum sehe ich angepasste Event-Daten mit einem Datum vor der Einrichtung meiner Currents-Integration? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze füllt keine Events nachträglich in Currents auf. Angepasste Events können jedoch mit einem vergangenen Zeitstempel protokolliert werden (zum Beispiel, wenn ein Gerät zum Zeitpunkt des Events offline war und die Daten erst später synchronisiert wurden). In diesen Fällen spiegelt der Event-Zeitstempel den ursprünglichen Zeitpunkt des Events wider, der vor der Konfiguration der Currents-Integration liegen kann.

## Welche Nutzerbezeichner sind in Currents-Events enthalten? {#what-user-identifiers-are-included-in-currents-events}

Message-Engagement-Events (Versand, Öffnungen, Klicks usw.) enthalten die Braze-Nutzer-ID (`user_id`) und, sofern im Profil vorhanden, den externen Bezeichner (`external_user_id` in Event-Payloads, in der Braze-Schemazuordnungstabelle als `external_id` bezeichnet). Einige E-Mail-Message-Engagement-Events enthalten auch `email_address`. Angepasste Attribute sind nicht enthalten.

Wenn Sie Currents-Daten an ein Data Warehouse oder CRM weiterleiten und mit Profildaten verknüpfen müssen, führen Sie diesen Join in Ihrem nachgelagerten System mithilfe von `user_id` oder `external_user_id` durch.

## Kann ich angepasste Attribute in Currents-Sende-Events einbeziehen? {#can-i-include-custom-attributes-in-currents-send-events}

Nein. Currents enthält keine angepassten Attribute in Sende-Events. Currents protokolliert angepasste Events und Nachrichten-Engagement-Events. Eine vollständige Liste der verfügbaren Felder finden Sie in den [Event-Glossaren]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary).

## Enthält Currents Campaign- oder Canvas-Tags oder Schlüssel-Wert-Paare? {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

Nein. Currents enthält keine Campaign- oder Canvas-Tags oder Schlüssel-Wert-Paare auf Nachrichtenebene. Um Tag-Daten abzurufen, verwenden Sie die [Export-REST-API]({{site.baseurl}}/api/endpoints/export). Als alternative Lösung können Sie einen Webhook-Kanal in einer Campaign nutzen, um Tag- oder Schlüssel-Wert-Paar-Daten an Ihren eigenen Endpunkt zu senden, indem Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) verwenden, um die Werte als Template einzusetzen.

## Wie informiert Braze Kund:innen über Änderungen an Currents? {#how-does-braze-notify-customers-of-changes-to-currents}

In dem seltenen Fall, dass grundlegende Änderungen auftreten, sendet Braze eine Vorankündigungs-E-Mail an den Kontakt jeder aktiven Integration sowie an alle Admins mit aktiven Currents-Integrationen, die das Dashboard in den letzten 30 Tagen genutzt haben. Bei nicht grundlegenden Änderungen, wie neuen Events oder neuen Feldern in einem bestehenden Event, sendet Braze keine Benachrichtigung. Im [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) finden Sie die neuesten Änderungen.

## Wie viel Speicherplatz benötige ich für Currents-Daten? {#how-much-storage-do-i-need-for-currents-data}

Die Speicheranforderungen hängen von Ihrem Event-Volumen und den Arten von Events ab, die Sie exportieren. Braze stellt [Beispiel-Events im Avro-Format](https://github.com/appboy/currents-examples/tree/master/sample-data) bereit, mit denen Sie die Dateigrößen für Ihren Anwendungsfall abschätzen können.

## Warum ist der Campaign-Name oder Canvas-Schritt-Name in meinen Currents-Daten `NULL`? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Wenn Sie eine neue Campaign oder einen neuen Canvas erstellen, kann es einige Zeit dauern, bis der Name in allen Braze-Systemen verbreitet wird. Events, die während dieses Zeitfensters über Currents gesendet werden, können `NULL` in den Namensfeldern enthalten (z. B. `campaign_name` oder `canvas_step_name`). Dies ist auch zu erwarten, wenn der Name kurz vor der Protokollierung der Events geändert wurde. Um dies zu vermeiden, warten Sie nach dem Erstellen oder Umbenennen einer Campaign oder eines Canvas-Schritts einige Zeit, bevor Sie den Versand starten.

## Warum sind Sitzungsende-Events in Currents verzögert oder fehlen? {#why-are-session-end-events-delayed-or-missing-in-currents}

Sitzungsende-Events folgen dem normalen Upload-Zeitplan des SDK. Das Braze SDK speichert Sitzungsdaten lokal zwischen und sendet sie in regelmäßigen Abständen abhängig von der Netzwerkqualität – beispielsweise etwa alle 10 Sekunden bei einer starken Verbindung. Solange das SDK das Event nicht hochgeladen hat, erscheint es nicht in Currents.

Wenn Nutzer:innen die App erzwungen beenden oder offline gehen, bevor der nächste Flush stattfindet, kann das Sitzungsende-Event verspätet oder gar nicht eintreffen. Unter iOS werden Sitzungsende-Events häufig erst gesendet, wenn die App erneut geöffnet wird, da das SDK keine Daten übertragen kann, während die App im Hintergrund läuft.

Wenn Sie zeitnahere Sitzungsgrenzen in Currents benötigen, rufen Sie `requestImmediateDataFlush()` an Lifecycle-Punkten auf, z. B. wenn die App in den Hintergrund wechselt oder in den Vordergrund zurückkehrt. Weitere Informationen finden Sie unter [Daten-Upload und -Download]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#data-upload-and-download) und [Sitzungsende und Sitzungsstart haben ähnliche Zeitstempel (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log#session-end-and-session-start-have-similar-timestamps-ios).

## Was passiert, wenn mein Storage-Bucket nicht verfügbar ist, wenn Currents versucht, Daten zu schreiben? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Wenn Ihr Storage-Bucket zum Zeitpunkt der Datenübertragung nicht verfügbar ist, gehen diese Daten verloren. Braze ist nicht in der Lage, Events nachzuliefern, die nicht erfolgreich zugestellt wurden. Um Datenverlust zu vermeiden, stellen Sie sicher, dass Ihr Storage-Bucket jederzeit verfügbar und ordnungsgemäß konfiguriert ist.

## Warum sehe ich Meldungen zu Berechtigungslimits, wenn ich eine Currents-Integration erstelle oder bearbeite? {#why-do-i-see-entitlement-limit-messages-when-creating-or-editing-a-currents-integration}

Currents verwendet separate Berechtigungspools für unterschiedliche Konnektor-Funktionen:

- **Engagement Events**: Erforderlich, um einen Standard-Currents-Konnektor zu erstellen oder zu aktualisieren.
- **Customer Behavior Events**: Erforderlich, um **Track Customer Behavior and User Events** zu aktivieren.
- **User Profiles and Attributes**: Erforderlich, um **Track user profiles and attributes** zu aktivieren.

Wenn ein Pool erschöpft ist, zeigt Braze eine Berechtigungswarnung an und blockiert die jeweilige Aktion. Wenden Sie sich an Ihren Braze Account Manager:in, um zusätzliche Berechtigungen anzufordern oder Ihre Konfiguration anpassen zu lassen.

## Wie oft ändert sich die Currents-Version im Speicherpfad? {#how-often-does-the-currents-version-in-the-storage-path-change}

Das Segment `version=<currents_version>` im Speicherpfad wird mit jedem Currents-Release in einem monatlichen Rhythmus aktualisiert (zum Beispiel von `version=6` auf `version=7`). Wir empfehlen, Dateien rekursiv vom Stammpfad zu lesen, anstatt ein bestimmtes Versionssegment fest zu codieren, damit Ihre Pipeline nach einem Versionswechsel automatisch die Daten erfasst. Weitere Einzelheiten zum Pfadformat finden Sie unter [Event-Zustellungssemantik]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics). Eine Übersicht der Änderungen nach Version finden Sie im [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

## Warum fehlen `campaign_id` oder `canvas_id` bei einem Message-Engagement-Event? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Je nach Eventtyp und Kontext ist ein Message-Engagement-Event möglicherweise nicht an eine bestimmte Campaign oder einen bestimmten Canvas-Schritt gebunden. In diesen Fällen können `campaign_id`, `canvas_id` und zugehörige Namensfelder in der Event-Payload fehlen. Wenn Sie diese Felder bei einem bestimmten Event nicht sehen, prüfen Sie, ob dieser Eventtyp und Kontext normalerweise Campaign- oder Canvas-Bezeichner enthalten.

## Warum sind Zeitstempel in Currents auf Sekundenpräzision beschränkt? {#why-are-currents-timestamps-limited-to-second-precision}

Das Feld `time` in Currents-Events wird als 32-Bit-Ganzzahl gespeichert und ist daher auf Sekundenpräzision beschränkt. Einige Events enthalten zusätzlich ein separates 64-Bit-Zeitstempelfeld mit Millisekunden-Präzision. Prüfen Sie im [Event-Glossar]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary), welche Felder für den jeweiligen Event-Typ verfügbar sind.

## Warum hat das `users.canvas.Conversion`-Event aus Currents einen anderen Zeitpunkt als das Canvas? {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

Der Zeitpunkt des `users.canvas.Conversion`-Events in Currents spiegelt das gesamte Konversionsfenster wider – die Canvas-Dauer plus die Konversionsfrist – gemessen ab dem Canvas-Eintritt.

## Was passiert, wenn Engagement-Berichte an S3 gesendet werden? {#what-happens-when-engagement-reports-are-sent-to-s3}

Wenn S3-Zugangsdaten für den Datenexport konfiguriert sind, aber nicht für Currents, lädt Braze die Engagement-Berichte in den angegebenen S3-Bucket hoch. Die im Feld **Send Report To** aufgeführte Person erhält eine E-Mail mit einem Link zum Bericht in S3.

## Können anonyme Nutzerdaten über Braze-Currents an Amplitude gesendet werden? {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

Anonyme Nutzerdaten, die durch eine `device_id` identifiziert werden, können über Currents an Amplitude gesendet werden. Hierfür ist eine Feature-Aktivierung durch Ihr Braze-Account-Team erforderlich.

## Wie werden Kontrollgruppen-Impressionen für Content Cards und In-App-Nachrichten in Currents protokolliert? {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

Wenn Nutzer:innen einer Kontrollgruppe für eine Content-Card- oder In-App-Message-Campaign zugewiesen werden, sendet Currents ein `users.campaigns.EnrollInControl`-Event anstelle eines Impression-Events.

## Was passiert, wenn Sie über die API eine:n nicht existierende:n Nutzer:in ansprechen? {#what-happens-when-you-target-a-non-existent-user-through-the-api}

Wenn Sie eine:n Nutzer:in ansprechen, die:der nicht existiert, gibt die API eine `200`-Antwort zurück, aber der Versand wird mit dem Ergebnis „Unknown external ID“ abgebrochen. Für diesen Versand werden keine Currents-Events generiert. Beachten Sie, dass der Parameter `send_to_existing_only` standardmäßig auf `true` gesetzt ist, sodass Sendungen an unbekannte Nutzer:innen stillschweigend übersprungen werden, es sei denn, Sie setzen ihn explizit auf `false`.