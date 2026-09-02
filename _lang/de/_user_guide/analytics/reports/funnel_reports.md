---
nav_title: Funnel-Berichte
article_title: Funnel-Berichte für Campaigns und Canvase
page_order: 8
page_type: reference
description: "Diese Seite behandelt die Vorteile von Funnel-Berichten, wie Sie diese einrichten und wie Sie Ihren Bericht interpretieren."
tool: Reports
---

# Funnel-Berichte {#funnel-reports}

> Die Seite **Funnel-Bericht** bietet einen visuellen Bericht, mit dem Sie die Journeys Ihrer Kund:innen nach dem Empfang einer Campaign oder eines Canvas analysieren können, einschließlich der verschiedenen Aktionen, die Kund:innen auf ihrem Weg zur Conversion durchführen, und wo Abbrüche auftreten. ![Screenshot der Funnel-Bericht-Seite mit einem Konversionstrichter für die Campaign- oder Canvas-Performance]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Wenn Ihre Campaign oder Ihr Canvas eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie nachvollziehen, wie die verschiedenen Varianten den Konversionstrichter auf einer detaillierteren Ebene beeinflusst haben, und auf Basis dieser Daten optimieren.

![Funnel-Bericht 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Anwendungsfälle {#use-cases}

Funnel-Berichte können Fragen beantworten wie:

- **Onboarding:** Wie viele Nutzer:innen haben nach dem Versand eines „Willkommen, Neuling!“-Canvas jeden Schritt des Onboarding-Pfads abgeschlossen?
- **Kaufabschluss:** Wo traten Kaufabbrüche bei einer saisonalen Aktion auf?
- **Angepasste Conversions:** Welcher Anteil der Nutzer:innen hat nach einem „Neues Release“-Push eine Sitzung gestartet, einen Track angehört und eine Playlist erstellt?
- **Upsell-Abbrüche:** An welcher Stelle eines Upsell-Canvas sind Nutzer:innen ausgestiegen, bevor sie ein Abonnement abgeschlossen haben?
- **Verhalten nach dem Engagement:** Welche E-Mail-Variante hat nach dem Öffnen zu mehr Käufen geführt?
- **Conversion-Häufigkeit:** Welcher Prozentsatz der Nutzer:innen hat nach dem Empfang einer Campaign mindestens dreimal eine:n Freund:in empfohlen?

## Funnel-Berichte einrichten {#setting-up-funnel-reports}

![Funnel-Bericht 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Sie können Funnel-Berichte für bestehende aktive Campaigns und Canvase erstellen. Diese Berichte zeigen eine Reihe von Events, die ein:e Campaign-Empfänger:in über einen Zeitraum von 1–30 Tagen ab dem Datum des Eintritts in den Canvas oder die Campaign durchläuft. Ein:e Nutzer:in gilt als durch einen Schritt im Funnel konvertiert, wenn er/sie das Event in der angegebenen Reihenfolge ausführt.

Funnel-Berichte sind an folgenden Stellen im Dashboard verfügbar:

- Die Seite **Campaign Analytics** für eine bestimmte Campaign
- Die Seite **Canvas Details** für einen bestimmten Canvas, über den Button **Analyze Variants**

{% alert important %}
Funnel-Berichte sind nicht verfügbar für [API-Kampagnen]({{site.baseurl}}/api/api_campaigns).
{% endalert %}

### 1. Schritt: Datumsbereich auswählen {#step-1-select-a-date-range}

Sie können einen Zeitrahmen für Ihren Bericht auswählen (innerhalb der letzten sechs Monate) und die Daten verfeinern, um Nutzer:innen anzuzeigen, die beim Eintritt in die Campaign oder den Canvas die Funnel-Events innerhalb eines festgelegten Fensters (maximal 30 Tage) abgeschlossen haben. Im folgenden Beispiel würde Ihr Funnel nach Nutzer:innen suchen, die diese Campaign oder diesen Canvas in den letzten sieben Tagen erhalten haben und den Funnel innerhalb von drei Tagen abgeschlossen haben.

{% alert note %}
Wenn Sie das Fenster zum Abschluss des Funnels auf einen Tag setzen, muss das Funnel-Event innerhalb von 24 Stunden nach Nachrichtenempfang stattfinden. Wenn Sie jedoch mehrere Tage auswählen, wird das Zeitfenster als Kalendertage in der Zeitzone des Unternehmens gezählt.
{% endalert %}

![Funnel-Bericht für einen Canvas mit „Letzte 7 Tage“ als ausgewähltem Zeitrahmen im Dropdown.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### 2. Schritt: Events für Funnel-Schritte auswählen {#step-2-select-events-for-funnel-steps}

Für jeden Funnel-Bericht ist das erste Event der Empfang Ihrer Nachricht durch die Nutzer:innen. Von dort aus filtern die nachfolgenden Events, die Sie auswählen, die Anzahl der Nutzer:innen, die diese Events sowie die vorherigen Events ausgeführt haben.

#### Verfügbare Funnel-Bericht-Events {#available-funnel-report-events}

| Campaign | Sitzung gestartet, Kauf getätigt, angepasstes Event ausgeführt, Nachrichten-Engagement-Event |
| Canvas | Sitzung gestartet, Kauf getätigt, angepasstes Event ausgeführt, Canvas-Schritt erhalten, mit Schritt interagiert |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Funnel-Bericht-Events" }

{% alert note %}
Das Bericht-Event **Mit Schritt interagiert** kann nur mit Canvas-Schritten verwendet werden, die die Messaging-Kanäle E-Mail oder Push nutzen.
{% endalert %}

![Funnel-Bericht für einen Canvas mit einem Dropdown der verfügbaren Bericht-Events.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Funnel-Berichte ermöglichen es Ihnen, den Erfolg Ihrer Nachrichten über die ursprünglich eingerichteten Konversions-Events oder Nachrichten-Engagement-Events hinaus zu vergleichen. Wenn es also ein Konversions-Event gibt, das Sie anfangs nicht hinzugefügt haben, können Sie Conversions für dieses Event dennoch mithilfe eines Funnels verfolgen.

Wenn Sie beispielsweise ein 14-Tage-Berichtszeitfenster auswählen, gefolgt von den Events `Added to cart` und `Made purchase`, sehen Sie sowohl die Anzahl der Nutzer:innen, die innerhalb von 14 Tagen nach Nachrichtenempfang etwas in den Warenkorb gelegt haben, als auch die Anzahl der Nutzer:innen, die etwas in den Warenkorb gelegt und dann innerhalb von 14 Tagen nach Empfang der Campaign einen Kauf getätigt haben.

Als weiteres Beispiel möchten Sie vielleicht den Prozentsatz der Nutzer:innen sehen, die nach dem Klicken auf eine E-Mail konvertiert haben. Um dies zu berechnen, könnten Sie einen Bericht erstellen, bei dem das zweite Event das Klicken auf Ihre E-Mail und das dritte Event die Ausführung Ihres Konversions-Events ist.

Nachdem Sie **Build Report** ausgewählt haben, kann die Erstellung des Funnel-Berichts einige Minuten dauern. Während dieser Zeit können Sie den Bericht verlassen und zu anderen Seiten im Dashboard navigieren. Sie erhalten eine Benachrichtigung im Dashboard, wenn Ihr Bericht fertig ist.

## Ihren Funnel-Bericht interpretieren {#interpreting-your-funnel-report}

In Ihrem Funnel-Bericht können Sie die Kontrollgruppe direkt mit den von Ihnen eingerichteten Varianten vergleichen. Jedes aufeinanderfolgende Event zeigt, welcher Prozentsatz der vorherigen Nutzer:innen diese Aktion ausgeführt und durch den Funnel konvertiert hat.

### Komponenten des Funnel-Berichts {#funnel-report-components}

- **Horizontale Achse**: Zeigt den Prozentsatz der Nachrichtenempfänger:innen an, die diese Aktionen ausgeführt haben.
- **Chart**: Zeigt die Anzahl der empfangenen Nachrichten, die Anzahl der Nutzer:innen, die die vorherigen Aktionen sowie die von Ihnen gewählte Aktion ausgeführt haben, die Konversionsrate und die prozentuale Veränderung gegenüber der Kontrollgruppe.
- **Option „Regenerieren“**: Ermöglicht es Ihnen, Ihren Bericht neu zu generieren, und zeigt an, wann der aktuelle Bericht zuletzt erstellt wurde.
- **Varianten**: Durch farbige Spalten gekennzeichnet, ermöglicht das Funnel-Reporting bis zu 8 Varianten und eine Kontrollgruppe. Standardmäßig zeigt das **Chart** nur drei Varianten an. Um weitere zu sehen, können Sie die restlichen Varianten manuell auswählen.

![Funnel-Bericht-Chart.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Für Campaigns mit mehreren Varianten**: Braze zeigt eine Tabelle mit Metriken für jedes Event und jede Variante sowie die prozentuale Veränderung gegenüber der Kontrollgruppe. Die Konversionsrate ist die Anzahl der Nutzer:innen, die das Event (und die nachfolgenden) pro Nachrichtenempfänger:in ausgeführt haben.

**Für Campaigns mit erneuter Berechtigung**: Wenn ein:e Nutzer:in die Campaign innerhalb des Berichtszeitfensters mehr als einmal erhält, bestimmt Braze anhand der Aktionen, die diese:r Nutzer:in nach dem ersten Empfang der Campaign innerhalb des Zeitfensters ausgeführt hat, ob er/sie in den Funnel aufgenommen werden soll.
- Beachten Sie, dass es eine Diskrepanz zwischen den Funnel- und den Standard-Conversion-Werten geben kann, da Nutzer:innen bei erneuter Berechtigung mehr als einmal konvertieren können, Funnel-Berichte jedoch maximal einmal konvertieren, selbst wenn ein:e Nutzer:in das Event mehr als einmal ausführt.

**Für Campaigns mit mehreren Varianten und erneuter Berechtigung**: Wenn ein:e Nutzer:in während des Berichtszeitfensters mehrere Varianten der Campaign erhält, bestimmt Braze anhand der Aktionen, die diese:r Nutzer:in nach dem ersten Empfang der Kampagnenvariante ausgeführt hat, ob er/sie in den Varianten-Funnel aufgenommen werden soll. Das bedeutet, dass dieselbe Person in mehreren verschiedenen Varianten gezählt werden kann, wenn sie während des Funnel-Zeitfensters mehrere Varianten erhalten hat.

{% alert important %}
Verwaiste Nutzer:innen werden in Funnel-Berichten nicht erfasst. Wenn ein:e anonyme:r Nutzer:in einen Canvas oder eine Campaign betritt und später durch die Methode `changeUser()` identifiziert wird, ändert sich die Braze-ID. Funnel-Berichte verfolgen nur Folge-Events, die mit der Nutzer-ID zum Zeitpunkt des Eintritts übereinstimmen, und berücksichtigen keine Events, die von der/dem Nutzer:in nach der ID-Änderung ausgeführt wurden. Das bedeutet, dass Konversions-Events, die von der/dem Nutzer:in nach der Identifizierung ausgeführt werden, nicht im Funnel-Bericht enthalten sind.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Fällt ein:e Nutzer:in aus dem Bericht heraus, wenn er/sie ein Event überspringt? {#does-a-user-fall-out-of-the-report-if-they-skip-an-event}

Ja. Ein:e Nutzer:in verlässt den Funnel beim ersten Schritt, bei dem er/sie das nächste Event in der von Ihnen konfigurierten exakten Reihenfolge nicht ausführt.

### Wie viele Events kann ich in einen Funnel-Bericht aufnehmen? {#how-many-events-can-i-include-in-a-funnel-report}

Es gibt kein festes Limit, aber vier bis sechs Events decken die meisten Anwendungsfälle ab. Sehr lange Funnels können langsam laufen oder ein Timeout verursachen.

### Welche Kanäle unterstützen das Funnel-Event „Mit Schritt interagiert“? {#what-channels-support-the-interacted-with-step-funnel-event}

**Mit Schritt interagiert** ist für Canvas-Schritte verfügbar, die die Kanäle **E-Mail** oder **Push** verwenden.

### Warum dauert das Laden meines Funnel-Berichts so lange? {#why-is-my-funnel-report-taking-a-long-time-to-load}

Große Abfragen können ein Timeout verursachen. Versuchen Sie ein kürzeres Berichtsfenster, weniger Funnel-Schritte oder beides.

### Warum unterscheiden sich die Analytics im Canvas vom Funnel-Bericht? {#why-are-the-analytics-on-the-canvas-different-from-the-funnel-report}

Canvas-Schritt-Analytics können für dieselben Kalenderdaten höhere Zahlen als der Funnel anzeigen, da Schritt-Analytics ein breiteres Engagement und breitere Conversions umfassen, während der Funnel Event-Reihenfolge und Timing-Regeln durchsetzt.

#### Canvas Analytics (Analyze Variants) {#canvas-analytics-analyze-variants}

Der Datumsbereich filtert Events danach, **wann sie aufgetreten sind**. Wenn Sie den 1.–7. Januar auswählen, sehen Sie alle Eintritte und Konversions-Events, die in diesem Zeitfenster stattgefunden haben – unabhängig davon, wann die/der Nutzer:in den Canvas betreten hat. Ein:e Nutzer:in, der/die am 1. Januar eingetreten ist, aber am 8. Januar konvertiert hat, würde einen Eintritt und null Conversions anzeigen, da die Conversion außerhalb der ausgewählten Daten lag. Das auf dem Canvas-Schritt konfigurierte Conversion-Fenster kann über das maximale Nachverfolgungsfenster des Funnels hinausgehen, sodass Schritt-Analytics Conversions über einen längeren Zeitraum erfassen können.

#### Funnel-Berichte

Der Datumsbereich filtert Nutzer:innen danach, **wann sie den Canvas betreten haben**. Wenn Sie den 1.–7. Januar auswählen, umfasst der Bericht alle Nutzer:innen, die in diesem Zeitfenster eingetreten sind, und verfolgt dann deren Aktionen für das von Ihnen konfigurierte Funnel-Abschlussfenster (bis zu 30 Tage nach dem Eintritt). Dieselbe Person, die am 1. Januar eingetreten ist und am 8. Januar konvertiert hat, würde einen Eintritt und eine Conversion anzeigen, da die Conversion innerhalb des Fensters nach dem Eintritt stattfand.

Darüber hinaus erfordern Funnel-Berichte, dass Events in der angegebenen Reihenfolge auftreten, und zählen jede:n Nutzer:in maximal einmal, während Canvas Analytics alle Conversions und das gesamte Engagement ohne Reihenfolgebeschränkung zählen.