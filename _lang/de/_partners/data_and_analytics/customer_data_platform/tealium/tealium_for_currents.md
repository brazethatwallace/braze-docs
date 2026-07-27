---
nav_title: Tealium für Currents
article_title: Tealium für Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Tealium, einer Customer Data Platform (CDP), die Informationen zwischen Quellen in Ihrem Marketing Stack sammelt und weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium für Currents {#tealium-for-currents}

> [Tealium](https://www.tealium.com) ist eine Customer Data Platform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Orte in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und Tealium erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit Currents können Sie auch Daten mit Tealium verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tealium EventStream oder Tealium AudienceStream | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Tealium-Konto](https://my.tealiumiq.com/). |
| Currents | Um Daten zurück nach Tealium zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| Tealium-URL | Diese erhalten Sie, indem Sie zu Ihrem Tealium-Dashboard navigieren und die Ingestion-URL kopieren.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Erstellen Sie eine Datenquelle für Braze in Tealium {#step-1-create-a-data-source-for-braze-within-tealium}

Eine Anleitung zur Erstellung einer Datenquelle finden Sie auf der [Tealium-Website](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Wenn Sie fertig sind, stellt Tealium eine URL der Datenquelle zum Kopieren bereit, die Sie im nächsten Schritt verwenden werden.

### 2. Schritt: Current erstellen {#step-2-create-current}

Navigieren Sie in Braze zu **Currents** > **+ Create Current** > **Tealium-Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail und Ihre Tealium-URL an.

Wählen Sie dann aus der Liste der verfügbaren Ereignisse aus, was Sie tracken möchten. Standardmäßig enthalten alle an Tealium gesendeten Ereignisse die `external_user_id` der Nutzer:innen. Sie können jedoch das Kontrollkästchen **Include events from anonymous users** aktivieren, um auch Ereignisse ohne `external_user_id` an Tealium zu senden.

Nachdem Sie Ihre Integration eingerichtet haben, wählen Sie **Launch Current**.

{% alert important %}
Es ist wichtig, dass Sie Ihre Tealium-URL auf dem neuesten Stand halten. Wenn die URL Ihres Konnektors falsch ist, kann Braze keine Ereignisse senden. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Ereignisse des Konnektors verworfen und die Daten gehen dauerhaft verloren.
{% endalert %}

## Details zur Integration {#integration-details}

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) aufgeführt sind (einschließlich aller Eigenschaften in [Messaging-Engagement-]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) und [Kundenverhalten-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)), nach Tealium.

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.