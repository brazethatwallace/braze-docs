## In-app message editor blocks

Editor blocks are located under the **Build** section for in-app messages. To use them, drag an editor block inside a column. It will auto-adjust to the column width. Each editor block has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.

For more information about creating in-app messages in the **Drag-And-Drop Editor**, see [Create an in-app message with drag-and-drop]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/).

## Types

The following table describes each editor block type. Select a block to view its properties.

| Name | Description |
| --- | --- |
| [Title](#inappmessages_title-and-paragraph) | Enters a title text into the message. |
| [Paragraph](#inappmessages_title-and-paragraph) | Enters a paragraph text into the message. |
| [Button](#inappmessages_button) | Adds a standard button. Properties for this block allow for editing, setting links, and logging analytics. |
| [Radio Button](#inappmessages_radio-button) | Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute, which must be a string to be saved. Custom attributes with other data types do not save to the user profile. |
| [Image](#inappmessages_image) | Inserts an image from the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). |
| [Link](#inappmessages_link) | Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| [Spacer](#inappmessages_spacer) | Adds space or padding between other blocks. |
| [Custom Code](#inappmessages_custom-code) | Inserts and runs custom HTML, CSS, or JavaScript for advanced customization. |
| [Phone Capture](#inappmessages_phone-capture) | Inserts a form field for phone numbers. When submitted, the user is subscribed to the [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp subscription group]({{site.baseurl}}/whatsapp_subscription_groups/). |
| [Email Capture](#inappmessages_email-capture) | Inserts a form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| [Short Text](#inappmessages_short-text) | Inserts a form field that supports standard attributes (such as first and last name) or a custom attribute string of your choice. |
| [Dropdown](#inappmessages_dropdown) | Inserts a dropdown with a pre-defined list of items from which users can select one. You can add any custom attribute strings to the list. |
| [Checkbox](#inappmessages_checkbox) | Inserts a checkbox. If the user checks the box, the block's attribute is set to `true`. If left unchecked, its attribute is set to `false`. |
| [Checkbox Group](#inappmessages_checkbox-group) | Users can select from multiple choices presented. Values are either set or added to a defined array custom attribute. |
| [Long text](#inappmessages_long-text) | Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
| [Saved row](#inappmessages_saved-row) | Inserts a reusable row you saved earlier. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Properties

Details for each editor block's properties are provided in the following tables.

### Title and Paragraph

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Radio button

| Property | Description |
| --- | --- |
| Custom attribute name | Selects which custom user attribute stores the user's selected option when the form is submitted. |
| Total choices | The list of options; each option has a **Label text** (what users see) and an **Attribute value** (what is stored). You can add up to 15 choices, with a minimum of 2. |
| Font family | Typeface for the radio group text. |
| Font weight | Thickness (such as light, normal, or bold) of the text. |
| Font size | Size of the text. |
| Line height | Vertical spacing between lines of text. |
| Text color | Color of the option label text. |
| Letter spacing | Horizontal spacing between characters. |
| Align | Horizontal alignment of the choices within the block. |
| Accent color | Color used for the radio button controls (such as the selected state indicator). |
| Padding | Spacing around the block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

### Short text

| Property | Description |
| --- | --- |
| Required input field | Marks whether the field must be filled before the form can be submitted. |
| Maximum characters | Limits how many characters a user can type (string custom attributes cap at 255). |
| Placeholder text | Text shown inside the input until the user types. |
| Attribute | Stores the submitted value as **First name**, **Last name**, or a **Custom attribute** on the user profile. |
| Custom attribute name | Selects which string custom attribute receives the submitted value (available when **Attribute** is set to **Custom attribute**). |
| Font family | Typeface for the input text. |
| Font weight | Thickness (such as light, normal, or bold) of the input text. |
| Font size | Size of the input text. |
| Line height | Vertical spacing between lines of text. |
| Letter spacing | Horizontal spacing between characters. |
| Color | Color of the text typed in the field. |
| Text alignment | Horizontal alignment of the input text within the field. |
| Padding | Spacing around the block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Dropdown

| Property | Description |
| --- | --- |
| Required input field | Marks whether the user must select an option before the form can be submitted. |
| Placeholder text | Text shown in the dropdown until a user selects an option. |
| Custom attribute name | Selects which custom user attribute receives the selected value. |
| Total options | The list of options; each option has an **Option label** (what users see) and an **Attribute value** (what is stored). |
| Font family | Typeface for the dropdown text. |
| Font weight | Thickness (such as light, normal, or bold) of the text. |
| Font size | Size of the text. |
| Line height | Vertical line spacing. |
| Text color | Color of the dropdown text. |
| Letter spacing | Horizontal spacing between characters. |
| Align | Horizontal alignment of the dropdown (left or center). |
| Padding | Spacing around the block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Checkbox

| Property | Description |
| --- | --- |
| Required input field | Marks whether the checkbox must be checked before the form can be submitted. |
| Custom attribute name | Selects which boolean custom attribute receives `true` when checked or `false` when unchecked. |
| Accent color | Color used for the checkbox control styling. |
| Padding | Spacing around the block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Checkbox group

| Property | Description |
| --- | --- |
| Required input field | Marks whether the user must select at least the minimum number of options before submitting. |
| Minimum choices | Minimum number of options a user must select (when the field is required). |
| Maximum choices | Maximum number of options a user can select. |
| Custom attribute name | Selects which array custom attribute the selected values write to. |
| Action | Sets whether submission **Sets items** (replaces the array) or **Adds items** (appends to the array). |
| Total choices | The list of options; each option has a **Label text** (what users see) and an **Attribute value** (what is stored). |
| Font family | Typeface for option labels. |
| Font weight | Thickness (such as light, normal, or bold) of the option label text. |
| Font size | Size of the option label text. |
| Line height | Vertical spacing between lines of text. |
| Text color | Color of the option label text. |
| Letter spacing | Horizontal spacing between characters. |
| Align | Horizontal alignment of the group (start or center). |
| Accent color | Color of the checkbox controls. |
| Padding | Spacing around the block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Long text

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

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
