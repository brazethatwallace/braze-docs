---
nav_title: Capabilities
article_title: What you can do with Operator
page_order: 1
page_type: reference
toc_headers: h2
description: "This reference article covers the AI tasks available through BrazeAI Operator™ — including copywriting, Liquid, image generation, data transformation code, and content review."
---

# What you can do with Operator {#operator-capabilities}

> The AI capabilities previously available as standalone assistants are now accessible through [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/). Because Operator is built into the dashboard and understands your workspace (your brand guidelines, attributes, Connected Content, and the page you're working on), the output is more context-aware than what the previous assistants could produce.

Instead of opening a different tool for each task, describe what you want in natural language and Operator handles it in context. You can also keep the conversation going—asking for a different tone, a shorter version, or a translation—without starting over. Operator can also propose and execute changes directly through [action cards]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) that you review before they take effect.

## Prerequisites

Operator has the same permissions you do, so certain actions require the relevant permission for that surface—for example, generating an image requires *Edit Media Library Assets*. If you don't see an entry point, check your permissions with your admin. For more information, see [List of permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions).

## What's available through Operator {#whats-available-through-operator}

All existing entry points remain in place, so your workflows are unaffected. These experiences are now powered by Operator. The following table maps each previous standalone assistant to where to find it now.

| Previous assistant | What it did | Where to find it now |
| --- | --- | --- |
| AI Copywriter | Generated marketing copy from a product name or description | A new **Ask Operator** icon in the SMS, push, HTML email, and Canvas composers |
| AI Liquid Assistant | Generated Liquid for personalization | A new **Ask Operator** icon in the SMS, push, HTML email, and Canvas composers |
| AI Image Generator | Generated images from a text prompt for the media library | A new **Generate with Operator** button in the media library |
| Data Transformations AI Copilot | Generated transformation code | The **Insert Code** button on the Data Transformation page |
| Content review | Checked content for spelling, grammar, tone, offensive language, and stray code | **Review with Operator** button on the **Test** tab |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="What's available through Operator" }

## Apply brand guidelines {#apply-brand-guidelines}

Operator uses the brand guidelines configured in your workspace so generated copy, templates, and images match your brand's voice, tone, and style. To set up brand guidelines, go to **Content** > **Brand Guidelines**. For more information, see [Brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/). For details on applying brand guidelines for use with Operator, see [Apply brand guidelines]({{site.baseurl}}/user_guide/brazeai/operator/#apply-brand-guidelines).

## Generate copy {#generate-copy}

You can use Operator to brainstorm or generate copy from anywhere, but you get the best experience using it directly in the message composer, where it can work alongside you on the message you're building. Describe your product or campaign, and Operator returns copy you can review and insert.

Operator improves on the standalone copywriter in a few ways:

- It applies your [brand guidelines](#apply-brand-guidelines) automatically when they're configured.
- It uses [page-aware context]({{site.baseurl}}/user_guide/brazeai/operator/#leverage-page-aware-context), so you don't have to re-describe the channel or message you're working on. Because it's page-aware, you can also use it to edit or refine an existing message instead of generating one from scratch.
- It can look up your [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) and events, so you can ask it to personalize copy recommendations with real Liquid.
- You can keep the conversation going and iterate. For example, ask for a different tone, a shorter version, or a translation.

### Tones {#generate-copy-tones}

The tone of generated copy is driven by your prompt. Describe the style you want—for example, formal, casual, urgent, or eye-catching—and Operator adjusts its output to match. You can also refine the tone in follow-up prompts, such as asking for a more relaxed or more polished version. When [brand guidelines](#apply-brand-guidelines) are configured, Operator applies them automatically so copy stays consistent with your brand's voice.

### Example prompts {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

## Generate Liquid {#generate-liquid}

In any message composer, open Operator to generate and refine Liquid for personalization. Operator understands [Liquid syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/), your standard and [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), and [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), and it can explain what the code does.

### Where you can generate Liquid {#generate-liquid-supported-channels}

As with copywriting, you can ask Operator to generate Liquid from anywhere, and it works across all channels and message composers. You get the best results from within a message composer, where Operator has the full context of the message you're building.

### Liquid capabilities {#generate-liquid-attributes}

Operator is highly capable with Liquid. It can generate complex Liquid logic grounded in the data in your workspace—including looking up [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) data to find example values—and it can review and explain the existing Liquid in your campaigns.

### Best practices {#generate-liquid-best-practices}

#### Use natural language {#generate-liquid-use-natural-language}

Operator is trained to understand natural language. Chat with it as you would with a coworker when asking for help. This helps Operator comprehend your needs and provide accurate assistance.

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

### Example prompts {#generate-liquid-example-prompts}

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

## Generate images {#generate-images}

Operator generates images using [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), an AI system from OpenAI and a Braze third-party provider. This lets you create realistic images and art from a description in natural language.

In the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/), select **Generate with Operator** from the **Upload Assets** panel. Describe the image you want, and Operator generates it and saves it directly to your media library.

### Prompt tips {#generate-images-prompt-tips}

- Describe the subject, style, mood, and colors specifically. The more detail you include, the better the result.
- Text input only; uploading a reference image is not supported.
- When you apply [brand guidelines](#apply-brand-guidelines) as context in your Operator prompt, Operator applies them directly to the generated image, so the result reflects your brand's visual style.
- Image generations count toward your daily Operator usage limit. For more information, see [Limitations]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/#limitations).

### Example prompts {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

## Generate data transformation code {#generate-data-transformation-code}

In the [Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/) editor, select **Insert Code** to generate transformation code that turns an incoming webhook payload into valid Braze API requests.

For step-by-step instructions on creating a transformation, see [Create a transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation/).

### Example prompts {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## Review content quality {#review-content-quality}

On the **Test** tab for SMS, Android push, iOS push, and traditional in-app messages, select **Review with Operator** to review your content before sending. By default, Operator reviews your campaign for spelling and grammar errors, off-brand or inappropriate tone, offensive language, and any stray code, test content, or unrendered Liquid, and it recommends how to fix what it finds. You can also ask Operator to tailor how it reviews your content directly in your prompt.

### What you can ask Operator to check {#review-content-quality-supported-features}

Beyond its default review, you can direct Operator to focus on specific checks. Consider prompting it to look at any of the following:

| Check | What to ask for |
| --- | --- |
| Spelling and grammar | Ask Operator to proofread for spelling and grammar mistakes and suggest corrections that improve the accuracy of your content. |
| Tone | Ask Operator to evaluate whether the tone matches your intended communication style and flag anything that could be misunderstood. |
| Offensive language | Ask Operator to scan for potentially offensive or inappropriate language so you can revise it and keep your messaging respectful. |
| Accidental content | Ask Operator to catch stray code, markup, or test messages that you added unintentionally, including Liquid that didn't render for a test user. |
| Other languages | Ask Operator to review content written in another language. Support for non-English content can vary, so review the results carefully. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What you can ask Operator to check" }

### Best practices {#review-content-quality-best-practices}

Consider the following to make the most of content review:

- **Proofread your message:** Although content review can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
- **Understand the tone analysis:** The tone analysis results are subjective and based on the AI model's understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
- **Double-check flagged offensive language:** Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

### Example prompts {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Data privacy and security {#data-privacy-and-security}

Operator integrates with OpenAI to generate output. For more information about what information Braze sends to OpenAI, how that data is used, and your intellectual property rights, see [How data is used with OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/#how-data-is-used-with-openai).

## Next steps {#next-steps}

- [Get started with Operator]({{site.baseurl}}/user_guide/brazeai/operator/): Access and use Operator
- [Review actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Review and approve Operator's proposed changes
- [Troubleshooting]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): Reference common issues and solutions
