---
nav_title: Shopify-Produktsynchronisierung
article_title: Shopify-Produktsynchronisierung
alias: /shopify_catalogs/
page_order: 5
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre Produkte aus Shopify in Braze-Kataloge importieren."
---

# Shopify-Produktsynchronisierung {#shopify-product-sync}

> Sie können alle Produkte aus Ihrem Shopify-Shop mit einem Braze-[Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs) synchronisieren, um die Personalisierung von Nachrichten zu vertiefen.

Shopify-Kataloge werden nahezu in Realtime aktualisiert, wenn Sie die Produkte in Ihrem Shopify-Shop bearbeiten und ändern. Sie können Ihren Warenkorb-Abbruch, Ihre Bestellbestätigung und vieles mehr mit den aktuellsten Produktdetails und Informationen anreichern.

Zusätzlich zu den [grundlegenden Shopify-Produktdaten](#supported-shopify-catalog-data) können Sie Shopify-Kollektionen, Produkt-Tags und Produkt-Metafelder mit Ihrem Braze-Katalog synchronisieren. Diese zusätzlichen Felder ermöglichen eine umfangreichere Personalisierung, präzisere Katalogauswahlen und eine leistungsstärkere Segmentierung durch [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension).

## Shopify-Produktsynchronisierung einrichten {#set-up}

Wenn Sie Ihren Shopify-Shop bereits installiert haben, können Sie Ihre Produkte trotzdem synchronisieren, indem Sie die Anweisungen in diesem Abschnitt befolgen.

### Schritt 1: Synchronisierung einschalten {#step-1-turn-on-the-sync}

Sie können Ihre Produkte mit einem Braze-Katalog über den Shopify-Installationsablauf oder auf der Shopify-Partnerseite synchronisieren.

![Schritt 3 der Einrichtung mit „Shopify Variant ID“ als „Catalog product identifier“.]({% image_buster /assets/img/shopify/sync_products_step1.png %})

### Schritt 2: Produktbezeichner auswählen {#step-2-select-your-product-identifier}

Wählen Sie den primären Produktbezeichner aus, der als Braze-Katalog-ID verwendet werden soll:

- **Shopify Variant ID** ist ein guter Standard, wenn Ihre SKUs fehlen, über Varianten hinweg dupliziert sind oder Zeichen wie Schrägstriche, Punkte, Leerzeichen oder kaufmännische Und-Zeichen enthalten können. Varianten-IDs sind numerisch und erfüllen diese Anforderungen immer.
- **SKU** eignet sich gut, wenn jede Variante eine eindeutige SKU hat, die denselben Zeichenregeln wie die Shopify Variant ID folgt, und Sie Messaging oder Analytics mit Einzelhandels-SKUs als Katalogschlüssel verwenden möchten.
  - Sie können Freitext-SKUs, die unzulässige Zeichen enthalten, verwenden, indem Sie statt SKU die Shopify Variant ID nutzen.

Der von Ihnen gewählte Wert wird zur Katalog-`item_id` und darf nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten.

{% alert note %}
Wenn Sie SKU als Katalog-ID verwenden, stellen Sie sicher, dass alle Ihre Produkte und Varianten in Ihrem Shop eine SKU haben und diese eindeutig sind.<br><br>
- Wenn ein Artikel keine SKU hat, kann Braze dieses Produkt nicht mit dem Katalog synchronisieren.
- Wenn Sie mehr als ein Produkt mit der gleichen SKU haben, kann dies zu unerwartetem Verhalten führen oder Produktinformationen unbeabsichtigt überschreiben.
{% endalert %}

### Schritt 3: Zusätzliche Produktdaten konfigurieren (optional) {#step-3}

Sie können optional die Synchronisierung für Produkt-Tags, Shopify-Kollektionen und Metafelder aktivieren. Aktivieren oder ändern Sie diese Einstellungen nach der ersten Synchronisierung über die Shopify-Partnerseite.

{% alert note %}
Fügen Sie Produkt-Tags, Shopify-Kollektionen und Metafelder zuerst in Shopify hinzu. Wenn sie in Shopify nicht vorhanden sind, werden sie in Braze nicht angezeigt.
{% endalert %}

![Einstellungen zur Synchronisierung von Shopify-Produkten und -Varianten mit Braze.]({% image_buster /assets/img/shopify/additional_product_data.png %})

{% tabs global %}
{% tab Produkt-Tags %}

1. Aktivieren Sie auf der Seite **Sync product data to Braze** das Kontrollkästchen **Sync product tags**, um das Modal **Select product tags** zu öffnen.
2. Wählen Sie bis zu 20 Produkt-Tags aus, die mit Ihrem Braze-Katalog synchronisiert werden sollen. Nur die von Ihnen ausgewählten Tags werden synchronisiert.

![Modal zur Auswahl von Produkt-Tags mit einer Auswahl an Tags.]({% image_buster /assets/img/shopify/select_product_tags.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Produkt-Metafelder %}

1. Wenn Sie eine bestehende Shopify-Integration haben, autorisieren Sie die Braze Shopify-App erneut, um die neuen erforderlichen Berechtigungen für die Produktsynchronisierung zu installieren. Wenn Sie ein:e neue:r Kund:in sind, fahren Sie mit dem nächsten Schritt fort.

![Banner mit der Aufforderung, die Braze Shopify-App erneut zu autorisieren.]({% image_buster /assets/img/shopify/banner_to_reauthorize.png %})

{: start="2"}
2. Wählen Sie **Sync product metafields**, um das Konfigurationsmodal für Metafelder zu öffnen.

![Abschnitt „Sync product data to Braze“ mit Optionen zur Auswahl aus mehreren Einstellungen, einschließlich Kollektionen.]({% image_buster /assets/img/shopify/select_collections.png %})

{: start="3"}
3. Wählen Sie bis zu 20 der durchsuchbaren Metafelder zur Synchronisierung aus. Jedes wird zu einer separaten Spalte in Ihrem Katalog, die Sie in Features wie Katalogauswahlen oder Segmenterweiterungen verwenden können.
- Beachten Sie bei der Benennung von Metafeldern, dass Leerzeichen zu „_“ werden und alle Sonderzeichen entfernt werden, um den Benennungsbeschränkungen für Braze-Katalogfelder zu entsprechen.

![Modal zur Auswahl von Produkt-Metafeldern.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

{% subtabs %}
{% subtab Unterstützte Metafelder %}

Braze unterstützt die folgenden Metafeld-Objekte und einige ihrer jeweiligen Typen.

| Metafeld-Typ | Datentyp |
|--------------------------------------------------|--------------------------------------------------------|
| `boolean` | Boolescher Wert |
| `color`, `list.color` | String (Hex-Farbcode, z. B. `#FFF123`), String-Array |
| `date`, `list.date` | String (ISO-8601-Datum), String-Array (ISO-8601-Daten) |
| `date_time`, `list.date_time` | String (ISO-8601-Datetime), String-Array (ISO-8601-Datetimes) |
| `id`, `list.id` | String, String-Array |
| `multi_line_text_field` | String |
| `number_decimal` | String |
| `number_integer` | Integer |
| `single_line_text_field`, `list.single_line_text_field` | String, String-Array |
| `url`, `list.url` | String (URL), String-Array (URLs) |
| `metaobject_reference`, `list.metaobject_reference` | String, String-Array |
| `mixed_reference`, `list.mixed_reference` | String, String-Array |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Zusätzliche Produktdaten konfigurieren (optional)" }

{% endsubtab %}
{% subtab Nicht unterstützte Metafelder %}

Braze unterstützt keine Metafeld-Objekte, einschließlich einiger jeweiliger Listentypen:

- `dimension` (`list.dimension`)
- `weight` (`list.weight`)
- `link` (`list.link`)
- `json`
- `list.number_decimal`
- `list.number_integer`
- `money`
- `rating` (`list.rating`)
- `volume` (`list.volume`)
- `rich_text_field`

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Kollektionen %}

1. Wählen Sie **Sync Shopify collections**, um das Modal zur Einrichtung der Kollektionen zu öffnen.
2. Wählen Sie bis zu 20 Kollektionen zur Synchronisierung aus.
  - Das Modal bietet eine durchsuchbare Liste von bis zu 5.000 der zuletzt erstellten oder aktualisierten Kollektionen aus Ihrem Shopify-Shop.
  - Zuvor ausgewählte Kollektionen, die nicht mehr in den Top 5.000 sind, werden weiterhin in Ihrer Auswahl angezeigt.

{% alert note %}
Braze verwendet die Shopify-Kollektions-ID, um synchronisierte Kollektionen zu identifizieren, die dann beim Erstellen von Katalogauswahlen und Segment-Filtern verwendet werden.
{% endalert %}

![Modal zur Auswahl von Kollektionen aus einem Dropdown.]({% image_buster /assets/img/shopify/selected_collections.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{% alert tip %}
Beispiele zur Verwendung der einzelnen Produktdatentypen finden Sie unter [Anwendungsfälle für Shopify-Kataloge]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/?tab=shopify%20product%20metafields#shopify-catalog-use-cases).
{% endalert %}

### Schritt 4: Synchronisierungsfortschritt verfolgen {#step-4-track-your-sync-progress}

Nachdem Sie Ihre Konfiguration gespeichert haben, beginnt Braze mit der Synchronisierung Ihrer Produkte und aktualisiert den Status auf Ihrer Shopify-Partnerseite auf **In Progress**. Die Synchronisierungsdauer hängt von der Anzahl der Produkte und Varianten in Ihrem Shop ab.

Sie können die Seite verlassen, sobald die Synchronisierung läuft; Braze sendet Ihnen eine Dashboard-Benachrichtigung, wenn die Synchronisierung abgeschlossen ist. Nach Abschluss wird der Status auf **Active** aktualisiert, und Sie können Ihre Produkte anzeigen, indem Sie den Katalognamen auf Ihrer Shopify-Partnerseite auswählen.

![Seite mit Integrationseinstellungen und einem Status der Produktsynchronisierung.]({% image_buster /assets/img/shopify/track_sync_progress.png %})

Sie können auch synchronisierte Produkt-Tags, Metafelder und Kollektionen in Ihrem Shopify-Katalog als neue Spalten anzeigen.

![Shopify-Katalog mit synchronisierten Daten.]({% image_buster /assets/img/shopify/synced_catalog.png %})

{% alert important %}
Wenn Ihre Synchronisierung Ihr Katalogspeicherlimit überschreitet, stoppt Braze die Synchronisierung und neue Produkt-Updates werden nicht mehr berücksichtigt. Wenden Sie sich an Ihren Customer-Success-Manager, um bei Bedarf ein Upgrade Ihrer Stufe durchzuführen.
{% endalert %}

### Schritt 5: Konfiguration verwalten {#step-5-manage-your-configuration}

Jeder Synchronisierungstyp hat eine Übersichtskarte auf der Shopify-Partnerseite, die die Gesamtanzahl der synchronisierten Elemente, den aktuellen Status und einen Link zu Ihrem Katalog anzeigt. Wählen Sie das Ansichtssymbol, um Ihre aktive Konfiguration anzuzeigen und zu bearbeiten.

Sie können Ihre Shopify-Produktsynchronisierung jederzeit über die Shopify-Partnerseite ändern, einschließlich der Verwaltung Ihrer Produkt-Tags, Kollektionen und Produkt-Metafelder.

![Seite mit Integrationseinstellungen und einer aktiven Produkt-Katalogsynchronisierung.]({% image_buster /assets/img/shopify/active_catalog_sync.png %})

{% alert important %}
Das Ändern Ihrer synchronisierten Auswahlen kann sich auf aktive Campaigns, Canvases oder Katalogauswahlen auswirken, die darauf verweisen. Aktualisieren Sie aktive Inhalte, damit sie ordnungsgemäß funktionieren, wenn Sie die Änderungen übernehmen.
{% endalert %}

## Unterstützte Shopify-Katalogdaten {#supported-shopify-catalog-data}

| Feld | Datentyp | Beispiele |
|----------------------|----------------|-----------------------------------------------------------------------------------|
| `id` | String | `45264808411274` wenn der Katalog-Produktbezeichner **Shopify Variant ID** ist<br><br>`12345` wenn der Katalog-Produktbezeichner **SKU** ist (entspricht dem Wert, den Sie in [Schritt 2](#step-2-select-your-product-identifier) ausgewählt haben) |
| `store_name` | String | „your-store“ (Shopify-Shop-Subdomain, ohne `.myshopify.com`) |
| `shopify_product_id` | Zahl | `7939032613002` (als Zahl in Ihrem Braze-Katalog gespeichert; Shopify-APIs können diese ID als String zurückgeben) |
| `shopify_variant_id` | Zahl | `45264808411274` (als Zahl in Ihrem Braze-Katalog gespeichert; Shopify-APIs können diese ID als String zurückgeben) |
| `product_title` | String | „Classic leather jacket“ |
| `variant_title` | String | „Large / Red“, „Medium“ oder „Default Title“ für Produkte mit einer einzelnen Variante |
| `status` | String | „active“, „draft“, „archived“ |
| `product_image_url` | String | „https://cdn.shopify.com/s/files/1/0641/0970/7402/files/t_shir.jpg?v=1736538760“ |
| `variant_image_url` | String | Gleiche CDN-URL wie das Produktbild, wenn kein Variantenbild vorhanden ist; andernfalls eine variantenspezifische Bild-URL |
| `vendor` | String | „Flash and Thread“, „PantsLabyrinth“ |
| `product_type` | String | „Outerwear“, „T-Shirts“ (aus dem **Product type** des Produkts in Shopify) |
| `product_url` | String | „https://your-store.myshopify.com/products/classic-leather-jacket“ |
| `product_handle` | String | „classic-leather-jacket“ |
| `published_scope` | String | „web“, „global“ |
| `price` | Zahl | `10.00`, `24.99`<br><br>Shopify gibt Preise häufig als Strings zurück (z. B. `"199.00"` in der REST Admin API). Braze konvertiert sie für dieses Katalogfeld in Zahlen. |
| `compare_at_price` | Zahl | `15.00` wenn **Compare at price** in Shopify gesetzt ist<br><br>`0` wenn Shopify keinen Vergleichspreis hat. Shopify-APIs geben typischerweise `null` für einen nicht gesetzten Vergleichspreis zurück; Braze speichert `0` im Katalog, damit das Feld immer numerisch ist (dies ist ein Braze-Standardwert, kein Wert, den Shopify als `0` sendet). |
| `inventory_quantity` | Zahl | `20`, `0` oder ein negativer Wert, wenn Überverkauf erlaubt ist (z. B. `-18`) |
| `options` | String | „Size,Color“<br><br>Shopify erlaubt bis zu drei Optionstypen pro Produkt (z. B. Size, Color, Material). Der `options`-Wert ist eine kommagetrennte Liste dieser Namen. |
| `option_values` | String | „Medium,Red“, „Large,Red“<br><br>Jeder Wert entspricht der gleichen Reihenfolge wie `options` (bis zu drei Werte). |
| `sku` | String | „12345“, „SKU-001-RED-L“ |
| `product_tags` | Array | `["Summer", "Sale", "New"]`<br><br>Erfordert die Synchronisierung von Produkt-Tags. |
| `collection_ids` | Array | `[123456789012, 987654321098]` (Shopify-Kollektions-IDs)<br><br>Erfordert die Synchronisierung von Shopify-Kollektionen. |
| Metafeld-Spalten | Variiert je nach Typ | Jedes synchronisierte Metafeld erscheint als separate Spalte, benannt nach seinem Schlüssel. Informationen finden Sie unter [Unterstützte Metafelder](#step-3) im Tab „Produkt-Metafelder“ von Schritt 3. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Shopify-Katalogdaten" }

{% alert warning %}
Ihr Shopify-Katalog wird von Shopify verwaltet. Um Ihren Katalog zu aktualisieren, nehmen Sie Änderungen direkt in Ihrem Shopify-Shop vor, und sie werden automatisch mit Braze synchronisiert. Um Ihren Shopify-Katalog zu löschen, gehen Sie zur Shopify-Partnerseite in Braze und [deaktivieren Sie die Synchronisierung](#deactivate).
{% endalert %}

## Anwendungsfälle für Shopify-Kataloge {#shopify-catalog-use-cases}

Diese Anwendungsfälle zeigen, wie Sie Ihre synchronisierten Shopify-Katalogdaten zur Personalisierung von Nachrichten verwenden können.

{% alert warning %}
Braze synchronisiert bis zu 250 Varianten jedes Shopify-Produkts in Ihren Katalog. Varianten, die dieses Limit überschreiten, werden nicht synchronisiert. Wenn Sie mehr als 250 Varianten pro Produkt benötigen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

{% tabs %}
{% tab Produkt-Tags %}

Verwenden Sie Produkt-Tags, um Nachrichten basierend auf der Kategorisierung Ihrer Produkte in Shopify zu personalisieren. Sie können beispielsweise eine Aktion mit allen Produkten, die mit „Summer Sale“ getaggt sind, über eine [Katalogauswahl]({{site.baseurl}}/catalog_selections) versenden oder ein Segment von Nutzer:innen erstellen, die Produkte mit dem Tag „Premium“ gekauft haben.

Produkt-Tags werden als Array-Feld für jeden Katalogartikel gespeichert. Informationen zur Konfiguration der Produkt-Tag-Synchronisierung finden Sie unter [Shopify-Produkt-Tags](#shopify-product-tags).

### Katalogauswahl {#catalog-selection}

1. Vergeben Sie in Shopify den relevanten Produkten den Produkt-Tag „Women's“.

![Ein Produkttyp „Women's - Sweaters“ mit den Tags „Women's“, „Sweaters“ und „Men“.]({% image_buster /assets/img/shopify/product_tag_womens.png %}){: style="max-width:40%;"}

{: start="2"}
2. Aktivieren Sie in Braze die Tag-Synchronisierung und wählen Sie den Produkt-Tag „Women's“ aus.

![Modal zur Auswahl von Shopify-Produkt-Tags mit 15 ausgewählten bekleidungsbezogenen Tags, darunter „Women's“.]({% image_buster /assets/img/shopify/select_product_tags_womens.png %}){: style="max-width:80%;"}

### Personalisierung {#personalization}

{% alert note %}
Wenn Sie Produkt-Tags oder Kollektionen in Katalogauswahlen referenzieren, verwenden Sie nur den Wert selbst ohne die Array-Klammern `[]` oder Anführungszeichen `""`, die in den Katalogdaten erscheinen. Wenn ein Produkt-Tag beispielsweise als `["Women's"]` in Ihrem Katalog angezeigt wird, schreiben Sie `Women's` in Ihren Auswahlfilter.
{% endalert %}

1. Erstellen Sie eine Katalogauswahl, die nach Produkten mit dem jeweiligen Produkt-Tag filtert, z. B. „Women's“. Sie können nur ein eindeutiges Array-Feld innerhalb einer einzelnen Katalogauswahl verwenden und bis zu 50 Produkte in Ihrer Katalogauswahl.

![Eine Katalogauswahl, die nach Produkt-Tags mit dem Attribut „Women's“ filtert.]({% image_buster /assets/img/shopify/edit_product_tags_selection.png %})

{: start="2"}
2. Fügen Sie im Nachrichten-Editor die Auswahl dort ein, wo Sie die Produkte aus der Katalogauswahl mit dem Tag „Women's“ einbinden möchten. Sie könnten beispielsweise einen HTML-Produktblock wie diesen verwenden:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Wenn Sie bestimmte Produkte mit dem Tag „Women's“ in einer Push-Benachrichtigung erwähnen möchten, können Sie das Tool **Add Personalization** verwenden und Ihre Katalogartikel angeben.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Push-Benachrichtigungs-Editor mit einer Katalogauswahl, die drei Artikel mit einem Produkt-Tag einbindet.]({% image_buster /assets/img/shopify/add_personalization_product_tags.png %})

### Katalogsegmentierung (SQL) {#catalog-segmentation-sql}

Verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension), um Segmente basierend auf Nutzer:innen zu erstellen, die mit einem Produkt-Tag interagiert haben. Um beispielsweise Nutzer:innen zu finden, die mit Katalogartikeln interagiert haben, die einen bestimmten Produkt-Tag enthalten, verwenden Sie diese Abfrage:

{% raw %}
```liquid
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific product tag. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'product_tags' AND ARRAY_CONTAINS('<product_tag_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% tab Produkt-Metafelder %}

Verwenden Sie Produkt-Metafelder, um Nachrichten mit angepassten Produktdetails zu personalisieren, die über die Standardfelder von Shopify hinausgehen. Sie können beispielsweise Pflegehinweise in eine Bestellbestätigung einfügen, das Herkunftsland in einer Empfehlungs-E-Mail anzeigen oder Nutzer:innen segmentieren, die ein bestimmtes Material gekauft haben.

Jedes synchronisierte Metafeld wird zu einer separaten Spalte in Ihrem Katalog, wobei der Datentyp durch den Metafeld-Typ bestimmt wird. Informationen zur Einrichtung der Metafeld-Synchronisierung finden Sie unter [Shopify-Produkt-Metafelder](#shopify-product-metafields).

### Katalogauswahl

1. Setzen Sie in Shopify das Produkt-Metafeld `seasonal` bei den relevanten Produkten auf `summer` (dies ist ein Metafeld-Wert, kein Produkt-Tag).

![Modal zum Hinzufügen von Produkt-Metafeldern, einschließlich des Metafelds „seasonal“ mit dem Wert „summer“.]({% image_buster /assets/img/shopify/summer_product_metafield.png %}){: style="max-width:80%;"}

{: start="2"}
2. Aktivieren Sie in Braze die Metafeld-Synchronisierung und wählen Sie `custom.seasonal` (oder den Namespace und Schlüssel, die Ihrem Shopify-Metafeld entsprechen).

![Modal zur Auswahl von Produkt-Metafeldern mit einem erweiterten Dropdown, in dem vier Elemente ausgewählt sind, darunter „custom.seasonal“.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

### Personalisierung

1. Erstellen Sie eine [Katalogauswahl]({{site.baseurl}}/catalog_selections), die nach Metafeldern mit dem jeweiligen Wert filtert.

![Eine Katalogauswahl, die nach Metafeldern mit dem Attribut „summer“ filtert.]({% image_buster /assets/img/shopify/metafields_selection.png %})

{: start="2"}
2. Fügen Sie im Nachrichten-Editor die Auswahl dort ein, wo Sie Produkt-Metafelder einbinden möchten. Sie könnten beispielsweise einen HTML-Produktblock wie diesen verwenden:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Wenn Sie bestimmte Produkte mit einem bestimmten Metafeld-Wert in einer Push-Benachrichtigung erwähnen möchten, können Sie das Tool **Add Personalization** verwenden und Ihre Katalogartikel angeben.

{% raw %}
```liquid
Check out the latest summer products:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Push-Benachrichtigungs-Editor mit einer Katalogauswahl, die drei Artikel über eine metafeldbasierte Auswahl einbindet.]({% image_buster /assets/img/shopify/add_personalization_metafields.png %})

### Katalogsegmentierung (SQL)

Verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension), um Segmente basierend auf Nutzer:innen zu erstellen, die mit einem Produkt-Metafeld interagiert haben. Um beispielsweise Nutzer:innen zu finden, die ein E-Commerce-Event mit einem Produkt ausgelöst haben, dessen Metafeld-Array einen bestimmten Wert enthält, verwenden Sie diese Abfrage:

{% raw %}
```sql
-- -----------------------------------------------------------------------------
-- When the metafield is stored as a JSON array in catalog field_value (for example,
-- '["winter","summer"]' or a list-type Shopify metafield serialized to JSON),
-- use ARRAY_CONTAINS like product_tags. Cast the element you search for to
-- VARIANT so types match the parsed array elements.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product whose
-- metafield array contains a specific value (for example, segment on "seasonal").
-- For a date range, add events.time >= $start_date AND events.time <= $end_date.
-- For first/last triggered, reuse the CTE pattern from Template 3 with this
-- ARRAY_CONTAINS predicate instead of items.field_value = '<metafield_value>'.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND ARRAY_CONTAINS('<array_element_value>'::VARIANT, TRY_PARSE_JSON(items.field_value));
```
{% endraw %}

Wenn Sie Kund:innen segmentieren möchten, die eine Bestellung mit bestimmten Produkt-Metafeldern aufgegeben haben, verwenden Sie eines der folgenden SQL-Segmenterweiterungs-Templates (gesamter Zeitraum, bestimmter Zeitraum, erstes oder letztes Auslösen eines Events).

{% raw %}
```sql
-- =============================================================================
-- Segment Extension: Metafields × Ecommerce Events — Example SQL Templates
-- =============================================================================
-- Metafield column names in CATALOGS_ITEMS_SHARED follow:
--   field_name = 'metafield_<namespace>_<key>'
-- Replace placeholders: app_group_id, catalog_id, event name, and the metafield
-- field_name + value. For array-type metafield values, use ARRAY_CONTAINS
-- with TRY_PARSE_JSON(items.field_value) similar to the product_tags example.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Template 1: Map metafields to event triggers (all time)
-- -----------------------------------------------------------------------------
-- Users who have ever triggered the ecommerce event with a product that has
-- the given metafield value. Event-agnostic: change events.name for the
-- desired event (e.g. ecommerce.order_placed, ecommerce.product_viewed).
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who have engaged with catalog items that have a specific
-- product metafield. Joins the catalog to custom events by matching
-- events.properties.products (e.g. variant_id) to catalog items.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 2: Map metafields to event triggers (for a specific period)
-- -----------------------------------------------------------------------------
-- Same as Template 1, restricted to events within a time window. Use
-- $start_date and $end_date (Segment Extension parameters) or literal
-- Unix timestamps.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product that has
-- the given metafield value within the specified time range.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND events.time >= $start_date
    AND events.time <= $end_date
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 3: Map metafields — first or last triggered an event
-- -----------------------------------------------------------------------------
-- Users for whom the *first* (earliest) or *last* (most recent) matching
-- event (by time) involved a product with the given metafield. Switch
-- ORDER BY to time ASC for first, time DESC for last.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users whose first (or last) occurrence of the ecommerce event
-- involved a catalog item with the specified metafield value.
WITH events_with_catalog_metafield AS (
    SELECT
        events.user_id,
        events.time,
        events.id AS event_id,
        ROW_NUMBER() OVER (
            PARTITION BY events.user_id
            ORDER BY events.time ASC   -- use DESC for "last triggered"
        ) AS rn
    FROM
        USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
        LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
        JOIN CATALOGS_ITEMS_SHARED AS items ON (
            (
                items.field_name = 'id'
                AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
            items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
        )
    WHERE
        events.name = 'ecommerce.order_placed'
        AND events.app_group_id = '<app_group_id>'
        AND items.catalog_id = '<catalog_id>'
        AND items.field_name = '<metafield_name>'
        AND items.field_value = '<metafield_value>'
)
SELECT
    user_id
FROM
    events_with_catalog_metafield
WHERE
    rn = 1;
```
{% endraw %}

{% endtab %}
{% tab Kollektionen %}

Verwenden Sie Shopify-Kollektionen, um kuratierte Produktgruppierungen in Ihre Nachrichten einzubinden, die auch auf Ihrer Shopify-Website und in Ihren App-Erlebnissen verwendet werden. Sie können beispielsweise „Neuheiten“ in einer Werbe-E-Mail hervorheben, „Bestseller“ in einem Warenkorb-Abbruch-Canvas cross-sellen oder Nutzer:innen ansprechen, die eine saisonale Kollektion durchstöbert haben.

### Katalogauswahl

1. Erstellen Sie in Shopify eine Kollektion „New Women's Products - In Stock“ mit Ihren leistungsstärksten Produkten.

![Liste der Shopify-Kollektionen, einschließlich „New Women's Products - In Stock“.]({% image_buster /assets/img/shopify/shopify_collections.png %})

{: start="2"}
2. Aktivieren Sie in Braze die Kollektionssynchronisierung und wählen Sie „Women's Products - In Stock“.

![Modal zur Auswahl von Kollektionen mit einem erweiterten Dropdown, in dem vier Kollektionen ausgewählt sind.]({% image_buster /assets/img/shopify/select_collections_id.png %})

{% alert note %}
Für Shopify-Kollektionen müssen Sie die **Kollektions-ID** verwenden, die in der URL zu finden ist, wenn Sie die Kollektion anzeigen. Beispielsweise hat eine URL wie `https://admin.shopify.com/store/se-team-ecommerce/collections/470645342446` die Kollektions-ID `470645342446`.
{% endalert %}

### Personalisierung

{% alert note %}
Wenn Sie Kollektions-IDs in Katalogauswahlen referenzieren, verwenden Sie nur den numerischen ID-Wert ohne die Array-Klammern `[]`, die in den Katalogdaten erscheinen. Wenn Kollektions-IDs beispielsweise als `[123456789012, 987654321098]` in Ihrem Katalog angezeigt werden, schreiben Sie nur die numerische ID (z. B. `470645342446`) in Ihren Auswahlfilter.
{% endalert %}

1. Erstellen Sie eine Katalogauswahl mit dem Namen „New Women's Products - In Stock“, die nach Produkten mit der Kollektions-ID filtert. Sie können nur ein eindeutiges Array-Feld innerhalb einer einzelnen Katalogauswahl verwenden und bis zu 50 Produkte in Ihrer Kollektion.
 - Sie können auch eigene angepasste Auswahlen erstellen, indem Sie mit dem Feld **Collections** filtern.

![Eine Katalogauswahl, die nach Kollektionen mit dem Kollektions-ID-Attribut „470645342446“ filtert.]({% image_buster /assets/img/shopify/collections_selection.png %})

{: start="2"}
2. Binden Sie in Ihrer Nachricht Ihre Kollektion ein, indem Sie Ihre erstellte Auswahl verwenden oder die Kollektion direkt referenzieren. Sie könnten beispielsweise einen HTML-Produktblock wie diesen verwenden:

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
      {% if url == blank %}
      <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      {% else %}
      <a href="{{ url }}" style="text-decoration:none;">
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      </a>
      {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

Wenn Sie bestimmte neue Produkte in einer Push-Benachrichtigung erwähnen möchten, können Sie das Tool **Add Personalization** verwenden und Ihre Katalogartikel angeben.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Push-Benachrichtigungs-Editor mit einer Katalogauswahl, die drei Artikel mit einem Produkt-Tag einbindet.]({% image_buster /assets/img/shopify/add_personalization_collections.png %})

### Katalogsegmentierung (SQL)

Erstellen Sie ein Segment von Nutzer:innen, die mit einer Kollektion interagiert haben. Verwenden Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension), um Segmente basierend auf der Kollektionszugehörigkeit zu erstellen. Um beispielsweise Nutzer:innen zu finden, die im letzten Jahr Produkte aus einer bestimmten Kollektion gekauft haben, verwenden Sie diese Abfrage:

{% raw %}
```json
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific collection ID. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'collection_ids' AND ARRAY_CONTAINS('<collection_ids_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Sie können auch [Preissenkungsbenachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) und [Wieder-auf-Lager-Benachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) einrichten!<br><br> Beachten Sie, dass Sie für jeden Anwendungsfall ein angepasstes Event erstellen müssen, das den Abo-Status einer Nutzerin oder eines Nutzers in Ihrem Katalog erfasst. Für das angepasste Event benötigen Sie eine Event-Eigenschaft, die entweder der <a href="/docs/partners/ecommerce/shopify/shopify_catalogs#step-2-select-your-product-identifier">SKU oder der Shopify-Varianten-ID</a> zugeordnet ist, die Sie im Rahmen Ihrer Shopify-Produktsynchronisierung ausgewählt haben.
{% endalert %}

## Produktsynchronisierung deaktivieren {#deactivate}

Wenn Sie das Shopify-Feature zur Produktsynchronisierung deaktivieren, werden Ihr gesamter Katalog und Ihre Produkte gelöscht. Dies kann sich auch auf alle Nachrichten auswirken, die die Produktdaten dieses Katalogs aktiv nutzen. Vergewissern Sie sich, dass Sie diese Campaigns oder Canvases vor der Deaktivierung entweder aktualisiert oder pausiert haben, da dies dazu führen kann, dass Nachrichten ohne Produktangaben versendet werden. Löschen Sie den Shopify-Katalog nicht direkt auf der Katalogseite.

## Fehlerbehebung {#troubleshooting}

Wenn bei der Shopify-Produktsynchronisierung ein Fehler auftritt, kann dies auf die folgenden Fehler zurückzuführen sein. Folgen Sie den Anweisungen, um das Problem zu beheben und die Synchronisierung wiederherzustellen:

| Fehler | Grund | Lösung |
| --- | --- | --- |
| Server-Fehler | Dies tritt auf, wenn ein Server-Fehler auf Seiten von Shopify auftritt, wenn wir versuchen, Ihre Produkte zu synchronisieren. | [Deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Bestand an Produkten erneut. |
| Doppelte SKU | Dies tritt auf, wenn Sie SKU als Katalogartikel-ID verwenden und mehrere Varianten dieselbe SKU haben. Jede Katalog-`item_id` muss eindeutig sein, sodass betroffene Artikel möglicherweise nicht synchronisiert werden, Fehlerdatensätze ansammeln oder Produktinformationen unbeabsichtigt überschrieben werden. | Prüfen Sie Ihre vollständige Liste der Produkte und Varianten in Shopify, um sicherzustellen, dass es keine doppelten SKUs gibt. Wenn es doppelte SKUs gibt, aktualisieren Sie diese so, dass sie nur in Ihrem Shopify-Shop-Konto eindeutige SKUs sind. Nachdem das Problem behoben ist, [deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Bestand an Produkten erneut. |
| Katalog-Limit überschritten | Dies geschieht, wenn Sie Ihr Katalog-Limit überschreiten. Braze ist nicht in der Lage, die Synchronisierung zu beenden oder aktiv zu halten, da kein Speicherplatz mehr verfügbar ist. | Es gibt zwei Lösungen für dieses Problem:<br><br>1. Wenden Sie sich an Ihren Account Manager, um Ihre Stufe zu upgraden und Ihr Katalog-Limit zu erhöhen.<br><br>2. Geben Sie Speicherplatz frei, indem Sie Folgendes löschen:<br>- Katalogartikel aus anderen Katalogen<br>- Andere Kataloge<br>- Erstellte Auswahlen<br><br> Nachdem Sie eine der beiden Lösungen verwendet haben, müssen Sie die Synchronisierung deaktivieren und dann erneut synchronisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fehlerbehebung" }

Einzelheiten zur Validierung von Katalogartikeln finden Sie unter [Fehlerbehebung]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk#troubleshooting) in der Katalog-API-Dokumentation.