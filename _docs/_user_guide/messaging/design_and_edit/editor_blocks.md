---
nav_title: Editor blocks
article_title: Drag-and-drop editor blocks
alias: "/dnd/editor_blocks/"
channel: 
- email
- in-app messages
- landing pages
- banners
- preference center
page_order: 3
page_type: reference
description: "This reference article covers editor blocks in the drag-and-drop editor for email, in-app messages, landing pages, Banners, and drag-and-drop email preference centers."
tool: Media
---

# Drag-and-drop editor blocks

> Editor blocks are the tiles you drag into rows and columns in the drag-and-drop editor. 

Select the editor you're using:

{% sdktabs %}

{% sdktab email %}
## Email editor blocks

Editor blocks are in the **Content** section for email messages. Drag a block inside a column in the **Drag-And-Drop Editor**; it auto-adjusts to the column width.

For more information about creating emails in the **Drag-And-Drop Editor**, see [Create an email with drag-and-drop]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/) and <a href="{{site.baseurl}}/user_guide/channels/email/drag_and_drop/#other-customizations">Other customizations</a> in that article.

{% alert tip %}
You can also add [custom attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) to any URL within the `Image`, `Button`, or `Text` editor blocks.
{% endalert %}

### Title

Adds text for headers within the email.

| Property | Description |
|---|---|
| Title | Selects the heading style. |
| Font family | The font style for your title. |
| Font weight | The overall boldness of the font. |
| Font size | Determines the size of your text. |
| Text color | Modifies the color of the title. |
| Link color | Modifies the color of the link. |
| Align | Moves the title to be left, center, or right-oriented. |
| Line height | Modifies the distance between lines of text. |
| Letter spacing | Modifies the distance in between each character. |
| Text direction | Default left-to-right, but can be edited to be [right-to-left]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Title" }

### Paragraph

Enters text into the message. A toolbar helps with font and text editing functionality.

| Property | Description |
|---|---|
| Font family | The font style for your paragraph text. |
| Font weight | The overall boldness of the font. |
| Font size | Determines the size of your text. |
| Text color | Modifies the color of the text. |
| Link color | Modifies the color of the link. |
| Align | Moves the text to be left, center, or right-oriented. |
| Paragraph spacing | Modifies the space between paragraphs. |
| Line height | Modifies the distance between lines of text. |
| Letter spacing | Modifies the distance in between each character. |
| Text direction | Default left-to-right, but can be edited to be [right-to-left]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paragraph" }

### List

Adds a bulleted list.

| Property | Description |
|---|---|
| List type | The type of list. Can be either bulleted or numbered. |
| List style type | Determines the style of your list. |
| Start list from | Determines the starting number for your list. |
| Font family | The font style for your paragraph text. |
| Font weight | The overall boldness of the font. |
| Font size | Determines the size of your text. |
| Text color | Modifies the color of the text. |
| Link color | Modifies the color of the link. |
| Align | Moves the text to be left, center, or right-oriented. |
| List items spacing | Modifies the space between list items. |
| List items indent | Modifies the indentation of list items. |
| Line height | Modifies the distance between lines of text. |
| Letter spacing | Modifies the distance in between each character. |
| Text direction | Default left-to-right, but can be edited to be [right-to-left]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="List" }

### Button

Adds a standard button. Properties allow for editing styling and setting link behavior.

| Property | Description |
|---|---|
| Button options | Sets various button options, such as font, size, width, color, and padding. |
| Button hover | The style of the button when a user hovers over it using a mouse or trackpad. Includes the button's background color, font color, and border styles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Button" }

#### On-click behavior

| Property | Description |
|---|---|
| Link type | Determines the action when clicking the button and sets the appropriate protocol. |
| URL | Dynamic based on the **Open web page** link type. |
| Mail to, subject, and body | For the **Send email** link type, sets the recipient email address, subject, and content that will populate in a draft email when the user selects the button. |
| Tel | For the **Make call** and **Send SMS** link type, sets the phone number the user will call or text when selecting the button. |
| Message | For the **Send SMS** link type, sets the content that will populate in a draft SMS message when the user selects the button. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="On-click behavior" }

### Divider

Inserts a solid, dotted, or dashed line to help with spacing.

| Property | Description |
|---|---|
| Transparent | If enabled, the line and width options are removed. |
| Line | The different line formats, whether dotted, dashed, or solid. You can also modify the thickness and color of the divider line. |
| Width | Adjusts the spread of the divider in increments of 5. |
| Align | Moves the line to be either left, center, or right-oriented. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Divider" }

### Spacer

Adds space or padding between other blocks.

| Property | Description |
|---|---|
| Height | Adjusts the height of the spacer block. The default is 60px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spacer" }

### Image

Inserts an image from the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). For dynamic images (images with Liquid or Connected Content), you must set a fallback image to use the auto-width settings. For image specifications, see [email image specifications]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Property | Description |
|---|---|
| Auto width | Modifies the width of the image in pixels. |
| Align | Sets image alignment to left, center, or right within the block. |
| Image with Liquid | Use [Liquid]({{site.baseurl}}/liquid/) logic to dynamically set different images within the same block of content. |
| URL | Set an image using the address to where it's hosted. |
| Alternate text | A short description of the image that gives users the same information shown in the image. Essential for screen-reader accessibility or when the image fails to load. |
| Image with rounded corners | Renders the image with rounded corners. By default, images are rendered with squared corners. |
| Action | Triggers an action when the user clicks the image. |
| Block options | Sets padding around the image block. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image" }

{% alert tip %}
For **Auto width**, automatic image resizing picks the best size for the image based on a combination of image width and available space in the layout:
- Images wider than the available space are set at 100% width and keep this ratio on mobile, using the entire device display width.
- Images smaller than the available space use the image's natural size to avoid distortion effects or blurry pictures.
{% endalert %}

#### Gmail download button behavior

Gmail automatically appends a download button to images that do not have a hyperlink (`href`) associated with them. However, if the image's aspect ratio is 299 x 524 px or smaller, Gmail will not display the download button.

To prevent the download button from appearing on larger images, you can apply the "#" link workaround:

1. Select the **Image** block.
2. In the **Block Options** panel, go to the **Link** section.
3. Set the **Link type** to **Open web page**.
4. Enter a pound sign (`#`) in the **URL** input field.

Adding this link prevents Gmail from displaying the download button while not affecting the user experience.

### Video

Creates a link to video content. Only YouTube and Vimeo are supported.

| Property | Description |
|---|---|
| URL | The URL for the video. |
| Title | Auto-generated from the video metadata or can be customized. |
| Play icon style | Includes different options for the play button located at the top of a video image. |
| Play icon color | Option to select either **Light** or **Dark** for the play button. |
| Play icon size | Choose the pixel size for the play button. Predefined range from 50&nbsp;px to 80&nbsp;px (incremented by 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Video" }

{% alert tip %}
Videos hosted by Vimeo only work if they are set to public. All other security settings available within Vimeo (for example, "Hide from Vimeo.com") generate a different link format that is not supported by this Content Block. These types of links are altered by the builder, which prevents Braze from generating a thumbnail.
{% endalert %}

### Social

Inserts social media platform icons. You can upload custom images for brand-specific icons.

| Property | Description |
|---|---|
| Select icon collection | Sets the style of your icon collection. |
| Configure icon collection | Sets the URL for each social icon. Includes the **More options** toggle to edit the title and alternative text. |
| Align | Moves the social icon to be left, center, or right-oriented. |
| Icon spacing | Determines the spacing between each social icon. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Social" }

### Icons

Inserts an icon. You can upload custom images. Braze uses an oversized placeholder icon until you upload an image.

| Property | Description |
|---|---|
| Font family | The font style for your paragraph text. |
| Font weight | The overall boldness of the font. |
| Font size | Determines the size of your text. |
| Text color | Modifies the color of the title. |
| Link color | Modifies the color of the link. |
| Align | Moves the icon to be left, center, or right-oriented. |
| Letter spacing | Modifies the distance in between each character. |
| Icon size | Determines the size of your icon. |
| Icon spacing | Modifies the space of the icon. |
| Icon padding | Modifies the padding of the icon. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Icons" }

### HTML

Inserts raw HTML. Recommended for [Liquid]({{site.baseurl}}/liquid/), such as Connected Content or conditional statements.

| Property | Description |
|---|---|
| HTML | Add or edit raw HTML, including [Liquid]({{site.baseurl}}/liquid/) for personalization or conditional logic. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML" }

### Menu

Creates a flexible menu for the message you're designing.

| Property | Description |
|---|---|
| Configure menu items | Add a menu item. |
| Font family | The font style for the menu. |
| Font size | The size of your menu. |
| Text color | Modifies the color of the menu. |
| Link color | Modifies the color of the menu text. |
| Align | Moves the menu to be left, center, or right-oriented. |
| Letter spacing | Modifies the distance in between each character. |
| Layout | Determines the layout to be either horizontal or vertical. |
| Separator | Adds character(s) between the menu options. |
| Mobile menu | Includes options to modify the icon size, color, and icon type when shown on a mobile device. |
| Item padding | Modifies the padding by using either the **+** or **-** button, or by entering a specific number. |
| All sides | Sets a consistent padding number if item padding is disabled. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Menu" }

### Product

Renders product rows from a [Product Catalog]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/), either as static items from a catalog Selection (up to 12) or as dynamic products driven by a [Canvas eCommerce trigger]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/) (up to 24).

| Property | Description |
| --- | --- |
| Content type | Sets whether products come from a fixed catalog **Selection** (**Static**, up to 12 products) or from a Canvas eCommerce recommendation trigger (**Dynamic**, up to 24 products). **Dynamic** is only available in Canvas message steps. |
| Catalog | Selects which Product Catalog supplies product data and field mappings. |
| Selection | *(Static only)* Selects which filtered set on the catalog defines which products appear. |
| Show source details | Toggles help text showing the underlying catalog or event field mapped to each product field. |
| Variant image | Shows or hides the variant image for each product tile. |
| Product title | Shows or hides the product title for each tile. |
| Price | Shows or hides the product price. |
| Button for product URL | Shows or hides a call-to-action button linking to the product URL. |
| Quantity | *(Dynamic, Canvas only, when the entry trigger is not a product view event)* Shows or hides the product quantity from the trigger event. |
| Product orientation | Sets the image position within each tile: **Image left**, **Image center**, or **Image right**. |
| Alignment | Sets the horizontal alignment of content within each tile. |
| Max products per row | Sets how many products appear per row: **1**, **2**, or **3** (**3** is only available when orientation is **Image center**). |
| Product spacing | Sets spacing between products: **Auto** or **Custom**. |
| Custom spacing | *(When **Custom** is selected)* Sets the gap in pixels between products. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Product" }

## Personalization

You can add personalization to your email using Liquid or Connected Content.

- **Liquid:** Under **Content** > **Personalization**, select an attribute, copy the snippet, and paste it into an HTML block. While basic Liquid snippets may work in Title, Paragraph, and List blocks, placing Liquid in these blocks can cause unexpected behavior and layout issues. To avoid issues, use HTML blocks for any Liquid logic. Note that Liquid isn't supported in image blocks or in button URL fields.
- **[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/):** Add an **HTML** block and place your {% raw %}`{% connected_content %}`{% endraw %} call there.

{% endsdktab %}

{% sdktab in-app messages %}
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

Inserts a checkbox. If the user checks the box, the block's [boolean custom attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) is set to `true`. If left unchecked, its attribute is set to `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Checkbox group

Users can select from multiple choices. Values are set or added to a defined [array custom attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

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

{% endsdktab %}

{% sdktab landing pages %}
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

Inserts custom HTML, CSS, or JavaScript for advanced customization, such as [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page).

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

When checked, sets the block's [boolean custom attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) to `true`; when unchecked, to `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Checkbox group

Users pick multiple options; values set or append to a defined [array custom attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Manage subscriptions

Adds a checklist of [email]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-groups) or [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) subscription groups so visitors can opt in to or manage their subscriptions when they submit the form. Each block is for one channel. Configure it after you add subscription groups to the block. This block doesn't list RCS or WhatsApp subscription groups.

For identified users who open the page through the landing page's [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/), the block pre-fills each checkbox with the user's current subscription state, so it can also serve as a preference management page.

Select the block in the editor to:

- Reorder subscription groups
- Add or remove subscription groups
- Add or remove descriptions
- Add or remove a "Subscribe to all" checkbox that selects every subscription group in the block

| Property | Description |
| --- | --- |
| Subscription groups | Add, remove, or reorder the subscription groups shown in the block. |
| Include descriptions | Displays each subscription group's description alongside its name. |
| **Subscribe to all** checkbox | Adds a checkbox that selects every subscription group in the block. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Manage subscriptions" }

For the full setup flow, see [Manage Subscriptions block]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions/).

### Long text

Multi-line text field for survey-style flows. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager. This block is not available for standard landing pages.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## Things to know

- **Video:** The standard composer does not include a dedicated video block. Use **Custom code** to embed a player if needed. For more information, see [Landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/).

{% endsdktab %}

{% sdktab banners %}
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

{% endsdktab %}

{% sdktab preference center %}
## Preference center editor blocks

Drag blocks from the **Build** section into a row in the drag-and-drop preference center editor. Each block has its own settings; the right-side panel switches to properties or styling for the selected element.

Before you edit blocks, add subscription groups and configure the subscription **smart block** (see the following section). For the full setup flow, see [Create an email preference center with drag-and-drop]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/).

### Title and paragraph

Adds heading or body copy with rich text options.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Adds a clickable button (for example **Save** or navigation).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Image

Displays an image from the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) or a URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Spacer

Adds vertical spacing between blocks.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Subscription groups (smart block)

Adds a template block that lists subscription groups, optional **Subscribe to all** / **Unsubscribe from all** controls, and descriptions. Configure it after you add groups in the preference center workflow.

After you [add subscription groups]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-3-add-subscription-groups-to-the-preference-center), select the smart block in the canvas to:

- Reorder subscription groups  
- Add or remove groups  
- Add or remove descriptions  
- Toggle **Subscribe to all** and **Unsubscribe from all** for the groups in that block  

The **Unsubscribe from all** control at the bottom of the default template is required and performs a [global unsubscribe]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-states) from email.

## Things to know

- **Common styles:** You can set page-wide defaults under **Common Styles** before adjusting individual blocks. For more information, see [Customize the preference center using the drag-and-drop editor]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Confirmation page:** Switch to **Confirmation Page** at the top of the editor to style the post-save experience using the same block types.

{% endsdktab %}

{% endsdktabs %}

