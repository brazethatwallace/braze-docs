---
nav_title: Event-Analytics
article_title: Predictive-Event-Analytics
description: "Dieser Referenzartikel behandelt die verschiedenen Komponenten der Seite Predictive Events Analytics und zeigt, wie Sie diese nutzen können, um aufschlussreiche, zielgerichtete Entscheidungen zu treffen."
page_order: 1.3

---

# Predictive-Event-Analytics {#predictive-event-analytics}

> Nachdem Ihre Prognose erstellt und trainiert wurde, haben Sie Zugriff auf die Seite **Prediction Analytics**. Diese Seite hilft Ihnen bei der Entscheidung, welche Nutzer:innen Sie auf der Grundlage ihres Wahrscheinlichkeitswerts oder ihrer Kategorie ansprechen sollten.

## Über Predictive-Event-Analytics {#about-predictive-event-analytics}

Sobald das Training der Prognose abgeschlossen und diese Seite gefüllt ist, können Sie mit der Verwendung von [Filtern]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users#filters) in Segmenten oder Campaigns beginnen, um die Ergebnisse des Modells zu nutzen. Wenn Sie Hilfe bei der Entscheidung benötigen, wen Sie ansprechen und warum, kann Ihnen diese Seite auf der Grundlage der historischen Genauigkeit des Modells und Ihrer eigenen Geschäftsziele helfen.

Dies sind die Komponenten, aus denen sich die Predictive-Event-Analytics zusammensetzen:

- [Wahrscheinlichkeitswert](#purchase_score)
- [Prognosequalität](#prediction_quality)
- [Geschätzte Genauigkeit](#estimated_results)
- [Event-Korrelationstabelle](#correlation_table)

Die Verteilung der Wahrscheinlichkeitswerte für die gesamte Prognosegruppe wird oben auf der Seite angezeigt. Nutzer:innen in den Buckets weiter rechts haben höhere Werte und werden das Event mit größerer Wahrscheinlichkeit durchführen. Nutzer:innen in den Buckets weiter links führen das Event mit geringerer Wahrscheinlichkeit durch. Mit dem Schieberegler unterhalb des Charts können Sie einen Bereich von Nutzer:innen auswählen und die Ergebnisse der Ansprache dieser Nutzer:innen abschätzen.

Wenn Sie die Griffe des Schiebereglers in verschiedene Positionen bewegen, informiert Sie der Balken in der linken Hälfte des Panels darüber, wie viele Nutzer:innen aus der gesamten Prognosegruppe mit dem von Ihnen ausgewählten Teil der Population angesprochen werden würden.

![Wenn Sie die Griffe des Schiebereglers in verschiedene Positionen bewegen, informiert Sie der Balken in der linken Hälfte des Panels darüber, wie viele Nutzer:innen aus der gesamten Prognosegruppe mit dem von Ihnen ausgewählten Teil der Population angesprochen werden würden.]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"}

## Wahrscheinlichkeitswert {#purchase_score}

Den Nutzer:innen in der Prognosegruppe wird ein Wahrscheinlichkeitswert zwischen 0 und 100 zugewiesen. Je höher der Wert, desto größer ist die Wahrscheinlichkeit, dass das Event durchgeführt wird.

Im Folgenden sehen Sie, wie Nutzer:innen je nach Wahrscheinlichkeitswert eingestuft werden:

- **Niedrig:** zwischen 0 und 50
- **Mittel:** zwischen 50 und 75
- **Hoch:** zwischen 75 und 100

Die Werte und die entsprechenden Kategorien werden entsprechend dem Zeitplan aktualisiert, den Sie auf der Seite **Prediction Creation** ausgewählt haben. Die Anzahl der Nutzer:innen mit Wahrscheinlichkeitswerten in jedem der 20 gleichgroßen Buckets oder in jeder der Wahrscheinlichkeitskategorien wird im Chart oben auf der Seite angezeigt.

### Zugriff auf Wahrscheinlichkeitswerte auf Nutzer:innen-Ebene {#accessing-user-level-likelihood-scores}

Um den Wahrscheinlichkeitswert für eine:n einzelne:n Nutzer:in anzuzeigen, suchen Sie diese:n Nutzer:in im Dashboard und gehen Sie zu **Engagement** > **Predictions**, um den Wert anzuzeigen. Um auf die Werte und Kategorien für mehrere Nutzer:innen gleichzeitig zuzugreifen, erstellen Sie ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mithilfe der Filter [Event Likelihood Score]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#event-likelihood-score) oder [Event Likelihood Category]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#event-likelihood-category) und exportieren Sie anschließend die Nutzer:innen aus diesem Segment. Beim Exportieren können Sie die Wahrscheinlichkeitswerte in die Exportdaten aufnehmen.

{% alert note %}
Obwohl sowohl bei Predictive Events als auch bei [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) den Nutzer:innen Werte zugewiesen werden, gibt es wichtige Unterschiede:<br><br>

- **Predictive Events** (Kaufprognosen): Berücksichtigen alle Nutzer:innen in der Prognosegruppe, unabhängig davon, ob sie das Ziel-Event zuvor durchgeführt haben. Beispielsweise kann eine Kaufprognose Nutzer:innen identifizieren, die wahrscheinlich ihren ersten Kauf tätigen werden.
- **Predictive Churn**: Berücksichtigt nur Nutzer:innen, die das angepasste Event bereits durchgeführt haben. Churn-Prognosen identifizieren Nutzer:innen, die zuvor eine bestimmte Handlung durchgeführt haben und diese wahrscheinlich nicht mehr ausführen werden. Ein:e Nutzer:in, die sich noch nie angemeldet hat, kann nicht als „abgewandert“ betrachtet werden, wenn sie sich nicht anmeldet.

Beim Exportieren von Churn-Risiko-Werten aus einem Segment spiegeln diese Werte das Churn-Prognosemodell wider, das sich von Kauf- oder anderen Event-Prognosemodellen unterscheidet.
{% endalert %}

## Geschätzte Genauigkeit {#estimated_results}

In der rechten Hälfte des Panels unterhalb des Charts werden Schätzungen der erwarteten Genauigkeit bei der Ansprache des ausgewählten Teils der Prognosegruppe auf zwei Weisen angezeigt: wie viele ausgewählte Nutzer:innen das Event voraussichtlich durchführen und wie viele nicht.

![Die ausgewählte Zielgruppe und die geschätzte Genauigkeit im Braze-Dashboard.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Voraussichtliche Durchführung {#expected-to-perform}

Anhand der geschätzten Genauigkeit können Sie überprüfen, wie viele ausgewählte Nutzer:innen das Event voraussichtlich durchführen werden.

Die Prognose ist nicht perfekt genau, und keine Prognose ist das jemals. Das bedeutet, dass Braze nicht in der Lage sein wird, jede einzelne zukünftige Nutzer:in zu identifizieren, die das Event durchführt. Die Wahrscheinlichkeitswerte sind wie eine Reihe von fundierten und zuverlässigen Vorhersagen. Der Fortschrittsbalken zeigt an, wie viele der in der Prognosegruppe erwarteten „True Positives“ mit der ausgewählten Zielgruppe erreicht werden. Dabei wird davon ausgegangen, dass diese Nutzer:innen das Event auch dann durchführen, wenn Sie ihnen keine Nachricht senden.

### Voraussichtlich keine Durchführung {#not-expected-to-perform}

Anhand der geschätzten Genauigkeit können Sie überprüfen, wie viele ausgewählte Nutzer:innen das Event voraussichtlich nicht durchführen werden.

Alle Modelle für maschinelles Lernen machen Fehler. Es kann Nutzer:innen in Ihrer Auswahl geben, die zwar einen hohen Wahrscheinlichkeitswert haben, aber das Event nicht tatsächlich durchführen. Sie würden das Event auch dann nicht durchführen, wenn Sie gar nichts unternehmen. Sie werden trotzdem angesprochen, also ist dies ein Fehler oder „False Positive“. Die gesamte Breite dieses zweiten Fortschrittsbalkens steht für die erwartete Anzahl von Nutzer:innen, die das Event nicht durchführen werden, und der gefüllte Teil für diejenigen, die anhand der aktuellen Schiebereglerposition fälschlicherweise angesprochen werden.

Anhand dieser Informationen sollten Sie entscheiden, wie viele der True Positives Sie erfassen möchten, wie viele False Positives hinnehmbar sind und wie hoch die Fehlerkosten für Ihr Unternehmen sind. Wenn Sie eine hochwertige Aktion starten, sollten Sie nur Nichtkäufer:innen (also False Positives) ansprechen und dazu die linke Seite des Charts bevorzugen. Oder Sie möchten Käufer:innen, die häufig kaufen (True Positives), dazu ermutigen, dies wieder zu tun, indem Sie einen Bereich von Nutzer:innen auswählen, der die rechte Seite des Charts bevorzugt.

## Prognosequalität {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Event-Korrelationstabelle {#correlation_table}

Diese Analyse zeigt Nutzerattribute oder -verhaltensweisen an, die mit Events in der Prognosegruppe korreliert sind. Die bewerteten Attribute sind Alter, Land, Geschlecht und Sprache. Zu den analysierten Verhaltensweisen gehören Sitzungen, Käufe, Gesamtausgaben, angepasste Events sowie Campaigns und Canvas-Schritte, die in den letzten 30 Tagen empfangen wurden.

Die Tabellen sind in links und rechts unterteilt – für höhere bzw. geringere Wahrscheinlichkeit, das Event durchzuführen. Für jede Zeile wird in der rechten Spalte das Verhältnis angezeigt, in dem die Nutzer:innen mit dem Verhalten oder Attribut in der linken Spalte eher oder weniger wahrscheinlich das Event durchführen. Diese Zahl ist das Verhältnis der Wahrscheinlichkeitswerte von Nutzer:innen mit diesem Verhalten oder Attribut geteilt durch die Wahrscheinlichkeit, das Event bei der gesamten Prognosegruppe durchzuführen.

Diese Tabelle wird nur aktualisiert, wenn die Prognose neu trainiert wird, und nicht, wenn die Wahrscheinlichkeitswerte der Nutzer:innen aktualisiert werden.

{% alert note %}
Die Korrelationsdaten für Vorschau-Prognosen werden teilweise ausgeblendet. Um diese Informationen zu erhalten, ist ein Kauf erforderlich. Kontaktieren Sie Ihren Account Manager für weitere Informationen.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### Prognose kann nicht erstellt werden {#unable-to-create-a-prediction}

Sollten Sie keine Prognose für ein angepasstes Event erstellen können, könnte dies an einer unzureichenden Stichprobengröße liegen. Braze schätzt die Anzahl der Nutzer:innen, die das Event durchgeführt haben. Wenn nicht genügend Nutzer:innen das Event durchgeführt haben, liefert die Stichprobe möglicherweise nicht genügend Daten, um das Modell zu trainieren. In diesem Fall kann das System auf keine Nutzer:innen extrapolieren, wodurch die Erstellung von Prognosen verhindert wird.

Um eine erfolgreiche Prognose zu erstellen, stellen Sie sicher, dass eine ausreichende Anzahl von Nutzer:innen in Ihrer Prognosegruppe Ihr angepasstes Ziel-Event durchgeführt hat. Der genaue Schwellenwert variiert, jedoch liefern Events mit sehr geringer Nutzung in Ihrer Nutzerbasis möglicherweise nicht genügend Daten für ein zuverlässiges Modelltraining.