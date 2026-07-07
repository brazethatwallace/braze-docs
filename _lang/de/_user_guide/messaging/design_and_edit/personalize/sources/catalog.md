---
nav_title: Katalog
article_title: Katalog
page_order: 2
description: "Erfahren Sie, wie Sie Kataloge als Datenquelle nutzen, um Ihre Braze-Nachrichten mit Nicht-Nutzerdaten wie Produktdetails, Inhalts-Feeds und Preisen zu personalisieren."
---

# Katalog {#catalog}

> Referenzieren Sie Nicht-Nutzerdaten in Ihren Nachrichten, indem Sie Kataloge verbinden. Kataloge speichern strukturierte Datensätze – wie Produktinformationen, Restaurantlisten oder Inhalts-Feeds –, auf die Sie über Liquid zugreifen können, um jede Nachricht zu personalisieren.

## So funktioniert es {#how-it-works}

{% raw %}
Nachdem Sie Daten in einen Katalog importiert haben (per CSV oder API), referenzieren Sie Katalogartikel in Ihren Nachrichten mit dem Liquid-Tag `items`. Um beispielsweise einen Produktnamen aus einem Katalog namens `products` abzurufen:

```liquid
{% catalog_items products {{${product_id}}} %}
{{items[0].name}} is back in stock!
```
{% endraw %}

Kataloge unterstützen bis zu 1.000 Felder pro Artikel und können Millionen von Zeilen speichern, was sie für große Produktbestände und Inhaltsbibliotheken geeignet macht.

## Häufige Anwendungsfälle {#common-use-cases}

| Anwendungsfall | Beschreibung |
| --- | --- |
| Produktdetails | Namen, Beschreibungen, Preise und Bilder aus einem Produktkatalog einfügen |
| Restaurant- oder Shop-Listen | Nachrichten mit standortspezifischen Details personalisieren |
| Inhaltsempfehlungen | Artikel, Videos oder andere Medieninhalte referenzieren |
| Ereignisinformationen | Ereignisdaten, Veranstaltungsorte und Beschreibungen in Nachrichten einfügen |
| Stufenbasierte Angebote | Aktionen mit der Mitgliedschaftsstufe oder dem Segment von Nutzer:innen abgleichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Häufige Anwendungsfälle" }

## Katalog-Trigger {#catalog-triggers}

Kataloge ermöglichen auch automatisiertes Messaging über Katalog-Trigger. Richten Sie Wieder-verfügbar-Benachrichtigungen und Preissenkungsbenachrichtigungen ein, um Nutzer:innen automatisch zu benachrichtigen, wenn sich Katalogartikel ändern.

Weitere Informationen finden Sie unter [Katalog-Trigger]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers).

## Auswahl {#selections}

Verwenden Sie Auswahlen, um Katalogartikel nach von Ihnen definierten Filtern zu gruppieren. Erstellen Sie beispielsweise eine Auswahl von Artikeln unter 20 € oder Artikeln in einer bestimmten Kategorie und referenzieren Sie dann die gefilterte Menge in Ihren Nachrichten.

Weitere Informationen finden Sie unter [Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Erste Schritte {#getting-started}

Informationen zum Erstellen und Verwalten von Katalogen finden Sie unter [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs). Um zu erfahren, wie Sie Katalogdaten in Ihren Nachrichten referenzieren, lesen Sie [Kataloge in einer Nachricht verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/use).