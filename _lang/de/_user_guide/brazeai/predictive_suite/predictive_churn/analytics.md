---
nav_title: Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Analytics
article_title: Predictive-Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Analytics
description: "Dieser Referenzartikel behandelt die verschiedenen Komponenten der Seite Abwanderung or Abwanderung, Churn or Abwanderung, churnen Prognose-Analytics und zeigt, wie Sie diese nutzen können, um aufschlussreiche, zielgerichtete Entscheidungen zu treffen."
page_order: 1.5

---

# Predictive-Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Analytics {#predictive-churn-analytics}

> Nachdem Ihre Prognose erstellt und trainiert wurde, haben Sie Zugriff auf die Seite **Prognose-Analytics**. Diese Seite hilft Ihnen bei der Entscheidung, welche Nutzer:innen Sie auf der Grundlage ihres _Churn-Risiko-Scores_ oder ihrer Kategorie ansprechen sollten.

## Über Predictive-Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Analytics {#about-predictive-churn-analytics}

Sobald das Training der Prognose abgeschlossen und diese Seite gefüllt ist, können Sie direkt [Filter]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users#filters) in Segmenten oder Campaigns verwenden, um die Ergebnisse des Modells zu nutzen. Wenn Sie jedoch Hilfe bei der Entscheidung benötigen, wen Sie ansprechen und warum, kann Ihnen diese Seite auf der Grundlage der historischen Genauigkeit des Modells und Ihrer eigenen Geschäftsziele helfen.

Dies sind die Komponenten, aus denen sich die Predictive-Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Analytics zusammensetzen:

- [Abwanderung or Abwanderung, Churn or Abwanderung, churnen Score und Kategorie](#churn_score)
- [Prognosequalität](#prediction_quality)
- [Geschätzte Genauigkeit](#estimated_results)
- [Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Korrelationstabelle](#correlation_table)

Die Verteilung der Scores für die gesamte Prognosegruppe wird oben auf der Seite in einem Chart angezeigt, das Sie nach Kategorie oder Score anzeigen können. Nutzer:innen in den weiter rechts gelegenen Bereichen haben höhere Scores und werden eher abwandern. Nutzer:innen in den weiter links gelegenen Bereichen werden weniger wahrscheinlich abwandern. Mit dem Schieberegler unterhalb des Charts können Sie einen Bereich von Nutzer:innen auswählen und abschätzen, wie die Ergebnisse aussehen würden, wenn Sie Nutzer:innen im ausgewählten Bereich des _Churn-Risiko-Scores_ oder der Kategorie ansprechen würden.

Wenn Sie den Schieberegler verschieben, informiert Sie der Balken in der linken Hälfte des unteren Panels darüber, wie viele Nutzer:innen aus der gesamten Prognosegruppe angesprochen werden würden.

![Predictive-Churn-Analytics-Chart mit Schieberegler zur Auswahl eines Ziel-Score-Bereichs.]({% image_buster /assets/img/churn/churnTargeting.gif %})

## Abwanderung or Abwanderung, Churn or Abwanderung, churnen Score und Kategorie {#churn_score}

Den Nutzer:innen in der Prognosegruppe wird ein _Churn-Risiko-Score_ zwischen 0 und 100 zugewiesen. Je höher der Score, desto größer ist die Wahrscheinlichkeit der Abwanderung.
- Nutzer:innen mit Scores zwischen 0 und 50 werden in die Kategorie _Geringes Risiko_ eingestuft.
- Nutzer:innen mit Scores zwischen 50 und 75 bzw. 75 und 100 werden in die Kategorien _Mittleres Risiko_ bzw. _Hohes Risiko_ eingestuft.

Die Scores und die entsprechenden Kategorien werden nach dem Zeitplan aktualisiert, den Sie auf der Seite zur Modellerstellung gewählt haben. Die Anzahl der Nutzer:innen mit Abwanderung or Abwanderung, Churn or Abwanderung, churnen Scores in jedem der 20 gleich großen Buckets wird im Chart oben auf der Seite angezeigt. So können Sie abschätzen, wie das Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Risiko in der Gesamtpopulation gemäß dieser Prognose aussieht.

## Prognosequalität {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Geschätzte Genauigkeit {#estimated_results}

In der rechten Hälfte des Panels unterhalb des Charts zeigen wir Schätzungen der erwarteten Genauigkeit bei der Ansprache dieses Teils der Prognosegruppe. Auf der Grundlage von Daten über Nutzer:innen in der Prognosegruppe in der Vergangenheit und der offensichtlichen Genauigkeit des Modells bei der Unterscheidung zwischen abwandernden und nicht abwandernden Nutzer:innen auf der Grundlage dieser vergangenen Daten schätzen diese Fortschrittsbalken für eine zukünftige potenzielle Nachricht unter Verwendung der mit dem Schieberegler hervorgehobenen Zielgruppe:

![Panel „Geschätzte Genauigkeit“ mit erwarteten Abwandernden und Nicht-Abwandernden für den ausgewählten Zielgruppenbereich.]({% image_buster /assets/img/churn/churnEstimatedResults.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

- Wie viele ausgewählte Nutzer:innen voraussichtlich abwandern werden
- Wie viele ausgewählte Nutzer:innen voraussichtlich **nicht** abwandern werden

Anhand dieser Informationen empfehlen wir Ihnen zu entscheiden, wie viele der Abwandernden Sie erfassen möchten und wie hoch die Kosten eines falsch positiven Ergebnisses für Ihr Unternehmen sind. Wenn Sie eine hochwertige Werbeaktion versenden, sollten Sie möglichst wenige Nicht-Abwandernde ansprechen und gleichzeitig so viele erwartete tatsächliche Abwandernde einbeziehen, wie das Modell zulässt. Oder wenn Sie weniger empfindlich auf falsch positive Ergebnisse reagieren und Nutzer:innen zusätzliche Nachrichten erhalten, können Sie mehr Nachrichten an die Zielgruppe senden, um mehr erwartete Abwandernde zu erfassen und die wahrscheinlichen Fehler zu ignorieren.

### Nutzer:innen, die voraussichtlich abwandern {#users-expected-to-churn}

Dies ist eine Schätzung, wie viele tatsächlich Abwandernde korrekt angesprochen werden. Natürlich kennen wir die Zukunft nicht genau, sodass wir nicht präzise wissen, welche Nutzer:innen aus der Prognosegruppe in Zukunft abwandern werden. Aber die Prognose ist eine zuverlässige Schlussfolgerung. Basierend auf der bisherigen Performance zeigt dieser Fortschrittsbalken an, wie viele der insgesamt „tatsächlichen“ oder „echten“ Abwandernden, die in der Prognosegruppe erwartet werden (basierend auf früheren Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Raten), mit der aktuellen Targeting-Auswahl angesprochen werden. Wir würden erwarten, dass diese Anzahl von Nutzer:innen abwandert, wenn Sie sie nicht mit zusätzlichen oder ungewöhnlichen Nachrichten ansprechen.

### Nutzer:innen, die voraussichtlich nicht abwandern {#users-expected-not-to-churn}

Dies ist eine Schätzung, wie viele Nutzer:innen, die nicht abgewandert wären, fälschlicherweise angesprochen werden. Alle Modelle für maschinelles Lernen machen Fehler. Möglicherweise gibt es in Ihrer Auswahl Nutzer:innen mit einem hohen _Churn-Risiko-Score_, die dann aber doch nicht abwandern. Diese würden auch dann nicht abwandern, wenn Sie überhaupt nichts unternehmen. Sie werden trotzdem angesprochen, was einen Fehler oder ein „falsch positives Ergebnis“ darstellt. Die gesamte Breite dieses zweiten Fortschrittsbalkens steht für die erwartete Anzahl der Nutzer:innen, die nicht abwandern werden, und der gefüllte Teil steht für diejenigen, die anhand der aktuellen Schiebereglerposition fälschlicherweise angesprochen werden.

## Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Korrelationstabelle {#correlation_table}

Diese Analyse zeigt Nutzerattribute oder -verhaltensweisen, die in der historischen Prognosegruppe mit der Abwanderung korreliert haben. Die Tabellen sind in links und rechts für mehr bzw. weniger abwanderungsgefährdet unterteilt. Für jede Zeile wird in der zweiten Spalte das Verhältnis angezeigt, in dem Nutzer:innen mit dem Verhalten oder Attribut in der ersten Spalte eher oder weniger wahrscheinlich abwandern. Diese Zahl gibt die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Wahrscheinlichkeit bei Vorhandensein dieses Verhaltens oder Attributs geteilt durch die Abwanderung or Abwanderung, Churn or Abwanderung, churnen-Wahrscheinlichkeit der gesamten Prognosegruppe an.

Diese Tabelle wird nur aktualisiert, wenn die Prognose neu trainiert wird, und nicht, wenn die _Churn-Risiko-Scores_ der Nutzer:innen aktualisiert werden.

{% alert note %}
Die Korrelationsdaten für Vorschau-Prognosen werden teilweise ausgeblendet. Um diese Informationen zu erhalten, ist ein Kauf erforderlich. Kontaktieren Sie Ihren Account Manager:in für weitere Informationen.
{% endalert %}