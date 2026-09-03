---
nav_title: Segment-Reporting
article_title: Segment-Reporting im Berichts-Builder
permalink: /segment_reporting_report_builder/
description: "Dieser Referenzartikel behandelt Segment als Berichtsdimension im Berichts-Builder, einschließlich der Berichterstattung über Segments, der Aufschlüsselung nach Segment und der unterstützten Kombinationen."
hidden: true
noindex: true
page_type: reference
---

# Segment-Reporting im Berichts-Builder {#segment-reporting-in-report-builder}

> Dieser Artikel erläutert, wie Sie Segments als Berichtsdimension im Berichts-Builder verwenden, einschließlich der Berichterstattung über Segments, der Aufschlüsselung nach Segment und der unterstützten Kombinationen.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Segment reporting' contact='customer success manager' %}

Der Berichts-Builder unterstützt **Segments** in Zeilen und als Drilldown-Option, sodass Sie sehen können, wie Ihre Segmente performen, und die Campaign- oder Canvas-Performance nach Segment-Zugehörigkeit aufschlüsseln können. Wenn **Segments** nicht in Ihren **Zeilen**- oder **Drilldown**-Dropdowns erscheint, wurde dieses Feature für Ihr Konto noch nicht aktiviert.

Sie können Fragen beantworten wie:

- Wie performt ein bestimmtes Segment im Zeitverlauf?
- Welche Campaigns und Canvases zielen auf ein bestimmtes Segment ab, und wie hat jede/jedes performt?
- Wie unterscheidet sich das Engagement über Segmente hinweg für eine einzelne Campaign oder ein einzelnes Canvas?

{% alert note %}
Segment-Reporting ist nur für Segmente mit aktiviertem [Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) verfügbar. Um **Segments** im **Zeilen**-Dropdown auszuwählen, benötigen Sie die Workspace-Berechtigung [„Dashboard-Berichte anzeigen“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Über Segments berichten {#report-on-segments}

Um direkt über Segments zu berichten:

1. Gehen Sie zu **Analytics** > **Berichts-Builder (Neu)**.
2. Klicken Sie auf **Neuen Bericht erstellen**.
3. Wählen Sie im **Zeilen**-Dropdown **Segments** aus.
4. (Optional) Wählen Sie **Drilldown hinzufügen**, um die Segment-Daten weiter aufzuschlüsseln:
   - **Campaigns und Canvases:** Sehen Sie, welche Campaigns und Canvases auf das Segment abzielen und wie jede/jedes performt hat.
   - **Datum:** Sehen Sie, wie sich die Größe oder Performance eines Segments im Zeitverlauf entwickelt. Kombinieren Sie dies mit einem Liniendiagramm, um den Trend zu visualisieren.
5. Öffnen Sie unter **Berichtsinhalt** das **Segments**-Dropdown und wählen Sie Segmente aus, die Sie Ihrem Bericht hinzufügen möchten.
6. Wählen Sie Metriken unter **Spalten** > **Metriken anpassen** aus und legen Sie dann Ihren Datumsbereich unter **Berichtsinhalt** fest.
7. Wenn Sie einen **Campaigns und Canvases**-Drilldown hinzugefügt haben, fügen Sie die Campaigns und Canvases hinzu, die im Bericht enthalten sein sollen.
8. Klicken Sie auf **Speichern und ausführen**.

Den vollständigen Berichts-Builder-Workflow finden Sie unter [Einen Bericht erstellen]({{site.baseurl}}/user_guide/analytics/reports/report_builder#creating-a-report).

## Nach Segment aufschlüsseln {#drill-down-by-segment}

Um Campaign-, Canvas- oder Kanal-Berichte nach Segment aufzuschlüsseln:

1. Wählen Sie im **Zeilen**-Dropdown **Campaigns**, **Canvases** oder **Campaigns und Canvases** aus.
2. Wählen Sie **Drilldown hinzufügen** und dann **Segment**.
3. Öffnen Sie unter **Berichtsinhalt** das **Segments**-Dropdown und wählen Sie Segmente aus, die Sie Ihrem Bericht hinzufügen möchten.
4. Wählen Sie Metriken unter **Spalten** > **Metriken anpassen** aus und legen Sie dann Ihren Datumsbereich unter **Berichtsinhalt** fest.
5. Fügen Sie die Campaigns oder Canvases hinzu, die im Bericht enthalten sein sollen.
6. Klicken Sie auf **Speichern und ausführen**, um die Performance aufgeschlüsselt nach jedem Segment zu sehen, auf das Ihre Campaigns oder Canvases abzielen.

Dies ist besonders nützlich für Workspaces, die dieselbe Campaign oder dasselbe Canvas an mehrere Segmente senden. Sie können sehen, wie jedes Segment reagiert hat, ohne manuell Segment-Zugehörigkeit und Campaign-Performance abzugleichen.

## Unterstützte Kombinationen {#supported-combinations}

Die folgenden **Zeilen**- und **Drilldown**-Kombinationen werden für das Segment-Reporting unterstützt:

| Zeilen | Drilldown |
| ----- | ----- |
| Segment | Campaigns und Canvases |
| Segment | Datum |
| Campaign | Segment |
| Campaign | Variante |
| Canvas | Segment |
| Campaigns und Canvases | Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Zeilen- und Drilldown-Kombinationen"}

{% alert note %}
Der Berichts-Builder unterstützt jeweils einen Drilldown. Wenn Sie **Campaigns** im **Zeilen**-Dropdown auswählen, können Sie nach **Variante** oder **Segment** aufschlüsseln, aber nicht beides im selben Bericht.
{% endalert %}

## Verfügbarkeit von Metriken {#metrics-availability}

Nicht alle Metriken des Berichts-Builders sind verfügbar, wenn Sie über Segmente berichten. Welche Metriken Sie auswählen können, hängt auch davon ab, ob **Segments** in **Zeilen** oder **Drilldown** steht und ob der Bericht eine Campaign- oder Canvas-Dimension enthält.

| Metrik | Verfügbarkeit |
| ----- | ----- |
| Kanal- und allgemeine Messaging-Metriken | Verfügbar für unterstützte Zeilen- und Drilldown-Kombinationen. |
| Konversionsanzahlen (Konversionen A–D) und Konversions-Event-Namen | Verfügbar, wenn Segment- und Campaign- oder Canvas-Dimensionen zusammen erscheinen. Verwenden Sie **Segments** in Zeilen mit einem **Campaigns und Canvases**-Drilldown; oder verwenden Sie **Campaigns**, **Canvases** oder **Campaigns und Canvases** in Zeilen mit einem **Segment**-Drilldown. |
| Umsatz und Konversionsrate | Nicht verfügbar für Berichte mit Segment-Dimension. |
| Segment-Kaufumsatz und -anzahl | Nur verfügbar, wenn **Segments** in Zeilen steht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbarkeit von Segment-Reporting-Metriken"}

Weitere Informationen darüber, wie Ihre Zeilen- und Drilldown-Auswahl die Metriken beeinflusst, finden Sie unter [Verfügbarkeit von Metriken]({{site.baseurl}}/user_guide/analytics/reports/report_builder#metrics-availability) im Berichts-Builder.