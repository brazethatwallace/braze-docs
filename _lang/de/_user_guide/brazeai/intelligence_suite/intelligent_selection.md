---
nav_title: Intelligente Auswahl
article_title: Intelligente Auswahl
page_order: 1.0
description: "Dieser Artikel behandelt die intelligente Auswahl, ein Feature, das die Performance einer wiederkehrenden Campaign oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer:innen, die jede Nachrichtenvariante erhalten, automatisch anpasst."
search_rank: 10
toc_headers: h2
---

# Intelligente Auswahl {#intelligent-selection}

> Intelligente Auswahl ist ein Feature, das die Performance einer wiederkehrenden Campaign oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer:innen, die jede Nachrichtenvariante erhalten, automatisch anpasst.

## Voraussetzungen {#prerequisites}

{% tabs %}
{% tab Campaign %}
Bevor Sie die intelligente Auswahl zu Ihrer Campaign hinzufügen, stellen Sie sicher, dass alles korrekt eingerichtet ist:

- Ihre Campaign sendet nach einem wiederkehrenden Zeitplan. Einmalig versendete Campaigns werden nicht unterstützt.
- Sie haben mindestens zwei Nachrichtenvarianten hinzugefügt.
- Sie haben ein Konversions-Event definiert, um die Performance über die Varianten hinweg zu messen.
- Das Zeitfenster für die erneute Anspruchsberechtigung ist auf 24 Stunden oder länger festgelegt. Kürzere Fenster werden nicht unterstützt, da sie die Integrität der Kontrollvariante beeinträchtigen würden. Weitere Informationen finden Sie in den [FAQ zur intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
Um die intelligente Auswahl in einem Canvas zu verwenden, bestätigen Sie Folgendes:
- Ihr Canvas enthält mindestens zwei Nachrichtenvarianten in einem Nachrichtenschritt.
- Sie haben mindestens ein Konversions-Event hinzugefügt.
{% endtab %}
{% endtabs %}

## Über die intelligente Auswahl {#about-intelligent-selection}

Eine Variante, die anscheinend besser abschneidet als andere, wird an mehr Nutzer:innen gesendet, während Varianten mit schwächerer Performance an weniger Nutzer:innen gesendet werden. Jede Anpassung erfolgt mithilfe eines [statistischen Algorithmus](https://en.wikipedia.org/wiki/Multi-armed_bandit), der sicherstellt, dass Braze echte Performance-Unterschiede berücksichtigt und nicht nur zufällige Schwankungen.

![Abschnitt „A/B-Tests“ einer Campaign mit aktivierter intelligenter Auswahl.]({% image_buster /assets/img/intelligent_selection1.png %})

Die intelligente Auswahl wird:
- Wiederholt Performance-Daten analysieren und den Campaign-Traffic schrittweise auf die Gewinnervarianten verlagern.
- Sicherstellen, dass mehr Nutzer:innen Ihre leistungsstärkste Variante erhalten, ohne die statistische Sicherheit zu beeinträchtigen.
- Varianten mit schwacher Performance ausschließen und Varianten mit hoher Performance schneller identifizieren als ein [herkömmlicher A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing).
- Häufiger und mit größerer Zuversicht testen, dass Ihre Nutzer:innen Ihre beste Nachricht sehen.

Die intelligente Auswahl funktioniert am besten bei Campaigns, die mehr als einmal gesendet werden. Die Funktion benötigt frühe Performance-Daten, um mit der Optimierung zu beginnen, sodass einmalig versendete Campaigns nicht davon profitieren. Für diese Campaigns empfehlen wir stattdessen einen herkömmlichen [A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing).


Sie können Ihren Campaigns und Canvases eine intelligente Auswahl hinzufügen.

{% tabs %}
{% tab Campaign %}
Die intelligente Auswahl kann zu jeder Multi-Send-Campaign im Schritt **Zielgruppe** des Braze-Campaign-Composers hinzugefügt werden. Campaigns, die nur einmal senden, können dieses Feature nicht nutzen.

{% alert note %}
Die intelligente Auswahl kann nicht in Campaigns mit einer Wiederzulassungsfrist von weniger als 24 Stunden verwendet werden, da sie die Integrität der Kontrollvariante beeinträchtigen würde. Weitere Informationen finden Sie in den [Intelligence-FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Fügen Sie mindestens ein Konversions-Event und zwei Varianten zu Ihrem Canvas hinzu. Wählen Sie dann im Build-Schritt einen der Varianten-Prozentsätze aus.

![Ein Canvas mit zwei Varianten, die jeweils auf 50 % Variantenverteilung eingestellt sind, sodass die intelligente Auswahl aktiviert werden kann.]({% image_buster /assets/img/intelligent_selection.png %})

Damit können Sie die Variantenverteilung bearbeiten und die intelligente Auswahl einschalten.

![Die Option „Intelligente Auswahl“ ist für ein Canvas aktiviert.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Die intelligente Auswahl ist nicht verfügbar, wenn Sie Ihrem Canvas noch keine Konversions-Events hinzugefügt haben oder wenn Ihr Canvas aus einer einzelnen Variante besteht.

{% alert note %}
Canvases können die intelligente Auswahl mit aktivierter Wiederzulassung verwenden, aber Braze kann nicht garantieren, dass Nutzer:innen bei erneutem Eintritt dieselbe Variante erhalten, da sich die optimale Zuweisung im Laufe der Zeit verschiebt. Campaigns erfordern ein Wiederzulassungsfenster von 24 Stunden oder länger, wenn die intelligente Auswahl aktiviert ist. Weitere Informationen finden Sie unter [Warum ist die Wiederzulassung in weniger als 24 Stunden in Kombination mit intelligenter Auswahl nicht verfügbar?](#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}
{% endtabs %}

## Laufzeit {#run-time}

Bei Campaigns und Canvases läuft die intelligente Auswahl so lange, bis sie genügend Erkenntnisse über die „wahren“ Konversionsraten der Varianten gesammelt hat. „Genug“ wird durch eine spezielle Metrik namens „Regret“ bestimmt. Sie können sich das ähnlich wie Konfidenz vorstellen: Die intelligente Auswahl schaltet sich von selbst ab, wenn genügend Daten vorhanden sind, um zu wissen, welche Variante die beste ist.

In den meisten Fällen wird die intelligente Auswahl eine der Varianten als Gewinnervariante auswählen. Diese Variante erhält 100 % der Zielgruppe für zukünftige Sendungen.

{% alert note %}
Es ist möglich, dass die intelligente Auswahl die Optimierung beendet, ohne eine einzelne klare Gewinnervariante auszuwählen. Die intelligente Auswahl stellt die Optimierung ein, wenn sie mit 95-prozentiger Sicherheit davon ausgehen kann, dass die Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1 % der aktuellen Rate verbessern wird.
{% endalert %}

## Variantenverteilung der intelligenten Auswahl {#intelligent-selection-variant-distribution}

Die intelligente Auswahl basiert ihre Variantenverteilung auf dem aktuellen Stand der Campaign-Conversions. Sie bestimmt die endgültigen Verteilungen erst nach der Trainingsphase.

Das bedeutet, dass in der Anfangsphase der Campaign sowohl die 99-%-Variante als auch die 1-%-Variante der intelligenten Auswahl ungefähr gleich viele Sendungen erhalten können, die endgültigen Prozentsätze für die Variantenzuweisung jedoch auf 99 % zu 1 % festgelegt werden können.

Wenn Sie nicht möchten, dass die intelligente Auswahl in der Anfangsphase der Campaign 50/50 verteilt, empfehlen wir die Verwendung eines herkömmlichen A/B-Tests mit festen Varianten.

## Häufig gestellte Fragen {#faq}

### Warum ist die Wiederzulassung in weniger als 24 Stunden in Kombination mit intelligenter Auswahl nicht verfügbar? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection}

Wir lassen nicht zu, dass Campaigns mit intelligenter Auswahl in einem zu kurzen Zeitfenster erneut zugelassen werden, da dies die Integrität der Kontrollvariante beeinträchtigen würde. Durch eine Lücke von 24 Stunden stellen wir sicher, dass der Algorithmus mit einem statistisch validen Datensatz arbeiten kann.

Normalerweise führen Campaigns mit Wiederzulassung dazu, dass Nutzer:innen dieselbe Variante erneut erhalten, die sie zuvor bekommen haben. Bei der intelligenten Auswahl kann Braze nicht garantieren, dass Nutzer:innen dieselbe Kampagnenvariante erhalten, da sich die Variantenverteilung aufgrund der optimalen Zuweisung für dieses Feature verschoben hätte. Würde es Nutzer:innen erlaubt, erneut einzutreten, bevor die intelligente Auswahl die Performance der Varianten überprüft, könnten die Daten durch die erneut eingetretenen Nutzer:innen verzerrt werden.

Zum Beispiel, wenn eine Campaign diese Varianten verwendet:

- Variante A: 20 %
- Variante B: 20 %
- Kontrollgruppe: 60 %

Dann könnte die Variantenverteilung für die zweite Runde wie folgt aussehen:

- Variante A: 15 %
- Variante B: 25 %
- Kontrollgruppe: 60 %

### Warum zeigen meine Varianten der intelligenten Auswahl in der Anfangsphase meiner Campaign gleiche Sendungen an? {#why-are-my-intelligent-selection-variants-showing-equal-sends-during-the-early-stages-of-my-campaign}

Die intelligente Auswahl weist Varianten für den Versand auf Grundlage des aktuellen Stands der Campaign-Conversions zu. Sie bestimmt die endgültigen Variantenzuweisungen erst nach einer Trainingsphase, in der die Sendungen gleichmäßig auf die Varianten verteilt werden. Wenn Sie nicht möchten, dass die intelligente Auswahl in den frühen Phasen Ihrer Campaign gleichmäßig sendet, verwenden Sie feste Varianten für einen herkömmlichen A/B-Test.

### Wird die intelligente Auswahl aufhören zu optimieren, ohne einen klaren Gewinner zu ermitteln? {#will-intelligent-selection-stop-optimizing-without-picking-a-clear-winner}

Die intelligente Auswahl stellt die Optimierung ein, wenn sie mit 95-prozentiger Sicherheit davon ausgehen kann, dass die Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1 % der aktuellen Rate verbessern wird.

### Warum kann ich die intelligente Auswahl in meinem Canvas oder meiner Campaign nicht aktivieren (ausgegraut)? {#why-cant-i-enable-intelligent-selection-in-my-canvas-or-campaign-grayed-out}

Die intelligente Auswahl ist nicht verfügbar, wenn:

- Sie keine Konversions-Events zu Ihrer Campaign oder Ihrem Canvas hinzugefügt haben
- Sie eine einmalig versendete Campaign erstellen
- Sie die Wiederzulassung mit einem Zeitfenster von weniger als 24 Stunden aktiviert haben
- Ihr Canvas aus einer einzelnen Variante besteht, der keine weiteren Varianten oder Kontrollgruppen hinzugefügt wurden
- Ihr Canvas aus einer einzelnen Kontrollgruppe besteht, der keine Varianten hinzugefügt wurden