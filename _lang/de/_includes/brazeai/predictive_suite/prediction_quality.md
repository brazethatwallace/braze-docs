Um die Genauigkeit Ihres Modells zu messen, zeigt Ihnen die Metrik _Prognosequalität_, wie effektiv dieses bestimmte Modell für maschinelles Lernen zu sein scheint, wenn es mit historischen Daten getestet wird. Braze zieht die Daten entsprechend den Gruppen, die Sie auf der Seite zur Modellerstellung angegeben haben. Das Modell wird anhand eines Datensatzes (dem „Trainingsdatensatz“) trainiert und anschließend anhand eines neuen, separaten Datensatzes (dem „Testdatensatz“) getestet.

Die Prognose wird alle zwei Wochen erneut trainiert und zusammen mit der Metrik _Prognosequalität_ aktualisiert, damit Ihre Prognosen immer auf dem neuesten Stand des Nutzer:innenverhaltens sind. Außerdem werden jedes Mal die Prognosen der letzten zwei Wochen mit den tatsächlichen Ergebnissen der Nutzer:innen verglichen. Die _Prognosequalität_ wird dann anhand dieser realen Ergebnisse (und nicht anhand von Schätzungen) berechnet. Dabei handelt es sich um einen automatischen Backtest (d. h. das Testen eines Prognosemodells anhand historischer Daten), um sicherzustellen, dass die Prognose in realen Szenarien korrekt ist. Der Zeitpunkt des letzten Retrainings und Backtests wird auf der Seite **Prognosen** und auf der Analytics-Seite einer einzelnen Prognose angezeigt. Auch eine Vorschau-Prognose führt diesen Backtest einmal nach der Erstellung durch. Auf diese Weise können Sie sich der Genauigkeit Ihrer individuellen Prognose sicher sein, selbst mit der kostenlosen Version des Features.

{% details Beispiel für Prognosequalität %}

Wenn beispielsweise 20 % Ihrer Nutzer:innen im Durchschnitt abwandern und Sie eine zufällige Teilmenge von 20 % Ihrer Nutzer:innen auswählen und diese nach dem Zufallsprinzip als abgewandert bezeichnen (unabhängig davon, ob sie es wirklich sind oder nicht), werden Sie voraussichtlich nur 20 % der tatsächlichen Abgewanderten korrekt identifizieren. Das ist reines Raten. Wenn das Modell nur so gut funktionieren würde, wäre der Lift in diesem Fall 1.

Wenn das Modell es Ihnen hingegen erlauben würde, 20 % der Nutzer:innen anzusprechen und dabei alle „echten“ Abgewanderten zu erfassen und niemanden sonst, wäre der Lift 100 % / 20 % = 5. Wenn Sie dieses Verhältnis für jeden Anteil der wahrscheinlichsten Abgewanderten, die Sie ansprechen könnten, aufzeichnen, erhalten Sie die [Lift-Kurve](https://en.wikipedia.org/wiki/Lift_(data_mining)).

Eine andere Möglichkeit, die Lift-Qualität (und auch die _Prognosequalität_) zu betrachten, ist die Frage, wie weit die Lift-Kurve der Prognose bei der Identifizierung von Abgewanderten im Testdatensatz zwischen zufälligem Raten (0 %) und Perfektion (100 %) liegt. Die Originalarbeit zur Lift-Qualität finden Sie unter [Measuring lift quality in database marketing](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}

### Wie sie gemessen wird {#how-its-measured}

Unser Maß für die _Prognosequalität_ ist die [Lift-Qualität](https://dl.acm.org/doi/10.1145/380995.381018). Im Allgemeinen bezeichnet „Lift“ den erhöhten Anteil oder Prozentsatz eines erfolgreichen Ergebnisses, wie z. B. einer Conversion. In diesem Fall ist das erfolgreiche Ergebnis die korrekte Identifizierung einer Nutzerin oder eines Nutzers, die oder der abgewandert wäre. Die Lift-Qualität ist der durchschnittliche Lift, den die Prognose für alle möglichen Zielgruppengrößen beim Messaging des Testdatensatzes liefert. Dieser Ansatz misst, um wie viel besser als zufälliges Raten das Modell ist. Bei diesem Maß bedeutet 0 %, dass das Modell nicht besser ist als eine zufällige Schätzung, wer abwandern wird, und 100 % bedeutet, dass man genau weiß, wer abwandern wird.

### Empfohlene Bereiche {#recommended-ranges}

Hier finden Sie unsere Empfehlungen für verschiedene Bereiche der _Prognosequalität_:

| Prognosequalität – Bereich (%) | Empfehlung |
| ---------------------- | -------------- |
| 60 – 100 | Ausgezeichnet. Größtmögliche Genauigkeit. Es ist unwahrscheinlich, dass eine Änderung der Zielgruppendefinitionen einen zusätzlichen Nutzen bringt. |
| 40 – 60 | Gut. Dieses Modell generiert genaue Prognosen, aber mit anderen Zielgruppeneinstellungen können eventuell noch bessere Ergebnisse erzielt werden. |
| 20 – 40 | Ausreichend. Dieses Modell kann Genauigkeit und Mehrwert liefern, aber probieren Sie andere Zielgruppendefinitionen aus, um zu sehen, ob sich die Performance verbessert. |
| 0 – 20 | Schlecht. Wir empfehlen, die Zielgruppendefinitionen zu ändern und es erneut zu versuchen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Empfohlene Bereiche" }