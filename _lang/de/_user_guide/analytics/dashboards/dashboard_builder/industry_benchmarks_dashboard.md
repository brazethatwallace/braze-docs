---
nav_title: Industry-Benchmarks-Dashboard
article_title: Industry-Benchmarks-Dashboard
alias: "/industry_benchmarks_dashboard/"
page_order: 3
description: "Dieser Artikel bietet eine Übersicht über das Industry-Benchmarks-Dashboard."
hidden: true
noidex: true
---

# Industry-Benchmarks-Dashboard {#industry-benchmarks-dashboard}

> Das **Industry-Benchmarks**-Dashboard vergleicht die Engagement-Performance Ihres Workspace mit aggregierten, datenschutzkonformen Benchmarks von vergleichbaren Unternehmen in jeder Branche.

Verwenden Sie das **Industry-Benchmarks**-Dashboard, um Ihre E-Mail-, Push-, Content-Card- und SMS-Performance mit Branchenvergleichswerten zu vergleichen und Kanäle und Regionen zu identifizieren, in denen Optimierungspotenzial besteht.

Um das **Industry-Benchmarks**-Dashboard aufzurufen, gehen Sie zu **Analytics** > **Dashboard Builder** und wählen Sie **Industry Benchmarks** aus. Wenn das Dashboard keine Daten enthält, wählen Sie **Run Dashboard** aus, um die neuesten Ergebnisse zu generieren. Verwenden Sie die Filter oben im Dashboard, um die Ergebnisse nach Branchenvertikale oder Zeitraum einzugrenzen.

{% alert note %}
Das **Industry-Benchmarks**-Dashboard befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie an der Teilnahme am Early Access interessiert sind.
{% endalert %}

## Über das Dashboard {#about-the-dashboard}

Das Dashboard ist in vier Kanalabschnitte unterteilt: **E-Mail**, **Push-Benachrichtigung**, **Content Card** und **SMS**:

| Abschnitt | Beschreibung |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| KPI-Karten | Zeigen die Rate Ihres Workspace für jede Schlüsselmetrik zusammen mit dem Delta im Vergleich zur Branchenrate an. Ein grüner Aufwärtspfeil zeigt an, dass Ihr Workspace über der Branchenrate liegt; ein roter Abwärtspfeil zeigt an, dass er darunter liegt. |
| Monatliches Trend-Chart | Stellt die Rate Ihres Workspace im Zeitverlauf der Branchenrate gegenüber, sodass Sie Saisonalität und längerfristige Trends erkennen können. |
| Regionale Aufschlüsselung | Schlüsselt die Rate Ihres Workspace im Vergleich zur Branchenrate nach Regionen auf, sodass Sie erkennen können, wo die regionale Performance von der Branche abweicht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abschnitt" }

In jedem Chart stellt die hellere Datenreihe den Branchen-Benchmark dar, und die dunklere Reihe (mit dem Präfix **Workspace**) repräsentiert Ihre eigene Performance.

## Verfügbare Metriken {#available-metrics}

Jede kanalbasierte Metrik ist in zwei Typen verfügbar:

| Metriktyp | Beschreibung | Beispiel |
|----------|---------------------------------------|------------------------------------------------------|
| _Total_ | Zählt jedes Engagement-Ereignis. | Wenn Nutzer:innen dreimal klicken, wird das als drei Klicks gezählt. |
| _Distinct_ | Zählt eindeutige Nutzer:innen. | Wenn Nutzer:innen dreimal klicken, wird das als ein Klick gezählt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Metriktyp" }

Metriken werden nach den folgenden Kombinationen aus Branche, Region, Unterbranche und Datum gruppiert:

- Branche + Datum
- Branche + Region + Datum
- Branche + Unterbranche + Region + Datum

Wählen Sie einen Tab aus, um die Metriken für jeden Kanal anzuzeigen.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

{% tabs %}
{% tab E-Mail %}

<table aria-label="E-Mail-Metriken"><thead><tr><th>Metrik</th><th>Beschreibung</th><th>Formel</th></tr></thead><tbody>
<tr><td class="no-split"><i>Eindeutige Öffnungsrate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Diese Rate schließt maschinelle Öffnungen aus.</td><td class="no-split"><i>Unique Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Eindeutige Klickrate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Eindeutige Click-to-Open-Rate</i></td><td class="no-split">Der Prozentsatz der Nutzer:innen, die eine E-Mail nach dem Öffnen angeklickt haben.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Opens</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="E-Mail-Metriken" }

![E-Mail-Industry-Benchmarks-Metriken dargestellt in Linien- und Balkendiagrammen.]({% image_buster /assets/img/dashboards/email_industry.png %})

{% endtab %}
{% tab Push %}

Push-Metriken sind für iOS, Android, Internet und plattformübergreifend verfügbar.

<table aria-label="Push-Metriken"><thead><tr><th>Metrik</th><th>Beschreibung</th><th>Formel</th></tr></thead><tbody>
<tr><td class="no-split"><i>Direkte Öffnungsrate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td><td class="no-split"><i>Direct Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Beeinflusste Öffnungsrate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}</td><td class="no-split"><i>Influenced Opens</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Gesamtöffnungsrate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td><td class="no-split">(<i>Direct Opens</i> + <i>Influenced Opens</i>) / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push-Metriken" }

![Push-Industry-Benchmarks-Metriken dargestellt in Linien- und Balkendiagrammen.]({% image_buster /assets/img/dashboards/push_industry.png %})

{% endtab %}
{% tab SMS %}

<table aria-label="SMS-Metriken"><thead><tr><th>Metrik</th><th>Beschreibung</th><th>Formel</th></tr></thead><tbody>
<tr><td class="no-split"><i>Zustellrate</i></td><td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td><td class="no-split"><i>Deliveries</i> / <i>Unique Sends</i></td></tr>
<tr><td class="no-split"><i>Kurzlink-Klickrate</i></td><td class="no-split">Der Prozentsatz der Nutzer:innen, die nach dem Empfang einer SMS auf einen Kurzlink geklickt haben.</td><td class="no-split"><i>Short Link Clicks</i> / <i>Unique Sends</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS-Metriken" }

![SMS-Industry-Benchmarks-Metriken dargestellt in Linien- und Balkendiagrammen.]({% image_buster /assets/img/dashboards/sms_industry.png %})

{% endtab %}
{% tab Content Cards %}

<table aria-label="Content-Cards-Metriken"><thead><tr><th>Metrik</th><th>Beschreibung</th><th>Formel</th></tr></thead><tbody>
<tr><td class="no-split"><i>Klickrate</i></td><td class="no-split">Der Prozentsatz der Nutzer:innen, die eine Content Card erhalten und auf einen Link geklickt haben.</td><td class="no-split"><i>Unique Clicks</i> / <i>Unique Impressions</i></td></tr>
</tbody></table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content-Cards-Metriken" }

![Content-Cards-Industry-Benchmarks-Metriken dargestellt in Linien- und Balkendiagrammen.]({% image_buster /assets/img/dashboards/content_card_industry.png %})

{% endtab %}
{% endtabs %}

## Methodik {#methodology}

Braze-Benchmarks werden in einem dreistufigen Verfahren berechnet, das darauf ausgelegt ist, stabile und repräsentative Werte zu liefern.

### Schritt 1: Dynamisches Sampling {#step-1-dynamic-sampling}

Anstatt jeden Datenpunkt zu analysieren, wählt Braze eine repräsentative Stichprobe aus. Die Sampling-Methode überrepräsentiert kleinere Nutzergruppen für eine angemessene Darstellung und berücksichtigt die Unternehmensgröße, sodass eine kleine Anzahl sehr großer Unternehmen die Ergebnisse für eine gesamte Branche nicht verzerrt.

### Schritt 2: Ausreißer-Entfernung {#step-2-outlier-removal}

Braze identifiziert und entfernt statistische Ausreißer. Dies reduziert die Volatilität in den Daten erheblich, bei minimaler Auswirkung auf die durchschnittlichen Performance-Raten – Anomalien werden also entfernt, ohne die zugrunde liegenden Trends zu verändern.

### Schritt 3: Post-Stratifikations-Gewichtung {#step-3-post-stratification-weighting}

Die Stichprobe wird gewichtet, um die reale Population abzubilden. Gewichtungen werden auf Untergruppen angewendet, um verbleibende Ungleichgewichte aus dem Sampling zu korrigieren, sodass die endgültigen Benchmarks repräsentativ und unverzerrt sind.

## Data Governance {#data-governance}

- **Aktualisierungszyklus:** Die Daten werden monatlich am 5. jedes Monats aktualisiert und sind bis zum letzten abgeschlossenen Monat aktuell.
- **Datenschutz:** Alle Benchmarks sind aggregiert und anonymisiert, um Nutzerinformationen zu schützen.