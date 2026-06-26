---
nav_title: Analyze
article_title: Operator Analyze
page_order: 100
description: "Stellen Sie Fragen in natürlicher Sprache zu Ihrem Kanal-Engagement, zugeordnetem Umsatz und wie Sie im Vergleich zu Branchen-Benchmarks abschneiden. Sie erhalten Charts, Vergleiche und umsetzbare Insights in Sekunden."
page_type: reference
hidden: true
---

# Operator Analyze {#operator-analyze}

> Operator Analyze beantwortet Performance-Fragen in natürlicher Sprache in BrazeAI Operator<sup>TM</sup>. Die Antworten umfassen Charts, Vergleiche und kurze Insights. Sie müssen kein Dashboard erstellen oder zuerst einen vollständigen Bericht abrufen.

{% alert important %}
Operator Analyze befindet sich derzeit in der Beta-Phase. Funktionen und unterstützte Analysen werden weiterentwickelt. Um Zugang für Ihr Konto anzufordern, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Warum Operator Analyze verwenden? {#why-use-operator-analyze}

Die meisten Performance-Fragen erfordern immer noch einen Wechsel zwischen Tools, das Erstellen von Ansichten oder das Warten auf jemand anderen. Beispiele sind „Wie lief die letzte Woche“, „Liegen wir im Vergleich zum Benchmark auf Kurs“ und „Welche Campaign erzielt die stärksten Ergebnisse?“

Operator Analyze deckt Engagement-Metriken, *Attributed Revenue* und Branchen-Benchmarks ab. Das sind dieselben Daten, die Sie sonst in einen Bericht oder ein Dashboard ziehen würden. Fragen Sie in Ihren eigenen Worten über das Operator-Panel. Sie erhalten ein Chart, einen Rangvergleich oder eine Tabelle plus ein bis fünf umsetzbare Insights.

## Zugriff auf Operator Analyze {#access-operator-analyze}

Operator Analyze läuft im Operator-Konversations-Panel.

1. Wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Nutzerprofil auf einer beliebigen Seite im Braze-Dashboard aus.
2. Fragen Sie nach Kanal-Engagement oder Benchmark-Vergleichen (siehe [Beispielfragen](#example-questions)).
3. Operator gibt die Antwort zurück und, wenn hilfreich, ein Chart oder eine Tabelle sowie eine kurze Liste von Insights.

Weitere Informationen zum Operator-Chat-Panel finden Sie unter [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/).

## Beispielfragen {#example-questions}

Beschreiben Sie, was Sie wissen möchten. Es ist keine feste Formulierung erforderlich. Wählen Sie einen Tab für Beispiel-Prompts.

{% tabs %}
{% tab Benchmark-Vergleiche %}

* „Wie schneidet unsere E-Mail-*Öffnungsrate* im Vergleich zu Branchen-Benchmarks der letzten 30 Tage ab?“
* „Liegen wir in diesem Quartal über oder unter dem Benchmark für die SMS-*Click-Through-Rate*?“
* „Wo liegen wir in unserem Kanal-Mix unter dem Branchendurchschnitt?“

{% endtab %}
{% tab Kanal-Übersichten %}

* „Welche Kanäle performen für uns im bisherigen GJ26 am besten?“
* „Schlüssle das Engagement nach Kanal für die letzten 90 Tage auf.“
* „Wie viel *Attributed Revenue* hat jeder Marketing-Kanal im letzten Quartal erzielt?“

{% endtab %}
{% tab Campaign- und Canvas-Detailanalysen %}

* „Was sind unsere Top-10-E-Mail-Campaigns nach *Click-Through-Rate* in diesem Geschäftsquartal?“
* „Welche Canvases haben letzten Monat die meisten *Klicks* erzielt?“
* „Welche Campaigns haben im GJ26 Q1 den meisten *Attributed Revenue* generiert?“
* „Zeige unsere am schlechtesten performenden Push-Campaigns der letzten 30 Tage.“

{% endtab %}
{% tab Trendanalyse %}

* „Wie sieht der Monats-über-Monats-Trend beim Push-Engagement für GJ26 aus?“
* „Wie hat sich die E-Mail-*Click-Through-Rate* im Quartalsvergleich über das letzte Jahr verändert?“
* „Wie hat sich unser *Attributed Revenue* in den letzten 12 Monaten entwickelt?“
* „Zeige mir unseren wöchentlichen Engagement-Trend für In-App-Nachrichten über die letzten 90 Tage.“

{% endtab %}
{% tab Umsatz und Conversions %}

Fragen Sie nach *Attributed Revenue* und *Conversions*, aggregiert auf Campaign-, Canvas-, Kanal- oder Programmebene.

* „Vergleiche *Attributed Revenue* und *Conversions* für das letzte Quartal mit dem vorherigen Quartal.“
* „Welche Campaigns haben in den letzten 90 Tagen den meisten *Attributed Revenue* erzielt?“
* „Schlüssle *Attributed Revenue* nach Kanal für das bisherige GJ26 auf.“

{% endtab %}
{% tab Umfassende Bewertungen %}

* „Gib mir eine vollständige Bewertung unseres Engagement-Programms mit Empfehlungen.“
* „Wo liegen unsere größten Chancen und Risiken über alle Kanäle hinweg gerade?“

{% endtab %}
{% endtabs %}

## Visualisierungen {#visualizations}

Operator fügt ein Chart hinzu, wenn die Daten es unterstützen. **Liniendiagramme** eignen sich für Zeitreihen, **Balkendiagramme** für Kategorievergleiche und **Tabellen** für andere Fälle. Tabellen zeigen Prozentsätze mit zwei Dezimalstellen und verwenden Punkte als Tausendertrennzeichen.

Wenn eine Antwort mehrere Metriken enthält, priorisiert Operator Engagement-Raten (*Öffnungsrate*, *Klickrate*, *Push-Öffnungsrate*) gegenüber reinen Zählwerten.

## Unterstützte Kanäle und Metriken {#supported-channels-and-metrics}

*Attributed Revenue* und *Conversions* verwenden dieselbe Campaign-, Canvas-, Kanal- und Programm-Aggregation, die unter [Beispielfragen](#example-questions) im Tab **Umsatz und Conversions** gezeigt wird.

| Kanal | Metriken | Branchen-Benchmarks |
| --- | --- | --- |
| E-Mail | *Sends*, *Deliveries*, *Unique Opens*, *Unique Clicks*, *Unsubscribes* | Ja |
| Push (iOS, Android, Web) | *Sends*, *Deliveries*, *Opens* | Ja |
| SMS | *Sends*, *Deliveries*, *Link Clicks* | Ja |
| In-App Messages | *Impressions*, *Clicks* | Ja |
| Content Cards | *Sends*, *Impressions*, *Clicks* | Ja |
| WhatsApp | *Sends*, *Deliveries*, *Reads*, *Clicks* | Noch nicht |
| RCS | *Sends*, *Deliveries*, *Reads*, *Clicks* (einschließlich Text-URL-, Button-, Aktions-, Antwort-Aktions- und Antwort-Button-Untertypen) | Noch nicht |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Kanäle, Metriken und Benchmark-Verfügbarkeit" }

{% alert tip %}
Operator verwendet eindeutige Zählungen für Raten (zum Beispiel *Unique Opens* geteilt durch *Deliveries* für die *E-Mail-Öffnungsrate*). Wenn eine Zahl von einem Dashboard abweicht, vergleichen Sie Attributionsfenster, Zeitraum und Definition. Operator listet alle drei in jeder Antwort auf.
{% endalert %}

## Zeiträume und Attributionsfenster {#time-periods-and-attribution-windows}

### Geschäftsjahr vs. Kalenderjahr {#fiscal-year-vs-calendar-year}

Operator Analyze verwendet standardmäßig das **Braze-Geschäftsjahr**, das vom 1. Februar bis zum 31. Januar läuft.

| Geschäftsquartal | Monate |
| --- | --- |
| GQ1 | Feb – Apr |
| GQ2 | Mai – Jul |
| GQ3 | Aug – Okt |
| GQ4 | Nov – Jan |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze-Geschäftsquartale und Kalendermonate" }

Für Kalenderjahr-Fragen verwenden Sie „KJ“, „Kalenderjahr“ oder „Standardjahr“. Mehrdeutige Formulierungen wie „letztes Jahr“ veranlassen Operator, nachzufragen, welchen Kalender Sie meinen.

Sie können auch ISO-Bereiche wie `Q4 2025` oder `2025-03-01 to 2025-05-31` verwenden.

### Attributionsfenster {#attribution-windows}

Operator Analyze verwendet standardmäßig **7 Tage**. Nennen Sie ein Fenster in Ihrer Frage, um den Standard zu überschreiben:

* **1 Tag** für schnelle Engagement-Checks
* **3 Tage** für Kurzzeit-Campaigns
* **7 Tage** für allgemeine Übersichten und Campaign-Auswertungen (Standard)
* **30 Tage** für strategische oder langfristige Betrachtungen
* **Alle Fenster** für einen 1T / 3T / 7T / 30T Seite-an-Seite-Vergleich

Wenn sich die Ergebnisse über die Fenster hinweg um mehr als 50 % unterscheiden, zeigt Operator alle vier nebeneinander an.

## Datenaktualität {#data-freshness}

Die Daten werden täglich aktualisiert. Aktivitäten des aktuellen Tages erscheinen nach der nächsten Aktualisierung. Jede Antwort gibt das neueste Datum im Datensatz an. Wenn dieses Datum veraltet erscheint, wenden Sie sich an Ihren Customer-Success-Manager.

## Was nicht abgedeckt wird {#whats-out-of-scope}

* **Performance-Aufschlüsselungen auf Produktebene.** *Attributed Revenue* und Engagement werden auf Campaign-, Canvas-, Kanal- oder Programmebene aggregiert. Sie werden nicht auf Produkte oder SKUs heruntergebrochen. Fragen auf Produkt- oder SKU-Ebene werden nicht unterstützt. Wenden Sie sich für diese Analysen an Ihren Customer-Success-Manager.
* **Branchen-Benchmarks für WhatsApp und RCS.** Engagement-Metriken für beide Kanäle werden unterstützt. Benchmarks sind noch nicht verfügbar.

Fragen außerhalb des Umfangs erhalten eine direkte Antwort, wenn möglich eine vorgeschlagene Alternative oder einen Verweis an Ihren Customer-Success-Manager.

## Tipps für bessere Ergebnisse {#tips-for-better-results}

* **Zeitraum:** Bevorzugen Sie explizite Bereiche („GJ26 Q2“, „die letzten 90 Tage“) gegenüber vagen Formulierungen wie „letztes Quartal“, wenn Sie Präzision benötigen.
* **Metriken:** Nennen Sie die Rate, die Sie interessiert (*Öffnungsrate*, *Click-Through-Rate*, *Click-to-Open-Rate*). Operator gibt die verwendete Formel an.
* **Nachfragen:** Vertiefen Sie ein Ergebnis, ändern Sie das Fenster oder wechseln Sie den Kanal. Operator behält den Kontext über den Thread hinweg bei.
* **Kanal-Formulierung:** WhatsApp und RCS verwenden *Read Rate* (nicht *Öffnungsrate*). SMS verwendet *Link Click Rate*.
* **Kombinierte Fragen:** Benchmark plus Trend in einem Prompt wird unterstützt.

## Datenschutz und Sicherheit {#data-privacy-and-security}

Operator Analyze folgt demselben Datenschutz- und Sicherheitsmodell wie BrazeAI Operator<sup>TM</sup>. Weitere Informationen finden Sie unter [Datenschutz und Sicherheit]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security/).

## Nächste Schritte {#next-steps}

* [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)
* [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/)