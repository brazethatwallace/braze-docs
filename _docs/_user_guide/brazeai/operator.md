---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Learn how to access and use BrazeAI Operator<sup>TM</sup>, an AI-powered assistant built into the Braze dashboard, including its features and best."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> is an AI-powered assistant built into the dashboard. Operator helps you build—drafting campaigns, Canvases, segments, and content—and helps you get unstuck, from answering questions and troubleshooting issues to brainstorming ideas.

## Access Operator

Open Operator from any page in the Braze dashboard.  

1. Select **BrazeAI Operator<sup>TM</sup>** next to your user profile.
2. The Operator chat panel opens in a side panel.

![The Operator chat panel.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximize to expand the panel for easier reading, or minimize to keep Operator available while working.  
{% endalert %}

## Use Operator

Describe what you're trying to accomplish using natural language. Clear and specific prompts lead to more helpful responses. Prompts can range from a single question to a full build request:

- **Ask a question:** Why isn't my Liquid rendering?
- **Build something:** Draft a segment of users who abandoned their card in the last 7 days.

Operator can provide step-by-step instructions, links to Braze documentation, plain-language explanations, and drafts of campaigns, Canvases, segments, and content that you can review and insert directly into your work. For how Operator proposes and applies changes, see [Take action with Operator](#take-action-with-operator). 

Operator uses [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), which is suited for complex, multi-step tasks. For the full range of what Operator can help you build, see [What you can do with Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). For ready-to-use examples, see the [prompt library]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

Watch this video to see one example of what Operator can do.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Best practices

Treat Operator as a conversation, not a search engine. Short, natural prompts work best.

- **Be specific:** Instead of "Tell me about Canvas", try "How do I use Action Paths in Canvas?".  
- **Ask follow-up questions:** If the first response doesn't address your need, ask for clarification or additional details. Operator remembers earlier messages in the conversation until you clear your chat history.
- **Use page-aware context:** Operator understands your location in Braze. Open Operator while viewing the relevant page for the most accurate results.

## Customize your experience

### Apply brand guidelines

Add brand guidelines as context so Operator can match your brand's voice, tone, and personality when it suggests copy or explains features.

1. Select <i class="fa-regular fa-plus"></i>&nbsp;**Add context for Operator** in the chat panel.
2. Under **Brand guidelines**, select one or more guidelines.

Operator applies only the guidelines you select. Nothing is selected by default, including the workspace default.

When you open Operator from **Generate with Operator** or **Refine with Operator** in Agent Console, Operator attaches the guideline already on the agent as context. You can add or remove guidelines from the same menu.

To set up brand guidelines, go to **Content** > **Brand Guidelines**. For more information, see [Brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines).

![Selecting brand guidelines in the Operator chat panel.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Leverage page-aware context

Operator automatically understands your location in Braze and tailors responses based on that context. For example, when you open Operator while building a Canvas, it can suggest relevant steps or provide guidance about Canvas features without you having to explain where you are in your workflow.

This context-awareness means you can use short, natural prompts to interact with Operator, like "Update my editor settings to match my brand guidelines." When your request needs a different part of the dashboard, Operator can [navigate you there]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) directly.


For ready-to-use prompt ideas, see the [prompt library]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Work with Operator responses

### Get started with suggested prompts

When you open a conversation with Operator, suggested prompts appear based on common tasks and your current page. Select one to get started quickly, or type your own custom question.

### Understand how Operator thinks

Operator shows its reasoning steps in collapsible sections labeled **Reasoned**. Select the dropdown to expand these sections and see how Operator determined an answer. This is helpful when you want to understand the logic behind a suggestion or verify the approach.

![The collapsed "Reasoned" dropdown in an Operator response.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Take action with Operator

Operator can propose and execute changes directly in the Braze dashboard, such as filling in form fields, updating settings, generating content, or navigating you to a different page to complete your request. Each proposed change is presented as an action card for you to review and approve before it takes effect. For more on how this works, see [Reviewing actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions).

### Copy responses to other tools

Operator responses are formatted in Markdown. When you've received a response, select **Copy** in the toolbar that appears to copy the full response to your clipboard. Most tools render Markdown natively or accept it with minor adjustments. Select a tab for your destination:

{% tabs %}
{% tab Google Docs %}

First, go to **Tools** > **Preferences** and select **Automatically detect Markdown**. Then to paste Markdown, go to **Edit** > **Paste from Markdown**. You can also right-click and select **Paste from Markdown**.

{% endtab %}
{% tab Microsoft Word and Outlook %}

Word and Outlook don't render Markdown natively. Paste the response into a web-based Markdown previewer, then copy the rendered output and paste it into Word or Outlook with **Keep Source Formatting**. Alternatively, paste as plain text and format manually.

{% endtab %}
{% tab Confluence and Notion %}

Paste directly. Both platforms render Markdown automatically.

{% endtab %}
{% tab Slack %}

Paste directly. Slack renders bold, inline code, code blocks, block quotes, and bulleted lists, but it doesn't render Markdown headings or link syntax.

{% endtab %}
{% tab Other tools %}

If you want to work in a file or use conversion tools, you can also:

- Open a text editor like [VS Code](https://code.visualstudio.com/) and create a new text file, then paste the Markdown and preview to review the formatting before you convert or paste it elsewhere.
- Use [Pandoc](https://pandoc.org/) to convert Markdown into a Word document, HTML, or PDF when you need predictable structure in Word or Outlook without pasting from a browser.

{% endtab %}
{% endtabs %}

## Manage your session

### Stop a response

While Operator is generating a response, the **Send** button becomes a **Stop** button. Select **Stop** to end the response early if you need to rephrase your question or if the response is going in the wrong direction.

### Clear your history

To start fresh or remove sensitive information from the conversation, select **Clear chat history**. This removes all current content and resets the conversation context.

### Provide feedback

At the bottom of each response, use the thumbs up or thumbs down buttons to provide quick feedback. Your feedback helps improve Operator's answers over time.

## Data privacy and security

BrazeAI Operator<sup>TM</sup> integrates with OpenAI, which acts as a Braze sub-processor subject to the Data Processing Addendum (DPA) between you and Braze. Data sent to OpenAI via Braze is not used to train or improve OpenAI models. For details on HIPAA compliance, data retention, PII handling, and governance, see [Data privacy and security]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Next steps

{% article_tiles %}
- name: What you can do with Operator
  link: /docs/user_guide/brazeai/operator/capabilities
- name: Prompt library
  link: /docs/user_guide/brazeai/operator/prompt_library
- name: Review actions
  link: /docs/user_guide/brazeai/operator/reviewing_actions
- name: File support tickets
  link: /docs/user_guide/brazeai/operator/support_tickets
- name: Troubleshooting
  link: /docs/user_guide/brazeai/operator/troubleshooting
- name: Data privacy and security
  link: /docs/user_guide/brazeai/operator/data_privacy_security
{% endarticle_tiles %}
