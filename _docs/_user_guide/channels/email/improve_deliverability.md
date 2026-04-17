---
nav_title: Improve deliverability
article_title: Improve email deliverability
page_order: 8
page_type: reference
description: "This reference article explains why marketing email can reach the spam folder and how sending patterns, message content, and recipient behavior affect inbox placement."
channel: email

---

# Improve email deliverability

Mailbox providers (MBPs) weigh your sending domain's reputation when they accept or bounce a message. Sometimes a message is accepted but not placed in the inbox. It can be routed to the spam folder instead, where recipients are less likely to see it.

The sections below summarize common drivers of spam-folder placement and low engagement. They aren't exhaustive; use them alongside your deliverability team and the resources at the end of this article.

## Sending patterns

Sending patterns influence domain reputation. When they drift from best practices, MBPs are more likely to bounce or filter mail.

- Collect high-quality subscriber data. Gather valid addresses, use voluntary opt-in with clear language, and consider confirmed opt-in or validation services so people know what they're signing up for. Design the signup flow to be clear and resistant to fraudulent signups.
- Set expectations about content and frequency, then honor them. Avoid mailing products or cadences the subscriber didn't agree to.
- Send mail subscribers want to open and interact with. Ask what value each send provides before you schedule it.
- When you can, prioritize recipients who recently opted in or engaged (opens, clicks, site activity). Avoid repeatedly mailing long-inactive addresses.
- Many MBPs treat transactional mail differently from marketing. Separate streams when it makes sense for your program—Gmail has published guidance that distinct **From** addresses can be enough separation in some cases.

## Message content

Content filters help MBPs protect their users from phishing, malware, and unwanted mail. Your creative can look benign to you but still resemble patterns filters watch for.

- Review whether recent changes (HTML, image ratio, image hosts, new templates) line up with when placement shifted. If known-good creative still reaches the inbox when sent through Braze, the current content may be contributing to spam-folder routing.
- Keep templates and copy fresh when engagement drops. Stale, repetitive sends give subscribers little reason to open.

## Recipient reports and behavior

Subscriber actions feed both reputation systems and future inbox decisions.

- MBPs act quickly on spam complaints. High complaint volume can divert later messages to spam, which acts like a quarantine when the MBP or the user isn't confident in the mail's quality.
- Deletes without opens, low engagement, and weak subject lines all signal disinterest before the body is read. Write relevant subject lines and body content with clear calls to action.
- When mail lands in spam, ask engaged subscribers (through other channels) to mark it as **Not spam** and to add your **From** address to their contacts. Google's postmaster guidance has also suggested asking subscribers to mark messages as **Important** where that control exists.

If placement doesn't improve after you adjust targeting and creative, treat it as subscriber feedback that your program needs a broader change—not only a copy tweak.

## Related resources

- [Sunset policies]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/)
- [IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/)
- [Deliverability pitfalls and spam traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/)
- [Know before you send]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send/#general)
- [Consent and address collection]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection/#subscriber-states)
- [Email FAQ]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)
- [Deliverability indicators: Understanding spam complaints and what they mean for customer engagement](https://www.braze.com/resources/articles/deliverability-indicators-understanding-spam-complaints)
- [Destination inbox: Navigating the modern landscape of email deliverability](https://www.braze.com/resources/articles/navigating-email-deliverability)
