---
nav_title: Berichte und Insights
article_title: Berichte und Insights
description: "Erfahren Sie, wie Sie Berichte aus dem BrazeAI Decisioning Studio™ in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Campaigns beeinflussen."
page_order: 6
---

# Berichte und Insights {#reports-and-insights}

> Erfahren Sie, wie Sie Berichte aus dem BrazeAI Decisioning Studio™ in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Campaigns beeinflussen. Von Performance-Metriken über Datenintegrität bis hin zu Systemänderungen – diese Berichte helfen Ihnen, Ergebnisse zu verstehen, Probleme zu beheben und fundierte Entscheidungen mit Zuversicht zu treffen.

## Voraussetzungen {#prerequisites}

Bevor Sie Decisioning-Studio-Berichte in Braze einsehen können, müssen Sie:

- Einen aktiven Vertrag für Braze und BrazeAI Decisioning Studio™ haben.
- Ihren CSM kontaktieren, um BrazeAI Decisioning Studio™ für Sie aktivieren zu lassen.
- Einen aktiven BrazeAI Decisioning Studio™ Agenten haben.

## Berichte anzeigen {#view}

Um die Metriken für einen Decisioning Studio-Agenten in Braze anzuzeigen, navigieren Sie zu **AI Decisioning** > **BrazeAI Decisioning Studio™** und wählen Sie anschließend einen Agenten aus.

Hier können Sie Berichte wie Performance, Insights, Diagnosen und Zeitleisten einsehen. Weitere Einzelheiten finden Sie unter [Verfügbare Berichte](#available-reports).

## Berichtsdaten ändern {#change-report-dates}

Nachdem Sie [einen Bericht geöffnet haben](#view), können Sie den Datumsbereich ändern, indem Sie ein neues Start- und Enddatum aus dem Kalender-Dropdown auswählen.

![BrazeAI Decisioning Studio™ Datumsbereichsauswahl mit geöffnetem Kalender-Dropdown. Der Kalender zeigt auswählbare Start- und Enddaten zur Anpassung der Berichtsansicht.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Sie können auch ein Standard-Startdatum festlegen oder Daten auswählen, die immer ausgeschlossen werden sollen. Ausgeschlossene Daten werden aus allen Berichten für diesen Agenten herausgefiltert.

Um Daten festzulegen oder auszuschließen, wählen Sie <i class="fa-solid fa-gear" aria-label="Einstellungen"></i> **Settings** und ändern Sie dann Ihr Standarddatum oder schließen Sie Daten nach Bedarf aus.

![Geöffnetes Settings-Panel in BrazeAI Decisioning Studio™ mit Optionen zum Festlegen eines Standard-Startdatums und zum Ausschließen bestimmter Daten aus Berichten. Das Panel zeigt zwei Abschnitte mit den Bezeichnungen „Default start date“ und „Exclude dates“. Unter „Exclude dates“ sind mehrere Daten mit Kontrollkästchen aufgelistet.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Verfügbare Berichte {#available-reports}

- [Performance]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance): Übergeordnete Agenten-Metriken, die Behandlungsgruppen mit Kontrollgruppen vergleichen, mit den Ansichten **Trending** und **Driver Tree**.
- [Insights]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights): Wie Empfehlungsoptionen in Ihrer Aktionsbank generiert werden, einschließlich Agentenpräferenzen und SHAPs-Berichten.
- [Diagnosen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics): Datenintegrität für ausgehende und eingehende Daten, einschließlich Empfehlungsvolumen und Daten-Feed-Überwachung.
- [Zeitleiste]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline): Eine visuelle Aufzeichnung wichtiger Ereignisse (Agent-Ausführungen, Konfigurationsänderungen, Updates der Sicherheitsvorkehrungen) zusammen mit Performance-Metriken.