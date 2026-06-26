---
nav_title: Optimizations
article_title: Optimize A/B Tests with Winning Variant or Personalized Variants
page_order: 1
page_type: reference
description: "Learn how to use Winning Variant or Personalized Variant when creating multivariate and A/B tests."
---

# Optimize A/B tests

> Learn how to use variant optimization when creating multivariate and A/B tests.


## Push
When [creating an A/B test]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) for push then there is one optimization option [BrazeAI™ Variant Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection/). It is a feature that enables your single send or recurring A/B tests to automatically run an experiment and optimize for the best engagement results.

## Email, Webhook, SMS, and WhatsApp

When [creating an A/B test]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/) for email, webhook, SMS, and WhatsApp campaigns scheduled to send once, you can select an optimization between two optimization options: **Winning Variant** and **Personalized Variant**.

![Optimization options listed in the A/B Testing section when choosing your target audience. Three options are listed: No Optimization, Winning Variant, and Personalized Variant. Personalized Variant is selected.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Both options work by sending an initial test to a percentage of your target segment. After the test ends, the remaining users in your audience are sent either the best performing variant (Winning Variant) or the variant they're most likely to engage with (Personalized Variant).

{% alert tip %}
Optimizations are located in the **Target Audiences** step of campaign creation, under **A/B Testing**.
{% endalert %}

## Winning Variant

Sending the Winning Variant is similar to a standard A/B test. Users in this group will receive the Winning Variant when the initial test is complete.

1. Select **Winning Variant**, then specify what percentage of your campaign audience should be assigned to the Winning Variant group.
2. Configure the following additional settings.

| Field | Description |
| --- | --- | 
| Determine Winning Variant | The metric to optimize for. Choose between *Unique Opens* or *Clicks* for email, *Opens* for push, or *Primary Conversion Rate* for all channels. Selecting *Opens* or *Clicks* to determine the winner does not affect what you choose for the campaign's [conversion events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/). <br><br>Keep in mind that if you're using a control group, users in the control group can't perform *Opens* or *Clicks*, so the performance of the control group is guaranteed to be `0`. As a result, the control group can't win the A/B test. However, you may still want to use a control group to track other metrics for users who do not receive a message. |
| Winning Variant Send Time | The date and time the winning variant is sent. |
| If No Winning Variant Can Be Determined | What happens if no variant wins by a statistically significant margin. Choose between sending the best performing variant anyway, or ending the test and not sending any further messages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Winning Variant" }

{% alert note %}
For Winning Variants and Personalized Variants, Braze runs an eligibility check again on the second send. Users who were not in the target segment (or otherwise not reachable) at the first send can enter later; users who left the segment may no longer receive the follow-up. Plan your segment and scheduling so the audience you intend to include is eligible at both sends.
{% endalert %}

## Personalized Variant

Use Personalized Variants to send each user in your target segment the variant they're most likely to engage with.

To determine the best variant for each user, Braze will send an initial test to a portion of your target audience to look for associations between user characteristics and message preferences. Based on how users respond to each variant in the initial test, these characteristics are used to determine which remaining users will get each variant. If no associations are found and no personalizations can be made, the Winning Variant is automatically sent to the remaining users. To learn more about how Personalized Variants are determined, refer to [Multivariate and A/B test analytics]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#personalized-variant).

1. Select **Personalized Variant**, then specify what percentage of your campaign audience should be assigned to the Personalized Variant group.
2. Configure the following additional settings.

| Field | Description |
| --- | --- | 
| Determine Personalized Variant | The metric to optimize for. Choose between *Unique Opens* or *Clicks* for email, *Opens* for push, or *Primary Conversion Rate* for all channels. Selecting *Opens* or *Clicks* to determine the winner does not affect what you choose for the campaign's [conversion events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/). <br><br>Keep in mind that if you're using a control group, users in the control group can't perform *Opens* or *Clicks*, so the performance of the control group is guaranteed to be `0`. As a result, the control group can't win the A/B test. However, you may still want to use a control group to track other metrics for users who do not receive a message. |
| Personalized Variant Send Time | The date and time the personalized variant is sent. |
| If No personalized Variant Can Be Determined | What happens if no Personalized Variants are found. Choose between sending the Winning Variant instead, or ending the test and not sending any further messages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalized Variant" }

## Analytics

To learn about the results of your A/B test with an optimization, refer to [Multivariate and A/B test analytics]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics/).
