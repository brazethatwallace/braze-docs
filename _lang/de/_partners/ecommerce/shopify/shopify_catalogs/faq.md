---
nav_title: FAQ
article_title: FAQ zur Shopify-Produktsynchronisierung
page_order: 0
page_type: FAQ
description: "Diese Seite enthält Antworten auf häufig gestellte Fragen zur Synchronisierung von Shopify-Produkten mit Braze-Katalogen."
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Diese Seite enthält Antworten auf einige häufig gestellte Fragen zur [Shopify-Produktsynchronisierung]({{site.baseurl}}/shopify_catalogs/).

## Katalog- und Synchronisierungsverhalten {#catalog-and-sync-behavior}

### Kann ich meinen Shopify-Katalog direkt in Braze bearbeiten? {#can-i-edit-my-shopify-catalog-directly-in-braze}

Nein. Der Shopify-Katalog ist in Braze schreibgeschützt. Manuelle Änderungen können bei der nächsten Synchronisierung überschrieben werden. Nehmen Sie alle Produktaktualisierungen direkt in Shopify vor.

### Wie lösche ich meinen Shopify-Katalog? {#how-do-i-delete-my-shopify-catalog}

Um Ihren Shopify-Katalog zu löschen, deaktivieren Sie die Synchronisierung auf der Shopify-Partnerseite. Löschen Sie den Katalog nicht direkt über die Seite **Catalogs**. Durch die Deaktivierung wird Ihr gesamter Katalog entfernt, einschließlich aller synchronisierten Tags, Kollektionen und Metafeld-Daten. Bevor Sie die Synchronisierung deaktivieren, aktualisieren oder pausieren Sie alle Campaigns oder Canvases, die auf diesen Katalog verweisen, da diese möglicherweise Nachrichten mit fehlenden Produktdetails senden.

### Was passiert, wenn ich ein zuvor synchronisiertes Produkt oder Produktfeld in Shopify lösche? {#what-happens-if-i-delete-a-previously-synced-product-or-product-field-in-shopify}

Braze entfernt das Produkt oder Feld automatisch aus Ihrem Shopify-Katalog, sobald die Löschung erkannt wird. Allerdings werden alle Campaigns, Canvases oder Segmente, die auf das gelöschte Produkt oder Feld verweisen, fehlerhaft. Überprüfen Sie vor dem Löschen von Produkten oder Feldern in Shopify, ob diese nicht aktiv in Braze verwendet werden.

### Wie ändere ich meine Katalog-ID (Produktbezeichner)? {#how-do-i-change-my-catalog-id-product-identifier}

Um Ihre Katalog-ID zu ändern, deaktivieren Sie zunächst die Synchronisierung und stellen Sie sicher, dass keine aktiven Nachrichten auf diese Katalogdaten verweisen. Führen Sie dann die initiale Synchronisierung erneut durch und wählen Sie den gewünschten Bezeichner aus.

### Wirkt sich eine Änderung meiner synchronisierten Tags, Kollektionen oder Metafelder auf aktive Campaigns aus? {#will-changing-my-synced-tags-collections-or-metafields-affect-active-campaigns}

Ja. Änderungen an Ihren synchronisierten Auswahlen können sich auf aktive Campaigns, Canvases oder [Katalogauswahlen]({{site.baseurl}}/catalog_selections/) auswirken, die darauf verweisen. Stellen Sie sicher, dass Ihre aktiven Inhalte aktualisiert sind, bevor Sie Änderungen vornehmen.

### Wie lange dauert die initiale Synchronisierung? {#how-long-does-the-initial-sync-take}

Die Synchronisierungsdauer hängt von der Anzahl der Produkte und Varianten in Ihrem Shop ab. Die initiale Synchronisierung ruft Produkte in Stapeln ab, sodass es einige Zeit dauern kann, bis alle Produkt-Tags, Metafelder und Kollektionszuordnungen angezeigt werden. Überwachen Sie den Synchronisierungsstatus auf der Shopify-Partnerseite.

## Konfiguration und Limits {#configuration-and-limits}

### Wie viele Tags, Kollektionen oder Metafelder kann ich synchronisieren? {#how-many-tags-collections-or-metafields-can-i-sync}

Sie können bis zu 20 pro Konfiguration synchronisieren:

- Bis zu 20 Produkt-Tags
- Bis zu 20 Kollektionen
- Bis zu 20 Produkt-Metafelder

### Was passiert, wenn ein Produkt zu mehr als 250 Kollektionen gehört? {#what-if-a-product-belongs-to-more-than-250-collections}

Shopify erlaubt es, dass Produkte zu mehr als 250 Kollektionen gehören, aber Braze kann nur die ersten 250 Kollektionszuordnungen pro Produkt abrufen. Wenn ein Produkt zu einer ausgewählten Kollektion gehört, die außerhalb der ersten 250 abgerufenen liegt, wird diese Zuordnung nicht in Ihrem Shopify-Katalog widergespiegelt. Wenn Ihnen fehlende Kollektionszuordnungen auffallen, wenden Sie sich an Ihren Customer-Success-Manager.

### Warum sehe ich nicht alle meine Kollektionen im Konfigurationsmodal? {#why-dont-i-see-all-my-collections-in-the-configuration-modal}

Das Konfigurationsmodal zeigt bis zu 5.000 der zuletzt aktualisierten Kollektionen an. Wenn Ihr Shop dieses Limit überschreitet, werden ältere Kollektionen möglicherweise nicht angezeigt. Zuvor ausgewählte Kollektionen, die außerhalb der Top 5.000 liegen, werden weiterhin in Ihrer Auswahl angezeigt.

### Kann ich in einer einzelnen Katalogauswahl nach Tags und Kollektionen gleichzeitig filtern? {#can-i-filter-by-both-tags-and-collections-in-a-single-catalog-selection}

Nein. Katalogauswahlen unterstützen nur ein Array-Feld pro Auswahlfilter. Sie können Tags und Kollektionen nicht in derselben Auswahl kombinieren. Wenn Sie Nutzer:innen basierend auf Tag- und Kollektionskriterien ansprechen möchten, verwenden Sie stattdessen [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) mit SQL-Anfragen.

### Welche Limits gelten für Katalogauswahlen? {#what-are-the-catalog-selection-limits}

Für Katalogauswahlen gelten dieselben Limits wie für Standard-Katalogauswahlen. Details zu Artikellimits, Filterbeschränkungen und stufenbasierten Speichergrenzen finden Sie unter [Katalogauswahlen]({{site.baseurl}}/catalog_selections/).

## Metafelder und Fehlerbehebung {#metafields-and-troubleshooting}

### Warum werden einige meiner Metafeldtypen nicht angezeigt? {#why-are-some-of-my-metafield-types-not-showing-up}

Im Konfigurationsmodal werden nur unterstützte Metafeldtypen angezeigt. Die folgenden Typen werden derzeit nicht unterstützt: `dimension`, `json`, `link`, `money`, `rating`, `rich_text_field`, `volume` und `weight`. Informationen zu unterstützten Typen und die vollständige Liste finden Sie unter [Shopify-Produkt-Metafelder]({{site.baseurl}}/shopify_catalogs/#shopify-product-metafields) auf der Seite zur Shopify-Produktsynchronisierung.

### Ich habe den Fehler „Duplicate Metafield Column Name“ erhalten. Was soll ich tun? {#i-got-a-duplicate-metafield-column-name-error-what-do-i-do}

Zwei oder mehr Ihrer ausgewählten Metafelder würden denselben Spaltennamen im Katalog erzeugen. Deselektieren Sie eines der in Konflikt stehenden Metafelder oder benennen Sie den Metafeld-Schlüssel in Shopify um, sodass jedes Feld einem eindeutigen Spaltennamen zugeordnet wird. Speichern Sie dann Ihre Konfiguration erneut.

### Warum dauert das Laden meiner Tags länger als erwartet? {#why-are-my-tags-taking-longer-than-expected-to-load}

Tags werden direkt von Shopify abgerufen, wenn Sie das Konfigurationsmodal öffnen. Wenn Ihr Shop eine große Anzahl von Produkten oder Tags hat, kann das Laden länger dauern. Dies ist ein erwartetes Verhalten und beeinträchtigt nicht die Synchronisierungsleistung. Wenn das Laden regelmäßig zu Zeitüberschreitungen führt, versuchen Sie, die Gesamtzahl der Tags in Ihrem Shopify-Shop zu reduzieren, oder wenden Sie sich an den Support.

## Speicher {#storage}

### Wirkt sich die Synchronisierung zusätzlicher Produktdaten auf meinen Katalogspeicher aus? {#will-syncing-additional-product-data-affect-my-catalog-storage}

Ja. Die Synchronisierung von Tags, Metafeldern und Kollektionen erhöht Ihre Katalogspeichernutzung. Die kostenlose Katalogstufe hat ein Speicherlimit von 100 MB. Wenn Ihre Synchronisierung Ihr Limit überschreitet, stoppt Braze die Synchronisierung und Produktaktualisierungen werden nicht mehr widergespiegelt. Wenden Sie sich an Ihren Account Manager, um bei Bedarf Ihre Stufe zu upgraden.