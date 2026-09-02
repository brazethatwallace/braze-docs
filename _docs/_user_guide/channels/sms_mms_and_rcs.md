---
nav_title: "SMS, MMS, and RCS"
article_title: "SMS, MMS, and RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "Learn SMS, MMS, and RCS in Braze, including setup, compliance, and best practices for reaching users by phone number."
---

# SMS, MMS, and RCS

> SMS (Short Messaging Service), MMS (Multimedia Messaging Service), and RCS (Rich Communication Services) offer a direct way to reach users on their phone numbers in real time. SMS remains one of the most widely used channels worldwide because it is fast, familiar, and effective for time-sensitive updates. This hub covers sender setup, compliance, opt-in collection, message creation, and reporting for SMS, MMS, and RCS in Braze. Review [Laws and regulations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) and [Collecting user opt-ins]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) before you send your first message.

## Prerequisites

SMS, MMS, and RCS availability depends on your Braze package. Contact your account manager or customer success manager to get started.

Before you start, make sure you have the following:

- Short codes, long codes, or Alphanumeric sender IDs configured. For more information, refer to [Sender setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).
- Familiarity with SMS laws and regulations, including TCPA and carrier requirements. For more information, refer to [Laws and regulations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).
- Explicit opt-in consent collected from users. For more information, refer to [Collecting user opt-ins]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins).

## Use cases

| Use case | Explanation |
| --- | --- |
| Appointment reminders | Send timely reminders before scheduled appointments, reducing no-shows and keeping customers informed. |
| Order updates | Notify customers about order confirmations, shipping status, and delivery updates in real time. |
| Two-factor authentication | Deliver one-time verification codes for account login and transaction confirmation. |
| Promotional offers | Reach customers with time-sensitive promotions, flash sales, and personalized discounts directly on their phone. |
| Customer support | Enable two-way conversations to resolve customer inquiries, collect feedback, or confirm service requests. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

## SMS, MMS, and RCS compared

- **SMS** delivers text-only messages up to 160 characters (or 70 characters with Unicode). It's universally supported across all mobile devices and carriers.
- **MMS** extends SMS with support for multimedia content, including images, GIFs, and audio. MMS requires carrier and device support.
- **RCS** is the next generation of business messaging, offering rich features such as branded sender profiles, suggested replies, carousels, and read receipts. RCS availability depends on carrier and device support.

### Why use RCS?

RCS (Rich Communication Services) builds on SMS with a richer, more app-like experience in the default messaging app on supported devices. Brands use RCS to:

- Deliver high-resolution images and video instead of only plain text.
- Add suggested replies and actions so customers can respond with one tap.
- Show a verified sender profile with branding so messages are easy to trust.
- Support read receipts and typing indicators where carriers allow it.

RCS is suited to use cases such as transactional updates (shipping, appointments), promotions with rich creative, customer support with quick-reply paths, and onboarding or tutorials that benefit from media and structured actions. For setup and migration from SMS, see [RCS setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Frequently asked questions

### Do I need opt-in consent before sending SMS in Braze? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

Yes. Collect explicit opt-in consent and follow applicable laws such as TCPA and carrier requirements. Refer to [Collecting user opt-ins]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) and [Laws and regulations]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### What is the difference between SMS, MMS, and RCS? {#what-is-the-difference-between-sms-mms-and-rcs}

SMS sends text-only messages, MMS adds multimedia such as images, and RCS adds rich features such as branded sender profiles and suggested replies on supported devices. See **SMS, MMS, and RCS compared** earlier on this page.

### How do I configure sender numbers for SMS? {#how-do-i-configure-sender-numbers-for-sms}

Set up short codes, long codes, or alphanumeric sender IDs in Braze before you launch campaigns. Refer to [Sender setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Next steps

- [Message setup]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [Create a message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)
