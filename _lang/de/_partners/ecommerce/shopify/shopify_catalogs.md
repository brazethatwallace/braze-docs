---
nav_title: Shopify Produkt-Synchronisation
article_title: Shopify Produkt-Synchronisation
alias: /shopify_catalogs/
page_order: 5
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre Produkte aus Shopify in Braze-Kataloge importieren."
---

# Shopify Produkt-Synchronisation {#shopify-product-sync}

> Sie können alle Produkte aus Ihrem Shopify Shop mit einem Braze-[Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) synchronisieren, um die Personalisierung von Nachrichten zu vertiefen.

Shopify-Kataloge werden nahezu in Realtime aktualisiert, wenn Sie die Produkte in Ihrem Shopify-Shop bearbeiten und ändern. Sie können Ihren Warenkorb-Abbruch, Ihre Bestellbestätigung und vieles mehr mit den aktuellsten Produktdetails und Informationen anreichern.

{% alert warning %}
Braze synchronisiert bis zu 250 Varianten jedes Shopify-Produkts in Ihren Katalog. Varianten, die dieses Limit überschreiten, werden nicht synchronisiert. Wenn Sie mehr als 250 Varianten pro Produkt benötigen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Einrichten der Shopify Produkt-Synchronisation {#setting-up}

Wenn Sie Ihren Shopify Shop bereits installiert haben, können Sie Ihre Produkte trotzdem synchronisieren, indem Sie die folgenden Anweisungen befolgen.

### 1. Schritt: Synchronisation einschalten {#step-1-turn-on-the-sync}

Sie können Ihre Produkte mit einem Braze-Katalog über den Shopify-Installationsablauf oder auf der Shopify-Partnerseite synchronisieren.

![Schritt 3 der Einrichtung mit „Shopify Variant ID“ als „Bezeichner für das Produkt im Katalog“.]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Produkte, die mit einem Braze-Katalog synchronisiert werden, tragen zu Ihrem [Katalog-Limit]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers) bei.

### 2. Schritt: Produktbezeichner auswählen {#step-2-select-your-product-identifier}

Wählen Sie den Produktbezeichner aus, der als Katalog-ID verwendet werden soll:
- Shopify-Varianten-ID
- SKU

Die ID- und Header-Werte für den von Ihnen gewählten Produktbezeichner dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. Wenn der Produktbezeichner nicht diesem Format entspricht, filtert Braze ihn aus Ihrer Katalogsynchronisierung heraus.

Dies ist der primäre Bezeichner, mit dem Sie die Kataloginformationen von Braze referenzieren.

{% alert note %}
Wenn Sie SKU als Katalog-ID auswählen, stellen Sie sicher, dass alle Produkte und Varianten in Ihrem Shop eine SKU haben und diese eindeutig sind.
- Wenn ein Artikel keine SKU hat, kann Braze dieses Produkt nicht mit dem Katalog synchronisieren.
- Wenn Sie mehr als ein Produkt mit der gleichen SKU haben, kann dies zu unerwartetem Verhalten führen oder dazu, dass die Produktinformationen unbeabsichtigt durch die doppelte SKU überschrieben werden.
{% endalert %}

### 3. Schritt: Synchronisierung läuft {#step-3-sync-in-progress}

Sie erhalten eine Dashboard-Benachrichtigung und Ihr Status wird als „In Bearbeitung“ angezeigt, um anzuzeigen, dass die erste Synchronisierung beginnt. Beachten Sie, dass die Dauer der Synchronisierung davon abhängt, wie viele Produkte und Varianten Braze von Shopify synchronisieren muss. Während dieser Zeit können Sie diese Seite verlassen und auf eine Dashboard-Benachrichtigung oder eine E-Mail warten, die Sie benachrichtigt, wenn der Vorgang abgeschlossen ist.

Beachten Sie, dass Braze keine weiteren Produkte mehr synchronisiert, wenn die erste Synchronisierung Ihr [Katalog-Limit]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers) überschreitet. Wenn Sie das Limit nach erfolgreicher Synchronisierung überschreiten, weil im Laufe der Zeit neue Produkte hinzukommen, wird die Synchronisierung nicht mehr aktiv sein. In beiden Fällen werden Produkt-Updates von Shopify nicht mehr in Braze angezeigt. Wenden Sie sich an Ihren Account Manager, um ein Upgrade Ihrer Stufe zu erwägen.

### 4. Schritt: Synchronisierung abgeschlossen {#step-4-sync-completed}

Sie erhalten eine Dashboard-Benachrichtigung und eine E-Mail, nachdem die Synchronisierung erfolgreich war. Auf der Shopify-Partnerseite wird außerdem der Status unter Shopify-Kataloge auf „Synchronisierung“ aktualisiert. Sie können sich Ihre Produkte ansehen, indem Sie auf der Shopify-Partnerseite auf den Katalognamen klicken.

Unter [Weitere Anwendungsfälle für Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/use/) erfahren Sie mehr darüber, wie Sie Katalogdaten zur Personalisierung Ihrer Nachrichten nutzen können.

#### Unterstützte Shopify-Katalogdaten {#supported-shopify-catalog-data}

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Wenn Sie den Shopify-Katalog in irgendeiner Weise ändern, kann dies die Realtime-Produktsynchronisierung unbeabsichtigt beeinträchtigen. Nehmen Sie keine Änderungen am Shopify-Katalog vor, da diese von Shopify überschrieben werden könnten. Nehmen Sie stattdessen die notwendigen Produkt-Updates in Ihrer Shopify-Instanz vor.<br><br>Um Ihren Shopify-Katalog zu löschen, gehen Sie auf die Shopify-Seite und deaktivieren Sie die Synchronisierung. Löschen Sie den Shopify-Katalog nicht direkt auf der Katalogseite.
{% endalert %}

## Anwendungsfälle für Back-in-Stock und Preissenkungen {#back-in-stock-and-price-drop-use-cases}

Um Benachrichtigungen über die Wiederverfügbarkeit von Artikeln einzurichten, folgen Sie den Schritten [hier]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/).

Um Benachrichtigungen über Preissenkungen einzurichten, folgen Sie den Schritten [hier]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/).

Beachten Sie, dass Sie bei der Shopify-Integration für jeden Anwendungsfall ein angepasstes Event erstellen müssen, das den Abo-Status einer Nutzerin oder eines Nutzers in Ihrem Katalog erfasst. Für das angepasste Event benötigen Sie eine Event-Eigenschaft, die entweder der [SKU oder der Shopify-Varianten-ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/#step-2-select-your-product-identifier) zugeordnet ist, die Sie im Rahmen Ihrer Shopify Produkt-Synchronisation ausgewählt haben.

## Ändern der Katalog-ID {#changing-catalog-id}

Um den Produktbezeichner für Ihren Shopify-Katalog zu ändern, müssen Sie die Synchronisierung deaktivieren. Vergewissern Sie sich zunächst, dass Sie keine Nachrichten mehr mit diesen Shopify-Katalogdaten versenden. Führen Sie die erste Synchronisierung des Shopify-Katalogs erneut durch und wählen Sie den gewünschten Produktbezeichner aus, indem Sie die Schritte zur [Produkt-Synchronisation](#setting-up) befolgen.

## Deaktivieren der Produkt-Synchronisation {#deactivate}

Wenn Sie das Shopify-Feature zur Produkt-Synchronisation deaktivieren, werden Ihr gesamter Katalog und Ihre Produkte gelöscht. Dies kann sich auch auf alle Nachrichten auswirken, die die Produktdaten dieses Katalogs aktiv nutzen. Vergewissern Sie sich, dass Sie diese Campaigns oder Canvases vor der Deaktivierung entweder aktualisiert oder pausiert haben, da dies dazu führen kann, dass Nachrichten ohne Produktangaben versendet werden. Löschen Sie den Shopify-Katalog nicht direkt auf der Katalogseite.

## Fehlerbehebung {#troubleshooting}
Wenn bei der Shopify Produkt-Synchronisation ein Fehler auftritt, kann dies auf die folgenden Fehler zurückzuführen sein. Folgen Sie den Anweisungen, um das Problem zu beheben und die Synchronisierung wiederherzustellen:

| Fehler | Grund | Lösung |
| --- | --- | --- |
| Server-Fehler | Dies tritt auf, wenn ein Server-Fehler auf Seiten von Shopify auftritt, wenn wir versuchen, Ihre Produkte zu synchronisieren. | [Deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Bestand an Produkten erneut. |
| Doppelte SKU | Dies tritt auf, wenn Sie eine SKU als ID für Ihren Katalogartikel verwenden und Produkte mit der gleichen SKU haben. Da die ID des Katalogartikels eindeutig sein muss, müssen alle Ihre Produkte eindeutige SKUs haben. | Prüfen Sie Ihre vollständige Liste der Produkte und Varianten in Shopify, um sicherzustellen, dass es keine doppelten SKUs gibt. Wenn es doppelte SKUs gibt, aktualisieren Sie diese so, dass sie nur in Ihrem Shopify-Konto eindeutige SKUs sind. Nachdem das Problem behoben ist, [deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Bestand an Produkten erneut. |
| Katalog-Limit überschritten | Dies geschieht, wenn Sie Ihr Katalog-Limit überschreiten. Braze ist nicht in der Lage, die Synchronisierung zu beenden oder aktiv zu halten, da kein Speicherplatz mehr verfügbar ist. | Es gibt zwei Lösungen für dieses Problem:<br><br>1. Wenden Sie sich an Ihren Account Manager, um Ihre Stufe zu upgraden und Ihr Katalog-Limit zu erhöhen. <br><br>2. Geben Sie Speicherplatz frei, indem Sie Folgendes löschen:<br>- Katalogartikel aus anderen Katalogen<br>- Andere Kataloge<br>- Erstellte Auswahlen<br><br> Nachdem Sie eine der beiden Lösungen verwendet haben, müssen Sie die Synchronisierung deaktivieren und dann erneut synchronisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }