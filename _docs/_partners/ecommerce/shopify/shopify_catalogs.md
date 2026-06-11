---
nav_title: Shopify Product Sync
article_title: Shopify Product Sync
alias: /shopify_catalogs/
page_order: 5
description: "This reference article covers how to import your products from Shopify into Braze catalogs."
---

# Shopify product sync 

> You can sync all products from your Shopify store to a Braze [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs) for deeper messaging personalization. 

Shopify catalogs will update in near real-time as you make edits and changes to the products in your Shopify store. You can enrich your abandoned cart, order confirmation, and more with the most up-to-date product details and information.

In addition to supporting [core Shopify product data](#supported-shopify-catalog-data), you can sync Shopify collections, product tags, and product metafields to your Braze catalog. These additional fields unlock richer personalization, more precise catalog selections, and more powerful segmentation through [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/).

## Set up your Shopify product sync {#set-up}

If you have already installed your Shopify store, you can still sync your products by following the instructions below. 

### Step 1: Turn on the sync

You can sync your products to a Braze catalog through the Shopify install flow or on the Shopify partner page. 

![Step 3 of the set up process with "Shopify Variant ID" as the "Catalog product identifier".]({% image_buster /assets/img/shopify/sync_products_step1.png %})

### Step 2: Select your product identifier

Select what product identifier to use as the catalog ID:
- Shopify Variant ID
- SKU

The ID and header values for the product identifier you choose can only include letters, numbers, hyphens, and underscores. If the product identifier doesn't follow this format, Braze will filter it out of your catalog sync.

This will be the primary identifier you use to reference Braze catalog information. 

{% alert note %}
If you are selecting SKU as your catalog ID, make sure that all your products and variants in your store have a SKU set and they are unique.<br><br>  
- If an item has a missing SKU, Braze cannot sync that product into the catalog.
- If you have more than one product with the same SKU, this can cause unexpected behavior or result in product information being overridden unintentionally by the duplicate SKU.
{% endalert %}

### Step 3: Configure additional product data (optional) {#step-3}

You can optionally enable syncing for product tags, Shopify Collections, and metafields. Enable or modify these settings after the initial sync from the Shopify partner page. 

{% alert note %}
Add product tags, Shopify Collections, and metafields in Shopify first. If they do not exist in Shopify, they will not appear in Braze.
{% endalert %}

![Settings to sync Shopify products and variants to Braze.]({% image_buster /assets/img/shopify/additional_product_data.png %})

{% tabs global %}
{% tab Product tags %}

1. On the **Sync product data to Braze** page, select the **Sync product tags** checkbox to open the **Select product tags** modal. 
2. Select up to 20 product tags to sync to your Braze catalog. Only the tags you select will be synced.

![Select product tags modal with a selection of tags.]({% image_buster /assets/img/shopify/select_product_tags.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Product metafields %}

1. If you have an existing Shopify integration, reauthorize the Braze Shopify app to install new required scopes to sync products. If you're a new customer, go to the next step.

![Banner saying to reauthorize the Braze Shopify app.]({% image_buster /assets/img/shopify/banner_to_reauthorize.png %})

{: start="2"}
2. Select **Sync product metafields** to open the metafield configuration modal. 

![Sync product data to Braze section with options to select from multiple settings, including collections.]({% image_buster /assets/img/shopify/select_collections.png %})

{: start="3"}
3. Select up to 20 of the searchable metafields to sync. Each becomes a separate column in your catalog to use in features like Catalog Selections or Segment Extensions. 
- When naming metafields, note that spaces become "_" and all special characters are removed to account for Braze catalog field naming restrictions.

![Modal to select product metafields.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

{% subtabs %}
{% subtab Supported metafields %}

Braze supports the following metafield objects some of their respective types. 

| Metafield type                                   | Data type                                              |
|--------------------------------------------------|--------------------------------------------------------|
| `boolean`                                        | Boolean                                                |
| `color`, `list.color`                            | String (hex color, such as `#FFF123`), Array of Strings|
| `date`, `list.date`                              | String (ISO 8601 date), Array of Strings (ISO 8601 dates)|
| `date_time`, `list.date_time`                    | String (ISO 8601 datetime), Array of Strings (ISO 8601 datetimes)|
| `id`, `list.id`                                  | String, Array of Strings                               |
| `multi_line_text_field`                          | String                                                 |
| `number_decimal`                                 | String                                                 |
| `number_integer`                                 | Integer                                                |
| `single_line_text_field`, `list.single_line_text_field` | String, Array of Strings                        |
| `url`, `list.url`                                | String (URL), Array of Strings (URLs)                  |
| `metaobject_reference`, `list.metaobject_reference` | String, Array of Strings                          |
| `mixed_reference`, `list.mixed_reference`        | String, Array of Strings                               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Configure additional product data (optional) #step-3" }

{% endsubtab %}
{% subtab Unsupported metafields %}

Braze does not support metafield objects, including some respective list types:

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
{% tab Collections %}

1. Select **Sync Shopify collections** to open the collection setup modal.
2. Select up to 20 collections to sync. 
  - The modal provides a searchable list of up to 5,000 of the most recently created or updated collections from your Shopify store. 
  - Previously selected collections that are no longer in the top 5,000 will still appear in your selection.

{% alert note %}
Braze uses the Shopify Collection ID to identify synced collections, which are then used when building Catalog selections and segment filters. 
{% endalert %}

![Modal to select collections from a dropdown.]({% image_buster /assets/img/shopify/selected_collections.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{% alert tip %}
For examples of how to use each product data type, see [Shopify catalog use cases]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/?tab=shopify%20product%20metafields#shopify-catalog-use-cases)
{% endalert %}

### Step 4: Track your sync progress

After saving your configuration, Braze will begin syncing your products and update the status to **In Progress** on your Shopify partner page. The sync time depends on the number of products and variants in your store.

You can leave the page once the sync is in progress; Braze sends you a dashboard notification when the sync completes. After the completion, the status updates to **Active** and you can view your products by selecting the catalog name on your Shopify partner page.

![Integration settings page with a product sync status.]({% image_buster /assets/img/shopify/track_sync_progress.png %})

You can also view synced product tags, metafields, and collections within your Shopify catalog as new columns. 

![Shopify catalog with synced data.]({% image_buster /assets/img/shopify/synced_catalog.png %})

{% alert important %}
If your sync exceeds your catalog storage limit, Braze stops syncing and new product updates are no longer reflected. Contact your customer success manager to upgrade your tier if needed.
{% endalert %}

### Step 5: Manage your configuration 

Each sync type has a summary card on the Shopify partner page showing the total count synced, current status, and a link to your catalog. Select the view icon to view your active configuration and edit it.

You can modify your Shopify product sync, including managing your product tags, collections, and product metafields at any time from the Shopify partner page.

![Integration settings pag with an active product catalog sync.]({% image_buster /assets/img/shopify/active_catalog_sync.png %})

{% alert important %}
Changing your synced selections may affect active campaigns, Canvases, or catalog selections that reference them. Update active content so they work properly when you apply the changes.
{% endalert %}

## Supported Shopify catalog data

| Field                | Data type       | Examples                                                                   |
|----------------------|----------------|-----------------------------------------------------------------------------------|
| `id`                 | string         | `45264808411274` when the catalog product identifier is **Shopify Variant ID**<br><br>`12345` when the catalog product identifier is **SKU** (matches the value you selected in [Step 2](#step-2-select-your-product-identifier)) |
| `store_name`         | string         | "your-store" (Shopify store subdomain, without `.myshopify.com`)                |
| `shopify_product_id` | number         | `7939032613002` (stored as a number in your Braze catalog; Shopify APIs may return this ID as a string) |
| `shopify_variant_id` | number         | `45264808411274` (stored as a number in your Braze catalog; Shopify APIs may return this ID as a string) |
| `product_title`      | string         | "Classic leather jacket"                                                      |
| `variant_title`      | string         | "Large / Red", "Medium", or "Default Title" for single-variant products     |
| `status`             | string         | "active", "draft", "archived"                                                     |
| `product_image_url`  | string         | "https://cdn.shopify.com/s/files/1/0641/0970/7402/files/t_shir.jpg?v=1736538760" |
| `variant_image_url`  | string         | Same CDN-style URL as the product image when no variant image exists; otherwise a variant-specific image URL |
| `vendor`             | string         | "Flash and Thread", "PantsLabyrinth"                                            |
| `product_type`       | string         | "Outerwear", "T-Shirts" (from the product’s **Product type** in Shopify)      |
| `product_url`        | string         | "https://your-store.myshopify.com/products/classic-leather-jacket"            |
| `product_handle`     | string         | "classic-leather-jacket"                                                          |
| `published_scope`    | string         | "web", "global"                                                                   |
| `price`              | number         | `10.00`, `24.99`<br><br>Shopify often returns prices as strings (for example `"199.00"` in the REST Admin API). Braze converts them to numbers for this catalog field. |
| `compare_at_price`   | number         | `15.00` when **Compare at price** is set in Shopify<br><br>`0` when Shopify has no compare-at price. Shopify APIs typically return `null` for an unset compare-at price; Braze stores `0` in the catalog so the field is always numeric (this is a Braze default, not a value Shopify sends as `0`). |
| `inventory_quantity` | number         | `20`, `0`, or a negative value when overselling is allowed (for example `-18`)   |
| `options`            | string         | "Size,Color"<br><br>Shopify allows up to three option types per product (for example Size, Color, Material). The `options` value is a comma-separated list of those names. |
| `option_values`      | string         | "Medium,Red", "Large,Red"<br><br>Each value maps to the same order as `options` (up to three values). |
| `sku`                | string         | "12345", "SKU-001-RED-L"                                                    |
| `product_tags`       | array          | `["Summer", "Sale", "New"]`<br><br>Requires product tag syncing.                 |
| `collection_ids`     | array          | `[123456789012, 987654321098]` (Shopify collection IDs)<br><br>Requires Shopify collection syncing. |
| `Metafield columns`  | Varies by type | Each synced metafield appears as a separate column named by its key. See [Supported metafields](#step-3) in the "Product metafields" tab of step 3 for information. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported Shopify catalog data" }

{% alert warning %}
Your Shopify catalog is managed by Shopify. To update your catalog, make changes directly in your Shopify store, and they will automatically sync to Braze. To delete your Shopify catalog, go to the Shopify partner page in Braze and [deactivate the sync](#deactivate).
{% endalert %}

## Shopify catalog use cases

These use cases show how you can use your synced Shopify catalog data to personalize messages.

{% alert warning %}
Braze syncs up to 250 variants of each Shopify product into your catalog. Variants beyond that limit are not synced. If you need more than 250 variants per product, contact your Braze customer success manager.
{% endalert %}

{% tabs %}
{% tab Product tags %}

Use product tags to personalize messages based on how your products are categorized in Shopify. For example, you can send a promotion featuring all products tagged "Summer Sale" through a [catalog selection]({{site.baseurl}}/catalog_selections/), or build a segment of users who purchased products tagged "Premium." 

Product tags are stored as an array field on each catalog item. To configure product tag syncing, see [Shopify product tags](#shopify-product-tags).

### Catalog selection

1. In Shopify, give relevant products in Shopify the product tag of "Women's".

![A product type of "Women's - Sweaters" with the tags of "Women's", "Sweaters", and "Men".]({% image_buster /assets/img/shopify/product_tag_womens.png %}){: style="max-width:40%;"}

{: start="2"}
2. In Braze, enable tag syncing and select the "Women's" product tag.

![Modal to select Shopify product tags, with 15 clothing-related tags selected, including "Women's".]({% image_buster /assets/img/shopify/select_product_tags_womens.png %}){: style="max-width:80%;"}

### Personalization

1. Create a catalog selection that filters for products that have the respective product tag, such as "Women's". You can only use one unique array field within a single catalog selection, and up to 50 products in your catalog selection.

![A catalog selection that filters for product tags that have the attribute "Women's".]({% image_buster /assets/img/shopify/edit_product_tags_selection.png %})

{: start="2"}
2. In the message composer, add the selection where you want to template in the products from the catalog selection that are tagged with "Women's". For example, you could use an HTML product block like this:

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

Or, if you want to mention specific products tagged with "Women's" in a push notification, you can use the **Add Personalization** tool and specify your catalog items.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Push notification composer with a catalog selection pulling in three items with a product tag.]({% image_buster /assets/img/shopify/add_personalization_product_tags.png %})

### Catalog segmentation (SQL) 

Use [Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) to build segments based on users who interacted with a product tag. For example, to find users who have engaged with catalog items that contain a specific product tag, use this query:

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
{% tab Product metafields %}

Use product metafields to personalize messages with custom product details beyond Shopify's standard fields. For example, include care instructions in an order confirmation, display country of origin in a recommendation email, or segment users who purchased a specific material.

Each synced metafield becomes a separate column in your catalog, with data type determined by the metafield type. To set up metafield syncing, see [Shopify product metafields](#shopify-product-metafields).

### Catalog selection

1. In Shopify, set the `seasonal` product metafield on relevant products to `summer` (this is a metafield value, not a product tag).

![Modal to add product metafields, including metafield seasonal with value summer.]({% image_buster /assets/img/shopify/summer_product_metafield.png %}){: style="max-width:80%;"}

{: start="2"}
2. In Braze, enable metafield syncing and select `custom.seasonal` (or the namespace and key that match your Shopify metafield).

![Modal to select product metafields, with an expanded dropdown that has four items selected, including custom.seasonal.]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

### Personalization

1. Create a [catalog selection]({{site.baseurl}}/catalog_selections/) that filters for metafields that include the respective value.

![A catalog selection that filters for metafields that have the attribute summer.]({% image_buster /assets/img/shopify/metafields_selection.png %})

{: start="2"}
2. In the message composer, add the selection where you want to template in product metafields. For example, you could use an HTML product block like this: 

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

Or, if you want to mention specific products with a specific metafield value in a push notification, you can use the **Add Personalization** tool and specify your catalog items.

{% raw %}
```liquid
Check out the latest summer products:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Push notification composer with a catalog selection pulling in three items using a metafield-based selection.]({% image_buster /assets/img/shopify/add_personalization_metafields.png %})

### Catalog segmentation (SQL) 

Use [Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) to build segments based on users who interacted with a product metafield. For example, to find users who triggered an ecommerce event with a product whose metafield array contains a specific value, use this query:

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

If you want to segment customers who have placed an order with the specific product metafields, use one of the following SQL Segment Extension templates (all time, specific time period, first or last triggered an event).

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
{% tab Collections %}

Use Shopify collections to pull curated product groupings into your messages that are also used on your Shopify site and app experiences. For example, feature "New Arrivals" in a promotional email, cross-sell "Best Sellers" in an abandoned cart Canvas, or target users who browsed a seasonal collection.

### Catalog selection

1. In Shopify, create a "New Women's Products - In Stock" collection with your top-performing products.

![List of Shopify collections, including "New Women's Products - In Stock".]({% image_buster /assets/img/shopify/shopify_collections.png %})

{: start="2"}
2. In Braze, enable collection syncing and select "Women's Products - In Stock".

![Modal to select collections, with an extended dropdown that selects four collections.]({% image_buster /assets/img/shopify/select_collections_id.png %})

{% alert note %}
For Shopify collections, you must use the **Collection ID**, which is found in the URL when you view the collection. For example, a URL of `https://admin.shopify.com/store/se-team-ecommerce/collections/470645342446` has the Collection ID of `470645342446`.
{% endalert %}

### Personalization

1. Create a catalog selection named "New Women’s Products - In Stock" that is filtered with products that have that collection's ID. You can only use one unique array field within a single catalog selection, and up to 50 products in your collection.
 - You can also create your own custom selections by filtering with the **Collections** field.

![A catalog selection that filters for collections that have the Collection ID attribute "470645342446".]({% image_buster /assets/img/shopify/collections_selection.png %})

{: start="2"}
2. In your message, template in your collection by using your created selection or directly referencing the collection. For example, you could use an HTML product block like this: 

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

Or, if you want to mention specific new products in a push notification, you can use the **Add Personalization** tool and specify your catalog items.

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![Push notification composer with a catalog selection pulling in three items with a product tag.]({% image_buster /assets/img/shopify/add_personalization_collections.png %})

### Catalog segmentation (SQL) 

Create a segment of users who interacted with a collection. Use [Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) to build segments based on collection membership. For example, to find users who purchased products from a specific collection in the last year, use this query:

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
You can also set up [price drop notifications]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/) and [back-in-stock notifications]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/)!<br><br> Note that for each use case, you must create a custom event that captures a user's subscription status in your catalog. The custom event requires an event property that maps to either the [SKU or Shopify variant ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) that you have selected as part of your Shopify product sync. 
{% endalert %}

## Deactivate your product sync {#deactivate}

Deactivating the Shopify product sync feature will delete your entire catalog and products. This can also impact any messages that may be actively using the product data from this catalog. Confirm that you have either updated or paused these campaigns or Canvases before deactivation, as this could result in sending messages with no product details. Do not delete the Shopify catalog directly on the catalogs page.

## Troubleshooting

If your Shopify product sync runs into an error, it could be a result of the following errors. Follow the instructions on how to correct the issue and resolve the sync:

| Error | Reason | Solution |
| --- | --- | --- |
| Server Error | This occurs if there is a server error on Shopify’s side when we attempt to sync your products. | [Deactivate sync](#deactivate) and re-sync your entire inventory of products again. |
| Duplicate SKU | This occurs if you use a SKU as your catalog item ID and have products with the same SKU. Because the catalog item ID must be unique, all your products must have unique SKUs. | Audit your full list of products and variants in Shopify to make sure that there are no duplicate SKUs. If there are duplicate SKUs, update these to be unique SKUs only in your Shopify store account. After this is corrected, [deactivate sync](#deactivate) and re-sync your entire inventory of products again. |
| Catalog Limit Exceeded | This occurs if you exceed your catalog limit. Braze will be unable to finish the sync or keep the syncing active due to no more storage availability. | There are two solutions to this issue:<br><br>1. Contact your account manager to upgrade your tier to increase your catalog limit. <br><br>2. Free up storage space by deleting any of the following:<br>- Catalog items from other catalogs<br>- Other catalogs<br>- Selections created<br><br> After using either of the solutions, the sync must be deactivated and then re-synced. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Troubleshooting" }

