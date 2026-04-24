## Banner editor blocks

In the Banner composer, drag rows and blocks from the **Build** section into the canvas to lay out your message. Select **Styles** to adjust page-level styling, or select a block or row to edit its properties in the side panel.

For the full Banner creation flow, see [Create a Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner).

## Types

The Banner composer offers the same kinds of layout blocks as other drag-and-drop surfaces, but **not** the full in-app form set (for example no radio button, short text, dropdown, or checkbox blocks). You can add **Phone capture** and **Email capture** blocks; only **one** phone capture and **one** email capture block are allowed per message.

| Name | Description |
| --- | --- |
| Title | Adds a heading or title line in the Banner. |
| Paragraph | Adds body text with rich text options. |
| Button | Adds a clickable button. You can set links and, where available, analytics options similar to other drag-and-drop surfaces. |
| Image | Displays an image from a hosted URL and options you set in the properties panel. |
| Link | Inserts a hyperlink users can select. |
| Spacer | Adds vertical spacing between blocks. |
| Custom code | Inserts custom HTML for advanced layouts or embedded content (for example video). Requires explicit click tracking in HTML—see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/). |
| Phone capture | Collects a phone number. When submitted, subscribes the user to your selected [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) subscription group. Only one per Banner. |
| Email capture | Collects an email address and adds it to the user's Braze profile when submitted. Only one per Banner. |
| Long text | Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. It appears when survey mode is on. |
| Saved row | Inserts a reusable row you saved earlier. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" %}

## Properties

### Title and paragraph

For typography and alignment, see [Title and Paragraph]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_title-and-paragraph) under in-app message editor blocks.

### Button

For button styling properties, see [Button]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_button) under in-app message editor blocks.

For on-click behavior and logging, see [Actions]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_actions) under in-app message editor blocks, and [Define on-click behavior]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) in the Banner article.

### Image

For image styling properties, see [Image]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_image) under in-app message editor blocks.

For image actions (alt text, click behavior, logging), see [Actions]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_actions) in that tab.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Link

For link text styling, see [Link]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_link) under in-app message editor blocks.

For link actions, see [Actions]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_actions) in that tab.

### Spacer

For spacer properties, see [Spacer]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_spacer) under in-app message editor blocks.

### Custom code

| Property | Description |
| --- | --- |
| Custom code | Add or edit HTML (and related assets) for the Banner. Clicks inside custom HTML are not tracked unless you call `brazeBridge.logClick()`—see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" %}

### Phone capture and email capture

For property fields and subscription behavior, see [Phone capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_phone-capture) and [Email capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_email-capture) under in-app message editor blocks. You can only add **one** phone capture block and **one** email capture block per Banner.

### Long text

When **Long text** is available in your workspace, it behaves like the in-app message long-text block for survey-style flows. Use the properties panel after you place the block. Where options match in-app messages, you can follow the same patterns as in the **in-app messages** tab on this page.

### Saved row

When **Saved row** appears under **Rows**, you can insert reusable content from your library. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/).

## Things to know

- **Video:** The standard composer does not include a dedicated video block. Use **Custom code** to embed a player if needed. For more information, see [Banners: Frequently Asked Questions]({{site.baseurl}}/user_guide/channels/banners/faq/).
- **Liquid:** Most Liquid is supported; there are exceptions such as catalog rerender tags. For more information, see [Banners: Frequently Asked Questions]({{site.baseurl}}/user_guide/channels/banners/faq/).
