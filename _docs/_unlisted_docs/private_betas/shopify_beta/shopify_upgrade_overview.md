---
nav_title: Shopify Upgrade Overview
article_title: "Shopify Upgrade Overview"
description: "This reference article outlines how to upgrade your Shopify integration to the latest version."
page_type: partner
search_tag: Partner
permalink: "/shopify_upgrade_overview/"
hidden: true
---

# Shopify upgrade overview 

> As part of our commitment to provide you with the best possible experience, we are requiring all Shopify integrations to [upgrade]({{site.baseurl}}/shopify/) to the latest version by August 28, 2025. This upgrade is essential because significant changes in Shopify's technology will impact how our integration functions.

## Key dates

- **End of February through April:** You will receive notifications regarding when your specific group (cohort) will be ready to upgrade. Keep an eye out for this important information.
- **Upgrade deadline:** All customers must complete the upgrade by **August 28, 2025**.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## What’s changing in the Shopify integration?

As part of Shopify’s plans to enhance checkout extensibility, significant changes are coming to its integration with Braze. Here’s what you need to know:

- **Deprecation of Script Tags and `checkout.liquid`:** Shopify is phasing out Script Tags and `checkout.liquid`. After August 2025, Braze’s Web SDK will no longer load on checkout pages through Script Tags unless you migrate to the latest version of the integration.
- **General improvements to the integration:**
    - **Introduction of recommended events:** We’re adding recommended eCommerce events to the integration, which simplifies common eCommerce use cases through pre-built templates in Braze.
    - **Streamlined identity management:** We’re enhancing our approach to managing user identities, which will improve tracking and attribution of anonymous user data. For more information on how identity management will be processed, refer to [User and data syncing]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
    - **Email and SMS subscriber lists:** If you’re currently collecting email and SMS subscribers, default subscription groups for each channel will be automatically created as part of the upgrade. When Braze syncs email and SMS opt-ins, Braze will no longer override the global subscription state on the user profile and just update the subscription group opt-in.
    - For full details on all the changes from the current version to the new version, refer to the [changelog](#full-changelog). 

{% alert important %}
This upgrade is essential to maintain the functionality of your integration between Shopify and Braze. We recommend collaborating closely with your development team to evaluate the scope and implications of these changes and to facilitate a seamless transition.
{% endalert %}

## Upgrade requirements 

Before you start the upgrade process on the Shopify integration page, complete the following requirements with your engineering team:

- **Check SDK customizations:** If you've customized your Braze and Shopify integration (for example, by logging custom events or attributes), make sure these customizations will work correctly after the upgrade. If you’ve created your own browser events for actions like "product viewed" or "cart updated", coordinate with your developers to remove them before the upgrade, as they will duplicate the functionality provided by the new connector.

{% alert important %}
If you're a Shopify online store and your developers implemented the Braze SDKs directly to your Shopify site, or through Google Tag Manager or a Customer Data Platform, you must plan to stop using them as you upgrade to the new Shopify connector. 
{% endalert %}

- **Review identity management:** If you're using a Braze external ID, work with your development team to ensure it's compatible with the new integration. If you set the external ID within your Shopify store experience, have your developers adjust it to avoid conflicts with the [new identity management process]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).
- **Prepare impacted campaigns, Canvases, and segments:** During the guided upgrade process, you can view and export any campaigns, Canvases, and segments that rely on Shopify data. We recommend adding the new required Shopify events and attributes using an “OR” operator to facilitate a smooth upgrade for your active messages.
- **Create Abandoned Cart and Checkout user journeys:** The Abandoned Cart user journey must now use the “Performed Cart Updated” trigger as part of the entry criteria in your Canvas. Additionally, you need to use the new shopping cart Liquid tag for both Abandoned Cart and Abandoned Checkout user journeys. You can use our new [Canvas templates]({{site.baseurl}}/using_shopify_with_braze#create-your-canvas-user-journeys) to help you get started.

Completing these steps will help facilitate a successful upgrade to the latest version of the Shopify integration.

## Integration options

Braze offers two integration options for Shopify merchants that are designed to meet the diverse needs of eCommerce businesses: **Standard integration** and **Custom integration**.

{% tabs local %}
{% tab standard %}
The standard integration is tailored for Shopify online stores, providing a seamless and straightforward setup process. This option allows you to quickly connect your Shopify store to Braze, empowering you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

To upgrade your existing Shopify integration through the standard upgrade path, refer to [Upgrading your Shopify integration (standard)]({{site.baseurl}}/shopify_standard_upgrade/).
{% endtab %}

{% tab custom %}
The custom integration offers a more flexible and composable solution if you use Shopify Hydrogen or support a headless store. This option empowers you to implement Braze SDKs directly into your Shopify environment, enabling deeper integration and tailored functionalities. Whether you’re looking to create unique customer experiences or optimize specific workflows, the custom integration provides the tools necessary to fully leverage Braze’s capabilities in a headless setup.

To upgrade your existing Shopify integration through the custom upgrade path, refer to [Upgrading your Shopify integration (custom)]({{site.baseurl}}/shopify_custom_upgrade/).
{% endtab %}
{% endtabs %}

## Changelog 

{% alert important %}
This integration uses Shopify as the source of truth for supported attributes and events. As a result, Shopify can replace pre-existing values, like standard or custom attributes, on a user profile when the data syncs.
{% endalert %}

### Standard integration 

| Previous version | Latest version |
| --- | --- | 
| {::nomarkdown}<ul><li>Script Tag support</li><li>Braze Web SDK only</li><li>Shopify webhooks for events and products</li></ul>{:/} | {::nomarkdown}<ul><li>Web Pixel API support</li><li>New Braze app embed</li><li>Braze Web SDK & JavaScript SDK</li><li>Shopify webhooks for events and products</ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard integration" }

### User identifiers supported by the integration 

| User identifiers | Previous version | Latest version |
| --- | --- | --- | 
| Braze device ID |  {::nomarkdown}<ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/} | {::nomarkdown} <ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/}|
| Braze aliases | {::nomarkdown}<ul><li>Shopify customer ID</li><li>Shopify email</li></ul>{:/} | {::nomarkdown}<ul><li>Shopify cart token</li><li>Shopify checkout token</li></ul>{:/}|
| Braze external ID | {::nomarkdown}<ul><li>N/A</li></ul>{:/}| {::nomarkdown}<ul><li>Shopify customer ID</li><li>Email</li><li>Hashed email (SHA-256, SHA-1, MD5)</li><li>Custom external ID</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User identifiers supported by the integration" }

For more details on user syncing and ID management, refer to [User data and syncing]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing).

{% alert note %}
By default, Braze automatically converts emails from Shopify to lowercase before using them as the external ID. If you're using email or hashed email as your external ID, confirm that your email addresses are also converted to lowercase before you assign them as your external ID or before hashing them from other data sources. This will help prevent discrepancies in external IDs and avoid creating duplicate user profiles in Braze.
{% endalert %}

### Supported Shopify events 

| Events or attributes | Previous version | Latest version |
| --- | --- | --- | 
| Events |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=product%20viewed">shopify_product_viewed</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=product%20viewed">ecommerce.product_viewed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-browse">abandoned browse Canvas template</a></li></ul>{:/} |
| Events |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?tab=example%20payload">shopify_product_clicked</a></li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated event</li></ul>{:/} |
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20cart&tab=example%20payload">shopify_abandoned_cart</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=cart%20updated">ecommerce.cart_updated</a></li><li>Deprecated abandoned cart timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-cart">abandoned cart Canvas template</a></li></ul>{:/} |
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20checkout&tab=example%20payload">shopify_abandoned_checkout</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=checkout%20started">ecommerce.checkout_started</a></li><li>Deprecated abandoned checkout timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-checkout">abandoned checkout Canvas template</a></li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20order&tab=example%20payload">shopify_created_order</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#order-confirmation-and-feedback-survey">order confirmation & post-purchase survey Canvas template</a></li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="https://braze.com/unlisted_docs/using_shopify_with_braze/?tab=order%20confirmation">Braze purchase event</a></li></ul>{:/}| {::nomarkdown}<ul><li>Deprecated event. Use <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a>.</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=paid%20order&tab=example%20payload">shopify_paid_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=partially%20fulfilled%20order&tab=example%20payload">shopify_partially_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=fulfilled%20order&tab=example%20payload">shopify_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=cancelled%20order&tab=example%20payload">shopify_cancelled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20cancelled">ecommerce.order_cancelled</a></li></ul>{:/}|
| Events | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20refund&tab=example%20payload">shopify_created_refund</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20refunded">ecommerce.order_refunded</a></li></ul>{:/}|
| Events| {::nomarkdown}<ul><li>No Shopify account login event</li></ul>{:/}| {::nomarkdown}<ul><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=account%20login#tracked-shopify-events">shopify_account_login</a></li></ul>{:/}|
| Attributes | {::nomarkdown}<ul><li>shopify_total_spent</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributes | {::nomarkdown}<ul><li>shopify_order_count</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributes | {::nomarkdown}<ul><li>shopify_last_order_id</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributes | {::nomarkdown}<ul><li>shopify_last_order_name</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributes | {::nomarkdown}<ul><li>shopify_zipcode</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| Attributes | {::nomarkdown}<ul><li>shopify_province</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported Shopify events" }

### Subscriber collection 

| Collection type | Previous version | Latest version |
| --- | --- | --- | 
| Email subscriber collection |  {::nomarkdown}<ul><li>Override for global email subscription state</li><li>Ability to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated override functionality</li><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
| SMS subscriber collection |  {::nomarkdown}<ul><li>Required to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscriber collection" }

{% alert note %}
If you're currently collecting email or SMS subscribers, a new default subscription group will be created after the upgrade is completed. The default subscription group will be the name of your Shopify storefront. This process may take up to 5 hours. <br><br>After the subscription groups are available, make sure to include them in your active campaigns, Segments, or Canvases to effectively reach your subscribed shoppers.
{% endalert %}

### Product sync 

| Sync type | Previous version | Latest version |
| --- | --- | --- | 
| Initial product sync | {::nomarkdown}<ul><li>If product syncing is enabled, initial import of all products in your storefront</li><li>Ability to only import active products</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
| Real-time product syncs | {::nomarkdown}<ul><li>Real-time syncs when products are created, updated, or deleted from your store</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Product sync" }

### Channels 

| Channel | Previous version | Latest version |
| --- | --- | --- | 
| In-app messages |  {::nomarkdown}<ul><li>Included within standard integrations for Shopify online stores</li></ul>{:/} | {::nomarkdown}<ul><li>No changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Channels" }