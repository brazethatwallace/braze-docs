---
nav_title: Zufällige Bucket-Nummern
article_title: Zufällige Bucket-Nummern
page_order: 2
page_type: reference
description: "Dieser Artikel behandelt das Konzept der zufälligen Bucket-Nummern und wie Sie damit Varianten und Kontrollgruppen erstellen können."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Zufällige Bucket-Nummern {#random-bucket-numbers}

> Eine zufällige Bucket-Nummer ist ein Nutzerattribut, das verwendet werden kann, um gleichmäßig verteilte Segmente von zufälligen Nutzer:innen zu erstellen.

## Übersicht {#overview}

Wenn ein Kundenprofil in Braze erstellt wird, wird dieser Person automatisch eine zufällige Bucket-Nummer zwischen 0 und 9999 (einschließlich) zugewiesen. Sie können diese Segmente verwenden, um die Effektivität mehrerer Campaigns oder Canvases bei Gruppen von Nutzer:innen im Laufe der Zeit zu testen.

### Verwendung der globalen Kontrollgruppe {#global-control-group-usage}

Zufällige Bucket-Nummern werden in Ihrer globalen Kontrollgruppe verwendet&#8212;einer Gruppe von Nutzer:innen, die keine Campaigns oder Canvases erhalten. Braze wählt zufällig mehrere Bereiche von zufälligen Bucket-Nummern aus und schließt Nutzer:innen aus diesen ausgewählten Buckets ein. Zufällige Bucket-Nummern werden ohne Gewichtung oder Berücksichtigung kürzlich zugewiesener Nummern vergeben.

{% alert note %}
Wenn ein:e Nutzer:in gelöscht und neu erstellt wird, wird eine andere zufällige Bucket-Nummer zugewiesen, da die Person als neue:r Nutzer:in betrachtet wird.
{% endalert %}

Wenn Sie eine globale Kontrollgruppe eingerichtet haben und zufällige Bucket-Nummern für andere Anwendungsfälle nutzen möchten, lesen Sie die Hinweise, auf die [Sie achten sollten]({{site.baseurl}}/user_guide/audience/global_control_group#things-to-watch-for).

### Wann Sie zufällige Bucket-Nummern verwenden sollten {#when-to-use-random-bucket-numbers}

Wenn Sie langfristige Tests zur Wirksamkeit mehrerer Campaigns oder Canvases über einen bestimmten Zeitraum durchführen möchten, können Sie zufällige Bucket-Nummern verwenden, um Ihre Nutzer:innen zu segmentieren.

### Wann Sie etwas anderes verwenden sollten {#when-to-use-something-else}

Wenn Sie Nutzer:innen für Tests innerhalb einer einzelnen Campaign oder eines einzelnen Canvas segmentieren möchten, verwenden Sie [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) für Campaigns. Für Canvases können Sie verschiedene [Varianten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-21-add-a-variant) für Tests auf Journey-Ebene erstellen oder [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) für Tests auf Schritt-Ebene verwenden.

## Segmente mit zufälligen Bucket-Nummern erstellen {#create-segments-using-random-bucket-numbers}

Fügen Sie beim [Erstellen eines Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) den Filter „Random Bucket #“ hinzu. Geben Sie dann eine Nummer oder einen Nummernbereich an, der in Ihr Segment aufgenommen werden soll.

![Ein Segment-Filter für zufällige Bucket-Nummern, die nicht mehr als „3000“ betragen.]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Diese Art von Segmenten kann nützlich sein, wenn Sie einen Test mit drei verschiedenen Varianten und einer Kontrollgruppe durchführen möchten. Betrachten Sie den folgenden Beispielplan für die Erstellung gleich großer Segmente für drei Varianten und eine Kontrollgruppe:

- Bucket-Nummern 0 bis 2499 entsprechen dem Kontrollsegment
- Bucket-Nummern 2500 bis 4999 entsprechen dem Segment, das Variante 1 erhält
- Bucket-Nummern 5000 bis 7499 entsprechen dem Segment, das Variante 2 erhält
- Bucket-Nummern 7500 bis 9999 entsprechen dem Segment, das Variante 3 erhält

Je nachdem, wie viele Segmente Sie benötigen und wie die Verteilung der Nutzer:innen innerhalb jedes Segments aussehen soll, kann Ihr Plan anders aussehen.

Aktivieren Sie für jedes Ihrer Segmente mit zufälligen Bucket-Nummern, einschließlich der Kontrollgruppe, das [Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking). Bei der Bewertung des Erfolgs der Varianten im Vergleich zur Kontrollgruppe können Sie auf der Seite [Angepasste Events]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) einsehen, wie oft jedes Segment bestimmte angepasste Events abgeschlossen hat.

{% alert tip %}
Wenn Sie Segmente mit zufälligen Bucket-Nummern in einem Canvas verwenden, z. B. als Filter in einem [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Schritt, stellen Sie sicher, dass die [Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) Ihres Canvas, Zielgruppenfilter und vorgelagerte Schritte keine Segmente ansprechen, die sich mit einem Ihrer Bucket-Bereiche überschneiden. Andernfalls könnten Nutzer:innen in diesem Bereich unverhältnismäßig oft entfernt werden, bevor sie den Split erreichen, was zu einer ungleichmäßigen Verteilung zwischen den Pfaden führt.
{% endalert %}

### Zufälliger Wiedereintritt der Zielgruppe mit zufälligen Bucket-Nummern {#random-audience-re-entry-using-random-bucket-numbers}

Der zufällige Wiedereintritt der Zielgruppe kann für [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/faq#what-is-the-difference-between-ab-testing-and-multivariate-testing) oder das Targeting bestimmter Nutzergruppen in Ihren Campaigns nützlich sein. Um einen zufälligen Wiedereintritt der Zielgruppe mit zufälligen Bucket-Nummern durchzuführen, gehen Sie wie folgt vor:

1. [Erstellen Sie Ihr Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Definieren Sie die zufälligen Buckets. Verwenden Sie in Ihrer Campaign oder Ihrem Canvas den Filter für zufällige Buckets, um Ihre Zielgruppe in verschiedene Gruppen aufzuteilen. Sie können beispielsweise genau zwei zufällige Buckets angeben, um Ihre Zielgruppe aufzuteilen (50 % der Nutzer:innen pro Bucket).
3. Geben Sie im Abschnitt **Target Audiences** Ihrer Campaign oder Ihres Canvas die Einstellungen für zufällige Buckets an. So kann Braze Nutzer:innen automatisch den entsprechenden Buckets basierend auf den definierten Prozentsätzen zuweisen.
4. Richten Sie eine Logik ein, die es Nutzer:innen ermöglicht, erneut in das Segment einzutreten. Sie können beispielsweise festlegen, dass Nutzer:innen erneut in das Segment eintreten, wenn sie 15 Tage lang keine App genutzt haben.
5. Starten Sie Ihre Campaign und überwachen Sie die Performance jedes Buckets. Sie können Metriken wie Engagement-Raten und Konversionsraten analysieren, um festzustellen, wie effektiv der zufällige Wiedereintritt der Zielgruppe für Ihren Anwendungsfall ist.