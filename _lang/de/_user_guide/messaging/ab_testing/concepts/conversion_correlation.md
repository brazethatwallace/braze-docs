---
nav_title: Konversionskorrelation
article_title: Konversionskorrelation
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Dieser Referenzartikel erklärt die Konversionskorrelationsanalyse auf der Seite Campaign Analytics."
tool:
  - Reports

---

# Konversionskorrelation {#conversion-correlation}

> Die Analyse der Konversionskorrelation auf der Seite **Campaign Analytics** gibt Ihnen Aufschluss darüber, welche Nutzerattribute und Verhaltensweisen von Nutzer:innen die von Ihnen für Campaigns festgelegten Ergebnisse fördern oder beeinträchtigen.

## Übersicht {#overview}

Für jede Campaign prüft Braze eine Liste von Attributen und dem Verhalten von Nutzer:innen und berechnet, ob Nutzer:innen statistisch signifikant mit einem Anstieg oder einem Rückgang der einzelnen [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) verbunden sind, die Sie für die Campaign festgelegt haben. Wir berechnen auch, wie viel wahrscheinlicher oder unwahrscheinlicher es ist, dass Nutzer:innen mit dem jeweiligen Attribut oder Verhalten konvertieren, und wenn dies signifikant ist, zeigen wir dies auf der entsprechenden Seite der Tabelle an. Nutzer:innen mit dem jeweiligen Attribut oder Verhalten werden mit den Raten für die gesamte Zielgruppe der Campaign verglichen. Verhaltensweisen und Attribute, die keine signifikante Korrelation mit der Conversion aufweisen, sind in der Tabelle nicht aufgeführt.

Um eine Konversionskorrelationsanalyse durchzuführen, wählen Sie das gewünschte Konversions-Event aus dem Dropdown-Menü aus.

![Das Panel „Konversionskorrelation“ zeigt ein Beispiel, bei dem „Wählen Sie ein Konversions-Event“ auf „Primäres Konversions-Event - A“ gesetzt ist und die Event-Einstellung „Made Purchase within 12 hours (Any product)“ lautet.]({% image_buster /assets/img/convcorr.png %})

## Was wird geprüft? {#what-is-checked}

Wir prüfen die folgenden Attribute, indem wir sie als kategoriale Variablen behandeln. Das bedeutet, dass Nutzer:innen entweder einen bestimmten Wert dieser Attribute haben oder nicht – und wir testen, ob dies die Konversionsrate beeinflusst.

- Land
- Sprache
- Geschlecht

Außerdem prüfen wir, ob Folgendes die Konversionsrate beeinflusst:

- Ausführung beliebiger angepasster Events
- Campaigns und Canvase, die in den letzten 30 Tagen empfangen wurden (außer der aktuell bewerteten Campaign)

Schließlich prüfen wir mehrere Verhaltensvariablen, die verschiedene Werte annehmen können. Wir teilen die folgenden Variablen in vier Buckets oder Quartile auf und messen dann den Zusammenhang zwischen der Zugehörigkeit zu einem Quartil und einem Anstieg oder Rückgang der Conversion:

- Alter
- Gesamtausgaben in Dollar
- Anzahl der Sitzungen

## Wann kann ich diese Analyse einsehen? {#when-can-i-check-this-analysis}

Diese Analyse wird frühestens 24 Stunden nach Beginn des Campaign-Versands verfügbar und berücksichtigt nur Sendungen der letzten 30 Tage. Wenn keine Verhaltensweisen oder Attribute signifikant mit einem der Konversions-Events der Campaign korrelieren, wird das Dropdown-Menü deaktiviert und eine entsprechende Meldung angezeigt.

## Wie Braze die Signifikanz prüft {#how-braze-checks-for-significance}

Wir prüfen die statistische Signifikanz mithilfe des [Wilson-Konfidenzintervalls](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Wir bestimmen mit 95-prozentiger Konfidenz die Rate, mit der die gesamte Campaign-Zielgruppe konvertiert hat. Dies wird als Basisrate bezeichnet.

Anschließend berechnen wir für jede der Variablen ebenfalls mit 95-prozentiger Konfidenz die Rate, mit der Nutzer:innen mit dem jeweiligen Attribut oder Verhalten konvertiert haben. Indem wir diesen Wert durch die Basisrate teilen, können wir das Verhältnis ermitteln. Ist es deutlich größer als 1, konvertieren Nutzer:innen mit diesem Attribut oder Verhalten mit höherer Wahrscheinlichkeit. Ist es deutlich kleiner, ist die Wahrscheinlichkeit geringer. Wir zeigen den Wert des Verhältnisses in der Tabelle an. Der Wert wird nur angezeigt, wenn er weit genug von 1 entfernt ist, um auf dem 95-Prozent-Konfidenzniveau signifikant zu sein.