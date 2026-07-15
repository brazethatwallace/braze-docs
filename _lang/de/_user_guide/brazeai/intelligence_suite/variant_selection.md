---
nav_title: Variantenauswahl
article_title: Variantenauswahl
page_order: 1.6
description: "Dieser Artikel behandelt die BrazeAI<sup>TM</sup>-Variantenauswahl, ein Feature, das Ihren A/B-Campaigns ermöglicht, automatisch für das beste Engagement zu optimieren."
search_rank: 10
toc_headers: h2
---

# BrazeAI<sup>TM</sup>-Variantenauswahl {#variant-selection}

> Die BrazeAI<sup>TM</sup>-Variantenauswahl ist ein Feature, das Ihren einmaligen oder wiederkehrenden A/B-Tests ermöglicht, automatisch ein Experiment durchzuführen und für die besten Engagement-Ergebnisse zu optimieren.

{% alert note %}
Die BrazeAI<sup>TM</sup>-Variantenauswahl ist derzeit nur für Push verfügbar.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um die BrazeAI<sup>TM</sup>-Variantenauswahl zu verwenden, benötigen Sie Folgendes in Ihrer Campaign oder Ihrem Canvas:

{% tabs %}
{% tab Campaign %}
- Fügen Sie mindestens zwei Nachrichtenvarianten hinzu.
- Wenn Sie keinen Einzelversand verwenden, definieren Sie mindestens ein Konversions-Event und setzen Sie Ihr Fenster für die erneute Berechtigung auf 24 Stunden oder länger. Kürzere Fenster werden nicht unterstützt, da sie die Integrität der Kontrollvariante beeinträchtigen würden.
{% endtab %}

{% tab Canvas %}
- Fügen Sie mindestens zwei Nachrichtenvarianten in einem Nachrichtenschritt hinzu.
- Wenn Sie keinen Einzelversand verwenden, benötigen Sie mindestens ein Konversions-Event.
{% endtab %}
{% endtabs %}

## Einzelversand {#single-send}

Nachdem Sie Ihre zweite Variante hinzugefügt haben, schaltet sich die BrazeAI<sup>TM</sup>-Variantenauswahl automatisch ein, legt optimale Parameter für das Experiment fest (wir haben eine Steigerung von ca. 25 % bei Verwendung der optimalen Parameter beobachtet), führt Ihr Experiment durch und sendet dann die Gewinnervariante. Sie müssen nichts weiter tun.

Um Ihr Experiment anzupassen, bieten wir die folgenden Anpassungsmöglichkeiten:

### Optimierungsziel {#optimization-goal}

Wir empfehlen die Verwendung von Öffnungen, es sei denn, Sie haben ein starkes Konversions-Event-Setup mit einer aussagekräftigen Anzahl von Conversions, damit der Algorithmus die Daten hat, die er für die besten Ergebnisse benötigt.
- Öffnungen
- Konversions-Events

### Experimentdauer {#experiment-duration}

Wir empfehlen die Verwendung der Standardeinstellung; wir bieten jedoch zwei weitere Optionen an, einschließlich der Möglichkeit, eine eigene benutzerdefinierte Dauer zu verwenden:
- 4 Stunden
- 24 Stunden
- 72 Stunden
- Benutzerdefiniert

### Kontrollgruppe und Variantenverteilungen {#control-group-and-variant-distributions}

Sie können eine Kontrollgruppe entfernen oder die Variantenverteilungen bearbeiten, aber wir empfehlen die Verwendung der von uns festgelegten optimalen Parameter.

![Optimierungsoptionen für Einzelversand-Varianten]({% image_buster /assets/img_archive/braze_ai_variant_selection_single_send_options.png %})

## Wiederkehrend {#recurring}

Nachdem Sie Ihre zweite Variante hinzugefügt haben, schaltet sich die BrazeAI<sup>TM</sup>-Variantenauswahl automatisch ein und optimiert kontinuierlich mithilfe eines statistischen Multi-Armed-Bandit-Tests. Sie sendet mehr Nachrichten an die Varianten, die besser abschneiden, und weniger an diejenigen, die schlechter abschneiden.

Sie beginnt mit einer gleichmäßigen Verteilung zum Trainieren und Optimieren und verschiebt dann zweimal täglich die Verteilung in Richtung der leistungsstarken Varianten und weg von den leistungsschwachen, bis sie genügend Evidenz gesammelt hat, um mit ausreichender Konfidenz (95 %+) sicher zu sein, dass sie die optimale Verteilung gewählt hat.

## Berichterstattung {#reporting}

![Uplift-Berichterstattung]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Nach Abschluss des Tests für den Einzelversand und nach einer kurzen Verzögerung für den wiederkehrenden Versand liegen zuverlässige Daten für die Berichterstattung vor. Wir berichten über jede Steigerung, die die BrazeAI<sup>TM</sup>-Variantenauswahl im Dashboard erzielen konnte.

{% tabs %}
{% tab Einzelversand %}
Nach dem Versand der Trainingskohorte wartet Braze den in der Dauereinstellung festgelegten Zeitraum ab und überprüft die Daten. Basierend auf der Verteilung der konkurrierenden Varianten berechnen wir einen Durchschnitt dessen, wie die Performance ohne Optimierung aussehen würde, und berechnen dann die Steigerung basierend auf der Gewinnervariante.

Zum Beispiel (bei gleichmäßiger Verteilung):
- Variante 1: 3,5 %
- Variante 2: 3 %
- Variante 3: 2,5 %
- Variante 4: 2 %

Die Öffnungsrate ohne Optimierung beträgt 2,75 % (.035\*.25 + .03\*.25 + 0.025\*.25 + 0.02\*.25). Die Variantenauswahl wählt Variante 1 mit 3,5 %, sodass die Steigerung 27,3 % beträgt.
{% endtab %}

{% tab Wiederkehrend %}
Braze analysiert routinemäßig die Ergebnisse, wenn Anpassungen vorgenommen werden, und zeigt die Steigerung basierend auf dem Durchschnitt der Steigerung jedes Zeitraums an.

Wir berechnen die Steigerung des Zeitraums basierend darauf, wie stark wir anpassen, ähnlich wie beim Einzelversand.

Zum Beispiel:
- Variante 1: 3,5 %, 25 % der Kohorte
- Variante 2: 3 %, 25 % der Kohorte
- Variante 3: 2,5 %, 25 % der Kohorte
- Variante 4: 2 %, 25 % der Kohorte

Die Öffnungsrate ohne Optimierung beträgt 2,75 % (.035\*.25 + .03\*.25 + 0.025\*.25 + 0.02\*.25). Die Variantenauswahl gewichtet die leistungsstärkeren Varianten stärker.

Nehmen wir an, sie verteilt wie folgt:
- Variante 1: 65 %
- Variante 2: 15 %
- Variante 3: 10 %
- Variante 4: 5 %

Dies ergibt eine gewählte Öffnungsrate von 3,075 % (.035\*.65 + .03\*.15 + 0.025\*.1 + 0.02\*.05), was einer Steigerung von 11,8 % entspricht. Wir berechnen dies für jeden Zeitraum und bilden dann den Durchschnitt über den gesamten Optimierungszeitraum.
{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen {#faq}

### Warum ist die erneute Berechtigung in weniger als 24 Stunden nicht verfügbar, wenn sie mit der Variantenauswahl für wiederkehrende Campaigns oder Canvases kombiniert wird? {#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-variant-selection-for-recurring-campaigns-or-canvases}

Wir erlauben es nicht, dass Campaigns mit Variantenauswahl eine erneute Berechtigung in einem zu kurzen Fenster haben, da unsere Tests zeigen, dass dies die Integrität der Kontrollvariante beeinträchtigt und möglicherweise zu unerwünschten Verteilungen führt.

### Warum zeigen meine Varianten in den frühen Phasen meiner wiederkehrenden Campaign gleichmäßige Versendungen? {#why-are-my-variants-showing-equal-sends-during-the-early-stages-of-my-recurring-campaign}

Die Variantenauswahl bestimmt die endgültigen Variantenzuweisungen erst nach einer Trainingsphase, in der die Versendungen gleichmäßig über die Varianten verteilt werden. Sie passt sich im Laufe der Zeit an, wenn sie Performance-Trends erkennt. Wenn Sie in den frühen Phasen Ihrer Campaign nicht gleichmäßig versenden möchten, verwenden Sie feste Varianten für einen traditionellen A/B-Test.

### Hört die wiederkehrende Variantenauswahl auf zu optimieren, ohne einen klaren Gewinner zu wählen? {#does-recurring-variant-selection-stop-optimizing-without-picking-a-clear-winner}

Ja, sie hört auf zu optimieren, wenn sie mit 95 % Konfidenz davon ausgeht, dass die Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1 % ihres aktuellen Werts verbessern wird.

### Warum kann ich die Variantenauswahl in meinem Canvas oder meiner Campaign nicht aktivieren? {#why-cant-i-enable-variant-selection-in-my-canvas-or-campaign}

Für den Einzelversand können Sie die Variantenauswahl nicht aktivieren, wenn Ihr Canvas oder Ihre Campaign nur aus einer einzelnen Variante besteht.

Für wiederkehrende Versendungen können Sie die Variantenauswahl nicht aktivieren, wenn:
- Sie keine Konversions-Events zu Ihrer Campaign oder Ihrem Canvas hinzugefügt haben.
- Sie die erneute Berechtigung mit einem Fenster von weniger als 24 Stunden aktiviert haben.
- Ihr Canvas oder Ihre Campaign nur aus einer einzelnen Variante besteht.