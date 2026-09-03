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

> Richten Sie in Ihren [E-Mail-Präferenzen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) einen Bot-Filter ein, um alle mutmaßlichen Maschinen- oder Bot-Klicks auszuschließen. Ein „Bot-Klick“ in E-Mails bezieht sich auf einen Klick auf Hyperlinks innerhalb einer E-Mail, der von einem automatisierten Programm generiert wurde. Indem Sie diese Bot-Klicks filtern, können Sie Nachrichten gezielt triggern und an Empfänger:innen zustellen, die engagiert sind.

{% alert important %}
Ab dem 9. Juli 2025 wird für alle neu erstellten Workspaces die Bot-Filter-Einstellung aktiviert sein, um eine genauere Berichterstattung über Klicks in Braze zu ermöglichen.
{% endalert %}

## Über Bot-Klicks {#about-bot-clicks}

Braze verfügt über ein Erkennungssystem, das mehrere Eingaben verwendet, um verdächtige Bot-Klicks zu identifizieren, die auch als nicht-menschliche Interaktionen (NHI) bezeichnet werden. Bot-Klicks können Ihre E-Mail-Engagement-Metriken verzerren, indem sie Klickraten künstlich aufblähen. Dieser Ansatz ermöglicht es uns, zwischen echten menschlichen Interaktionen und verdächtigen Bot-Aktivitäten zu unterscheiden, um die Integrität der Klick-Engagement-Metriken und Insights zu wahren.

## Von Bot-Klicks betroffene Metriken {#metrics-affected-by-bot-clicks}

{% alert note %}
Die Bot-Filterung blockiert aktiv verdächtige automatisierte Klicks, um die Genauigkeit Ihrer Engagement-Metriken zu verbessern. Da sich Scanner und Bots jedoch ständig weiterentwickeln, kann Braze nicht garantieren, dass alle nicht-menschlichen Interaktionen entfernt werden.
{% endalert %}

Die folgenden Braze-Metriken können von Bot-Klicks betroffen sein:

- Gesamtklickrate
- Eindeutige Klickrate
- Klick-zu-Öffnungsrate
- Konversionsrate (wenn „Klicks auf Campaign“ als Konversions-Event ausgewählt ist)
- Heatmap
- Bestimmte Segment-Filter

Wenn die Bot-Filterung aktiviert ist, werden verdächtige Bot-Klicks aus den Klickdaten ausgeschlossen. Die folgenden [Braze-Intelligence-Features]({{site.baseurl}}/user_guide/brazeai/intelligence_suite) können infolgedessen geringere klickbezogene Volumen aufweisen:

- Intelligenter Kanal
- Intelligentes Timing
- Experiment-Schritt
    - Winning Path
- Geschätzte reale Öffnungsrate

[Mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) kann ebenfalls geringere klickbezogene Volumen aufweisen, wenn Sie für ein klickbasiertes Ziel optimieren.

Abmeldungen durch verdächtige Bot-Klicks sind davon nicht betroffen. Braze verarbeitet weiterhin alle Abmeldeanfragen wie gewohnt. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="blocking unsubscribes from suspected bot clicks" %}

## Segmentierungsfilter, die von der Bot-Filterung betroffen sind {#segmentation-filters-affected-by-bot-filtering}

Die folgenden [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) können von der Bot-Filterung für E-Mail-Nachrichten betroffen sein:

- [Clicked/Opened Campaign or Canvas With Tag]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Clicked/Opened Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-opened-step)
- [Clicked Alias in Campaign]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-campaign)
- [Clicked Alias in Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Clicked Alias in Any Campaign or Canvas Step]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Last Engaged with Message]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#last-engaged-with-message)
- [Intelligent Channel]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#intelligent-channel)

## Bot-Filterung aktivieren {#turning-on-bot-filtering}

Gehen Sie zu **Einstellungen** > **E-Mail-Einstellungen**. Wählen Sie dann **Bot-Klicks entfernen** aus. Diese Einstellung wird auf Workspace-Ebene angewendet.

Verdächtige Bot-Klicks werden erst entfernt, nachdem die Einstellung aktiviert wurde, und gelten nicht rückwirkend für Metriken in Ihrem Workspace.

![Bot-Filterung-E-Mail-Einstellung in den E-Mail-Einstellungen aktiviert.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Wenn Sie diese Einstellung aktivieren und später wieder deaktivieren, kann Braze zuvor entfernte Bot-Aktivitäten nicht in Ihren Analytics wiederherstellen.
{% endalert %}

## Felder in E-Mail-Klick-Events für Currents und Snowflake {#fields-in-email-click-events-for-currents-and-snowflake}

Braze sendet die Felder `is_suspected_bot_click` und `suspected_bot_click_reason` in Currents und Snowflake für ein E-Mail-Klick-Event.

| Feld | Datentyp | Beschreibung |
| `is_suspected_bot_click` | Boolean | Gibt an, dass es sich um einen vermuteten Bot-Klick handelt. Dieses Feld wird als Null-Werte gesendet, bis Sie die Workspace-Einstellung **Bot-Klicks entfernen** aktivieren. Dieser Ansatz ermöglicht es Ihnen, programmatisch nachzuvollziehen, wann die Filterung vermuteter Bot-Klicks in Ihrem Workspace begonnen hat, sodass Sie dies genau mit den Daten in Currents und Snowflake vergleichen können. |
| `suspected_bot_click_reason` | Array | Gibt den Grund an, warum es sich um einen vermuteten Bot-Klick handelt. Dieses Feld wird mit Werten wie `user_agent` und `ip_address` befüllt, auch wenn die Workspace-Einstellung für die Bot-Filterung deaktiviert ist. Dieses Feld kann Insights über die potenziellen Auswirkungen der Aktivierung dieser Einstellung liefern, indem die Anzahl der Klicks aus vermuteten Bot-Klicks mit menschlichen Interaktionen verglichen wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Felder in E-Mail-Klick-Events für Currents und Snowflake" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie wirkt sich die Bot-Filterung auf die Performance meiner Campaign aus? {#how-will-bot-filtering-impact-my-campaigns-performance}

Dies hat keine Auswirkungen auf die Metriken bereits gesendeter Campaigns. Wenn die Bot-Filterung in Ihrem Workspace aktiviert ist, beginnt Braze, vermutete Bot-Klicks aus allen Klicks herauszufiltern. Möglicherweise bemerken Sie einen Rückgang der Klickraten, aber die Klickrate ist dann eine genauere Darstellung des Engagements Ihrer Nutzer:innen mit ihren E-Mail-Nachrichten.

### Verhindert die Bot-Filterung, dass Bots, die auf den Braze-Abmeldelink klicken, sich abmelden? {#will-bot-filtering-prevent-bots-clicking-on-the-braze-unsubscribe-link-from-unsubscribing}

Nein. Alle Abmeldeanfragen werden weiterhin verarbeitet.

### Werden maschinelle Öffnungen bei der Bot-Klick-Filterung berücksichtigt? {#are-machine-opens-considered-in-the-bot-click-filtering}

Nein.