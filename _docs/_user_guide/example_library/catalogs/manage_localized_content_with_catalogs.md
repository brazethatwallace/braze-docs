---
nav_title: Localized catalog content
article_title: Manage localized content with Braze catalogs
page_order: 3
page_type: reference
description: "Store localized product copy, prices, and image URLs in Braze catalogs and resolve the correct language at send time."
---

# Manage localized content with Braze catalogs

> Store localized strings and URLs in catalogs so each user receives copy in their language from a single campaign or Canvas, without separate variants per locale.

## About this example

PantsLabyrinth, a fictional clothing retailer, sells its products across North America and Europe. Product names, prices, and hero images differ by language, but marketing wants one email or push template that personalizes at send time.

This example covers three catalog patterns that read the user's {% raw %}`${language}`{% endraw %} [standard attribute]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) (collected by the SDK from device locale):

- JSON object fields: all locales in one row per item
- Flat per-language columns: `header_en`, `header_fr`, and so on
- Separate catalog per language: dynamic catalog name such as `pantslabyrinth-promo-en`

Use catalogs when localized content is structured data (products, promotions, image URLs). For free-form message copy in email or push, prefer [multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) when your channels support them. To compare localization patterns more broadly, see [Translation management]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/#translation-management).

## Considerations

- Examples are illustrative. Confirm {% raw %}`${language}`{% endraw %} casing and format in your user base before you name catalog keys or suffixes.
- For Methods 1 and 2, if {% raw %}`${language}`{% endraw %} is blank or does not match a catalog key or field, localized output can be empty—check each field independently and fall back to a default (for example English).
- For Method 3, allowlist supported language codes before you build the catalog name; a missing catalog aborts the message.
- [JSON objects]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#supported-data-types) in catalogs can be created or updated through the API or [Cloud Data Ingestion (CDI) for catalogs]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/), not through CSV upload.
- Method 2 supports CSV maintenance but multiplies columns as languages grow. CSV files support up to [1,000 columns]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#step-1-review-your-csv-file).
- Method 3 requires a catalog for every language code that reaches the `catalog_items` tag. If the catalog does not exist, Braze aborts the message. A missing item ID in an existing catalog returns an empty items array.
- Catalog Liquid tags cannot be used [recursively]({{site.baseurl}}/user_guide/data/activation/catalogs/use/#using-liquid).
- [Catalog selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) support up to 10 filters and return up to 50 items—validate filters against your catalog schema.
- Review [catalog storage tiers]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers) if you maintain large multi-locale product feeds.

## Setup

### Step 1: Choose a catalog structure

Choose a catalog structure using the guidance in this table.

| Method | Best when | Tradeoff |
| --- | --- | --- |
| JSON object fields | Medium catalog size; one row per item; updates through API or CDI | Adding a language updates every item through API; no CSV for JSON fields |
| Flat per-language fields | Few languages and fields; non-engineering teams use CSV | Each new language adds columns; field naming must stay consistent |
| Catalog per language | Large per-locale feeds or separate locale owners; CSV per language | Every allowlisted language code needs a catalog; missing catalogs abort the send |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Choose a catalog structure" }

### Step 2: Create the catalog and items

1. Go to **Data Settings** > **Catalogs** and create a catalog (or multiple catalogs for Method 3).
2. Add fields and items based on your chosen structure. See [Create a catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create/).
3. (Optional) Create a [catalog selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to filter items—for example by `category` matching a user custom attribute.

{% tabs local %}
{% tab Method 1: JSON fields %}
Example item in catalog `PantsLabyrinth_Product_Copy`:

| Item | Value |
| --- | --- |
| `id` | `trail-runner-001` |
| `name` | `{"EN":"Trail Runner","FR":"Chaussure de trail","DE":"Trailrunner"}` |
| `category` | `footwear` |
| `url` | `https://pantslabyrinth.shop/products/trail-runner-001` |
| `price` | `{"EN":"$120 USD","FR":"112 EUR","DE":"112 EUR"}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example catalog item with JSON locale fields" }

{% endtab %}
{% tab Method 2: Flat fields %}
Example item in catalog `PantsLabyrinth_Promo_Copy`:

| Item | Value |
| --- | --- |
| `id` | `spring-sale` |
| `header_en` | `Spring trail sale` |
| `header_fr` | `Soldes de printemps` |
| `body_en` | `Save on trail runners this week.` |
| `body_fr` | `Économisez sur les chaussures de trail cette semaine.` |
| `cta_text_en` | `Shop now` |
| `cta_text_fr` | `Acheter` |
| `img_src_en` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
| `img_src_fr` | `https://cdn.pantslabyrinth.shop/fr/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example catalog item with flat per-language fields" }

{% endtab %}
{% tab Method 3: Catalog per language %}
Create one catalog per language with the same fields. For example, repeat the same `id` and fields in `pantslabyrinth-promo-fr` and `pantslabyrinth-promo-de` with localized values.

Example item in `pantslabyrinth-promo-en`:

| Item | Value |
| --- | --- |
| `id` | `spring-sale` |
| `header` | `Spring trail sale` |
| `body` | `Save on trail runners this week.` |
| `cta_text` | `Shop now` |
| `img_src` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example item in an English per-language catalog" }

{% endtab %}
{% endtabs %}

### Step 3: Add Liquid to your message

Select the Liquid pattern that matches the catalog structure you chose in Step 1.

{% tabs local %}
{% tab Method 1: JSON fields %}
Store all locales in JSON object fields on a single catalog row, then use the `property_accessor` filter to read the `name` and `price` keys that match {% raw %}`${language}`{% endraw %} (normalized to uppercase). Check each field independently and fall back to `EN` when that field is blank, so a locale with a name but no price still gets an English price.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Product_Copy trail-runner-001 %}
{% assign lang = ${language} | upcase %}
{% assign localized_name = items[0].name | property_accessor: lang %}
{% assign localized_price = items[0].price | property_accessor: lang %}
{% if localized_name == blank %}
  {% assign localized_name = items[0].name | property_accessor: 'EN' %}
{% endif %}
{% if localized_price == blank %}
  {% assign localized_price = items[0].price | property_accessor: 'EN' %}
{% endif %}
Product: {{ localized_name }}
Price: {{ localized_price }}
```
{% endraw %}

See [Property accessor filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#property-accessor-filter).
{% endtab %}
{% tab Method 2: Flat fields %}
Build dynamic field names from {% raw %}`${language}`{% endraw %} (normalized to lowercase), then read those fields from the item with bracket lookup. For example, {% raw %}`items[0][header_field]`{% endraw %} reads the header for the resolved language. Check each field independently and fall back to the English column when that field is blank, so a locale with a header but no body still gets English body text.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Promo_Copy spring-sale %}
{% assign lang = ${language} | downcase %}
{% assign header_field = 'header_' | append: lang %}
{% assign body_field = 'body_' | append: lang %}
{% assign cta_field = 'cta_text_' | append: lang %}
{% assign img_field = 'img_src_' | append: lang %}
{% assign header_val = items[0][header_field] %}
{% assign body_val = items[0][body_field] %}
{% assign cta_val = items[0][cta_field] %}
{% assign img_val = items[0][img_field] %}
{% if header_val == blank %}
  {% assign header_val = items[0].header_en %}
{% endif %}
{% if body_val == blank %}
  {% assign body_val = items[0].body_en %}
{% endif %}
{% if cta_val == blank %}
  {% assign cta_val = items[0].cta_text_en %}
{% endif %}
{% if img_val == blank %}
  {% assign img_val = items[0].img_src_en %}
{% endif %}
<img src="{{ img_val }}" alt="" />
<h2>{{ header_val }}</h2>
<p>{{ body_val }}</p>
<a href="#">{{ cta_val }}</a>
```
{% endraw %}
{% endtab %}
{% tab Method 3: Catalog per language %}
{% alert warning %}
If the catalog name you pass to `catalog_items` does not exist, Braze aborts the message. Allowlist supported language codes before you build the catalog name. A missing item ID in an existing catalog returns an empty items array—you can fall back to the English catalog for that case only.
{% endalert %}

Allowlist the language codes that have matching catalogs (here `en`, `fr`, and `de`), default unsupported or blank values to `en`, then look up the item. If the item ID is missing in that catalog, fall back to the English catalog.

{% raw %}
```liquid
{% assign lang = ${language} | downcase %}
{% assign supported = 'en,fr,de' | split: ',' %}
{% if supported contains lang %}{% else %}{% assign lang = 'en' %}{% endif %}
{% assign theCatalog = 'pantslabyrinth-promo-' | append: lang %}
{% catalog_items {{ theCatalog }} spring-sale %}
{% if items[0] == blank %}
  {% catalog_items pantslabyrinth-promo-en spring-sale %}
{% endif %}
<img src="{{ items[0].img_src }}" alt="" />
<h2>{{ items[0].header }}</h2>
<p>{{ items[0].body }}</p>
<a href="#">{{ items[0].cta_text }}</a>
```
{% endraw %}

See [Using templates in catalog names]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#template-catalog-names) and [Aborting messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).
{% endtab %}
{% endtabs %}

#### Optional catalog selection by category

Filter items before personalization—for example footwear promos for users with `preferred_category = footwear`:

{% raw %}
```liquid
{% catalog_selection_items PantsLabyrinth_Product_Copy footwear_promos %}
{% for item in items %}
  {{ item.name }}
{% endfor %}
```
{% endraw %}

Define the selection in the dashboard with filters on your `category` column and user attributes as needed.

### Step 4: Preview and test

1. Use **Preview as User** with user profiles that have different {% raw %}`${language}`{% endraw %} values.
2. Confirm fallback copy when language is missing or unsupported, including partial locales (for example a name without a price).
3. For Method 3, confirm every allowlisted language has a matching catalog, and that unsupported language codes map to your default catalog without aborting the send.

## Related articles

- [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/)
- [Use catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/use/)
- [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)
- [Create a catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)
- [Advanced Liquid filters]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#property-accessor-filter)
- [Localization]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/)
- [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)
- [Sync and delete catalog data]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)
- [Abort Liquid messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)
