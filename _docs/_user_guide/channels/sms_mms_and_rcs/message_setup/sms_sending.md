---
nav_title: SMS sending
article_title: SMS sending
page_order: 4
alias: /sms_message_sending/
description: "Review subscription groups, message billing, and keyword fundamentals for sending SMS messages."
page_type: reference
channel:
  - SMS
  
---

# SMS message sending

> Review the subscription, billing, and keyword fundamentals that apply when you send SMS messages with Braze.

## SMS sending basics

### Select your subscription group

Send SMS messages from a [subscription group]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups). A subscription group contains sending phone numbers, such as short codes, long codes, and alphanumeric sender IDs, for a specific messaging purpose. Use separate subscription groups for use cases such as transactional and promotional messaging.

### Compose the message

For message fields, character limits, personalization, media, and link shortening, see [Create an SMS, MMS, or RCS message]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#sms-and-mms-fields-and-settings).

### Understand message segments and character limits

SMS messages use GSM-7 or UCS-2 encoding and are charged per message segment. For encoding rules, segment sizes, and the segment calculator, see [SMS and RCS billing calculators]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

### Keyword customization (optional)

Regulations require responses to opt-in, opt-out, and Help or Info keywords. Define keywords, responses, and language-specific keyword sets through [Keyword processing]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

For sending best practices, including multi-country and high-volume sending guidance, refer to [Best practices for SMS, MMS, and RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices).

