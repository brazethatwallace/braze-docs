---
nav_title: FAQ
article_title: Rate limiting and frequency capping FAQ
page_order: 0
page_type: FAQ
description: "This article provides answers to some frequently asked questions about rate limiting and frequency capping."
tool: Campaigns

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about rate limiting and frequency capping.

### If I change a send throttle on an active Canvas, does it affect users already in the Canvas?

Yes, when you increase or decrease a Canvas rate limit, the updated limit will take effect for new messages within approximately 30 seconds of the change due to caching.

### What happens if a user reaches a Canvas Message step but is over the global frequency cap?

The user won't receive that send for the capped channel, but they still follow your Message step advancement rules. Message steps advance users when a message isn't sent because of global frequency capping, so they continue to the next Canvas step. For the full list of advancement cases, see [How users advance]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#how-users-advance).

### How can I identify users who were frequency capped in a Canvas?

Users who are frequency capped don't generate a send event for that step. To identify these users, you can use [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) to track message aborted events where `abort_type` is `frequency_capped`. Alternatively, you can create a [Segment Extension]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) to analyze users who entered the Canvas but didn't receive the expected message.

### How are calendar days and time zones used for "per day" global frequency caps?

Global frequency capping uses the user's time zone and counts by calendar day, not rolling 24-hour periods. For an example, see [Delivery rules]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules).

### Does global frequency capping apply to triggered in-app messages?

No, global frequency capping only applies to push, email, SMS, webhook, WhatsApp, and LINE messages.

### Does frequency capping limit campaigns received or individual messages inside a send?

Frequency capping applies per dispatch, meaning each time Braze sends a campaign or Canvas step to a user counts toward your caps—not each message variant or platform inside that send.

For example, if users can receive only two push campaigns per week and you run a push campaign scheduled to send daily, each day's send counts toward the push cap. After two daily sends from that campaign, the user is capped for push for the rest of the week unless another campaign ignores frequency capping rules.

When a single dispatch uses multiple channels, that dispatch counts at most once per frequency capping rule that applies. For example, let's say a campaign sends email, iOS push, and Android push in one delivery, and your workspace has rules for push, email, and a channel-agnostic limit. Each recurrence of that campaign counts once toward the push rule, once toward the email rule, and once toward the channel-agnostic rule. It does not count once per push platform or per message inside the send. For more on multichannel campaigns, see [Delivery rules]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-rules).

### If several messages are eligible at the same time and only some fit under the cap, which messages send?

Braze sends up to the limit. When multiple sends compete in the same window, the messages that are processed first are the ones that count toward the cap. Remaining sends in that window are capped.

### Do failed webhooks count toward the global frequency cap?

No. A webhook counts toward the cap when Braze records a successful delivery. Unsuccessful webhook responses (for example, `4xx` or `5xx` status codes) don't count toward the cap.