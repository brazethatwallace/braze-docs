---
nav_title: Personalisierte Pfade
article_title: Personalisierte Pfade in Experimentpfaden
page_type: reference
description: "Personalisierte Pfade ermöglichen es Ihnen, jeden Punkt einer Canvas-Journey für einzelne Nutzer:innen basierend auf der Conversion-Wahrscheinlichkeit zu personalisieren."
tool: Canvas
---

# Personalisierte Pfade in Experimentpfaden {#personalized-paths-in-experiment-paths}

> Personalisierte Pfade ähneln der [personalisierten Variante]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations#personalized-variant) in Campaigns und ermöglichen es Ihnen, jeden Punkt einer Canvas-Journey für einzelne Nutzer:innen basierend auf der Conversion-Wahrscheinlichkeit zu personalisieren.

## Wie Personalisierte Pfade funktionieren {#how-personalized-paths-works}

Wenn Personalisierte Pfade in einem Experimentpfade-Schritt aktiviert sind, unterscheidet sich das Verhalten leicht, je nachdem, ob Ihr Canvas für einen einmaligen Versand oder für wiederkehrende Versendungen konfiguriert ist:

- **Einmaliger Canvas-Versand:** Eine Gruppe von Nutzer:innen wird in einer Verzögerungsgruppe zurückgehalten. Die übrigen Nutzer:innen durchlaufen einen ersten Test, um ein Vorhersagemodell für eine von Ihnen konfigurierte Dauer zu trainieren – mindestens 24 Stunden für optimale Ergebnisse. Nach dem Test wird ein Modell erstellt, das lernt, welche Verhaltensweisen der Nutzer:innen mit einer höheren Wahrscheinlichkeit einer Konversion auf einem bestimmten Pfad verbunden waren. Schließlich wird jede:r Nutzer:in in der Verzögerungsgruppe auf den Pfad geleitet, der basierend auf den gezeigten Verhaltensweisen und den Erkenntnissen des Vorhersagemodells aus dem ersten Test am wahrscheinlichsten zu einer Konversion führt.
- **Wiederkehrende, aktionsbasierte und API-getriggerte Canvases:** Ein erstes Experiment wird mit allen Nutzer:innen durchgeführt, die den Experimentpfad während eines festgelegten Zeitfensters betreten. Um die Integrität des Experiments zu wahren, wird Nutzer:innen, die vor Ende des Zeitfensters mehrere Nachrichten erhalten, jedes Mal dieselbe Variante zugewiesen. Nach dem Experimentfenster wird jede:r Nutzer:in auf den Pfad geleitet, der für sie am wahrscheinlichsten zu einer Konversion führt.

## Personalisierte Pfade verwenden {#using-personalized-paths}

### Schritt 1: Experimentpfad hinzufügen {#step-1-add-an-experiment-path}

Fügen Sie Ihrem Canvas einen [Experimentpfad]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) hinzu und aktivieren Sie dann **Personalisierte Pfade**.

![Fügen Sie Ihrem Canvas einen Experimentpfad hinzu und aktivieren Sie dann „Personalisierte Pfade“.]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Schritt 2: Einstellungen für personalisierte Pfade konfigurieren {#step-2-configure-personalized-paths-settings}

Legen Sie das Konversions-Event fest, das den Gewinner bestimmen soll. Wenn keine Konversions-Events verfügbar sind, kehren Sie zum ersten Schritt der Canvas-Einrichtung zurück und [weisen Sie Konversions-Events zu]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Wenn Sie Öffnungen oder Klicks als Konversions-Event auswählen, stellen Sie sicher, dass der erste Schritt im Pfad ein [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) ist. Braze zählt nur das Engagement des ersten Nachrichtenschritts in jedem jeweiligen Pfad. Wenn der Pfad mit einem anderen Schritt beginnt (z. B. einem Verzögerungs- oder Zielgruppenpfadschritt) und die Nachricht erst später kommt, wird diese Nachricht bei der Performance-Bewertung nicht berücksichtigt.

Legen Sie dann das **Experimentfenster** fest. Das **Experimentfenster** bestimmt, wie lange Nutzer:innen alle Pfade durchlaufen, bevor der beste Pfad für jede:n Nutzer:in in der Verzögerungsgruppe ausgewählt wird. Das Fenster beginnt, wenn die/der erste Nutzer:in den Schritt betritt.

![Screenshot zu Schritt 2: Einstellungen für personalisierte Pfade konfigurieren.]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Schritt 3: Fallback festlegen {#step-3-determine-fallback}

Standardmäßig werden alle zukünftigen Nutzer:innen den einzelnen leistungsstärksten Pfad durchlaufen, wenn die Testergebnisse nicht ausreichen, um einen statistisch signifikanten Gewinner zu ermitteln.

Alternativ können Sie **Alle zukünftigen Nutzer:innen weiterhin den Mix aus Pfaden senden** auswählen.

![Alternativ können Sie „Alle zukünftigen Nutzer:innen weiterhin den Mix aus Pfaden senden“ auswählen.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Diese Option sendet zukünftige Nutzer:innen gemäß den in der Experimentpfad-Verteilung angegebenen Prozentsätzen durch den Mix aus Pfaden.

![Screenshot zu Schritt 3: Fallback festlegen.]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

{% alert note %}
Wenn das Experiment mit unzureichenden Ergebnissen abgeschlossen wird, wird nur der Tab **Initiales Experiment** angezeigt, da das Modell feststellt, dass die Personalisierung einen einzelnen leistungsstärksten Pfad nicht übertreffen würde. Weitere Details finden Sie unter [Analytics](#analytics).
{% endalert %}

### Schritt 4: Pfade hinzufügen und Canvas starten {#step-4-add-your-paths-and-launch-the-canvas}

{% tabs local %}
{% tab Einmalversand-Canvas %}

Eine einzelne Experimentpfad-Komponente kann bis zu vier Pfade enthalten. Bei Einmalversand-Canvases können Sie jedoch nur bis zu drei Pfade hinzufügen, wenn personalisierte Pfade aktiviert sind. Der vierte Pfad sollte für die Verzögerungsgruppe reserviert sein, die Braze automatisch zu Ihrem Experiment hinzufügt.

Schließen Sie die Einrichtung Ihres Canvas nach Bedarf ab und starten Sie ihn. Sobald die/der erste Nutzer:in das Experiment betreten hat, können Sie das Canvas überprüfen, um die eingehenden Analytics zu sehen und die [Performance Ihres Experiments zu verfolgen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

![Screenshot zu Schritt 4: Pfade hinzufügen und Canvas starten.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Wenn das Experimentfenster abgelaufen und das Experiment abgeschlossen ist, sendet Braze die Nutzer:innen in der Verzögerungsgruppe auf ihre jeweiligen Pfade mit der höchsten personalisierten Konversionswahrscheinlichkeit, basierend auf der Empfehlung des prädiktiven Modells.

![Screenshot zu Schritt 4: Pfade hinzufügen und Canvas starten.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Wiederkehrendes, aktionsbasiertes oder API-getriggertes Canvas %}

Sie können bis zu vier Pfade in einem einzelnen Experimentpfad testen. Fügen Sie Ihre Pfade hinzu, schließen Sie die Einrichtung Ihres Canvas nach Bedarf ab und starten Sie ihn.

Sobald die/der erste Nutzer:in das Experiment betreten hat, können Sie das Canvas überprüfen, um die eingehenden Analytics zu sehen und die [Performance Ihres Experiments zu verfolgen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Wenn das Experimentfenster abgelaufen und das Experiment abgeschlossen ist, werden alle nachfolgenden Nutzer:innen, die das Canvas betreten, auf den Pfad geleitet, der für sie am wahrscheinlichsten zu einer Konversion führt.

![Screenshot zu Schritt 4: Pfade hinzufügen und Canvas starten.]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Analytics {#analytics}

Wenn personalisierte Pfade aktiviert sind und ausreichende Ergebnisse liefern, ist Ihre Analytics-Ansicht in zwei Tabs unterteilt: **Initial Experiment** und **Personalized Paths**.

Wenn das Experiment mit unzureichenden Ergebnissen abgeschlossen wird (zum Beispiel wenn der prognostizierte Lift des Modells unter dem Schwellenwert von 0,5 % liegt oder keine aussagekräftigen Nutzersegmente identifiziert werden), wird nur der Tab **Initial Experiment** angezeigt, da das Modell feststellt, dass die Personalisierung nicht besser abschneiden würde als ein einzelner leistungsstärkster Pfad. In diesem Fall wird Ihr konfiguriertes Fallback-Verhalten angewendet, und es stehen keine Analytics für personalisierte Pfade zur Verfügung.

{% tabs local %}
{% tab Initial Experiment %}

Der Tab **Initial Experiment** zeigt die Metriken für jeden Pfad während des Experiment-Zeitfensters. Sie können eine Zusammenfassung sehen, wie alle Pfade für die angegebenen Konversions-Events abgeschnitten haben.

![Ergebnisse eines initialen Experiments, das gesendet wurde, um den leistungsstärksten Pfad für jede:n Nutzer:in zu ermitteln. Eine Tabelle zeigt die Performance jedes Pfads basierend auf verschiedenen Metriken für den Zielkanal.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Standardmäßig sucht der Test nach Zusammenhängen zwischen den angepassten Events der Nutzer:innen und ihren Pfadpräferenzen, also der Nachrichtenvariante, auf die eine Person am besten reagiert. Diese Analyse erkennt, ob angepasste Events die Wahrscheinlichkeit erhöhen oder verringern, auf einen bestimmten Pfad zu reagieren. Diese Zusammenhänge werden dann verwendet, um zu bestimmen, welche Nutzer:innen nach Ablauf des Experiment-Zeitfensters welchem Pfad zugewiesen werden.

Die Zusammenhänge zwischen angepassten Events und Pfadpräferenzen werden in der Tabelle auf dem Tab **Initial Experiment** angezeigt.

![Screenshot zu Analytics.]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Wenn der Test keinen aussagekräftigen Zusammenhang zwischen angepassten Events und Pfadpräferenzen finden kann, greift der Test auf eine sitzungsbasierte Analysemethode zurück, und es werden keine Tabellen mit angepassten Event-Daten angezeigt.

{% details Fallback-Analysemethode %}

**Sitzungsbasierte Analysemethode**<br>
Wenn die Fallback-Methode zur Bestimmung personalisierter Pfade verwendet wird, zeigt der Tab **Initial Experiment** eine Aufschlüsselung der bevorzugten Varianten der Nutzer:innen basierend auf einer Kombination bestimmter Merkmale.

Diese Merkmale sind:

- **Aktualität:** Wann die letzte Sitzung stattfand
- **Häufigkeit:** Wie oft Sitzungen stattfinden
- **Zugehörigkeitsdauer:** Wie lange die Person bereits Nutzer:in ist

![Die Tabelle „Nutzermerkmale“ zeigt, welche Nutzer:innen voraussichtlich Pfad 1 und Pfad 2 bevorzugen, basierend auf den drei Buckets, in die sie für Aktualität, Häufigkeit und Zugehörigkeitsdauer fallen.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Stellen Sie sich Aktualität als den Zeitpunkt der letzten Interaktion vor, Häufigkeit als die Regelmäßigkeit des Engagements und Zugehörigkeitsdauer als die Gesamtdauer des Engagements mit Ihnen. Wir gruppieren Nutzer:innen basierend auf diesen drei Faktoren in „Buckets“ (wie in der Tabelle **Nutzermerkmale** erläutert) und sehen dann, welcher Bucket welchen Pfad bevorzugt. Es ist, als würden Sie Nutzer:innen in Hunderte verschiedener Listen sortieren – basierend darauf, wann sie zuletzt bei Ihnen eingekauft haben, wie oft sie einkaufen und wie lange sie bereits Kund:innen sind.

Bei der Auswahl einer Nachricht für eine:n Nutzer:in untersucht Braze die Buckets, in die sie fallen. Jeder Bucket übt einen unterschiedlichen Einfluss auf die Pfadauswahl aus. Wir quantifizieren diesen Einfluss mit einer statistischen Methode namens [logistische Regression](https://en.wikipedia.org/wiki/Logistic_regression), die zukünftiges Verhalten basierend auf vergangenen Aktionen vorhersagt. Diese Methode berücksichtigt Nutzerinteraktionen während des initialen Nachrichtenversands. Die Tabelle fasst die Ergebnisse lediglich zusammen, indem sie anzeigt, mit welchem Pfad Nutzer:innen in jedem Bucket tendenziell interagiert haben.

Letztendlich kombiniert Braze all diese Daten, um für jede:n Nutzer:in einen maßgeschneiderten Nachrichtenpfad auszuwählen, damit er so ansprechend und relevant wie möglich ist.

{% alert note %}
Die Zeitintervalle für jeden Bucket werden basierend auf Canvas-spezifischen Nutzerdaten bestimmt, die zwischen Canvases variieren können.
{% endalert %}

**Wie personalisierte Pfade ausgewählt werden**<br>
Bei dieser Methode ist die empfohlene Nachricht für eine:n einzelne:n Nutzer:in die Summe der Effekte ihrer spezifischen Aktualität, Häufigkeit und Zugehörigkeitsdauer. Aktualität, Häufigkeit und Zugehörigkeitsdauer werden in Buckets aufgeteilt, wie in der Tabelle **Nutzermerkmale** dargestellt. Der Zeitbereich jedes Buckets wird durch die Daten der Nutzer:innen in jedem einzelnen Canvas bestimmt und variiert von Canvas zu Canvas.

Jeder Bucket kann einen unterschiedlichen Beitrag oder „Impuls“ in Richtung jedes Pfads haben. Die Stärke des Impulses für jeden Bucket wird aus den Nutzerantworten im initialen Experiment mittels [logistischer Regression](https://en.wikipedia.org/wiki/Logistic_regression) bestimmt. Die Tabelle fasst die Ergebnisse lediglich zusammen, indem sie anzeigt, mit welchem Pfad Nutzer:innen in jedem Bucket tendenziell interagiert haben. Der tatsächliche personalisierte Pfad einer einzelnen Person hängt von der Summe der Effekte der drei Buckets ab, in denen sie sich befindet – einer für jedes Merkmal.

{% enddetails %}

{% endtab %}
{% tab Personalisierte Pfade %}

Der Tab **Personalized Paths** zeigt die Ergebnisse des finalen Experiments, bei dem die Nutzer:innen in der Verzögerungsgruppe den für sie leistungsstärksten Pfad entlang gesendet wurden.

Die drei Karten auf dieser Seite zeigen Ihren prognostizierten Lift, die Gesamtergebnisse und die prognostizierten Ergebnisse, wenn Sie stattdessen nur den Gewinnerpfad gesendet hätten. Selbst wenn es keinen Lift gibt, was manchmal vorkommen kann, ist das Ergebnis dasselbe wie beim Senden nur des Gewinnerpfads (ein traditioneller A/B-Test).

- **Projected Lift:** Die Verbesserung Ihres ausgewählten Konversions-Events durch die Verwendung personalisierter Pfade anstelle des Sendens aller Nutzer:innen über den insgesamt leistungsstärksten Pfad.
- **Overall Results:** Die Ergebnisse des zweiten Versands basierend auf Ihrem Konversions-Event.
- **Projected Results:** Die prognostizierten Ergebnisse des zweiten Versands basierend auf Ihrer gewählten Optimierungsmetrik, wenn Sie stattdessen nur die Gewinnervariante gesendet hätten.

![Tab „Personalized Paths“ für einen Canvas. Die Karten zeigen den prognostizierten Lift, die Gesamt-Conversions (mit personalisierten Pfaden) und die prognostizierten eindeutigen Öffnungen (mit Gewinnerpfad).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Personalisierte Pfade mit Zustellung zur Ortszeit verwenden {#using-personalized-paths-with-local-time-delivery}

Wir empfehlen nicht, die Zustellung zur Ortszeit in Canvases mit personalisierten Pfaden zu verwenden. Der Grund dafür ist, dass Experimentfenster beginnen, sobald die erste Nutzer:in den Schritt durchläuft. Nutzer:innen in sehr frühen Zeitzonen können den Schritt betreten und den Start des Experimentfensters viel früher als erwartet auslösen, was dazu führen kann, dass das Experiment endet, bevor der Großteil Ihrer Nutzer:innen in typischeren Zeitzonen genügend Zeit hatte, den Canvas zu betreten und zu konvertieren.

Wenn Sie alternativ die Zustellung zur Ortszeit verwenden möchten, nutzen Sie ein Experimentfenster von 24–48 oder mehr Stunden. Auf diese Weise betreten Nutzer:innen in frühen Zeitzonen den Canvas und lösen den Start des Experiments aus, aber es verbleibt noch ausreichend Zeit im Experimentfenster. Nutzer:innen in späteren Zeitzonen haben dann immer noch genügend Zeit, den Canvas und den Experimentschritt mit personalisierten Pfaden zu betreten und möglicherweise zu konvertieren, bevor das Experimentfenster abläuft.