---
nav_title: Connected Content reference
article_title: Connected Content Reference
page_order: 4
layout: dev_guide
search_rank: 3
guide_top_header: "Connected Content"
guide_top_text: "Braze Connected Content expands on marketing personalization to boost customer engagement and conversions. This feature allows you to insert any information accessible via API directly into messages you send to users. Connected Content allows for pulling content either directly from your web server or from publicly accessible APIs. You can also use our Connected Content capabilities with our Technology Partners, like <b><a href='/docs/partners/data_augmentation/contextual_location/accuweather'>AccuWeather</a></b> and <b><a href='/docs/partners/channel_extensions/localization/transifex'>Transifex</a></b>.<br><br>In addition to the following articles listed, we recommend checking out our <b><a href='https://learning.braze.com/connected-content'>Connected Content</a></b> Braze Learning course."
description: "This landing page is home to all things Connected Content. Here, you can find articles on how to make API calls, local Connected Content variables, aborting content, and more."

guide_featured_title: "Section articles"
guide_featured_list:
- name: Make a Connected Content API call
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: Local Connected Content variables
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables
  image: /assets/img/braze_icons/server-01.svg
- name: Cache Connected Content responses
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses
  image: /assets/img/braze_icons/edit-05.svg
- name: Abort Connected Content
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content
  image: /assets/img/braze_icons/stop-circle.svg
- name: Pull user profile data
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/user_profile_fields_connected_content
  image: /assets/img/braze_icons/users-01.svg
- name: Connected Content retries
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Troubleshoot webhooks and Connected Content
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Use public APIs
  link: /docs/user_guide/messaging/design_and_edit/personalize/connected_content/public_apis
  image: /assets/img/braze_icons/target-05.svg
---

<br><br>

# Frequently asked questions

> Common questions about Connected Content behavior and troubleshooting.

## Why does Connected Content fail when my endpoint returns a redirect (301 or 302)?

Connected Content treats only **2xx** responses as successful. **3xx redirect responses are not followed** and are not treated as successful content retrieval. If your endpoint returns `301 Moved Permanently` or `302 Found`, Braze does not automatically follow the redirect to the final URL.

This can cause Connected Content to render blank, fail during message preview, or log errors such as HTTP status code 302 for an unsaved campaign. Postman and other clients often follow redirects automatically, so a URL can work in Postman but fail in Braze.

Configure your endpoint to return **200** with the response body at the URL Braze calls. If you use services that redirect (for example, some Google Apps Script URLs), use the final destination URL instead of the redirect URL.

For more information, see [Making an API call]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#things-to-know) and [Troubleshoot webhook and Connected Content requests]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content).

