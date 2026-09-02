---
nav_title: Tangerine
article_title: Tangerine
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Tangerine Store360, einer Omnichannel-Plattform, die physische Geschäfte mit Online-Shops verbindet, um Verbraucher:innen und Mitarbeiter:innen in den Geschäften ein besseres Erlebnis zu bieten. Durch diese Integration sind die Rohdaten der Campaigns und Impressionen von Braze über Snowflake Secure Data Sharing auf Store360 verfügbar, und Marken können messen, wie sich ihre Campaigns auf das Engagement im Laden und die Besucherzahlen im Shop auswirken."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine entwickelt, baut und betreibt eine Omnichannel-Plattform namens Store360. Store360 ist eine Omnichannel-Enablement-Plattform, die physische Läden mit Online-Shops verbindet, um das Erlebnis für Verbraucher:innen und Mitarbeiter:innen in den Läden zu verbessern. Store360 verfolgt und analysiert den Besuchsverkehr in physischen Läden, einschließlich der Nutzer:innen mobiler Apps von Einzelhändlern und deren Engagement in den Läden.

Die Integration von Braze und Tangerine erlaubt es Ihnen, rohe Campaign- und Impressionsdaten von Braze über Snowflake Secure Data Sharing in Store360 zu integrieren. Marken können jetzt die Auswirkungen dieser Campaigns auf die Besuche in den Geschäften und das Engagement in den Geschäften messen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Store360-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Store360-Konto. |
| Braze-Konto-ID | Ihre Braze-App-Gruppen-ID. |
| Übereinstimmende Nutzer-IDs | Ihre Kundendaten in Store360 und Braze müssen übereinstimmende Nutzer-IDs auf beiden Plattformen haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

### Auswirkungen von Campaigns auf den Besuch physischer Geschäfte analysieren {#analyze-campaign-impact-on-physical-store-visit}

Marken nutzen Braze, um Campaign-Nachrichten an Verbraucher:innen zu senden, um die Zahl der Besuche im Shop zu erhöhen. Während der Campaign erfasst Store360 die Besuche von Nutzer:innen einer mobilen App, die durch ihre Nutzer-ID identifiziert werden.

Mit den Analysefunktionen von Store360 Insight können Marken die Wirkung von Campaigns im Detail visualisieren – von gesendeten und gelesenen Nachrichten (Daten von Braze) bis hin zu der Frage, wer und wie viele Empfänger:innen physische Shops besucht haben (Daten von Store360).

## Integration

### 1. Schritt: Snowflake Secure Data Share aktivieren {#step-1-enable-snowflake-secure-data-share}

Arbeiten Sie mit Ihrem Braze-Team zusammen, um Snowflake Secure Data Share zu aktivieren und zu konfigurieren.

### 2. Schritt: Store360 für den Abruf von Braze-Daten konfigurieren {#step-2-configure-store360-to-get-braze-data}

Konfigurieren Sie die ID Ihrer Braze-App-Gruppe für Ihr Store360-Dienstkonto über die Webkonsole des Store360-Admin-Managers. Dadurch wird beim Tangerine-Admin-Team die Synchronisierung der Braze-Daten mit Store360 über Snowflake Data Sharing angefragt.

### 3. Schritt: Store360 SDKs in die mobile App integrieren {#step-3-integrate-store360-sdks-to-mobile-app}

Um die Besuche von Nutzer:innen im Shop und die Aktivitäten im Laden zusammen mit den Braze-Campaign- und Impressionsdaten zu verfolgen und zu analysieren, müssen Sie das Store360 SDK or Software-Development-Kit in Ihre mobile App integrieren. Gehen Sie dazu wie in der Dokumentation zur Store360-SDK or Software-Development-Kit-Installation beschrieben vor. Diese Dokumentation wird Ihnen nach Unterzeichnung eines Client-Vertrags mit Tangerine Store 360 zur Verfügung gestellt.

## Braze-Daten in Store360 analysieren {#analyze-braze-data-in-store360}

Nutzen Sie die Vorteile der sicheren Datenfreigabe von Snowflake, um Ihre Braze-Rohdaten zu Campaigns und Impressionen mit Store360 Insight Analytics auszutauschen. So erhalten Sie ein vollständiges Bild des Lebenszyklus und der Aktivitäten der Nutzer:innen – von online bis offline.

Als Referenz finden Sie hier alle [Braze-Felder](/docs/assets/download_file/data-sharing-raw-table-schemas.txt), die in Store360 Analytics integriert werden können. Die Details dieses Schrittes sind sehr kundenspezifisch und erfordern spezielle Konfigurationen. Sprechen Sie mit Ihrem Store360 Account Manager:in oder wenden Sie sich an support@tangerine.io, um mehr zu erfahren.

## Wichtige Informationen und Einschränkungen {#important-information-and-limitations}

### Verfügbarkeit des Dienstes {#service-availability}

Derzeit ist der Dienst Store360 in Japan und Indonesien kommerziell verfügbar.

Tangerine plant die Einführung eines Store360-Produkts in den folgenden Ländern im Jahr 2023.
- Vereinigte Staaten von Amerika
- Thailand
- Singapur
- Vietnam
- Korea

### Datenaufbewahrung {#data-retention}

Für die Datenfreigabe über Snowflake gilt eine Aufbewahrungsrichtlinie von zwei Jahren für Ihre Braze-Daten.

### Zeitverzögerung beim Befüllen von Braze-Ereignisdaten {#time-lag-in-populating-braze-event-data}

Braze-Ereignisse werden mit Streaming-Technologie verarbeitet und sind nahezu in Realtime verfügbar. In der Regel sind die Ereignisse innerhalb von 30 Minuten nach ihrem Eintreten verfügbar.