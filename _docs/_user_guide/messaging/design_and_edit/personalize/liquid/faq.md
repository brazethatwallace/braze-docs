---
nav_title: FAQ
article_title: Frequently Asked Questions
page_order: 12
description: "This article provides answers to frequently asked questions about Liquid."
toc_headers: h2
---

# Frequently asked questions

> On this page, you find answers to frequently asked questions about Liquid.

{% alert note %}
Braze does not currently support 100% of Shopify's Liquid, only certain portions, which we have attempted to outline in our documentation. Test all messages using Liquid before sending them to reduce the risk of errors or using unsupported Liquid.
{% endalert %}

## About Liquid in Braze

### How do I use Liquid snippets in Braze?

In many cases, you can incorporate Liquid snippets by going to your campaigns or Canvases and inserting Liquid in the personalization modal in areas such as the email message body or in your segments.

#### Where can I learn more?

For more on Liquid, check out our guided [Dynamic Personalization with Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze Learning path. You can also reference the [Liquid use case library]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) for inspiration and a range of personalization examples using Liquid.

### What's the difference between using Liquid and Connected Content for personalization?

Braze Connected Content is an example of a Liquid tag. It's also used for personalization, but this data comes from an external endpoint rather than stored data within Braze. Check out our dedicated [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) section to learn more about expanding how you can personalize your messages.

### What is Liquid templating?

This is the most common way of using Liquid in Braze. Liquid templating involves pulling data from a user's profile into a message. This data can range from a user's first name to custom events from an event triggered message.

Refer to [Supported personalization tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) for a complete list of the supported Liquid tags.

### Does using Liquid log data points?

No.

## Personalization tags and data sources

### How can I use Liquid to send a personalized greeting?

For a personalized greeting using a user's first name, pull the standard user profile attributes such as {% raw %}`{{${first_name}}}` and `{{${last_name}}}`{% endraw %}.

You can also use a Liquid {% raw %}`{% if X %}`{% endraw %} statement to do conditional rendering based on anything, such as the day of the week or custom attributes. For more information on the supported Liquid operators that can be used in conditional statements, check out [Operators]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### How can I personalize a message based on a user's location?

{% raw %}
There is a default attribute for the user's location: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### What's the difference between {{campaign.${name}}} and {{campaign.${message_name}}}?

Both `{{campaign.${name}}}` and `{{campaign.${message_name}}}` are supported Liquid personalization tags. Both tags reference campaign attributes. `{{campaign.${name}}}` denotes the name of your campaign, and `{{campaign.${message_name}}}` is the name of your message variant.
{% endraw %}

For URL and query string use (for example, when a name contains `%` or spaces), see [Campaign names in URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### How do I use Liquid with nested objects?

Braze has a built-in feature that generates Liquid code for segments that can be used in a message. Specifically, you can create a segment that matches multiple criteria in an object.

For more information, check out [Multi-criteria segmentation]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects).

### How do I use event attributes to personalize a message that an event is triggering?

{% raw %}
You can access properties of API triggered events with the `api_triggered_property` tag: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Does Braze support an array of arrays in Liquid?

Liquid does not natively support arrays of arrays. Store values as an array of comma-separated strings and use the `split` filter to parse them when needed.

## Variables and syntax

### How do I assign variables with Liquid?

You can create and assign variables by using the `assign` tag. This creates a variable in the message composer that can also be referenced throughout your message.

You can split an `assign` across multiple lines if you wrap all Braze Liquid variables with double curly braces (`{{ }}`). Without those braces, multi-line assign statements can cause unexpected rendering, including custom attributes that fail to template. For examples and related syntax rules, see [Use Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

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

### What is for loop logic, and how can I use it?

For loops are also known as [iteration tags](https://shopify.github.io/liquid/tags/iteration/). Using for loop logic in your Liquid snippets allows you to cycle through blocks of Liquid until a condition is met.

In Braze, this could be used for checking items in an array custom attribute, or a list of values and objects returned by a [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs), [selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections), or [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) call response. Specifically, you can use for loop logic as part of your messaging to check whether a product is in stock, or if a product has a minimum rating.

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

### What is abort logic, and how can I use it?

Abort logic allows you to stop a message from being sent if the conditions are met. This is especially helpful in preventing incomplete messages from being sent to your users. For examples of abort logic in your marketing campaigns, read more at [Aborting messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### Can I use Liquid inside the `abort_message` tag?

No. The {% raw %}`{% abort_message %}`{% endraw %} tag accepts a static string in quotes, not Liquid personalization. Use other Liquid logic before the tag if you need conditional abort behavior.

### How do I mask phone numbers with Liquid?

You can mask phone numbers using the `slice` filter to extract specific digits and the `append` filter to combine them with masking characters.

#### Mask all but the last four digits

To display a 10-digit phone number as `******7890`:

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | split: '' %}
{% assign masked_phone = '' %}
{% for i in (0..5) %}
  {% assign masked_phone = masked_phone | append: '*' %}
{% endfor %}
{% for i in (6..9) %}
  {% assign masked_phone = masked_phone | append: phone[i] %}
{% endfor %}
{{ masked_phone }}
```
{% endraw %}

#### Show the first three and last four digits

To display a 10-digit phone number as `123***7890`:

{% raw %}
```liquid
{% assign first_part = {{${phone_number}}} | slice: 0, 3 %}
{% assign last_part = {{${phone_number}}} | slice: -4, 4 %}
{% assign masked_phone_number = first_part | append: "***" | append: last_part %}
{{ masked_phone_number }}
```
{% endraw %}

## Canvas, catalogs, and trigger properties

### Why is my API-triggered Liquid failing in Braze?

{% raw %}
An extra pair of curly braces is a common cause. For example, `{{{api_trigger_properties.${attribute_key}}}}` is not valid Braze personalization syntax. Use exactly two opening braces and two closing braces: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Are there size limits for Canvas context properties?

Braze does not enforce a hard limit on [Canvas context properties]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), but keep payloads under approximately 1 KB (~1,000 characters). Larger objects can increase memory use and delay message rendering during high-volume sends.

### Why do I get a Liquid error when previewing certain data types in the dashboard?

Some [Canvas context property]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) types require coercion in Liquid before you use them in comparisons or math. For example, when you need numeric behavior:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### Why does my catalog Liquid snippet return an abort message?

If a catalog Liquid snippet aborts during send, recreate the snippet from the personalization menu by selecting individual catalog items instead of using a bulk or fully dynamic selection. See [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs) and [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks and the message composer

### Why is there extra spacing in messages that use Content Blocks?

If you notice extra spacing in sent messages that use Content Blocks with Liquid, you may have unnecessary paragraph or line breaks within your conditional statements. Write your conditional statements on a single line rather than across multiple lines.

#### Example

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}


### Why does multi-line Liquid create unexpected whitespace in the drag-and-drop editors?

When Liquid code is spread across multiple lines in the in-app message drag-and-drop editor or email drag-and-drop editor, each {% raw %}`{% %}`{% endraw %} block renders as non-visible text. The line breaks are preserved as empty lines before the visible output, causing unexpected whitespace.

#### Solution 1: Use whitespace control tags (recommended)

Add hyphens inside the tag delimiters to strip surrounding whitespace while keeping code readable:

{% raw %}
```liquid
{%- assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" -%}
{%- assign today = 'now' | date: "%s" -%}
{%- assign difference = event_date | minus: today -%}
{%- assign difference_days = difference | divided_by: 86400 -%}
Only {{ difference_days }} days until your move!
```
{% endraw %}

#### Solution 2: Consolidate Liquid onto a single line

Remove all line breaks so the Liquid is on one continuous line:

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" %}{% assign today = 'now' | date: "%s" %}{% assign difference = event_date | minus: today %}{% assign difference_days = difference | divided_by: 86400 %}Only {{ difference_days }} days until your move!
```
{% endraw %}

Both approaches prevent unwanted empty lines in your rendered message. This applies to the in-app message drag-and-drop editor, the email drag-and-drop editor, and Content Blocks with Liquid. For more information, see Shopify's [Whitespace control](https://shopify.github.io/liquid/basics/whitespace/) documentation and Braze [Liquid syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### Why is my Content Block missing from **Row** in the drag-and-drop search tool?

Some Content Blocks do not appear under **Row** in the drag-and-drop editor search. Add an HTML block from the **Content** tab (**Advanced**), then insert the Content Block Liquid tag in that HTML block to render the block content.

### Why does my drag-and-drop Content Block preview differ from the compose view?

When you template a Content Block with Liquid, mobile media queries in the block may not apply in the preview the same way they do when you drag the block directly into a message. Dragging the block preserves layout but decouples it from the source block, so future block edits no longer update the message automatically.

### How do I preview event property values in Message Composer?

Use **Preview as Custom User** and enter sample custom event property values for the user you preview. This is also useful for messages with abort logic when you need preview values that do not trigger an abort.

## Liquid in email messages

### Why does my message abort with "Invalid from email address for recipient:"?

This abort occurs when Liquid in the **From** address produces invalid syntax, such as a missing variable, extra spaces, or disallowed characters. Preview with a test user and verify the rendered **From** address matches your configured sending domain.

### How do I create a dynamic Reply-To address?

Use Liquid in the **Reply-To** field when your workspace supports dynamic Reply-To configuration. Pair it with your **From** display name settings as needed. See [Email settings]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) for workspace-specific options.

## Troubleshooting Liquid errors

### Why is my Liquid code not working when it looks correct?

If your Liquid code appears syntactically correct but isn't working, check for smart quotes (curly quotes like `' '` or `" "`) and smart dashes (em dashes like `—`) instead of straight quotes (`' '` or `" "`) and hyphens (`-`). Liquid only recognizes straight ASCII characters, so smart quotes and dashes will cause parsing errors.

This commonly happens when the macOS keyboard setting **Use smart quotes and dashes** is enabled, which automatically converts characters as you type in the Braze dashboard.

To disable this setting on macOS:

1. Go to **System Settings** > **Keyboard** > **Text Input** > **Edit**.
2. Uncheck **Use smart quotes and dashes**.

| Example | Curly quotes (does not work) | Straight quotes (works) |
| --- | --- | --- |
| Default value | {% raw %}`{{${first_name} | default: ‘Torchie’}}`{% endraw %} | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} |
| Conditional | {% raw %}`{% if ${country} contains ‘US’ %}`{% endraw %} | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Smart quote examples" }

This applies to default values, conditionals, and any other Liquid that uses quotes. Curly and straight quotes can look the same on screen, so compare your code carefully or paste it into a plain-text editor.

For more information on quote usage in Liquid, see [Liquid syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### Why am I seeing an "Unexpected end token" Liquid error?

This error usually indicates extra or missing curly braces. Do not nest {% raw %}`{{ }}`{% endraw %} inside another Liquid tag expression. For example, use {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %} rather than wrapping the attribute reference in an additional pair of braces.

### Why is Connected Content retry unavailable for my in-app message?

{% raw %}
The `{% connected_content %}` tag with retry is not supported for all message types, including some in-app message formats. Remove retry parameters or use a supported channel for retried Connected Content calls.
{% endraw %}

### Why am I seeing "Liquid Error: Comparison of Time with String Failed"?

This error occurs when comparing a time custom attribute or event property directly to a blank value (an empty string). Liquid does not support direct comparisons between different data types, such as a time object and a string.

The following is a common example that causes this error:

{% raw %}
```liquid
{% if {{custom_attribute.${expiration_date}}} == blank %}
  <a>Some words</a>
{% endif %}
```
{% endraw %}

This fails because you cannot compare a custom attribute with a data type of time to a string (`blank`).

To resolve this, convert the time attribute to a string by assigning it to a variable and using the `default` filter when the attribute evaluates to blank at render time:

{% raw %}
```liquid
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% endif %}
```
{% endraw %}


When comparing a time custom attribute against the current time or future dates, use the same approach:

{% raw %}
```liquid
{% assign today = 'now' | date: '%s' %}
{% assign month = 'now' | date: '%s' | plus: 2592000 %}
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% elsif expiration_date >= today and expiration_date >= month %}
  <a>More Words</a>
{% endif %}
```
{% endraw %}
