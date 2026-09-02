---
nav_title: Segment für Currents
article_title: Segment für Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Segment, einer Customer Data Platform, die Informationen zwischen Quellen in Ihrem Marketing-Stack sammelt und weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment für Currents {#segment-for-currents}

> [Segment](https://segment.com) ist eine Customer Data Platform, mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. Dieser Referenzartikel gibt eine Übersicht über die Verbindung zwischen Braze-Currents und Segment und beschreibt die Anforderungen und Prozesse für die korrekte Implementierung und Nutzung.

Die Integration von Braze und Segment ermöglicht es Ihnen, Braze-Currents zu nutzen, um Ihre Braze-Events nach Segment zu exportieren und so tiefgreifendere Analytics zu Conversions, Bindung und Produktnutzung zu erzielen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segment-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Braze-Ziel | Sie müssen [Braze bereits als Ziel eingerichtet]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) haben in Ihrer Segment-Integration.<br><br>Dazu gehört die Angabe des richtigen Braze-Rechenzentrums und des Representational State Transfer-API-Schlüssels in Ihren [Verbindungseinstellungen]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment#connection-settings). |
| Currents | Um Daten zurück nach Segment zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Segment-Schreibschlüssel abrufen {#step-1-obtain-segment-write-key}

Wählen Sie in Ihrem Segment-Dashboard Ihre Segment-Quelle aus. Gehen Sie dann zu **Settings > API keys**. Hier finden Sie den **Segment Write Key**.

{% alert warning %}
Es ist wichtig, dass Sie Ihren Segment-Schreibschlüssel auf dem neuesten Stand halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Events mehr senden. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Events des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

### 2. Schritt: Neuen Currents-Konnektor erstellen {#step-2-create-a-new-currents-connector}

1. Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Klicken Sie auf **+ Create New Current** > **Segment Data Export**.
3. Geben Sie anschließend den Integrationsnamen, die Kontakt-E-Mail, den Segment-Schreibschlüssel und die Segment-Region an.

![Die Segment-Currents-Seite in Braze. Hier finden Sie Felder für den Integrationsnamen, die Kontakt-E-Mail, die Segment-Region und den API-Schlüssel.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### 3. Schritt: Nachrichten-Engagement-Events exportieren {#step-3-export-message-engagement-events}

Wählen Sie als Nächstes die Nachrichten-Engagement-Events aus, die Sie exportieren möchten. Beachten Sie die nachfolgend aufgelistete Tabelle der Export-Events und Eigenschaften. Alle an Segment gesendeten Events enthalten die `external_user_id` der Nutzer:innen als `userId` und die `braze_id` der Nutzer:innen als `anonymousId`.

Beachten Sie, dass Braze nur dann Event-Daten für Nutzer:innen ohne `external_user_id` sendet, wenn die Option **Include events from anonymous users** aktiviert ist.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Anonymous user export' %}

![Liste aller verfügbaren Nachrichten-Engagement-Events auf der Segment-Currents-Seite in Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Wählen Sie abschließend **Launch Current**.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

Weitere Informationen finden Sie in der Segment-[Dokumentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/).

## Ihren Current Update or aktualisieren or aktualisieren {#updating-your-current}

{% multi_lang_include currents/updating_currents.md %}

## Unterstützte Currents-Events {#supported-currents-events}

Braze unterstützt den Export der folgenden Events nach Segment:

- [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Für die Payload-Struktur jedes Events wählen Sie den Tab **Segment** im [Glossar der Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und im [Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).