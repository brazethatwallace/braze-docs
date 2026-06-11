## In-app message editor blocks

Editor blocks are in the **Build** section for in-app messages. Drag a block into a column; it auto-adjusts to the column width. Select a block to edit its settings in the right-side panel.

For more information about creating in-app messages in the **Drag-And-Drop Editor**, see [Create an in-app message with drag-and-drop]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/).

### Title and paragraph

Adds title or paragraph text to the message.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Adds a standard button with configurable styling, links, and analytics.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Radio button

Adds a list of options from which users can select one. When submitted, the user profile logs the associated [custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), which must be a string to be saved. Custom attributes with other data types do not save to the user profile.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Image

Inserts an image from the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

For image specifications, refer to our [in-app message image specifications]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/#in-app-messages).

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Spacer

Adds space or padding between other blocks.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Custom code

Inserts custom HTML, CSS, or JavaScript for advanced customization.

| Property | Description |
| --- | --- |
| Custom code | Allows you to add, edit, or delete HTML, CSS, and JavaScript for an in-app message. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### Phone capture

Inserts a form field for phone numbers. When submitted, the user is subscribed to the [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp subscription group]({{site.baseurl}}/whatsapp_subscription_groups/).

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Email capture

Inserts a form field for email addresses. When submitted, the email address is added to that user's profile in Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Short text

Inserts a form field that supports standard attributes (such as first and last name) or a custom attribute string of your choice.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Dropdown

Inserts a dropdown with a predefined list of items from which users can select one. You can add any custom attribute strings to the list.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Checkbox

Inserts a checkbox. If the user checks the box, the block's [boolean custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) is set to `true`. If left unchecked, its attribute is set to `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Checkbox group

Users can select from multiple choices. Values are set or added to a defined [array custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types).

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Long text

Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Things to know

- **Video:** The standard composer does not include a dedicated video block. Use **Custom code** to embed a player if needed. For more information, see [In-app messages: Frequently asked questions]({{site.baseurl}}/user_guide/channels/in_app_messages/faq/).
