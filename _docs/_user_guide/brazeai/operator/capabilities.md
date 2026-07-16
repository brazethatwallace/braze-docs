---
nav_title: Capabilities
article_title: What you can do with Operator
page_order: 1
page_type: reference
toc_headers: h2, h3
description: "This reference article covers what BrazeAI Operator™ can do across the dashboard, including building campaigns, segments, and agents; generating copy, messages, Liquid, and images; transforming data; reviewing content quality; and looking up information."
---

# What you can do with Operator {#operator-capabilities}

> The AI capabilities previously available as standalone assistants are now accessible through [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator). Because Operator is built into the dashboard and understands your workspace (your brand guidelines, attributes, Connected Content, and the page you're working on), the output is more context-aware than what the previous assistants could produce.

Instead of opening a different tool for each task, describe what you want in natural language and Operator handles it in context. You can also keep the conversation going—asking for a different tone, a shorter version, or a translation—without starting over. Operator can also propose and execute changes directly through [action cards]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) that you review before they take effect.

## Prerequisites

Operator has the same permissions you do, so certain actions require the relevant permission for that surface—for example, generating an image requires *Edit Media Library Assets*. If you don't see an entry point, check your permissions with your admin. For more information, see [List of permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## Build campaigns and audiences {#build-campaigns-and-audiences}

Operator can help you go from an idea to a drafted campaign or audience, and refine either one once it exists.

### Go from brief to campaign {#go-from-brief-to-campaign}

Describe a full campaign brief, and Operator helps you build a draft that includes copy, images, personalization, targeting, and send-time recommendations. Review the draft in the campaign composer and refine it with follow-up prompts before you launch it.

#### Example prompt {#go-from-brief-to-campaign-example-prompt}

{% include copy_block.html content="Build an HTML email campaign for our loyalty program. Generate a hero image, and write a personalized headline and CTA for each loyalty tier using the Loyalty Tier custom attribute. Only send to users who have a loyalty tier set, and recommend a send time and frequency cap." %}

### Create and edit segments {#create-and-edit-segments}

When you start a segment, describe the audience you want and Operator helps you build the filter logic—attribute conditions, event history, and catalog lookups included. Operator can also help you edit an existing segment's filters when your targeting needs change.

{% include copy_block.html content="Build a segment of users who made a purchase in the last 30 days but haven't opened the app in the last 7 days." %}

### Create and edit campaigns {#create-and-edit-campaigns}

When you start a campaign, Operator can help you draft it end-to-end—audience, content, and delivery settings—from a single natural-language brief. You can also ask Operator to help you edit an existing campaign, such as adjusting targeting or refreshing the message content.

### Create Segment Extensions {#create-segment-extensions}

Operator can help you build a [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension) by writing the SQL query that defines it. Describe the audience logic you want, and Operator drafts the query for you to review before you save it. For more on Operator and SQL, see [Write SQL queries](#write-sql-queries).

## Build and configure agents {#build-and-configure-agents}

Operator can help you build and refine agents in [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents).

### Create an agent from scratch {#create-an-agent-from-scratch}

Operator has access to every field in Agent Console, so you can describe the agent you want and Operator helps you configure it—instructions, output settings, and other agent fields included.

### Start from a template {#start-from-a-template}

Agent Console also offers a **Create agent with Operator** option that loads a pre-written prompt for a common use case, such as copywriting, sentiment analysis, journey routing, or catalog enrichment. Select a category, and Operator helps you draft an agent you can refine. For the full list of templates, see [Agent templates built with Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

### Refine an existing agent {#refine-an-existing-agent}

When you're editing an agent, select **Generate with Operator** or **Refine with Operator** near the agent's instructions field to get Operator's help writing or revising the agent's prompt and output settings.

## Generate content {#generate-content}

### Apply brand guidelines {#apply-brand-guidelines}

Operator uses the brand guidelines configured in your workspace so generated copy, templates, and images match your brand's voice, tone, and style. To set up brand guidelines, go to **Content** > **Brand Guidelines**. For more information, see [Brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines). For details on applying brand guidelines for use with Operator, see [Apply brand guidelines]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines).

### Generate copy {#generate-copy}

You can use Operator to brainstorm or generate copy from anywhere, but you get the best experience using it directly in the message composer, where it can work alongside you on the message you're building. Describe your product or campaign, and Operator returns copy you can review and insert.

Operator improves on the standalone copywriter in a few ways:

- It applies your [brand guidelines](#apply-brand-guidelines) automatically when they're configured.
- It uses [page-aware context]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), so you don't have to re-describe the channel or message you're working on. Because it's page-aware, you can also use it to edit or refine an existing message instead of generating one from scratch.
- It can look up your [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) and events, so you can ask it to personalize copy recommendations with real Liquid.
- You can keep the conversation going and iterate. For example, ask for a different tone, a shorter version, or a translation.

#### Tones {#generate-copy-tones}

The tone of generated copy is driven by your prompt. Describe the style you want—for example, formal, casual, urgent, or eye-catching—and Operator adjusts its output to match. You can also refine the tone in follow-up prompts, such as asking for a more relaxed or more polished version. When [brand guidelines](#apply-brand-guidelines) are configured, Operator applies them automatically so copy stays consistent with your brand's voice.

#### Example prompts {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

### Generate messages {#generate-messages}

Operator can generate message HTML in supported composers. Describe the message you want in natural language, review the output, and insert it into your composer.

You get the best results when you use Operator in the composer you're building, where it has [page-aware context]({{site.baseurl}}/user_guide/brazeai/operator/#leverage-page-aware-context) for the channel and message type. When [brand guidelines](#apply-brand-guidelines) are configured, Operator applies them automatically.

#### HTML Banners {#generate-messages-html-banners}

In the [Banner HTML editor]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner), select **Ask Operator** to generate HTML for your Banner. Describe the layout, content, and styling you want. Operator can include [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) personalization in the generated markup.

Keep the conversation going to refine the result—for example, ask for a different layout, shorter copy, or updated button styling—before you insert the HTML into the editor.

##### Example prompts {#generate-messages-html-banners-example-prompts}

{% include copy_block.html content="Build a Banner that promotes our summer sale with a headline, short description, and Shop now button." %}

{% include copy_block.html content="Use a two-column layout with a product image in the first column and the headline, description, and Shop now button stacked in the second column." %}

{% include copy_block.html content="Make the dismiss button smaller and position it as a corner dismiss control." %}

### Generate Liquid {#generate-liquid}

In any message composer, open Operator to generate and refine Liquid for personalization. Operator understands [Liquid syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), your standard and [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), and [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), and it can explain what the code does.

#### Where you can generate Liquid {#generate-liquid-supported-channels}

As with copywriting, you can ask Operator to generate Liquid from anywhere, and it works across all channels and message composers. You get the best results from within a message composer, where Operator has the full context of the message you're building.

#### Liquid capabilities {#generate-liquid-attributes}

Operator is highly capable with Liquid. It can generate complex Liquid logic grounded in the data in your workspace—including looking up [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs) data to find example values—and it can review and explain the existing Liquid in your campaigns.

#### Best practices {#generate-liquid-best-practices}

##### Use natural language {#generate-liquid-use-natural-language}

Operator is trained to understand natural language. Chat with it as you would with a coworker when asking for help. This helps Operator comprehend your needs and provide accurate assistance.

##### Give context {#generate-liquid-give-context}

Providing context helps Operator understand the bigger picture surrounding your project. It's helpful to include context such as:

- Your company name and industry
- A campaign you're working on, such as Black Friday or holiday sales
- Your goal, such as increasing your click-through rate
- Specific custom attributes you want to include in your message

Including context in your prompt helps Operator tailor its responses to better suit your needs. You can also include details from your campaign, message brief, or brainstorming document to bring Operator up to speed.

##### Be specific {#generate-liquid-be-specific}

Operator can ask follow-up questions, but providing details upfront can lead to more precise results sooner. Consider including details such as:

- Any known preferences or requirements for the message
- Instructions on how to handle situations, such as a lack of responses from the message recipient or fallback message options
- Exact or similar values for the custom attributes you want to use, which help Operator generate and test more accurate logic
- When asking for Liquid that uses Connected Content, documentation for the API endpoint, a sample API response, or both

##### Get creative {#generate-liquid-get-creative}

Try different prompts to see how Operator can enhance your messaging. Experiment with different prompts and ideas, as creativity can lead to more engaging results.

#### Example prompts {#generate-liquid-example-prompts}

{% tabs local %}
{% tab About Liquid %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% endtab %}
{% tab Personalization %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." %}

{% endtab %}
{% endtabs %}

### Generate images {#generate-images}

Operator generates images using [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), an AI system from OpenAI and a Braze third-party provider. This lets you create realistic images and art from a description in natural language.

In the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), select **Generate with Operator** from the **Upload Assets** panel. Describe the image you want, and Operator generates it and saves it directly to your media library.

#### Prompt tips {#generate-images-prompt-tips}

- Describe the subject, style, mood, and colors specifically. The more detail you include, the better the result.
- Text input only; uploading a reference image is not supported.
- When you apply [brand guidelines](#apply-brand-guidelines) as context in your Operator prompt, Operator applies them directly to the generated image, so the result reflects your brand's visual style.
- Image generations count toward your daily Operator usage limit. For more information, see [Limitations]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting#limitations).

#### Example prompts {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

### What Operator can create {#what-operator-can-create}

Beyond copy, messages, and Liquid, Operator can help you build several other objects across the dashboard, including but not limited to:

- Content Blocks
- Message templates
- Banners
- [Images](#generate-images)
- [Segments](#create-and-edit-segments) and [campaigns](#create-and-edit-campaigns)

This list isn't exhaustive—ask Operator directly if you're not sure whether it can help with a specific object.

### Channel support {#channel-support}

Operator can generate message HTML for any channel or editor with an HTML mode, including Email, SMS/RCS, In-App Messages, Content Cards, Push, and webhooks. Drag-and-drop editors aren't supported. For channel-specific guidance, see [Generate messages](#generate-messages).

## Automate and transform data {#automate-and-transform-data}

### Generate data transformation code {#generate-data-transformation-code}

In the [Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) editor, select **Insert Code** to generate transformation code that turns an incoming webhook payload into valid Braze API requests.

For step-by-step instructions on creating a transformation, see [Create a transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

#### Example prompts {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## Review and quality-check content {#review-and-quality-check-content}

### Review content quality {#review-content-quality}

On the **Test** tab for SMS, Android push, iOS push, and traditional in-app messages, select **Review with Operator** to review your content before sending. By default, Operator reviews your campaign for spelling and grammar errors, off-brand or inappropriate tone, offensive language, and any stray code, test content, or unrendered Liquid, and it recommends how to fix what it finds. You can also ask Operator to tailor how it reviews your content directly in your prompt.

#### What you can ask Operator to check {#review-content-quality-supported-features}

Beyond its default review, you can direct Operator to focus on specific checks. Consider prompting it to look at any of the following:

| Check | What to ask for |
| --- | --- |
| Spelling and grammar | Ask Operator to proofread for spelling and grammar mistakes and suggest corrections that improve the accuracy of your content. |
| Tone | Ask Operator to evaluate whether the tone matches your intended communication style and flag anything that could be misunderstood. |
| Offensive language | Ask Operator to scan for potentially offensive or inappropriate language so you can revise it and keep your messaging respectful. |
| Accidental content | Ask Operator to catch stray code, markup, or test messages that you added unintentionally, including Liquid that didn't render for a test user. |
| Other languages | Ask Operator to review content written in another language. Support for non-English content can vary, so review the results carefully. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What you can ask Operator to check" }

#### Best practices {#review-content-quality-best-practices}

Consider the following to make the most of content review:

- **Proofread your message:** Although content review can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
- **Understand the tone analysis:** The tone analysis results are subjective and based on the AI model's understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
- **Double-check flagged offensive language:** Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

#### Example prompts {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

## Look things up {#look-things-up}

### What Operator can look up {#what-operator-can-look-up}

Operator can reference the following to answer questions or ground the content it generates:

- [Custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) and events
- [Catalog]({{site.baseurl}}/user_guide/data/activation/catalogs) data
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) responses
- Existing campaign and Canvas configuration, such as targeting and delivery settings
- Braze documentation

Ask Operator directly if you're not sure whether it can look up a specific piece of information.

### Write SQL queries {#write-sql-queries}

Operator can help you write SQL for [Segment Extensions](#create-segment-extensions) and for [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) [query templates]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates). Describe the query you want in natural language, and Operator generates SQL for you to review before you run it.

## Where Operator has limits {#where-operator-has-limits}

Operator's dashboard support is broad, but it has boundaries. Operator's coverage changes frequently—if you're not sure whether it supports a specific screen or workflow, ask it directly.

### Editors and surfaces {#editors-and-surfaces}

Operator doesn't support drag-and-drop editors, such as Beefree, GrapesJS, or Craft.js. If you're working in one of these editors, switch to the corresponding HTML editor to use Operator, or ask Operator to generate content you can paste in manually.

### What Operator can see on screen {#what-operator-can-see-on-screen}

Operator uses page-aware context to understand what you're looking at, including content inside supported previews and editors. When part of a page falls outside what Operator can read, it tells you instead of guessing, so you know to describe that content yourself.

## Quick answers {#quick-answers}

### Does Operator work in the drag-and-drop email editor? {#quick-answers-drag-and-drop-editor}

No. Switch to the HTML editor to use Operator, or ask Operator to generate content you can paste in manually. See [Editors and surfaces](#editors-and-surfaces).

### Can Operator see everything on my screen? {#quick-answers-screen-visibility}

No. Operator tells you when part of a page falls outside what it can read instead of guessing. See [What Operator can see on screen](#what-operator-can-see-on-screen).

### Does Operator work the same way in every message composer? {#quick-answers-composer-parity}

Message generation requires an HTML mode. See [Channel support](#channel-support).

### Can Operator save changes without my approval? {#quick-answers-approval}

No. Operator proposes changes as [action cards]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) that you review and approve first.

### Is there a limit to how much I can use Operator? {#quick-answers-usage-limits}

Yes, a company-wide daily usage limit applies; image generation counts toward it. See [Limitations]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting#limitations).

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Legacy assistants {#legacy-assistants}

Before Operator, several AI features stood alone as separate assistants: the AI Copywriter, AI Liquid Assistant, AI Image Generator, the Data Transformations AI Copilot, and content review. All of their entry points remain in place and route to Operator, so your existing workflows are unaffected. For what these do today, see [Generate content](#generate-content), [Automate and transform data](#automate-and-transform-data), and [Review and quality-check content](#review-and-quality-check-content).

## Data privacy and security {#data-privacy-and-security}

Operator integrates with OpenAI to generate output. For more information about what information Braze sends to OpenAI, how that data is used, and your intellectual property rights, see [How data is used with OpenAI]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security).

## Next steps {#next-steps}

- [Get started with Operator]({{site.baseurl}}/user_guide/brazeai/operator): Access and use Operator
- [Review actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Review and approve Operator's proposed changes
- [Troubleshooting]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Reference common issues and solutions
