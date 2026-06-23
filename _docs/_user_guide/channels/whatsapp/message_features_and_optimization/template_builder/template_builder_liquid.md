---
nav_title: Liquid
article_title: Liquid in the WhatsApp Template Builder
description: "This reference article covers Message Extras and conditional Liquid logic in the WhatsApp Template Builder."
alias: /whatsapp_template_builder_liquid/
page_type: reference
channel:
  - WhatsApp
page_order: 1
---

# Liquid in the WhatsApp Template Builder

> You can use Liquid to personalize templates in the WhatsApp Template Builder, but Meta's template structure creates constraints that don't exist in other Braze channels. Two Liquid patterns in particular require special handling: Message Extras and conditional messaging logic.

For Message Extras and conditional messaging logic, Meta requires that each variable in a template contains actual rendered content at send time. Variables that pull in empty strings, or that behave as invisible metadata rather than visible text, cause send failures. Conditionals that change the static message structure rather than only the variable's content also causes unexpected behavior.

{% alert note %}
The constraints described in this article apply only to template messages (outbound messages that use a Meta-approved template). The constraints don't apply to Response messages (sent within a 24-hour messaging window opened by a user), or Message Extras, conditional logic, and other Liquid patterns in other Braze channels.
{% endalert %}

## Overview

| Pattern | Supported? | Notes |
| ----- | ----- | ----- |
| `message_extras` inside a variable with other visible content | ✅ Yes | Tag is captured; visible text satisfies Meta's variable content requirement |
| `message_extras` as the sole content of a variable | ❌ No | Resolves to empty string; causes send failure |
| Conditional Liquid inside a variable slot | ✅ Yes | Braze evaluates before send; Meta only sees the final rendered value |
| Conditional Liquid outside a variable slot | ❌ No | Liquid tags rendered as literal text; recipient sees raw syntax |
| Template starting or ending with a variable slot | ❌ No | Meta requires static text at the start and end of every template |
| Variable slot that resolves to an empty string | ❌ No | Meta requires non-empty content in every variable at send time |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Quick Reference" }

## Message Extras

The [`message_extras` Liquid tag]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras/) lets you annotate a message with key-value metadata at send time. This data is not rendered in the message body. Instead, the data flows to Connected Content, Currents, or other data capture mechanisms for purposes like attribution, impact measurement, and event enrichment.

{% raw %}
```liquid
{% message_extras :key campaign_id :value "spring_promo_2025" %}
```
{% endraw %}

### Why standalone Message Extras variables fail

In the WhatsApp Template Builder, template variables (such as {% raw %}`{{1}}`, `{{2}}`{% endraw %}) map directly to Liquid expressions. Meta's validation requires that every variable slot in the approved template contains non-empty content at send time, it must be something that would render as visible text to the recipient.

Because `message_extras` don't render output, placing it alone inside a template variable submits an empty string for that variable slot. Meta rejects this, so the message sending fails.

{% details Incorrect usage for the WhatsApp Template Builder %}

{% raw %}
```
Template variable {{1}}: {% message_extras :key attribution_source :value "canvas_a" %}
```
{% endraw %}

At send time, {% raw %}`{{1}}`{% endraw %} resolves to an empty string, causing a send failure.

{% enddetails %}

### Correct usage

To correctly include a `message_extras` tag, embed the tag in an existing variable. This means placing the tag inside a Liquid block that produces visible output; specifically, inside the same expression that populates a real template variable. Meta accepts the variable because it contains content, Braze captures the metadata, and the recipient sees only the rendered text.

#### Example

Let's say the template body is:

{% raw %}
```
Hi {{1}}, your order has shipped.
```
{% endraw %}

And the variable {% raw %}`{{1}}`{% endraw %} is mapped to:

{% raw %}
```
{{ ${first_name} | default: "there" }}
```
{% endraw %}

To attach a Message Extra, rewrite the variable expression as:

{% raw %}
```
{{ ${first_name} | default: "there" }}{% message_extras :key order_source :value "canvas_spring" %}
```
{% endraw %}

At send time, {% raw %}`{{1}}`{% endraw %} resolves to something like `"Alex"`, visible content that satisfies Meta's requirement. The `message_extras` tag is evaluated and its data is captured, but it contributes nothing to the rendered string the recipient sees.

### Key rules

- Never assign `message_extras` as the sole content of a template variable.
- Always attach the tag to a variable that resolves to visible text.
- You can append multiple `message_extras` tags to the same variable expression without affecting the rendered output.
- Use this pattern in the body, header, and any other variable slots.

## Conditional messaging logic

In messaging channels, Liquid `if/elsif/else` blocks can conditionally include or exclude entire sections of text. Braze renders the full Liquid output before sending, and the result is whatever the logic produces.

However, Meta-approved WhatsApp templates have a fixed structure. Meta thinks of template content in two categories:

- **Static text:** Hardcoded strings that are confirmed at template creation and remain identical for every recipient.
- **Variable slots:** Placeholder positions (such as {% raw %}`{{1}}`{% endraw %}) whose content is filled at send time.

### Why conditional messaging logic outside a variable slot fails

The ratio of static text to variable slots in an approved template is fixed and can't change per send, and has hard limits. Meta requires a minimum amount of static text for every variable slot in the template; you can't have a template that is mostly or entirely variables. This means you can't include conditional Liquid that would add or remove text that Meta sees as confirmed static content.

If you try using an `if/else` block to conditionally include or exclude a chunk of static text, Meta won't evaluate the logic. Liquid tags outside of a variable slot are treated as literal output text. The recipient will see the raw Liquid syntax tags ({% raw %}`{% if %}`, `{% else %}`, `{% endif %}`{% endraw %}) and all branch content verbatim in their message.

{% details Incorrect usage for the WhatsApp Template Builder %}

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}Hi {{1}}, we have an exclusive Gold member offer.{% else %}Hi {{1}}, we have a special offer for you.{% endif %}
```
{% endraw %}

This tries to include two different approved templates in one. The conditional wrapping static text won't behave as expected.

{% enddetails %}

### Correct usage

Conditionals are valid and supported inside a variable slot, where they control what value fills that variable. Meta only sees that {% raw %}`{{1}}`{% endraw %} was populated with content; it doesn't inspect how the Liquid inside arrived at that value.

#### Example

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}exclusive Gold member{% else %}valued customer{% endif %}
```
{% endraw %}

Used as the value for a template variable, this produces either `"exclusive Gold member"` or `"valued customer"`. Both are non-empty strings that satisfy Meta's variable content requirement.

The template body itself remains structurally unchanged:

{% raw %}
```
Hi {{1}}, we have a special offer for you.
```
{% endraw %}

### Place conditional logic inside a variable slot

There are two ways to place conditional Liquid into a variable slot in the Template Builder:

1. **Use a Content Block (supports prefill):** Build your conditional logic inside a Content Block, then reference the Block from the variable. This approach supports prefill, meaning the variable can display a preview value in the Template Builder before send.
2. **Use a placeholder and paste Liquid (no prefill):** Add a placeholder like {% raw %}`{{1}}`{% endraw %} when creating the template, then paste your full Liquid expression directly into that variable slot. This approach doesn't support prefill, but it works for any Liquid logic.

### Other Liquid components affected by the same constraint

Any Liquid tag that doesn't produce visible output is rendered as raw text if placed outside a variable. This includes:

- **`catalog_items`:** Liquid that looks up and references Catalog data must be inside a variable slot, or the tags appears verbatim in the message.
- **`assign`:** Variable assignment tags (such as {% raw %}{% assign discount = "20%" %}{% endraw %}) don't produce output themselves. If used outside a variable slot to set up a value for later use in the message, the `assign` tag renders literally. Include any `assign` logic at the start of the Liquid expression inside the variable slot where its output is needed.
- **Content Blocks containing only Liquid tags:** If a Content Block contains Liquid logic but doesn't produce visible text (for example, it only uses `assign` or `message_extras` tags), referencing it outside a variable slot causes the raw block content to appear in the message. Content Blocks that don't produce visible output must be embedded inside a variable slot alongside content that does render.

### Additional structural constraints

Meta requires that templates:

- **Begin with static text.** Templates can't open with a variable slot (such as {% raw %}`{{1}} is ready for you`{% endraw %}).
- **End with static text.** Templates can't end on a variable slot.

These constraints exist regardless if Liquid is used. They apply to the approved template structure itself.

### Key rules

- Use conditionals freely inside variable slot expressions to control what value is rendered.
- Don't use conditionals to add, remove, or swap static text (the parts of the message that are not variable slots).
- Make sure every conditional branch inside a variable produces a non-empty string (see [Message Extras](#message-extras) for why empty strings cause failures).
- The template must begin and end with static text as submitted to Meta.
