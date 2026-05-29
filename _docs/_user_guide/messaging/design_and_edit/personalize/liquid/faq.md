---
nav_title: FAQ
article_title: Frequently Asked Questions
page_order: 12
description: "This article provides answers to frequently asked questions about Liquid."

---

# Frequently asked questions

> On this page, you'll find answers to some frequently asked questions about Liquid.<br><br>Braze does not currently support 100% of Shopify’s Liquid, only certain portions which we have attempted to outline in our documentation. We highly recommend testing all messages using Liquid before sending them to reduce the risk of errors or using unsupported Liquid.

### How do I use Liquid snippets in Braze?

In many cases, you can incorporate Liquid snippets by navigating to your campaigns or Canvases, and inserting Liquid in the personalization modal in areas such as the email message body or in your segments. 

#### Where can I learn more?

For more on Liquid, check out our guided [Dynamic Personalization with Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze Learning path! You can also reference the [Liquid use case library]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/) for inspiration and a range of personalization examples using Liquid.

### What’s the difference between using Liquid and Connected Content for personalization?

Braze Connected Content is an example of a Liquid tag. It's also used for personalization, but this data comes from an external endpoint rather than stored data within Braze. Check out our dedicated [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) section to learn more about expanding how you can personalize your messages.

### What is Liquid templating?

This is the most common way of using Liquid in Braze. Liquid templating involves pulling data from a user's profile into a message. This data can range from a user's first name to custom events from an event triggered message.

Refer to [Supported personalization tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) for a complete list of the supported Liquid tags.

### How do I assign variables with Liquid?

You can create and assign variables by using the `assign` tag. This creates a variable in the message composer that can also be referenced throughout your message.

### Does using Liquid log data points?

No.

### How can I use Liquid to send a personalized greeting?

For a personalized greeting using a user's first name, you can pull the standard user profile attributes such as {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

You can also use a Liquid `{% if X %}` {% endraw %}statement to do conditional rendering based on anything, such as the day of the week or custom attributes. For more information on the supported Liquid operators that can be used in conditional statements, check out [Operators]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/).

### How can I personalize a message based on a customer’s location?

{% raw %}
There is a default attribute for the user’s location: `{{${most_recent_location}}}`.

### What's the difference between {{campaign.${name}}} and {{campaign.${message_name}}}?

Both `{{campaign.${name}}}` and `{{campaign.${message_name}}}` are supported Liquid personalization tags. Both tags reference campaign attributes. `{{campaign.${name}}}` denotes the name of your campaign, and `{{campaign.${message_name}}}` is the name of your message variant.
{% endraw %}

For URL and query string use (for example, when a name contains `%` or spaces), see [Campaign names in URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#campaign-names-in-urls).

### How do I use Liquid with nested objects?

Braze has a built-in feature that generates Liquid code for segments that can be used in a message. Specifically, you can create a segment that matches multiple criteria in an object.

For more information, check out [Multi-criteria segmentation]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#multi-criteria-segmentation).

### How do I use event attributes to personalize a message that an event is triggering?

{% raw %}
You can access properties of API triggered events with the `api_triggered_property` tag: `{{api_trigger_properties.${attribute_key}}}`.  
{% endraw %}

### Why is my API-triggered Liquid failing in Braze?

{% raw %}
An extra pair of curly braces is a common cause. For example, `{{{api_trigger_properties.${attribute_key}}}}` is not valid Braze personalization syntax. Use exactly two opening braces and two closing braces: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### What is abort logic, and how can I use it?

Abort logic allows you to stop a message from being sent if the conditions are met. This is especially helpful in preventing incomplete messages from being sent to your users. For examples of abort logic in your marketing campaigns, read more at [Aborting messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/).

### What is for loop logic, and how can I use it?

For loops are also known as [iteration tags](https://shopify.github.io/liquid/tags/iteration/). Using for loop logic in your Liquid snippets allows you to cycle through blocks of Liquid until a condition is met. 

In Braze, this could be used for checking items in an array custom attribute, or a list of values and objects returned by a [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/), [selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/), or [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) call response. Specifically, you can use for loop logic as part of your messaging to check whether a product is in stock, or if a product has a minimum rating. 

For example, let's say you have a catalog called "Games" that has a selection called "cheap_games". To pull the titles of the games in "cheap_games", you could use this Liquid snippet:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Once the set conditions are met, your message can proceed. Using this logic is a helpful way to save time, instead of repeating Liquid blocks for different conditions.

### Why is there extra spacing in messages that use Content Blocks?

If you notice extra spacing in sent messages that use Content Blocks with Liquid, you may have unnecessary paragraph or line breaks within your conditional statements. Write your conditional statements on a single line rather than across multiple lines.

#### Example

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### When should I use `assign` versus `capture`?

Both `assign` and `capture` create Liquid variables, but they serve different purposes:

- `assign` is for simple variables that store a single value, such as a boolean, number, or simple string. You can also apply a single filter in the same line.
- `capture` is for storing a block of text that may include multiple variables, strings, or complex expressions. 

Use `capture` when the value is too complex for a single `assign` statement, such as URLs that use other Liquid variables or custom attributes as parameters. `capture` is also preferred when implementing Liquid variables in the body of Connected Content calls.

#### Examples

{% raw %}
```liquid
{% comment %}Use assign for custom attributes{% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %}Use assign for a simple variable{% endcomment %}
{% assign discount_label = "20% off" %}
Hello {{ customer.first_name | default: "there" }}, enjoy {{ discount_label }} on your next order!

{% comment %}Use capture for complex strings{% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}

{% comment %}Use capture to create conditional content{% endcomment %}
{% capture promo_block %}
{% if customer.vip == true %}
As a VIP member, you get free shipping.
{% else %}
Join our VIP program to unlock free shipping.
{% endif %}
{% endcapture %}
```
{% endraw %}

### Do Liquid variables carry between subject line and body?

No. Braze renders each message component separately (such as subject line, HTML body, preheader, and push title). Assignments or captures you make in one field are not available in another. Repeat the Liquid or Connected Content call in each field that needs the value.

<!-- sf-kb-phase2-batch -->

## Salesforce Knowledge updates

### Can I supply liquid inside the abort_message tag?

it accepts only a static string; Liquid personalization is not supported. Consider adding to Liquid personalization or abort logic docs.

### Why am I facing an error Unexpected end token when working with Liquid?

Add troubleshooting section to liquid/faq.md or using_liquid.md: 'Unexpected end token' typically caused by extra or missing curly braces. Example: {{${date_of_birth}} | date: '%s'} should not have nested {{}} inside. Link to Liquid syntax and use case library.

### Aborted Message Error "Invalid from email address for recipient:"

Add troubleshooting to outbound email settings: 'Invalid from email address' error when Liquid produces invalid syntax (missing variable, spaces, disallowed chars).

### Why is my content block not appearing under 'Row' in the DnD search tool?

If your Content Block does not appear under Row in the DnD search tool, you can add it via Liquid: add an HTML block (under Advanced in the Content tab), then insert the Content Block Liquid Tag. The HTML will display the Content Block content.

### How Do I Create A Dynamic 'Reply-To' Email Address?

Consider adding a short troubleshooting/guru section on dynamic Reply-To setup (exclude-reply address + Customize From Display Name checkbox) or cross-link from email_settings to a dedicated article. Alternatively archive KA if docs cover this.

### DnD content block preview different from compose view

When templating via Liquid, media queries for mobile may be ignored; dragging the content block in preserves layout. Tradeoff: drag-in is not linked (no auto-updates).

### Are There Size Limits of Canvas Entry Properties Object?

Add a section to braze-docs on Canvas entry properties (e.g., in Canvas or Liquid personalization docs) documenting: no formal limit; recommend keeping under 1Kb (~1000 characters); larger objects may cause memory pressure and message delays during mass sends. Cite platform usage of canvas_entry_properties.

### Why is my Liquid snippet containing Catalog items returning an abort message?

Add troubleshooting to docs: if Catalog Liquid snippet aborts, create snippet via Personalization menu with individual catalog item selections rather than bulk/dynamic selection. Verify Catalogs + Liquid docs for this workflow.

### Liquid Error Occurs On The Dashboard When Previewing Some Data Types

Consider adding Liquid workaround for canvas_entry_properties type coercion (plus: 0 filter) to Liquid FAQ or personalization docs if not already present.

### IAM Campaign Error: Warning: Use of the {% connected_content %} tag with retry is not available for this message type.

Add IAM + connected content retry limitation to Liquid or IAM docs.

### Liquid: Event Property Values in Message Composer Preview Mode

Preview as Custom User allows inputting sample custom event properties for Liquid templating. Also useful for messages with abort logic (preview values that prevent condition trigger).

### Do we support an array of arrays in Liquid?

Consider adding to Liquid/custom attributes docs: Liquid does not natively support array of arrays; workaround is to store as array of comma-separated strings and use split filter. Link to Shopify Liquid split filter.
