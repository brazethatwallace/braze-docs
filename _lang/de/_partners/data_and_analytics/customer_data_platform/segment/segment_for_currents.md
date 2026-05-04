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

Die Integration von Braze und Segment ermöglicht es Ihnen, Braze-Currents zu nutzen, um Ihre Braze-Ereignisse nach Segment zu exportieren und so tiefgreifendere Analytics zu Conversions, Bindung und Produktnutzung zu erzielen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segment-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Braze-Ziel | Sie müssen [Braze bereits als Ziel eingerichtet]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) haben in Ihrer Segment-Integration.<br><br>Dazu gehört die Angabe des richtigen Braze-Rechenzentrums und des REST-API-Schlüssels in Ihren [Verbindungseinstellungen]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Um Daten zurück nach Segment zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Segment-Schreibschlüssel abrufen {#step-1-obtain-segment-write-key}

Wählen Sie in Ihrem Segment-Dashboard Ihre Segment-Quelle aus. Gehen Sie dann zu **Settings > API keys**. Hier finden Sie den **Segment Write Key**.

{% alert warning %}
Es ist wichtig, dass Sie Ihren Segment-Schreibschlüssel auf dem neuesten Stand halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Ereignisse mehr senden. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

### 2. Schritt: Neuen Currents-Konnektor erstellen {#step-2-create-a-new-currents-connector}

1. Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Klicken Sie auf **+ Create New Current** > **Segment Data Export**.
3. Geben Sie anschließend den Integrationsnamen, die Kontakt-E-Mail, den Segment-Schreibschlüssel und die Segment-Region an.

![Die Segment-Currents-Seite in Braze. Hier finden Sie Felder für den Integrationsnamen, die Kontakt-E-Mail, die Segment-Region und den API-Schlüssel.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### 3. Schritt: Nachrichten-Engagement-Ereignisse exportieren {#step-3-export-message-engagement-events}

Wählen Sie als Nächstes die Nachrichten-Engagement-Ereignisse aus, die Sie exportieren möchten. Beachten Sie die nachfolgend aufgelistete Tabelle der Exportereignisse und Eigenschaften. Alle an Segment gesendeten Ereignisse enthalten die `external_user_id` der Nutzer:innen als `userId` und die `braze_id` der Nutzer:innen als `anonymousId`.

Beachten Sie, dass Braze nur dann Ereignisdaten für Nutzer:innen ohne `external_user_id` sendet, wenn die Option **Ereignisse von anonymen Nutzer:innen einbeziehen** aktiviert ist.

{% multi_lang_include early_access_beta_alert.md feature='Anonymous user export' %}

![Liste aller verfügbaren Nachrichten-Engagement-Ereignisse auf der Segment-Currents-Seite in Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Wählen Sie abschließend **Launch Current**.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

Weitere Informationen finden Sie in der Segment-[Dokumentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/).

## Ihren Current aktualisieren {#updating-your-current}

{% multi_lang_include updating_currents.md %}

## Unterstützte Currents-Ereignisse {#supported-currents-events}

Braze unterstützt den Export der folgenden Daten, die in den Currents-Glossaren für [Nutzer:innen-Verhalten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) und [Nachrichten-Engagement]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach Segment:

### Verhaltensweisen {#behaviors}
- Deinstallation: `users.behaviors.Uninstall`
- Abo (globale Statusänderung): `users.behaviors.subscription.GlobalStateChange`
- Abo-Gruppe (Statusänderung): `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- Abbruch: `users_campaigns_abort`
- Conversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`

### Canvas
- Abbruch: `users_canvas_abort`
- Conversion: `users.canvas.Conversion`
- Eingang: `users.canvas.Entry`
- Exit (übereinstimmende Zielgruppe, ausgeführtes Ereignis)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Experiment-Schritt (Conversion, aufgeteilter Eingang)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Nachrichten {#messages}
- Content-Card (Abbruch, Klick, Schließen, Impression, Senden)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-Mail (Abbruch, Bounce, Klick, Zustellung, als Spam markieren, Öffnung, Senden, Soft-Bounce, Abmeldung)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- In-App-Nachricht (Abbruch, Klick, Impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Push-Benachrichtigung (Abbruch, Bounce, iOS-Vordergrund, Öffnung, Senden)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (Abbruch, Carrier-Versand, Zustellung, Zustellungsfehler, eingehender Empfang, Ablehnung, Senden, Kurzlink-Klick)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (Abbruch, Senden)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (Abbruch, Zustellung, Fehler, eingehender Empfang, Gelesen, Senden)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`