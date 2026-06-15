---
nav_title: Message Template Assistant
article_title: Message Template Assistant
permalink: "/template_assistant/"
description: "This reference article covers how to use the message template assistant to generate templates for your email messaging."
page_type: reference
---

# Message template assistant

> The message template assistant helps you iterate on an existing HTML email template by using GenAI to generate templates based on your specific needs. This functionality can help optimize your content for a specific use case, audience, or conversion, and help reduce the time and effort when composing emails.

{% alert important %}
The message template assistant is in early access. Contact your customer success manager if you're interested in participating in this early access. <br><br>This functionality is currently only supported for the email channel and only in the HTML editor, not any other editors (such as drag-and-drop or AMP).
{% endalert %}

## How it works

The message template assistant uses your [brand guidelines](https://www.braze.com/docs/user_guide/administrative/app_settings/brand_guidelines) and [global style settings](https://www.braze.com/docs/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) to tailor the message content and style to your brand.

For example, if you have global style settings set up, the message template assistant will incorporate your brand’s colors and styles. If you have brand guidelines defined in Braze, the assistant can also reference these to create copy in the tone and personality of your brand.

The message template assistant can remember your chat history only when you’re still in the same chat window. This means it may refer to previous prompts used to generate future ones. The assistant will also try to iterate your template for mobile responsiveness.

For example, if you go from a prompt specifically about a fitness brand to a generic brand in your subsequent prompts, the message template assistant may inform the template that this is for that same fitness brand. To start a new chat, select **Clear History** in the chat window and open the message template assistant again.

## Creating a template

1. In the dashboard, go to **Templates** > **Email Templates**.
2. Select an existing email template.
3. In the **Create with AI** section of the HTML editor, select **Template**.
4. From here, you can enter a variety of prompts or ask questions about your content.
5. The message template assistant will provide a response and determine what changes are needed to your template.
6. Select **Generate** to apply the suggestions.

{% alert important %}
We highly recommend testing the generated output to make sure it matches your messaging.
{% endalert %}

![An example prompt to create a template with multiple sections to be used for multiple emails. The message template assistant explains the modifications to the current template.]({% image_buster /assets/unlisted_docs/img/ai_message_template_assistant1.png %}){: style="width:70%;"}

### Example prompts

Here are some example prompts to get you started:

- Add a feedback survey at the bottom of the email
- Change font to {% raw %}`{{font name}}` and font size of the paragraph to size `{{number}}`{% endraw %}
- Make all the images have rounded corners
- Add another section with an image and a call-to-action

{% alert note %}
Depending on your prompt and the response, the message template assistant may add placeholder images when generating the new template.
{% endalert %}
