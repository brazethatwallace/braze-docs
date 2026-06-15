---
nav_title: Bot-Filter für E-Mails
article_title: Bot-Filter für E-Mails
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Dieser Artikel bietet eine Übersicht über Bot-Filter für E-Mails."
---

# Bot-Filter für E-Mails {#bot-filtering-for-emails}

> Richten Sie in Ihren [E-Mail-Präferenzen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/) einen Bot-Filter ein, um alle mutmaßlichen Maschinen- oder Bot-Klicks auszuschließen. Ein „Bot-Klick“ in E-Mails bezieht sich auf einen Klick auf Hyperlinks innerhalb einer E-Mail, der von einem automatisierten Programm generiert wurde. Indem Sie diese Bot-Klicks filtern, können Sie Nachrichten gezielt triggern und an Empfänger:innen zustellen, die engagiert sind.

{% alert important %}
Ab dem 9. Juli 2025 wird für alle neu erstellten Workspaces die Bot-Filter-Einstellung aktiviert sein, um eine genauere Berichterstattung über Klicks in Braze zu ermöglichen.
{% endalert %}

## Über Bot-Klicks {#about-bot-clicks}

Braze verfügt über ein Erkennungssystem, das mehrere Eingaben verwendet, um mutmaßliche Bot-Klicks zu identifizieren, die auch als nicht-menschliche Interaktionen (NHI) bezeichnet werden. Bot-Klicks können Ihre Metriken für das E-Mail-Engagement verzerren, indem sie die Klickraten künstlich aufblähen. Dieser Ansatz erlaubt es uns, zwischen echten menschlichen Interaktionen und vermuteten Bot-Aktivitäten zu unterscheiden, um die Integrität der Klick-Engagement-Metriken und Insights zu erhalten.

## Von Bot-Klicks betroffene Metriken {#metrics-affected-by-bot-clicks}

{% alert note %}
Bot-Filter blockieren aktiv mutmaßliche automatisierte Klicks, um die Genauigkeit Ihrer Engagement-Metriken zu verbessern. Scanner und Bots entwickeln sich jedoch ständig weiter, sodass Braze nicht garantieren kann, dass alle nicht-menschlichen Interaktionen entfernt werden.
{% endalert %}

Die folgenden Braze-Metriken können von Bot-Klicks betroffen sein:

- Gesamte Klickrate
- Eindeutige Klickrate
- Klick-zu-Öffnungs-Rate
- Konversionsrate (wenn „Klickt auf Campaign“ als Konversions-Event ausgewählt ist)
- Heatmap
- Bestimmte Segment-Filter

[Braze-Intelligence-Features]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/), die Klickdaten zusätzlich zu unseren Erkennungssystemen nutzen, können beeinträchtigt werden. Das Aktivieren der Einstellung kann unsere Erkennungssysteme vorübergehend stören, was zu einem Rückgang der Metrik oder des Eingabewerts führen kann, da mutmaßliche Bot-Klicks ausgeschlossen werden:

- Intelligente Auswahl
- Intelligenter Kanal
- Intelligentes Timing
- Experiment-Schritt
    - Winning Path
    - Personalized Path
- Campaign
    - Gewinnervariante
    - Personalisierte Variante
- Geschätzte reale Öffnungsrate

Abmeldungen durch mutmaßliche Bot-Klicks sind nicht betroffen. Braze verarbeitet weiterhin alle Abmeldeanfragen wie gewohnt. Wenn Sie möchten, dass Braze diese Abmeldungen blockiert, reichen Sie [Produktfeedback]({{site.baseurl}}/user_guide/administer/personal/product_portal/) ein.

## Von Bot-Filtern betroffene Segmentierungsfilter {#segmentation-filters-affected-by-bot-filtering}

Die folgenden [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) können durch Bot-Filter für E-Mail-Nachrichten betroffen sein:

- [Clicked/Opened Campaign or Canvas With Tag]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-opened-campaign-or-canvas-with-tag)
- [Clicked/Opened Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-opened-step)
- [Clicked Alias in Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-alias-in-campaign)
- [Clicked Alias in Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-alias-in-canvas-step)
- [Clicked Alias in Any Campaign or Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#clicked-alias-in-any-campaign-or-canvas-step)
- [Last Engaged with Message]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#last-engaged-with-message)
- [Intelligent Channel]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#intelligent-channel)

## Bot-Filter aktivieren {#turning-on-bot-filtering}

Gehen Sie zu **Einstellungen** > **E-Mail-Präferenzen**. Wählen Sie dann **Bot-Klicks entfernen** aus. Diese Einstellung wird auf Workspace-Ebene angewendet.

Mutmaßliche Bot-Klicks werden erst nach dem Aktivieren der Einstellung entfernt und nicht rückwirkend auf Metriken in Ihrem Workspace angewendet.

![Bot-Filter-E-Mail-Einstellung, die in den E-Mail-Präferenzen aktiviert ist.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Wenn Sie diese Einstellung aktivieren und später wieder deaktivieren, kann Braze zuvor entfernte Bot-Aktivitäten nicht in Ihren Analytics wiederherstellen.
{% endalert %}

## Felder in E-Mail-Klick-Events für Currents und Snowflake {#fields-in-email-click-events-for-currents-and-snowflake}

Braze sendet die Felder `is_suspected_bot_click` und `suspected_bot_click_reason` in Currents und Snowflake für ein E-Mail-Klick-Event.

| Feld | Datentyp | Beschreibung |
| `is_suspected_bot_click` | Boolescher Wert | Gibt an, dass es sich um einen mutmaßlichen Bot-Klick handelt. Dieses Feld sendet Null-Werte, bis Sie die Workspace-Einstellung **Bot-Klicks entfernen** aktivieren. Dieser Ansatz ermöglicht es Ihnen, programmatisch nachzuvollziehen, wann die Filterung mutmaßlicher Bot-Klicks in Ihrem Workspace begonnen hat, damit Sie dies genau mit den Daten in Currents und Snowflake vergleichen können. |
| `suspected_bot_click_reason` | Array | Gibt den Grund an, warum es sich um einen mutmaßlichen Bot-Klick handelt. Dieses Feld wird mit Werten wie `user_agent` und `ip_address` befüllt, auch wenn die Bot-Filter-Workspace-Einstellung deaktiviert ist. Dieses Feld kann Insights in die potenziellen Auswirkungen der Aktivierung dieser Einstellung geben, indem die Anzahl der Klicks aus mutmaßlichen Bot-Klicks mit menschlichen Interaktionen verglichen wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Felder in E-Mail-Klick-Events für Currents und Snowflake" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie wirkt sich der Bot-Filter auf die Performance meiner Campaign aus? {#how-will-bot-filtering-impact-my-campaigns-performance}

Dies hat keine Auswirkungen auf Metriken für bereits gesendete Campaigns. Wenn der Bot-Filter in Ihrem Workspace aktiviert ist, beginnt Braze, mutmaßliche Bot-Klicks aus allen Klicks herauszufiltern. Möglicherweise bemerken Sie einen Rückgang der Klickraten, aber die Klickrate ist dann eine genauere Darstellung des Engagements Ihrer Nutzer:innen mit ihren E-Mail-Nachrichten.

### Verhindert der Bot-Filter, dass Bots, die auf den Braze-Abmeldelink klicken, Abmeldungen auslösen? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

Nein. Alle Abmeldeanfragen werden weiterhin verarbeitet.

### Werden maschinelle Öffnungen beim Bot-Klick-Filter berücksichtigt? {#are-machine-opens-considered-in-the-bot-click-filtering}

Nein.