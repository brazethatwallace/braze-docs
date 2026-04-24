---
nav_title: Personalisierte Pfade
article_title: Personalisierte Pfade in Experimentpfaden
page_type: reference
description: "Personalisierte Pfade ermöglichen es Ihnen, jeden Punkt einer Canvas-Journey für einzelne Nutzer:innen basierend auf der Conversion-Wahrscheinlichkeit zu personalisieren."
tool: Canvas
---

# Personalisierte Pfade in Experimentpfaden

> Personalisierte Pfade ähneln der [personalisierten Variante]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations#personalized-variant) in Kampagnen und ermöglichen es Ihnen, jeden Punkt einer Canvas-Journey für einzelne Nutzer:innen basierend auf der Conversion-Wahrscheinlichkeit zu personalisieren.

## So funktionieren personalisierte Pfade

Wenn personalisierte Pfade in einem Experiment-Pfad-Schritt aktiviert sind, unterscheidet sich das Verhalten leicht, je nachdem, ob Ihr Canvas für einen einmaligen Versand oder für wiederkehrende Versendungen konfiguriert ist:

- **Einmaliger Canvas-Versand:** Eine Gruppe von Nutzer:innen wird in einer Verzögerungsgruppe zurückgehalten. Die übrigen Nutzer:innen durchlaufen einen initialen Test, um ein prädiktives Modell für eine von Ihnen konfigurierte Dauer zu trainieren – mindestens 24 Stunden für beste Ergebnisse. Nach dem Test wird ein Modell erstellt, das lernt, welche Nutzerverhalten mit einer höheren Conversion-Wahrscheinlichkeit auf einem bestimmten Pfad verbunden waren. Schließlich wird jede:r Nutzer:in in der Verzögerungsgruppe den Pfad entlang gesendet, der basierend auf dem gezeigten Verhalten und den Erkenntnissen des prädiktiven Modells aus dem initialen Test am wahrscheinlichsten zu einer Conversion führt.
- **Wiederkehrende, aktionsgetriggerte und API-getriggerte Canvases:** Ein initiales Experiment wird mit allen Nutzer:innen durchgeführt, die während eines festgelegten Zeitfensters den Experiment-Pfad betreten. Um die Integrität des Experiments zu wahren, wird Nutzer:innen, die vor Ende des Zeitfensters mehrere Nachrichten erhalten, jedes Mal dieselbe Variante zugewiesen. Nach dem Experiment-Zeitfenster wird jede:r Nutzer:in den Pfad entlang gesendet, der am wahrscheinlichsten zu einer Conversion führt.

## Personalisierte Pfade verwenden

### 1. Schritt: Einen Experiment-Pfad hinzufügen

Fügen Sie Ihrem Canvas einen [Experiment-Pfad]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) hinzu und aktivieren Sie dann **Personalisierte Pfade**.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### 2. Schritt: Einstellungen für personalisierte Pfade konfigurieren

Legen Sie das Konversions-Event fest, das den Gewinner bestimmen soll. Wenn keine Konversions-Events verfügbar sind, kehren Sie zum ersten Schritt der Canvas-Einrichtung zurück und [weisen Sie Konversions-Events zu]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#choose-conversion-events).

Wenn Sie Öffnungen oder Klicks als Konversions-Event wählen, stellen Sie sicher, dass der erste Schritt im Pfad ein [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) ist. Braze zählt nur das Engagement des ersten Nachrichten-Schritts in jedem jeweiligen Pfad. Wenn der Pfad mit einem anderen Schritt beginnt (wie einem Verzögerungs- oder Zielgruppenpfad-Schritt) und die Nachricht erst später kommt, wird diese Nachricht bei der Performance-Bewertung nicht berücksichtigt.

Legen Sie dann das **Experiment-Zeitfenster** fest. Das **Experiment-Zeitfenster** bestimmt, wie lange Nutzer:innen alle Pfade durchlaufen, bevor der beste Pfad für jede:n Nutzer:in in der Verzögerungsgruppe ausgewählt wird. Das Zeitfenster beginnt, wenn die erste Person den Schritt betritt.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### 3. Schritt: Fallback festlegen

Standardmäßig werden alle zukünftigen Nutzer:innen den einzelnen leistungsstärksten Pfad entlang gesendet, wenn die Testergebnisse nicht ausreichen, um einen statistisch signifikanten Gewinner zu ermitteln.

Alternativ können Sie **Alle zukünftigen Nutzer:innen weiterhin den Mix aus Pfaden senden** auswählen.

![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Diese Option sendet zukünftige Nutzer:innen den Mix aus Pfaden gemäß den in der Experiment-Pfad-Verteilung angegebenen Prozentsätzen entlang.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### 4. Schritt: Pfade hinzufügen und den Canvas starten

{% tabs local %}
{% tab Einmaliger Canvas-Versand %}

Eine einzelne Experiment-Pfad-Komponente kann bis zu vier Pfade enthalten. Bei einmaligen Canvases können Sie jedoch nur bis zu drei Pfade hinzufügen, wenn personalisierte Pfade aktiviert sind. Der vierte Pfad sollte für die Verzögerungsgruppe reserviert sein, die Braze automatisch zu Ihrem Experiment hinzufügt.

Schließen Sie die Einrichtung Ihres Canvas nach Bedarf ab und starten Sie ihn. Sobald die erste Person das Experiment betreten hat, können Sie den Canvas überprüfen, um die eingehenden Analytics zu sehen und die [Performance Ihres Experiments zu verfolgen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Wenn das Experiment-Zeitfenster abgelaufen und das Experiment abgeschlossen ist, sendet Braze die Nutzer:innen in der Verzögerungsgruppe auf ihre jeweiligen Pfade mit der höchsten personalisierten Conversion-Wahrscheinlichkeit, basierend auf der Empfehlung des prädiktiven Modells.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Wiederkehrender, aktionsgetriggerter oder API-getriggerter Canvas %}

Sie können bis zu vier Pfade in einem einzelnen Experiment-Pfad testen. Fügen Sie Ihre Pfade hinzu, schließen Sie die Einrichtung Ihres Canvas nach Bedarf ab und starten Sie ihn.

Sobald die erste Person das Experiment betreten hat, können Sie den Canvas überprüfen, um die eingehenden Analytics zu sehen und die [Performance Ihres Experiments zu verfolgen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Wenn das Experiment-Zeitfenster abgelaufen und das Experiment abgeschlossen ist, werden alle nachfolgenden Nutzer:innen, die den Canvas betreten, den Pfad entlang gesendet, der am wahrscheinlichsten zu einer Conversion für sie führt.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Analytics {#analytics}

Wenn personalisierte Pfade aktiviert waren, ist Ihre Analytics-Ansicht in zwei Tabs unterteilt: **Initiales Experiment** und **Personalisierte Pfade**.

{% tabs local %}
{% tab Initiales Experiment %}

Der Tab **Initiales Experiment** zeigt die Metriken für jeden Pfad während des Experiment-Zeitfensters. Sie können eine Zusammenfassung sehen, wie alle Pfade für die angegebenen Konversions-Events abgeschnitten haben.

![Ergebnisse eines initialen Experiments, das gesendet wurde, um den leistungsstärksten Pfad für jede:n Nutzer:in zu ermitteln. Eine Tabelle zeigt die Performance jedes Pfads basierend auf verschiedenen Metriken für den Zielkanal.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Standardmäßig sucht der Test nach Zusammenhängen zwischen den angepassten Events der Nutzer:innen und ihren Pfadpräferenzen, also der Nachrichtenvariante, auf die eine Person am besten reagiert. Diese Analyse erkennt, ob angepasste Events die Wahrscheinlichkeit erhöhen oder verringern, auf einen bestimmten Pfad zu reagieren. Diese Zusammenhänge werden dann verwendet, um zu bestimmen, welche Nutzer:innen nach Ablauf des Experiment-Zeitfensters welchem Pfad zugewiesen werden.

Die Zusammenhänge zwischen angepassten Events und Pfadpräferenzen werden in der Tabelle auf dem Tab **Initiales Experiment** angezeigt.

![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Wenn der Test keinen aussagekräftigen Zusammenhang zwischen angepassten Events und Pfadpräferenzen finden kann, greift der Test auf eine sitzungsbasierte Analysemethode zurück, und es werden keine Tabellen mit angepassten Event-Daten angezeigt.

{% details Fallback-Analysemethode %}

**Sitzungsbasierte Analysemethode**<br>
Wenn die Fallback-Methode zur Bestimmung personalisierter Pfade verwendet wird, zeigt der Tab **Initiales Experiment** eine Aufschlüsselung der bevorzugten Varianten der Nutzer:innen basierend auf einer Kombination bestimmter Merkmale.

Diese Merkmale sind:

- **Aktualität:** Wann die letzte Sitzung stattfand
- **Häufigkeit:** Wie oft Sitzungen stattfinden
- **Zugehörigkeitsdauer:** Wie lange die Person bereits Nutzer:in ist

![Die Tabelle „Nutzermerkmale", die zeigt, welche Nutzer:innen voraussichtlich Pfad 1 und Pfad 2 bevorzugen, basierend auf den drei Buckets, in die sie für Aktualität, Häufigkeit und Zugehörigkeitsdauer fallen.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Stellen Sie sich Aktualität als den Zeitpunkt der letzten Interaktion vor, Häufigkeit als die Regelmäßigkeit des Engagements und Zugehörigkeitsdauer als die Gesamtdauer des Engagements mit Ihnen. Wir gruppieren Nutzer:innen basierend auf diesen drei Faktoren in „Buckets" (wie in der Tabelle **Nutzermerkmale** erläutert) und sehen dann, welcher Bucket welchen Pfad bevorzugt. Es ist, als würden Sie Nutzer:innen in Hunderte verschiedener Listen sortieren – basierend darauf, wann sie zuletzt bei Ihnen eingekauft haben, wie oft sie einkaufen und wie lange sie bereits Kund:innen sind.

Bei der Auswahl einer Nachricht für eine:n Nutzer:in untersucht Braze die Buckets, in die sie fallen. Jeder Bucket übt einen unterschiedlichen Einfluss auf die Pfadauswahl aus. Wir quantifizieren diesen Einfluss mit einer statistischen Methode namens [logistische Regression](https://en.wikipedia.org/wiki/Logistic_regression), die zukünftiges Verhalten basierend auf vergangenen Aktionen vorhersagt. Diese Methode berücksichtigt Nutzerinteraktionen während des initialen Nachrichtenversands. Die Tabelle fasst die Ergebnisse lediglich zusammen, indem sie anzeigt, mit welchem Pfad Nutzer:innen in jedem Bucket tendenziell interagiert haben.

Letztendlich kombiniert Braze all diese Daten, um für jede:n Nutzer:in einen maßgeschneiderten Nachrichtenpfad auszuwählen, damit er so ansprechend und relevant wie möglich ist.

{% alert note %}
Die Zeitintervalle für jeden Bucket werden basierend auf Canvas-spezifischen Nutzerdaten bestimmt, die zwischen Canvases variieren können.
{% endalert %}

**Wie personalisierte Pfade ausgewählt werden**<br>
Bei dieser Methode ist die empfohlene Nachricht für eine:n einzelne:n Nutzer:in die Summe der Effekte ihrer spezifischen Aktualität, Häufigkeit und Zugehörigkeitsdauer. Aktualität, Häufigkeit und Zugehörigkeitsdauer werden in Buckets aufgeteilt, wie in der Tabelle **Nutzermerkmale** dargestellt. Der Zeitbereich jedes Buckets wird durch die Daten der Nutzer:innen in jedem einzelnen Canvas bestimmt und variiert von Canvas zu Canvas.

Jeder Bucket kann einen unterschiedlichen Beitrag oder „Impuls" in Richtung jedes Pfads haben. Die Stärke des Impulses für jeden Bucket wird aus den Nutzerantworten im initialen Experiment mittels [logistischer Regression](https://en.wikipedia.org/wiki/Logistic_regression) bestimmt. Die Tabelle fasst die Ergebnisse lediglich zusammen, indem sie anzeigt, mit welchem Pfad Nutzer:innen in jedem Bucket tendenziell interagiert haben. Der tatsächliche personalisierte Pfad einer einzelnen Person hängt von der Summe der Effekte der drei Buckets ab, in denen sie sich befindet – einer für jedes Merkmal.

{% enddetails %}

{% endtab %}
{% tab Personalisierte Pfade %}

Der Tab **Personalisierte Pfade** zeigt die Ergebnisse des finalen Experiments, bei dem die Nutzer:innen in der Verzögerungsgruppe den für sie leistungsstärksten Pfad entlang gesendet wurden.

Die drei Karten auf dieser Seite zeigen Ihren prognostizierten Lift, die Gesamtergebnisse und die prognostizierten Ergebnisse, wenn Sie stattdessen nur den Gewinnerpfad gesendet hätten. Selbst wenn es keinen Lift gibt, was manchmal vorkommen kann, ist das Ergebnis dasselbe wie beim Senden nur des Gewinnerpfads (ein traditioneller A/B-Test).

- **Prognostizierter Lift:** Die Verbesserung Ihres ausgewählten Konversions-Events durch die Verwendung personalisierter Pfade anstelle des Sendens aller Nutzer:innen über den insgesamt leistungsstärksten Pfad.
- **Gesamtergebnisse:** Die Ergebnisse des zweiten Versands basierend auf Ihrem Konversions-Event.
- **Prognostizierte Ergebnisse:** Die prognostizierten Ergebnisse des zweiten Versands basierend auf Ihrer gewählten Optimierungsmetrik, wenn Sie stattdessen nur die Gewinnervariante gesendet hätten.

![Tab „Personalisierte Pfade" für einen Canvas. Die Karten zeigen den prognostizierten Lift, die Gesamt-Conversions (mit personalisierten Pfaden) und die prognostizierten eindeutigen Öffnungen (mit Gewinnerpfad).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Personalisierte Pfade mit Zustellung zur Ortszeit verwenden

Wir empfehlen nicht, die Zustellung zur Ortszeit in Canvases mit personalisierten Pfaden zu verwenden. Dies liegt daran, dass Experiment-Zeitfenster beginnen, wenn die erste Person den Schritt durchläuft. Nutzer:innen in sehr frühen Zeitzonen können den Schritt betreten und den Start des Experiment-Zeitfensters viel früher als erwartet auslösen, was dazu führen kann, dass das Experiment abgeschlossen wird, bevor der Großteil Ihrer Nutzer:innen in typischeren Zeitzonen genügend Zeit hatte, den Canvas zu betreten und zu konvertieren.

Wenn Sie alternativ die Zustellung zur Ortszeit verwenden möchten, nutzen Sie ein Experiment-Zeitfenster von 24–48 oder mehr Stunden. Auf diese Weise betreten Nutzer:innen in frühen Zeitzonen den Canvas und lösen den Start des Experiments aus, aber es bleibt genügend Zeit im Experiment-Zeitfenster. Nutzer:innen in späteren Zeitzonen haben dann noch ausreichend Zeit, den Canvas und den Experiment-Schritt mit personalisierten Pfaden zu betreten und möglicherweise zu konvertieren, bevor das Experiment-Zeitfenster abläuft.