---
nav_title: "Bot-Klick-Filterung"
article_title: "SMS- und RCS-Bot-Klick-Filterung"
description: "Dieser Referenzartikel behandelt die Bot-Klick-Filterung für SMS und RCS."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 5
channel:
  - SMS
  - RCS
---

# SMS- und RCS-Bot-Klick-Filterung {#sms-and-rcs-bot-click-filtering}

> Die SMS- und RCS-Bot-Klick-Filterung verbessert Campaign-Analytics und Workflows, indem vermutete Bot-Klicks ausgeschlossen werden. Ein „Bot-Klick“ bezeichnet automatisierte Klicks auf gekürzte Links in SMS- und RCS-Nachrichten, beispielsweise durch Web-Crawler, Android- und iOS-Linkvorschauen oder CPaaS-Sicherheitssoftware. Dieses Feature ermöglicht präzises Reporting, Segmentierung und Orchestrierung, um echte Nutzer:innen anzusprechen. <br><br> Informationen zur Bot-Klick-Filterung für E-Mail-Campaigns finden Sie unter [Bot-Filterung für E-Mails]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering).

## Funktionsweise {#how-it-works}

Braze verfügt über ein proprietäres Erkennungssystem, das mehrere Eingaben nutzt, um vermutete Bot-Klicks zu identifizieren, auch bekannt als nicht-menschliche Interaktionen (NHI). Bot-Klicks können Klickraten aufblähen und Engagement-Metriken verzerren. Durch deren Filterung ermöglicht Braze die Erfassung zuverlässiger Daten für die Entscheidungsfindung.

Unser System analysiert User Agents, die mit Web-Crawlern, Android- und iOS-Linkvorschauen oder CPaaS-Sicherheitssoftware verknüpft sind. Einige Beispiele für gefilterte User Agents sind `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` und `Barracuda Sentinel (EE)`.

## Betroffene Metriken und Workflows {#affected-metrics-and-workflows}

Die folgenden Braze-Metriken und -Workflows werden durch Bot-Klicks beeinflusst:

- **_Gesamtklicks_:** Campaign-Analytics und Canvas-Analytics schließen Bot-Klicks aus und spiegeln nur menschliche Interaktionen wider.
- **Segmentierungsfilter:** Segmentfilter, die sich auf SMS-Link-Interaktionen beziehen, schließen Bot-Klicks für ein genaueres Retargeting in Campaigns und Canvases aus.
- **Orchestrierung:** Bot-Klicks werden aus aktionsbasierten Triggern und Canvas-Aktionspfaden gefiltert, die sich auf SMS-Link-Interaktionen beziehen, sodass Trigger menschliches Verhalten widerspiegeln.
- **Braze Intelligence:**
    - **Intelligente Auswahl:** Schließt Bot-Klicks bei der Optimierung der Variantenauswahl aus.
    - **Intelligenter Kanal:** Schließt Bot-Klicks aus, wenn SMS oder RCS für eine präzise Kanalauswahl ausgewählt wird.
    - **Experiment-Schritte:** Schließt Bot-Klicks für zuverlässige Experimentergebnisse aus.
    - **Currents-Datenexporte:** Enthält die Felder `is_suspected_bot_click` und `suspected_bot_click_reason`, um die Analyse von menschlichen gegenüber Bot-Klicks zu unterstützen. Diese Felder sind in [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) und [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) verfügbar.

Abmeldungen durch vermutete Bot-Klicks sind davon nicht betroffen. Braze verarbeitet alle Abmeldeanfragen wie gewohnt. Um diese Abmeldungen zu blockieren, [reichen Sie Produktfeedback ein]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Currents-Felder in SMS-Klick-Ereignissen {#currents-fields-in-sms-click-events}

Braze enthält die folgenden Currents-Felder für SMS-Klick-Ereignisse:

| Feld | Datentyp | Beschreibung |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolescher Wert | Gibt an, ob der Klick ein vermuteter Bot-Klick ist. Gibt `null` für alle Nutzer:innen zurück, bis die Bot-Klick-Filterung für Ihr Unternehmen aktiviert wird. Nach der Aktivierung wird das Feld für alle neuen Klicks mit `true` oder `false` befüllt. |
| `suspected_bot_click_reason` | String, Array | Gibt den Grund für einen vermuteten Bot-Klick an (z. B. `user_agent`). Wird auch befüllt, wenn die Filterung deaktiviert ist, und bietet Einblicke in potenzielle Bot-Aktivitäten. Dieses Feld ist global verfügbar und wird für alle Nutzer:innen mit einem Grund befüllt, auch wenn die Bot-Klick-Filterung noch nicht aktiviert ist. Dies bietet Einblicke in potenzielle Bot-Aktivitäten, bevor Sie die Bot-Klick-Filterung aktivieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Currents-Felder in SMS-Klick-Ereignissen" }

## Abfrage-Builder-Template {#query-builder-template}

Zur Unterstützung bei der Analyse Ihrer Daten können Sie das vorgefertigte Mobile-Template **SMS click events by bots** im [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) verwenden.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie wirkt sich die Bot-Klick-Filterung auf die Campaign-Performance aus? {#how-does-bot-click-filtering-impact-campaign-performance}

Die Filterung hat keinen Einfluss auf bereits gesendete Campaigns. Nach der Aktivierung reduziert sie die Klickraten ab diesem Zeitpunkt, indem Bot-Klicks ausgeschlossen werden.

### Verhindert die Bot-Klick-Filterung, dass Bots auf Abmeldelinks klicken? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

Nein. Alle Abmeldeanfragen werden wie gewohnt verarbeitet.

### Sind Linkvorschauen in der Bot-Klick-Filterung enthalten? {#are-link-previews-included-in-bot-click-filtering}

Ja. Linkvorschauen (z. B. Android- und iOS-Linkvorschauen) werden als Bot-Klicks gekennzeichnet und herausgefiltert.

### Wie aktiviere ich die Bot-Klick-Filterung? {#how-do-i-enable-bot-click-filtering}

Sie müssen Ihr Braze-Konto-Team kontaktieren, um die Bot-Klick-Filterung während des Early Access zu aktivieren. Wenn die Bot-Klick-Filterung allgemein verfügbar ist, wird das Feature standardmäßig für alle SMS- und RCS-Nutzer:innen aktiviert sein.

Stellen Sie außerdem sicher, dass Sie das erweiterte Klick-Tracking für die [Link-Kürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) aktiviert haben. Dadurch erhalten Sie die Bot-Klick-Analytics, da wir diese Daten auf der Ebene einzelner Nutzer:innen erfassen.

{% alert note %}
Für weitere Unterstützung [kontaktieren Sie den Support]({{site.baseurl}}/braze_support).
{% endalert %}