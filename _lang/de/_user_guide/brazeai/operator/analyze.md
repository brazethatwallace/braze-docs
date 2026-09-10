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
Operator Analyze befindet sich derzeit in der Beta-Phase. Funktionen und unterstützte Analysen werden weiterentwickelt. Um Zugang für Ihr Konto anzufordern, wenden Sie sich an Ihren CSM.
{% endalert %}

## Warum Operator Analyze verwenden? {#why-use-operator-analyze}

Die meisten Fragen zur Performance erfordern nach wie vor einen Wechsel zwischen Tools, das Erstellen von Ansichten oder das Warten auf jemand anderen. Beispiele sind „Wie lief die letzte Woche?“, „Liegen wir im Vergleich zum Benchmark auf Kurs?“ und „Welche Campaign erzielt die stärksten Ergebnisse?“

Operator Analyze deckt Engagement-Metriken, *Attributed Revenue* und Branchen-Benchmarks ab. Das sind dieselben Daten, die Sie sonst in einen Bericht oder ein Dashboard ziehen würden. Stellen Sie Ihre Frage in eigenen Worten über das Operator-Panel. Sie erhalten ein Chart, einen Rangvergleich oder eine Tabelle sowie ein bis fünf umsetzbare Insights.

## Auf Operator Analyze zugreifen {#access-operator-analyze}

Operator Analyze wird im Operator-Konversationspanel ausgeführt.

1. Wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Nutzerprofil auf einer beliebigen Seite im Braze-Dashboard aus.
2. Stellen Sie eine Frage zu Kanal-Engagement oder Benchmark-Vergleichen (siehe [Beispielfragen](#example-questions)).
3. Operator gibt die Antwort zurück und, wenn hilfreich, ein Chart oder eine Tabelle sowie eine kurze Liste von Insights.

Weitere Informationen zum Operator-Chat-Panel finden Sie unter [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator).

## Beispielfragen {#example-questions}

Beschreiben Sie, was Sie wissen möchten. Eine feste Formulierung ist nicht erforderlich. Wählen Sie einen Tab für Beispiel-Prompts aus.

{% tabs %}
{% tab Benchmark-Vergleiche %}

* „Wie schneidet unsere E-Mail-*Öffnungsrate* im Vergleich zu Branchen-Benchmarks der letzten 30 Tage ab?“
* „Liegen wir in diesem Quartal über oder unter dem Benchmark für die SMS-*Click-Through-Rate*?“
* „Wo liegen wir in unserem Kanalmix unter dem Branchendurchschnitt?“

{% endtab %}
{% tab Kanalübersichten %}

* „Welche Kanäle performen für uns im laufenden GJ26 am besten?“
* „Schlüssle das Engagement nach Kanal für die letzten 90 Tage auf.“
* „Wie viel *zugeordneten Umsatz* hat jeder Marketingkanal im letzten Quartal generiert?“

{% endtab %}
{% tab Campaign- und Canvas-Detailanalysen %}

* „Was sind unsere Top-10-E-Mail-Campaigns nach *Click-Through-Rate* in diesem Geschäftsquartal?“
* „Welche Canvases haben im letzten Monat die meisten *Klicks* erzielt?“
* „Welche Campaigns haben im 1. Quartal des GJ26 den meisten *zugeordneten Umsatz* generiert?“
* „Zeige unsere Push-Campaigns mit der schlechtesten Performance der letzten 30 Tage.“

{% endtab %}
{% tab Trendanalyse %}

* „Wie sieht der Monat-für-Monat-Trend beim Push-Engagement im GJ26 aus?“
* „Wie hat sich die E-Mail-*Click-Through-Rate* im Quartalsvergleich im letzten Jahr verändert?“
* „Wie hat sich unser *zugeordneter Umsatz* in den letzten 12 Monaten entwickelt?“
* „Zeige mir unseren wöchentlichen Engagement-Trend für In-App-Nachrichten der letzten 90 Tage.“

{% endtab %}
{% tab Umsatz und Konversionen %}

Fragen Sie nach *zugeordnetem Umsatz* und *Konversionen*, aggregiert auf Campaign-, Canvas-, Kanal- oder Programmebene.

* „Vergleiche *zugeordneten Umsatz* und *Konversionen* des aktuellen Quartals mit dem Vorquartal.“
* „Welche Campaigns haben in den letzten 90 Tagen den meisten *zugeordneten Umsatz* erzielt?“
* „Schlüssle den *zugeordneten Umsatz* nach Kanal für das laufende GJ26 auf.“

{% endtab %}
{% tab Umfassende Auswertungen %}

* „Erstelle eine vollständige Auswertung unseres Engagement-Programms mit Empfehlungen.“
* „Wo liegen aktuell unsere größten Chancen und Risiken über alle Kanäle hinweg?“

{% endtab %}
{% endtabs %}

## Visualisierungen {#visualizations}

Operator fügt ein Chart hinzu, wenn die Daten es unterstützen. **Liniendiagramme** eignen sich für Zeitreihen, **Balkendiagramme** für Kategorievergleiche und **Tabellen** für andere Fälle. Tabellen zeigen Prozentsätze mit zwei Dezimalstellen an und verwenden Kommas für große Zahlen.

Wenn eine Antwort mehrere Metriken enthält, priorisiert Operator Engagement-Raten (*Öffnungsrate*, *Klickrate*, *Push-Öffnungsrate*) gegenüber Rohwerten.

## Unterstützte Kanäle und Metriken {#supported-channels-and-metrics}

*Zugeordneter Umsatz* und *Konversionen* verwenden dieselbe Aggregation nach Campaign, Canvas, Kanal und Programm, die unter [Beispielfragen](#example-questions) im Tab **Umsatz und Konversionen** dargestellt wird.

| Kanal | Metriken | Branchen-Benchmarks |
| --- | --- | --- |
| E-Mail | *Sends*, *Deliveries*, *Unique Opens*, *Unique Clicks*, *Unsubscribes* | Ja |
| Push (iOS, Android, Web) | *Sends*, *Deliveries*, *Opens* | Ja |
| SMS | *Sends*, *Deliveries*, *Link Clicks* | Ja |
| In-App Messages | *Impressions*, *Clicks* | Ja |
| Content Cards | *Sends*, *Impressions*, *Clicks* | Ja |
| WhatsApp | *Sends*, *Deliveries*, *Reads*, *Clicks* | Noch nicht |
| RCS | *Sends*, *Deliveries*, *Reads*, *Clicks* (einschließlich der Untertypen Text-URL, Button, Aktion, Antwort-Aktion und Antwort-Button) | Noch nicht |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Kanäle, Metriken und Verfügbarkeit von Benchmarks" }

{% alert tip %}
Operator verwendet eindeutige Zählungen für Raten (zum Beispiel *Unique Opens* geteilt durch *Deliveries* für die *E-Mail-Öffnungsrate*). Wenn ein Wert vom Dashboard abweicht, vergleichen Sie das Attributionsfenster, den Zeitraum und die Definition. Operator listet alle drei Angaben in jeder Antwort auf.
{% endalert %}

## Zeiträume und Attributionsfenster {#time-periods-and-attribution-windows}

### Geschäftsjahr vs. Kalenderjahr {#fiscal-year-vs-calendar-year}

Operator Analyze verwendet standardmäßig das **Braze-Geschäftsjahr**, das vom 1. Februar bis zum 31. Januar läuft.

| Geschäftsquartal | Monate |
| --- | --- |
| FQ1 | Feb – Apr |
| FQ2 | Mai – Jul |
| FQ3 | Aug – Okt |
| FQ4 | Nov – Jan |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze-Geschäftsquartale und Kalendermonate" }

Für Fragen zum Kalenderjahr verwenden Sie „CY“, „calendar year“ oder „standard year“. Bei einem mehrdeutigen „last year“ fragt Operator nach, welchen Kalender Sie meinen.

Sie können auch ISO-konforme Bereiche wie `Q4 2025` oder `2025-03-01 to 2025-05-31` verwenden.

### Attributionsfenster {#attribution-windows}

Operator Analyze verwendet standardmäßig **7 Tage**. Geben Sie in Ihrer Frage ein Fenster an, um den Standard zu überschreiben:

* **1 Tag** für schnelle Engagement-Checks
* **3 Tage** für Campaigns mit kurzem Zyklus
* **7 Tage** für allgemeine Übersichten und Campaign-Auswertungen (Standard)
* **30 Tage** für strategische oder langfristige Betrachtungen
* **Alle Fenster** für einen 1D-/3D-/7D-/30D-Vergleich nebeneinander

Wenn sich die Ergebnisse über die Fenster hinweg um mehr als 50 % unterscheiden, zeigt Operator alle vier nebeneinander an.

## Aktualität der Daten {#data-freshness}

Die Daten werden täglich aktualisiert. Aktivitäten des aktuellen Tages erscheinen nach der nächsten Aktualisierung. Jede Antwort enthält das neueste Datum im Datensatz. Wenn dieses Datum veraltet erscheint, wenden Sie sich an Ihren Customer-Success-Manager.

## Was nicht abgedeckt wird {#whats-out-of-scope}

* **Performance-Aufschlüsselungen auf Produktebene.** *Attributed Revenue* und Engagement werden auf Campaign-, Canvas-, Kanal- oder Programmebene zusammengefasst. Sie werden nicht nach Produkten oder SKUs aufgeschlüsselt. Fragen auf Produkt- oder SKU-Ebene werden nicht unterstützt. Wenden Sie sich für diese Analysen an Ihre:n Customer-Success-Manager:in.
* **Branchenbenchmarks für WhatsApp und RCS.** Engagement-Metriken für beide Kanäle werden unterstützt. Benchmarks sind noch nicht verfügbar.

Fragen, die nicht abgedeckt werden, erhalten eine direkte Antwort, nach Möglichkeit einen Alternativvorschlag oder einen Verweis an Ihre:n Customer-Success-Manager:in.

## Tipps für bessere Ergebnisse {#tips-for-better-results}

* **Zeitraum:** Bevorzugen Sie explizite Zeiträume („FY26 Q2“, „die letzten 90 Tage“) gegenüber vagen Formulierungen wie „letztes Quartal“, wenn Sie Präzision benötigen.
* **Metriken:** Benennen Sie die Rate, die Sie interessiert (*Öffnungsrate*, *Click-Through-Rate*, *Click-to-Open-Rate*). Operator gibt die verwendete Formel an.
* **Nachfragen:** Vertiefen Sie ein Ergebnis, ändern Sie den Zeitraum oder wechseln Sie den Kanal. Operator behält den Kontext über den gesamten Thread hinweg.
* **Kanalspezifische Begriffe:** WhatsApp und RCS verwenden *Read Rate* (nicht *Öffnungsrate*). SMS verwendet *Link Click Rate*.
* **Kombinierte Anfragen:** Benchmark plus Trend in einem einzigen Prompt werden unterstützt.

## Datenschutz und Sicherheit {#data-privacy-and-security}

Operator Analyze folgt demselben Datenschutz- und Sicherheitsmodell wie BrazeAI Operator<sup>TM</sup>. Weitere Informationen finden Sie unter [Datenschutz und Sicherheit]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: BrazeAI Operator
  link: /docs/user_guide/brazeai/operator
  description: Greifen Sie auf den Operator zu und erkunden Sie seine Dashboard-Funktionen.
- name: Aktionen überprüfen
  link: /docs/user_guide/brazeai/operator/reviewing_actions
  description: Überprüfen und genehmigen Sie die vorgeschlagenen Änderungen des Operators.
{% endarticle_tiles %}