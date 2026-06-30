---
nav_title: Winning Path
article_title: Winning Path in Experimentpfaden
page_type: reference
description: "Dieser Referenzartikel behandelt Winning Path, ein Feature, mit dem Sie Ihre A/B-Tests automatisieren können, wenn es für einen Experiment-Pfad-Schritt aktiviert ist."
tool: Canvas
---

# Winning Path in Experimentpfaden {#winning-path-in-experiment-paths}

> Winning Path ist vergleichbar mit [Gewinnervariante]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) in Campaigns und ermöglicht es Ihnen, Ihre A/B-Tests zu automatisieren.

Wenn Winning Path in einem Experiment-Pfad-Schritt aktiviert ist, werden nach einem festgelegten Zeitraum alle nachfolgenden Nutzer:innen über den Pfad mit der höchsten Konversionsrate geleitet.

## Winning Path verwenden {#using-winning-path}

### 1. Schritt: Einen Experiment-Pfad-Schritt hinzufügen {#step-1-add-an-experiment-path-step}

Fügen Sie Ihrem Canvas einen [Experiment-Pfad]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) hinzu und aktivieren Sie dann **Winning Path**.

![Einstellungen im Experiment-Pfad mit dem Titel „Nachfolgende Nutzer:innen an den Winning Path weiterleiten“. Der Abschnitt enthält einen Schalter für Winning Path sowie Optionen zur Konfiguration des Konversions-Events und des Experiment-Fensters.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### 2. Schritt: Winning-Path-Einstellungen konfigurieren {#step-2-configure-winning-path-settings}

Legen Sie das Konversions-Event fest, das den Gewinner bestimmen soll. Falls keine Konversions-Events verfügbar sind, kehren Sie zum ersten Schritt der Canvas-Einrichtung zurück und [weisen Sie Konversions-Events zu]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Wenn Sie Öffnungen oder Klicks als Konversions-Event wählen, stellen Sie sicher, dass der erste Schritt im Pfad ein [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) ist. Braze zählt nur das Engagement des ersten Nachrichten-Schritts in jedem jeweiligen Pfad. Wenn der Pfad mit einem anderen Schritt beginnt (z. B. einem Verzögerungs- oder Zielgruppenpfad-Schritt) und die Nachricht erst später kommt, wird diese Nachricht bei der Performance-Bewertung nicht berücksichtigt.

Legen Sie als Nächstes das **Experiment-Fenster** fest. Das **Experiment-Fenster** bestimmt, wie lange das Experiment läuft, bevor der Winning Path ermittelt wird und alle nachfolgenden Nutzer:innen über diesen Pfad geleitet werden. Das Fenster beginnt, wenn die erste Person den Schritt betritt.

![Winning-Path-Einstellungen mit dem ausgewählten Konversions-Event „Klicks“ für ein 12-stündiges Experiment-Fenster.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### 3. Schritt: Fallback festlegen {#statistical-significance}

Standardmäßig werden alle zukünftigen Nutzer:innen über den leistungsstärksten Pfad geleitet, wenn die Testergebnisse nicht ausreichen, um einen statistisch signifikanten Gewinner zu ermitteln. Alternativ können Sie **Alle zukünftigen Nutzer:innen weiterhin über den Mix der Pfade senden** auswählen. Diese Option leitet zukünftige Nutzer:innen gemäß den in der Experiment-Pfad-Verteilung festgelegten Prozentsätzen über den Mix der Pfade.

Bei einem Gleichstand wählt Braze den Pfad aus, der zuerst erscheint.

![„Alle zukünftigen Nutzer:innen weiterhin über den Mix der Pfade senden“ ist ausgewählt als Aktion für den Fall, dass das Testergebnis nicht statistisch signifikant ist.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Eine Verzögerungsgruppe erscheint in Ihrer Pfadverteilung nur, wenn Ihr Canvas für einmaligen Eintritt eingerichtet ist und Ihr Experiment-Schritt drei oder weniger Pfade hat. Wiederkehrende und getriggerte Canvases haben keine Verzögerungsgruppe, wenn Winning Path aktiviert ist.
{% endalert %}

### 4. Schritt: Pfade hinzufügen und den Canvas starten {#step-4-add-your-paths-and-launch-the-canvas}

Eine einzelne Experiment-Pfad-Komponente kann bis zu vier Pfade enthalten. Wenn Ihr Canvas jedoch für [einmaligen Eintritt](#one-time-entry) eingerichtet ist, muss ein Pfad für die Verzögerungsgruppe reserviert werden, die Braze automatisch hinzufügt, wenn Winning Path aktiviert ist. Das bedeutet, dass Sie bei Canvases mit einmaligem Eintritt bis zu drei Pfade zu Ihrem Experiment hinzufügen können.

Schließen Sie die Einrichtung Ihres Canvas nach Bedarf ab und starten Sie ihn. Sobald die erste Person das Experiment betreten hat, können Sie den Canvas überprüfen, um die eingehenden Analytics zu sehen und die [Performance Ihres Experiments zu verfolgen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Nachdem ein Winning Path abgeschlossen ist, werden alle nachfolgenden Nutzer:innen, die den Canvas betreten, über den Winning Path geleitet – einschließlich Nutzer:innen, die erneut eingetreten sind und zuvor in der Kontrollgruppe des Experiment-Pfad-Schritts waren.

## Analytics {#analytics}

Wenn Winning Path aktiviert ist, wird Ihre Analytics-Ansicht in zwei Tabs unterteilt: **Initiales Experiment** und **Winning Path**.

- **Initiales Experiment:** Zeigt die Metriken für jeden Pfad während des Experiment-Fensters, welcher Pfad als Gewinner ausgewählt wurde, und die Canvas-Conversion-Metriken. Das Konversions-Event, das zur Bestimmung des Gewinners verwendet wird und in den Winning-Path-Einstellungen konfiguriert ist, muss nicht mit der in den Canvas-Analytics hervorgehobenen Conversion-Metrik übereinstimmen. Weitere Informationen darüber, wie Experiment-Pfad-Analytics mit Canvas-Konversions-Events und der Gewinner-Metrik zusammenhängen, finden Sie unter [Experimentpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#winning-path-and-personalized-paths-performance).
- **Winning Path:** Zeigt nur die Metriken für den Winning Path ab dem Zeitpunkt, an dem das initiale Experiment abgeschlossen wurde.

## Wissenswertes {#things-to-know}

### Einmaliger Eintritt {#one-time-entry}

Bei der Verwendung von Winning Paths in einem Canvas, in dem Nutzer:innen nur einmal eintreten dürfen, wird automatisch eine Verzögerungsgruppe einbezogen. Während der Dauer des Experiments wird ein Prozentsatz der Nutzer:innen in der Verzögerungsgruppe gehalten, während die übrigen Nutzer:innen Ihre Experimentpfade betreten.

![Experiment-Schritt mit einer Verzögerungsgruppe für Winning Path]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Wenn der Test abgeschlossen ist und ein Winning Path ermittelt wurde, werden die der Verzögerungsgruppe zugewiesenen Nutzer:innen zum gewählten Pfad geleitet und setzen ihren Weg durch den Canvas fort.

![Experiment-Schritt mit einer Verzögerungsgruppe, die über den Winning Path geleitet wird]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Zustellung zur Ortszeit {#local-time-delivery}

Wir empfehlen nicht, die Zustellung zur Ortszeit in Canvases mit Winning Paths zu verwenden. Der Grund dafür ist, dass Experiment-Fenster beginnen, wenn die erste Person den Schritt durchläuft. Nutzer:innen in sehr frühen Zeitzonen können den Schritt betreten und den Start des Experiment-Fensters viel früher als erwartet auslösen, was dazu führen kann, dass das Experiment endet, bevor der Großteil Ihrer Nutzer:innen in typischeren Zeitzonen genügend Zeit hatte, den Canvas zu betreten oder zu konvertieren – oder beides.

Wenn Sie stattdessen die Zustellung zur Ortszeit verwenden möchten, nutzen Sie ein Experiment-Fenster von 24–48 oder mehr Stunden. Auf diese Weise betreten Nutzer:innen in frühen Zeitzonen den Canvas und lösen den Start des Experiments aus, aber es verbleibt noch ausreichend Zeit im Experiment-Fenster. Nutzer:innen in späteren Zeitzonen haben dann immer noch genügend Zeit, den Canvas und den Experiment-Schritt mit Winning Paths zu betreten und möglicherweise zu konvertieren, bevor das Experiment-Fenster abläuft.

### Varianten basierend auf Klicks {#variants-based-on-clicks}

Wenn Sie eine Winning-Path-Variante basierend auf Klicks einrichten, beachten Sie, dass sich die Definitionen für Öffnungen und Klicks je nach Kanal unterscheiden. Spezifische Metriken und Definitionen nach Kanal finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics) und im [Glossar der E-Mail-Berichtsmetriken]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary).