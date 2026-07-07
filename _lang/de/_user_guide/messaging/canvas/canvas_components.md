---
nav_title: Canvas-Komponenten
article_title: Canvas-Komponenten
page_order: 3
alias: "/user_guide/messaging/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Canvas-Komponenten"
guide_top_text: "Optimieren Sie Ihre Canvas-Journey mit Canvas-Komponenten. Canvas-Komponenten können verwendet werden, um den Prozess der Effektivitätsmessung Ihres Canvas zu vereinfachen, indem übermäßig viele vollständige Schritte durch nur einen ersetzt werden. Komponenten in Canvas beziehen sich auf die personalisierte Nutzer-Journey in Ihren Canvas-Branches."

page_type: landing
description: "Diese Landing-Page enthält Artikel zu Canvas-Komponenten, die Ihnen helfen, fortgeschrittenere Canvases zu erstellen. Einige dieser Komponenten umfassen den Nachrichten-Schritt, den Verzögerungsschritt, den Decision-Split-Schritt und mehr."
tool: Canvas

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
  - name: Aktionspfade-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/action_paths
    image: /assets/img/braze_icons/zap.svg
  - name: Agent-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/agent_step
    image: /assets/img/braze_icons/briefcase-01.svg
  - name: Zielgruppenpfade-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/audience_paths
    image: /assets/img/braze_icons/users-01.svg
  - name: Audience-Sync-Schritt
    link: /docs/partners/canvas_audience_sync
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Content-Optimizer-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step
    image: /assets/img/braze_icons/target-04.svg
  - name: Kontext-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/context
    image: /assets/img/braze_icons/file-search-02.svg
  - name: Decision-Split-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/decision_split
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Verzögerungsschritt
    link: /docs/user_guide/messaging/canvas/canvas_components/delay_step
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Experimentpfade-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step
    image: /assets/img/braze_icons/columns-01.svg
  - name: Feature-Flags
    link: /docs/user_guide/messaging/canvas/canvas_components/feature_flags
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Nachrichten-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/message_step
    image: /assets/img/braze_icons/message-square-02.svg
  - name: An-Ziel-senden-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/send_to_destination
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Nutzeraktualisierungs-Schritt
    link: /docs/user_guide/messaging/canvas/canvas_components/user_update
    image: /assets/img/braze_icons/user-check-01.svg
---

## Über Canvas-Komponenten {#about-canvas-components}

Mit Canvas-Komponenten können Sie neue Nutzer-Journeys erschließen, um Ihre Prozesse zu verbessern und die Effektivität Ihrer Zielgruppenansprache zu steigern.

### Nutzer-Journeys anpassen {#customizing-user-journeys}

![Beispiel einer Canvas-Nutzer-Journey mit einem Decision-Split-Schritt, gefolgt von Verzögerungsschritten und Nachrichten-Schritten.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Verwenden Sie [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), um Ihre Nutzer-Journey basierend auf Aktionen und Engagement-Events wie einem Kauf aufzuteilen. Wenn Sie Ihre Zielgruppen filtern und gezielt ansprechen möchten, helfen [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) dabei, Ihr Nutzer-Targeting zu vereinfachen, indem Ihre Nutzer:innen basierend auf Zielgruppenkriterien auf verschiedene Canvas-Pfade geleitet werden.

[Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Komponenten verwenden eine einfache „Ja oder Nein“-Logik, um zwei sich gegenseitig ausschließende Pfade für Ihre Nutzer-Journeys zu erstellen, die auf einer Aktion oder einem Nutzerattribut basieren. Dies kann Ihnen helfen, Ihre Nutzergruppen zu identifizieren und gezielt anzusprechen.

[Verzögerungs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Komponenten ermöglichen es Ihnen, einen einzelnen Schritt in Ihrem Canvas zu verzögern. Dieser eigenständige Verzögerungsschritt in Ihrem Canvas eignet sich am besten, um Ihren Nutzer:innen Nachrichten zu einem bestimmten Zeitpunkt zu senden. Darüber hinaus können Verzögerungskomponenten auch Ihre Zielgruppenreichweite erhöhen, indem sie Ihrer Zielgruppe mehr Zeit geben, die Kriterien der Komponente zu erfüllen.

### Testen {#testing}

Beim Erstellen Ihrer Nutzer-Journeys möchten Sie möglicherweise auch den effektivsten Canvas-Pfad testen. Mit [Experimentpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) können Sie mehrere Canvas-Pfade an jedem Schritt testen. Sie können auch die Verbindungen zwischen den Schritten als allgemeine Vorschau nutzen. Orangefarbene Verbindungen zeigen an, dass der vorherige Schritt Nutzer:innen sofort zum nächsten Schritt weiterleitet.

### Integration {#integration}

Möchten Sie Ihre First-Party-Nutzerdaten mit Ihrer Marke synchronisieren? Nutzen Sie die verfügbaren Audience-Sync-Optionen für [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) und [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync).