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
