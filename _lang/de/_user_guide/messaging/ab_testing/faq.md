---
nav_title: FAQ
article_title: FAQ zu multivariaten und A/B-Tests
page_order: 21
page_type: reference
toc_headers: h2
description: "Dieser Artikel behandelt häufig gestellte Fragen zu multivariaten und A/B-Tests mit Braze."
---

# FAQ zu multivariaten und A/B-Tests {#multivariate-and-ab-test-faq}

> Dieser Artikel behandelt häufig gestellte Fragen zu multivariaten und A/B-Tests mit Braze.

## Grundlagen des Testens {#testing-basics}

### Was ist der Unterschied zwischen A/B-Tests und multivariaten Tests? {#what-is-the-difference-between-ab-testing-and-multivariate-testing}

#### A/B-Tests {#ab-testing}

Bei A/B-Tests experimentiert der Marketer mit einer einzelnen Variablen innerhalb der Kampagne (z. B. E-Mail-Betreffzeilen oder Versandzeitpunkt der Nachricht). Dabei wird eine Teilmenge der Zielgruppe zufällig in zwei oder mehr Gruppen aufgeteilt, jeder Gruppe eine andere Variante präsentiert und beobachtet, welche Variante die höchste Konversionsrate aufweist. In der Regel wird die am besten performende Variante anschließend an den Rest der Zielgruppe gesendet.

#### Multivariate Tests {#multivariate-testing}

Multivariate Tests sind eine Erweiterung von A/B-Tests, die es dem Marketer ermöglichen, mehrere Variablen gleichzeitig zu testen, um die effektivste Kombination zu ermitteln. Sie könnten beispielsweise die Betreffzeile Ihrer E-Mail-Nachricht, das Bild, das Ihren Text begleitet, und die Farbe des CTA-Buttons testen. Diese Art von Test ermöglicht es Ihnen, mehr Variablen und Variationskombinationen innerhalb eines einzelnen Experiments zu untersuchen und schneller sowie umfassender Insights zu gewinnen als bei A/B-Tests. Allerdings erfordert das Testen von mehr Variablen und Kombinationen innerhalb eines einzelnen Experiments eine größere Zielgruppe, um statistische Signifikanz zu erreichen.

### Wie werden A/B-Testergebnisse berechnet? {#how-are-ab-test-results-calculated}

Braze testet alle Varianten gegeneinander mit Pearsons Chi-Quadrat-Tests, die messen, ob eine Variante alle anderen statistisch signifikant bei einem Signifikanzniveau von p < 0,05 übertrifft – was wir als 95%ige Signifikanz bezeichnen. Unter allen Varianten, die diese Signifikanzschwelle überschreiten, wird die am besten performende Variante als „Gewinner“ bestimmt.

Dies ist ein separater Test vom Konfidenzwert, der nur die Performance einer Variante im Vergleich zur Kontrollgruppe mit einem numerischen Wert zwischen 0 und 100 % beschreibt. Konkret gibt er an, wie zuversichtlich wir sind, dass der standardisierte Unterschied in der Konversionsrate zwischen Variante und Kontrollgruppe signifikant größer als zufällig ist.

### Warum ist die Variantenverteilung nicht gleichmäßig? {#why-isnt-the-variant-distribution-even}

Die Variantenzuweisung wird bei jedem Versand zufällig vorgenommen, sodass die tatsächliche Aufteilung möglicherweise nicht exakt Ihren konfigurierten Prozentsätzen entspricht – insbesondere bei kleineren Stichprobengrößen. Weitere Informationen finden Sie unter [Variantenverteilung]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution/).

## Tests durchführen und abschließen {#running-and-concluding-tests}

### Wann ist der erste Test abgeschlossen? {#when-is-the-initial-test-over}

Bei Verwendung der Gewinnervariante für einmalige Campaigns ist der Test abgeschlossen, wenn der Versandzeitpunkt der Gewinnervariante erreicht ist. Braze bestimmt eine Variante als Gewinner, wenn sie die höchste Konversionsrate mit einem statistisch signifikanten Vorsprung aufweist.

Für wiederkehrende, aktionsbasierte und API-getriggerte Campaigns können Sie die Intelligente Auswahl verwenden, um die Performance-Daten jeder Variante kontinuierlich zu verfolgen und den Campaign-Traffic fortlaufend auf die am besten performenden Varianten zu optimieren. Bei der Intelligenten Auswahl definieren Sie nicht explizit eine Experimentgruppe, in der Nutzer:innen zufällige Varianten erhalten – stattdessen verfeinert der Braze-Algorithmus kontinuierlich seine Einschätzung der am besten performenden Variante, was eine schnellere Auswahl des Top-Performers ermöglichen kann.

### Wie geht Braze mit Nutzer:innen um, die eine Nachrichtenvariante in einer wiederkehrenden Kampagne oder einem Canvas-Eingangsschritt erhalten haben? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Nutzer:innen werden zufällig einer bestimmten Variante zugewiesen, bevor sie die Kampagne zum ersten Mal erhalten. Jedes weitere Mal, wenn die Kampagne empfangen wird (oder die Nutzer:innen erneut in eine Canvas-Variante eintreten), erhalten sie dieselbe Variante, es sei denn, die Variantenprozentsätze wurden geändert. Wenn sich die Variantenprozentsätze ändern, können Nutzer:innen anderen Varianten zugewiesen werden. Nutzer:innen bleiben in diesen Varianten, bis die Prozentsätze erneut geändert werden. Nutzer:innen werden nur für die Varianten neu verteilt, die bearbeitet wurden.

Nehmen wir beispielsweise an, wir haben eine Kampagne oder ein Canvas mit drei Varianten. Wenn nur Variante A und Variante B geändert oder aktualisiert werden, werden Nutzer:innen in Variante C nicht neu verteilt, da der Variantenprozentsatz von Variante C nicht geändert wurde. Kontrollgruppen bleiben konsistent, wenn der Variantenprozentsatz unverändert bleibt. Nutzer:innen, die zuvor Nachrichten erhalten haben, können bei einem späteren Versand nicht in die Kontrollgruppe gelangen, und keine Nutzer:innen in der Kontrollgruppe können jemals eine Nachricht erhalten.

{% alert note %}
Nutzer:innen können als „Nachricht erhalten“ markiert werden, wenn sie einen Kanalbezeichner (z. B. eine E-Mail-Adresse oder Telefonnummer) mit jemandem teilen, der die Nachricht erhalten, geöffnet oder angeklickt hat.
{% endalert %}

#### Was ist mit Experimentpfaden? {#what-about-experiment-paths}

Dasselbe gilt, da die Canvas-Pfade nach einem Experiment ebenfalls Varianten sind.

#### Kann ich Maßnahmen ergreifen, um Nutzer:innen in Campaigns und Canvases neu zu verteilen? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

Die einzige Möglichkeit, Nutzer:innen in Canvases neu zu verteilen, ist die Verwendung von [zufälligen Pfaden in Experimentpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), die bei erneutem Eintritt in das Canvas immer die Pfadzuweisungen zufällig neu vergeben. Dies ist jedoch kein Standardexperiment und könnte Experimentergebnisse ungültig machen, da die Kontrollgruppe durch Treatment-Nutzer:innen kontaminiert werden kann.

## Konfidenz und Verzerrung {#confidence-and-bias}

### Steigt die Konfidenz im Laufe der Zeit? {#does-confidence-increase-over-time}

Die Konfidenz steigt im Laufe der Zeit, wenn alle anderen Faktoren konstant bleiben. Konstant halten bedeutet, dass es keine anderen Marketing-Faktoren gibt, die die Varianten beeinflussen könnten, wie z. B. wenn Variante A über einen 25%-Rabatt spricht, der mitten im Test endet.

Konfidenz ist ein Maß dafür, wie zuversichtlich Braze ist, dass sich die Variante von der Kontrollgruppe unterscheidet. Je mehr Nachrichten gesendet werden, desto größer wird die statistische Aussagekraft des Tests, was die Zuversicht erhöht, dass gemessene Performance-Unterschiede nicht auf Zufall zurückzuführen sind. Im Allgemeinen erhöht eine größere Stichprobengröße unsere Zuversicht, kleinere Performance-Unterschiede zwischen Varianten und Kontrollgruppe zu identifizieren.

### Können Kontrollgruppen- und Testgruppenzuweisungen eine Verzerrung in Tests einführen? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

Es gibt praktisch keine Möglichkeit, dass die Attribute oder Verhaltensweisen von Nutzer:innen vor der Erstellung einer bestimmten Kampagne oder eines Canvas systematisch zwischen Varianten und Kontrollgruppe variieren könnten.

Um Nutzer:innen Nachrichtenvarianten, Canvas-Varianten oder ihren jeweiligen Kontrollgruppen zuzuweisen, verknüpfen wir zunächst ihre zufällig generierte Nutzer-ID mit der zufällig generierten Campaign- oder Canvas-ID. Anschließend wenden wir einen SHA-256-Hashing-Algorithmus an, teilen das Ergebnis durch 100 und behalten den Rest (auch bekannt als Modulo mit 100). Schließlich ordnen wir die Nutzer:innen in Segmente ein, die den im Dashboard gewählten Prozentsätzen für Varianten (und optionale Kontrollgruppe) entsprechen.

### Warum kann ich Rate-Limiting nicht mit einer Kontrollgruppe verwenden? {#why-cant-i-use-rate-limiting-with-a-control-group}

Braze unterstützt derzeit kein Rate-Limiting bei A/B-Tests mit einer Kontrollgruppe. Dies liegt daran, dass Rate-Limiting nicht auf die gleiche Weise auf die Kontrollgruppe angewendet wird wie auf die Varianten, was zu einer Verzerrung führt. Erwägen Sie stattdessen die Verwendung der [Intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection/), die den Prozentsatz der Nutzer:innen, die jede Variante erhalten, automatisch auf Basis von Analytics und der Performance der Campaign anpasst.