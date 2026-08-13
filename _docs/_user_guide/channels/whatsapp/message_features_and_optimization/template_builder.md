---
nav_title: WhatsApp Template Builder
article_title: WhatsApp Template Builder
description: "Learn how to create, configure, and submit WhatsApp message templates directly in Braze using the WhatsApp Template Builder."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp Template Builder

> The WhatsApp Template Builder lets you create and submit WhatsApp message templates directly in Braze—no need to switch between Braze and the Meta Business Manager. After Meta approves your template, use it in as many campaigns and Canvases as you'd like.

## Prerequisites

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Create a template

### Step 1: Go to WhatsApp Templates

Go to **Content** > **Templates** > **WhatsApp**, then select **Create new template**.

![WhatsApp templates page with button to create a new template.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Step 2: Configure template settings

Fill in the following fields:

| Field | Description |
| ----- | ----- |
| **Account** | The WhatsApp Business Account (WABA) you’d like to submit the template to. All subscription groups and phone numbers within a WABA will share template access. |
| **Language** | The language for this template. WhatsApp requires a separate template for each language. |
| **Template name** | A unique name for your template. Template names can only contain lowercase letters, numbers, and underscores. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure template settings" }

### Step 3: Choose a layout

Under **Layout**, select the template type:

- **Default:** A standard WhatsApp message. This is the layout covered in this article.  
- **Carousel:** A message with horizontally scrollable cards. For more information, see [Carousel templates]({{site.baseurl}}/whatsapp_carousel_templates).

### Step 4: Build your template

#### Header (optional)

Add a header to appear before the message body. You can choose:

- **Text:** A short text header.  
- **Media:** An image, video, or document (URL only). Braze stores the media reference and submits a sample to Meta for approval.  
- **None:** No header 

#### Body

Enter the main content of your message and personalize the body as needed by using Liquid or generic variables:

{% raw %}
- Use Liquid tags (for example, `{{${first_name}}}`). Braze saves your Liquid and surfaces it when you use the template in a campaign or Canvas composer.  
- Use generic variables, such as numbered placeholders (for example, `{{1}}`), if you prefer to add personalization later when building your message.
{% endraw %}

You can add personalization wherever the **+** plus button appears. Not all fields support personalization.

#### Liquid character limits

Meta enforces character limits on the template structure you submit for approval (for example, 1,024 characters for the body and 60 characters for a text header). In the Template Builder, these limits apply to the template sent to Meta, not the final rendered message at send time.

- **{% raw %}`{{ }}`{% endraw %} variables:** Braze converts Liquid variables to numbered placeholders ({% raw %}`{{1}}`, `{{2}}`{% endraw %}) before checking length. A long expression like {% raw %}`{{${first_name}}}`{% endraw %} counts as a short placeholder, not the full Liquid syntax.
- **{% raw %}`{% %}`{% endraw %} tags:** Liquid logic tags count as literal text at their full length and appear as uneditable copy in template messages.

For complex personalization, use a [Context step]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) to compute values, then reference shorter variables in the template. For Message Extras and conditional logic constraints, see [Liquid in the WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid).

#### Footer (optional)

Add a short footer to appear after the message body.

#### Buttons (optional)

Add up to 10 buttons to your template. Button types have different categories and specifications.

| Button type | Category | Specifications |
| --- | --- | --- |
| Quick reply | Quick reply buttons |{::nomarkdown}<ul><li><b>Maximum count:</b> 10</li><li><b>Button text:</b> Up to 25 characters</li></ul> {:/}|
| Phone number | Call to Action buttons | {::nomarkdown}<ul><li><b>Maximum count:</b> 1</li><li><b>Button text:</b> Up to 25 characters</li><li><b>Phone number:</b> Valid phone number with country code, without + (such as "14155552671")</li></ul> {:/}|
| Visit website | Call to Action buttons | {::nomarkdown}<ul><li><b>Maximum count:</b> 2</li><li><b>Button text:</b> Up to 25 characters</li><li><b>Website URL:</b> Up to 2,000 characters</li></ul> {:/}|
| Copy offer code | Call to Action buttons | {::nomarkdown}<ul><li><b>Maximum count:</b> 1</li><li><b>Button text:</b> "Copy offer code" (can't be edited)</li><li><b>Offer code:</b> Up to 15 characters</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Buttons (optional)" }

![WhatsApp template composer with quick reply and call to action buttons.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Step 5: Preview your template

Before submitting, preview how your message will appear to recipients:

- **Preview as a user:** See a generic preview of the message.  
- **Preview as a specific user:** Select a user profile to preview how the template will render with that user's data.

### Step 6: Submit for review

Select **Submit** to send your template to Meta for review, which typically takes a few minutes but can take up to 24 hours. The template appears on your **WhatsApp templates** page when it's submitted, and the status updates when you refresh the **WhatsApp templates** page.

## Supported template categories

Only Marketing templates are currently supported in the WhatsApp Template Builder.

## Use an approved template in a campaign

After Meta approves your template, you can use it in a WhatsApp campaign or Canvas.

1. Go to **Campaigns** and select **Create Campaign** > **WhatsApp**.  
2. In the message composer, select your approved template.  
3. Braze automatically populates the template's content—including any media and Liquid you entered during template creation—so you don't have to re-enter it.  
4. Update any variable content or personalization as needed. Fields locked by Meta (shown in gray) cannot be edited. To change locked content, you must edit and resubmit the template for approval.  
5. Use the **Test** tab to preview the message, update body variables, and confirm the message looks as expected before launch.

For more information about building WhatsApp campaigns, see [Create a WhatsApp message]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Frequently asked questions

### How long does Meta template review take?

Reviews typically complete within five minutes, but can take up to 24 hours.

### Can I edit a template after it's been approved?

You can update variable content and personalization when building a campaign or Canvas. Changes to locked content (body copy, button layout, or other Meta-controlled fields) require creating a new template in the Template Builder or editing the template in Meta's WhatsApp Manager and waiting for Meta re-approval. If you use [click tracking]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking), see that article before editing Braze-created templates in Meta's WhatsApp Manager.

### What happens to templates I submitted before the Template Builder was available?

Templates created in Meta Business Manager are still available to use in Braze. The Template Builder is an additional way to create and manage templates without leaving the Braze dashboard.

### Why can't I add personalization to every field?

Meta restricts which parts of a template can be personalized. The **+** plus button only appears in fields that support variable content.