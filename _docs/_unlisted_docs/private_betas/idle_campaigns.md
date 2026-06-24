---
nav_title: "Idle Campaigns and Canvases"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Idle campaigns and Canvases

> This reference article explains the idle status for campaigns and Canvases and answers frequently asked questions.

{% alert note %}
In 2024, Canvases will be marked **Idle** and stopped, similar to campaigns. When Canvases are idle or stopped, they will follow the logic in this document.
{% endalert %}

Campaigns and Canvases are assigned an idle status when they have not sent messages or entered users in some time. These campaigns and Canvases will be automatically stopped at their associated stop dates. You can filter for idle campaigns and Canvases to help you sort and manage your list of campaigns and Canvases.

Campaigns and Canvases with end dates and one-time sends are idle for 7 days before auto-stopping. Campaigns and Canvases that haven't sent a message in 11 months are idle for 1 month before auto-stopping.

## Idle campaigns

On an ongoing basis, the idle campaigns that meet the following criteria will be stopped:
 
- A scheduled one-time send is past its send date by seven days
- A scheduled or action-based campaign with an end date is past its end date by seven days
- A campaign without an end date that has not sent messages in one year

For campaigns without end dates, if a message is sent or the campaign is updated, the one-year countdown for stopping the campaign will be reset. When campaigns are stopped, Braze will notify customers in their dashboard and by email.

Campaigns will be stopped at the later of the default stop date and one day after their last occurring conversion deadline. Sends that are a result of a Winning or Personalized Variant are treated as scheduled sends, and will be stopped seven days after the Winning or Personalized Variant is sent. All campaigns will be stopped at 4 am UTC every day for all Braze users.

Content Cards will not be stopped until their expiration deadline, and will also abide by the aforementioned criteria as well as the conversion deadline rule.

Reference this table for how to keep an idle campaign active:

| Reason for idle status                                                                              | Steps to make campaign active                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campaigns that are scheduled one-time sends, and are past the send date                 | Schedule a future send                            |
| Campaigns that are scheduled or action-based, have end dates, and are past the end date | Extend the end date                               |
| Campaigns without an end date that have not sent messages in one year                                | Send one message or make any edit to the campaign |
| Campaigns with end dates and one-time sends | Schedule a future send |
| Campaigns that have not sent a message in 11 months | Send one message or make any edit to the campaign | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### In-app message campaigns

If an in-app message campaign has no impressions and has not been edited for over 30 days, it becomes an idle campaign. An idle in-app message campaign continues to deliver based on its configuration, but the in-app message becomes a templated in-app message.

If your users trigger an impression event or the marketer edits the campaign, it brings the campaign back to active status and the 30-day counter resets.

## Idle Canvases

On an ongoing basis, idle Canvases that meet the following criteria will be stopped:

- A scheduled one-time send is past its send date and maximum duration by over 7 days
- A scheduled or action-based Canvas with an end date is past its end date and maximum duration by over 7 days
- A Canvas without an end date has not entered users or been edited in over 12 months and its maximum duration

For Canvases without end dates, if a user is entered or the Canvas is updated, the one-year countdown for stopping the Canvas will be reset. When Canvases are stopped, Braze will notify customers in their dashboard and via email.

The [maximum duration]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) of a Canvas is the longest possible time a user can take to complete a given Canvas. This duration includes expirations for Content Cards and in-app messages.

Reference this table for how to keep an idle Canvas active:

| Reason for idle status                                                                                                  | Steps to make Canvas active                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Canvases that are scheduled one-time sends, and maximum duration past the send date                 | Schedule a future send                          |
| Canvases that are scheduled or action-based, have end dates, and maximum duration past the end date | Extend the end date                             |
| Canvases without end dates that have not sent messages in one year                                                      | Send one message or make any edit to the Canvas |
| Canvases with end dates and one-time sends | Schedule a future send |
| Canvases that haven't sent a message in 11 months | Send one message or make any edit to the Canvas | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

If there isn't an option to restore interaction data, this may be because:

- The restoration or other interaction data-related operation is currently in progress.
- No interaction data existed for this Canvas.
- If the Canvas was created before 2021, the data may have been permanently deleted based on the previous policy.

## Frequently asked questions

#### What campaigns or Canvases does this apply to?

This will apply to campaigns and Canvases that already meet the previously listed criteria, and campaigns and Canvases that will meet the criteria moving forward.

#### How do I know if a campaign or Canvas is idle?

Idle campaigns and Canvases will be displayed in the campaign and Canvas list pages under the category **Idle**. The date on which the campaign or Canvas will be stopped is listed as a column in the list.

![The "Idle" filter on the "Campaigns" page.][1]{: style="max-width:60%;"}

#### What happens if an idle campaign or Canvas is updated?

If a campaign that hasn’t sent a message or a Canvas that hasn’t entered users is updated, the countdown will reset.

#### What happens to campaigns that haven’t sent a message in one year (or Canvases that haven’t entered users in one year), but have an end date in the future?

We will stop these campaigns and Canvases seven days after the end date at 4 am UTC.

##### Can I stop campaigns from automatically stopping?

No. This helps keep only the necessary campaigns active to keep dashboards less cluttered and improve performance. If you'd like a list of all auto-stopped campaigns, [submit a Support ticket]({{site.baseurl}}/help/support) to be provided one. 

#### Who will receive email notifications about stopped campaigns and Canvases?

By default, all users with administrator permissions are opted into email notifications about auto-stopping campaigns and Canvases. The creator of the campaign or Canvas will always be notified when it is stopped. Users can manage email notification preferences by going to **Company Settings** > **Notification Preferences**, then adding or removing recipients from the notification **Campaign Automatically Stopped** and the notification **Canvas Automatically Stopped**.

#### How does stopping Content Cards work?

Content Cards in campaigns will not be stopped until their expiration deadline and the appropriate buffer period. They will be stopped at the later of the buffer period (corresponding to whether the campaign is a one-time send, has an end date, or does not have an end date) and the expiration deadline. 

For example, if a Content Card expires on April 1, is a one-time send, and has a conversion deadline of 10 days, it will be stopped on April 12 (10 days after the conversion deadline, plus one day). If a Content Card expires on April 1, is API-triggered, and has not sent messages since March 15, it will expire on March 15 of next year.

Canvases are only stopped after the Content Cards are stopped, meaning their maximum duration has passed.

#### I have a feature flag experiment in my Canvas. After my feature flag is set, will the Canvas remain active?

Canvases with feature flag steps are not automatically stopped and do not become idle.

#### Why am I seeing idle campaigns displayed in my campaigns list when I applied a filter to show active campaigns only?

Idle campaigns are considered active until they're stopped.

#### Would a campaign be listed as idle when it's still sending push notifications?

No. A campaign will be listed as idle when it's no longer actively sending messages.

[1]: {% image_buster /assets/unlisted_docs/img/idle_filter.png %}