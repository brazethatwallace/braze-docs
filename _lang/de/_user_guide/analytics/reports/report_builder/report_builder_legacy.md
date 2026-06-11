---
nav_title: Berichts-Builder (Legacy)
article_title: Berichts-Builder (Legacy)
alias: /report_builder_legacy/
page_order: 1
page_type: reference
description: "Diese Seite beschreibt, wie Sie mit dem Legacy-Berichts-Builder einen Bericht erstellen, einschließlich Campaign- und Canvas-Vergleichsberichten sowie der Erstellung von Berichten und Charts."
tool:
  - Reports

---

# Berichts-Builder (Legacy) {#report-builder-legacy}

> Mit dem Berichts-Builder können Sie die Ergebnisse mehrerer Campaigns oder Canvases in einer einzigen Ansicht vergleichen, sodass Sie leicht feststellen können, welche Engagement-Strategien Ihre wichtigsten Metriken am stärksten beeinflusst haben. Sowohl für Campaigns als auch für Canvases können Sie Ihre Daten exportieren und Ihren Bericht speichern, um ihn in Zukunft erneut aufzurufen.<br><br>Eine beschreibende Liste der Metriken, die Sie in Ihren Berichten finden, finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

![Beispiel für einen Campaign-Vergleich]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Verwenden Sie diesen Bericht, um wichtige Engagement-Fragen zu beantworten, zum Beispiel:

- Welche Campaigns oder Canvases hatten die beste Performance für einen bestimmten Tag oder Kanal?
- Welche Varianten von multivarianten Campaigns hatten den größten Uplift gegenüber der Kontrollgruppe?
- Welche saisonale Aktions-Campaign führte zu einer höheren Kaufrate – der Sommerschlussverkauf, der Herbstverkauf oder der Winterverkauf?
- Welche Push-Benachrichtigungen innerhalb dieses Canvas hatten die höchsten Öffnungsraten?
- Welche Schritte in dieser Gruppe von Canvases hatten die meisten Conversions?
- Hat Version 1 einer Willkommens-E-Mail oder Version 2 einer Willkommens-E-Mail zu höherem Engagement und mehr Conversions geführt? Haben die Änderungen gewirkt?
- Wie wirken sich verschiedene Zustellmethoden (zum Beispiel 3 geplante Push-Benachrichtigungen, 3 aktionsbasierte Push-Benachrichtigungen und 3 API-getriggerte Push-Benachrichtigungen) auf Ihre Öffnungsraten, Konversionsraten oder Kaufraten aus?
- Haben die laufenden Verbesserungen an Nachrichten für inaktive Nutzer:innen Ihre KPIs im Laufe der Zeit positiv beeinflusst?

{% alert tip %}
Versuchen Sie, dieselben Konversions-Events für Conversion A, B usw. über alle Campaigns und Canvases hinweg zu verwenden, die Sie vergleichen möchten, damit Sie diese Conversions in Ihren Berichts-Builder-Berichten aufeinander abstimmen können.
{% endalert %}

## Einen Bericht erstellen {#running-a-report}

### 1. Schritt: Neuen Bericht erstellen {#step-1-create-a-new-report}

Navigieren Sie im Dashboard zu **Analytics** > **Berichts-Builder**.

Wählen Sie **Neuen Bericht erstellen** und wählen Sie entweder einen Campaign-Vergleichsbericht oder einen Canvas-Vergleichsbericht.

Wenn Sie sich für einen Bericht über Campaigns entscheiden, können Sie zwischen einem **manuellen** oder einem **automatisierten** Bericht wählen. Berichte können entweder Campaigns oder Canvases enthalten, aber nicht beides zusammen. Alle Campaigns und Canvases, deren letzte Nachrichten innerhalb der letzten 12 Monate gesendet wurden, kommen für einen Bericht infrage.

![Campaign-Dashboard]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

Im Folgenden finden Sie die Unterschiede zwischen diesen beiden Optionen:

| **Aktion** | **Manuell** | **Automatisiert** |
| ---- | ---------- | ------------- |
| **Bericht erstellen** | Sie können Ihre Campaign-Liste mithilfe von Filtern eingrenzen und dann bestimmte Campaigns auswählen. | Sie erstellen Ihren Bericht, indem Sie die Filteroptionen verwenden, um Ihre Campaign-Liste einzugrenzen. |
| **Bericht speichern und anzeigen** | Sie können Ihren Bericht speichern. Wenn Sie ihn das nächste Mal aufrufen, sehen Sie dieselben Campaigns, die Sie zuvor hinzugefügt haben, da diese Campaigns weiterhin unter Ihren „Zuletzt gesendet“-Filter fallen. | Sie können Ihren Bericht speichern. Wenn Sie ihn das nächste Mal aufrufen, wird der Bericht automatisch aktualisiert und enthält alle Campaigns, die derzeit Ihren Filtern entsprechen. |
| **Bericht bearbeiten** | Sie können **Bericht bearbeiten** auswählen, um Campaigns zu Ihrem Bericht hinzuzufügen oder daraus zu entfernen. | Sie können Ihren Bericht bearbeiten, indem Sie Ihre Filterkriterien anpassen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Neuen Bericht erstellen" }

{% alert note %}
Sowohl **manuelle** als auch **automatisierte** Berichte können maximal 250 Campaigns in einem Bericht enthalten.
{% endalert %}

Canvas-Berichte funktionieren ähnlich wie ein manueller Campaign-Bericht, da Canvas-Auswahlen und Berichtsaktualisierungen ebenfalls manuell vorgenommen werden müssen. Sie können maximal fünf Canvases in einem Bericht einschließen.

### 2. Schritt: Metriken auswählen {#step-2-choose-your-metrics}

Nachdem Sie Ihren Bericht erstellt haben, finden Sie eine leere Tabelle mit Campaigns in jeder Zeile. Die Tabelle wird befüllt, nachdem Sie **Edit Columns** auswählen und die Metriken auswählen, die Sie hinzufügen möchten.

![Campaign-Optionen]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Ihre Tabelle wird mit den von Ihnen gewählten Metriken befüllt. Definitionen dieser Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary/). Einige Metriken sind nur für Campaign-Vergleichsberichte verfügbar.

Sie können auch Berechnungen für den **Durchschnitt** jeder Rate oder numerischen Metrik und die **Summe** für jede numerische Metrik umschalten.

### 3. Schritt: Zeitraum auswählen {#step-3-choose-a-time-period}

Sie können einen bestimmten Zeitraum auswählen, für den Sie die Daten Ihres Berichts anzeigen möchten. Wenn eine bestimmte Campaign, ein Canvas, eine Canvas-Variante oder eine Canvas-Komponente keine Daten für den ausgewählten Zeitraum hat, sind die Ergebnisse für diese Zeile leer.

![Numerische Campaign-Metrik]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### 4. Schritt: Bericht benennen und speichern {#step-4-name-and-save-your-report}

Benennen Sie Ihren Bericht, bevor Sie ihn speichern. Wenn ein Bericht ohne Namen gespeichert wird, wendet Braze den Standardnamen „Campaign Comparison Report“ an.

![Campaign-Hinweis]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Wenn Sie bereit sind, wählen Sie **Save**. Gespeicherte Berichte können zu einem späteren Zeitpunkt auf der Seite **Berichts-Builder** aufgerufen werden.

## Campaign-Vergleichsbericht mit multivarianten Campaigns {#campaign-comparison-report-with-multivariate-campaigns}

Für alle multivarianten Campaigns können Sie diese Metriken aufgeschlüsselt nach Ihren Varianten und der Kontrollgruppe anzeigen, indem Sie auf den Pfeil neben dem Campaign-Namen klicken. Die Zeilen mit Ihren Varianten enthalten die Performance-Ergebnisse für diese Variante, und die Zeile mit Ihrer Kontrollgruppe enthält nur die Ergebnisse für Ihre Konversions-Events.

![Campaign-Hinweis]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Die Metriken in der Zeile für Ihre gesamte Campaign spiegeln die Performance ihrer Varianten wider, enthalten jedoch nicht die Performance der Kontrollgruppe. Zum Beispiel ist das primäre Konversions-Event A für Ihre gesamte Campaign die Summe des primären Konversions-Events A für Ihre Varianten und enthält nicht das primäre Konversions-Event A für Ihre Kontrollgruppe.

{% alert important %}
Wenn Sie eine Variante aus einer multivarianten Campaign löschen, stehen die Daten dieser Variante nicht für die Verwendung in einem zukünftigen Bericht zur Verfügung.
{% endalert %}

## Aufschlüsselung des Canvas-Vergleichsberichts {#canvas-comparison-report-breakdown}

Innerhalb eines Canvas-Berichts können Sie Ihre Canvases aufgeschlüsselt nach Variante, Schritten oder Nachricht anzeigen.

### Variante {#variant}

Wenn Sie **Aufschlüsselung nach Variante** auswählen, können Sie die übergeordneten Statistiken für Ihre gesamten Canvases sowie Statistiken für jede Variante anzeigen, die durch Klicken auf den Pfeil neben dem Canvas-Namen erweitert werden können.

![Varianten]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Schritte {#steps}

Wenn Sie **Aufschlüsselung nach Schritten** auswählen, können Sie Metriken auf Schrittebene anzeigen, wobei jede Zeile des Berichts die Zeile eines Schritts enthält.

![Schritte]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Nachricht {#message}

Ähnlich wie bei einer Aufschlüsselung auf Schrittebene zeigt die Auswahl von **Aufschlüsselung nach Nachricht** die Namen der Schritte in jeder Zeile an. Innerhalb von **Edit Columns** haben Sie jedoch Zugriff auf Metriken auf Nachrichtenebene, wie z. B. kanalspezifische Statistiken wie E-Mail-Klicks und Push-Öffnungen.

![Bericht]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Beachten Sie, dass Sie im Braze-Dashboard eine Vorschau der ersten 50 Zeilen Ihres Canvas-Berichts anzeigen können. Den vollständigen Bericht können Sie aufrufen, wenn Sie eine CSV-Datei exportieren.

## Auf gespeicherte Berichte zugreifen {#accessing-saved-reports}

Wenn Sie auf einen gespeicherten **manuellen Bericht** zugreifen, sehen Sie dieselben Campaigns, die Sie zuvor hinzugefügt haben, da diese Campaigns weiterhin unter Ihren „Zuletzt gesendet“-Filter fallen.

Wenn Sie auf einen gespeicherten **automatisierten Bericht** zugreifen, wird der Bericht automatisch aktualisiert und enthält alle Campaigns, die derzeit Ihren Filtern entsprechen. Wenn Ihr Bericht beispielsweise Campaigns mit dem Tag „Aktion“ filtert, sehen Sie bei jedem Aufruf dieses Berichts alle Campaigns mit dem Tag „Aktion“, auch wenn diese Campaigns erstellt wurden, nachdem Sie diesen Bericht angelegt haben.

## Berichte bearbeiten {#editing-reports}

In einem **manuellen Bericht** können Sie einen Bericht bearbeiten, indem Sie **Edit** auswählen. Von dort aus können Sie Campaigns auswählen oder abwählen, die in Ihrem Bericht enthalten sein sollen.

In einem **automatisierten Bericht** schalten Sie Ihre Filter um, um die Ergebnisse in Ihrem Bericht einzugrenzen.

## Berichte exportieren {#exporting-reports}

Sie können auch **Export** auswählen, um Ihren Bericht als CSV-Datei herunterzuladen.

Wenn Ihr Bericht multivariante Campaigns enthält, umfasst Ihr Export zwei CSV-Dateien:

- Eine Datei, die nur die übergeordneten Metriken für jede Campaign enthält
- Eine Datei, die Metriken auf Variantenebene enthält

Die Datei mit den Varianten-Metriken hat `variant_` am Anfang ihres Namens. Beim ersten Export eines automatisierten Berichts erhalten Sie ein Pop-up, in dem Sie um Erlaubnis zum Herunterladen mehrerer Dateien gebeten werden – klicken Sie auf **Allow**.

![Campaign-Download]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Canvas-Vergleichsberichte exportieren {#exporting-canvas-comparison-reports}

Ihr CSV-Export spiegelt die Aufschlüsselungsansicht wider, in der Sie sich befanden, als Sie **Export** ausgewählt haben. Wenn Sie sich beispielsweise in der Aufschlüsselungsansicht auf Schrittebene befanden, enthält Ihr Export Daten zu Ihren Schrittmetriken. Um Daten aus einer anderen Aufschlüsselung zu exportieren, müssen Sie zuerst zu dieser Aufschlüsselung navigieren und dort **Export** auswählen.

Wenn Sie einen Canvas-Bericht mit Varianten-Aufschlüsselung herunterladen, erhalten Sie zwei CSV-Dateien:

- Eine Datei, die nur die übergeordneten Metriken für jeden Canvas enthält
- Eine Datei, die Metriken auf Variantenebene enthält

## Charts erstellen {#building-charts}

Verwenden Sie Charts, um eine ausgewählte Metrik in Ihrem Bericht zu visualisieren. Charts sind für Berichte verfügbar, die Campaigns enthalten und mindestens eine Metrik in ihren Spalten haben.

![Campaign-Performance-Chart mit ausgewählter Metrik „Message Sent“]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Standardmäßig zeigt das Chart in jedem Bericht die Metrik in der ersten Spalte des Berichts an. Um eine andere Metrik für die Darstellung auszuwählen, wählen Sie Ihre Metrik aus dem Dropdown-Menü. Jede Metrik in Ihrer Berichtstabelle kann im Chart angezeigt werden.

Sie können maximal drei Metriken darstellen. Die Einheiten für alle Metriken müssen identisch sein – wenn Sie beispielsweise im ersten Dropdown eine Rate auswählen, stehen im zweiten Dropdown nur Raten zur Auswahl.

Wenn Ihr Chart nur eine Metrik enthält, werden bis zu 30 Campaigns in absteigender Reihenfolge basierend auf der ausgewählten Metrik angezeigt. Wenn die Metrik Ihres Charts beispielsweise E-Mail-Klicks ist, zeigt Ihr Chart die 30 E-Mail-Campaigns mit den meisten Klicks an, sortiert von den meisten zu den wenigsten Klicks. Wenn Ihr Bericht mehr als 30 Campaigns enthält, werden nur die Top 30 im Chart angezeigt. Wenn Sie mehr als eine Metrik auswählen, zeigt Ihr Chart nur die Top 5 Campaigns basierend auf der ersten ausgewählten Metrik an.

Charts werden derzeit nicht gespeichert, wenn Sie Ihren Bericht speichern.