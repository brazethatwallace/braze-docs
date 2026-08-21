---
nav_title: Retarget users
article_title: Retarget users
description: "Learn how to retarget users who've submitted a form through a landing page."
page_order: 3
---

# Retarget users through a landing page

> Learn how to retarget users who've submitted a form through a landing page by creating a dedicated segment or triggering a message when the form is submitted.

## Prerequisites

Before you start, create a [landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Retargeting users

Braze automatically tracks when a user submits a landing page form. You can view the total number of submissions for a form under [landing page analytics]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics). For user-specific retargeting, retarget users through your landing page form using one of the following methods:

{% tabs local %}
{% tab Using a segment %}

Create a new segment to automatically identify users who have or haven't submitted a landing page form. When you [create a segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), under "Retargeting" group, choose **Submitted Form on Landing Page**.

![Segment creation with the Filter Group selected as "Submitted Form on Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

From here, you can segment users based on whether they have or haven't submitted a landing page form for your landing page.
{% endtab %}

{% tab Using a message trigger %}

Set up a message trigger to automatically message users or enter them into a Canvas after they submit the form. When you choose your delivery option for your [campaign]({{site.baseurl}}/user_guide/messaging/campaigns) or [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), select **Action Based Delivery**, then **Submitted a Landing Page form**.

All users who submit a form through this landing page form are either messaged through the chosen messaging channel or entered into the chosen Canvas.

![Landing page trigger action in messaging.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
The action-based delivery option for landing pages isn't available for in-app messages. To target users who have submitted a form on a landing page with an in-app message, select the **Submitted Form on Landing Page** filter in the **Targeting Options** of your campaign.
{% endalert %}

{% endtab %}
{% endtabs %}

### Multi-step form

For a [multi-step form]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms), both retargeting methods rely on the **Submitted a Landing Page form** event, which only logs after a user completes every step. A user who submits some but not all steps is saved to their profile but isn't included in either method until they complete the entire form. For more information, see [Track data from partially completed forms]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms#track-data-from-partially-completed-forms).