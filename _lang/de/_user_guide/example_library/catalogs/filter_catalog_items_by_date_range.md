---
nav_title: Nach Datumsbereich filtern
article_title: Katalogartikel nach Datumsbereich filtern
page_order: 1
page_type: reference
description: "Verwenden Sie Katalogselektionen mit Liquid-Datumsausdrücken, um Katalogartikel innerhalb eines rollierenden Zeitfensters anzuzeigen, z. B. Ereignisse in den nächsten sieben Tagen."
---

# Katalogartikel nach Datumsbereich filtern {#filter-catalog-items-by-date-range}

> Dieses Beispiel zeigt, wie ein fiktiver Ticketmarktplatz Katalogselektionen und Liquid-Datumsausdrücke nutzt, um Verbraucher:innen per E-Mail nur über Ereignisse zu informieren, die innerhalb der nächsten sieben Tage ab dem Sendezeitpunkt stattfinden. Sie erstellen eine Selektion mit rollierenden Zeitfiltern und rendern die passenden Katalogartikel dann in einer Campaign- oder Canvas-Nachricht.

## Über dieses Beispiel {#about-this-example}

MovieCanon, ein fiktiver Ticketmarktplatz, verwendet dieses Muster, um sicherzustellen, dass E-Mail-Campaigns nur zeitlich relevante Konzerte und Shows auflisten.

Das Muster nutzt zwei Braze-Features zusammen:

- Eine [Katalogselektion]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) mit `time`-Feldfiltern, deren Werte Liquid-Snippets sind, die zum Sendezeitpunkt ein rollierendes Zeitfenster berechnen
- Den {% raw %}`{% catalog_selection_items %}`{% endraw %}-Liquid-Tag im Nachrichtentext, um passende Katalogzeilen zu rendern

## Hinweise {#considerations}

- Erstellen Sie für die Datetime-Spalte, nach der Sie filtern, ein Katalogfeld vom Typ `time` – kein String-Feld. Speichern Sie Werte im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format, z. B. `2026-06-20T19:30:00Z`. Unterstützte Typen finden Sie unter [Unterstützte Datentypen]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types).
- Die Operatoren `before` und `after` verwenden strikte Vergleiche. Ereignisse, die exakt einem Grenz-Zeitstempel entsprechen, können ausgeschlossen werden. Verwenden Sie vollständige Zeitstempel, wenn das Fenster zum Sendezeitpunkt beginnen soll. Reine Datumswerte im Format `YYYY-MM-DD` werden auf Mitternacht UTC dieses Tages umgewandelt.
- Liquid in Selektionsfiltern wird zum Sendezeitpunkt ausgewertet. Die Variable `'now'` gibt den Zeitpunkt wieder, zu dem die Nachricht gerendert wird – in der Regel in UTC. Überprüfen Sie, ob das resultierende Zeitfenster über alle Zeitzonen hinweg Ihrer Absicht entspricht.
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), Katalog-Tags und `abort_message` werden in Selektionsfilterwerten nicht unterstützt. Enthält ein Filter einen nicht zulässigen Tag, gibt die Selektion keine Artikel zurück, ohne einen Fehler auszulösen.
- Sie können bis zu 10 Filter pro Selektion hinzufügen und bis zu 50 Artikel zurückgeben. Passen Sie das Sieben-Tage-Fenster an, indem Sie die zu `'now'` addierten Sekunden ändern (`604800` = 7 Tage multipliziert mit `86400` Sekunden pro Tag).
- Ergebnis-Arrays von Katalogselektionen sind nullindexiert (`items[0]` ist der erste Artikel).
- Testen Sie Filter-Liquid, Nachrichten-Liquid und Abbruchlogik außerhalb Ihres Produktions-Workspace, bevor Sie an Produktionszielgruppen senden.

## Einrichtung {#setup}

Dieses Beispiel setzt einen Katalog namens `live_events` mit folgenden Feldern voraus:

| Feld | Typ | Beispielwert |
| ---- | --- | ------------ |
| `id` | String | `show-1042` |
| `event_name` | String | `Summer Jazz Night` |
| `event_date_time` | Time | `2026-06-20T19:30:00Z` |
| `ticket_price` | Number | `45` |
| `city` | String | `Austin` |
| `venue` | String | `Riverside Amphitheater` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Katalogfelder" }

Falls Sie noch keinen vergleichbaren Katalog haben, [erstellen Sie einen Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create) und laden oder synchronisieren Sie zuerst Ihre Ereignisdaten.

### Schritt 1: Katalogselektion erstellen {#step-1-create-the-catalog-selection}

1. Gehen Sie zu **Data Settings** > **Catalogs** und wählen Sie den Katalog `live_events` aus.
2. Öffnen Sie den Tab **Selection** und wählen Sie **Create Selection**.
3. Benennen Sie die Selektion `seven_day_window` und fügen Sie eine optionale Beschreibung hinzu, z. B. „Ereignisse innerhalb der nächsten sieben Tage“.
4. Legen Sie ein **Results limit** für die maximale Anzahl zurückzugebender Ereignisse fest (bis zu 50).
5. Speichern Sie noch nicht. Fügen Sie die Datumsfilter in den nächsten Schritten hinzu.

### Schritt 2: Obergrenze-Filter hinzufügen {#step-2-add-the-upper-bound-filter}

Fügen Sie einen Filter auf dem Feld `event_date_time` hinzu:

| Einstellung | Wert |
| ----------- | ---- |
| **Filter field** | `event_date_time` |
| **Operator** | `before` |
| **Value** | Liquid-Snippet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einstellungen für den Obergrenze-Filter" }

Geben Sie im Filterwertfeld dieses Liquid-Snippet ein. Es berechnet einen Zeitstempel sieben Tage ab dem Sendezeitpunkt:

{% raw %}
```liquid
{% assign seven_days = 'now' | date: '%s' | plus: 604800 %}{{ seven_days | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Dies legt die Obergrenze des Zeitfensters fest, sodass nur Ereignisse vor diesem Zeitstempel einbezogen werden.

### Schritt 3: Untergrenze-Filter hinzufügen {#step-3-add-the-lower-bound-filter}

Fügen Sie einen zweiten Filter auf demselben Feld hinzu:

| Einstellung | Wert |
| ----------- | ---- |
| **Filter field** | `event_date_time` |
| **Operator** | `after` |
| **Value** | Liquid-Snippet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einstellungen für den Untergrenze-Filter" }

Geben Sie dieses Liquid-Snippet für die Untergrenze ein. Es verwendet den aktuellen Sendezeitpunkt, sodass bereits begonnene Ereignisse ausgeschlossen werden:

{% raw %}
```liquid
{{ 'now' | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Zusammen geben die beiden Filter Katalogartikel zurück, bei denen `event_date_time` nach dem aktuellen Sendezeitpunkt und vor sieben Tagen ab dem Sendezeitpunkt liegt. Wählen Sie **Create Selection**, um zu speichern.

### Schritt 4: Selektion in einer Nachricht referenzieren {#step-4-reference-the-selection-in-a-message}

Fügen Sie in Ihrer Campaign- oder Canvas-Nachricht Liquid ein, das Artikel aus der Selektion abruft. Sie können **Add personalization** (**Catalog Items** > **Use a selection**) verwenden oder den Tag manuell einfügen:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
Here are some upcoming events:

{{ items[0].event_name }} — ${{ items[0].ticket_price }}
{{ items[0].city }} · {{ items[0].venue }}

{{ items[1].event_name }} — ${{ items[1].ticket_price }}
{{ items[1].city }} · {{ items[1].venue }}
```
{% endraw %}

Ersetzen Sie fest codierte Array-Indizes durch eine Schleife, wenn Sie eine variable Anzahl von Ergebnissen rendern möchten.

### Schritt 5: Leere Ergebnisse behandeln {#step-5-handle-empty-results}

Wenn keine Katalogartikel der Selektion entsprechen, ist das `items`-Array leer und der getaggte Block rendert nichts. Um den Versand zu überspringen oder Fallback-Text anzuzeigen, umschließen Sie den Tag mit einer Bedingung:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
{% if items.size == 0 %}
{% abort_message('Catalog selection returned 0 items') %}
{% endif %}

Here are some upcoming events:
{{ items[0].event_name }}
```
{% endraw %}

Weitere Informationen finden Sie unter [Nachrichten abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

## Verwandte Artikel {#related-articles}

- [Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Selektionen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Kataloge in Campaigns verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Liquid-`date`-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)
- [Liquid-Anwendungsfallbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)