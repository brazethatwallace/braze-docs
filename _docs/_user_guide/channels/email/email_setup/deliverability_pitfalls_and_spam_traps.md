---
nav_title: Deliverability pitfalls and spam traps
article_title: Deliverability Pitfalls & Spam Traps
page_order: 7
page_type: reference
description: "This reference article covers potential email deliverability pitfalls, spam traps, and how to avoid them."
channel: email

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}Deliverability pitfalls and spam traps

> This article covers common email deliverability pitfalls, spam traps, and how to avoid them.

Your email deliverability can be affected by any of the following spam traps:

| Trap Type | Description |
|---|---|
| Pristine Traps | Email addresses and domains that have never been used. |
| Recycled Traps | Email addresses that were originally real users, but are now dormant. |
| Typo Traps | Email addresses containing common typos. |
| Spam Complaints | When your email is marked as spam by a customer. |
| High Bounce Rate | When your email consistently fails to deliver because the recipient's address is invalid. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="![Braze Learning course](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability): style="float:right;width:120px;border:0;" class="noimgborder"Deliverability pitfalls and spam traps" }

## How to avoid spam traps

These traps can be avoided if you set up a confirmed opt-in process. By sending an initial opt-in email and asking customers to verify that they want your messages, you're ensuring your recipients want to hear from you, and that you're sending to real, valid addresses. Here are additional ways to avoid spam traps:

1. Send a double opt-in email. This is an email that will require users to confirm their subscription choices by clicking a link.
2. As a best practice, implement a [sunset policy]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/).
3. **Never purchase email lists.** 

{% alert tip %}
The Braze Customer Success and Deliverability teams can help make sure you're following best practices to maximize deliverability across the globe.
{% endalert %}

## How to resolve a free email domain block for Microsoft

It is very rare for Microsoft to unblock a sender who is having trouble delivering to the free email domains (Hotmail, Live, MSN, Outlook). Instead, we recommend that senders aggressively reduce their volumes to those domains and send only to recently engaged contacts, or even stop sending to those domains altogether if they're unable to identify a core group of engaged recipients.

An example free email domain block message is: 

`550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your Internet service provider since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

You can slowly add more volume similar to during the initial warming period, paying close attention to metrics. There's often a root cause of the deliverability issues to identify and resolve. In general, this is a lack of proper permission, a lack of ongoing list hygiene, or a combination of those factors.

## Remove an email address from your bounce or spam list

You can remove bounced emails and emails on your Braze spam list with the following endpoints:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## Improve email deliverability

For best practices to improve your email deliverability, see [Improve email deliverability]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/).