---
nav_title: Ruhezeiten
article_title: Ruhezeiten
page_order: 4
page_type: reference
description: "Dieser Referenzartikel behandelt, was Ruhezeiten sind, wie Braze Nachrichten während der Ruhezeit handhabt und wie Ruhezeiten mit intelligentem Timing interagieren."
---

# Ruhezeiten {#quiet-hours}

> Ruhezeiten verhindern, dass Nachrichten während eines festgelegten Zeitfensters gesendet werden. Sie können sie nutzen, um Nutzer:innen nicht zu ungünstigen Zeiten zu kontaktieren (z. B. nachts oder früh morgens), während die Nachrichten trotzdem zu einem optimalen Zeitpunkt außerhalb dieses Fensters zugestellt werden.

Ruhezeiten werden auf Campaign- oder Canvas-Ebene konfiguriert. Sie können auch [Workspace-Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) als Standard für einen Messaging-Kanal in Ihrem gesamten Workspace festlegen (Early Access).

## Funktionsweise von Ruhezeiten {#how-quiet-hours-work}

Wenn Ruhezeiten aktiviert sind und eine Nachricht andernfalls während des eingeschränkten Fensters gesendet würde, hält Braze die Nachricht zurück und stellt sie zum nächsten verfügbaren Zeitpunkt nach Ende der Ruhezeiten zu.

Wenn Ruhezeiten beispielsweise von 22:00 bis 6:00 Uhr gelten und eine Nachricht für 5:30 Uhr geplant ist, stellt Braze sie stattdessen um 6:00 Uhr zu.

{% alert note %}
Ruhezeiten gelten in der Ortszeit jeder Nutzerin und jedes Nutzers.
{% endalert %}

## Ruhezeiten und intelligentes Timing {#quiet-hours-and-intelligent-timing}

Ruhezeiten und intelligentes Timing funktionieren unabhängig voneinander. Die Aktivierung von Ruhezeiten erfordert nicht, dass intelligentes Timing eingeschaltet ist, und umgekehrt gilt dasselbe. Im Allgemeinen empfehlen wir, sich für eine der beiden Optionen zu entscheiden, anstatt beide zusammen zu verwenden, es sei denn, es gibt Richtlinien-, Compliance- oder andere Anforderungen, die Ruhezeiten neben intelligentem Timing erforderlich machen.

- **Ohne intelligentes Timing:** Ruhezeiten fungieren als Nicht-Senden-Fenster für Ihre geplante Sendezeit. Wenn die geplante Zeit in die Ruhezeiten fällt, wird die Nachricht zurückgehalten und gesendet, wenn das Fenster endet.
- **Mit intelligentem Timing:** Braze berechnet weiterhin die optimale Sendezeit für jede Nutzerin und jeden Nutzer. Wenn diese Zeit in die Ruhezeiten fällt, wird die Nachricht zurückgehalten und stattdessen am nächstgelegenen Rand des Ruhezeitfensters zugestellt.

Weitere Informationen zur Konfiguration von Ruhezeiten innerhalb einer Campaign mit intelligentem Timing finden Sie unter [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

## Hinweise {#considerations}

- **Nachrichten werden gleichzeitig gesendet, wenn die Ruhezeiten enden.** Wenn eine große Zielgruppe Nachrichten hat, die während der Ruhezeiten zurückgehalten werden, werden alle diese Nachrichten auf einmal gesendet, sobald das Fenster endet. Berücksichtigen Sie bei zeitkritischen Campaigns, wie sich dies auf den Zustellungszeitpunkt auswirkt.
- **Ruhezeiten sind nicht dasselbe wie das Abbrechen einer Nachricht.** Beim Abbrechen einer Nachricht wird diese vollständig verworfen. Ruhezeiten halten die Nachricht zurück und stellen sie später zu.
- **Ruhezeiten überprüfen die Segment-Zugehörigkeit für eine zurückgehaltene Sendung nicht erneut.** Braze prüft die Segment-Zugehörigkeit, wenn die Nachricht getriggert wird. Wenn die Nutzerin oder der Nutzer zu diesem Zeitpunkt berechtigt ist, hält Braze die Nachricht zurück und sendet sie, wenn die Ruhezeiten enden. Dies ist unabhängig von der [erneuten Überprüfung der Segment-Zugehörigkeit zum Sendezeitpunkt]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#audience-criteria-evaluation) oder den Canvas-[Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Ruhezeiten sind unabhängig von Frequency-Capping und Rate-Limiting.** Jede dieser Zustellungskontrollen wird unabhängig angewendet. Eine Nachricht, die Frequency- und Rate-Limits passiert, kann dennoch durch Ruhezeiten zurückgehalten werden, und eine durch Ruhezeiten zurückgehaltene Nachricht wird beim tatsächlichen Versand gegen Rate-Limits geprüft. Weitere Informationen finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

## Verwandte Artikel {#related-articles}

- [Workspace-Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours)