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

## Gewinnerpfad verwenden {#using-winning-path}

### Schritt 1: Experimentpfade-Schritt hinzufügen {#step-1-add-an-experiment-path-step}

Fügen Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt zu Ihrem Canvas hinzu und aktivieren Sie dann **Winning Path**.

![Einstellungen im Experimentpfade-Schritt mit dem Titel „Distribute Subsequent Users to Winning Path“. Der Abschnitt enthält einen Schalter für Winning Path sowie Optionen zur Konfiguration des Konversions-Events und des Experimentfensters.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Schritt 2: Winning-Path-Einstellungen konfigurieren {#step-2-configure-winning-path-settings}

Geben Sie das Konversions-Event an, das den Gewinner bestimmen soll. Wenn keine Konversions-Events verfügbar sind, kehren Sie zum ersten Schritt der Canvas-Einrichtung zurück und [weisen Sie Konversions-Events zu]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Wenn Sie Öffnungen oder Klicks als Konversions-Event wählen, stellen Sie sicher, dass der erste Schritt im Pfad ein [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) ist. Braze zählt nur das Engagement des ersten Nachrichtenschritts in jedem jeweiligen Pfad. Wenn der Pfad mit einem anderen Schritt beginnt (z. B. einem Verzögerungs- oder Zielgruppenpfad-Schritt) und die Nachricht erst später folgt, wird diese Nachricht bei der Performance-Bewertung nicht berücksichtigt.

Legen Sie als Nächstes das **Experimentfenster** fest. Das **Experimentfenster** gibt an, wie lange das Experiment läuft, bevor der Gewinnerpfad bestimmt wird und alle nachfolgenden Nutzer:innen diesen Pfad durchlaufen. Das Fenster beginnt, wenn die erste Person den Schritt betritt.

![Winning-Path-Einstellungen mit dem ausgewählten Konversions-Event „Clicks“ für ein 12-stündiges Experimentfenster.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Schritt 3: Fallback festlegen {#statistical-significance}

Standardmäßig werden alle zukünftigen Nutzer:innen den leistungsstärksten Pfad entlanggesendet, wenn die Testergebnisse nicht ausreichen, um einen statistisch signifikanten Gewinner zu ermitteln. Alternativ können Sie **Continue sending all future users the mix of paths** auswählen. Diese Option sendet zukünftige Nutzer:innen gemäß den in der Experimentpfad-Verteilung angegebenen Prozentsätzen durch die Mischung der Pfade.

Bei einem Gleichstand wählt Braze den Pfad aus, der zuerst erscheint.

![„Continue sending all future users the mix of paths“ als ausgewählte Option für den Fall, dass das Testergebnis nicht statistisch signifikant ist.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Eine Verzögerungsgruppe erscheint in Ihrer Pfadverteilung nur, wenn Ihr Canvas für einmaligen Entry eingerichtet ist und Ihr Experimentschritt drei oder weniger Pfade hat. Wiederkehrende und getriggerte Canvases haben keine Verzögerungsgruppe, wenn Winning Path aktiviert ist.
{% endalert %}

### Schritt 4: Pfade hinzufügen und Canvas starten {#step-4-add-your-paths-and-launch-the-canvas}

Eine einzelne Experimentpfade-Komponente kann bis zu vier Pfade enthalten. Wenn Ihr Canvas jedoch für [einmaligen Entry](#one-time-entry) eingerichtet ist, muss ein Pfad für die Verzögerungsgruppe reserviert werden, die Braze automatisch hinzufügt, wenn Winning Path aktiviert ist. Das bedeutet, dass Sie bei Canvases mit einmaligem Entry bis zu drei Pfade zu Ihrem Experiment hinzufügen können.

Schließen Sie die Einrichtung Ihres Canvas nach Bedarf ab und starten Sie ihn. Sobald die erste Person das Experiment betreten hat, können Sie das Canvas überprüfen, um eingehende Analytics zu sehen und die [Performance Ihres Experiments zu verfolgen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Nachdem ein Gewinnerpfad abgeschlossen ist, durchlaufen alle nachfolgenden Nutzer:innen, die das Canvas betreten, den Gewinnerpfad – einschließlich Nutzer:innen, die erneut eingetreten sind und zuvor in der Kontrollgruppe des Experimentpfade-Schritts waren.

## Analytics {#analytics}

Wenn Winning Path aktiviert ist, wird Ihre Analytics-Ansicht in zwei Tabs unterteilt: **Initiales Experiment** und **Winning Path**.

- **Initiales Experiment:** Zeigt die Metriken für jeden Pfad während des Experiment-Fensters, welcher Pfad als Gewinner ausgewählt wurde, und die Canvas-Conversion-Metriken. Das Konversions-Event, das zur Bestimmung des Gewinners verwendet wird und in den Winning-Path-Einstellungen konfiguriert ist, muss nicht mit der in den Canvas-Analytics hervorgehobenen Conversion-Metrik übereinstimmen. Weitere Informationen darüber, wie Experiment-Pfad-Analytics mit Canvas-Konversions-Events und der Gewinner-Metrik zusammenhängen, finden Sie unter [Experimentpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#winning-path-and-personalized-paths-performance).
- **Winning Path:** Zeigt nur die Metriken für den Winning Path ab dem Zeitpunkt, an dem das initiale Experiment abgeschlossen wurde.

## Wissenswertes {#things-to-know}

### Einmaliger Eintritt {#one-time-entry}

Wenn Sie Gewinnerpfade in einem Canvas verwenden, bei dem Nutzer:innen nur einmal eintreten dürfen, wird automatisch eine Verzögerungsgruppe eingeschlossen. Während der Dauer des Experiments wird ein Prozentsatz der Nutzer:innen in der Verzögerungsgruppe gehalten, während die übrigen Nutzer:innen Ihre Experimentpfade betreten.

![Experimentschritt mit einer Verzögerungsgruppe für den Gewinnerpfad]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Wenn der Test abgeschlossen ist und ein Gewinnerpfad ermittelt wurde, werden die der Verzögerungsgruppe zugewiesenen Nutzer:innen zum gewählten Pfad weitergeleitet und setzen ihren Weg durch den Canvas fort.

![Experimentschritt mit einer Verzögerungsgruppe, die den Gewinnerpfad durchläuft]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Zustellung zur Ortszeit {#local-time-delivery}

Wir empfehlen nicht, die Zustellung zur Ortszeit in Canvases mit Gewinnerpfaden zu verwenden. Der Grund dafür ist, dass Experimentfenster beginnen, wenn die ersten Nutzer:innen den Schritt durchlaufen. Nutzer:innen in sehr frühen Zeitzonen können den Schritt betreten und den Start des Experimentfensters viel früher als erwartet auslösen. Dies kann dazu führen, dass das Experiment endet, bevor der Großteil Ihrer Nutzer:innen in typischeren Zeitzonen genügend Zeit hatte, den Canvas zu betreten, zu konvertieren, oder beides.

Wenn Sie alternativ die Zustellung zur Ortszeit nutzen möchten, verwenden Sie ein Experimentfenster von 24–48 oder mehr Stunden. Auf diese Weise betreten Nutzer:innen in frühen Zeitzonen den Canvas und lösen den Start des Experiments aus, aber es verbleibt noch ausreichend Zeit im Experimentfenster. Nutzer:innen in späteren Zeitzonen haben dann immer noch genügend Zeit, den Canvas und den Experimentschritt mit Gewinnerpfaden zu betreten und möglicherweise zu konvertieren, bevor das Experimentfenster abläuft.

### Varianten basierend auf Klicks {#variants-based-on-clicks}

Wenn Sie eine Gewinnerpfad-Variante auf Basis von Klicks einrichten, beachten Sie, dass die Definitionen für Öffnungen und Klicks je nach Kanal unterschiedlich sind. Spezifische Metriken und Definitionen nach Kanal finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) und im [Glossar der E-Mail-Berichtsmetriken]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary).