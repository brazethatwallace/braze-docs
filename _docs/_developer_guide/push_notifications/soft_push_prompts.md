---
page_order: 6
nav_title: Soft push prompts
article_title: Soft push prompts for Web
description: "Learn how to set up soft push prompts for the Braze Web SDK before the native browser notification permission prompt."
channel:
  - push notifications
---

# Soft push prompts for Web

> Soft push prompts are custom messages you show before the browser's native notification permission prompt. They explain why users should enable push notifications and can improve opt-in rates compared with displaying the system prompt on first visit. This guide covers how to implement soft push prompts with the Braze Web SDK, including when to trigger the prompt, how to customize the message content, and best practices for timing the request after users understand the value of push.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications/soft_push_prompts.md %}
{% endsdktab %}
{% endsdktabs %}

## Frequently asked questions

### What is a soft push prompt? {#what-is-a-soft-push-prompt}

A soft push prompt is a custom in-app or on-site message you show before the browser's native notification permission dialog. It explains the value of push so users are more likely to accept when the system prompt appears.

### When should I show a soft push prompt? {#when-should-i-show-a-soft-push-prompt}

Show a soft push prompt after users understand your product value—for example, after onboarding or a meaningful in-app action—not on first page load. Refer to the Web SDK steps in this guide for implementation details.
