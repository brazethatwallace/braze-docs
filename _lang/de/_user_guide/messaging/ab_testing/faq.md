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

Beim A/B-Test experimentiert der Marketer mit einer einzelnen Variablen innerhalb der Campaign (z. B. E-Mail-Betreffzeilen oder Versandzeitpunkt der Nachricht). Dabei wird eine Teilmenge der Zielgruppe zufällig in zwei oder mehr Gruppen aufgeteilt, jeder Gruppe eine andere Variante präsentiert und beobachtet, welche Variante die höchste Konversionsrate aufweist. In der Regel wird die leistungsstärkste Variante anschließend an den Rest der Zielgruppe gesendet.

#### Multivariater Test {#multivariate-testing}

Ein multivariater Test ist eine Erweiterung des A/B-Tests, bei dem der Marketer mehrere Variablen gleichzeitig testen kann, um die effektivste Kombination zu ermitteln. Sie könnten beispielsweise die Betreffzeile Ihrer E-Mail, das Bild, das Ihren Text begleitet, und die Farbe des CTA-Buttons testen. Diese Art von Test ermöglicht es Ihnen, mehr Variablen und Variationskombinationen innerhalb eines einzelnen Experiments zu untersuchen und schneller sowie umfassender Insights zu gewinnen als bei A/B-Tests. Allerdings erfordert das Testen von mehr Variablen und Kombinationen innerhalb eines einzelnen Experiments eine größere Zielgruppe, um statistische Signifikanz zu erzielen.

### Wie werden die Ergebnisse von A/B-Tests berechnet? {#how-are-ab-test-results-calculated}

Braze vergleicht alle Varianten untereinander mithilfe des Chi-Quadrat-Tests nach Pearson, der misst, ob eine Variante statistisch alle anderen auf einem Signifikanzniveau von p < 0,05 übertrifft – was wir als 95%ige Signifikanz bezeichnen. Unter allen Varianten, die diese Signifikanzschwelle überschreiten, wird die leistungsstärkste Variante als „Gewinnerin“ bestimmt.

Dies ist ein separater Test vom Konfidenzwert, der nur die Performance einer Variante im Vergleich zur Kontrollgruppe mit einem numerischen Wert zwischen 0 und 100 % beschreibt. Konkret gibt er an, wie sicher wir sind, dass der standardisierte Unterschied in der Konversionsrate zwischen Variante und Kontrollgruppe signifikant größer ist als der Zufall.

### Warum ist die Variantenverteilung nicht gleichmäßig? {#why-isnt-the-variant-distribution-even}

Die Variantenzuweisung wird bei jedem Versand zufällig bestimmt, sodass die tatsächliche Aufteilung möglicherweise nicht exakt mit Ihren konfigurierten Prozentsätzen übereinstimmt – insbesondere bei kleineren Stichprobengrößen. Weitere Informationen finden Sie unter [Variantenverteilung]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/variant_distribution).

## Tests durchführen und abschließen {#running-and-concluding-tests}

### Wann ist der erste Test abgeschlossen? {#when-is-the-initial-test-over}

Bei einer Einzelversand-Campaign mit **Optimieren mit BrazeAI<sup>TM</sup>** endet der erste Test nach der konfigurierten Experimentdauer. BrazeAI<sup>TM</sup> sendet dann die leistungsstärkste Variante an die verbleibende Zielgruppe.

Bei wiederkehrenden, aktionsbasierten und API-getriggerten Campaigns, die mehrfach versendet werden, verfolgt **Optimieren mit BrazeAI<sup>TM</sup>** kontinuierlich die Varianten-Performance und verschiebt den Campaign-Traffic in Richtung leistungsstärkerer Varianten.

### Wie geht Braze mit Nutzer:innen um, die eine Nachrichtenvariante in einer wiederkehrenden Campaign oder einem Canvas-Entry-Schritt erhalten haben? {#how-does-braze-handle-users-who-received-a-message-variant-in-a-recurring-campaign-or-canvas-entry-step}

Nutzer:innen werden vor dem erstmaligen Empfang der Campaign zufällig einer bestimmten Variante zugewiesen. Bei jedem weiteren Empfang der Campaign (oder wenn Nutzer:innen erneut in eine Canvas-Variante eintreten) erhalten sie dieselbe Variante, sofern die Variantenanteile nicht geändert wurden. Falls sich die Variantenanteile ändern, können Nutzer:innen anderen Varianten neu zugewiesen werden. Nutzer:innen verbleiben in diesen Varianten, bis die Anteile erneut geändert werden. Nutzer:innen werden nur für die Varianten umverteilt, die bearbeitet wurden.

Nehmen wir beispielsweise an, wir haben eine Campaign oder ein Canvas mit drei Varianten. Wenn nur Variante A und Variante B geändert oder aktualisiert werden, werden Nutzer:innen in Variante C nicht umverteilt, da der Variantenanteil von Variante C nicht geändert wurde. Kontrollgruppen bleiben konsistent, wenn der Variantenanteil unverändert bleibt. Nutzer:innen, die zuvor Nachrichten erhalten haben, können bei einem späteren Versand nicht in die Kontrollgruppe gelangen, und Nutzer:innen in der Kontrollgruppe können niemals eine Nachricht erhalten.

{% alert note %}
Nutzer:innen können als „Nachricht erhalten“ markiert werden, wenn sie eine Kanalkennung (z. B. eine E-Mail-Adresse oder Telefonnummer) mit jemandem teilen, der die Nachricht erhalten, geöffnet oder angeklickt hat.
{% endalert %}

#### Was gilt für Experimentpfade? {#what-about-experiment-paths}

Dasselbe gilt, da die Canvas-Pfade nach einem Experiment ebenfalls Varianten sind.

#### Kann ich Maßnahmen ergreifen, um Nutzer:innen in Campaigns und Canvases umzuverteilen? {#can-i-take-actions-to-redistribute-users-in-campaigns-and-canvases}

Die einzige Möglichkeit, Nutzer:innen in Canvases umzuverteilen, ist die Verwendung von [Randomisierten Pfaden in Experimentpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#step-1-choose-the-number-of-paths-and-audience-distribution), die bei erneutem Canvas-Eintritt von Nutzer:innen die Pfadzuweisungen stets zufällig festlegen. Dies ist jedoch kein Standardexperiment und könnte die Experimentergebnisse ungültig machen, da die Kontrollgruppe durch Nutzer:innen aus der Behandlungsgruppe kontaminiert werden kann.

## Konfidenz und Verzerrung {#confidence-and-bias}

### Steigt die Konfidenz im Laufe der Zeit? {#does-confidence-increase-over-time}

Die Konfidenz steigt im Laufe der Zeit, wenn alle anderen Faktoren konstant bleiben. Konstant bedeutet, dass es keine anderen Marketing-Faktoren gibt, die die Varianten beeinflussen könnten – zum Beispiel, wenn Variante A einen 25-%-Rabatt bewirbt, der mitten im Test endet.

Konfidenz ist ein Maß dafür, wie sicher Braze ist, dass sich die Variante von der Kontrollgruppe unterscheidet. Mit zunehmender Anzahl gesendeter Nachrichten steigt die statistische Aussagekraft des Tests, was die Konfidenz erhöht, dass gemessene Performance-Unterschiede nicht auf Zufall zurückzuführen sind. Generell erhöht eine größere Stichprobe das Vertrauen, auch kleinere Performance-Unterschiede zwischen Varianten und Kontrollgruppe zu identifizieren.

Wenn sich die Konversionsraten der Varianten und der Kontrollgruppe jedoch annähern (enger zusammenrücken), während mehr Nachrichten gesendet werden, kann die Konfidenz sinken. Das liegt daran, dass der gemessene Unterschied, auf den es ankommt, kleiner wird – und das kann den Vorteil einer größeren Stichprobe überwiegen.

### Können Zuweisungen zu Kontroll- und Testgruppen Verzerrungen bei Tests verursachen? {#can-control-and-test-group-assignments-introduce-bias-to-testing}

Es gibt praktisch keine Möglichkeit, dass die Attribute oder Verhaltensweisen von Nutzer:innen vor der Erstellung einer bestimmten Campaign oder eines Canvas systematisch zwischen Varianten und Kontrollgruppe variieren könnten.

Um Nutzer:innen Nachrichtenvarianten, Canvas-Varianten oder den jeweiligen Kontrollgruppen zuzuweisen, verknüpfen wir zunächst ihre zufällig generierte Nutzer-ID mit der zufällig generierten Campaign- oder Canvas-ID. Anschließend wenden wir einen SHA-256-Hashing-Algorithmus an, teilen das Ergebnis durch 100 und behalten den Rest (auch bekannt als Modulo 100). Schließlich ordnen wir die Nutzer:innen in Segmente ein, die den im Dashboard gewählten prozentualen Zuweisungen für Varianten (und optionale Kontrollgruppe) entsprechen.

### Warum kann ich Rate-Limiting nicht mit einer Kontrollgruppe verwenden? {#why-cant-i-use-rate-limiting-with-a-control-group}

Braze unterstützt derzeit kein Rate-Limiting bei A/B-Tests mit einer Kontrollgruppe. Rate-Limiting wird auf die Kontrollgruppe nicht in gleicher Weise angewendet wie auf die Varianten, was zu Verzerrungen führt. Ziehen Sie stattdessen die Verwendung von [Optimierung mit BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) in Betracht, die den Prozentsatz der Nutzer:innen, die jede Variante erhalten, automatisch basierend auf der Campaign-Performance anpasst.