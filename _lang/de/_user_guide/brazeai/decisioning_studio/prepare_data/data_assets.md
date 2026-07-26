---
nav_title: Kritische Datenressourcen
article_title: Kritische Datenressourcen für Decisioning Studio
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt die erforderlichen und optionalen Datenressourcen für BrazeAI Decisioning Studio, einschließlich der Feedback-Daten, die zum Schließen der KI-Entscheidungsschleife benötigt werden."
---

# Kritische Datenressourcen {#critical-data-assets}

> Decisioning Studio benötigt bestimmte Datenressourcen, um zu funktionieren, und profitiert von zusätzlichen optionalen Daten. Dieser Artikel beschreibt, was jede Ressource ist, warum sie wichtig ist und welche Felder erforderlich sind.

## Die KI-Entscheidungsschleife schließen {#close-the-ai-decisioning-loop}

Die drei erforderlichen Ereignis-Ressourcen (Aktivierungen, Engagements und Conversions) bilden zusammen die Feedback-Schleife, die es Decisioning Studio ermöglicht, im Laufe der Zeit zu lernen und sich zu verbessern.

- **Aktivierungen** teilen dem Modell mit, welche Entscheidung es getroffen hat
- **Engagements** teilen dem Modell mit, wie Kund:innen auf die Nachricht reagiert haben
- **Conversions** teilen dem Modell mit, ob das angestrebte Geschäftsergebnis erreicht wurde

Jede dieser Ressourcen muss als inkrementeller Ereignis-Stream (nicht als Snapshot) strukturiert sein. Weitere Informationen finden Sie unter [Snapshots versus Ereignis-Streams]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams).

{% alert note %}
Wenn Decisioning Studio nativ in Ihre geschäftskunden-Engagement-Plattform integriert ist (z. B. Braze oder Salesforce Marketing Cloud), können Aktivierungs- und Engagement-Daten automatisch ohne zusätzliche Konfiguration erfasst werden. Prüfen Sie Ihre Setup-Dokumentation, um dies zu bestätigen.
{% endalert %}

## Erforderliche Ressourcen {#required-assets}

### Kundenprofil {#customer-profile}

Kundenprofildaten beschreiben, wer Ihre Kund:innen sind. Decisioning Studio nutzt diese Daten, um den aktuellen Zustand jeder Kundin und jedes Kunden zu verstehen und relevante Empfehlungen zu generieren.

Häufige Profilattribute umfassen:

- Jahre als geschäftskunden
- Geografie (sofern durch Ihre Branche und Datenschutzanforderungen erlaubt)
- Akquisitionskanal (z. B. Internet, Telefon, im Shop)
- Zufriedenheits- oder Stimmungswert
- Modellbasierte Scores (z. B. Churn-Wahrscheinlichkeit, Lifetime-Value-Schätzung)
- Treuestufe oder Programmmitgliedschaft

### Aktivierungs- und Engagement-Daten {#activation-and-engagement-data}

Aktivierungsdaten erfassen, was Decisioning Studio tatsächlich gesendet hat: welche Empfehlung an welche Kund:innen über welchen Kanal zugestellt wurde. Engagement-Daten erfassen, was die Kund:innen als Reaktion getan haben: ob sie die Nachricht geöffnet, angeklickt oder anderweitig damit interagiert haben.

Bei nativen Braze-Integrationen können Aktivierungs- und Engagement-Daten automatisch über Braze-Currents verfügbar sein. Bei anderen Konfigurationen müssen diese Daten explizit bereitgestellt werden.

Diese Daten sind entscheidend, weil sie die Schleife zwischen einer Empfehlung und ihrem Ergebnis schließen. Ohne sie kann das Modell nicht lernen, welche Entscheidungen funktionieren.

### Conversion-Daten {#conversions-data}

Conversion-Daten beschreiben, was mit den Kund:innen passiert ist, nachdem eine Empfehlung ausgesprochen und eine Nachricht gesendet wurde. Dies ist das primäre Signal, das das Modell verwendet, um zu bewerten, ob eine Empfehlung erfolgreich war.

| Anforderung | Grund |
|-------------|-------|
| Jeder Datensatz enthält den Kundenbezeichner, konsistent mit allen anderen Ressourcen | Decisioning Studio muss Conversions mit den vorangegangenen Empfehlungen verknüpfen können. |
| Jeder Datensatz hat einen Zeitstempel für den Zeitpunkt des Konversions-Events | Genaues Timing ist für die Attribution unerlässlich. Das Modell muss wissen, welcher Empfehlung eine Conversion zugeordnet werden kann. |
| Bei Verwendung einer nicht-binären Erfolgsmetrik (z. B. Umsatz statt „konvertiert“ oder „nicht konvertiert“) muss der Metrikwert in jedem Conversion-Datensatz enthalten sein | Decisioning Studio verwendet den Metrikwert, um Trainingserfahrungen zu generieren. Ohne den Wert kann das Modell nur lernen, dass eine Conversion stattgefunden hat, nicht wie wertvoll sie war. |
| Wenn Conversions direkt einer bestimmten Kommunikation zugeordnet werden können (z. B. Coupon-Einlösung), fügen Sie die Felder hinzu, die zum Abgleich der Conversion mit dem Aktivierungsdatensatz erforderlich sind | Direkte Attribution gibt dem Modell das klarste Lernsignal. Wenn eine direkte Attribution nicht möglich ist, verwendet Decisioning Studio eine näherungsbasierte Attribution als Fallback. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion-Daten" }

## Optionale Ressourcen {#optional-assets}

Mehr Daten führen in der Regel zu einer besseren Modell-Performance, sollten jedoch gegen den erforderlichen Implementierungsaufwand abgewogen werden. Die folgenden optionalen Ressourcen sind häufig nützlich:

### Kundenverhalten {#customer-behavior}

- Anmeldeverlauf des Kontos
- Gerätetyp und Betriebssystem
- Kundenservice-Interaktionen (z. B. Anzahl der Support-Anrufe, besprochene Themen)
- Produktnutzung (z. B. genutzte Stunden pro Tag, aufgerufene Features, angesehene Inhaltskategorien)

### Weitere Transaktionen {#other-transactions}

- Gekaufte Produkte nach Datum, einschließlich Produktattribute
- Transaktionsbeträge
- Transaktionskanäle (z. B. im Shop versus online)
- Zahlungsmethoden

### Weiteres Marketing-Engagement {#other-marketing-engagement}

- Ausgehende Kommunikation, die außerhalb von Decisioning-Studio-Empfehlungen gesendet wurde (z. B. E-Mails, SMS)
- E-Mail-Engagement, das nicht von Decisioning Studio getriggert wurde (z. B. Öffnungen, Klicks)
- Umfrageantworten (z. B. NPS-Scores, Engagement-Umfragen)
- Web- und Mobile-App-Aktivität (z. B. durchsuchte Seiten, angesehene Produkte)