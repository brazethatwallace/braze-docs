---
article_title: Message Prioritization
permalink: /message_prioritization/
toc_headers: h2
description: "This reference article describes top-level Message Prioritization and how to configure this for your workspace."
---

# Message Prioritization

> Use Message Prioritization to make sure your users receive the campaigns that matter most.

{% alert important %}
Message Prioritization is currently in beta. Contact your Braze account manager if you're interested in participating in this beta.
{% endalert %}

Only administrators can configure top-level Message Prioritization settings. Limited users may view each page in this section, but may not make changes.

For top-level Message Prioritization settings, go to **Settings** > **Message Prioritization**.

## How it works

Message Prioritization allows you to create [categories](#categories) and [prioritization rules](#prioritization-rules) to rank how your messages are sent. 

Let's say you're managing email promotions for paid partnerships and loyalty programs for a beauty brand. With Message Prioritization, you could create two categories named "Paid Partnerships" and "Loyalty". You could then rank these categories based on which is more business critical to your brand. For example, during the holiday season, you could rank "Loyalty" higher than "Paid Partnerships" to prioritize your brand's customers who have been part of your membership program for over a year.

![An example of prioritization rules for two categories: Paid Partnerships and Loyalty.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

## Categories

Prioritization rules are based on a ranking of categories, which is a label you can assign to a given campaign (similar to a [tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). You can create up to 20 categories at a given time.

To add a new category:

1. Go to **Settings** > **Message Prioritization** > **Categories**.
2. Select **Create new category**.

![The "Create new category" button in the Message Prioritization section.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Give the category a name and an optional description.
4. Select **Create category**.

![An example category named "P3" with the description "This will become my third highest priority category."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

To edit or delete a category, select the <i class="fas fa-ellipsis-vertical"></i> menu.

## Prioritization rules

After your categories are set up, you can rank them in a set of prioritization rules. Rules are ranked in descending order of priority. You can create up to 10 prioritization rules at a given time.

1. Go to **Settings** > **Message Prioritization** > **Prioritization Rules** to configure your rules. 

!["Prioritization Rules" section with no priorities set yet.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Select **Add rule**. 
3. Select a category from the dropdown. 

!["Priority 1" prioritization rule with P1 selected as the category.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Continue to add rules by selecting **+ Add rule** under your last rule.

To reorder rules, select and drag the <i class="fa-solid fa-grip-vertical"></i> icon at the start of a rule. To delete a rule, select the <i class="fas fa-ellipsis-vertical"></i> menu and then **Delete Rule**. 

Be sure to select **Save** for your updates to apply.

## Campaign-level settings

### Opt-in

{% alert important %}
Only scheduled, single-channel campaigns can be opted into prioritization at this time. Action-based and API-triggered campaigns and Canvases are not supported.
{% endalert %}

To opt a campaign into prioritization, select the **Opt-in to Message Prioritization** checkbox in the campaign's **Schedule Delivery** page. 

![The checkbox for "Opt-in to Message Prioritization".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})
 
Next, assign the campaign to a category by selecting one from the **Category** dropdown.

![The checkbox for "Opt-in to Message Prioritization".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

You can opt in up to 25 active campaigns at a given time. Draft, stopped, or archived campaigns do not count toward this limit.

### Retry window

A retry window lets opted-in campaigns retry for up to three days if the first attempt is not high enough priority to send. On each subsequent day, at the same time the message was originally scheduled, the message is attempted to send again. After the last day in the retry window, if the message still isn't sent, it is not retried further and is permanently deprioritized.

The retry window must be shorter than the time between sends for that campaign. If you have a campaign sends every Monday and Wednesday, the retry attempt occurs on Tuesday. This means the retry window must be set to one day.

![The "Retry Window" setting set to 1 day.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

## Frequency caps

### For campaigns

To be eligible for Message Prioritization, a campaign must be opted into frequency capping. You can confirm the campaign is opted in within the **Delivery Controls** section of the **Schedule Delivery** page. 

![An example of the frequency capping rule for any applicable channel and no additional filters.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Frequency capping rules

We'll optimize priority within your existing frequency capping rules. While not required, we highly recommend you set at least one frequency capping rule that captures all messages regardless of channel, tag, or category. This frequency capping rule will capture every message opted into Message Prioritization so that prioritized messages are compared to each other–not just other messages that share the same characteristics.

To set this up, go to **Settings** > **Frequency Capping Rules**. Create a rule where the channel is **Any applicable channel**, and additional filters are **None**.

![An example of the frequency capping rule for any applicable channel and no additional filters.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization11.png %})

You can also create frequency capping rules by category. This allows you to manage your marketing messages to avoid sending too many messages from a given category just because it's marked as high priority. Select **Message prioritization category** under **Additional filters**, and select a category from the dropdown.

![An example of the frequency capping rule with the "Category" field dropdown to select P2 or P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Messages outside of the Message Prioritization will share frequency cap limits with prioritized messages, so even a high-priority message can be aborted due to a message outside of the Message Prioritization.

## Frequently asked questions

### How are ties broken between messages in the same category?

When prioritizing two messages in the same category against each other, we will give higher priority to the message with the earliest send time. For recurring campaigns, the send time is calculated as the next occurrence as of midnight today in company time. For campaigns scheduled in local time, we’ll assume a send time in company time.

### What is the relationship between Message Prioritization and frequency capping?

At send time, we will compare the message being sent with other messages that the user is eligible to receive, which follow the same frequency capping rule and are opted into message prioritization. The message will be sent if:

1. The relevant frequency capping rule has not been reached yet for that user, and
2. Sending this message to this user would not cause a cap to be reached before a subsequent, higher-priority message is sent.

### How can I make sure a message is always sent?

There may be some scenarios where you want a message to always be sent, like in the case of transactional or legal notifications. In this case, you should opt the message out of frequency capping (which also makes it ineligible for Message Prioritization). This will send the message whenever it's scheduled or triggered without consideration for what else is sending.

### When are messages actually prioritized? Is there a schedule?

Each message is prioritized at its own scheduled send time. There is no universal evaluation time for prioritized messages. 

### My message was scheduled to send already, but it hasn't yet because of rate limiting or other delays. What does this mean for prioritizing other campaigns?

We will assume your message was sent at the originally scheduled time if it is still processing. We will use that assumption to determine whether to send other upcoming prioritized messages. When that message does ultimately send, we will use the actual send time.

### My message was prioritized but aborted last-minute. What does that mean for prioritization?

When a message is prioritized, Braze will assume it was sent at its originally scheduled time. In general for Message Prioritization, we don't recommend using Liquid aborts. If a message is aborted due to [`abort_message` Liquid logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), we'll assume it was sent to that user and will prioritize future campaigns accordingly.

Let's say you have two messages: Message 1 and Message 2. If Message 1 is aborted in favor of a future higher-priority Message 2, this doesn't guarantee that Message 2 will actually send. Message 2 can still abort for any reason, including:

- Liquid abort messages
- The user no longer being in the segment
- Frequency caps because of a message outside of the prioritization rules.

If Message 2 aborts, there will not be another attempt to send Message 1.

Note that a user could receive a lower-priority message, but not a higher-priority message for the same frequency capping rule for the following reasons:

- The higher-priority message was frequency capped by a different rule.
- The higher-priority message conflicted with another, future campaign of even higher priority for a different rule.
- At the time of the lower-priority message send, the user was not in the audience for the higher-priority message.
- Both messages should have been able to send, but a message outside of the prioritization setup sent before the higher-priority message could send.

### Can I opt Canvases into Message Prioritization?

No. At this time, you cannot opt Canvases into Message Prioritization.

### What about action-based or API-triggered campaigns?

At this time, Message Prioritization is not supported for action-based or API-triggered campaigns.

### Is there any reporting or analytics functionality specific to Message Prioritization?

At this time, there is no reporting or analytics functionality specific to this feature. We encourage you to use existing [Braze reporting functionality]({{site.baseurl}}/user_guide/analytics/reporting) to monitor the health and performance of your prioritized campaigns. 
