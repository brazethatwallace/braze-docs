---
nav_title: Quiet hours
article_title: Quiet hours
page_order: 4
page_type: reference
description: "This reference article covers what quiet hours are, how Braze handles messages during the quiet period, and how quiet hours interact with Intelligent Timing."
---

# Quiet hours

> Quiet hours prevent messages from being sent during a specified time window. You can use them to avoid contacting users at inconvenient times (like overnight or early in the morning) while still sending at an optimal time outside that window.

Quiet hours are configured at the campaign or Canvas level. You can also set [workspace quiet hours]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) as a default for a messaging channel across your workspace (early access).

## How quiet hours work

When quiet hours are enabled and a message would otherwise be sent during the restricted window, Braze holds the message and delivers it at the next available time after quiet hours end.

For example, if quiet hours run from 10 pm to 6 am and a message is scheduled for 5:30 am, Braze delivers it at 6 am instead.

{% alert note %}
Quiet hours apply in each user's local time zone.
{% endalert %}

## Quiet hours and Intelligent Timing

Quiet hours and Intelligent Timing operate independently. Enabling quiet hours does not require Intelligent Timing to be on, and the same is true in reverse. In general, we recommend choosing one or the other rather than using both together, unless there are policy, compliance, or other requirements that make quiet hours necessary alongside Intelligent Timing.

- **Without Intelligent Timing:** Quiet hours act as a no-send window for your scheduled send time. If the scheduled time falls within quiet hours, the message is held and sent when the window closes.
- **With Intelligent Timing:** Braze still calculates each user's optimal send time. If that time falls within quiet hours, the message is held and delivered at the nearest edge of the quiet window instead.

For more information on configuring quiet hours within an Intelligent Timing campaign, see [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing).

## Considerations

- **Messages send at the same time when quiet hours end.** If a large audience has messages held during quiet hours, all of those messages send at once when the window closes. For time-sensitive campaigns, consider how this affects delivery timing.
- **Quiet hours are not the same as aborting a message.** Aborting a message discards it entirely. Quiet hours hold the message and deliver it later.
- **Quiet hours do not re-evaluate segment membership for a held send.** Braze checks segment membership when the message is triggered. If the user is eligible then, Braze holds the message and sends it when quiet hours end. This is separate from [re-evaluating segment membership at send-time]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#audience-criteria-evaluation) or Canvas [delivery validations]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Quiet hours are separate from frequency capping and rate limiting.** Each of these delivery controls applies independently. A message that clears frequency and rate limits can still be held by quiet hours, and a message held by quiet hours is evaluated against rate limits when it eventually sends. For more information, refer to [Rate limiting and frequency capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

## Related articles

- [Workspace quiet hours]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours)