---
nav_title: Preference center
article_title: Preference center
page_order: 8
layout: dev_guide
guide_top_header: "Preference center"
guide_top_text: "An email preference center lets users manage notification preferences for email campaigns and newsletters from a branded page in your app or website. Use these articles to create and manage a preference center with the <a href='/docs/api/endpoints/preference_center'>Braze Preference Center API</a> or the drag-and-drop editor, including subscription groups, opt-in states, and hosted page customization."
description: "This landing page includes articles on the Braze email preference center and how to use the Preference Center API."
channel:
  - email

guide_featured_title: "Section articles"
guide_featured_list:
- name: API email preference center
  link: /docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
  image: /assets/img/braze_icons/list.svg
- name: Drag-and-drop preference center
  link: /docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
  image: /assets/img/braze_icons/mail-01.svg

---

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

## Frequently asked questions

### What is an email preference center? {#what-is-an-email-preference-center}

An email preference center is a hosted page where users update email subscription status and choose message categories. Braze supports API-built and drag-and-drop preference centers.

### Should I use the Preference Center API or the drag-and-drop editor? {#should-i-use-the-preference-center-api-or-the-drag-and-drop-editor}

Use the [drag-and-drop preference center]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center) for faster setup with less code. Use the [API email preference center]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/api_preference_center) when you need full control over layout, hosting, and custom logic.