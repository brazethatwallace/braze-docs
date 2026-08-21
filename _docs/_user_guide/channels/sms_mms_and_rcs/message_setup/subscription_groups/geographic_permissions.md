---
nav_title: "Geographic permissions"
article_title: Geographic permissions
description: "This article covers the country allowlist for Geographic Permissions, which allows you to choose which countries SMS, MMS, and RCS can be delivered to."
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# Geographic permissions

> Geographic permissions enhance security and protect against fraudulent SMS, MMS, and RCS traffic by enforcing controls on the countries to which you can send messages. You can specify an allowlist of countries to only send SMS, MMS, and RCS messages to approved regions. Messages are only sent to phone numbers with those countries' dialing codes.<br><br> Only admins can make changes to the country allowlist. Non-admin users have access to a read-only version of the allowlist that indicates which countries a subscription group is able to send to.

If you're an admin, you can configure the countries that are on the allowlist. The country allowlist is configured at the [subscription group]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) level. You can access it by going to **Audience** > **Subscription Group Management** and selecting an SMS, MMS, or RCS subscription group. The allowlist is under **Geographic Permissions**.

![The editable Geographic Permissions section for an admin with several countries selected in the "Country allowlist".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## Selecting countries

Add countries to the allowlist with the dropdown. The most common SMS, MMS, and RCS countries are shown at the top, with others shown in the following section. You can also search for countries by typing in the text field.

![The "Country allowlist" dropdown with the most common countries displaying at the top.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Remove previously selected countries by clearing the respective boxes next to them.

### Saving your changes

Changes take effect after you save. Removing countries from your allowlist prevents all SMS, MMS, and RCS messages from being sent to phone numbers with those countries' dialing codes.

![Warning modal confirming the countries that will be deleted from the allowlist.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## High fraud risk countries

Certain countries have a higher risk of SMS, MMS, and RCS traffic pumping. These countries are indicated by a **High Fraud Risk** tag in the country dropdown.

![The country dropdown with Azerbaijan having a "High Fraud Risk" tag.]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

If you allow sending in these countries, you must first acknowledge the risk of doing so before the country is added to your allowlist.

{% alert note %}
Limit the countries on your allowlist to only those required to support your business needs. This minimizes your potential for fraudulent traffic. For more guidance on preventing SMS, MMS, and RCS traffic pumping, view [Understanding and preventing SMS, MMS, and RCS traffic pumping fraud]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud).
{% endalert %}

## Visibility of sends outside the allowlist

Attempted sends to countries that aren't on your country allowlist will be aborted. Aborted messages will be logged to the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) and within the [SMS abort message engagement event]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events). 

Aborted messages for recipients in countries not on your allowlist show as **Aborted Message Errors** and have the message "The recipient's phone number is in a blocked country".

![Abort log showing several SMS, MMS, and RCS sends aborted because the phone number's country isn't on the country allowlist.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## Important notice for High Fraud Risk countries and traffic pumping fraud

### What is SMS, MMS, and RCS traffic pumping? 

SMS, MMS, and RCS traffic pumping (also known as Artificially Inflated Traffic) is an escalating fraud scheme that may result in significant financial exposure to customers. Fraudsters can exploit your unprotected public-facing web forms, authentication flows, or API endpoints to trigger large volumes of SMS, MMS, and RCS sends (such as opt-in confirmations, one-time passwords, or notifications) to phone numbers they control or influence. The attackers then collect a revenue share from complicit or unknowing mobile networks for generating that artificial traffic. The downstream impact introduces significant financial exposure.

### What are High Fraud Risk countries?

A country or territory is designated as High Fraud Risk if it possesses an unusually high density of small, premium-rate local roaming carriers or lacks stringent regulatory oversight. Bad actors systematically target these high-rate carrier networks because they maximize the revenue share payout per message generated.

Furthermore, system routing restrictions are enforced based on destination country codes rather than a recipient’s actual physical location. This means if you have customers who travel frequently, you do not need to add their traveling locations to your Country Allowlist, as messaging will route based on the original destination country code, not their current physical location. For example, territories sharing a country code with lower-risk regions (such as Jersey or Guernsey sharing the +44 country code with the UK) still carry high carrier-rate exposure and are managed under these same high fraud risk framework conditions.

### Customer responsibility and financial liability 

The customer is responsible for and will be invoiced for all Mobile Messages sent through the Services on its behalf, including any messages resulting from SMS, MMS, and RCS traffic pumping. Platform safeguards, such as the Country Allowlist, will assist you in restricting delivery to trusted regions. Ultimately, however, securing your external-facing endpoints and preventing devastating financial harm remains the sole responsibility of the customer.

### How to prevent traffic pumping 

Failure to limit your message distribution strictly to the geographic regions where your actual customers reside creates immediate vulnerability to fraud and severe financial harm. To protect your company, you must proactively restrict your delivery regions using the Country Allowlist. In addition, and most importantly, you should secure any online phone number request form or API endpoint that triggers SMS, MMS, and RCS sends in accordance with industry best practices, as described in [Understanding and preventing SMS, MMS, and RCS traffic pumping fraud]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud).