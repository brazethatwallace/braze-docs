---
nav_title: Best Practices
article_title: Best Practices für Canvas
page_order: 1
description: "Dieser Artikel enthält einige Best Practices für die Erstellung und Anpassung von Journeys mit Canvas und Canvas Flow."
tool: Canvas
---

# Best Practices für Canvas {#canvas-best-practices}

> Dieser Artikel enthält einige Best Practices für die Erstellung und Anpassung von Journeys mit Canvas und Canvas Flow.

## Definieren Sie Ihr Ziel {#identify-your-purpose}

Gehen Sie dem Was, Wer und Warum auf den Grund!
- Was möchten Sie den Nutzer:innen helfen zu erreichen?
- Welche Nutzer:innen möchten Sie ansprechen?
- Warum erstellen Sie dieses Canvas?

## Kombinieren und variieren {#mix-and-match}

Erschließen Sie neue Kombinationen von Journeys mit [Canvas-Komponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about).
- Teilen Sie Ihre Nutzer:innen mit einem [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) auf und erstellen Sie verschiedene Workflows.
- Verteilen Sie Ihre Journeys zeitlich mit einem [Delay]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Schritt.
- Fügen Sie [eigenständige Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) an beliebiger Stelle in Ihrem Canvas-Flow hinzu.

{% alert note %}
Canvas-Schritte können Nutzer:innen nur vorwärts im Flow bewegen. Sie können ein Canvas nicht so konfigurieren, dass ein Schritt mit einem vorherigen Schritt verknüpft wird, da dies Nutzer:innen rückwärts senden würde. Diese Validierung stellt sicher, dass Nutzer:innen sich nur in eine Richtung durch Ihr Canvas bewegen.
{% endalert %}

## Erstellen Sie reichhaltigere Nachrichten {#create-richer-messages}

Begeistern Sie Ihre Nutzer:innen mit reichhaltigeren Nachrichten.

- Erstellen Sie [In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) für Onboarding-Canvases, um den ersten Eindruck optimal zu nutzen.
- Integrieren Sie [Content Cards]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas) in eine Canvas-Journey für Aktionen und Push-Benachrichtigungen.

## Testen Sie Ihre Journeys {#test-your-user-journeys}

Ermitteln Sie die Wirkung Ihres Canvas-Messagings, indem Sie Kontrollgruppen einbeziehen. So können Sie nachvollziehen, wie Ihr Canvas aufgenommen wurde!

- Benennen Sie jeden Schritt Ihres Canvas, um Ihre Journey zu identifizieren.
- Nutzen Sie die Komponente [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) in Ihrer Journey, um Nutzer:innen zufällig verschiedenen Pfaden zuzuweisen, die Sie erstellt haben.
- Diversifizieren Sie Ihre Journeys mit Delay- und Message-Schritten, um herauszufinden, welcher Pfad am effektivsten ist.
- Überprüfen Sie die [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics), um die Performance jeder Komponente in Ihrer Journey zu sehen.
- [Bearbeiten Sie Ihr Canvas]({{site.baseurl}}/post-launch_edits) nach dem ersten Start.

## Zeitplanung Ihrer Canvases {#scheduling-your-canvases}

{% alert note %}
Canvas verhindert, dass Sie einen geplanten Versand mit einer bereits vergangenen Uhrzeit verwenden. Es ist jedoch möglich, ein Canvas in genau derselben Minute zu starten, in der die Campaign geplant ist (oder in den Sekunden davor). Dies kann dazu führen, dass das Canvas den geplanten Eintrittszeitpunkt verpasst und Nutzer:innen nicht in das Canvas eintreten. Wir empfehlen, Canvases sofort zu senden, falls Campaigns innerhalb von Minuten vor dem geplanten Versandzeitpunkt bearbeitet werden.
{% endalert %}

{% alert important %}
Wenn Sie Zielgruppen-, Zeitplan- oder Zustellungseinstellungen kurz vor einem geplanten Eintritts- oder Versandfenster ändern, warten einige Nutzer:innen möglicherweise bereits auf einen Schritt oder wurden unter früheren Einstellungen ausgewertet, sodass nicht garantiert ist, dass alle die Änderung übernehmen. Informationen dazu, wie Zeitplanänderungen, Zielgruppenänderungen, **Zum Zeitpunkt der Einreihung auswerten** und die Zustellungszeitpunkte von Message-Schritten zusammenwirken, finden Sie unter [Canvas nach dem Start ändern]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch). Im Zweifelsfall stoppen Sie das Canvas, duplizieren Sie es und starten Sie es neu, um eine saubere Neuauswertung zu gewährleisten.
{% endalert %}

Beachten Sie bei Canvas-Schritten die folgenden Details bei der Zeitplanung Ihres Canvas:

- Änderungen am Zeitplan gelten nur für Nutzer:innen, die nicht bereits darauf warten, den Schritt zu erhalten.
- Änderungen an der Zielgruppe gelten standardmäßig für alle Nutzer:innen, es sei denn, Sie planen Änderungen so, dass sie nur für Nutzer:innen gelten, die nicht darauf warten, den Schritt zu erhalten.
- Wenn Sie ein Canvas bearbeiten, das so geplant ist, dass es sofort nach der Bereitstellung versendet wird, und **Update** auswählen, wird es im Wesentlichen sofort gesendet.

### Bearbeitungen nach dem Start {#post-launch-edits}

Wenn Sie ein aktives Canvas stoppen, während ein nicht gespeicherter Entwurf vorhanden ist, kann das Stoppen diesen Entwurf verwerfen. Speichern, starten oder verwerfen Sie den Entwurf, bevor Sie stoppen, wenn Sie laufende Bearbeitungen beibehalten möchten.

#### Zeitpunkt der Zielgruppenauswertung {#audience-evaluation-timing}

Braze wertet Zielgruppen an verschiedenen Stellen im Canvas-Builder und in einzelnen Schritten aus. Weitere Informationen zur Einrichtung finden Sie unter:

- [Legen Sie Ihre Eintritts-Zielgruppe fest]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-13-set-your-target-entry-audience) und [Bestimmen Sie Ihren Canvas-Entry-Zeitplan]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) beim Erstellen eines Canvas
- [Wie Zielgruppe und Eintrittskriterien zusammenwirken]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users#how-target-audience-and-entry-criteria-work-together)
- [Zustellungseinstellungen bearbeiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) für Message-Schritte
- [Wie Nutzer:innen ausgewertet werden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths#how-users-are-evaluated) für Zielgruppenpfade-Schritte

Wenn Sie ein aktives Canvas kurz vor einem geplanten Eintritts- oder Versandfenster bearbeiten, übernehmen Nutzer:innen, die bereits für einen **Message**-Schritt in der Warteschlange stehen, Ihre Änderungen möglicherweise nicht. Weitere Informationen finden Sie unter [Canvases nach dem Start bearbeiten]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch).