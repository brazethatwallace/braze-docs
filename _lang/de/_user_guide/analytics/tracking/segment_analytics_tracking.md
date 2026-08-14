---
nav_title: Segment Analytics Tracking
article_title: Segment Analytics Tracking
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt das Segment Analytics Tracking und zeigt Ihnen, wie Sie Umsätze und Käufe im Zeitverlauf, Sitzungen im Zeitverlauf und angepasste Events im Zeitverlauf betrachten können."
tool:
  - Segments
  - Reports
---

# Segment Analytics Tracking {#segment-analytics-tracking}

> Wenn das Analytics Tracking für ein Segment aktiviert ist, können Sie Sitzungen, angepasste Events und Umsätze im Zeitverlauf für dieses Segment anzeigen.

Wenn Sie das Analytics Tracking für ein Segment nicht einschalten, können Sie dennoch auf [Realtime-Statistiken]({{site.baseurl}}/user_guide/audience/segments/segment_data#segment-statistics) für dieses Segment zugreifen und die Nutzer:innen mit Campaigns ansprechen. Der einzige Unterschied besteht darin, ob Sie auf die auf dieser Seite erwähnten Analyse-Tools zugreifen können.

## Segment-Analytics aktivieren {#turning-on-segment-analytics}

Aktivieren Sie im Bereich **Segment Details** auf der Seite eines Segments die Option **Analytics Tracking**.

![Analytics-Tracking-Umschalter für ein Segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

In einem Workspace kann das Tracking für bis zu 25 Segments aktiviert werden. Braze empfiehlt, Segments zu tracken, die für die Analyse der Auswirkungen Ihrer Campaigns auf Sitzungen, Umsatz und Käufe wichtig sind.

{% alert note %}
Nach der Aktivierung des Analytics-Trackings kann es eine Weile dauern, bis die Segment-Daten in Ihren Berichten angezeigt werden. Wenn die Daten nicht innerhalb von 24 Stunden angezeigt werden, [kontaktieren Sie den Support]({{site.baseurl}}/braze_support).
{% endalert %}

## Umsatz und Käufe im Zeitverlauf anzeigen {#viewing-revenue-and-purchases-over-time}

Gehen Sie zu **Analytics** > **Revenue Report**, um Daten zu [Umsatz und Käufen im Zeitverlauf für dieses Segment]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) anzuzeigen.

Umsatz- und Kauf-Charts spiegeln Aktivitäten wider, die nach dem Aktivieren des Analytics-Trackings für dieses Segment erfasst wurden. Das Aktivieren des Trackings füllt frühere Käufe nicht rückwirkend in diese Berichte ein. Wenn Sie Segments vergleichen, verwenden Sie nur Zeiträume, in denen das Tracking für jedes ausgewählte Segment aktiviert war.

![Umsatzdaten nach Segment]({% image_buster /assets/img_archive/Revenue.png %})

Um Segment-Daten für einen beliebigen angepassten Zeitraum visuell zu vergleichen, fügen Sie Segments zum Chart hinzu oder entfernen Sie sie. Wählen Sie **By Segment** im **Breakdown**-Dropdown aus und wählen Sie dann Ihre Segments unter **Breakdown values** aus.

Wählen Sie einen beliebigen Segmentnamen in der Chart-Legende aus, um die Sichtbarkeit der Metriken dieses Segments ein- oder auszuschalten.

![Umsatz für mehrere Segments]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessions im Zeitverlauf {#sessions-over-time}

Ebenso finden Sie Daten zu [Sessions im Zeitverlauf für dieses bestimmte Segment]({{site.baseurl}}/user_guide/analytics/dashboards/home) auf der **Home**-Seite.

![Sessiondaten nach Segment]({% image_buster /assets/img_archive/events_over_time2.png %})

## Angepasste Events im Zeitverlauf anzeigen {#view-custom-events-over-time}

Zeigen Sie Daten zu [angepassten Events im Zeitverlauf für Segmente]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics) an, indem Sie zu **Analytics** > **Custom events report** navigieren.

## Verwendung von Query-Builder-Templates {#using-query-builder-templates}

Wenn Analytics-Tracking aktiviert ist, können Sie Query-Builder-Report-Templates verwenden, um Performance-Metriken für Campaigns, Canvas, Varianten und Schritte nach Segments aufzuschlüsseln. Weitere Informationen finden Sie unter [Segment-Daten]({{site.baseurl}}/user_guide/audience/segments/segment_data#viewing-performance-data-by-segment).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was sollte ich überprüfen, wenn das Analytics-Tracking fehlerhaft oder leer erscheint? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

Bestätigen Sie, dass **Analytics Tracking** unter **Segment Details** noch aktiviert ist, dass Sie das Limit pro Workspace (25 Segments mit Tracking) nicht überschritten haben, und warten Sie bis zu 24 Stunden, bis die Daten nach der erstmaligen Aktivierung des Trackings befüllt werden. Falls die Probleme weiterhin bestehen, überprüfen Sie die Segment-Definition und den Berichtszeitraum und [kontaktieren Sie den Support]({{site.baseurl}}/braze_support).