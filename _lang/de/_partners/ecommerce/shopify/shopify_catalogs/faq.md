---
nav_title: FAQ
article_title: FAQ zur Shopify-Produktsynchronisierung
page_order: 0
page_type: FAQ
description: "Diese Seite enthält Antworten auf häufig gestellte Fragen zur Synchronisierung von Shopify-Produkten mit Braze-Katalogen."
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Diese Seite enthält Antworten auf einige häufig gestellte Fragen zur [Shopify-Produktsynchronisierung]({{site.baseurl}}/shopify_catalogs).

## Katalog- und Synchronisationsverhalten {#catalog-and-sync-behavior}

### Kann ich meinen Shopify-Katalog direkt in Braze bearbeiten? {#can-i-edit-my-shopify-catalog-directly-in-braze}

Nein. Der Shopify-Katalog ist in Braze schreibgeschützt. Manuelle Änderungen können bei der nächsten Synchronisation überschrieben werden. Nehmen Sie alle Produktaktualisierungen direkt in Shopify vor.

### Wie lösche ich meinen Shopify-Katalog? {#how-do-i-delete-my-shopify-catalog}

Um Ihren Shopify-Katalog zu löschen, deaktivieren Sie die Synchronisation auf der Shopify-Partnerseite. Löschen Sie den Katalog nicht direkt über die Seite **Kataloge**. Durch das Deaktivieren wird Ihr gesamter Katalog entfernt, einschließlich aller synchronisierten Tags, Kollektionen und Metafeld-Daten. Bevor Sie deaktivieren, aktualisieren oder pausieren Sie alle Campaigns oder Canvases, die auf diesen Katalog verweisen, da diese Nachrichten mit fehlenden Produktdetails senden könnten.

### Was passiert, wenn ich ein zuvor synchronisiertes Produkt oder Produktfeld in Shopify lösche? {#what-happens-if-i-delete-a-previously-synced-product-or-product-field-in-shopify}

Braze entfernt das Produkt oder Feld automatisch aus Ihrem Shopify-Katalog, sobald die Löschung erkannt wird. Allerdings werden alle Campaigns, Canvases oder Segments, die auf das gelöschte Produkt oder Feld verweisen, nicht mehr funktionieren. Stellen Sie vor dem Löschen von Produkten oder Feldern in Shopify sicher, dass diese nicht aktiv in Braze verwendet werden.

### Wie ändere ich meine Katalog-ID (Produktbezeichner)? {#how-do-i-change-my-catalog-id-product-identifier}

Um Ihre Katalog-ID zu ändern, deaktivieren Sie zunächst die Synchronisation und bestätigen Sie, dass keine aktiven Nachrichten auf diese Katalogdaten verweisen. Führen Sie dann die initiale Synchronisation erneut durch und wählen Sie den gewünschten Bezeichner aus.

### Wirkt sich eine Änderung meiner synchronisierten Tags, Kollektionen oder Metafelder auf aktive Campaigns aus? {#will-changing-my-synced-tags-collections-or-metafields-affect-active-campaigns}

Ja. Das Ändern Ihrer synchronisierten Auswahl kann sich auf aktive Campaigns, Canvases oder [Katalogselektionen]({{site.baseurl}}/catalog_selections) auswirken, die darauf verweisen. Überprüfen Sie, ob Ihre aktiven Inhalte aktualisiert sind, bevor Sie Änderungen vornehmen.

### Wie lange dauert die initiale Synchronisation? {#how-long-does-the-initial-sync-take}

Die Synchronisationsdauer hängt von der Anzahl der Produkte und Varianten in Ihrem Shop ab. Die initiale Synchronisation ruft Produkte in Batches ab, sodass es einige Zeit dauern kann, bis alle Produkt-Tags, Metafelder und Kollektionszuordnungen erscheinen. Überwachen Sie den Synchronisationsstatus auf der Shopify-Partnerseite.

## Konfiguration und Limits {#configuration-and-limits}

### Wie viele Tags, Sammlungen oder Metafields kann ich synchronisieren? {#how-many-tags-collections-or-metafields-can-i-sync}

Sie können bis zu 20 von jedem pro Konfiguration synchronisieren:

- Bis zu 20 Produkt-Tags
- Bis zu 20 Sammlungen
- Bis zu 20 Produkt-Metafields

### Was passiert, wenn ein Produkt zu mehr als 250 Sammlungen gehört? {#what-if-a-product-belongs-to-more-than-250-collections}

Shopify erlaubt es Produkten, zu mehr als 250 Sammlungen zu gehören, aber Braze kann nur die ersten 250 Sammlungszuordnungen pro Produkt abrufen. Wenn ein Produkt zu einer ausgewählten Sammlung gehört, die außerhalb der ersten 250 abgerufenen liegt, wird diese Zuordnung nicht in Ihrem Shopify-Katalog widergespiegelt. Wenn Ihnen fehlende Sammlungszuordnungen auffallen, wenden Sie sich an Ihren Customer-Success-Manager.

### Warum sehe ich nicht alle meine Sammlungen im Konfigurationsmodal? {#why-dont-i-see-all-my-collections-in-the-configuration-modal}

Das Konfigurationsmodal zeigt bis zu 5.000 der zuletzt aktualisierten Sammlungen an. Wenn Ihr Shop dieses Limit überschreitet, werden ältere Sammlungen möglicherweise nicht angezeigt. Zuvor ausgewählte Sammlungen, die außerhalb der Top 5.000 liegen, werden weiterhin in Ihrer Auswahl angezeigt.

### Kann ich in einer einzelnen Katalogauswahl sowohl nach Tags als auch nach Sammlungen filtern? {#can-i-filter-by-both-tags-and-collections-in-a-single-catalog-selection}

Nein. Katalogauswahlen unterstützen nur ein Array-Feld pro Auswahlfilter. Sie können Tags und Sammlungen nicht in derselben Auswahl kombinieren. Wenn Sie Nutzer:innen basierend auf sowohl Tag- als auch Sammlungskriterien ansprechen möchten, verwenden Sie stattdessen [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) mit SQL-Anfragen.

### Welche Limits gelten für Katalogauswahlen? {#what-are-the-catalog-selection-limits}

Für Katalogauswahlen gelten dieselben Limits wie für Standard-Katalogauswahlen. Einzelheiten zu Artikellimits, Filtereinschränkungen und stufenbasierten Speicherlimits finden Sie unter [Katalogauswahlen]({{site.baseurl}}/catalog_selections).

## Metafelder und Fehlerbehebung {#metafields-and-troubleshooting}

### Warum werden einige meiner Metafeldtypen nicht angezeigt? {#why-are-some-of-my-metafield-types-not-showing-up}

Im Konfigurationsmodal werden nur unterstützte Metafeldtypen angezeigt. Die folgenden Typen werden derzeit nicht unterstützt: `dimension`, `json`, `link`, `money`, `rating`, `rich_text_field`, `volume` und `weight`. Informationen zu unterstützten Typen und die vollständige Liste finden Sie unter [Shopify-Produkt-Metafelder]({{site.baseurl}}/shopify_catalogs#shopify-product-metafields) auf der Seite zur Shopify-Produktsynchronisierung.

### Ich habe den Fehler „Duplicate Metafield Column Name“ erhalten. Was soll ich tun? {#i-got-a-duplicate-metafield-column-name-error-what-do-i-do}

Zwei oder mehr Ihrer ausgewählten Metafelder würden denselben Spaltennamen im Katalog erzeugen. Deaktivieren Sie eines der in Konflikt stehenden Metafelder oder benennen Sie den Metafeld-Schlüssel in Shopify um, damit jedes Metafeld einem eindeutigen Spaltennamen zugeordnet wird. Speichern Sie anschließend Ihre Konfiguration erneut.

### Warum dauert das Laden meiner Tags länger als erwartet? {#why-are-my-tags-taking-longer-than-expected-to-load}

Tags werden direkt von Shopify abgerufen, wenn Sie das Konfigurationsmodal öffnen. Wenn Ihr Shop eine große Anzahl von Produkten oder Tags enthält, kann das Laden länger dauern. Dies ist ein erwartetes Verhalten und hat keinen Einfluss auf die Synchronisierungs-Performance. Wenn es wiederholt zu Zeitüberschreitungen kommt, versuchen Sie, die Gesamtanzahl der Tags in Ihrem Shopify-Shop zu reduzieren, oder wenden Sie sich an den Support.

## Speicher {#storage}

### Wirkt sich das Synchronisieren zusätzlicher Produktdaten auf meinen Katalogspeicher aus? {#will-syncing-additional-product-data-affect-my-catalog-storage}

Ja. Das Synchronisieren von Tags, Metafeldern und Sammlungen erhöht die Nutzung Ihres Katalogspeichers. Die kostenlose Katalogstufe hat ein Speicherlimit von 100 MB. Wenn Ihre Synchronisierung Ihr Limit überschreitet, stoppt Braze die Synchronisierung und Produktaktualisierungen werden nicht mehr übernommen. Wenden Sie sich an Ihren Account Manager, um bei Bedarf ein Upgrade Ihrer Stufe durchzuführen.