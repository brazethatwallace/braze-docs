## Landing page editor blocks

Editor blocks for landing pages are in the **Build** section of the drag-and-drop editor, under **Rows** and block categories (basic blocks and form blocks). Drag a block into a row column; it auto-adjusts to the column width. Each block has its own settings in the right-side properties panel.

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" %}

{% alert note %}
If a block's behavior matches the in-app message editor, this article links to [in-app message editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages) for full property tables. Landing-specific behavior is called out here. For which blocks appear on each surface, use the tabs on [Editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/).
{% endalert %}

## Properties

### Title and paragraph

For typography and alignment properties, see [Title and Paragraph]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_title-and-paragraph) under in-app message editor blocks.

### Button

For styling properties, see [Button properties]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_button) under in-app message editor blocks.

For button actions (submit, on-click behavior, logging), see the **Actions** section under [in-app message editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_actions).

For form submission and links to a confirmation page, follow [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#step-4-create-a-confirmation-page-optional).

### Radio button

For behavior aligned with in-app messages, see [Types]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_types) for the in-app **Radio button** description. Configure options and custom attributes in the properties panel after you place the block.

### Image

For image properties and dynamic image guidance, see [Image]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_image) under in-app message editor blocks.

### Link

For link text styling, see [Link]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_link) under in-app message editor blocks.

### Spacer

For spacer properties, see [Spacer]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_spacer) under in-app message editor blocks.

### Custom code

For the Custom code property field, see [Custom code]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_custom-code) under in-app message editor blocks.

You can use Custom code for advanced integrations, for example [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#google-tag-manager).

### Countdown timer

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.

### Long text

Use the properties panel to set label, placeholder, and attribute mapping. Behavior matches the in-app message **Long text** block for survey-style forms.

### Saved row

Add a **Saved row** from the **Rows** category when it appears in your editor. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/).

### Email capture, phone capture, input field, dropdown, checkbox, and checkbox group

These form blocks align with the in-app message editor. For **Email capture** and **Phone capture** property tables, see [Email capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_email-capture) and [Phone capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_phone-capture) under in-app message editor blocks.

For **Short text** (the in-app editor name for the same control as **Input field** on landing pages), **Dropdown**, **Checkbox**, and **Checkbox group**, see the [Types]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_types) table in that tab, then use the properties panel in the editor for field-level settings.

For required fields, confirmation pages, and submit behavior, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

## Actions

For button, image, and link actions where the landing page acts as a form (submit, open URL, log attributes), use the same patterns as in-app messages. See [Actions]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_actions) in that tab.

{% alert important %}
If you configure a button with **Submit form when button is clicked** and open a web URL in a new tab, iOS Safari may block the navigation. Prefer opening the post-submit URL in the same tab when submitting forms. For more information, see [Create landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).
{% endalert %}
