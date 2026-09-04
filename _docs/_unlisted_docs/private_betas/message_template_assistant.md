---
nav_title: HTML email templates
article_title: Generate HTML email templates
permalink: "/template_assistant/"
description: "This reference article covers how to generate HTML email templates using Operator, including how it works and example prompts."
page_type: reference
---

# Generate HTML email templates

> Generate and iterate on HTML email templates using Operator. Describe the template you need in natural language, and Operator builds or modifies it using your brand guidelines and global style settings.

{% alert important %}
Generating HTML email templates with Operator is in early access. Contact your Braze account manager if you're interested in participating in this early access.

This functionality is only supported for the email channel in the HTML editor, not in other editors (such as drag-and-drop or AMP).
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## How to access

In the HTML email template editor, the **Generate** sidebar group contains the **Template** option. Select it to generate or iterate on an on-brand HTML email template. Operator applies your [brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) so the result matches your voice and style.


## How it works

Operator uses your [brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) and [global style settings]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) to tailor the message content and style to your brand.

For example, if you have global style settings set up, Operator incorporates your brand's colors and styles. If you have brand guidelines defined in Braze, Operator also references these to create copy in the tone and personality of your brand.

Operator also iterates your template for mobile responsiveness.

## Example prompts

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}
