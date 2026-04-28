## In-app message editor blocks

Editor blocks are located under the **Build** section for in-app messages. To use them, drag an editor block inside a column. It will auto-adjust to the column width. Each editor block has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.

For more information about creating in-app messages in the **Drag-And-Drop Editor**, see [Create an in-app message with drag-and-drop]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/).

## Types

The following table describes each editor block type.

| Name | Description |
| --- | --- |
| Title | Enters a title text into the message. |
| Paragraph | Enters a paragraph text into the message. |
| Button | Adds a standard button. Properties for this block allow for editing, setting links, and logging analytics. |
| Radio Button | Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute, which must be a string to be saved. Custom attributes with other data types do not save to the user profile. |
| Image | Inserts an image from the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). |
| Link | Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| Spacer | Adds space or padding between other blocks. |
| Custom Code | Inserts and runs custom HTML, CSS, or JavaScript for advanced customization.  |
| Phone Capture | Inserts a form field for phone numbers. When submitted, the user is subscribed to the [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp subscription group]({{site.baseurl}}/whatsapp_subscription_groups/). |
| Email Capture | Inserts a form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| Short Text    | Inserts a form field that supports standard attributes (such as first and last name) or a custom attribute string of your choice. |
| Dropdown      | Inserts a dropdown with a pre-defined list of items from which users can select one. You can add any custom attribute strings to the list. |
| Checkbox      | Inserts a checkbox. If the user checks the box, the block's attribute is set to `true`. If left unchecked, its attribute is set to `false`. |
| Checkbox Group| Users can select from multiple choices presented. Values are either set or added to a defined array custom attribute. |
| Long text | Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
| Saved row | Inserts a reusable row you saved earlier. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Properties

Details for each editor block's properties are provided in the following tables.

### Title and Paragraph

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

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
| Custom Code | Allows you to add, edit, or delete HTML, CSS, and JavaScript for an in-app message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Phone capture

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Email capture

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Long text

Use the properties panel to set label, placeholder, validation, and the custom attribute that stores the submitted value.

### Saved row

Add a **Saved row** from the **Rows** category when it appears in your editor. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/).

## Actions

You can assign an action that occurs when a user taps a button, link, or image in the message. You can also use [Liquid]({{site.baseurl}}/liquid/) to personalize the actions. Details for each editor block's actions are provided in the following tables.

### Button

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Image

For image specifications, refer to our [in-app message image specifications]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}
