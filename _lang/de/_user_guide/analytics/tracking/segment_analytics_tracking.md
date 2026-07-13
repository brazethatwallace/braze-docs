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

## Segment Analytics einschalten {#turning-on-segment-analytics}

Schalten Sie im Abschnitt **Segment Details** auf der Seite eines Segments **Analytics Tracking** ein.

![Analytics-Tracking-Umschalter für ein Segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

In einer App kann das Tracking für bis zu 25 Segmente aktiviert werden. Braze empfiehlt das Tracking von Segmenten, die für Sie wichtig sind, um die Auswirkungen Ihrer Campaigns auf Sitzungen, Umsätze und Käufe zu analysieren.

{% alert note %}
Nach der Aktivierung des Analytics Trackings kann es zu einer Verzögerung kommen, bis die Segment-Daten befüllt sind. Wenn die Daten innerhalb von 24 Stunden nicht angezeigt werden, [kontaktieren Sie den Support]({{site.baseurl}}/braze_support).
{% endalert %}

## Anzeigen von Umsätzen und Käufen im Zeitverlauf {#viewing-revenue-and-purchases-over-time}

Gehen Sie zu **Analytics** > **Umsatzbericht**, um Daten zu [Umsatz und Käufen im Zeitverlauf für dieses Segment]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) anzuzeigen.

Umsatz- und Kauf-Charts spiegeln die Aktivitäten wider, die nach der Aktivierung des Analytics Trackings für dieses Segment erfasst wurden. Das Einschalten des Trackings füllt frühere Käufe nicht rückwirkend in diese Berichte ein. Verwenden Sie beim Vergleich von Segmenten nur Zeiträume, in denen das Tracking für jedes ausgewählte Segment aktiviert war.

![Umsatzdaten nach Segment]({% image_buster /assets/img_archive/Revenue.png %})

Um die Segment-Daten für einen beliebigen angepassten Zeitraum visuell zu vergleichen, fügen Sie dem Diagramm Segmente hinzu oder entfernen Sie sie. Wählen Sie in der Dropdown-Liste **Aufschlüsselung** die Option **By Segment** und wählen Sie dann Ihre Segmente unter **Breakdown values** aus.

Wählen Sie einen beliebigen Segmentnamen oberhalb des Diagramms aus, um die Sichtbarkeit der Metriken für dieses Segment ein- oder auszuschalten.

![Umsätze für mehrere Segmente]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sitzungen im Zeitverlauf {#sessions-over-time}

Auf ähnliche Weise finden Sie auf der **Home**-Seite Daten über [Sitzungen im Zeitverlauf für dieses bestimmte Segment]({{site.baseurl}}/user_guide/analytics/dashboards/home#exporting-app-usage-data).

![Sitzungsdaten nach Segment]({% image_buster /assets/img_archive/events_over_time2.png %})

## Angepasste Events im Zeitverlauf anzeigen {#view-custom-events-over-time}

Sehen Sie sich Daten über [angepasste Events im Zeitverlauf für Segmente]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics) an, indem Sie zu **Analytics** > **Bericht zu angepassten Events** gehen.

## Verwendung von Abfrage-Builder-Templates {#using-query-builder-templates}

Wenn das Analytics Tracking aktiviert ist, können Sie mit den Berichts-Templates des Abfrage-Builders die Performance-Metriken für Campaigns, Canvas, Varianten und Schritte nach Segmenten aufschlüsseln. Mehr erfahren Sie unter [Segment-Daten]({{site.baseurl}}/user_guide/audience/segments/segment_data#performance-data-by-segment).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was sollte ich überprüfen, wenn das Analytics Tracking falsch aussieht oder leer ist? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

Vergewissern Sie sich, dass **Analytics Tracking** unter **Segment Details** noch aktiviert ist, dass Sie das Limit pro App (25 Segmente mit Tracking) nicht überschritten haben, und warten Sie bis zu 24 Stunden, bis die Daten nach der erstmaligen Aktivierung des Trackings befüllt sind. Wenn die Probleme weiterhin bestehen, überprüfen Sie die Segment-Definition und den Berichtszeitraum und [kontaktieren Sie den Support]({{site.baseurl}}/braze_support).