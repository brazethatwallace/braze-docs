---
nav_title: Capabilities
article_title: What you can do with Operator
page_order: 1
page_type: reference
toc_headers: h2
description: "This reference article covers what BrazeAI Operator™ can do across the dashboard, including building campaigns, segments, and agents; generating copy, messages, Liquid, and images; transforming data; reviewing content quality; and looking up information."
---

# What you can do with Operator {#operator-capabilities}

> [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator) is an AI assistant built into the Braze dashboard. It answers questions, composes messages, and acts across supported pages—describe what you want in natural language and Operator handles it in context.

Because Operator understands your workspace—your brand guidelines, custom attributes, Connected Content, and the page you're working on—its output is more context-aware than what standalone assistants can produce. When Operator proposes a change to a campaign, segment, or other object, it shows the change as a visual diff in an [action card]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) that you review and approve before anything is saved.

You can keep the conversation going with follow-ups. Operator remembers earlier messages until you clear your chat history.

## Prerequisites

Operator has the same permissions you do, so certain actions require the relevant permission for that surface. For example, generating an image requires *Edit Media Library Assets*. If you don't see an entry point, check your permissions with your admin. For more information, see [List of permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

## What Operator can create {#what-operator-can-create}

Beyond generating copy and Liquid, Operator can help you build several other objects across the dashboard, including but not limited to:

- Campaigns
- Content Blocks
- Custom agents
- Images
- Messages and message templates (see [Generate messages](#generate-messages) and [Create message templates](#create-message-templates))
- Segments
- Segment Extensions

{% alert note %}
Operator's capabilities across the dashboard expand regularly. **Ask Operator directly** for the most current answer of what it can do.
{% endalert %}

## Campaigns and audiences {#campaigns-and-audiences}

Operator can help you go from an idea to a drafted campaign or audience, and refine either one once it exists. Any changes Operator proposes to a campaign or segment appear as an action card you review before they're saved.

To get started, look for the **Create with Operator** option when you create a campaign or segment.

![The Create campaign and Create Segment menus, each showing the Create with Operator option.]({% image_buster /assets/img/operator/operator_create_with_operator.png %})

- **Create and edit campaigns:** When you start a campaign, Operator can help you draft it end-to-end from a single natural-language brief. This includes audience, content, and delivery settings. You can also ask Operator to help you edit an existing campaign, such as adjusting targeting or refreshing the message content.
- **Go from brief to campaign:** Describe a full campaign brief, and Operator helps you build a draft that includes copy, images, personalization, targeting, and send-time recommendations. Review the draft in the campaign composer and refine it with follow-up prompts before you launch it.
- **Create and edit segments:** When you start a segment, describe the audience you want and Operator helps you build the filter logic—attribute conditions, event history, and catalog lookups included. Operator can also help you edit an existing segment's filters when your targeting needs change.
- **Create Segment Extensions:** Operator can help you build a SQL-defined [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension) by writing the query that defines it. Describe the audience logic you want, and Operator drafts the query for you to review before you save it. For more on Operator and SQL, see [Write SQL queries](#write-sql-queries).

## Agents {#agents}

Operator can help you build and refine agents in [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents). Any changes Operator proposes to an agent appear as an action card you review before they're saved.

![The Create agent menu, showing the Custom agent option and Operator-built agent templates.]({% image_buster /assets/img/operator/operator_create_agent.png %})

- **Create an agent from scratch:** Operator has access to every field in Agent Console, so you can describe the agent you want and Operator helps you configure it—instructions, output settings, and other agent fields included.
- **Start from template:** Agent Console offers a **Create agent with Operator** option that loads a pre-written prompt for a common use case, such as copywriting, sentiment analysis, journey routing, or catalog enrichment. Select a category, and Operator helps you draft an agent you can refine. For the full list of templates, see [Agent templates built with Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).
- **Refine an existing agent:** When you're editing an agent, select **Generate with Operator** or **Refine with Operator** near the agent's instructions field to get Operator's help writing or revising the agent's prompt and output settings.

## Content and creative {#content-and-creative}

Operator can generate and review the content in your messages, including copy, message HTML, Liquid, and images, and applies your brand guidelines automatically wherever they're configured.

### Apply brand guidelines {#apply-brand-guidelines}

Operator uses the brand guidelines configured in your workspace so generated copy, templates, and images match your brand's voice, tone, and style. To set up brand guidelines, go to **Content** > **Brand Guidelines**. For more information, see [Brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) and [Apply brand guidelines]({{site.baseurl}}/user_guide/brazeai/operator#apply-brand-guidelines) in the Operator usage guide.

### Generate copy {#generate-copy}

You can use Operator to brainstorm or generate copy from anywhere, but you get the best experience using it directly in the message composer, where it can work alongside you on the message you're building. Describe your product or campaign, and Operator returns copy you can review and insert.

Operator improves on the standalone copywriter in a few ways:

- It applies your [brand guidelines](#apply-brand-guidelines) automatically when they're configured.
- It uses [page-aware context]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context), so you don't have to re-describe the channel or message you're working on. Because it's page-aware, you can also use it to edit or refine an existing message instead of generating one from scratch.
- It can look up your [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) and events, so you can ask it to personalize copy recommendations with real Liquid.
- You can keep the conversation going and iterate. For example, ask for a different tone, a shorter version, or a translation.

#### Tones {#generate-copy-tones}

The tone of generated copy is driven by your prompt. Describe the style you want and Operator adjusts its output to match. For example, ask for formal, casual, urgent, or eye-catching. You can also refine the tone in follow-up prompts, such as asking for a more relaxed or more polished version. When brand guidelines are configured, Operator applies them automatically so copy stays consistent with your brand's voice.

### Generate messages {#generate-messages}

Operator can generate a full message design for any channel or editor with an HTML mode, including but not limited to:

- Email
- SMS/MMS/RCS
- In-app message
- Content Card
- Banner
- Push
- Webhook

Drag-and-drop editors don't support direct design generation, though Operator can still help with copy or other content you add manually. Describe the message you want in natural language, review the output, and insert it into your composer. Keep the conversation going to refine the result. For example, you can ask for a different layout, shorter copy, or updated button styling before you insert the HTML into the editor. 

You get the best results when you use Operator in the composer you're building, where it has [page-aware context]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context) for the channel and message type. When brand guidelines are configured, Operator applies them automatically.

### Create Content Blocks {#create-content-blocks}

Operator can help you create [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), the reusable pieces of content you insert across messages. Describe the block you want, and Operator drafts its content for you to review before you save it. Because Content Blocks are shared, updating one updates every message that references it.

### Create message templates {#create-message-templates}

Operator can help you create reusable [message templates]({{site.baseurl}}/user_guide/messaging/templates) that you can apply across campaigns. Describe the template you want, and Operator drafts it for you to review before you save it. Generating a template works much like generating a message, so see [Generate messages](#generate-messages) for the supported channels and editors.

### Generate Liquid {#generate-liquid}

Operator is highly capable with [Liquid syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). It can generate complex Liquid logic grounded in the data in your workspace, including looking up attribute, event, and [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs) data to find example values. It can also review and explain the existing Liquid in your campaigns.

As with copywriting, you can ask Operator to generate Liquid from anywhere, and it works across all channels and message composers. You get the best results from within a message composer, where Operator has the full context of the message you're building.

{% details Liquid prompting best practices %}

#### Give context {#generate-liquid-give-context}

Providing context helps Operator understand the bigger picture surrounding your project. It's helpful to include context such as:

- Your company name and industry
- A campaign you're working on, such as Black Friday or holiday sales
- Your goal, such as increasing your click-through rate
- Specific custom attributes you want to include in your message

Including context in your prompt helps Operator tailor its responses to better suit your needs. You can also include details from your campaign, message brief, or brainstorming document to bring Operator up to speed.

#### Be specific {#generate-liquid-be-specific}

Operator can ask follow-up questions, but providing details upfront can lead to more precise results sooner. Consider including details such as:

- Any known preferences or requirements for the message
- Instructions on how to handle situations, such as a lack of responses from the message recipient or fallback message options
- Exact or similar values for the custom attributes you want to use, which help Operator generate and test more accurate logic
- When asking for Liquid that uses Connected Content, documentation for the API endpoint, a sample API response, or both

#### Get creative {#generate-liquid-get-creative}

Try different prompts to see how Operator can enhance your messaging. Experiment with different prompts and ideas, as creativity can lead to more engaging results.

{% enddetails %}

### Generate images {#generate-images}

Operator generates images using [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), an AI system from OpenAI and a Braze third-party provider. This lets you create realistic images and art from a description in natural language.

In the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), select **Generate with Operator** from the **Upload Assets** panel. Describe the image you want, and Operator generates it and saves it directly to your media library.

#### Prompt tips {#generate-images-prompt-tips}

- Describe the subject, style, mood, and colors specifically. The more detail you include, the better the result. Uploading a reference image is not supported.
- When you apply [brand guidelines](#apply-brand-guidelines) as context in your Operator prompt, Operator applies them directly to the generated image, so the result reflects your brand's visual style.
- Image generations count toward your daily Operator usage limit. For more information, see [Limitations](#limitations).

### Review content quality {#review-content-quality}

On the **Test** tab for SMS, Android push, iOS push, and traditional in-app messages, select **Review with Operator** to review your content before sending. By default, Operator reviews your campaign for spelling and grammar errors, off-brand or inappropriate tone, offensive language, and any stray code, test content, or unrendered Liquid, and it recommends how to fix what it finds. You can also ask Operator to tailor how it reviews your content directly in your prompt.

Beyond its default review, you can direct Operator to focus on specific checks. Consider prompting it to look at any of the following:

- **Spelling and grammar:** Proofread for spelling and grammar mistakes and suggest corrections that improve the accuracy of your content.
- **Tone:** Evaluate whether the tone matches your intended communication style and flag anything that could be misunderstood.
- **Offensive language:** Scan for potentially offensive or inappropriate language so you can revise it and keep your messaging respectful.
- **Accidental content:** Catch stray code, markup, or test messages that were added unintentionally, including Liquid that didn't render for a test user.
- **Other languages:** Review content written in another language. Support for non-English content can vary, so review the results carefully.

#### Best practices {#review-content-quality-best-practices}

Consider the following to make the most of content review:

- **Proofread your message:** Although content review can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
- **Understand the tone analysis:** The tone analysis results are subjective and based on the AI model's understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
- **Double-check flagged offensive language:** Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

## Data automation and lookup {#data-automation-and-lookup}

Operator can act as a reference for your workspace data and Braze documentation, write SQL when you need to query that data directly, and generate the code that transforms incoming data, such as a webhook payload, into a format Braze can use.

### What Operator can look up {#what-operator-can-look-up}

Operator can reference the following to answer questions or ground the content it generates, including but not limited to:

- Braze documentation
- Existing [campaign]({{site.baseurl}}/user_guide/messaging/campaigns) and [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) configuration, such as targeting and delivery settings
- [Segments]({{site.baseurl}}/user_guide/audience/segments)
- [Custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) and [custom events]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [Catalog]({{site.baseurl}}/user_guide/data/activation/catalogs) data
- [Agents]({{site.baseurl}}/user_guide/brazeai/agents)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Promotion codes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) responses

Ask Operator directly if you're not sure whether it can look up a specific piece of information.

### Write SQL queries {#write-sql-queries}

Operator can help you write SQL for [Segment Extensions](#campaigns-and-audiences) and for Query Builder [query templates]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates). Describe the query you want in natural language, and Operator generates SQL for you to review before you run it.

### Generate data transformation code {#generate-data-transformation-code}

In the [Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) editor, select **Insert Code** to generate transformation code that turns an incoming webhook payload into valid Braze API requests. For step-by-step instructions on creating a transformation, see [Create a transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

## Limitations {#limitations}

{% alert note %}
Operator's coverage changes frequently. If you're not sure whether a specific screen or workflow is supported, ask Operator directly.
{% endalert %}

Operator's dashboard support is broad, but it has boundaries.

- **Canvases:** Operator can't create or edit [Canvases]({{site.baseurl}}/user_guide/messaging/canvas) yet, though this support is coming soon. Operator can still read an existing Canvas's configuration to answer questions and ground its output.
- **Drag-and-drop editors:** Operator can't generate or insert a message design directly in a drag-and-drop editor, such as the ones for [email]({{site.baseurl}}/user_guide/channels/email/drag_and_drop), [Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner), and [in-app messages]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop). Switch to the corresponding HTML editor to use Operator, or ask Operator to generate content, such as copy, that you can paste in manually. See [Generate messages](#generate-messages) for supported channels and editors.
- **Screen visibility:** Operator uses page-aware context to understand what you're looking at, including content inside supported previews and editors. When part of a page falls outside what Operator can read, it tells you instead of guessing, so you know to describe that content yourself.
- **Usage limits:** Operator has a company-wide daily usage limit that resets every 24 hours. Image generations count toward this limit. If the limit is reached, a "Daily usage limit exceeded" message appears and no further requests can be made until it resets. For troubleshooting steps, see [Troubleshooting]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting).

## Legacy assistants {#legacy-assistants}

Before Operator, several AI features stood alone as separate assistants: the AI Copywriter, AI Liquid Assistant, AI Image Generator, AI SQL Generator, the Data Transformations AI Copilot, and content review. All of their entry points remain in place and route to Operator, so your existing workflows are unaffected. For what these do today, see [Content and creative](#content-and-creative) and [Data automation and lookup](#data-automation-and-lookup).

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Data privacy and security {#data-privacy-and-security}

Operator integrates with OpenAI to generate output. For more information about what information Braze sends to OpenAI, how that data is used, and your intellectual property rights, see [How data is used with OpenAI]({{site.baseurl}}/user_guide/brazeai/operator#data-privacy-and-security).

## Next steps {#next-steps}

- [Get started with Operator]({{site.baseurl}}/user_guide/brazeai/operator): Access and use Operator
- [Prompt library]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): Browse ready-to-use example prompts
- [Review actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Review and approve Operator's proposed changes
- [Troubleshooting]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Reference common issues and solutions
