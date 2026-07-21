---
nav_title: Shopify Markets
article_title: Shopify Markets
description: "This reference article covers how to set up and use the Shopify Markets integration with Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_markets/"
hidden: true
---

# Shopify Markets

> This article covers the Shopify Markets integration (currently in beta), including what's in scope, how it works, and how to use your markets data in your messaging. Braze is progressively releasing additional Markets functionality throughout the beta period, scaling up to support more complex market structures over time.

{% alert important %}
Shopify Markets is currently in beta. For more information, contact your Braze customer success manager.
{% endalert %}

## How the integration works

Shopify Markets extends your existing Shopify integration. Connect your default storefront through the [standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) or [custom (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/) integration path, then select the markets you want Braze to sync from your store's configured markets. Existing integrations can add markets without disrupting catalogs, subscription groups, or events. For step-by-step instructions, see [Shopify Markets setup](#shopify-markets-setup).

Shopify Markets provides these capabilities:

- **Market-aware profiles.** The integration captures each user's Shopify locale along with Braze's standard country and language attributes, so you can segment and trigger by market with no custom setup.
- **Localized catalogs.** Market-specific product data syncs daily: prices, currency, and availability per market, plus translated titles, descriptions, and product URLs.
- **Market-aware personalization.** Use the {% raw %}`{% shopify_market %}`{% endraw %} Liquid tag to personalize with catalog products from each user's market, including Shopify's translated content. You can also reference market details, such as presentment currency, from supported Shopify events like `ecommerce.order_placed`.
- **Default store fallback.** When a user doesn't belong to one of your connected markets, Braze uses your default store settings and products, so every user receives a complete, accurate message.

For examples, see [Use Markets user data](#use-markets-user-data) and [markets-aware catalog use case](#tutorial-show-products-and-prices-per-market).

## Supported Shopify market types

During this phase of the beta, you can select up to 25 single-country markets in Braze, subject to the following rules:

- Each selected market must be an active [single-country market](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets). B2B and retail markets aren't supported.
  - Shopify's "Use local currencies" setting isn't supported
- A country can only belong to one selected market.
- Multi-country markets aren't supported in this phase of the beta.

Each selected market requires a market catalog with active products for Braze to support:

- Market-specific pricing on products, using the currency set in the market catalog
- Product availability per market
- Product translations made through the Shopify Translate & Adapt app (such as product title or variant title)

![Shopify market profile for an Australia market.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Considerations

#### General

- **One connected store:** You can connect only one Markets-enabled Shopify store to a Braze workspace at a time.
- **Locale scope:** Locales pull in translated product titles and descriptions based on what you configured using the Shopify Translate & Adapt app, and locale-specific URLs. Price, currency, and other shared catalog fields stay the same across locales within a market. By default, Braze uses each market's [default language](https://help.shopify.com/en/manual/markets/languages), the primary locale Shopify assigns to that market. If expanded locale support is turned on for your account, Braze syncs additional locales configured for that market.

#### Market catalog

- **New market views in your original Shopify catalog:** Markets doesn't create separate catalogs. Instead, they are shown as part of your original Shopify catalog. Markets data is added to new catalog rows to your Shopify catalog.
- **Catalog selections:** Up to 30 catalog selections.
- **Refresh timing:** Market catalog product data refreshes once daily.
- **Pricing-only market catalogs:** A pricing-only market catalog sets market-specific prices without publishing products to a sales channel. Inventory and product availability sync from your default store catalog, while price reflects the market catalog's price list or contextual pricing.

### Unsupported features 

The following aren't supported in this beta:

- Price-drop and back-in-stock triggers for market catalogs
- Email and SMS double opt-in for markets-configured subscription groups
- Nested market groups or country-group workflows beyond the current single-country and multi-country selection model
- Selecting more than 25 markets
- Catalog export for markets-enabled catalogs
- Full parity with Shopify's local-currency conversion, rounding rules, and multi-catalog lowest-price behavior at browse and checkout

## Shopify Markets setup

### Step 1: Connect your Shopify Markets-enabled store

1. Connect your store using either the [Shopify standard integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) or [Shopify custom integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/) path. After your store is connected, configure Shopify Markets in the setup composer.
2. Complete the OAuth flow and confirm Braze requests the markets scopes in the OAuth:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. After authorization succeeds and the setup composer opens, select **Begin Setup**.
4. Turn on the Braze SDKs.

### Step 2: Select your market and data settings

1. In **Track Shopify Data**, select **Sync Shopify Markets data**.
2. Select **Select Markets** to pick your market, and make sure you've chosen to track behavioral events and user attributes.
   - (Optional) Turn on historical backfill

#### Markets user data

To support Shopify Markets, Braze syncs more data than the integration's [standard events and attributes]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#tracked-shopify-events).

Braze writes these additional market context to each user profile:

| Data Type | Value | Data Source |
| --- | --- | --- |
| Custom Attribute | `shopify_locale` | Shopify |
| Standard Attribute | browser language | Braze SDKs |
| Standard Attribute | country | Braze SDKs |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User profile data type"}

Braze also collects the following additional order event properties to support markets context:

| Data type | Impacted events | New properties added |
| --- | --- | --- |
| eCommerce recommended events | `ecommerce.order_placed`<br>`ecommerce.order_cancelled`<br>`ecommerce.order_refunded` | `country`, `presentment_currency`, `market_handle` |
| Custom events | `shopify_paid_order`<br>`shopify_fulfilled_order`<br>`shopify_partially_fulfilled_order` | `country`, `presentment_currency`, `market_handle` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Order event data type"}

Each property is derived from the following sources:

| Property | Data source |
| --- | --- |
| `country` | Shopify customer `default_address`; if unavailable, Braze uses `shipping_address` |
| `presentment_currency` | Shopify presentment money value |
| `market_handle` | Configured Shopify market for the order country; set only when markets are configured and the country matches |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Order event property data sources"}

### Step 3: Manage users

1. Select your `external_id` type from the dropdown.
2. Turn on email and SMS opt-ins from Shopify, which allows Braze to sync email and SMS subscription states from Shopify. You have two options:
  - **Use the integration:** Braze syncs email and SMS states. You only need to pick the subscription groups they sync to.
  - **Build your own:** For more control over state management, you can build a custom integration using Braze subscription group endpoints.
3. Create default subscription groups for each country associated with your synced markets during setup.
  - **New Shopify integration:** Assign a default email and SMS subscription group per country. 
  - **Existing Shopify integration:** Your store's current default group stops syncing. Assign new default email and SMS groups per country. Your old setup doesn't carry over automatically.

#### How opt-ins and unsubscribes work

During setup, you configure default email and SMS subscription groups for each country associated with your synced markets (up to 25 countries). This is required before you can save your country configuration. You can also assign additional subscription groups per country if you want to route consent to more than one list.

##### Consent applies to all configured countries

When a user's consent state changes in Shopify, Braze applies that change across every country's default subscription groups tied to your connected store, not just the user's specific country:
  - If a user becomes subscribed in Shopify, they're subscribed to the default email or SMS subscription group for each country you've configured.
  - If a user becomes unsubscribed in Shopify, they're unsubscribed from the default email or SMS subscription group for each country you've configured.

{% alert important %}
Shopify consent is per store, not per country. In Shopify, consent is tracked once for email and once for SMS per customer record, and doesn't subscribe or unsubscribe by country or by list type. Because of this, Braze can't apply consent changes to a single country or single subscription group. A subscribe or unsubscribe event in Shopify always applies to all your configured countries' default subscription groups at once. <br><br> Within Braze, however, you can have more granular control of subscription group-level opt-ins and opt-outs as users engage with messaging channels.
{% endalert %}

### Step 4: Sync products

1. To sync products within your market, select **Sync Shopify products and variants to Braze**.
2. Assign the Braze **catalog ID** and configure any additional settings.

Your catalog includes a per-market view for your store's default products. For each product published to your market, Braze adds a market row to your existing catalog, on top of the [standard Shopify catalog fields]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/#supported-shopify-catalog-data) already supported. It may take a few minutes for these to sync if you turn on Shopify Markets on an existing integration.

On market rows, these fields have markets-specific values:

| Field | Description |
| --- | --- |
| {% raw %}`market_handle`{% endraw %} | Identifies the market for the row. Default-market rows use `default`; additional markets use their handle (for example, `au`). |
| {% raw %}`locale`{% endraw %} | When expanded locale support is enabled, identifies the locale for the row (for example, `fr`). |
| {% raw %}`price`{% endraw %} | Market-specific price from the market's contextual pricing. |
| {% raw %}`compare_at_price`{% endraw %} | Market-specific compare-at price, or `0` when Shopify has no compare-at price for that market. |
| {% raw %}`product_title`{% endraw %} | Translated product title when a Shopify translation exists for the row's locale. |
| {% raw %}`variant_title`{% endraw %} | Translated variant title when a Shopify translation exists for the row's locale. |
| {% raw %}`product_url`{% endraw %} | Storefront URL for the market and locale when localized URLs are enabled; otherwise this is the default `myshopify.com` product URL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="market row catalog fields"}

Market rows use a composite `id` prefixed with the market handle, such as `<market>_<variant_id>`. When expanded locale support is enabled, the ID also includes the locale (for example, `<market>_<locale>_<variant_id>`). Your default products keep their original IDs.

### Step 5: Activate channels

1. (Optional) Choose whether to enable **in-browser messaging**.
2. Select **Finish Setup**.

## Use Markets user data

After these attributes and properties are on user profiles, you can use them to target users by market and to personalize messages.

### Target by market in segmentation

Filter by country, browser language, or `shopify_locale` in segments and in campaign or Canvas entry criteria. As an example, build an audience of users in a specific market, or split a Canvas by locale.

### Personalize and trigger with Liquid

Reference the data directly in your messages.

| User data to reference | Liquid to use |
| --- | --- |
| The user's locale | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| The user's country | {% raw %}`{{${country}}}`{% endraw %} |
| An order's country (in a triggered message) | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| An order's market (in a triggered message) | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| An order's currency (in a triggered message) | {% raw %}`{{event_properties.${presentment_currency}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="User data to reference with Liquid"}

### Trigger messages from order activity

The new order properties travel with each order event, so you can trigger a message off an order and personalize what it says using market-aware details.

A simple version in the message body might look like:

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${presentment_currency}}} {{event_properties.${total_value}}}
```
{% endraw %}

Because the properties are on the event itself, the message stays accurate to each user's market without extra setup.

## Tutorial: Show products and prices per market

Use a markets-aware catalog to build a single message that shows each user the products and prices for their own market.

1. Create a selection that uses markets data.
2. Reference the selection in a message with Liquid.

You can use a fixed market when a message targets one specific market.

### Step 1: Create a selection using markets data

[Selections]({{site.baseurl}}/catalog_selections/) are curated product sets you reference in messages. For Shopify catalogs with synced markets, the **Filter settings** section includes a **Market scope** area that scopes product data to one market or personalizes it per user.

1. Go to your Shopify catalog and open the **Selections** tab.
2. Select **Create Selection**, then name the selection, add an optional description, and set a results limit.
3. In **Filter settings**, under **Market scope**, use the **Market** dropdown to choose how the selection resolves market-specific products:
   - **Personalized:** Each recipient sees products and prices from the market that matches their profile's `country` attribute.
   - **A synced market:** Select a market by name to pin the selection to that market's products and prices. Use this when a message targets a single market only.
4. Finish any additional filter criteria, then save the selection.
5. In **Preview for user**, select a user to see what the selection returns for that profile. Selections that use **Personalized** can only be previewed after you select a user.

| Target | Filter |
| --- | --- |
| A specific market | `market_handle` = `au` |
| Default products only | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Targets and associated filters"}

{% alert note %}
If you don't specify a market, Braze uses your default products.
{% endalert %}

### Step 2: Add market-aware catalog selections to messages

To serve every user the products from their own market in a single message, create one selection with this filter:

| Selection name | Field | Operator | Value |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Selection name and associated filters"}

At send time, Braze swaps {% raw %}`{{shopify_market.handle}}`{% endraw %} for each user's market, so `market_products` gives everyone the right products. `default_products` is the fallback for users with no matching market.

Reference your selection in your message with the {% raw %}`{% shopify_market %}`{% endraw %} tag:

{% raw %}
```liquid
{% shopify_market %}
{% if shopify_market.handle %}
  {% catalog_selection_items <your_catalog_name> <your_market-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% else %}
  {% catalog_selection_items <your_catalog_name> <your_default-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% endif %}
```
{% endraw %}

- Place {% raw %}`{% shopify_market %}`{% endraw %} before {% raw %}`{% catalog_selection_items %}`{% endraw %} so the user's market is set before the selection runs.
- Swap `<your_catalog_name>` for your catalog, and use your own selection names if they differ.
- The {% raw %}`{{shopify_market.handle}}`{% endraw %} check routes users with no matching market to `default_products`, so they still receive products instead of an empty message.

Preview as a user in your market to confirm the message shows that market's products, prices, and translated titles.