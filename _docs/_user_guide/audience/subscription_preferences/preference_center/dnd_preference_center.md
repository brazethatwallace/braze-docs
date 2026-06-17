---
nav_title: Drag-and-drop email preference center
article_title: Drag-and-drop email preference center
alias: "/dnd_preference_center/"
description: "This reference page covers how to create an email preference center with the drag-and-drop editor."
page_order: 2
---

# Create an email preference center with drag-and-drop

> Using the drag-and-drop editor, you can create and customize a preference center to help manage which users receive certain types of communication. You can have up to 100 preference centers per workspace.

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Step 1: Create and name your preference center

Go to **Audience** > **Email Preference Centers**. A list of any existing custom preference centers is displayed. 

Select **Create New**. When naming your preference center, note that names can only contain:
- Alphanumeric characters
- Dashes
- Underscores

The name you provide determines the syntax of the generated Liquid tag. This Liquid tag can be included in any outbound email campaigns or Canvas steps and directs users to the preference center.

## Step 2: Add subscription groups to the preference center

Select **Launch Editor** to begin designing your preference center in the drag-and-drop editor.

### Define available subscription groups

Every preference center includes a Subscription Group smart block, which controls which subscription groups are displayed to consumers. This block is required and can't be deleted from the editor.

To add subscription groups, open the modal by doing one of the following:

- **From the editor canvas:** Select **+ Add subscription groups** in the empty state of the Subscription Group block.
- **From the block properties panel:** Select the Subscription Group block in the canvas to open its properties in the side panel, then select **Add subscription groups**.

In the modal that opens, choose the groups you want to include, then select **Add Subscription Groups**.

After adding groups, you can further configure the block from the side panel:

- Adjust the order of subscription groups
- Add or remove subscription groups
- Include descriptions
- Add or remove a **Subscribe to all** checkbox, which subscribes the consumer to all subscription groups shown in this block
- Add or remove an **Unsubscribe from all** checkbox, which unsubscribes the consumer from all subscription groups shown in this block

The **Unsubscribe from all** button at the bottom of the template is non-removable and [globally unsubscribes]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) the consumer from receiving any email messages.

![The drag-and-drop preference center editor showing the subscription group block, Save my preferences button, and Unsubscribe from all emails link.]({% image_buster /assets/img/preference_center/preference_center4.gif %})

## Step 3: Customize the preference center

Customize your preference center using the drag-and-drop editor.

### Set common styles

You can set certain styles to be applied across all relevant blocks in your preference center from the **Common Styles** tab. The styles set in this section are used everywhere in your message except where you override them for a specific block. For an easier design experience, we recommend setting up page-level styles before you customize styles at the block level.

![An example of common style settings for text, buttons, and links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
To return to the common styles, select the "X" button on individual block properties. Next, select the message container, message "X" button, or editor background.
{% endalert %}

## Step 4: Customize your confirmation page

Customize the confirmation page by selecting **Confirmation Page** at the top of the drag-and-drop editor window. This page is displayed to users after they update their preferences using the preference center. The same styling capabilities apply to this page as to the main preference center.

![An example of a confirmation page to communicate the user's preferences have been updated.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Step 5: Preview and launch your preference center

You can preview your preference center by selecting the **Preview** tab within the editor. Testing functionality is disabled in preview. After editing your preference center, close the editor by selecting **Done**.

You'll see a preview of both the preference center and the confirmation page. Select **Save as Draft** to return to this preference center later, or select **Launch Preference Center** if you're satisfied with it.

When launching the preference center, you'll be prompted to confirm the name, as it can't be edited after launching. After you confirm the name, the preference center is launched and ready for use.

## Step 6: Add the preference center to your emails

After launching, your preference center is ready to link to from any email. From the **Email Preference Centers** page, copy the Liquid tag for your preference center by selecting the **Copy Liquid** icon.

![The Copy Liquid option in the row of a preference center.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Add the Liquid tag to the desired location in your email, similar to how [unsubscribe URLs]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link) are inserted.

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

## Drag-and-drop preference center components

The drag-and-drop editor uses two key components for preference center composition: rows and blocks. All blocks must be placed in a row.

{% tabs %}
{% tab Rows %}

Rows are structural units that define the horizontal composition of a section of the message by using cells.

![Option to select the type of row in your message.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

When a row is selected, you can add or remove the number of columns you need from the Column customization section to put different content elements side by side. You can also slide to adjust the size of existing columns.

As a best practice, format your row and column properties before formatting any blocks inside the rows. You can adjust the spacing and alignment in many places, so starting from the foundation makes it easier to edit as you go.

{% endtab %}
{% tab Blocks %}

Blocks represent different types of content you can use in your message. Drag one inside an existing row segment, which will auto-adjust to the cell width.

![Option to select blocks, including title, paragraph, button, image, and spacer.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a styling panel for the selected content element. For more information, see [Editor blocks (preference center)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=preference%20center).

If you're using the Custom Code block in your preference center, inline frames may not generate in the custom code when delivered to your users.

{% endtab %}
{% endtabs %}

## Handling errors

If an error occurs when a consumer selects **Save** on your preference center, they'll be presented with the following default error message. This message can't be customized or styled in the editor, though localization is still supported.

![An error noting "There was a problem saving your preferences. Please try again."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}

## Manage preference centers

You can manage existing drag-and-drop preference centers from **Audience** > **Email Preference Centers**:

- To change a preference center's name or content, open the preference center from the dashboard.
- Drag-and-drop preference centers can't be deleted from the dashboard. To remove one, first remove its Liquid tag from any email campaigns or Canvas steps, then contact [Braze Support]({{site.baseurl}}/support_contact/).
- If a removed preference center was used in previously sent messages, it will stop working in those delivered emails.
