---
nav_title: Ruhezeiten
article_title: Ruhezeiten
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt, was Ruhezeiten sind, wie Braze Nachrichten während der Ruhezeit handhabt und wie Ruhezeiten mit intelligentem Timing interagieren."
---

# Ruhezeiten {#quiet-hours}

> Ruhezeiten verhindern, dass Nachrichten während eines festgelegten Zeitfensters gesendet werden. Sie können sie nutzen, um Nutzer:innen nicht zu ungünstigen Zeiten zu kontaktieren (z. B. nachts oder früh morgens), während die Nachrichten trotzdem zu einem optimalen Zeitpunkt außerhalb dieses Fensters zugestellt werden.

Ruhezeiten werden auf Campaign- oder Canvas-Ebene konfiguriert.

## Wie Ruhezeiten funktionieren {#how-quiet-hours-work}

Wenn Ruhezeiten aktiviert sind und eine Nachricht andernfalls während des eingeschränkten Fensters gesendet würde, hält Braze die Nachricht zurück und stellt sie zum nächsten verfügbaren Zeitpunkt nach Ende der Ruhezeiten zu.

Wenn die Ruhezeiten beispielsweise von 22:00 bis 6:00 Uhr laufen und eine Nachricht für 5:30 Uhr geplant ist, stellt Braze sie stattdessen um 6:00 Uhr zu.

{% alert note %}
Ruhezeiten gelten in der jeweiligen Ortszeit der Nutzer:innen.
{% endalert %}

## Ruhezeiten und intelligentes Timing {#quiet-hours-and-intelligent-timing}

Ruhezeiten und intelligentes Timing funktionieren unabhängig voneinander. Die Aktivierung von Ruhezeiten erfordert nicht, dass intelligentes Timing eingeschaltet ist, und umgekehrt gilt dasselbe. Generell empfehlen wir, sich für eine der beiden Optionen zu entscheiden, anstatt beide zusammen zu verwenden, es sei denn, es gibt Richtlinien-, Compliance- oder andere Anforderungen, die Ruhezeiten neben intelligentem Timing erforderlich machen.

- **Ohne intelligentes Timing:** Ruhezeiten fungieren als Nicht-Senden-Fenster für Ihre geplante Sendezeit. Wenn die geplante Zeit in die Ruhezeiten fällt, wird die Nachricht zurückgehalten und gesendet, sobald das Fenster endet.
- **Mit intelligentem Timing:** Braze berechnet weiterhin die optimale Sendezeit für jede:n Nutzer:in. Wenn diese Zeit in die Ruhezeiten fällt, wird die Nachricht zurückgehalten und stattdessen am nächstgelegenen Rand des Ruhezeitfensters zugestellt.

Weitere Informationen zur Konfiguration von Ruhezeiten innerhalb einer Campaign mit intelligentem Timing finden Sie unter [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).

## Wichtige Hinweise {#things-to-consider}

- **Nachrichten werden gleichzeitig gesendet, wenn die Ruhezeiten enden.** Wenn bei einer großen Zielgruppe Nachrichten während der Ruhezeiten zurückgehalten werden, werden alle diese Nachrichten auf einmal gesendet, sobald das Fenster endet. Berücksichtigen Sie bei zeitkritischen Campaigns, wie sich dies auf den Zustellungszeitpunkt auswirkt.
- **Ruhezeiten sind nicht dasselbe wie das Abbrechen einer Nachricht.** Das Abbrechen einer Nachricht verwirft sie vollständig. Ruhezeiten halten die Nachricht zurück und stellen sie später zu.
- **Ruhezeiten sind unabhängig von Frequency-Capping und Rate-Limiting.** Jede dieser Zustellungs-Kontrollgruppen wird unabhängig angewendet. Eine Nachricht, die Frequency- und Rate-Limits passiert, kann dennoch durch Ruhezeiten zurückgehalten werden, und eine durch Ruhezeiten zurückgehaltene Nachricht wird beim tatsächlichen Versand erneut gegen Rate-Limits geprüft. Weitere Informationen finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).