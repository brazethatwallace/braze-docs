## Landing page editor blocks

Editor blocks for landing pages are in the **Build** section of the **Drag-And-Drop Editor**, under **Rows** and block categories (basic blocks and form blocks). Drag a block into a row column; it auto-adjusts to the column width. Each block has its own settings in the right-side properties panel.

For more information about creating and publishing landing pages, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

## Types

The following table describes each editor block type. Select a block to view its properties.

| Name | Description |
| --- | --- |
| [Title](#landingpages_title-and-paragraph) | Adds a heading or title. Useful for structuring sections and improving readability. |
| [Paragraph](#landingpages_title-and-paragraph) | Adds longer descriptions or context. Supports rich text formatting. |
| [Button](#landingpages_button) | A clickable element for actions such as opening a link or submitting a form. |
| [Radio button](#landingpages_radio-button) | Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute. |
| [Image](#landingpages_image) | Displays an image from an upload or external URL. |
| [Link](#landingpages_link) | A hyperlink users can select to go to a URL. Can sit in text or stand alone. |
| [Spacer](#landingpages_spacer) | Adds vertical spacing between elements. |
| [Custom code](#landingpages_custom-code) | Inserts custom HTML, CSS, or JavaScript for advanced customization. |
| [Countdown timer](#landingpages_countdown-timer) | Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
| [Email capture](#landingpages_email-capture) | Form field for email addresses. On submit, the address is saved to the user's Braze profile. |
| [Phone capture](#landingpages_phone-capture) | Form field for phone numbers. On submit, subscribes the user to your selected [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) or [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) subscription group. |
| [Input field](#landingpages_input-field) | Form field for standard attributes (for example first or last name) or a custom attribute string. |
| [Dropdown](#landingpages_dropdown) | A predefined list of items; users pick one. You can map values to custom attribute strings. |
| [Checkbox](#landingpages_checkbox) | When checked, sets the block's attribute to `true`; when unchecked, to `false`. |
| [Checkbox group](#landingpages_checkbox-group) | Users pick multiple options; values set or append to a defined array custom attribute. |
| [Long text](#landingpages_long-text) | Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
| [Saved row](#landingpages_saved-row) | Inserts a reusable row you saved earlier. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Properties

Details for each editor block's properties are provided in the following tables.

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

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

### Saved row

Add a **Saved row** from the **Rows** category when it appears in your editor. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/).

### Email capture

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Phone capture

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Input field

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
