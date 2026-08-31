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

Um Experimentpfade zu verwenden, muss Ihr Canvas Konversions-Events enthalten. Sie können zwar keine Konversions-Events hinzufügen, nachdem ein Canvas gestartet wurde, aber Sie können das gestartete Canvas klonen und Konversions-Events hinzufügen, um Experimentpfade zu nutzen.

## Anwendungsfälle {#use-cases}

Experimentpfade eignen sich am besten zum Testen von Zustellung, Frequenz, Nachrichtentext und Kanalkombinationen.

- **Zustellung:** Vergleichen Sie die Ergebnisse von Nachrichten, die mit unterschiedlichen zeitlichen [Verzögerungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) gesendet werden, basierend auf Nutzeraktionen ([Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)), und unter Verwendung von [intelligentem Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#step-1-add-intelligent-timing-1).<br><br>
- **Frequenz:** Testen Sie mehrere Messaging-Abläufe über einen bestimmten Zeitraum. Sie könnten beispielsweise zwei verschiedene Onboarding-Frequenzen testen:
    - Frequenz 1: 2 Nachrichten in den ersten 2 Wochen senden
    - Frequenz 2: 3 Nachrichten in den ersten 2 Wochen senden

    Wenn Sie passive Nutzer:innen ansprechen, können Sie die Wirksamkeit von zwei Rückgewinnungs-Nachrichten in einer Woche im Vergleich zu nur einer testen.
- **Nachrichtentext:** Ähnlich wie bei einem standardmäßigen [A/B-Test]({{site.baseurl}}/user_guide/messaging/ab_testing) können Sie verschiedene Nachrichtentexte testen, um zu sehen, welche Formulierung eine höhere Konversionsrate erzielt.<br><br>
- **Kanalkombinationen:** Testen Sie die Wirksamkeit verschiedener Nachrichtenkanal-Kombinationen. Sie können beispielsweise die Wirkung einer reinen E-Mail mit der einer E-Mail in Kombination mit einem Push vergleichen.

## Einen Experimentpfad erstellen {#creating-an-experiment-path}

Um eine Experimentpfad-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Ende eines Schritts und wählen Sie **Experimentpfade** aus.

In der Standardkonfiguration dieser Komponente gibt es zwei Standard-Pfade, **Pfad 1** und **Pfad 2**, wobei jeweils 50 % der Zielgruppe durch jeden Pfad geleitet werden. Klicken Sie auf die Komponente, um das Panel **Experiment-Einstellungen** zu erweitern, und Sie sehen die Konfigurationsoptionen für die Komponente.

### 1. Schritt: Anzahl der Pfade und Zielgruppenverteilung festlegen {#step-1-choose-the-number-of-paths-and-audience-distribution}

Sie können bis zu vier Pfade hinzufügen, indem Sie auf **Pfad hinzufügen** klicken, und eine optionale Kontrollgruppe, indem Sie **Kontrollgruppe hinzufügen** aktivieren. Über die Prozentfelder für jeden Pfad können Sie festlegen, welcher Prozentsatz der Zielgruppe auf jeden Pfad und die Kontrollgruppe entfallen soll. Die angegebenen Prozentsätze müssen zusammen 100 % ergeben, um fortzufahren. Wenn Sie schnell alle verfügbaren Pfade (und die Kontrollgruppe) auf denselben Prozentsatz setzen möchten, klicken Sie auf **Pfade gleichmäßig verteilen**.

Sie können außerdem festlegen, ob Nutzer:innen in der Kontrollgruppe den Canvas weiter durchlaufen oder nach dem Konversions-Tracking-Fenster für das **Kontrollgruppenverhalten** aussteigen sollen. Optional können Sie eine Beschreibung hinzufügen, um anderen zu erklären, was dieser Experimentpfad testen soll, oder zusätzliche Informationen angeben, die hilfreich sein könnten.

![Experiment-Einstellungen, in denen Sie Pfade hinzufügen und den Prozentsatz der Nutzer:innen in jedem Pfad verteilen können.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Wenn die erneute Canvas-Berechtigung aktiviert ist, durchlaufen Nutzer:innen, die in den Canvas eintreten und einen zufällig ausgewählten Pfad nehmen, bei erneuter Berechtigung und erneutem Eintritt denselben Pfad. Dies gewährleistet die Validität des Experiments und der zugehörigen Analytics. Wenn der Schritt die Pfadzuweisung immer zufällig vornehmen soll, wählen Sie **Zufällige Pfade in Experimentpfaden**. Diese Option ist bei Verwendung von Winning Path oder personalisierten Pfaden nicht verfügbar.
{% endalert %}

### 2. Schritt: Winning Path oder personalisierte Pfade aktivieren (optional) {#step-2}

Sie können Ihr Experiment optimieren, indem Sie [Winning Path]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) oder [personalisierte Pfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths) aktivieren. Beide Optionen funktionieren, indem zunächst Ihre Pfade mit einem Teil Ihrer Zielgruppe getestet werden. Nachdem das Experiment beendet ist, werden die verbleibenden und nachfolgenden Nutzer:innen entweder über den insgesamt leistungsstärksten Pfad (Winning Path) oder den für jede:n Nutzer:in leistungsstärksten Pfad (personalisierte Pfade) geleitet.

### 3. Schritt: Pfade erstellen {#step-3-create-paths}

Abschließend müssen Sie Ihre nachgelagerten Pfade erstellen. Wählen Sie **Fertig** und kehren Sie zum Canvas-Builder zurück. Klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button unter jedem Pfad, um mit den üblichen Canvas-Werkzeugen Journeys nach Belieben zu erstellen, und starten Sie den Canvas, wenn Sie bereit sind.

![Schritte zu jedem Pfad hinzufügen, der von einer Experimentpfad-Komponente abzweigt.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Beachten Sie, dass Pfade und ihre nachgelagerten Schritte nach der Erstellung nicht mehr aus einem Canvas entfernt werden können. Nach dem Start können Sie jedoch die Zielgruppenverteilung über die Pfade nach Bedarf anpassen. Wenn Sie beispielsweise einen Tag nach dem Start eines Canvas auf Basis der Analytics feststellen, dass ein Pfad den anderen überlegen ist, können Sie diesen Pfad auf 100 % und die anderen auf 0 % setzen. Oder Sie können je nach Bedarf weiterhin Nutzer:innen über mehrere Pfade leiten.

{% alert important %}
Um eine Kontamination des Experiments zu vermeiden, gilt: Wenn Ihr Canvas ein aktives oder laufendes Winning-Path- oder personalisiertes-Pfade-Experiment hat und Sie den aktiven Canvas aktualisieren – unabhängig davon, ob Sie den Experimentpfad-Schritt selbst aktualisieren – wird das laufende Experiment beendet, und der Experiment-Schritt bestimmt keinen Winning Path und keine personalisierten Pfade. Um das Experiment neu zu starten, können Sie den bestehenden Experimentpfad trennen und einen neuen starten oder den Canvas duplizieren und einen neuen Canvas starten. Andernfalls durchlaufen Nutzer:innen den Experimentpfad, als wäre keine Optimierungsmethode ausgewählt worden. Sie können außerdem für einen bereits aktiven Canvas mit einem Experimentpfad-Schritt keine personalisierten Pfade oder Winning Paths aktivieren.<br><br>Weitere Informationen finden Sie unter [Canvases nach dem Start bearbeiten]({{site.baseurl}}/post-launch_edits).
{% endalert %}

## Performance tracken {#tracking-performance}

Wählen Sie auf der Seite **Canvas Analytics** den Experimentpfad aus, um eine [detaillierte Tabelle]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch) zu öffnen, die mit dem Tab **Varianten analysieren** identisch ist und detaillierte Performance- und Konversionsstatistiken pfadübergreifend vergleicht. Sie können die Tabelle auch als CSV exportieren und prozentuale Änderungen für relevante Metriken relativ zum ausgewählten Pfad oder zur Kontrollgruppe vergleichen.

Jeder Schritt in jedem Pfad zeigt Statistiken in der Ansicht [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) an, genau wie jeder andere Canvas-Schritt. Beachten Sie jedoch, dass die Analytics einzelner Schritte und die Experimentpfad-Analytics Konversionen unterschiedlich messen:

- **Experimentpfad-Analytics** tracken Konversionen ab dem Zeitpunkt, an dem Nutzer:innen den Experimentpfad-Schritt betreten. Dies ist die empfohlene Ansicht zum Vergleich der Performance über Pfade hinweg, da alle Pfade denselben Ausgangspunkt haben.
- **Analytics einzelner Schritte** (z. B. Nachrichten-Schritt-Analytics) tracken Konversionen ab dem Zeitpunkt, an dem Nutzer:innen diesen spezifischen Schritt erhalten (zum Beispiel wenn die Nachricht gesendet wird).

Da diese Konversionsfenster unterschiedliche Ausgangspunkte haben, können sie unterschiedliche Konversionsraten für denselben Pfad anzeigen – insbesondere wenn es Verzögerungen zwischen dem Experimentschritt und einer nachgelagerten Nachricht gibt. Für den zuverlässigsten Vergleich über Pfade hinweg verwenden Sie die Experimentpfad-Analytics.

### Winning Path und Performance personalisierter Pfade {#winning-path-and-personalized-paths-performance}

Nutzen Sie Winning Paths, um die Performance über einen Zeitraum zu tracken und nachfolgende Nutzer:innen dann automatisch über den Pfad mit der besten Performance zu leiten. Weitere Informationen zu den Analytics, wenn **Winning Path** oder **Personalisierte Pfade** für Ihr Experiment aktiviert sind, finden Sie unter:

- [Winning Path]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path#analytics)
- [Personalisierte Pfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths#analytics)

Die Gewinnmetrik und die in Experimentpfaden angezeigten Analytics können voneinander abweichen:

- Das Konversions-Event, das Sie für **Winning Path** oder **Personalisierte Pfade** konfigurieren, bestimmt, wie Braze Pfade vergleicht und während des Experimentfensters einen Gewinner auswählt.
- Experimentpfad-Analytics folgen weiterhin demselben [Konversions-Event]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)-Framework des Canvas wie der Rest des Canvas, einschließlich Ihres [primären Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events#primary-conversion-event). Daher stimmen die im Dashboard hervorgehobenen Metriken möglicherweise nicht mit der Gewinnmetrik überein.
- Bei Push unterscheiden sich *Direct Opens* und *Total Opens*. Weitere Informationen finden Sie unter [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

### Zusätzliche Einstellungen {#additional-settings}

Experimentpfade erfassen Nutzer:innen, die jeden Schritt betreten und im zugewiesenen Pfad konvertieren. Dabei werden alle in der Canvas-Einrichtung festgelegten Konversions-Events getrackt. Geben Sie im Tab **Zusätzliche Einstellungen** an, wie viele Tage (zwischen 1 und 30) dieses Experiment Konversionen tracken soll. Das hier festgelegte Zeitfenster bestimmt, wie lange die Konversions-Events (die in der Canvas-Einrichtung ausgewählt wurden) für das Experiment getrackt werden. Die in der Canvas-Einrichtung festgelegten Konversionsfenster pro Event gelten nicht für das Tracking dieses Schritts und werden durch dieses Konversionsfenster ersetzt.

Das Konversionsfenster beginnt, wenn Nutzer:innen den Experimentpfad-Schritt betreten, nicht wenn eine nachgelagerte Nachricht gesendet wird. Wenn ein Pfad Verzögerungen enthält – z. B. einen Verzögerungsschritt oder [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) – verbrauchen diese Verzögerungen einen Teil des Konversionsfensters.

{% alert important %}
Wenn Sie intelligentes Timing bei einem Nachrichten-Schritt innerhalb eines Experimentpfads verwenden, verringert die Zeit zwischen dem Experimenteintritt und dem tatsächlichen Nachrichtenversand das effektive Konversionsfenster für diesen Pfad. Wenn Ihr Experiment beispielsweise ein 5-Tage-Konversionsfenster hat und intelligentes Timing die Nachricht um 2 Tage verzögert, haben Nutzer:innen auf diesem Pfad nur 3 Tage nach Erhalt der Nachricht, um innerhalb des Experimentfensters zu konvertieren – obwohl die Analytics des Nachrichten-Schritts selbst Konversionen ab dem Zeitpunkt des Nachrichtenversands tracken.<br><br>Für klarere Experiment-Analytics platzieren Sie Verzögerungen (z. B. Verzögerungsschritte) **vor** dem Experimentpfad-Schritt statt innerhalb eines Experimentpfads. Auf diese Weise starten alle Pfade vom gleichen Punkt aus und Verzögerungen verbrauchen keinen Teil des Konversionsfensters.
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum unterscheiden sich die Versendungen zwischen den Pfaden, obwohl die Experiment-Aufteilung gleichmäßig aussieht? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Die nachgelagerten _Versendungen_ hängen von den Schritten, Verzögerungen, der Kanalberechtigung und den Inhalten jedes Pfads ab – nicht nur vom prozentualen Split am Experimentpfad. Beispielsweise können unterschiedliche Verzögerungen, intelligentes Timing oder der Abo-Status beeinflussen, wie viele Nutzer:innen eine Nachricht erhalten, selbst wenn die Pfadzuweisung ausgeglichen war. Um die Ergebnisse der Pfade zu vergleichen, verwenden Sie die [Experimentpfad-Analytics](#tracking-performance), die Konversionen ab einem gemeinsamen Einstiegspunkt messen.

### Wie lange dauert das Konversionsfenster des Experiments? {#how-long-does-the-experiment-conversion-window-last}

Das Konversionsfenster unter **Additional Settings** (1–30 Tage) beginnt, wenn Nutzer:innen den Experimentpfad-Schritt betreten. Die Zeit, die in nachgelagerten Verzögerungsschritten oder beim Warten auf intelligentes Timing verbracht wird, wird auf dieses Fenster angerechnet. Weitere Informationen finden Sie unter [Performance verfolgen](#tracking-performance).