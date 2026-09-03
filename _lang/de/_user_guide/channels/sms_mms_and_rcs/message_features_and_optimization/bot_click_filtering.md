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

## So funktioniert es {#how-it-works}

Braze verfügt über ein proprietäres Erkennungssystem, das mehrere Eingaben nutzt, um verdächtige Bot-Klicks zu identifizieren, die auch als nicht-menschliche Interaktionen (NHI) bezeichnet werden. Bot-Klicks können Klickraten künstlich erhöhen und so Engagement-Metriken verfälschen. Durch deren Filterung ermöglicht Braze die Erfassung zuverlässiger Daten für die Entscheidungsfindung.

Unser System analysiert User Agents, die mit Web-Crawlern, Android- und iOS-Link-Vorschauen oder CPaaS-Sicherheitssoftware verknüpft sind. Einige Beispiele für gefilterte User Agents sind `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3` und `Barracuda Sentinel (EE)`.

## Betroffene Metriken und Workflows {#affected-metrics-and-workflows}

Die folgenden Braze-Metriken und Workflows sind von Bot-Klicks betroffen:

- **_Gesamtklicks:_** Campaign-Analytics und Canvas-Analytics schließen Bot-Klicks aus und spiegeln nur menschliche Interaktionen wider.
- **Segmentierungsfilter:** Segment-Filter, die sich auf SMS-Link-Interaktionen beziehen, schließen Bot-Klicks aus, um ein genaueres Retargeting in Campaigns und Canvases zu ermöglichen.
- **Orchestrierung:** Bot-Klicks werden aus aktionsbasierten Triggern und Canvas-Aktionspfaden herausgefiltert, die sich auf SMS-Link-Interaktionen beziehen, sodass Trigger menschliches Verhalten widerspiegeln.
- **Braze Intelligence:**
    - **Optimieren mit BrazeAI<sup>TM</sup>:** Schließt Bot-Klicks bei der Optimierung der Variantenauswahl aus.
    - **Intelligenter Kanal:** Schließt Bot-Klicks aus, wenn SMS oder RCS für eine präzise Kanalauswahl ausgewählt wird.
    - **Experiment-Schritte:** Schließt Bot-Klicks für zuverlässige Experiment-Ergebnisse aus.
    - **Currents-Datenexporte:** Enthält die Felder `is_suspected_bot_click` und `suspected_bot_click_reason`, um die Analyse von menschlichen Klicks im Vergleich zu Bot-Klicks zu unterstützen. Diese Felder sind in [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) und [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) verfügbar.

Abmeldungen durch verdächtige Bot-Klicks sind nicht betroffen. Braze verarbeitet alle Abmeldeanfragen wie gewohnt. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Currents-Felder in SMS-Klickereignissen {#currents-fields-in-sms-click-events}

Braze enthält die folgenden Currents-Felder für SMS-Klickereignisse:

| Feld | Datentyp | Beschreibung |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolean | Gibt an, ob es sich bei dem Klick um einen vermuteten Bot-Klick handelt. Bei SMS- und RCS-Kurzlink-Klicks wertet Braze die Bot-Erkennung bei jedem Klick aus und befüllt dieses Feld mit `true` oder `false`. |
| `suspected_bot_click_reason` | String, Array | Gibt den Grund für einen vermuteten Bot-Klick an (z. B. `user_agent`). Wird befüllt, wenn die Bot-Erkennung für SMS- und RCS-Kurzlink-Klicks ausgeführt wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Currents-Felder in SMS-Klickereignissen" }

## Query Builder-Template {#query-builder-template}

Für Hilfe bei der Analyse Ihrer Daten können Sie das vorgefertigte mobile Template **SMS-Klick-Ereignisse durch Bots** im [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) verwenden.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie wirkt sich die Bot-Klick-Filterung auf die Campaign-Performance aus? {#how-does-bot-click-filtering-impact-campaign-performance}

Die Bot-Klick-Filterung wird automatisch für verkürzte Links in SMS und RCS ausgeführt. Die Klickraten im Dashboard schließen vermutete Bot-Klicks aus, sodass die angezeigten Raten menschliche Interaktionen widerspiegeln und nicht automatisierte Link-Vorschauen oder Crawler-Traffic.

### Verhindert die Bot-Klick-Filterung, dass Bots auf Abmelde-Links klicken? {#does-bot-click-filtering-prevent-bots-from-clicking-unsubscribe-links}

Nein. Alle Abmeldeanfragen werden wie gewohnt verarbeitet.

### Sind Link-Vorschauen in der Bot-Klick-Filterung enthalten? {#are-link-previews-included-in-bot-click-filtering}

Ja. Link-Vorschauen (z. B. Link-Vorschauen von Android und iOS) werden als Bot-Klicks gekennzeichnet und herausgefiltert.