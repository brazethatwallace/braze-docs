## Banner editor blocks

In the Banner composer, drag rows and blocks from the **Build** section into the canvas to lay out your message. Select **Styles** to adjust page-level styling, or select a block or row to edit its properties in the side panel.

For the full Banner creation flow, see [Create a Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner).

The Banner composer offers the same kinds of layout blocks as other drag-and-drop surfaces, but not the full form block set (for example no radio button, short text, dropdown, or checkbox blocks). You can add **Phone capture** and **Email capture** blocks; only **one** phone capture and **one** email capture block are allowed per message.

### Title and paragraph

Adds heading or body text with rich text options.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Adds a clickable button. You can set links and analytics options in the properties panel.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

For more information, see [Define on-click behavior]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) in the Banner article.

### Image

Displays an image from a hosted URL. Configure display options in the properties panel.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Inserts a hyperlink users can select.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Spacer

Adds vertical spacing between blocks.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Custom code

Inserts custom HTML for advanced layouts or embedded content (for example video). Clicks inside custom HTML are not tracked unless you call `brazeBridge.logClick()` — see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/).

| Property | Description |
| --- | --- |
| Custom code | Add or edit HTML (and related assets) for the Banner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### Phone capture

Collects a phone number. On submit, subscribes the user to your selected [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) subscription group. Only one per Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Email capture

Collects an email address and adds it to the user's Braze profile on submit. Only one per Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Long text

Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Things to know

- **Video:** The standard composer does not include a dedicated video block. Use **Custom code** to embed a player if needed. For more information, see [Banners: Frequently Asked Questions]({{site.baseurl}}/user_guide/channels/banners/faq/).
- **Liquid:** Most Liquid is supported; there are exceptions such as catalog rerender tags. For more information, see [Banners: Frequently Asked Questions]({{site.baseurl}}/user_guide/channels/banners/faq/).
