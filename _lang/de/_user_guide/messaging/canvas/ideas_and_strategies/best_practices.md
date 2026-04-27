---
nav_title: Best Practices
article_title: Best Practices für Canvas
page_order: 1
description: "Dieser Artikel enthält einige Best Practices für die Erstellung und Anpassung von Journeys mit Canvas und Canvas Flow."
tool: Canvas

---

# Best Practices für Canvas

> Dieser Artikel enthält einige Best Practices für die Erstellung und Anpassung von Journeys mit Canvas und Canvas Flow.

## Definieren Sie Ihr Ziel

Gehen Sie dem Was, Wer und Warum auf den Grund!
- Was möchten Sie den Nutzer:innen helfen zu erreichen?
- Welche Nutzer:innen möchten Sie ansprechen?
- Warum erstellen Sie dieses Canvas?

## Kombinieren und variieren

Erschließen Sie neue Kombinationen von Journeys mit [Canvas-Komponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/).
- Teilen Sie Ihre Nutzer:innen mit einem [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) auf und erstellen Sie verschiedene Workflows.
- Verteilen Sie Ihre Journeys zeitlich mit einem [Delay]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/)-Schritt.
- Fügen Sie [eigenständige Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) an beliebiger Stelle in Ihrem Canvas-Flow hinzu.

{% alert note %}
Canvas-Schritte können Nutzer:innen nur vorwärts im Flow bewegen. Sie können ein Canvas nicht so konfigurieren, dass ein Schritt mit einem vorherigen Schritt verknüpft wird, da dies Nutzer:innen rückwärts senden würde. Diese Validierung stellt sicher, dass Nutzer:innen sich nur in eine Richtung durch Ihr Canvas bewegen.
{% endalert %}

## Erstellen Sie reichhaltigere Nachrichten

Begeistern Sie Ihre Nutzer:innen mit reichhaltigeren Nachrichten.

- Erstellen Sie [In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) für Onboarding-Canvases, um den ersten Eindruck optimal zu nutzen.
- Integrieren Sie [Content-Cards]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) in eine Canvas-Journey für Aktionen und Push-Benachrichtigungen.

## Testen Sie Ihre Journeys

Ermitteln Sie die Wirkung Ihres Canvas-Messagings, indem Sie Kontrollgruppen einbeziehen. So können Sie nachvollziehen, wie Ihr Canvas aufgenommen wurde!

- Benennen Sie jeden Schritt Ihres Canvas, um Ihre Journey zu identifizieren.
- Nutzen Sie die Komponente [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) in Ihrer Journey, um Nutzer:innen zufällig verschiedenen Pfaden zuzuweisen, die Sie erstellt haben.
- Diversifizieren Sie Ihre Journeys mit Delay- und Message-Schritten, um herauszufinden, welcher Pfad am effektivsten ist.
- Überprüfen Sie die [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), um die Performance jeder Komponente in Ihrer Journey zu sehen.
- [Bearbeiten Sie Ihr Canvas]({{site.baseurl}}/post-launch_edits/) nach dem ersten Start.

## Zeitplanung Ihrer Canvases

{% alert note %}
Canvas verhindert, dass Sie einen geplanten Versand mit einer bereits vergangenen Uhrzeit verwenden. Es ist jedoch möglich, ein Canvas in genau derselben Minute zu starten, in der die Kampagne geplant ist (oder in den Sekunden davor). Dies kann dazu führen, dass das Canvas den geplanten Eintrittszeitpunkt verpasst und Nutzer:innen nicht in das Canvas eintreten. Wir empfehlen, Canvases sofort zu senden, falls Kampagnen innerhalb von Minuten vor dem geplanten Versandzeitpunkt bearbeitet werden.
{% endalert %}

Beachten Sie bei Canvas-Schritten die folgenden Details bei der Zeitplanung Ihres Canvas:

- Änderungen am Zeitplan gelten nur für Nutzer:innen, die nicht bereits darauf warten, den Schritt zu erhalten.
- Änderungen an der Zielgruppe gelten standardmäßig für alle Nutzer:innen, es sei denn, Sie planen Änderungen so, dass sie nur für Nutzer:innen gelten, die nicht darauf warten, den Schritt zu erhalten.
- Wenn Sie ein Canvas bearbeiten, das so geplant ist, dass es sofort nach der Bereitstellung versendet wird, und **Update** auswählen, wird es im Wesentlichen sofort gesendet.