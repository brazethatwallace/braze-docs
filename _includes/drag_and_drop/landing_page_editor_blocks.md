## Landing page editor blocks

Editor blocks for landing pages are in the **Build** section of the **Drag-And-Drop Editor**, under **Rows** and block categories (basic blocks and form blocks). Drag a block into a row column; it auto-adjusts to the column width. Each block has its own settings in the right-side properties panel.

For more information about creating and publishing landing pages, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

## Types

The following table summarizes landing page editor blocks. Basic blocks add layout and content; form blocks capture data tied to user profiles.

| Name | Description |
| --- | --- |
| Title | Adds a heading or title. Useful for structuring sections and improving readability. |
| Paragraph | Adds longer descriptions or context. Supports rich text formatting. |
| Button | A clickable element for actions such as opening a link or submitting a form. |
| Radio button | Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute. |
| Image | Displays an image from an upload or external URL. |
| Link | A hyperlink users can select to go to a URL. Can sit in text or stand alone. |
| Spacer | Adds vertical spacing between elements. |
| Custom code | Inserts custom HTML, CSS, or JavaScript for advanced customization. |
| Countdown timer | Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
| Email capture | Form field for email addresses. On submit, the address is saved to the user's Braze profile. |
| Phone capture | Form field for phone numbers. On submit, subscribes the user to your selected [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) subscription group. |
| Input field | Form field for standard attributes (for example first or last name) or a custom attribute string. Called **Short text** in the in-app message editor. |
| Dropdown | A predefined list of items; users pick one. You can map values to custom attribute strings. |
| Checkbox | When checked, sets the block's attribute to `true`; when unchecked, to `false`. |
| Checkbox group | Users pick multiple options; values set or append to a defined array custom attribute. |
| Long text | Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
| Saved row | Inserts a reusable row you saved earlier. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Properties

### Title and paragraph

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

For form submission and links to a confirmation page, follow [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#step-4-create-a-confirmation-page-optional).

### Radio button

Add a **Radio button** block and configure the options and associated custom attribute in the properties panel. The user profile logs the selected value as a string custom attribute when the form is submitted. Custom attributes with other data types do not save to the user profile.

### Image

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Link

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

### Spacer

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Custom code

| Property | Description |
| --- | --- |
| Custom code | Allows you to add, edit, or delete HTML, CSS, and JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

You can use Custom code for advanced integrations, for example [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#google-tag-manager).

### Countdown timer

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.

### Long text

Use the properties panel to set label, placeholder, and attribute mapping.

### Saved row

Add a **Saved row** from the **Rows** category when it appears in your editor. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/).

### Email capture

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Phone capture

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Input field, dropdown, checkbox, and checkbox group

Use the properties panel to configure the label, placeholder text, and the custom attribute the field maps to. For required fields, confirmation pages, and submit behavior, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

## Actions

You can assign an action that occurs when a user taps a button, link, or image on the landing page. You can also use [Liquid]({{site.baseurl}}/liquid/) to personalize the actions.

### Button

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Image

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

{% alert important %}
If you configure a button with **Submit form when button is clicked** and open a web URL in a new tab, iOS Safari may block the navigation. Prefer opening the post-submit URL in the same tab when submitting forms. For more information, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).
{% endalert %}
