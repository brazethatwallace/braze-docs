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

# Variantenverteilung

> Wenn Sie einen A/B- oder multivariaten Test einrichten, weist jeder Versand Nutzer:innen unabhängig auf Basis der von Ihnen konfigurierten Prozentsätze den Varianten zu. Da die Zuweisung zufällig erfolgt, stimmt die tatsächliche Verteilung möglicherweise nicht exakt mit Ihren Prozentsätzen überein – insbesondere bei kleineren Stichprobengrößen.

## So funktioniert es

Jedes Mal, wenn eine Nachricht in einer multivariaten Kampagne gesendet wird, wählt das System unabhängig eine zufällige Option gemäß den von Ihnen festgelegten Prozentsätzen aus und weist basierend auf dem Ergebnis eine Variante zu. Es ist wie ein Münzwurf – Abweichungen sind möglich. Wenn Sie schon einmal 100 Mal eine Münze geworfen haben, wissen Sie, dass Sie wahrscheinlich nicht jedes Mal eine exakte 50-50-Verteilung zwischen Kopf und Zahl erhalten, obwohl Sie nur zwei Möglichkeiten haben. Sie könnten 52 Mal Kopf und 48 Mal Zahl erhalten.

Wenn Sie mehrere Varianten haben, die Sie gleichmäßig aufteilen möchten, stellen Sie sicher, dass die Anzahl der Varianten ein Vielfaches von 100 ist. Andernfalls werden einigen Varianten prozentual mehr Nutzer:innen zugewiesen als anderen. Wenn Ihre Kampagne beispielsweise 7 Varianten hat, kann es keine gleichmäßige Variantenverteilung geben, da 7 nicht als ganze Zahl gleichmäßig durch 100 teilbar ist. In diesem Fall hätten Sie 2 Varianten mit 15 % und 5 Varianten mit 14 %.

## Verteilung bei In-App-Nachrichten

Wenn Sie einen A/B-Test mit In-App-Nachrichten durchführen, kann Ihre Analytics eine höhere Variantenverteilung zwischen einer Variante und einer anderen anzeigen, selbst wenn die Prozentsätze gleichmäßig aufgeteilt sind. Betrachten Sie zum Beispiel die folgende Grafik der *eindeutigen Empfänger:innen* für Variante A und Variante C.

![Grafik der eindeutigen Empfänger:innen, die zeigt, dass Variante A durchgehend eine höhere Anzahl als Variante C aufweist, trotz einer gleichmäßigen prozentualen Aufteilung.]({% image_buster /assets/img/variant_distribution_iam.png %})

Variante A hat durchgehend eine höhere Anzahl an *eindeutigen Empfänger:innen* als Variante C. Dies liegt nicht an der Variantenverteilung, sondern daran, wie *eindeutige Empfänger:innen* bei In-App-Nachrichten berechnet werden. Bei In-App-Nachrichten sind *eindeutige Empfänger:innen* tatsächlich *eindeutige Impressionen*, also die Gesamtzahl der Personen, die die In-App-Nachricht erhalten und angesehen haben. Das bedeutet: Wenn Nutzer:innen die Nachricht aus irgendeinem Grund nicht erhalten oder sich entscheiden, sie nicht anzusehen, werden sie nicht in die Zählung der *eindeutigen Empfänger:innen* einbezogen, und die Variantenverteilung kann verzerrt erscheinen.