---
nav_title: Scheduled delivery
article_title: Scheduled Delivery
page_order: 0
page_type: reference
description: "This reference article describes the differences between the time-based scheduling options for campaign delivery."
tool: Campaigns

---

# Scheduled delivery

> Campaigns sent using time-based scheduled delivery are delivered on specified days.

## Option 1: Send as soon as the campaign is launched

If you choose to send a message as soon as it's launched, your message will begin sending as soon as you finish creating your campaign.

![The "Delivery" section with "Scheduled" selected and the time-based scheduling option of sending as soon as the campaign is launched.]({% image_buster /assets/img_archive/schedule_immediately.png %})

This type of schedule is designed for one-off campaigns that you wish to send immediately, such as messages about a current event. A sports app, for instance, may schedule push notifications on score updates using this option. In addition, when sending test messages aimed at just yourself or your team, this option allows you to deliver them immediately. 

If you plan on editing the campaign and re-sending it after viewing the test, be sure to check the box that makes users [re-eligible]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) to receive the campaign. By default, Braze sends a campaign to a user just once unless that box is checked.

## Option 2: Send at a designated time

Scheduling a campaign for a designated time allows you to specify the days and times your campaign sends. You can send a message once, daily, weekly, or monthly at a certain time of day, as well as specify when your campaign should begin and end. This end date is inclusive, which means the last send is on the end date.

If you select a monthly recurring schedule, note that some months may not have the selected day. For example, let's say you set a campaign to send monthly on the 31st day. In this scenario, Braze sends on the last day of that month, such as April 30, because April 31 doesn't exist.

If you select **Scheduled Delivery** and don't choose to send at user local time, your campaign will send according to the time zone specified on your **Company Settings** page.

![The time-based scheduling options for sending a campaign at a designated time.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Local time zone campaigns

You can deliver the message in users' local time zones so that members of your international audience won't receive a notification at inconvenient times. Local time zone campaigns need to be scheduled 24 hours in advance to ensure that eligible users from all time zones can receive them. Check out [Campaign FAQ]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) to understand how local time zone campaigns work and the associated delivery rules.

Segments targeted with local time zone campaigns should include, at minimum, a 2-day window to incorporate users from all time zones. For instance, if your campaign is scheduled to send in the evening but has just a 1-day window, some users may have fallen out of the segment when their time zone is reached. Examples of filters that create a 2-day window are "last used more than 1 day ago" and "last used less than 3 days ago," or "first purchased more than 7 days ago" and "first purchased less than 9 days ago."

### Use cases

Designated time schedules are best suited for messages scheduled in advance and recurring campaigns, such as onboarding and retention, that run regularly on all qualified users.

## Option 3: Intelligent Timing

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) allows you to deliver a campaign to each user at a different time. Braze calculates each individual's time based on when that user typically engages with your app and its notifications. You can optionally specify that Intelligent Timing campaigns send only during a certain portion of the day. For instance, if you are notifying users of a promotion that ends at midnight, you may want your messages to send by 10 pm at the latest.

![The time-based scheduling options for using Intelligent Timing to send a campaign at the most popular time to use the app among all users.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Delivery rules

Because a user's optimal time can be any time over the course of 24 hours across all global time zones, all Intelligent Timing campaigns must be scheduled 48 hours in advance. Scheduling 48 hours ahead accounts for delivery to all users worldwide, as a single day spans approximately 48 hours across all time zones. In addition, similar to designated time campaigns, messages with a 1-day window miss users who fall out of the segment before their optimal time in their time zone is reached. Segments for Intelligent Timing campaigns should incorporate at minimum a 3-day window to account for this.

If a user's profile does not have enough data to calculate an optimal time, you can choose a backup method to either send during the most popular time to use the app among all users or a set custom fallback time. 

### Use cases

Intelligent Timing campaigns work best for one-off and recurring messages where there is some flexibility regarding delivery time such as when they aren't well suited for breaking news or timed announcements.

## Audience criteria evaluation with delays

For campaigns that use scheduled delivery, audience criteria are always evaluated at the time of the scheduled send, not when the campaign launches. This applies to any delay between scheduling and sending—for example, rate limiting, local time zone, Intelligent Timing, or a trigger schedule.

### Timing of segment changes

If you modify a segment that's used as the audience for a scheduled campaign, changes made close to the scheduled send time are typically included when the audience is evaluated. The exact cutoff varies, but changes are generally included if they finish processing before Braze builds the audience for that send.

For example, if you update a segment at 3:50 pm for a campaign scheduled to send at 4 pm, Braze uses the updated segment criteria when evaluating the audience, assuming the changes finish processing before campaign execution begins.

#### Best practices

To give segment changes time to finish processing before your scheduled campaigns send:

- **Plan ahead:** Make segment changes well before the scheduled send time so they have time to finish processing.
- **Test first:** When possible, test changes in a smaller campaign before applying them to larger, more critical campaigns.

For more on scheduled delivery options, see [Delivery and entry types]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#time-based-options).

## Troubleshooting

### Why didn't my scheduled email campaign reach the entire estimated audience?

Sends can be lower than the estimated audience when users lack an email address, aren't subscribed to email, or are excluded by deliverability filters at send time. A recent change to a user's email address can also affect eligibility when audience criteria are re-evaluated at send. For more factors, see [Why are sends lower than the estimated audience size?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size).

### Why did my campaign send a day before the scheduled time?

If a campaign sends earlier than the schedule you set in **Company Settings**, enable **Send in local time zone** or add a delivery time window for Intelligent Timing campaigns. Without those settings, timezone evaluation can queue sends for users in earlier time zones before your intended schedule time. For more information, see [Local time zone campaigns](#local-time-zone-campaigns) and [When does Braze evaluate users for local time zone delivery?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery).

### What is the maximum delivery delay for in-app message campaigns?

In-app message campaigns that use a scheduled delivery delay can delay delivery by up to two hours (7,200 seconds). If you need a longer gap between scheduling and display, use a [trigger-based]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) campaign or Canvas step instead.

