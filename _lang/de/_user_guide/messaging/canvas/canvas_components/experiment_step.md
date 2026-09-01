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

Um Experimentpfade zu verwenden, muss Ihr Canvas Konversions-Events enthalten. Obwohl Sie nach dem Start eines Canvas keine Konversions-Events mehr hinzufügen können, können Sie den gestarteten Canvas klonen und Konversions-Events hinzufügen, um Experimentpfade zu ergänzen.

## Anwendungsfälle {#use-cases}

Experimentpfade eignen sich am besten zum Testen von Zustellung, Kadenz, Nachrichtentext und Kanalkombinationen.

- **Zustellung:** Vergleichen Sie die Ergebnisse von Nachrichten, die mit unterschiedlichen zeitlichen [Verzögerungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) gesendet werden, basierend auf Nutzeraktionen ([Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)) und unter Verwendung von [intelligentem Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1).<br><br>
- **Kadenz:** Testen Sie mehrere Messaging-Abläufe über einen bestimmten Zeitraum. Sie könnten beispielsweise zwei verschiedene Onboarding-Kadenzen testen:
    - Kadenz 1: 2 Nachrichten in den ersten 2 Wochen der Nutzer:innen senden
    - Kadenz 2: 3 Nachrichten in den ersten 2 Wochen der Nutzer:innen senden

    Beim Targeting passiver Nutzer:innen können Sie die Wirksamkeit von zwei Rückgewinnungs-Nachrichten pro Woche im Vergleich zu nur einer testen.
- **Nachrichtentext:** Ähnlich wie bei einem standardmäßigen [A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing) können Sie verschiedene Nachrichtentexte testen, um herauszufinden, welche Formulierung zu einer höheren Konversionsrate führt.<br><br>
- **Kanalkombinationen:** Testen Sie die Wirksamkeit verschiedener Nachrichtenkanal-Kombinationen. Sie können beispielsweise die Wirkung einer reinen E-Mail mit der einer E-Mail in Kombination mit einer Push-Nachricht vergleichen.

## Einen Experimentpfad erstellen {#creating-an-experiment-path}

Um eine Experimentpfade-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag-and-drop aus der Seitenleiste, oder klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Ende eines Schritts und wählen Sie **Experimentpfade**.

In der Standardkonfiguration dieser Komponente gibt es zwei Standardpfade, **Pfad 1** und **Pfad 2**, wobei 50 % der Zielgruppe jeweils einem Pfad zugewiesen werden. Klicken Sie auf die Komponente, um das Panel **Experimenteinstellungen** zu öffnen. Dort sehen Sie die Konfigurationsoptionen für die Komponente.

### Schritt 1: Anzahl der Pfade und Zielgruppenverteilung festlegen {#step-1-choose-the-number-of-paths-and-audience-distribution}

Sie können bis zu vier Pfade hinzufügen, indem Sie auf **Pfad hinzufügen** klicken, sowie eine optionale Kontrollgruppe durch Aktivieren von **Kontrollgruppe hinzufügen**. Über die Prozentfelder für jeden Pfad können Sie festlegen, welcher Prozentsatz der Zielgruppe jedem Pfad und der Kontrollgruppe zugewiesen werden soll. Die angegebenen Prozentsätze müssen in der Summe 100 % ergeben, um fortfahren zu können. Wenn Sie alle verfügbaren Pfade (und die Kontrollgruppe) schnell auf denselben Prozentsatz setzen möchten, klicken Sie auf **Pfade gleichmäßig verteilen**.

Sie können außerdem festlegen, ob Nutzer:innen in der Kontrollgruppe im Canvas weitergehen oder nach dem Konversions-Tracking-Fenster den Canvas verlassen sollen – über die Einstellung **Verhalten der Kontrollgruppe**. Optional können Sie eine Beschreibung hinzufügen, um anderen zu erklären, was dieser Experimentpfad testen soll, oder zusätzliche hilfreiche Informationen festzuhalten.

![Experimenteinstellungen, in denen Sie Pfade hinzufügen und den Prozentsatz der Nutzer:innen in jedem Pfad festlegen können.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Wenn die erneute Canvas-Berechtigung aktiviert ist, durchlaufen Nutzer:innen, die den Canvas betreten und einen zufällig ausgewählten Pfad nehmen, bei erneutem Eintritt denselben Pfad. Dies gewährleistet die Validität des Experiments und der zugehörigen Analytics. Um die Pfadzuweisung bei jedem erneuten Eintritt zu randomisieren, wählen Sie **Randomisierte Pfade in Experimentpfaden**. Diese Option ist bei Verwendung von Winning Path nicht verfügbar.
{% endalert %}

### Schritt 2: Winning Path aktivieren (optional) {#step-2}

Um Ihr Experiment zu optimieren, aktivieren Sie [Winning Path]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path). Winning Path testet Ihre Pfade zunächst mit einem Teil der Zielgruppe. Nach Abschluss des Experiments leitet Braze die verbleibenden und nachfolgenden Nutzer:innen über den leistungsstärksten Pfad.

{% alert note %}
Personalisierte Pfade sind für neue Experimentpfad-Schritte nicht verfügbar. Bestehende Schritte, die personalisierte Pfade verwenden, laufen weiterhin.
{% endalert %}

### Schritt 3: Pfade erstellen {#step-3-create-paths}

Zuletzt müssen Sie Ihre nachgelagerten Pfade erstellen. Wählen Sie **Fertig** und kehren Sie zum Canvas-Builder zurück. Klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button unter jedem Pfad, um mit den üblichen Canvas-Tools Journeys nach Ihren Vorstellungen zu erstellen, und starten Sie den Canvas, wenn Sie bereit sind.

![Hinzufügen von Schritten zu jedem Pfad, der von einer Experimentpfade-Komponente abzweigt.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Beachten Sie, dass Pfade und ihre nachgelagerten Schritte nach der Erstellung nicht mehr aus einem Canvas entfernt werden können. Nach dem Start können Sie jedoch die Zielgruppenverteilung über die Pfade nach Bedarf anpassen. Wenn Sie beispielsweise einen Tag nach dem Start eines Canvas anhand der Analytics feststellen, dass ein Pfad den anderen überlegen ist, können Sie diesen Pfad auf 100 % und die anderen auf 0 % setzen. Oder Sie können je nach Bedarf weiterhin Nutzer:innen über mehrere Pfade senden.

{% alert important %}
Um eine Verfälschung des Experiments zu vermeiden, beendet das Aktualisieren eines aktiven Canvas mit einem laufenden Winning-Path-Experiment das Experiment. Dies gilt auch dann, wenn Sie den Experimentpfad-Schritt nicht aktualisieren. Um das Experiment neu zu starten, trennen Sie den bestehenden Experimentpfad und starten Sie einen neuen, oder duplizieren Sie den Canvas und starten Sie das Duplikat. Sie können Winning Path nicht für einen bereits aktiven Canvas mit einem Experimentpfad-Schritt aktivieren.<br><br>Weitere Informationen finden Sie unter [Canvases nach dem Start bearbeiten]({{site.baseurl}}/post-launch_edits).
{% endalert %}

## Performance-Tracking {#tracking-performance}

Wählen Sie auf der Seite **Canvas Analytics** den Experimentpfad aus, um eine [detaillierte Tabelle]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch) zu öffnen, die mit dem Tab **Analyze Variants** identisch ist und detaillierte Performance- und Konversionsstatistiken über alle Pfade hinweg vergleicht. Sie können die Tabelle auch als CSV exportieren und prozentuale Veränderungen für relevante Metriken relativ zum ausgewählten Pfad oder zur Kontrollgruppe vergleichen.

Jeder Schritt in jedem Pfad zeigt Statistiken in der [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)-Ansicht an, genau wie bei jedem anderen Canvas-Schritt. Beachten Sie jedoch, dass einzelne Schrittanalysen und Experimentpfad-Analysen Konversionen unterschiedlich messen:

- **Experimentpfad-Analysen** erfassen Konversionen ab dem Zeitpunkt, an dem Nutzer:innen den Experimentpfad-Schritt betreten. Dies ist die empfohlene Ansicht zum Vergleich der Performance über verschiedene Pfade hinweg, da alle Pfade denselben Ausgangspunkt teilen.
- **Einzelne Schrittanalysen** (wie z. B. Nachrichten-Schritt-Analysen) erfassen Konversionen ab dem Zeitpunkt, an dem Nutzer:innen diesen bestimmten Schritt erhalten (z. B. wenn die Nachricht gesendet wird).

Da diese Konversionsfenster unterschiedliche Ausgangspunkte haben, können sie unterschiedliche Konversionsraten für denselben Pfad anzeigen – insbesondere wenn es Verzögerungen zwischen dem Experimentschritt und einer nachgelagerten Nachricht gibt. Für den zuverlässigsten Vergleich über verschiedene Pfade hinweg verwenden Sie die Experimentpfad-Analysen.

### Winning-Path-Performance {#winning-path-performance}

Verwenden Sie Winning Path, um die Performance über die Zeit zu verfolgen und nachfolgende Nutzer:innen automatisch über den leistungsstärksten Pfad zu senden. Weitere Informationen finden Sie unter [Winning-Path-Analysen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics).

Die Gewinn-Metrik und die in Experimentpfaden angezeigten Analysen können voneinander abweichen:

- Das Konversions-Event, das Sie für **Winning Path** konfigurieren, bestimmt, wie Braze Pfade vergleicht und während des Experimentfensters einen Gewinner auswählt.
- Experimentpfad-Analysen folgen weiterhin dem gleichen [Konversions-Event]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)-Framework des Canvas wie der Rest des Canvas, einschließlich Ihres [primären Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#primary-conversion-event). Dadurch stimmen die im Dashboard hervorgehobenen Metriken möglicherweise nicht mit der Gewinn-Metrik überein.
- Für Push unterscheiden sich *Direct Opens* und *Total Opens*. Weitere Informationen finden Sie unter [Beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

### Zusätzliche Einstellungen {#additional-settings}

Experimentpfade erfassen Nutzer:innen, die jeden Schritt betreten und konvertieren, während sie sich auf dem zugewiesenen Pfad befinden. Dabei werden alle in der Canvas-Einrichtung angegebenen Konversions-Events verfolgt. Geben Sie im Tab **Additional Settings** an, wie viele Tage (zwischen 1 und 30) dieses Experiment Konversionen verfolgen soll. Das hier angegebene Zeitfenster bestimmt, wie lange Konversions-Events (die in der Canvas-Einrichtung ausgewählt wurden) für das Experiment erfasst werden. Die in der Canvas-Einrichtung angegebenen Konversionsfenster pro Event gelten nicht für das Tracking dieses Schritts und werden durch dieses Konversionsfenster ersetzt.

Das Konversionsfenster beginnt, wenn Nutzer:innen den Experimentpfad-Schritt betreten, nicht wenn eine nachgelagerte Nachricht gesendet wird. Wenn ein Pfad Verzögerungen enthält – wie z. B. einen Verzögerungsschritt oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) – verbrauchen diese Verzögerungen einen Teil des Konversionsfensters.

{% alert important %}
Wenn Sie intelligentes Timing in einem Nachrichten-Schritt innerhalb eines Experimentpfads verwenden, verkürzt die Zeit zwischen dem Experimenteintritt und dem tatsächlichen Nachrichtenversand das effektive Konversionsfenster für diesen Pfad. Wenn Ihr Experiment beispielsweise ein 5-Tage-Konversionsfenster hat und intelligentes Timing die Nachricht um 2 Tage verzögert, haben Nutzer:innen auf diesem Pfad nach Erhalt der Nachricht nur noch 3 Tage, um innerhalb des Experimentfensters zu konvertieren – auch wenn die eigenen Analysen des Nachrichten-Schritts Konversionen ab dem Zeitpunkt des Nachrichtenversands erfassen.<br><br>Für aussagekräftigere Experimentanalysen platzieren Sie Verzögerungen (wie z. B. Verzögerungsschritte) **vor** dem Experimentpfad-Schritt statt innerhalb eines Experimentpfads. Auf diese Weise starten alle Pfade vom selben Punkt aus und Verzögerungen verbrauchen keinen Teil des Konversionsfensters.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum unterscheiden sich die Versendungen zwischen den Pfaden, obwohl die Aufteilung im Experiment gleichmäßig aussieht? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Die nachgelagerten *Versendungen* hängen von den Schritten, Verzögerungen, Kanal-Berechtigungen und Inhalten der einzelnen Pfade ab – nicht nur vom prozentualen Split am Experimentpfad. Unterschiedliche Verzögerungen, intelligentes Timing oder der Abo-Status können beispielsweise dazu führen, dass unterschiedlich viele Nutzer:innen eine Nachricht erhalten, selbst wenn die Pfadzuweisung ausgeglichen war. Um Pfadergebnisse zu vergleichen, verwenden Sie die [Experimentpfad-Analytics](#tracking-performance), die Konversionen ab einem gemeinsamen Einstiegspunkt messen.

### Wie lange dauert das Konversionsfenster des Experiments? {#how-long-does-the-experiment-conversion-window-last}

Das Konversionsfenster unter **Additional Settings** (1–30 Tage) beginnt, wenn Nutzer:innen den Experimentpfade-Schritt betreten. Zeit, die in nachgelagerten Verzögerungsschritten oder beim Warten auf intelligentes Timing verbracht wird, wird auf dieses Fenster angerechnet. Weitere Details finden Sie unter [Performance tracken](#tracking-performance).