---
nav_title: Braze Action Credits Descriptions
permalink: "/message_credits_descriptions/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Action Credits descriptions

> Action Credits provide a flexible structure that allows you to easily access multi-channel messaging and advanced AI products while maximizing your marketing budget. Start by engaging on a single channel or region and seamlessly expand your mix to include AI agents as your business model, customer base, and engagement strategies evolve.

Action Credits can be applied across any of the channels and features presented on this page.

Note that the "Credit Ratio" referenced in this page is defined as the exact number of Action Credits it takes to perform the specified action.

## Table of contents

- [Email channel details](#email-channel-details)
- [SMS, MMS, and RCS channel details](#sms-mms-and-rcs-channel-details)
  - [SMS segments](#sms-segments)
  - [MMS messages](#mms-messages)
  - [RCS types](#rcs-types)
- [WhatsApp channel details](#whatsapp-channel-details)
  - [Billing region breakdown](#billing-region-breakdown)
- [Agent Console details](#agent-console-details)
- [Additional channel details](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [Banners](#banners)
  - [Audience Sync](#audience-sync)
  - [Message Archiving](#message-archiving)
  - [Webhooks](#webhooks)

## Email channel details

Email credit ratios are denominated in increments of one thousand emails sent (CPM) from the Braze platform.

{% alert note %}
Refer to our [email documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email) to learn more about our email channel.
{% endalert %}

## SMS, MMS, and RCS channel details

SMS and MMS credit ratios are denominated in increments of segments sent from the Braze platform. RCS credit ratios are denominated in increments of Basic and Rich Media types, or Single and Rich Media types delivered from the Braze platform. Both inbound and outbound types are billed.

{% alert note %}
Where applicable for these channels, carrier fees are billed separately (in arrears) and are not considered as part of Action Credits.
{% endalert %}

### SMS segments

The SMS industry counts messages in SMS message segments. A message segment is a grouping of up to a defined number of characters (160 for GSM-7 encoding; 67 for UCS-2 encoding) that will be sent in a single SMS dispatch. If you dispatch an SMS with 161 characters using GSM-7 encoding, two (2) message segments will be sent. Sending multiple message segments will result in additional charges.

### MMS messages

For MMS, the message limit is 5 MB (this includes the multimedia asset and the message body size). To be on the safer side, Braze recommends not exceeding 600 KB for your multimedia asset while also including a message body.

### RCS types

RCS is the next generation of SMS and MMS. It offers the benefits of a direct, high engagement channel like SMS–with richer capabilities that modern consumers have come to expect, like rich content (images, videos, documents), verified and branded sending, interactive features like suggested replies and actions, and more.

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
Refer to our [SMS and MMS documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms) to learn more about our SMS family offerings.
{% endalert %}

## WhatsApp channel details

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## Billing region breakdown

### North America

United States, Canada

### Rest of Africa

Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Chad, Congo, Eritrea, Ethiopia, Gabon, Gambia, Ghana,  Guinea-Bissau, Ivory Coast, Kenya, Lesotho, Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Morocco, Mozambique, Namibia, Niger, Rwanda, Senegal, Sierra Leone, Somalia, South Sudan, Sudan, Swaziland, Tanzania, Togo, Tunisia, Uganda, Zambia

### Rest of Asia Pacific

Afghanistan, Australia, Bangladesh, Cambodia, China, Japan, Laos, Mongolia, Nepal, New Zealand, Papua New Guinea, Philippines, Sri Lanka, Taiwan, Tajikistan, Thailand, Turkmenistan, Uzbekistan, Vietnam

### Rest of Central & Eastern Europe

Albania, Armenia, Azerbaijan, Belarus, Bulgaria, Croatia, Czech Republic, Georgia, Greece, Latvia, Lithuania, Macedonia, Moldova, Serbia, Slovakia, Slovenia, Ukraine

### Rest of Latin America

Bolivia, Costa Rica, Dominican Republic, Ecuador, El Salvador,Guatemala, Haiti, Honduras, Jamaica, Nicaragua, Panama, Paraguay, Puerto Rico, Uruguay, Venezuela

### Rest of Middle East

Bahrain, Iraq, Jordan, Kuwait, Lebanon, Oman, Yemen

### Rest of Western Europe

Austria, Belgium, Denmark, Finland, Ireland, Norway, Portugal, Sweden, Switzerland

{% alert note %}
Refer to our [WhatsApp documentation]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp) to learn more about our WhatsApp offerings.
{% endalert %}

## Agent Console details

Agent Console credit ratios are denominated in increments of one thousand (1,000) Invocations performed from the Braze platform. An Invocation is logged when an Agent initiates a call to an LLM. By default, your contract includes an allotment of invocations as specified by your Platform Edition per each Period of your Subscription Term. Additional invocations will be charged as per your Order Form.

{% alert note %}
Refer to our [Braze Agents documentation]({{site.baseurl}}/user_guide/brazeai/agents) to learn more about Agent Console.
{% endalert %}

## Additional channel details

### LINE

LINE credit ratios are denominated in increments of LINE messages sent from the Braze platform.

{% alert note %}
Refer to our [LINE documentation]({{site.baseurl}}/user_guide/message_building_by_channel/line) to learn more about using LINE with Braze.
{% endalert %}

### KakaoTalk

KakaoTalk credit ratios are denominated in increments of KakaoTalk messages sent from the Braze platform.

{% alert note %}
Refer to our [KakaoTalk documentation]({{site.baseurl}}/kakaotalk/) to learn more about using KakaoTalk with Braze.
{% endalert %}

### Content Cards

Content Cards credit ratios are denominated in increments of one thousand daily unique impressions.

Braze reserves the right to charge credits for Content Cards based on the number of Content Cards sent if the Customer does not set up Content Cards to log unique impressions according to Braze's guidance. This will be considered applicable if, within six (6) months of the first send of Content Cards, the Customer has:
- Sent more than five million (5,000,000) Content Cards, AND EITHER
    - Zero (0) impressions recorded
    - Sends-to-daily-unique-impressions ratio greater than one hundred (100)
    
{% alert note %}
Refer to our [Content Cards documentation]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) to learn more about Braze Content Cards.
{% endalert %}

### Banners

Banners credit ratios are denominated in increments of one thousand daily unique impressions.

{% alert note %}
Refer to our [Banner documentation]({{site.baseurl}}/developer_guide/banner_cards) to learn more about Braze Banners.
{% endalert %}

### Audience Sync

Audience Sync credit ratios are denominated in increments of one thousand total user syncs. By default, your contract includes five million user syncs per each Period of your Subscription Term. Additional user syncs will be charged as per your Order Form.

{% alert note %}
Refer to our [Canvas documentation]({{site.baseurl}}/partners/canvas_steps) to learn more about Canvas Audience Sync and available partners.
{% endalert %}

### Message Archiving

Message Archiving credit ratios are denominated in increments of one thousand archived messages across Push, Email, and SMS/MMS channels. 

{% alert note %}
Refer to our [message archiving documentation]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving#message-archiving) to learn more about Message Archiving.
{% endalert %}

### Webhooks

Webhooks credit ratios are denominated in increments of one thousand webhooks successfully sent from the Braze platform. By default, your contract includes one hundred thousand webhooks per each Period of your Subscription Term. Additional webhooks will be charged as per your Order Form.

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Refer to our [webhooks documentation]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) to learn more about Braze Webhooks.
{% endalert %}
