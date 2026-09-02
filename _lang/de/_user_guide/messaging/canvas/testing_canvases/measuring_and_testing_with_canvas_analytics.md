---
nav_title: Canvas Analytics
article_title: Canvas Analytics
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt die verschiedenen Analytics und Berichte, die Sie nutzen können, um die Performance Ihres Canvas zu verstehen."
tool:
  - Canvas
  - Reports


---

# Canvas Analytics {#canvas-analytics}

> Sie müssen wissen, ob das, was Sie erstellen, tatsächlich etwas bewirkt. Mit Canvas Analytics können Sie sich ein vollständiges Bild davon machen, wie die von Ihnen erstellten Erlebnisse Ihre Ziele beeinflussen.

Nachdem Sie Ihren Canvas erstellt und live geschaltet haben, navigieren Sie zur Seite **Canvas** und wählen Sie Ihren Canvas aus, um die Detailseite zu öffnen. Hier können Sie die Performance Ihres Canvas messen und testen.

## Canvas-Übersicht {#canvas-overview}

Oben auf der Seite **Canvas-Details** finden Sie die wichtigsten Canvas-Statistiken. Dazu gehören die Anzahl der innerhalb des Canvas gesendeten Nachrichten, die Gesamtzahl der Eintritte von Kund:innen in den Canvas, wie viele konvertiert haben und Ihre Gesamtrate, der durch den Canvas generierte Umsatz sowie die geschätzte Gesamtzielgruppe.

Dies ist ein idealer Ort, um sich einen allgemeinen Überblick zu verschaffen und zu prüfen, wie Ihr Canvas im Vergleich zu Ihrem Ziel abschneidet. Um proaktiv benachrichtigt zu werden, wenn die Performance eines Canvas außerhalb Ihres erwarteten Bereichs fällt, lesen Sie [Canvas-Schwellenwert-Benachrichtigungen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

### Erreichbare Nutzer:innen und exakte Statistiken {#reachable-users-and-exact-statistics}

Wenn **[Exakte Statistiken berechnen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#single-user-segments)** für Zielgruppen ausgeführt wird, die mit Ihrem Canvas verknüpft sind, zeigt Braze möglicherweise kurzzeitig eine gerundete Schätzung im Bereich **Erreichbare Nutzer:innen** an. Die exakte Gesamtzahl ersetzt die Schätzung, sobald die Berechnung abgeschlossen ist. Wählen Sie **Zusätzliche Statistiken anzeigen** für eine vollständige Aufschlüsselung nach Kanal. Der Canvas-Builder dokumentiert denselben Ablauf unter **Zielpopulation**; siehe [Zielpopulation berechnen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#calculating-target-population).

![Die Seite „Canvas-Details“ mit den wichtigsten Statistiken, darunter gesendete Nachrichten, Konversionsrate, Gesamteintritte, Gesamtumsatz, Gesamtaustritte und geschätzte Zielgruppe, mit Kanal- und Statistikfiltern.]({% image_buster /assets/img_archive/Journey_5.png %})

{% alert tip %}
Wenn ein Segment, das Sie aus Canvas-Aktivitäten erstellt haben, weniger erreichbare Nutzer:innen anzeigt, als Sie aufgrund der Canvas-Analytics erwarten, gibt es zwei häufige Gründe:

- **Schätzung durch Stichproben:** Segment-Statistiken können eine Schätzung auf Basis einer Zufallsstichprobe mit einem 95%-Konfidenzintervall von ±1 % anzeigen, anstatt einer exakten Zählung.
- **Nutzer:innen erfüllen die Kriterien nicht mehr:** Einige Nutzer:innen, die in den Canvas-Analytics gezählt wurden, qualifizieren sich möglicherweise nicht mehr für das Segment – zum Beispiel, weil sie sich abgemeldet haben oder sich ihre Profildaten seit der Ausführung des Canvas geändert haben. Prüfen Sie die **Historische Performance** des Canvas auf ein hohes Volumen an Abmeldungen.
{% endalert %}

### Änderungen seit der letzten Ansicht {#changes-since-last-viewed}

Die Anzahl der Aktualisierungen am Canvas durch andere Mitglieder Ihres Teams wird durch die Metrik *Änderungen seit der letzten Ansicht* auf der Canvas-Übersichtsseite erfasst. Wählen Sie **Änderungen seit der letzten Ansicht**, um ein Changelog der Aktualisierungen an Canvas-Name, Zeitplan, Tags, Nachricht, Zielgruppe, Genehmigungsstatus oder Team-Zugriffskonfiguration anzuzeigen. Für jede Aktualisierung können Sie sehen, wer sie durchgeführt hat und wann. Sie können dieses Changelog nutzen, um Änderungen an Ihren Canvase zu überprüfen.

## Performance-Visualisierung {#performance-visualization}

Wenn Sie auf der Seite **Canvas Details** nach unten scrollen, können Sie die Performance für jede Komponente einsehen – beispielsweise wie viele Nutzer:innen eingetreten sind, zum nächsten Schritt weitergegangen sind oder den Canvas verlassen haben. Wählen Sie einen bestimmten Canvas-Schritt oder eine Komponente aus, um das Panel auf diesen Teil der Journey zu fokussieren und die zugehörigen Metriken im Detail zu überprüfen.

{% alert note %}
Bei Canvas Flow verlassen Nutzer:innen den Canvas, nachdem sie den letzten Schritt der User-Journey betreten und die Nachrichten-Payload erhalten haben.
{% endalert %}

Die Metriken umfassen auch Impressionen, eindeutige Empfänger:innen, Konversionsanzahl und generierten Umsatz. Sie können auf eine Komponente klicken, um Ihre Daten weiter aufzuschlüsseln und die kanalspezifische Performance einzusehen.

![Zwei Beispiele für Performance-Details von Canvas-Komponenten. Links werden die Performance-Details für einen Nutzerpfad mit einer Canvas-Komponente angezeigt. Rechts werden die Performance-Details für eine erweiterte Canvas-Komponente und einen verschachtelten Schritt mit der Anzahl der In-App-Nachrichten-Impressionen angezeigt.]({% image_buster /assets/img_archive/Journey_6.png %})

## Performance-Aufschlüsselung nach Variante {#performance-breakdown-by-variant}

Klicken Sie unten auf der Seite **Canvas Details** auf **Analyze Variants**, um das Modal **Analyze Canvas** zu öffnen. Dieses Modal enthält drei Tabs:

- Analyze Variants
- Canvas Funnel Report
- Canvas Retention Report

### Analyze Variants {#analyze-variants}

Im Tab **Analyze Variants** können Sie eine Aufschlüsselung der Performance nach Variante und Kontrollgruppe sehen, sofern Sie mehr als eine haben. Sie können außerdem den Canvas-API-Bezeichner kopieren, eine CSV-Datei der Metriken herunterladen und die Zellen kopieren. Der Tab **Analyze Variants** enthält eine Tabelle, die Ihnen eine Aufschlüsselung jeder Variante auf mehreren Ebenen zeigt.

Sie können schnell effektive Varianten erkennen und die richtigen Kadenzen, Inhalte, Trigger or triggern, Zeitpunkte und mehr identifizieren.

![Das Modal „Analyze Canvas“ mit dem ausgewählten Tab „Analyze Variants“, das eine Vergleichstabelle für Pfad 1 und Pfad 2 mit Entries, Sends, Umsatz, Konversionsraten, prozentualer Veränderung und Konfidenz-Metriken zeigt.]({% image_buster /assets/img_archive/analyze_variants.png %})

Zu den grundlegenden Metriken gehören:

- **Variant API Identifier:** Der API-Bezeichner Ihrer Variante, den Sie in Ihren API-Aufrufen verwenden können.
- **Total Entries:** Die Gesamtzahl der Nutzer:innen, die in die Canvas-Variante eingetreten sind.
- **Total Sends:** Die Gesamtzahl der in der Canvas-Variante gesendeten Nachrichten.
- **Total Steps:** Die Gesamtzahl der Schritte in der Canvas-Variante.
- **Total Revenue:** Der Gesamtumsatz in Dollar von Canvas-Empfänger:innen innerhalb des festgelegten primären Konversionsfensters. _Total Revenue_ ist die Summe der Käufe, die Nutzer:innen zugeordnet werden, die diese Variante während dieses Fensters erhalten haben. Käufe zählen weiterhin zu _Total Revenue_, auch wenn die Nutzer:innen das konfigurierte primäre Konversions-Event nicht ausführen, solange der Kauf innerhalb der Attributionsregeln für das Fenster liegt.

{% alert note %}
Wie Konversionen wird auch der Umsatz technisch auf Canvas-Ebene erfasst, aber der zuletzt empfangenen Komponente und der zuletzt empfangenen Variante zugeordnet, von der die Nutzer:innen eine Nachricht erhalten haben (oder in die sie eingetreten sind, falls sie noch keine Nachricht erhalten haben).<br><br>
Wenn beispielsweise Nutzer:innen zwei Schritte abschließen und dann einen Kauf tätigen, wird dieser Umsatz der zweiten Komponente und der Variante zugeordnet, in die sie eingetreten sind. Wenn sie in den Canvas eintreten, aber einen Kauf tätigen, bevor sie die erste Canvas-Komponente erhalten, wird dieser Umsatz der Variante zugeordnet, in die sie eingetreten sind, aber keiner Komponente.
{% endalert %}

Darüber hinaus können Sie eine detailliertere Aufschlüsselung der [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) sehen, einschließlich:

- Konversions-Gesamtzahlen und Konversionsraten für jedes Konversions-Event
- Uplift gegenüber der Kontrollvariante
- Statistische Konfidenz für jedes Konversions-Event

### Wie Konversionen erfasst werden {#how-conversions-are-tracked}

Nutzer:innen können pro Konversions-Event und Canvas-Entry nur einmal konvertieren. Konversionen werden der zuletzt empfangenen Nachricht für diesen Entry zugeordnet. Die Canvas-Zusammenfassung spiegelt alle Konversionen wider, die von Nutzer:innen in diesem Pfad durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben oder nicht. Jeder nachfolgende Schritt zeigt nur Konversionen an, die stattfanden, als dieser der zuletzt empfangene Schritt war.

Betrachten Sie das folgende Beispiel: Ein Canvas hat 10 Push-Benachrichtigungen und das Konversions-Event ist „App öffnen“ (oder „Session Start“).
- Nutzer:in A öffnet die App nach dem Eintritt, aber bevor die erste Nachricht empfangen wird.
- Nutzer:in B öffnet die App nach jeder Push-Benachrichtigung.

Die Canvas-Zusammenfassung zeigt zwei Konversionen, während die einzelnen Schritte eine Konversion beim ersten Schritt und keine bei allen nachfolgenden Schritten anzeigen. Wenn Ruhezeiten aktiv sind, wenn das Konversions-Event eintritt, gelten dieselben Regeln.

Nehmen wir nun an, wir haben einen Canvas mit Ruhezeiten und die folgenden Ereignisse treten ein:

1. Nutzer:in A tritt in einen Canvas ein.
2. Der erste Schritt ist ein Delay-Schritt innerhalb der festgelegten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in A führt das Konversions-Event aus.

Nutzer:in A wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht im Schritt, da der Schritt nicht empfangen wurde.

Für unser letztes Beispiel nehmen wir an, wir haben einen Canvas mit aktivierter erneuter Berechtigung. Wenn berechtigte Nutzer:innen das Konversions-Event beim ersten und zweiten Entry ausführen, werden zwei Konversionen gezählt.

### Funnel-Bericht {#funnel-report}

Funnel-Berichte bieten einen visuellen Bericht, mit dem Sie die Journeys analysieren können, die Ihre Kund:innen nach dem Empfang eines Canvas durchlaufen. Wenn Ihr Canvas eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie nachvollziehen, wie die verschiedenen Varianten den Konversions-Funnel auf einer detaillierteren Ebene beeinflusst haben, und auf Basis dieser Daten optimieren. Weitere Informationen zu Funnel-Berichten finden Sie unter [Funnel-Berichte]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports).

### Bindungsbericht {#retention-report}

Nutzerbindung ist eine der wichtigsten Metriken für jeden Marketer. Engagierte Nutzer:innen, die immer wieder zurückkehren, zeigen, dass das Geschäft gesund ist. Braze ermöglicht es Ihnen, die Nutzerbindung direkt auf der Seite **Canvas Analytics** zu messen. Weitere Informationen zum Lesen und Interpretieren Ihres Bindungsberichts finden Sie unter [Bindungsberichte]({{site.baseurl}}/user_guide/analytics/reports/retention_reports).