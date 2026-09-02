---
nav_title: "RFM-Segmente"
article_title: RFM-SQL-Segmenterweiterungen
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Dieser Artikel beschreibt, wie Sie RFM-Segmenterweiterungen erstellen, die Ihre besten Nutzer:innen anhand ihres Kaufverhaltens identifizieren."
tool: Segments
---

# RFM-SQL-Segmente {#rfm-sql-segments}

> Sie können eine RFM-Segmenterweiterung (Recency, Frequency, Monetary) erstellen, um Ihre besten Nutzer:innen anhand ihres Kaufverhaltens gezielt anzusprechen.

Die RFM-Analyse ist eine Marketingtechnik, die Ihre besten Nutzer:innen identifiziert, indem sie auf einer Skala von 0–3 für jede Kategorie (Recency, Frequency, Monetary) bewertet werden, wobei 3 die beste und 0 die schlechteste Bewertung ist. Die Werte für Recency, Frequency und Monetary basieren alle auf Daten aus einem bestimmten Zeitraum Ihrer Wahl.

## RFM-Kategorien {#rfm-categories}

| Kategorie | Definition |
| --- | --- |
| Recency | Wie kürzlich ein:e Kund:in einen Kauf getätigt hat. Eine höhere Bewertung bedeutet aktuellere Käufe. |
| Frequency | Wie häufig ein:e Kund:in einen Kauf getätigt hat. Eine höhere Bewertung bedeutet höhere Häufigkeit. |
| Monetary | Gesamtbetrag, den ein:e Kund:in ausgegeben hat. Eine höhere Bewertung bedeutet höhere Ausgaben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RFM-Kategorien" }

{% alert note %}
Kauf-Events müssen aktiviert sein, um RFM-SQL-Segmente verwenden zu können, da der Monetary-Wert Ihrer Nutzer:innen durch den Umsatz bestimmt wird, den sie über Braze-Kauf-Events generiert haben.
{% endalert %}

## Ein RFM-Segment erstellen {#creating-an-rfm-segment}

1. Gehen Sie zu **Audience** > **Segment Extensions**.
2. Wählen Sie **New Extension** und dann **Recency, frequency, and monetary value (RFM) segment** aus.

![Modal mit der Option, ein Katalog-Segment für Events, Käufe oder RFM-Segmente zu erstellen.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3. Wählen Sie im **Variables**-Panel Ihren **Time Range** aus, um den Zeitraum der zu analysierenden Kaufdaten festzulegen. Sie können bis zu 60 Tage in der Vergangenheit angeben. Der von Ihnen gewählte Zeitraum ist der Zeitraum, aus dem Nutzerverhaltensdaten abgerufen werden, und hängt von Ihren Campaign-Zielen ab.

| Zeitraum-Feld | Beschreibung | Anwendungsfall |
| --- | --- | --- |
| Relative | Aktivität innerhalb der letzten X Tage angeben | Das aktuellste Nutzerverhalten mit einem rollierenden Fenster analysieren. |
| Start date | Einen festen Startpunkt für Ihre Analyse angeben | Nutzeraktivität ab einem bestimmten Datum analysieren, z. B. nach dem Start einer Campaign. |
| End date | Einen festen Endpunkt für Ihre Analyse angeben | Nutzeraktivität bis zu einem bestimmten Datum analysieren, z. B. vor einem Produkt-Update or aktualisieren. |
| Date range | Sowohl ein Start- als auch ein Enddatum für einen benutzerdefinierten Zeitraum angeben | Nutzerverhalten während eines definierten Zeitraums analysieren, z. B. während einer Aktion. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ein RFM-Segment erstellen" }

{: start="4"}
4. Wählen Sie die generierten [RFM-Gruppen](#rfm-groups) aus, die in Ihr Segment aufgenommen werden sollen. Wenn Sie mehrere Gruppen auswählen, umfasst Ihr Segment Nutzer:innen, die Teil einer der ausgewählten Gruppen sind.

![Variables-Panel mit den ausgewählten RFM-Gruppen „Champions“ und „Loyal Users“.]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5. Führen Sie eine Vorschau aus und speichern Sie dann Ihr Segment.

{% alert note %}
Sie müssen den SQL-Code im Template nicht bearbeiten, um ein RFM-Segment zu erstellen. Sie können ausschließlich das **Variables**-Panel verwenden, um Ihr Segment anzupassen.
{% endalert %}

### RFM-Gruppen {#rfm-groups}

RFM-Segmente werden in einer bestimmten Reihenfolge ausgewertet. Nutzer:innen werden dem ersten Segment zugewiesen, dessen Kriterien sie erfüllen, von oben in der Priorisierungsliste nach unten. Beispielsweise wird ein:e Nutzer:in, die/der sowohl für „Champions“ als auch für „Loyal Users“ qualifiziert ist, dem Segment „Champions“ zugewiesen, da es eine höhere Priorität hat.

| RFM-Gruppe | Segmentbeschreibung | Recency (R) Rang | Frequency (F) Rang | Monetary (M) Rang |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Champions | Das wertvollste Nutzersegment mit Spitzenwerten in allen Kategorien. | 3 | 2–3 | 2–3 |
| Loyal Users | Nutzer:innen mit hoher Recency und hoher Frequency. Können einen niedrigeren Monetary-Wert als Champions haben. | 2–3 | 2–3 | 1–3 |
| Potential Loyalists | Nutzer:innen, die kürzlich mit moderater Frequency und moderatem Monetary-Wert gekauft haben. | 3 | 1–3 | 1–3 |
| Promising | Nutzer:innen, die einen kürzlichen, hochwertigen Erstkauf getätigt haben, aber noch keine hohe Kaufhäufigkeit aufgebaut haben. | 3 | 0–3 | 1–3 |
| New Customer | Nutzer:innen, die erst kürzlich ihren ersten Kauf getätigt haben. | 3 | 0–3 | 0–3 |
| Needing Attention | Nutzer:innen mit überdurchschnittlicher Recency, deren Kaufhäufigkeit oder Monetary-Wert jedoch unterdurchschnittlich sind. | 2–3 | 0–3 | 0–3 |
| Cannot lose them | Nutzer:innen, die zuvor hochwertig waren mit guten Frequency- und Monetary-Werten, aber seit Langem nicht mehr gekauft haben. | 0–1 | 2–3 | 2–3 |
| At Risk | Nutzer:innen, die historisch moderate Frequency- und Monetary-Werte hatten, aber seit Langem nicht mehr gekauft haben. | 0–1 | 1–3 | 1–3 |
| About to Sleep | Nutzer:innen mit niedrigen Werten in allen Metriken. | 1 | 0–3 | 0–3 |
| Hibernating | Nutzer:innen mit moderater Frequency, die jedoch über einen längeren Zeitraum inaktiv waren. | 0 | 0–2 | 0–3 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="RFM-Gruppen" }