---
nav_title: FAQ
article_title: Currents FAQ
page_order: 4
page_type: reference
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von Braze-Currents auftreten."
tool: Currents
---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu Currents.

### Wie komme ich an historische Daten?

Currents ist ein Realtime-Live-Daten-Stream, d. h. Events können nicht erneut abgespielt werden. Sie können jedoch Currents-Daten in einem Data Warehouse wie [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) oder [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) speichern, sodass Sie nach Belieben auf vergangene Events zugreifen können. Die Daten werden 30 Tage lang aufbewahrt. Für weiter zurückliegende historische Daten können Sie [Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake/) abfragen.

### Warum gibt Currents die Daten im Avro-Format und nicht in JSON aus?

Im Gegensatz zu JSON ohne Schema unterstützt Avro von Haus aus die Schemaentwicklung. Außerdem profitieren Sie davon, dass Avro-Dateien mit weniger Bandbreite übertragen werden können und Speicherplatz gespart wird, da Avro stark komprimierbar ist.

### Wie geht Braze mit dem Datei-Overhead um?

Wir bauen einen Extract, Transform, Load (ETL)-Prozess auf, mit dem Sie große Datenmengen aus einer Datenbank ziehen und in einer anderen speichern können.

### Wo sollte ich diese Daten für Abfragen speichern?

Braze arbeitet mit mehreren Data Warehouses zusammen, in denen Sie Ihre Daten für Abfragen speichern können. Wir empfehlen:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### Wie zuverlässig sind Currents-Daten?

Currents garantiert eine „At-least-once“-Zustellung, d. h. doppelte Events können gelegentlich in Ihren Speicher-Bucket geschrieben werden. Wenn Ihr Anwendungsfall eine Exactly-once-Zustellung erfordert, können Sie Events mithilfe des eindeutigen Bezeichnerfelds (`id`) deduplizieren, das mit jedem Event gesendet wird. Weitere Informationen finden Sie unter [Event-Zustellungssemantik]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/).

### Wie oft werden Daten mit Currents synchronisiert?

Daten werden kontinuierlich gestreamt. Braze sendet einen Batch von Events, sobald ein vollständiger Batch vorliegt oder alle 5 Minuten – je nachdem, was zuerst eintritt. Bei Konnektoren mit hohem Volumen treffen die Daten nahezu in Realtime ein. Bei Konnektoren mit geringem Volumen ist mit einer Verzögerung von 5 bis 30 Minuten zu rechnen. Weitere Informationen finden Sie unter [Avro-Schreibschwellenwert]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
Wenn ein Gerät nicht mit dem Internet verbunden ist, kann es zu einer Verzögerung bei der Erstellung des Events kommen. Dies tritt am häufigsten bei In-App-Nachrichten-Events auf, da In-App-Nachrichten auch offline getriggert werden können.
{% endalert %}

### Wie finde ich heraus, welche Events für Currents verfügbar sind?

Eine vollständige Liste der Events, die Currents protokolliert, finden Sie in den Glossaren [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) und [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). Sie können diese Glossare nach Event-Typ filtern (z. B. Sendungen, Zustellungen oder Öffnungen).

### Warum unterscheidet sich die `external_id` in meinem Currents-E-Mail-Öffnungs- oder Klick-Event vom Nutzerprofil im Braze-Dashboard?

- **Im Braze-Dashboard:** Wenn eine Nutzer:in, die mit einer E-Mail-Adresse verknüpft ist, eine E-Mail öffnet oder anklickt, werden alle Nutzerprofile, die diese E-Mail-Adresse teilen, als geöffnet bzw. angeklickt markiert. Weitere Informationen finden Sie unter [Was passiert, wenn eine E-Mail versendet wird und mehrere Profile dieselbe E-Mail-Adresse haben?]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).
- **In Currents:** Dieselbe Öffnung oder derselbe Klick wird nur einem Profil zugeordnet. Braze ordnet das Event dem Profil zu, das ursprünglich für den Versand ausgewählt wurde, sofern dieses Profil die E-Mail-Adresse noch teilt. Andernfalls ordnet Braze es einem zufällig ausgewählten Profil unter denjenigen zu, die die E-Mail-Adresse teilen.

Aus diesem Grund stimmt die `external_id` eines Currents-E-Mail-Öffnungs- oder Klick-Events möglicherweise nicht mit dem Nutzerprofil überein, das Sie erwarten, wenn Sie Currents mit dem Braze-Dashboard vergleichen.

### Werden alle Sende-Events in Currents protokolliert?

Alle Events werden in Currents protokolliert. Es gibt keine Szenarien, in denen ein Event absichtlich aus dem Currents-Stream unterdrückt wird.

### Können Daten in Currents beschädigt werden?

Unter normalen Umständen werden Currents-Daten nicht beschädigt. Obwohl es immer die Möglichkeit eines seltenen Problems gibt, sind keine Bedingungen bekannt, unter denen Daten systematisch beschädigt werden würden.

### Warum sehe ich angepasste Event-Daten mit einem Datum vor der Einrichtung meiner Currents-Integration?

Braze füllt Events nicht rückwirkend in Currents auf. Angepasste Events können jedoch mit einem vergangenen Zeitstempel protokolliert werden (z. B. wenn ein Gerät zum Zeitpunkt des Events offline war und die Daten später synchronisiert wurden). In diesen Fällen spiegelt der Event-Zeitstempel den Zeitpunkt wider, an dem das Event ursprünglich aufgetreten ist, was vor der Konfiguration der Currents-Integration liegen kann.

### Kann ich angepasste Attribute in Currents-Sende-Events einbeziehen?

Nein. Currents enthält keine angepassten Attribute in Sende-Events. Currents protokolliert angepasste Events und Nachrichten-Engagement-Events. Eine vollständige Liste der verfügbaren Felder finden Sie in den [Event-Glossaren]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/).

### Enthält Currents Kampagnen-Tags oder Schlüssel-Wert-Paare?

Nein. Currents enthält keine Kampagnen-Tags oder Schlüssel-Wert-Paare auf Nachrichtenebene. Als Workaround können Sie einen Webhook-Kanal in der Kampagne verwenden, um diese Informationen an Ihren eigenen Endpunkt zu senden, und dabei [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) nutzen, um die Tag- und Schlüssel-Wert-Paar-Daten als Template einzubinden.

### Wie informiert Braze Kund:innen über Änderungen an Currents?

Wenn Änderungen an Currents vorgenommen werden (z. B. neue Event-Felder oder Event-Typen), sendet Braze eine E-Mail an alle Kund:innen mit aktiven Currents-Integrationen, die das Dashboard in den letzten 30 Tagen genutzt haben. Außerdem können Sie den [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/) für die neuesten Änderungen einsehen.

### Wie viel Speicherplatz benötige ich für Currents-Daten?

Der Speicherbedarf hängt von Ihrem Event-Volumen und den Typen der Events ab, die Sie exportieren. Braze stellt [Beispiel-Events im Avro-Format](https://github.com/braze-inc/currents-examples/tree/master/sample-data) bereit, mit denen Sie die Dateigrößen für Ihren Anwendungsfall schätzen können.

### Warum ist der Kampagnenname oder Canvas-Schrittname `NULL` in meinen Currents-Daten?

Wenn Sie eine neue Kampagne oder ein neues Canvas erstellen, kann es einige Zeit dauern, bis der Name in allen Braze-Systemen verfügbar ist. Events, die während dieses Zeitfensters über Currents gesendet werden, können `NULL` in den Namensfeldern enthalten (z. B. `campaign_name` oder `canvas_step_name`). Dies ist auch zu erwarten, wenn der Name kurz vor der Protokollierung der Events geändert wurde. Um dies zu vermeiden, warten Sie nach dem Erstellen oder Umbenennen einer Kampagne oder eines Canvas-Schritts etwas ab, bevor Sie senden.

### Was passiert, wenn mein Speicher-Bucket nicht verfügbar ist, wenn Currents versucht, Daten zu schreiben?

Wenn Ihr Speicher-Bucket zum Zeitpunkt der Datenübertragung nicht verfügbar ist, gehen diese Daten verloren. Braze kann Events, die nicht erfolgreich zugestellt wurden, nicht nachträglich auffüllen. Um Datenverlust zu vermeiden, stellen Sie sicher, dass Ihr Speicher-Bucket jederzeit verfügbar und korrekt konfiguriert ist.

### Warum wird die Meldung „You do not have any remaining Customer Behavior Events entitlements“ angezeigt, wenn ich meine Currents-Integration bearbeite?

Diese Meldung kann erscheinen, wenn Sie eine bestehende Currents-Integration aktualisieren und Ihr Workspace das Kontingent für Kundenverhalten-Events erreicht hat. Kontaktieren Sie Ihren Braze Account Manager, um ein zusätzliches Kontingent anzufordern oder Ihre Konfiguration anzupassen.

### Wie oft ändert sich die Currents-Version im Speicherpfad?

Das Segment `version=<currents_version>` im Speicherpfad wird mit jedem Currents-Release in einem monatlichen Rhythmus aktualisiert (z. B. von `version=6` auf `version=7`). Wir empfehlen, Dateien rekursiv vom Stammpfad aus zu lesen, anstatt ein bestimmtes Versionssegment fest zu codieren, damit Ihre Pipeline nach einer Versionsänderung automatisch die neuen Daten erfasst. Weitere Informationen zum Pfadformat finden Sie unter [Event-Zustellungssemantik]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/). Eine Übersicht der Änderungen nach Version finden Sie im [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/).

### Warum fehlen `campaign_id` oder `canvas_id` in einem Nachrichten-Engagement-Event?

Je nach Event-Typ und Kontext ist ein Nachrichten-Engagement-Event möglicherweise nicht mit einer bestimmten Kampagne oder einem bestimmten Canvas-Schritt verknüpft. In diesen Fällen können `campaign_id`, `canvas_id` und zugehörige Namensfelder im Event-Payload fehlen. Wenn Sie diese Felder bei einem bestimmten Event nicht sehen, prüfen Sie, ob dieser Event-Typ und Kontext normalerweise Kampagnen- oder Canvas-Bezeichner enthalten.