---
nav_title: Shopify for Currents
article_title: Shopify for Currents
description: "This reference article outlines the partnership between Braze Currents and Shopify, a global commerce company that allows you to seamlessly connect Braze with your Shopify store to power internal reporting and better track last-touch attribution for purchases."
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify for Currents

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a business of any size. Shopify's platform and services are engineered for reliability while delivering a better shopping experience for consumers everywhere.

{% alert important %}
This integration is currently in beta. For more information, contact your Braze customer success manager.
{% endalert %}

The Braze integration with Shopify provides a powerful solution for eCommerce businesses looking to enhance their customer engagement and drive personalized marketing efforts. With [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), you can connect data to Shopify to power internal reporting and better track last-touch attribution for purchases.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Currents | To export data into Shopify, you must have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| Shopify store | Be sure that you've already [set up at least one Shopify store with Braze]({{site.baseurl}}/shopify_standard_integration/). |
| Shopify store owner or staff member permissions | {::nomarkdown}<ul><li>Access to all <b>General</b> and <b>Online Store</b> settings.</li><li> Additional administrator permissions:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Set up your Shopify Store

If you have not already, follow [Shopify standard integration setup]({{site.baseurl}}/shopify_standard_integration/) steps to set up at least one Shopify store with Braze.

### Step 2: Create Braze Current

1. In Braze, go to **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**.
2. Provide an integration name and contact email.
3. In the **Credentials** section, select the Shopify store that you set up in [Step 1](#step-1-set-up-your-shopify-store).
4. Select the events you want to track. A list of available events is provided.
5. Select **Launch Current**

![The Braze Shopify Currents page. This page includes fields for integration name, contact email, and Shopify Store.]({% image_buster /assets/img/shopify/shopify_currents.png %})
