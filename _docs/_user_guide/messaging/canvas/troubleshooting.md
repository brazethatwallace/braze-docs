---
nav_title: Troubleshooting
article_title: Troubleshoot Canvases
page_order: 7
page_type: reference
description: "This page provides troubleshooting steps for Canvases."
tool: Canvas
---

# Troubleshoot Canvases

> This page helps you troubleshoot issues with your Canvases.

## "Too many Canvas branches" error

If you see a "Too many Canvas branches" error when launching a scheduled Canvas, the combination of step branching and entry audience size may create Braze cluster performance issues that prevent messages from sending.

Braze shows this message when you launch a Canvas with a scheduled entry—not when you save a draft. To resolve it, try the following:

- Reduce step branching in the Canvas.
- Reduce the entry audience size.
- Use [Audience Paths]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) to consolidate branching instead of many parallel paths.
- If your Canvas uses the original editor, [clone it to Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/) and rebuild with Canvas components.

If you still need to launch the Canvas without changes and can't move to Canvas Flow, contact [Support]({{site.baseurl}}/support_contact/).

## Why did a user not receive a triggered Canvas step?

First, confirm that the custom event is being passed to Braze. Go to **Analytics** > **Custom Events Report**, and then select the respective custom event and date range. If the event doesn't display, confirm that it's set up correctly and that the user performed the correct action.

If the custom event displays, further troubleshoot by doing the following:

- Check the user's profile download to confirm they triggered the event and when they did it. If the event was triggered, compare the timestamp for when the event was triggered to the time the Canvas went live. The event may have been triggered before the Canvas went live.
- Review changelogs for the Canvas and any segments used in targeting to determine if the user was in the segment when their custom event was triggered. If they weren't in the segment, they wouldn't have received the Canvas step.
- Verify whether the user was assigned to the Canvas control group at entry and consequently prevented from receiving the Canvas step.
- If there is a scheduled delay, check if the user's custom event was triggered before the delay. If the event was triggered before the delay, they wouldn't have received the Canvas step.

{% alert note %}
In-app messages can only be triggered by events sent through the SDK, not the REST API.
{% endalert %}

## Why isn't my Canvas sending as expected?

Canvases are robust and complex, and we know you dedicate time and care when creating them. So, if you find that your Canvas isn't sending the way you want it to, we recommend checking your Canvas schedule, entry audience, and entry settings, and reviewing the steps for [creating a Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

### Schedule

- Is the Canvas [scheduled correctly]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)?
- Have you selected the correct date and time?
- For [action-based delivery]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), have users performed the specified actions since you launched the Canvas?

### Entry settings

The [entry settings]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=basics#selecting-entry-controls) are important for understanding how your Canvases are sending. Check if you have limited the number of people who can potentially enter the Canvas.

Users can also exit a Canvas if they're no longer eligible to receive messages. For example, if the Canvas only contains push notifications, and a user opts out of push after receiving the first step, then that user would drop out of the Canvas. Consider using [different Canvas steps]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) to add alternative user journeys.

### Segmenting your audience

Consider the following questions for your target audience:

- Have you selected the correct segment?
- How is the segment set up?
- Have you confirmed that the segment contains any users?
- Have you added any additional filters that would limit the number of users entering the Canvas?
- Do the users qualify to receive the first step of your variants? For example, if the first step of your Canvas is a push notification, but the entry audience is all push-disabled, then no users receive messages.

## Why are sends or deliveries lower than my target audience size?

The number of messages sent or delivered often differs from the estimated audience or recipient count. Common reasons include:

- **Audience re-evaluation:** Users can fall out of the segment between when they enter a step and when the message is sent.
- **Channel eligibility:** Users may be missing email addresses, push tokens, or the subscription status required for that channel in that step.
- **Control groups:** A global or Canvas control group can withhold users from messaging.
- **Quiet Hours, Intelligent Timing, and rate limits:** These settings can defer or suppress sends.
- **In-app message steps:** In-app messages may show zero _Sends_ while impressions exist. This is expected because in-app delivery works differently from push notifications or email. See [Why may a Canvas show zero Sends even though impressions are logged?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged) in the Canvas FAQ.

For email and other channels, many of the same factors apply as for campaigns. For a detailed list, see [Why are sends lower than the estimated audience size?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size).

## Why did no users enter my daily scheduled Canvas on Daylight Saving Time day?

On Daylight Saving Time (DST) transition days, daily scheduled Canvases can run up to one hour earlier or later than usual. If your entry criteria relies on custom attributes or events with timestamps that fall within one hour of the scheduled entry time, users may not yet qualify on DST day because the attribute or event hasn't been logged.

For example, suppose users typically receive a custom attribute update at 3:00 p.m. in your Canvas's time zone and your Canvas runs daily at 3:30 p.m. in that same time zone. On a spring-forward DST day, the Canvas may evaluate users up to one hour earlier than usual relative to that attribute update—before the attribute has been logged. If re-eligibility is turned off, users who entered on previous days can't re-enter, resulting in zero entries for that day.

To avoid this, ensure your custom attribute or event updates occur more than one hour before the Canvas's scheduled entry time.

## Why didn't my audience split evenly between the control group and variant group?

When creating your Canvas, you may have expected your audience to split evenly between your control group and your variant group, like in the following [use case](#use-case). Let's discuss why that is and how to fix it!

Control group and variant assignment happens at Canvas entry based on the percentages you set in the builder—not through segment filters. A user enters a Canvas when they fit all of your criteria defined in the [Entry Step]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule).

If users enter the variant but don't receive messages because they aren't eligible for a channel, use [Send Settings]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-14-select-your-send-settings) on each step (for example, **Subscription Settings** set to opted-in users only) instead of adding channel filters to **Target Audience**. For multi-channel Canvases, don't limit the entry audience to a single channel (such as **Foreground Push Enabled**).

Users who can't receive a specific channel may still enter a variant. To limit who receives each message type, use per-step send settings instead of entry audience filters.

### Use case

Let's imagine the following scenario:
- A Canvas has a single variant and a control group.
- The first step of the variant is a push notification.
- 90% of users were selected to enter the variant, and 10% to enter the control group.

![Canvas example with 90% variant and 10% control group.]({% image_buster /assets/img_archive/trouble15.png %})

In this scenario, 90% of the users who enter the Canvas enter the variant. 

If we look back to the active users, we can see that even though it contains 29.8k users, only 64% of them push enabled:

![Segment with the "Push Enabled" filter set to "true", and estimated users of 29.8k.]({% image_buster /assets/img_archive/trouble16.png %})

This means that even though we specified 90% of users to enter the variant, not all of those users are actually able to receive a push notification. These users who are unable to receive a push notification still enter the variant regardless.

## Action-based steps and custom event properties

If an action-based Canvas or Action Path does not send when you expect, confirm that the custom event in the user profile matches the trigger configuration, including property filters. Braze evaluates the exact properties sent with the event; if a property is missing or the value does not match the filter, the user does not advance.

Events that occur too early or before the user qualifies for the audience do not trigger the step, so check the timestamp of the event relative to Canvas launch, [entry schedule]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types), and any scheduled delay before the step.

{% alert note %}
In-app messages in Canvas can only be triggered by events from the SDK, not the REST API. See [Why did a user not receive a triggered Canvas step?](#why-did-a-user-not-receive-a-triggered-canvas-step)
{% endalert %}

## Why is the Canvas editor freezing or not loading?

If you're making edits to large or complex Canvases with many branches or variants, lots of steps, or very wide flows, the editor may fail to load or freeze. In this case, we recommend the following:

- Clear browser cache and cookies, then reload the page. If you use any company ad blockers or browser extensions, this may interfere with the Braze platform.
- Use Canvas zoom controls to reduce the view to 25% or 10%. This reduces the amount of UI the browser must render at once.
- Try a different web browser.
