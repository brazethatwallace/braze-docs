---
nav_title: Experimentpfade
article_title: Experimentpfade
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Dieser Artikel behandelt Experimentpfade – eine Komponente, mit der Sie mehrere Canvas-Pfade gegeneinander und gegen eine Kontrollgruppe an jedem Punkt der User Journey testen können."
tool: Canvas
---

# Experimentpfade {#experiment-paths}

> Mit Experimentpfaden können Sie mehrere Canvas-Pfade gegeneinander und gegen eine Kontrollgruppe an jedem Punkt der User Journey testen. Mit dieser Komponente können Sie die Performance der Pfade verfolgen, um fundierte Entscheidungen über Ihre Canvas-Journey zu treffen.

Wenn Sie einen Experimentpfad-Schritt in Ihre User Journey einfügen, werden Nutzer:innen zufällig verschiedenen Pfaden (oder einer optionalen Kontrollgruppe) zugewiesen, die Sie erstellen. Teile der Zielgruppe werden den verschiedenen Pfaden gemäß den von Ihnen gewählten Prozentsätzen zugewiesen, sodass Sie verschiedene Nachrichten oder Pfade gegeneinander testen und ermitteln können, welcher am effektivsten ist.

![Ein Experimentpfad-Schritt, der sich in Pfad 1, Pfad 2 und Kontrollgruppe aufteilt.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Voraussetzungen {#prerequisites}

Um Experimentpfade zu verwenden, muss Ihr Canvas Konversions-Events enthalten. Zwar können Sie nach dem Start eines Canvas keine Konversions-Events mehr hinzufügen, aber Sie können den gestarteten Canvas klonen und Konversions-Events hinzufügen, um Experimentpfade zu nutzen.

## Anwendungsfälle {#use-cases}

Experimentpfade eignen sich am besten zum Testen von Zustellung, Kadenz, Nachrichtentext und Kanalkombinationen.

- **Zustellung:** Vergleichen Sie die Ergebnisse zwischen Nachrichten, die mit unterschiedlichen zeitlichen [Verzögerungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) gesendet werden, basierend auf Nutzeraktionen ([Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)) und unter Verwendung von [intelligentem Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1).<br><br>
- **Kadenz:** Testen Sie mehrere Messaging-Abläufe über einen bestimmten Zeitraum. Sie könnten beispielsweise zwei verschiedene Onboarding-Kadenzen testen:
    - Kadenz 1: 2 Nachrichten in den ersten 2 Wochen senden
    - Kadenz 2: 3 Nachrichten in den ersten 2 Wochen senden

    Beim Targeting passiver Nutzer:innen können Sie die Wirksamkeit von zwei Rückgewinnungs-Nachrichten pro Woche im Vergleich zu nur einer testen.
- **Nachrichtentext:** Ähnlich wie bei einem Standard-[A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing) können Sie verschiedene Nachrichtentexte testen, um herauszufinden, welche Formulierung zu einer höheren Konversionsrate führt.<br><br>
- **Kanalkombinationen:** Testen Sie die Wirksamkeit verschiedener Nachrichtenkanal-Kombinationen. Sie können beispielsweise die Wirkung einer reinen E-Mail mit der einer E-Mail in Kombination mit einem Push vergleichen.

## Einen Experimentpfad erstellen {#creating-an-experiment-path}

Um eine Experimentpfad-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Experiment Paths**.

In der Standardkonfiguration dieser Komponente gibt es zwei Standard-Pfade, **Path 1** und **Path 2**, wobei 50 % der Zielgruppe jeweils einen Pfad durchlaufen. Klicken Sie auf die Komponente, um das Panel **Experiment Settings** zu öffnen, und Sie sehen die Konfigurationsoptionen für die Komponente.

### 1. Schritt: Anzahl der Pfade und Zielgruppenverteilung wählen {#step-1-choose-the-number-of-paths-and-audience-distribution}

Sie können bis zu vier Pfade hinzufügen, indem Sie auf **Add Path** klicken, und eine optionale Kontrollgruppe, indem Sie **Add a Control Group** aktivieren. Über die Prozentfelder für jeden Pfad können Sie festlegen, welcher Prozentsatz der Zielgruppe jedem Pfad und der Kontrollgruppe zugewiesen werden soll. Die angegebenen Prozentsätze müssen zusammen 100 % ergeben, um fortfahren zu können. Wenn Sie alle verfügbaren Pfade (und die Kontrollgruppe) schnell auf den gleichen Prozentsatz setzen möchten, klicken Sie auf **Distribute Paths Evenly**.

Sie können auch festlegen, ob Nutzer:innen in der Kontrollgruppe den Canvas weiter durchlaufen oder nach dem Conversion-Tracking-Fenster aussteigen sollen – über das **Control Group Behavior**. Optional können Sie eine Beschreibung hinzufügen, um anderen zu erklären, was dieser Experimentpfad testen soll, oder zusätzliche Informationen festhalten, die hilfreich sein könnten.

![Experiment-Einstellungen, in denen Sie Pfade hinzufügen und den Prozentsatz der Nutzer:innen in jedem Pfad verteilen können.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Wenn die erneute Canvas-Berechtigung aktiviert ist, durchlaufen Nutzer:innen, die den Canvas betreten und einen zufällig gewählten Pfad nehmen, denselben Pfad erneut, wenn sie erneut berechtigt werden und den Canvas wieder betreten. Dies gewährleistet die Validität des Experiments und der zugehörigen Analytics. Wenn der Schritt die Pfadzuweisung immer zufällig vornehmen soll, wählen Sie **Randomized Paths in Experiment Paths**. Diese Option ist nicht verfügbar, wenn Winning Path oder personalisierte Pfade verwendet werden.
{% endalert %}

### 2. Schritt: Winning Path oder personalisierte Pfade aktivieren (optional) {#step-2}

Sie können Ihr Experiment optimieren, indem Sie [Winning Path]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) oder [personalisierte Pfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths) aktivieren. Beide Optionen testen Ihre Pfade zunächst mit einem Teil Ihrer Zielgruppe. Nach Abschluss des Experiments werden die verbleibenden und nachfolgenden Nutzer:innen entweder über den insgesamt leistungsstärksten Pfad (Winning Path) oder den für jede:n Nutzer:in leistungsstärksten Pfad (personalisierte Pfade) geleitet.

### 3. Schritt: Pfade erstellen {#step-3-create-paths}

Zuletzt müssen Sie Ihre nachgelagerten Pfade aufbauen. Wählen Sie **Done** und kehren Sie zum Canvas-Builder zurück. Klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button unter jedem Pfad, um Journeys mit den üblichen Canvas-Tools nach Bedarf zu erstellen, und starten Sie den Canvas, wenn Sie bereit sind.

![Schritte zu jedem Pfad hinzufügen, der von einer Experimentpfad-Komponente abzweigt.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Beachten Sie, dass Pfade und ihre nachgelagerten Schritte nach der Erstellung nicht mehr aus einem Canvas entfernt werden können. Nach dem Start können Sie jedoch die Zielgruppenverteilung über die Pfade nach Bedarf anpassen. Wenn Sie beispielsweise einen Tag nach dem Start eines Canvas anhand der Analytics feststellen, dass ein Pfad den anderen überlegen ist, können Sie diesen Pfad auf 100 % und die anderen auf 0 % setzen. Oder Sie können je nach Bedarf weiterhin Nutzer:innen über mehrere Pfade leiten.

{% alert important %}
Um eine Kontamination des Experiments zu vermeiden: Wenn Ihr Canvas ein aktives oder laufendes Winning-Path- oder Personalized-Path-Experiment hat und Sie den aktiven Canvas aktualisieren – unabhängig davon, ob Sie den Experimentpfad-Schritt selbst aktualisieren – wird das laufende Experiment beendet und der Experiment-Schritt ermittelt keinen Winning Path und keine personalisierten Pfade. Um das Experiment neu zu starten, können Sie den bestehenden Experimentpfad trennen und einen neuen starten oder den Canvas duplizieren und einen neuen Canvas starten. Andernfalls durchlaufen Nutzer:innen den Experimentpfad, als wäre keine Optimierungsmethode ausgewählt worden. Sie können personalisierte Pfade oder Winning Path auch nicht für einen bereits aktiven Canvas mit einem Experimentpfad-Schritt aktivieren.<br><br>Weitere Informationen finden Sie unter [Canvases nach dem Start bearbeiten]({{site.baseurl}}/post-launch_edits).
{% endalert %}

## Performance verfolgen {#tracking-performance}

Wählen Sie auf der Seite **Canvas Analytics** den Experimentpfad aus, um eine [detaillierte Tabelle]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch) zu öffnen, die dem Tab **Analyze Variants** entspricht und detaillierte Performance- und Conversion-Statistiken über die Pfade hinweg vergleicht. Sie können die Tabelle auch als CSV exportieren und prozentuale Veränderungen für relevante Metriken im Vergleich zum ausgewählten Pfad oder der Kontrollgruppe vergleichen.

Jeder Schritt in jedem Pfad zeigt Statistiken in der [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)-Ansicht an, genau wie jeder andere Canvas-Schritt. Beachten Sie jedoch, dass die Analytics einzelner Schritte und die Experimentpfad-Analytics Conversions unterschiedlich messen:

- **Experimentpfad-Analytics** verfolgen Conversions ab dem Zeitpunkt, an dem Nutzer:innen den Experimentpfad-Schritt betreten. Dies ist die empfohlene Ansicht für den Vergleich der Performance über Pfade hinweg, da alle Pfade denselben Startpunkt teilen.
- **Analytics einzelner Schritte** (z. B. Nachrichten-Schritt-Analytics) verfolgen Conversions ab dem Zeitpunkt, an dem Nutzer:innen den jeweiligen Schritt erhalten (z. B. wenn die Nachricht gesendet wird).

Da diese Conversion-Fenster unterschiedliche Startpunkte haben, können sie unterschiedliche Konversionsraten für denselben Pfad anzeigen – insbesondere wenn es Verzögerungen zwischen dem Experiment-Schritt und einer nachgelagerten Nachricht gibt. Für den zuverlässigsten Vergleich über Pfade hinweg verwenden Sie die Experimentpfad-Analytics.

### Winning Path und personalisierte Pfade – Performance {#winning-path-and-personalized-paths-performance}

Nutzen Sie Winning Path, um die Performance über einen Zeitraum zu verfolgen und nachfolgende Nutzer:innen dann automatisch über den leistungsstärksten Pfad zu leiten. Weitere Informationen zu den Analytics, wenn **Winning Path** oder **personalisierte Pfade** für Ihr Experiment aktiviert sind, finden Sie unter:

- [Winning Path]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics)
- [Personalisierte Pfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths#analytics)

Die Gewinner-Metrik und die in den Experimentpfaden angezeigten Analytics können sich unterscheiden:

- Das Konversions-Event, das Sie für **Winning Path** oder **personalisierte Pfade** konfigurieren, bestimmt, wie Braze Pfade vergleicht und während des Experiment-Fensters einen Gewinner auswählt.
- Die Experimentpfad-Analytics folgen weiterhin dem gleichen Canvas-[Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events)-Framework wie der Rest des Canvas, einschließlich Ihres [primären Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events#primary-conversion-event). Daher stimmen die im Dashboard hervorgehobenen Metriken möglicherweise nicht mit der Gewinner-Metrik überein.
- Bei Push unterscheiden sich *Direkte Öffnungen* und *Gesamtöffnungen*. Weitere Informationen finden Sie unter [Beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

### Zusätzliche Einstellungen {#additional-settings}

Experimentpfade erfassen Nutzer:innen, die jeden Schritt betreten und während des zugewiesenen Pfads konvertieren. Dies verfolgt alle im Canvas-Setup festgelegten Konversions-Events. Geben Sie im Tab **Additional Settings** ein, wie viele Tage (zwischen 1 und 30) dieses Experiment Conversions verfolgen soll. Das hier angegebene Zeitfenster bestimmt, wie lange Konversions-Events (die im Canvas-Setup ausgewählt wurden) für das Experiment verfolgt werden. Die im Canvas-Setup festgelegten Conversion-Fenster pro Event gelten nicht für das Tracking dieses Schritts und werden durch dieses Conversion-Fenster ersetzt.

Das Conversion-Fenster beginnt, wenn Nutzer:innen den Experimentpfad-Schritt betreten, nicht wenn eine nachgelagerte Nachricht gesendet wird. Wenn ein Pfad Verzögerungen enthält – wie einen Verzögerungsschritt oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) – verbrauchen diese Verzögerungen einen Teil des Conversion-Fensters.

{% alert important %}
Wenn Sie intelligentes Timing bei einem Nachrichten-Schritt innerhalb eines Experimentpfads verwenden, reduziert die Zeit zwischen dem Experiment-Eintritt und dem tatsächlichen Nachrichtenversand das effektive Conversion-Fenster für diesen Pfad. Wenn Ihr Experiment beispielsweise ein 5-Tage-Conversion-Fenster hat und intelligentes Timing die Nachricht um 2 Tage verzögert, haben Nutzer:innen auf diesem Pfad nur 3 Tage nach Erhalt der Nachricht, um innerhalb des Experiment-Fensters zu konvertieren – obwohl die Analytics des Nachrichten-Schritts selbst Conversions ab dem Zeitpunkt des Nachrichtenversands verfolgen.<br><br>Für sauberere Experiment-Analytics platzieren Sie Verzögerungen (wie Verzögerungsschritte) **vor** dem Experimentpfad-Schritt und nicht innerhalb eines Experimentpfads. So starten alle Pfade vom gleichen Punkt aus und Verzögerungen verbrauchen keinen Teil des Conversion-Fensters.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum unterscheiden sich die Sendungen zwischen Pfaden, obwohl die Experiment-Aufteilung gleichmäßig aussieht? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Nachgelagerte *Sendungen* hängen von den Schritten, Verzögerungen, der Kanalberechtigung und dem Inhalt jedes Pfads ab – nicht nur von der prozentualen Aufteilung am Experimentpfad. Beispielsweise können unterschiedliche Verzögerungen, intelligente Sendezeiten oder der Abo-Status beeinflussen, wie viele Nutzer:innen eine Nachricht erhalten, selbst wenn die Pfadzuweisung ausgewogen war. Um die Ergebnisse der Pfade zu vergleichen, verwenden Sie die [Experimentpfad-Analytics](#tracking-performance), die Conversions ab einem gemeinsamen Einstiegspunkt messen.

### Wie lange dauert das Experiment-Conversion-Fenster? {#how-long-does-the-experiment-conversion-window-last}

Das Conversion-Fenster unter **Additional Settings** (1–30 Tage) beginnt, wenn Nutzer:innen den Experimentpfad-Schritt betreten. Die Zeit, die in nachgelagerten Verzögerungsschritten oder beim Warten auf intelligentes Timing verbracht wird, wird auf dieses Fenster angerechnet. Weitere Details finden Sie unter [Performance verfolgen](#tracking-performance).