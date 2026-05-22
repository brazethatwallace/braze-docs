## Landing page editor blocks

Editor blocks for landing pages are in the **Build** section of the **Drag-And-Drop Editor**, under **Rows** and block categories. Drag a block into a row column; it auto-adjusts to the column width. Select a block to edit its settings in the right-side properties panel.

For more information about creating and publishing landing pages, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

### Title and paragraph

Adds heading or body text. Useful for structuring sections and improving readability.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Adds a clickable element for actions such as opening a link or submitting a form.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
If you configure a button with **Submit form when button is clicked** and open a web URL in a new tab, iOS Safari may block the navigation. Open the post-submit URL in the same tab when submitting forms. For more information, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).
{% endalert %}

### Radio button

Adds a list of options from which users can select one. Use the properties panel to configure the available options and the custom attribute that receives the selected value. The user profile logs the selected value as a [string custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) when the form is submitted. Custom attributes with other data types do not save to the user profile.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Image

Displays an image from an upload or external URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Adds a hyperlink users can select to go to a URL. Can sit in text or stand alone.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### On-click behavior

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Spacer

Adds vertical spacing between elements.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Custom code

Inserts custom HTML, CSS, or JavaScript for advanced customization, such as [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#google-tag-manager).

| Property | Description |
| --- | --- |
| Custom code | Allows you to add, edit, or delete HTML, CSS, and JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### Email capture

Adds a form field for email addresses. On submit, the address is saved to the user's Braze profile.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Phone capture

Adds a form field for phone numbers. On submit, subscribes the user to your selected [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) subscription group.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Input field

Adds a form field for standard attributes (for example, first or last name) or a custom attribute string.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Dropdown

A predefined list of items; users pick one. You can map values to custom attribute strings.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Checkbox

When checked, sets the block's [boolean custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types) to `true`; when unchecked, to `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Checkbox group

Users pick multiple options; values set or append to a defined [array custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types).

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Long text

Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. This block is not available for standard landing pages.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Things to know

- **Video:** The standard composer does not include a dedicated video block. Use **Custom code** to embed a player if needed. For more information, see [Landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/).
