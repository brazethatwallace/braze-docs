## Preference center editor blocks

Drag blocks from the **Build** section into a row in the drag-and-drop preference center editor. Each block has its own settings; the right-side panel switches to properties or styling for the selected element.

Before you edit blocks, add subscription groups and configure the subscription **smart block** (see below). For the full setup flow, see [Create an email preference center with drag-and-drop]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/).

## Types

| Name | Description |
| --- | --- |
| Title | Adds a heading or label text. |
| Paragraph | Adds body copy with rich text options. |
| Button | Adds a clickable button (for example **Save** or navigation). |
| Image | Displays an image from the [media library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) or a URL. |
| Spacer | Adds vertical spacing between blocks. |
| Custom code | Inserts custom HTML, CSS, or JavaScript. Inline frames may not generate in delivered preference centers—see the note below. |
| Subscription groups (smart block) | The template block that lists subscription groups, optional **Subscribe to all** / **Unsubscribe from all** controls, and descriptions. Configure it after you add groups in the preference center workflow. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" %}

{% alert note %}
For typography and layout behavior shared with in-app messages, this article links to [in-app message editor blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages) for full property tables where they apply. **Custom code** may not appear in every preference center editor—if you need it and don't see it, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
{% endalert %}

## Properties

### Title and paragraph

See [Title and Paragraph]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_title-and-paragraph) under in-app message editor blocks.

### Button

See [Button]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_button) for styling properties and [Actions]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_actions) for on-click options where they align with in-app messages.

### Image

See [Image]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_image) under in-app message editor blocks.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Spacer

See [Spacer]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_spacer) under in-app message editor blocks.

### Custom code

If **Custom code** is not in your block list, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.

| Property | Description |
| --- | --- |
| Custom code | Add or edit HTML, CSS, or JavaScript. If you use Custom code, inline frames may not generate in the custom code when the preference center is delivered to users. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" %}

For advanced HTML patterns, compare with [Custom code]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_custom-code) under in-app message editor blocks.

### Subscription groups (smart block)

After you [add subscription groups]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-3-add-subscription-groups-to-the-preference-center), select the smart block in the canvas to:

- Reorder subscription groups  
- Add or remove groups  
- Add or remove descriptions  
- Toggle **Subscribe to all** and **Unsubscribe from all** for the groups in that block  

The **Unsubscribe from all** control at the bottom of the default template is required and performs a [global unsubscribe]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-states) from email.

## Things to know

- **Common styles:** You can set page-wide defaults under **Common Styles** before tuning individual blocks. For more information, see [Customize the preference center using the drag-and-drop editor]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Confirmation page:** Switch to **Confirmation Page** at the top of the editor to style the post-save experience using the same block types.
