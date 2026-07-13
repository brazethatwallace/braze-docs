---
article_title: Message Prioritization
permalink: /message_prioritization/
toc_headers: h2
description: "This reference article describes top-level Message Prioritization and how to configure this for your workspace."
---

# Message Prioritization

> Use Message Prioritization to make sure your users receive the campaigns that matter most.

{% alert important %}
Message Prioritization is currently in beta. Contact your Braze account manager if you're interested in participating in this beta.<br><br>This article reflects the version of Message Prioritization planned for production release in late July 2026. Some behavior described here may not yet be available in all beta workspaces.
{% endalert %}

Only administrators can configure top-level Message Prioritization settings. Limited users may view each page in this section, but may not make changes.

For top-level Message Prioritization settings, go to **Settings** > **Message Prioritization**.

## How it works

Use Message Prioritization to create [categories](#categories) and [prioritization rules](#prioritization-rules) to rank how your messages are sent.

A beauty brand managing email promotions for paid partnerships and loyalty programs uses Message Prioritization to create two categories named "Paid Partnerships" and "Loyalty". The brand ranks these categories based on which is more business critical to the brand. During the holiday season, the brand ranks "Loyalty" higher than "Paid Partnerships" to prioritize customers who have been part of the membership program for over a year.

![An example of prioritization rules for two categories: Paid Partnerships and Loyalty.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

At send time, Braze compares the message being sent against other messages the user may receive that are opted into prioritization, have a priority category set, and count toward the same frequency capping rule within the same frequency capping window. If sending the current message would prevent a higher-priority message from sending later, Braze deprioritizes the lower-priority message. Depending on the configured retry window, that lower-priority message is either retried later or not sent.

Message Prioritization can evaluate:

- Scheduled campaigns
- Action-based campaigns
- Canvases

Braze uses its prediction of when each message is expected to send when evaluating whether sending one message now could prevent a higher-priority message from sending later. For more information on how Braze predicts future send timing for campaigns and Canvases, see [How does Braze predict when a future message sends?](#how-does-braze-predict-when-a-future-message-sends)

### Supported message types

Message Prioritization supports the same channels as frequency capping:

- Push notifications
- Email
- SMS
- Webhooks
- WhatsApp
- LINE

For prioritization and frequency capping, iOS push, Android push, web push, and other push notification platforms are treated as one shared push channel, not as separate channels.

## Categories

Prioritization rules are based on a ranking of categories, which is a label you can assign to a given campaign or Canvas (similar to a [tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). You can create up to 20 categories at a given time.

To add a new category:

1. Go to **Settings** > **Message Prioritization** > **Categories**.
2. Select **Create new category**.

![The "Create new category" button in the Message Prioritization section.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Give the category a name and an optional description.
4. Select **Create category**.

![An example category named "P3" with the description "This is my third highest priority category."]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

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

To reorder rules, select and drag the <i class="fa-solid fa-grip-vertical"></i> icon on a rule. To delete a rule, select the <i class="fas fa-ellipsis-vertical"></i> menu and then **Delete Rule**.

Be sure to select **Save** for your updates to apply.

## Campaign-level settings

### Opt-in

To opt a campaign into prioritization, select the **Opt-in to Message Prioritization** checkbox in the campaign's delivery settings.

![The checkbox for "Opt-in to Message Prioritization".]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Next, assign the campaign to a category by selecting one from the **Category** dropdown.

![The Message Prioritization category dropdown in a campaign's delivery settings.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

Message Prioritization supports scheduled campaigns and action-based campaigns.

### Intelligent Timing

For campaigns that use Intelligent Timing, Message Prioritization compares messages using the send time Braze selects for each user instead of only the original campaign schedule. This lets Braze account for the message that is most likely to be sent to that user first.

For recurring Intelligent Timing campaigns, Braze can use the known send time selected for the current recurrence when comparing that campaign against other eligible prioritized messages.

### Retry window

A retry window lets opted-in messages retry for up to three days if the first attempt is not high enough priority to send. On each subsequent day, at the same time the message was originally scheduled or triggered to send, the message is attempted again. After the last day in the retry window, if the message still is not sent, it is not retried further and is permanently deprioritized.

For recurring scheduled campaigns, the retry window must be shorter than the minimum time between sends for that campaign. Retries always happen one day at a time from the original send time, even if the campaign is not normally scheduled to send on that day. For example, if you have a campaign that sends every Monday and Wednesday, the retry attempt occurs on Tuesday, so the retry window must be set to one day. If you have a campaign that sends every Monday, Wednesday, and Friday, and the Friday send is retried with a one-day retry window, the retry attempt occurs on Saturday, not Monday.

![The "Retry Window" setting set to 1 day.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

For action-based campaigns, retries are based on the time the triggered message was originally expected to send.

Action-based campaigns that use exception events do not support retry windows.

Retry windows for Canvas messages are configured at the step level. For supported Canvas messaging steps, if a Canvas message step is deprioritized and has a retry window configured, Braze can retry that step later within its retry window.

## Canvas-level settings

To opt a Canvas into Message Prioritization, enable Message Prioritization in the Canvas settings and assign the Canvas to a category.

When a user is eligible for multiple prioritized messages, Braze evaluates opted-in campaigns and eligible Canvas message steps together on supported channels.

For campaigns, this includes eligible scheduled and action-based sends.

For Canvases, this includes:

- Future scheduled Canvases that the user is eligible to enter
- Canvases that the user is currently in

Canvas prioritization is not all-or-nothing. A higher-priority campaign can cause one Canvas step to be deprioritized while later eligible steps in that same Canvas can still send, depending on category ranking, send timing, and frequency capping rules.

### How Braze evaluates future messages

Braze evaluates campaigns and Canvases differently based on message type.

#### Campaigns

Braze compares each eligible campaign message using the time that message is expected to send.

#### Canvases

Braze traverses the Canvas to determine which future messages a user may receive, starting from:

- Canvas entry, for future scheduled Canvases
- The user's current step, if the user is already in the Canvas

Braze then evaluates Canvas steps in the following ways.

##### Messaging steps

These steps are counted toward prioritization and added to the set of eligible messages when they send on a supported channel.

- Message step
- Content Optimizer step

##### Continuation steps 
 
These steps are ignored for prioritization and do not affect look-ahead.

- Context Update step
- User Update step
- Audience Sync step
- Feature Flag step
- Delay step with a fixed delay

##### Boundary steps

Braze stops look-ahead at these steps until the user actually progresses through them in the Canvas.

- Delay step with a personalized delay
- Delay step that follows a branching step
- Action Path step
- Experiment step

##### Branching steps 
 
These steps split the Canvas into multiple possible paths.

- Decision Split step
- Audience Path step

When a prioritization path contains branching steps, Braze assumes all paths are viable and considers all parallel message steps on supported channels for prioritization. Because frequency capping rules can be channel-specific, parallel message steps are de-duplicated by channel when needed.

For example, if one branch can send email and another branch can also send email, Braze treats those as a single possible email send for forward-looking prioritization. If another branch can send push, Braze also considers that possible push send separately.

For Canvas message steps that use Intelligent Timing, Braze predicts timing best-effort until the user actually reaches that step. Once the user enters the Intelligent Timing step and Braze calculates the per-user send time, Message Prioritization uses that calculated send time for the current step. On deterministic paths, Braze also reflects that updated timing in following message steps when determining their expected send times.

Content Optimizer steps are treated like messaging steps because they always send on a specified channel. However, retry windows do not apply to Content Optimizer steps because retrying would interfere with the experiment. Other supported Canvas messaging steps can use retry windows. Canvas steps on unsupported channels do not participate in Message Prioritization.

## Frequency caps

Message Prioritization works within your existing frequency capping rules. A prioritized message can send only if:

1. The relevant frequency capping rule has not been reached yet for that user, and
2. Sending that message would not cause the user to hit a cap before a later, higher-priority message can send.

Messages that are not subject to frequency capping are not eligible for Message Prioritization. If you want a message to always send, opt it out of frequency capping. This also removes it from Message Prioritization.

### For supported campaigns and Canvas steps

To be eligible for Message Prioritization, the campaign or Canvas step must use a supported channel and be evaluated within your frequency capping configuration.

![An example of a frequency capping rule.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Frequency capping rules

Braze optimizes priority within your existing frequency capping rules. Prioritized messages are compared only when they share the same applicable frequency capping rule.

For example, two email campaigns that count toward the same email frequency capping rule can be prioritized against each other. A lower-priority email campaign is not deprioritized in favor of a higher-priority SMS message unless both messages count toward the same frequency capping rule.

You can use channel-specific frequency capping rules, category-specific rules, tag filters, or rules that apply to any channel. Message Prioritization works with whichever rules apply to your opted-in messages.

You can create frequency capping rules by category to manage how many messages a user receives from a given category. This helps prevent a high-priority category from sending too many messages. Select **Message prioritization category** under **Additional filters**, and select a category from the dropdown.

![An example of the frequency capping rule with the "Category" field dropdown to select P2 or P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Messages outside of Message Prioritization share frequency cap limits with prioritized messages, so even a high-priority message can be aborted due to a message outside of Message Prioritization.

## Examples

### Higher-priority campaign versus lower-priority campaign

Suppose a user is eligible for two email campaigns on the same day, and both campaigns count toward the same frequency capping rule. If the higher-priority campaign is expected to send later that day, Braze can deprioritize the lower-priority campaign so the higher-priority campaign can send instead. If the lower-priority campaign has a retry window, Braze can try it again later.

### Higher-priority action-based campaign versus lower-priority message

Suppose a user triggers a higher-priority action-based campaign that is set to send two hours later. During that delay, Braze can consider that upcoming action-based campaign when deciding whether another prioritized message should send first. This helps prevent a lower-priority message from sending now if the higher-priority action-based campaign is expected to send soon.

### Higher-priority Canvas versus lower-priority campaign

Suppose a user is eligible for a lower-priority campaign, but is also expected to receive a higher-priority Canvas message later that day. If Braze can already evaluate that future Canvas message, it can deprioritize the lower-priority campaign so the higher-priority Canvas message can send instead.

### Higher-priority Canvas with a boundary step versus lower-priority campaign

Suppose a higher-priority Canvas includes an Action Path Step, an experiment, or a personalized delay before its next message step. Until the user reaches and moves past that step, Braze does not look ahead to the downstream higher-priority Canvas message. In that case, a lower-priority campaign may still send first.

### Higher-priority branching Canvas versus lower-priority message

Suppose a higher-priority Canvas can send different messages depending on which branch a user follows. Braze evaluates those possible future paths conservatively when comparing messages. This helps prevent a lower-priority message from sending now if a higher-priority Canvas branch could use that same frequency cap later.

### Canvas Intelligent Timing step and downstream steps

Suppose a user enters a higher-priority Canvas message step that uses Intelligent Timing. Once Braze calculates that user's send time for the Intelligent Timing step, Message Prioritization uses that per-user send time for the current step and for later message steps on the same deterministic path. This helps Braze compare downstream Canvas messages against other prioritized sends using the updated timing instead of only the earlier path estimate.

## Limitations

Message Prioritization has the following limitations:

- Up to 20 categories per workspace
- Up to 10 prioritization rules per workspace
- Up to 25 active opted-in prioritized scheduled items at a time
- Up to 25 active opted-in prioritized action-based items at a time
- Retry windows of up to 3 days

The scheduled-item limit is a combined total across scheduled campaigns and scheduled opted-in Canvases. The action-based-item limit is a combined total across action-based campaigns and action-based opted-in Canvases.

## Frequently asked questions

### How are ties broken between messages in the same category?

When prioritizing two campaigns in the same category against each other, Braze gives higher priority to the one with the earlier send time. If a retry window is configured, Braze uses the end of that retry window when comparing campaigns within the same priority rule. For recurring campaigns, the send time is calculated as the next occurrence as of midnight in company time. For campaigns scheduled in local time, Braze assumes a send time in company time.

For Canvases in the same category, Braze uses Canvas entry timing as the tiebreaker so that all steps in the same Canvas preserve the same relative priority against other campaigns and Canvases.

### How can I make sure a message is always sent?

There may be some scenarios where you want a message to always be sent, like in the case of transactional or legal notifications. In this case, you should opt the message out of frequency capping, which also makes it ineligible for Message Prioritization. This sends the message whenever it is scheduled or triggered without consideration for what else is sending.

### When are messages actually prioritized? Is there a schedule?

Each message is prioritized based on when it is expected to send. There is no universal evaluation time for prioritized messages.

### How does Braze predict when a future message sends?

Braze predicts future send timing differently for each message type:

- **Scheduled campaigns:** Braze uses the time each campaign is expected to send. For scheduled campaigns that use Intelligent Timing, Braze uses each user's optimal send time for that campaign occurrence.
- **Action-based campaigns:** Braze uses the time each triggered message is expected to send, including any configured delay between trigger and send.
- **Canvas steps:** Braze uses the user's Canvas entry or current Canvas position, plus the timing of downstream steps. For Canvas message steps that use Intelligent Timing, once a user enters that step, Braze uses the per-user send time it calculates for that user. For following message steps on the same deterministic prioritization path, Braze uses that Intelligent Timing send time when determining later expected send timing. Before a user reaches the Intelligent Timing step, prediction remains best-effort.

### My message was scheduled to send already, but it hasn't yet because of rate limiting or other delays. What does this mean for prioritizing other campaigns?

Braze assumes your message was sent at the originally scheduled time if it is still processing, which determines whether to send other upcoming prioritized messages. When that message does ultimately send, Braze uses the actual send time.

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

### How do boundary steps affect Canvas prioritization?

Boundary steps stop look-ahead through the Canvas until the user actually reaches or completes that point in the Canvas. For example, if a higher-priority message sits after an Action Path Step, personalized delay, or experiment step, Braze does not use that downstream message to block a lower-priority campaign until the user has moved past that boundary.

### How does branching work in Canvas prioritization?

When a Canvas contains branching paths, Braze assumes each path is viable and compares the highest possible future send volume by channel. This helps avoid sending a lower-priority message now if a higher-priority Canvas path could consume that same frequency cap later.

### What happens if a user has multiple paths through a prioritized Canvas at the same time?

Braze treats each viable path as a possible future path and evaluates the eligible message steps on those paths independently. When multiple paths can send on the same channel, Braze de-duplicates those possible sends by channel when needed.

### How does Intelligent Timing work in Canvas prioritization?

Before a user reaches an Intelligent Timing Canvas message step, Braze predicts that step's timing best-effort. Once the user enters the step and Braze calculates the per-user send time, Message Prioritization uses that calculated send time for the current step and for following message steps on the same deterministic prioritization path.

### Is there any reporting or analytics functionality specific to Message Prioritization?

Braze provides Message Prioritization-related events in Currents and data sharing for supported channels, including email, LINE, push notifications, SMS, webhooks, and WhatsApp. These include deprioritized and frequency-capped events, logged to the `users.messages.<channel>.abort` table, as well as retry events that show when a message was later retried within the configured retry window, logged to the `user_messages_<channel>_retry` table.

For campaigns, you can also use the Messaging Diagnostics dashboard, the existing deprioritized and retried daily stats, and existing [Braze reporting functionality]({{site.baseurl}}/user_guide/analytics/reporting) to monitor the health and performance of your prioritized campaigns and Canvases.
