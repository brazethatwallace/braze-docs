---
nav_title: Prompt library
article_title: Prompt library for BrazeAI Operator
page_order: 4
page_type: reference
description: "Browse example prompts for BrazeAI Operator, organized by what you want to accomplish."
---

# Prompt library for BrazeAI Operator

> Browse a curated collection of example Operator prompts, compiled by Braze experts. Select a goal to find relevant prompts. For more information, see [Leverage page-aware context]({{site.baseurl}}/user_guide/brazeai/operator#leverage-page-aware-context).


<div class="prompt-library-tabs">
{% sdktabs local %}
{% sdktab Data analysis %}

{% include copy_block.html content="Summarize the key trends for MAU, DAU, and New Users in this date range and what to do next." available="Home page" %}

{% include copy_block.html content="Show the MAU, DAU, and New Users trends for the last 90 days—where are the biggest dips and spikes?" available="Home page" %}

{% include copy_block.html content="Break down sessions by app (if available) and highlight which app is driving the most growth this month." available="Home page" %}

{% include copy_block.html content="Give me a 5-bullet health check of our engagement program for the last 30 days, with the biggest opportunities." available="Home page" %}

{% include copy_block.html content="Which Active Canvases drove the most attributed conversions and revenue in FY26 Q1 (7-day attribution)?" available="Canvas" %}

{% include copy_block.html content="Summarize this Campaign Digest in 5 bullets: biggest wins, biggest issues, and what changed versus the prior period." available="Campaigns" %}

{% endsdktab %}
{% sdktab Strategy and optimization %}

{% include copy_block.html content="What are 3 ways to use these app usage insights to shape a re-engagement Canvas for churn risk users?" available="Home page" %}

{% include copy_block.html content="What does our x% stickiness imply, and what are 3 ways to improve it with lifecycle messaging?" available="Home page" %}

{% include copy_block.html content="What are 3 ways to optimize our active lifecycle Canvases to increase activation and reduce churn?" available="Canvas" %}

{% include copy_block.html content="What are 3 ways to restructure our onboarding Canvases to reduce drop-off and improve activation?" available="Canvas" %}

{% include copy_block.html content="Show my idle Canvases and summarize what they last sent and when users last entered (last 90 days)." available="Canvas" %}

{% include copy_block.html content="How can we use the [your segment name] segment to build a re-engagement journey and reduce churn?" available="Segments" %}

{% include copy_block.html content="How should we structure frequency-capping extensions (email/SMS/48h) to reduce over-messaging without hurting conversions?" available="Segment Extensions" %}

{% include copy_block.html content="What are 3 high-impact reports we should create here to monitor weekly campaign and Canvas health and catch issues early?" available="Report Builder" %}

{% endsdktab %}
{% sdktab Messaging performance %}

{% include copy_block.html content="Show this campaign's key engagement metrics (open/click rates) for the last 30 days and the prior 30 days." available="Individual campaign" %}

{% include copy_block.html content="How much Attributed Revenue and Conversions did this campaign drive in the last 90 days (7-day window)?" available="Individual campaign" %}

{% include copy_block.html content="Compare this campaign's conversion rate versus our other in-app campaigns in this quarter to date." available="Individual campaign" %}

{% include copy_block.html content="Show the top 10 active campaigns by engagement rate in the last 30 days (by channel)." available="Campaigns, Individual campaign" %}

{% include copy_block.html content="What channels performed best for campaigns targeting 'C&L Newsletter Clickers' versus 'Openers but not Clickers' in the last 30 days?" available="Segments" %}

{% include copy_block.html content="How much Attributed Revenue and Conversions did campaigns generate for users excluded by our caps in the last 30 days (7-day window)?" available="Segment Extensions" %}

{% include copy_block.html content="Compare our email Open Rate and Click-Through Rate versus industry benchmarks for the last 30 days." available="Email Performance" %}

{% include copy_block.html content="Which email campaigns had the lowest CTR (with high opens) in the last 30 days?" available="Email Performance" %}

{% endsdktab %}
{% sdktab Personalization and Liquid %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." available="Message composer" %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." available="Message composer" %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." available="Message composer" %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." available="Message composer" %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." available="Message composer" %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." available="Message composer" %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." available="Message composer" %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." available="Message composer" %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" available="Message composer" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." available="Message composer" %}

{% endsdktab %}
{% sdktab Audience management %}

{% include copy_block.html content="Which of our active segments were edited most recently, and which ones look like duplicates we should consolidate?" available="Segments" %}

{% include copy_block.html content='What does "Complex audience" mean here, and how can I simplify those campaigns without losing targeting?' available="Campaigns" %}

{% include copy_block.html content="What are 3 ways to reduce 'complex audience' in these campaigns without losing targeting accuracy?" available="Campaigns" %}

{% endsdktab %}
{% sdktab Onboarding %}

{% include copy_block.html content="Based on what's on this dashboard, what are the first 5 places I should visit in Braze to understand our setup (data, channels, sending, and targeting)?" available="Home page" %}

{% include copy_block.html content="I'm feeling overwhelmed, I want to get started with Agent Console but don't know how. Based on my currently running campaigns, what might I do?" available="Campaigns" %}

{% include copy_block.html content="What can I do on the Knowledge Sources page, and what's the fastest way to get my first source set up?" available="Agent Console" %}

{% endsdktab %}
{% sdktab Maintenance and cost savings %}

{% include copy_block.html content="Show me the 5 idle active campaigns and recommend which to pause, refresh, or archive." available="Campaigns" %}

{% include copy_block.html content="Which Segment Extensions are active but haven't been processed recently, and are they safe to archive for free slots?" available="Segment Extensions" %}

{% include copy_block.html content="How can we reduce Query Builder credit usage without losing reporting coverage? Suggest 3 tactics." available="Query Builder" %}

{% include copy_block.html content="Which saved queries haven't been run in 90 days—can you help me identify candidates to archive?" available="Query Builder" %}

{% endsdktab %}
{% endsdktabs %}
</div>
