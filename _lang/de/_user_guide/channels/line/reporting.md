---
nav_title: Reporting
article_title: LINE-Reporting
page_order: 21
description: "Dieser Referenzartikel behandelt die LINE-Metriken in Braze sowie deren Anzeige in Ihren LINE-Campaigns."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# LINE-Reporting {#line-reporting}

> Nach dem Start Ihrer Campaign oder Ihres Canvas können Sie wichtige Metriken auf der Seite mit den Campaign-Details oder in den Canvas-Analytics einsehen. Dieser Artikel beschreibt, wo Sie diese Metriken finden und was sie bedeuten.

{% alert tip %}
Sie suchen nach Definitionen für die Begriffe und Metriken in Ihrem Bericht? Weitere Informationen finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).
{% endalert %}

## Campaign-Analytics {#campaign-analytics}

Im Tab **Campaign Analytics** können Sie Ihre Berichte in einer Reihe von Panels einsehen. Je nach Konfiguration sehen Sie möglicherweise mehr oder weniger als die in den folgenden Abschnitten aufgeführten Panels, aber jedes hat seinen Zweck.

{% alert note %}
Öffnungs- und klickbezogene Statistiken für LINE werden nur berechnet, wenn mehr als 20 Nutzer:innen das Ereignis an einem bestimmten Tag ausführen.
{% endalert %}

### Campaign-Details {#campaign-details}

Das Panel **Campaign Details** zeigt eine allgemeine Übersicht über die Performance Ihrer LINE-Nachrichten.

Überprüfen Sie dieses Panel, um allgemeine Metriken wie die Anzahl der gesendeten Nachrichten an die Empfänger:innen, die primäre Konversionsrate und den gesamten durch diese Nachricht generierten Umsatz einzusehen. Sie können auf dieser Seite auch die Einstellungen für Zustellung, Zielgruppe und Konversion überprüfen.

#### Kontrollgruppen {#control-groups}

Um die Wirkung einer einzelnen LINE-Nachricht zu messen, können Sie eine [Kontrollgruppe]({{site.baseurl}}/user_guide/messaging/ab_testing) zu einem A/B-Test hinzufügen. Das übergeordnete Panel **Campaign Details** enthält keine Metriken der Kontrollgruppen-Variante.

### LINE-Performance {#line-performance}

Das Panel **LINE Performance** zeigt, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Panel variieren je nach gewähltem Messaging-Kanal und ob Sie einen multivariaten Test durchführen. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal anzuzeigen.

![Das Panel „LINE Performance“ zeigt Metriken für zwei Varianten.]({% image_buster /assets/img/line/line_performance.png %})

Wenn Sie die Ansicht vereinfachen möchten, wählen Sie **+ Add/Remove Columns** und entfernen Sie die gewünschten Metriken. Standardmäßig werden alle Metriken angezeigt.

#### LINE-Metriken {#line-metrics}

Hier sind einige wichtige LINE-Metriken, die Sie in Ihren Analytics sehen können. Die Definitionen aller in Braze verwendeten LINE-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

| Begriff | Definition |
| --- | --- |
| Sendungen | Die Gesamtzahl der Sendungen, die erfolgreich zwischen Braze und LINE übermittelt wurden. Dies bedeutet nicht, dass die Nachricht von den Nutzer:innen empfangen wurde. |
| Eindeutige Öffnungen | Die Gesamtzahl der gesendeten LINE-Nachrichten, die von Nutzer:innen geöffnet wurden, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. |
| Gesamtöffnungen | Die Gesamtzahl, wie oft die gesendeten LINE-Nachrichten von Nutzer:innen geöffnet wurden, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. |
| Eindeutige Klicks | Die Gesamtzahl der gesendeten LINE-Nachrichten, die von Nutzer:innen angeklickt wurden, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. |
| Gesamtklicks | Die Gesamtzahl, wie oft die gesendeten LINE-Nachrichten von Nutzer:innen angeklickt wurden, nachdem ein Mindestschwellenwert von 20 Nachrichten pro Tag erreicht wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE-Metriken" }

### Historische Performance {#historical-performance}

Das Panel **Historical Performance** ermöglicht es Ihnen, die Metriken aus dem Panel **Message Performance** als Diagramm im Zeitverlauf anzuzeigen. Verwenden Sie die Filter oben im Panel, um die angezeigten Statistiken und Kanäle im Diagramm zu ändern. Der Zeitraum dieses Diagramms entspricht immer dem oben auf der Seite angegebenen Zeitraum.

Für eine tageweise Aufschlüsselung wählen Sie das <i class="fas fa-bars"></i> Hamburger-Menü und dann **Download CSV**, um einen CSV-Export des Berichts zu erhalten.

### Details zu Konversions-Events {#conversion-event-details}

Das Panel **Conversion Event Details** zeigt Ihnen die Performance Ihrer Konversions-Events für Ihre Campaign. Weitere Informationen finden Sie unter [Konversions-Events]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation).

### Conversion-Korrelation {#conversion-correlation}

Das Panel **Conversion Correlation** gibt Ihnen Einblicke, welche Nutzerattribute und -verhaltensweisen die von Ihnen für Campaigns festgelegten Ergebnisse positiv oder negativ beeinflussen. Weitere Informationen finden Sie unter [Conversion-Korrelation]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation).