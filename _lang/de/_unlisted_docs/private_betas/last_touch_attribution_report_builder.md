---
nav_title: "Last-Touch-Attribution"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# Last-Touch-Attribution-Metriken {#last-touch-attribution-metrics}

> Fügen Sie Last-Touch-Attribution-Metriken zu Ihren Berichten im Berichts-Builder hinzu.

{% alert note %}
Last-Touch-Attribution-Metriken befinden sich im Early Access. Wenn Sie an der Teilnahme am Early Access interessiert sind, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

Last-Touch-Attribution (LTA) ist ein Konversions-Attributionsmodell, das die vollständige Zuordnung einer Konversion der letzten Nachricht zuschreibt, mit der ein:e Nutzer:in vor der Konversion interagiert hat. Im Gegensatz zu Konversions-Fenstern auf Campaign-Ebene verwendet LTA branchenübliche Attributionsfenster für jeden Kanal:

| Kanal | Attributionsfenster |
| --- | --- |
| E-Mail | 30 Tage |
| SMS | 7 Tage |
| WhatsApp | 7 Tage |
| Push | 7 Tage |
| In-App-Nachricht | 3 Tage |
| Content Cards | 3 Tage |
| Webhook | von diesem Modell ausgeschlossen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn eine Konversion außerhalb des Attributionsfensters eines Kanals stattfindet, wird sie in diesem Modell nicht gezählt.
{% endalert %}

## Vorteile {#benefits}

Last-Touch-Attribution bietet wesentliche Vorteile gegenüber dem Standard-Conversion-Tracking:

* Sie ermöglicht es Ihnen, Konversionen bestimmten Touchpoints zuzuordnen, sodass Sie nachvollziehen können, welche Kanäle (nicht nur Campaigns oder Canvases) Ergebnisse erzielen.
* Die Zuordnung erfolgt ausschließlich an die zuletzt berührte Nachricht, sodass jede Konversion nur einmal gezählt wird. Dadurch werden überlappende Konversionen über Campaigns oder Canvases mit gemeinsamen Konversions-Events und Zielgruppen hinweg eliminiert.

## Last-Touch-Attribution-Metriken zu Ihrem Bericht hinzufügen {#add-last-touch-attribution-metrics-to-your-report}

1. Gehen Sie zum **Berichts-Builder** unter **Analytics**.
2. Wählen Sie **Bericht erstellen** > **Benutzerdefinierten Bericht erstellen**.
3. Wählen Sie im Dropdown **Zeilen** aus, worüber Sie einen Bericht erstellen möchten.
4. (Optional) Wählen Sie **Drilldown hinzufügen** und dann einen Bereich, um tiefer in Ihre Berichterstattung einzutauchen.
5. Wählen Sie unter **Spalten** die Option **Metriken anpassen**.
6. Wählen Sie unter **Conversions** die Option **Last Touch Attribution** und dann **Alle auswählen**.

{% alert note %}
Umsatz- und Kauf-Metriken sind nicht verfügbar.
{% endalert %}

![Das Panel „Metriken anpassen“ mit Last-Touch-Attribution-Metriken.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. Folgen Sie den Schritten 7–9 auf der Seite [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder).

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="last-touch attribution metrics in Report Builder" %}
{% endalert %}