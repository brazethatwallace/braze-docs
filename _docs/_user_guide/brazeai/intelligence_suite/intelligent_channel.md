---
nav_title: Channel filter
article_title: Intelligent Channel Filter
page_order: 1.5
description: "This article covers the Intelligent Channel filter, a filter that selects the portion of your audience for whom the selected messaging channel is their best channel. In this case, best means has the highest likelihood of engagement, given the user's history."
search_rank: 11
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Channel filter

> The `Intelligent Channel` filter (previously `Most Engaged`) selects the portion of your audience for whom the selected messaging channel is their "best" channel. 

## About the filter

![The Intelligent Channel filter with a dropdown for the different channels that can be selected.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

In this case, best means the channel that has the highest likelihood of engagement, given the user's history. You can select email, SMS, WhatsApp, web push, or mobile push (including any available mobile OS or device) as a channel.

The Intelligent Channel computes an engagement rate for each user on each supported channel, ranks those channels, and treats the highest-ranked channel as that user's best channel.

To enable the Intelligent Channel filter, select the **Intelligent Channel** filter on the **Target Audiences** page when creating a campaign or Canvas.

## How engagement is calculated by channel

Intelligent Channel compares channels using an engagement rate: the number of message interactions divided by the number of messages received. Braze evaluates up to the last 100 messages received per channel within the last six months.

Every time a message is sent to a user or a user interacts with a message, the engagement rate is recalculated within seconds. A user can only be counted as interacting with a message once (for example, an open and a click on the same email causes that message to be marked as having been engaged with only once, not twice).

### Interaction data by channel

Braze tracks the following events when calculating engagement rates:

- **Email:** Opens ([machine opens]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) excluded). Email clicks are not included.
- **Mobile push:** Direct opens. Each mobile platform (such as iOS, Android, and Kindle) is scored separately. Push influenced opens are not included.
- **Web push:** Opens
- **SMS:** Clicks on shortened links
- **WhatsApp:** Message reads or clicks on tracked links

Push influenced opens, email clicks, and session activity are not used for Intelligent Channel. Session activity is used by [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#about-intelligent-timing).

Intelligent Channel does not support webhooks, LINE, Kakao Talk, in-app messages, or Content Cards.

{% alert important %}
To compute the engagement rate of the SMS channel, turn on [SMS link shortening]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) with advanced tracking and click tracking. Without this tracking, SMS may be selected as the Intelligent Channel for a 0% engagement rate because of our [tie-breaking behavior]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#tie-breaking).
{% endalert %}

## Not enough data

For Braze to determine which channel is "best", there needs to be enough data. This means that a user must have received at least three or more messages on a channel before that channel can be ranked, and must have sufficient data on at least two supported channels.

If users haven't received enough messages across the channels, those users fall into the "Not Enough Data" option of this filter. This allows you to use any supported messaging channel to target these users.

For example, let's say you want users who prefer push messages to receive a push, and users who don't have enough data to receive the same push message. In that case, you could set the Intelligent Channel filter to **Mobile push** and use **OR** to add a second Intelligent Channel filter set to **Not Enough Data**. A separate campaign with the Intelligent Channel filter set to email could address users who prefer email.

![Intelligent Channel filters for mobile push or not enough data.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Campaigns and Canvas steps that ignore [frequency capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules) are not accounted for by Intelligent Channel and cannot contribute to the data requirements.
{% endalert %}

## Mobile push

Mobile push incorporates Android, iOS, Kindle, and other mobile device channels available on Braze. Braze scores each mobile platform separately when calculating engagement rates.

When you use the Intelligent Channel filter set to **Mobile push**, a user matches if either iOS push or Android push is their highest-ranked channel. This does not force the user to receive push notifications on a specific device. The ranking is only used to determine whether mobile push is that user's best channel compared with email, web push, SMS, and WhatsApp.

## Message Open Likelihood filter for individual channels {#individual-channels}

Rather than let Braze choose the single best channel for a user, you can use the ["Message Open Likelihood" segmentation filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) to filter users based on whether or not they're likely to open a message on a specific channel you choose. This filter is calculated by the percentage of interactions divided by the total messages received for the last 100 messages sent per channel.

Message Open Likelihood uses the same underlying engagement data as Intelligent Channel, but lets you set a threshold for a single channel instead of selecting the user's best channel. It is available for email, mobile push, SMS, and web push.

Note that a user must have received at least three messages on a specific channel before they can have a likelihood score for that channel. Users without sufficient data to measure a likelihood for a channel can be selected using "is blank."

## Best practices and effective use strategy

### Tie-breaking

Because some users receive a low number of messages, it's not unusual to have ties in engagement rates across available channels for a given user (for example, a single user may have a 20% engagement rate for both email and mobile push). In such cases, ties are broken by prioritizing (giving a higher ranking to) the channel with the most recent interaction events.

If tied channels both have a 0% engagement rate, Braze breaks the tie using the channel with the most recent received message instead.

### Unreachable channels

A user may have sufficient data for Braze to determine a channel ranking, but then become unreachable on their highest-ranked channel. For example, a user whose historical best channel is email may have recently unsubscribed from email. If you send a message on that channel, it won't be delivered to that user. Users who are unreachable on specific channels should be targeted or routed separately.

### Audience sizing

Intelligent Channel allows you to selectively target in advance the fraction of users who have a much higher likelihood of engaging with a message than the rest of your audience. This is not likely to represent a majority of users in a typical audience. Rather, you can expect this filter to find the 5-20% from your usual audience who have an established record of engaging on a particular channel.
