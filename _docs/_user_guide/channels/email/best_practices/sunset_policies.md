---
nav_title: Sunset policies
article_title: Sunset Policies for Email
page_order: 8
page_type: reference
description: "This article covers best practices surrounding sunset policies and understanding situations when it's better to discontinue messages to disengaged users."
channel: email

---

# Sunset policies

> While you may be tempted to send campaigns to as many users as you can, there are situations when it is actually advantageous to stop messages to disengaged users. 

For emails, your sending IP and domain reputation factor in engagement, spam reporting, blocklisting, and more. If reputation stays low, ISPs and mailbox filters may sort your mail into spam or low-priority folders for all recipients, not only inactive ones. Sunset policies limit ongoing sends to disengaged users, which helps protect reputation; pair them with regular monitoring so you can spot issues early.

## Monitor IP and domain health

Use the [Deliverability Center]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center/) (**Analytics** > **Email Performance** > **Deliverability Center**) to track how mailbox providers see your sending:

- **Google Postmaster Tools** (after you connect your account): IP reputation, domain reputation, delivery errors, authentication (SPF, DKIM, DMARC), and encryption metrics for Gmail-related visibility.
- **Microsoft Smart Network Data Services (SNDS)** (when configured for your IPs): Outlook and Microsoft mailbox IP health, including filter results, complaint rates, and spam trap hits.

For broader sending hygiene, see [Improve email deliverability]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/) and [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/).

You can also leverage external tools such as [Sender Score](https://www.senderscore.org/) or [Outlook Smart Network Data Services](https://postmaster.live.com/snds/) outside Braze for additional signals.

## Use suppression lists

[Suppression lists]({{site.baseurl}}/user_guide/audience/suppression_lists/) are groups of users defined with segment filters who do not receive campaigns or Canvases by default, even when they appear in the target segment. For inactive or disengaged recipients, a suppression list acts as a workspace-wide guardrail. When users meet your inactive criteria, they stop receiving most messaging without you editing every segment or campaign.

To align with a sunset policy, build the suppression list with filters that capture users who should no longer get ongoing promotional email (for example, `Last Engaged With Message` or other filters under **Retargeting**) using the same lookback window and channel choices you use for “unengaged” in your policy. Membership is dynamic, so users enter when they meet the filters and exit when they engage again.

If you still want certain sends to reach inactive users, such as a final win-back or approved transactional journeys, configure exception tags on the suppression list so campaigns or Canvases with those tags still deliver when users are in the target audience. For setup steps, permissions, and limits, see [Setting up suppression lists]({{site.baseurl}}/user_guide/audience/suppression_lists/#setup).

Suppression lists work alongside segmentation, which can define who you include in a send.

## Use segmentation filters

Segmentation filters help prevent your messaging from appearing like spam by letting you easily implement sunset policies for emails, push, and in-app notifications. Here are some things to consider when you create a sunset policy:

- What counts as an "unengaged" user? 
- Is engagement defined by clicks, purchases, app usage, or a combination of these behaviors? 
- How long does the lapse in engagement need to be for you to stop sending messages?
- Will you deliver any special campaigns to users before excluding them from your segments?
- Which messaging channels will your sunset policy apply to? 

For example, if you have users who opt in to [Apple's Mail Privacy Protection (MPP)]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp), consider how this may impact your email campaigns and deliverability metrics and determine how to best structure your sunset policy.

To incorporate sunset policies into your campaigns, create a [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#creating-a-segment) that automatically excludes users who have marked your emails as spam or have not interacted with your messages for a certain period of time.  

To set up these segments, choose the `Has Marked You As Spam` and `Last Engaged With Message` filters located under the **Retargeting** section in the filter dropdown. 

When you apply the `Last Engaged With Message` filter, specify the type of messaging (push, email, or in-app notification) that the user has or has not interacted with, as well as the number of days it has been since the user last interacted. After you create a segment, choose to target this segment with any [messaging channel]({{site.baseurl}}/user_guide/channels).

![Segment Details page with the filter "Last Engaged with Message" selected.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

While Braze automatically stops sending emails to users who have marked you as spam, the `Has Marked You As Spam` filter allows you to also send these users targeted push messages and in-app notifications. This filter is useful for [retargeting campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#retarget-campaigns). For instance, you can send unengaged users messages that remind them of the features and deals that they are missing out on when they don't open your emails.

Sunset policies can be especially helpful in email campaigns that target lapsing users. While these campaigns focus on segments that have not interacted with your app for a period of time, they can put the deliverability of your emails at risk if they repeatedly include unengaged recipients. Sunset policies allow you to target lapsing users without landing in the spam folder.

