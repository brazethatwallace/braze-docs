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

- Reichen Sie eine [Produktanfrage](https://portal.braze.com/) für datumsbasierte Exporte ein, wenn Sie Dashboard-ähnliche Berichte außerhalb der Standard-API-Zeitfenster benötigen.
- Rufen Sie die Endpunkte für [Campaign Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) oder [Canvas Analytics]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) mit den Parametern `ending_at` und `length` auf (oder verwenden Sie [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) und [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)) für Zeitreihendaten.
- Streamen Sie Events mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) in Ihr Data Warehouse, wenn Sie fortlaufend abfragbare Nachrichten-Engagement-Daten in Amazon S3, Azure Blob Storage oder einem anderen unterstützten Ziel benötigen.

## Wie bearbeite ich eine aktive Currents-Integration? {#how-do-i-edit-a-live-currents-integration}

Um einen aktiven Currents-Konnektor zu ändern, öffnen Sie die Integration und klicken Sie unten links auf der Seite auf **Bearbeiten**. Ohne **Bearbeiten** bleibt die Integrations-UI schreibgeschützt, und Sie können die Konnektor-Einstellungen nicht allein über die Symbole ändern.

## Wie geht Braze mit Azure Blob Storage Avro-Dateien nach dem Hochladen um? {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Braze ändert Avro-Dateien in [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) nach Abschluss des Uploads nicht. Azure kann das Löschen eines Blobs blockieren, solange ein Upload noch läuft.

## Wie komme ich an historische Daten? {#how-do-i-get-historical-data}

Currents ist ein Realtime-Live-Daten-Stream, d. h. Events können nicht erneut abgespielt werden. Sie können jedoch Currents-Daten in einem Data Warehouse wie [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) oder [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) speichern, sodass Sie nach Belieben auf vergangene Events zugreifen können. Die Daten werden 30 Tage lang aufbewahrt. Für weiter zurückliegende historische Daten können Sie [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake/) abfragen.

## Warum gibt Currents die Daten im Avro-Format und nicht in JSON aus? {#why-does-currents-output-data-in-the-avro-format-not-json}

Im Gegensatz zu JSON ohne Schema unterstützt Avro von Haus aus die Schemaentwicklung. Außerdem profitieren Sie davon, dass Avro-Dateien mit weniger Bandbreite übertragen werden können und Speicherplatz gespart wird, da Avro stark komprimierbar ist.

## Wie geht Braze mit dem Datei-Overhead um? {#how-does-braze-handle-file-overhead}

Wir bauen einen Extract, Transform, Load (ETL)-Prozess auf, mit dem Sie große Datenmengen aus einer Datenbank ziehen und in einer anderen speichern können.

## Wo sollte ich diese Daten für Abfragen speichern? {#where-should-i-store-this-data-for-querying}

Braze arbeitet mit mehreren Data Warehouses zusammen, in denen Sie Ihre Daten für Abfragen speichern können. Wir empfehlen:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

## Wie zuverlässig sind Currents-Daten? {#how-reliable-is-currents-data}

Currents garantiert eine „At-least-once“-Zustellung, d. h. doppelte Events können gelegentlich in Ihren Speicher-Bucket geschrieben werden. Wenn Ihr Anwendungsfall eine Exactly-once-Zustellung erfordert, können Sie Events mithilfe des eindeutigen Bezeichnerfelds (`id`) deduplizieren, das mit jedem Event gesendet wird. Weitere Informationen finden Sie unter [Event-Zustellungssemantik]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/).

## Wie oft werden Daten mit Currents synchronisiert? {#how-often-is-data-synced-to-currents}

Daten werden kontinuierlich gestreamt. Braze sendet einen Batch von Events, sobald ein vollständiger Batch vorliegt oder alle 5 Minuten – je nachdem, was zuerst eintritt. Bei Konnektoren mit hohem Volumen treffen die Daten nahezu in Realtime ein. Bei Konnektoren mit geringem Volumen ist mit einer Verzögerung von 5 bis 30 Minuten zu rechnen. Weitere Informationen finden Sie unter [Avro-Schreibschwellenwert]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
Wenn ein Gerät nicht mit dem Internet verbunden ist, kann es zu einer Verzögerung bei der Erstellung des Events kommen. Dies tritt am häufigsten bei In-App-Nachrichten-Events auf, da In-App-Nachrichten auch offline getriggert werden können.
{% endalert %}

## Wie finde ich heraus, welche Events für Currents verfügbar sind? {#how-do-i-find-which-events-are-available-for-currents}

Eine vollständige Liste der Events, die Currents protokolliert, finden Sie in den Glossaren [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) und [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). Sie können diese Glossare nach Event-Typ filtern (z. B. Sendungen, Zustellungen oder Öffnungen).

## Warum unterscheidet sich die `external_id` in meinem Currents-E-Mail-Öffnungs- oder Klick-Event vom Nutzerprofil im Braze-Dashboard? {#why-does-the-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Im Braze-Dashboard:** Wenn ein:e Nutzer:in, der/die mit einer E-Mail-Adresse verknüpft ist, eine E-Mail öffnet oder anklickt, werden alle Nutzerprofile, die diese E-Mail-Adresse teilen, als geöffnet bzw. angeklickt markiert. Weitere Informationen finden Sie unter [Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben?]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **In Currents:** Dieselbe Öffnung oder derselbe Klick wird nur einem Profil zugeordnet. Braze ordnet das Event dem Profil zu, das ursprünglich für den Versand ausgewählt wurde, sofern dieses Profil die E-Mail-Adresse noch teilt. Andernfalls ordnet Braze es einem zufällig ausgewählten Profil unter denjenigen zu, die die E-Mail-Adresse teilen.

Aus diesem Grund stimmt die `external_id` eines Currents-E-Mail-Öffnungs- oder Klick-Events möglicherweise nicht mit dem Nutzerprofil überein, das Sie erwarten, wenn Sie Currents mit dem Braze-Dashboard vergleichen.

## Werden alle Sende-Events in Currents protokolliert? {#are-all-send-events-logged-to-currents}

Alle Events werden in Currents protokolliert. Es gibt keine Szenarien, in denen ein Event absichtlich aus dem Currents-Stream unterdrückt wird.

## Können Daten in Currents beschädigt werden? {#can-data-be-corrupted-in-currents}

Unter normalen Umständen werden Currents-Daten nicht beschädigt. Obwohl es immer die Möglichkeit eines seltenen Problems gibt, sind keine Bedingungen bekannt, unter denen Daten systematisch beschädigt werden würden.

## Warum sehe ich angepasste Event-Daten mit einem Datum vor der Einrichtung meiner Currents-Integration? {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

Braze füllt Events nicht rückwirkend in Currents auf. Angepasste Events können jedoch mit einem vergangenen Zeitstempel protokolliert werden (z. B. wenn ein Gerät zum Zeitpunkt des Events offline war und die Daten später synchronisiert wurden). In diesen Fällen spiegelt der Event-Zeitstempel den Zeitpunkt wider, an dem das Event ursprünglich aufgetreten ist, was vor der Konfiguration der Currents-Integration liegen kann.

## Kann ich angepasste Attribute in Currents-Sende-Events einbeziehen? {#can-i-include-custom-attributes-in-currents-send-events}

Nein. Currents enthält keine angepassten Attribute in Sende-Events. Currents protokolliert angepasste Events und Nachrichten-Engagement-Events. Eine vollständige Liste der verfügbaren Felder finden Sie in den [Event-Glossaren]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/).

## Enthält Currents Campaign- oder Canvas-Tags oder Schlüssel-Wert-Paare? {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

Nein. Currents enthält keine Campaign- oder Canvas-Tags und keine Schlüssel-Wert-Paare auf Nachrichtenebene. Um Tag-Daten abzurufen, verwenden Sie die [Export-REST-API]({{site.baseurl}}/api/endpoints/export/). Als weiteren Workaround können Sie einen Webhook-Kanal in einer Campaign verwenden, um Tag- oder Schlüssel-Wert-Paar-Daten an Ihren eigenen Endpunkt zu senden, und dabei [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) nutzen, um die Werte als Template einzubinden.

## Wie informiert Braze Kund:innen über Änderungen an Currents? {#how-does-braze-notify-customers-of-changes-to-currents}

Wenn Änderungen an Currents vorgenommen werden (z. B. neue Event-Felder oder Event-Typen), sendet Braze eine E-Mail an alle Kund:innen mit aktiven Currents-Integrationen, die das Dashboard in den letzten 30 Tagen genutzt haben. Außerdem können Sie den [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/) für die neuesten Änderungen einsehen.

## Wie viel Speicherplatz benötige ich für Currents-Daten? {#how-much-storage-do-i-need-for-currents-data}

Der Speicherbedarf hängt von Ihrem Event-Volumen und den Typen der Events ab, die Sie exportieren. Braze stellt [Beispiel-Events im Avro-Format](https://github.com/appboy/currents-examples/tree/master/sample-data) bereit, mit denen Sie die Dateigrößen für Ihren Anwendungsfall schätzen können.

## Warum ist der Campaign-Name oder Canvas-Schrittname `NULL` in meinen Currents-Daten? {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

Wenn Sie eine neue Campaign oder ein neues Canvas erstellen, kann es einige Zeit dauern, bis der Name in allen Braze-Systemen verfügbar ist. Events, die während dieses Zeitfensters über Currents gesendet werden, können `NULL` in den Namensfeldern enthalten (z. B. `campaign_name` oder `canvas_step_name`). Dies ist auch zu erwarten, wenn der Name kurz vor der Protokollierung der Events geändert wurde. Um dies zu vermeiden, warten Sie nach dem Erstellen oder Umbenennen einer Campaign oder eines Canvas-Schritts etwas ab, bevor Sie senden.

## Warum sind Sitzungsende-Events in Currents verzögert oder fehlen? {#why-are-session-end-events-delayed-or-missing-in-currents}

Sitzungsende-Events folgen dem normalen Upload-Zeitplan des SDK. Das Braze SDK speichert Sitzungsdaten lokal zwischen und überträgt sie periodisch basierend auf der Netzwerkqualität – beispielsweise etwa alle 10 Sekunden bei einer stabilen Verbindung. Bis das SDK das Event hochlädt, erscheint es nicht in Currents.

Wenn ein:e Nutzer:in die App erzwungen beendet oder offline geht, bevor der nächste Upload stattfindet, kann das Sitzungsende-Event verspätet oder gar nicht eintreffen. Unter iOS werden Sitzungsende-Events oft erst beim erneuten Öffnen der App übertragen, da das SDK keine Daten senden kann, während die App im Hintergrund läuft.

Wenn Sie zeitnähere Sitzungsgrenzen in Currents benötigen, rufen Sie `requestImmediateDataFlush()` an Lifecycle-Punkten auf, z. B. wenn die App in den Hintergrund wechselt oder in den Vordergrund zurückkehrt. Weitere Informationen finden Sie unter [Daten-Upload und -Download]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/#data-upload-and-download) und [Sitzungsende und Sitzungsstart haben ähnliche Zeitstempel (iOS)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/#session-end-and-session-start-have-similar-timestamps-ios).

## Was passiert, wenn mein Speicher-Bucket nicht verfügbar ist, wenn Currents versucht, Daten zu schreiben? {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

Wenn Ihr Speicher-Bucket zum Zeitpunkt der Datenübertragung nicht verfügbar ist, gehen diese Daten verloren. Braze kann Events, die nicht erfolgreich zugestellt wurden, nicht nachträglich auffüllen. Um Datenverlust zu vermeiden, stellen Sie sicher, dass Ihr Speicher-Bucket jederzeit verfügbar und korrekt konfiguriert ist.

## Warum wird die Meldung „You do not have any remaining Customer Behavior Events entitlements“ angezeigt, wenn ich meine Currents-Integration bearbeite? {#why-do-i-see-you-do-not-have-any-remaining-customer-behavior-events-entitlements-when-editing-my-currents-integration}

Diese Meldung kann erscheinen, wenn Sie eine bestehende Currents-Integration aktualisieren und Ihr Workspace das Kontingent für Kundenverhalten-Events erreicht hat. Kontaktieren Sie Ihren Braze Account Manager, um ein zusätzliches Kontingent anzufordern oder Ihre Konfiguration anzupassen.

## Wie oft ändert sich die Currents-Version im Speicherpfad? {#how-often-does-the-currents-version-in-the-storage-path-change}

Das Segment `version=<currents_version>` im Speicherpfad wird mit jedem Currents-Release in einem monatlichen Rhythmus aktualisiert (z. B. von `version=6` auf `version=7`). Wir empfehlen, Dateien rekursiv vom Stammpfad aus zu lesen, anstatt ein bestimmtes Versionssegment fest zu codieren, damit Ihre Pipeline nach einer Versionsänderung automatisch die neuen Daten erfasst. Weitere Informationen zum Pfadformat finden Sie unter [Event-Zustellungssemantik]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/). Eine Übersicht der Änderungen nach Version finden Sie im [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/).

## Warum fehlen `campaign_id` oder `canvas_id` in einem Nachrichten-Engagement-Event? {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

Je nach Event-Typ und Kontext ist ein Nachrichten-Engagement-Event möglicherweise nicht mit einer bestimmten Campaign oder einem bestimmten Canvas-Schritt verknüpft. In diesen Fällen können `campaign_id`, `canvas_id` und zugehörige Namensfelder im Event-Payload fehlen. Wenn Sie diese Felder bei einem bestimmten Event nicht sehen, prüfen Sie, ob dieser Event-Typ und Kontext normalerweise Campaign- oder Canvas-Bezeichner enthalten.

## Warum sind Currents-Zeitstempel auf Sekundenpräzision beschränkt? {#why-are-currents-timestamps-limited-to-second-precision}

Das Feld `time` in Currents-Events wird als 32-Bit-Ganzzahl gespeichert und ist daher auf Sekundenpräzision beschränkt. Einige Events enthalten zusätzlich ein separates 64-Bit-Zeitstempelfeld mit Millisekunden-Präzision. Welche Felder für den jeweiligen Event-Typ verfügbar sind, erfahren Sie im [Event-Glossar]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/).

## Warum hat das `users.canvas.Conversion`-Event aus Currents einen anderen Zeitpunkt als das Canvas? {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

Der Zeitpunkt des `users.canvas.Conversion`-Events in Currents spiegelt das gesamte Conversion-Fenster wider – die Canvas-Dauer plus die Conversion-Frist – gemessen ab dem Canvas-Eintritt.

## Was passiert, wenn Engagement-Berichte an S3 gesendet werden? {#what-happens-when-engagement-reports-are-sent-to-s3}

Wenn S3-Zugangsdaten für den Datenexport, aber nicht für Currents konfiguriert sind, lädt Braze Engagement-Berichte in den angegebenen S3-Bucket hoch. Die im Feld **Bericht senden an** aufgeführte Person erhält eine E-Mail mit einem Link zum Bericht in S3.

## Können anonyme Nutzerdaten über Braze-Currents an Amplitude gesendet werden? {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

Anonyme Nutzerdaten, die über `device_id` identifiziert werden, können über Currents an Amplitude gesendet werden. Dafür muss das Feature von Ihrem Braze Account-Team aktiviert werden.

## Wie werden Kontrollgruppen-Impressionen für Content Cards und In-App-Nachrichten in Currents protokolliert? {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

Wenn ein:e Nutzer:in einer Kontrollgruppe für eine Content-Card- oder In-App-Nachrichten-Campaign zugewiesen wird, gibt Currents ein `users.campaigns.EnrollInControl`-Event anstelle eines Impressions-Events aus.

## Was passiert, wenn Sie über die API eine:n nicht existierende:n Nutzer:in ansprechen? {#what-happens-when-you-target-a-non-existent-user-through-the-api}

Wenn Sie eine:n Nutzer:in ansprechen, der/die nicht existiert, gibt die API eine `200`-Antwort zurück, aber der Versand wird mit dem Ergebnis „Unknown external ID“ abgebrochen. Für diesen Versand werden keine Currents-Events generiert. Beachten Sie, dass der Parameter `send_to_existing_only` standardmäßig auf `true` gesetzt ist, sodass Sendungen an unbekannte Nutzer:innen stillschweigend übersprungen werden, es sei denn, Sie setzen ihn explizit auf `false`.