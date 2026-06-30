---
nav_title: Variantenverteilung
article_title: Variantenverteilung
page_order: 1
page_type: reference
description: "Dieser Referenzartikel erklärt, wie Braze Nutzer:innen in A/B- und multivariaten Tests auf Varianten verteilt."
tool:
  - Campaign
  - Canvas
---

# Variantenverteilung {#variant-distribution}

> Wenn Sie einen A/B- oder multivariaten Test einrichten, weist jeder Versand Nutzer:innen unabhängig auf Basis der von Ihnen konfigurierten Prozentsätze den Varianten zu. Da die Zuweisung zufällig erfolgt, stimmt die tatsächliche Verteilung möglicherweise nicht exakt mit Ihren Prozentsätzen überein – insbesondere bei kleineren Stichprobengrößen.

## So funktioniert es {#how-it-works}

Die Verteilung zwischen Varianten ist nicht immer gleichmäßig. Jedes Mal, wenn eine Nachricht in einer multivariaten Campaign gesendet wird, wählt Braze unabhängig eine zufällige Option gemäß den von Ihnen festgelegten Prozentsätzen aus und weist basierend auf dem Ergebnis eine Variante zu. Es ist wie ein Münzwurf – Abweichungen sind möglich. Wenn Sie eine Münze 100 Mal werfen, erhalten Sie wahrscheinlich keine exakte 50-50-Verteilung zwischen Kopf und Zahl, obwohl Sie nur zwei Möglichkeiten haben. Sie könnten 52 Mal Kopf und 48 Mal Zahl erhalten.

Wenn Sie mehrere Varianten gleichmäßig aufteilen möchten und dabei ganzzahlige Prozentsätze verwenden, stellen Sie sicher, dass die Anzahl der Varianten 100 gleichmäßig teilt. Andernfalls werden einigen Varianten prozentual mehr Nutzer:innen zugewiesen als anderen. Wenn Ihre Campaign beispielsweise sieben Varianten hat, kann es keine gleichmäßige Variantenverteilung geben, da sieben nicht als ganze Zahl gleichmäßig durch 100 teilbar ist. In diesem Fall hätten Sie zwei Varianten mit 15 % und fünf Varianten mit 14 %.

{% alert tip %}
Um Nutzer:innen in einem Canvas zu verteilen, können Sie einen [Decision-Split-Schritt]({{site.baseurl}}/decision_split) hinzufügen und Nutzer:innen anhand ihrer [zufälligen Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) aufteilen.
{% endalert %}

## Verteilung bei In-App-Nachrichten {#in-app-message-distribution}

Wenn Sie einen A/B-Test mit In-App-Nachrichten durchführen, kann Ihre Analytics eine höhere Variantenverteilung zwischen einer Variante und einer anderen anzeigen, selbst wenn die Prozentsätze gleichmäßig aufgeteilt sind. Betrachten Sie zum Beispiel die folgende Grafik der *eindeutigen Empfänger:innen* für Variante A und Variante C.

![Grafik der eindeutigen Empfänger:innen, die zeigt, dass Variante A durchgehend eine höhere Anzahl als Variante C aufweist, trotz einer gleichmäßigen prozentualen Aufteilung.]({% image_buster /assets/img/variant_distribution_iam.png %})

Variante A hat durchgehend eine höhere Anzahl an *eindeutigen Empfänger:innen* als Variante C. Dies liegt nicht an der Variantenverteilung, sondern daran, wie *eindeutige Empfänger:innen* bei In-App-Nachrichten berechnet werden. Bei In-App-Nachrichten sind *eindeutige Empfänger:innen* tatsächlich *eindeutige Impressionen*, also die Gesamtzahl der Personen, die die In-App-Nachricht erhalten und angesehen haben. Das bedeutet: Wenn Nutzer:innen die Nachricht aus irgendeinem Grund nicht erhalten oder sich entscheiden, sie nicht anzusehen, werden sie nicht in die Zählung der *eindeutigen Empfänger:innen* einbezogen, und die Variantenverteilung kann verzerrt erscheinen.