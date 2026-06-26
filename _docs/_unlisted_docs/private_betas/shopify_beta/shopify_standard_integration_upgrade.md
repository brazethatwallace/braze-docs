---
nav_title: Upgrading Shopify
article_title: "Upgrading your Shopify integration"
description: "Learn how to upgrade your Shopify integration for Braze."
page_type: partner
search_tag: Partner
permalink: "/shopify_standard_upgrade/"
hidden: true
---

# Upgrading your Shopify integration (standard)

> Learn how to upgrade your Shopify integration using the standard path for Braze. As part of our commitment to provide you with the best possible experience, we are requiring all Shopify integrations to [upgrade]({{site.baseurl}}/shopify/) to the latest version by August 28, 2025. This upgrade is essential because significant changes in Shopify's technology will impact how our integration functions.

## Who's eligible?

This upgrade path is intended for brands with a Shopify online store. 

{% multi_lang_include shopify_alerts.md alert='breaking' %}

## Upgrade requirements

Before you begin, review the following:

- **Critical changes:** Make sure you've reviewed all the important changes from the legacy connector to the new connector in [Shopify upgrade overview]({{site.baseurl}}/shopify_upgrade_overview/#subscriber-collection).
- **Upgrade prerequisites:** Ensure you've completed all necessary [upgrade prerequisites]({{site.baseurl}}/shopify_upgrade_overview#upgrade-prerequisites) with your engineering and marketing teams.
- **Breaking changes:** Review and fix all breaking changes flagged in Braze. For a full walkthrough, continue to [Fixing breaking changes](#fixing-breaking-changes-fixing-breaking-changes).

## Fixing breaking changes {#fixing-breaking-changes}

In Braze, go to **Partner Integrations** > **Shopify**, then select **Start upgrade**.

![Panel with an option to start the upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Any impacted Canvases, campaigns, and segments that use Shopify data will be flagged.

![A modal for reviewing what is impacted by breaking changes.]({% image_buster /assets/unlisted_docs/img/shopify/review_breaking_changes.png %})

For most events, we recommend including the new required Shopify events and attributes using an "OR" operator to facilitate a smooth upgrade of active messages. For more specific cases, refer to the following:

{% tabs local %}
{% tab Abandoned Cart %}
For Abandoned Cart messaging, you will need to use the new Abandoned Cart Canvas Templates which includes:

- A new trigger based on the “Performed cart updated” action 
- Pre-defined exit criteria to remove customers who have moved on in their purchasing journey 
- A new shopping cart Liquid tag to support product personalization 
{% endtab %}

{% tab Abandoned Checkout %}
For Abandoned Checkout messaging, you will need to use the new Abandoned Checkout Canvas Template which includes:

- The ecommerce.checkout_started event pre-defined in your entry criteria 
- Pre-defined exit criteria to remove customers who have moved on in their purchasing journey 
- A new shopping cart liquid tag to support product personalization 

For a complete list of new eCommerce Canvas templates and pre-defined HTML blocks for product personalization available through the integration, refer to [Create your Canvas user journeys]({{site.baseurl}}using_shopify_with_braze#create-your-canvas-user-journeys).

{% alert important %}
If you don't account for active messages that use discontinued events in the Shopify integration, impacted messages will no longer be sent to your customers.
{% endalert %}

To learn more, review [Supported Shopify events]({{site.baseurl}}/shopify_upgrade_overview/#supported-shopify-events).
{% endtab %}

{% tab Subscriber Lists %}
If you're collecting email or SMS subscribers from Shopify through the integration, confirm that your active messages include the corresponding subscriber lists for your Shopify store. 

When the upgrade is complete, new default subscription groups will be created for your integration which you will need to leverage as part of your active messaging. For more information on the changes, refer to [Subscriber collection]({{site.baseurl}}/shopify_upgrade_overview#subscriber-collection).
{% endtab %}
{% endtabs %}

## Upgrading Shopify

{% alert important %}
It's essential that you [fix all breaking changes](#fixing-breaking-changes) before starting your upgrade.
{% endalert %}

### Step 1: Start the upgrade

In Braze, go to **Partner Integrations** > **Shopify**, then select **Start upgrade**.

![Panel with an option to start the upgrade.]({% image_buster /assets/unlisted_docs/img/shopify/start_shopify_upgrade.png %}){: style="max-width:35%;"}

Agree to the terms and conditions by checking the box, then select **Start the upgrade**.

![Modal to confirm that you understand upgrading may cause breaking changes.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_upgrade.png %})

### Step 2: Set up the Braze SDKs 

The standard integration will automatically add the Braze SDKs to your Shopify site. If you have already integrated the Braze SDKs directly or used a third-party tool for this, coordinate with your developers to remove the previous SDK implementation as you’re upgrading.

![Modal confirming that the new integration will automatically implement the Braze and JavaScript SDK onto your store.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_integration.png %}){: style="max-width:70%;"}

### Step 3: Reauthorize the Braze app

To reauthorize the Braze app, select **Go to Shopify**.

![Shopify upgrade panel with a button to go to Shopify to reauthorize the Braze app.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorize_braze_app.png %}){: style="max-width:35%;"}

On the Shopify site, follow the prompts to reauthorize your Braze app. This allows Braze to access your Shopify data.

{% alert note %}
The reauthorization process may take a few minutes, but it will automatically update on your Shopify page when it's completed.
{% endalert %}

![The "Integration Settings" page showing the status of Shopify events.]({% image_buster /assets/unlisted_docs/img/shopify/reauthorization_status.png %})

### Step 4: Choose an external ID type

The external ID type you choose will be assigned to new Shopify customer profiles when either a Shopify account is created or an order is placed. It'll also be used to update existing user profiles if they already have a Shopify customer ID alias but aren't assigned an external ID in Braze.

To choose your external ID type, go back to Braze and then select **Confirm external ID**.

![Shopify upgrade panel with a button to confirm the external ID.]({% image_buster /assets/unlisted_docs/img/shopify/confirm_external_id.png %}){: style="max-width:35%;"}

Choose the external ID you'd like to use for your workspace's Shopify integration. When you're finished, select **Set external ID**.

![Modal with a dropdown to select the external ID.]({% image_buster /assets/unlisted_docs/img/shopify/external_id_field.png %}){: style="max-width:70%;"}

{% alert important %}
Using an email address or a hashed email address as your Braze external ID can help simplify identity management across your data sources. However, it's important to consider the potential risks to user privacy and data security.<br><br>

- **Guessable Information:** Email addresses are easily guessable, making them vulnerable to attacks.
- **Risk of Exploitation:** If a malicious user alters their web browser to send someone else's email address as their external ID, they could potentially access sensitive messages or account information.
{% endalert %}

By default, Braze automatically converts emails from Shopify to lowercase before using them as the external ID. If you're using email or hashed email as your external ID, confirm that your email addresses are also converted to lowercase before you assign them as your external ID or before hashing them from other data sources. This helps prevent discrepancies in external IDs and avoid creating duplicate user profiles in Braze.

If you selected a custom external ID type, proceed to steps 4.1—4.3. Otherwise, continue to step 5.

#### Step 4.1: Create the `braze.external_id` metafield

1. In your Shopify admin panel, go to **Settings** > **Metafields**.
2. Select **Customers** > **Add definition**.
3. For **Namespace and key**, enter `braze.external_id`.
4. For **Type**, select **ID Type**.

After the metafield is created, populate it for your customers. We recommend the following approaches:

- **Listen to customer creation webhooks:** Set up a webhook to listen for [`customer/create` events](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). This allows you to write the metafield when a new customer is created.
- **Backfill existing customers:** Use the [Admin API](https://shopify.dev/docs/api/admin-graphql) or [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) to backfill the metafield for previously created customers.

#### Step 4.2: Create an endpoint to retrieve your external ID

You need to create a public endpoint that Braze can call to retrieve the external ID. This is necessary for scenarios where Shopify can't provide the `braze.external_id` metafield. 

##### Endpoint specifications

**Method:** `GET`

| Parameters | Description |
| --- | --- |
| `shopify_customer_id` | The Shopify customer ID. |
| `email_address` | The email address of the logged-in user. |
| `shopify_storefront` | The storefront for the request. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Example endpoint

```
GET 
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```

##### Expected response

Braze expects a `200` status code. Any other code is considered a failure.

{% raw %}
```json
{ 
    "external_id": "my_external_id" 
}
```
{% endraw %}

{% alert important %}
It's important to validate that the `shopify_customer_id` and `email_address` match the customer values in Shopify. You can use the [Admin API](https://shopify.dev/docs/api/admin-graphql) or [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) to validate these parameters and retrieve the `braze.external_id` metafield.
{% endalert %}

#### Step 4.3: Input your external ID

Repeat [Step 4](#step-4-choose-an-external-id-type), and enter your endpoint URL after selecting custom external ID as your Braze external ID type.

##### Considerations

- If your external ID isn't generated when Braze sends a request to your endpoint, the integration will default to using the Shopify customer ID when the `changeUser` function is called. This step is crucial for merging the anonymous user profile with the identified user profile. As a result, there may be a temporary period during which different types of external IDs exist within your workspace.
- When the external ID is available in the `braze.external_id` metafield, the integration will prioritize and assign this external ID. 
    - If the Shopify customer ID was previously set as the Braze external ID, it will be replaced with the `braze.external_id` metafield value. 

### Step 5: Enable the Braze app embed

To enable the Braze app embed within your store's theme, go back to Braze and then select **Go to Shopify**.

![Shopify upgrade panel with a button to enable the Braze app embed.]({% image_buster /assets/unlisted_docs/img/shopify/enable_app_embed.png %}){: style="max-width:35%;"}

On the Shopify site, enable the Braze app embed, then save your changes.

![An example app embed.]({% image_buster /assets/unlisted_docs/img/shopify/app_embed.png %})

### Step 6: Verify the upgrade

Back in Braze, you'll be alerted when your Shopify integration is finished installing.

![Shopify integration page with a success banner.]({% image_buster /assets/unlisted_docs/img/shopify/success_integration.png %})

To verify that your new Shopify connector is live, test the following:

- **Active Canvases, campaigns, and segments:** Confirm that they are functioning properly.
- **Identity management processes:** Confirm that these processes are working as expected.
- **SDK customizations (optional):** If you made any customizations to your Braze and Shopify integration (such as logging custom events or attributes), verify that they are working correctly after the upgrade.
- **Email or SMS subscriber collection (optional):** If you previously enabled email or SMS subscriber collection, new default subscription groups will be created to reflect the latest status of your subscribers during the upgrade. The default subscription groups will be the name of your Shopify storefront. These new default subscription groups will be available approximately 5 hours after the upgrade, and you'll need to add them to your active messages.

If you have any questions, [contact Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/).
