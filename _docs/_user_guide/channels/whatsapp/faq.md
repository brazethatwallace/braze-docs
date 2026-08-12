---
nav_title: FAQ
article_title: "FAQ"
page_order: 30
description: "This article addresses some of the most frequently asked questions that arise when setting up WhatsApp campaigns."
page_type: FAQ
channel:
  - WhatsApp

---

# Frequently asked questions

> On this page, we'll attempt to answer your most stringent questions about WhatsApp!<br><br>This FAQ is not intended to provide, nor may it be relied upon as providing legal advice. The use of the WhatsApp channel is subject to specific Meta Platforms, Inc. requirements. To ensure that you are using the WhatsApp channel in compliance with all applicable requirements and any laws to which you may specifically be subject, you should seek the advice of your legal counsel.

## FAQ topics
- [WhatsApp business accounts](#whatsapp-business-accounts)
- [WhatsApp business account phone number](#whatsapp-business-account-phone-numbers)
- [Opt-in and subscription management](#opt-in-and-subscription-management) 
- [Messaging limits and quality rating](#messaging-limits-and-quality-rating) 
- [WhatsApp templates and composer](#whatsapp-templates-and-composer)
- [Deliverability and billing](#deliverability-and-billing) 
- [Integrations, data, and reporting](#integrations-data-and-reporting)
- [Media and images](#media-and-images)

### WhatsApp business accounts 

#### How do I create a WhatsApp business account? 
We recommend creating your WhatsApp business account (WABA) through the embedded sign-up flow in the Braze dashboard. 

#### I already have a Meta business account. Do I still need a WhatsApp business account? 
Yes, you still need to create a WhatsApp business account. We recommend you [nest your WABA underneath your main Meta business account]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup). 

#### How do I access my WhatsApp business account? 
After completing the embedded sign-up flow, you can access your account at business.facebook.com by navigating to the [WhatsApp section](https://business.facebook.com/wa/manage/home). 

#### Can I connect multiple WABAs to Braze? 
Yes, you can add up to 10 WhatsApp Business accounts per workspace, and each business account can be nested under a different Meta Business Manager.

![Diagram of the Braze and WhatsApp ecosystem, showing how workspaces and WhatsApp Business accounts connect to each other: you can connect one subscription group to one phone number, multiple WhatsApp Business accounts to one workspace, and one workspace to multiple Meta Business Portfolios.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

#### Can I change my WhatsApp Business Account currency?
No. Meta controls the currency for your WhatsApp Business Account, and Braze can't change or convert it. To use a different currency, [create a separate WhatsApp Business Account]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) with that currency, or contact Meta support to ask whether they can update the currency on your existing account.

#### What is business verification? 
Business verification is a WhatsApp concept used to ensure that the brand is a legitimate business. It can be completed in the WhatsApp Manager. Business verification is also required to scale messaging. Without business verification, customers can only send up to 250 unique end-users in a rolling 24-hour period. 

#### What is an official business account? 
OBA gives you the green check mark next to your display name and is optional. You can apply for an official business account after completing business verification. Note that business verification and an official business account are different WhatsApp concepts. 

#### Why might my WhatsApp Business display name be rejected?
WhatsApp Business display name rejections are governed by Meta. If your display name is rejected, refer to [WhatsApp's display name guidelines](https://faq.whatsapp.com/793641088597363) for their guidelines.

If your display name meets the guidelines and is still being rejected, Braze can't view the specific reasons. However, the most common reason for rejection is that a business's online presence is too low, or the business is marketing [regulated or restricted products](https://business.whatsapp.com/policy#further-guidance).

For further guidance on display name rejections, refer to [Meta resources]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources).

### WhatsApp business account phone numbers 
#### Do I need a phone number for my WhatsApp business account? 
Yes, you need a number that you have access to. You will be asked to verify your phone number with 2-factor authentication when you go through the embedded sign-up flow. The phone number cannot be used for other WhatsApp accounts (business or personal).

#### What types of phone numbers are supported with WhatsApp? 
Refer to Meta's requirements for [phone numbers](https://developers.facebook.com/docs/whatsapp/phone-numbers) for more information. 

#### Can I use one phone number across multiple WABAs? 
No. A phone number cannot be shared across multiple WABAs. 

#### Do I need a specific type of phone number to send messages to specific countries? 
No. WhatsApp allows you to send messages to end-users from any supported phone number in any country. Refer to Meta's requirements for [phone numbers](https://developers.facebook.com/docs/whatsapp/phone-numbers) for more information. 

#### How do user phone numbers need to be stored in Braze? 
User phone numbers need to be stored in [E.164 format]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers#formatting).

#### Can I import user phone numbers? 
Yes. You can [import user phone numbers]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers). 

### Opt-in and subscription management 

#### Do I need to collect opt-in to send marketing messages to end-users on WhatsApp? 
Yes, WhatsApp requires businesses to [collect opt-in consent](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) to send marketing messages to end-users.

#### Can I proactively message end-users on WhatsApp to collect opt-in consent? 
If you choose to proactively message end-users, your first business-initiated message should ask the user if the user wants to receive marketing messages from your business and should comply with Meta's requirements for [getting opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Keep in mind that WhatsApp will monitor your business reputation on the channel, so the recommended best practice is to be explicit with end-users and only send messages they have indicated they want to receive.
 
#### Do I need to collect the end user's phone number when I collect opt-in? 
You need to have the end-users phone number on the Braze profile to message them. 
- If you already have their number, you do not need to collect it during opt-in. 
- If you do not have the end-users number, your opt-in method should include phone number capture. 

#### How do I update the subscription status of end-users who opt-in? 
Subscription management of the WhatsApp Channel functions similarly to how it functions in other Braze channels. Refer to [Managing user subscriptions]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) for more information.  

#### If I already have a list of users who have opted-in to receive marketing messages on WhatsApp, how do I update their subscription status in Braze? 
You can update their subscription status via [user import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#updating-subscription-group-status-optional). 

#### What methods should I use to collect opt-ins? 
Braze recommends referring to [Meta's guidelines for opt-in methods](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) to maintain compliance. Refer to the following resource for Braze [channel and opt-in ideas and suggestions](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit).

#### Is double opt-in required for WhatsApp? 
No, double opt-in is not required. 

#### How do my users opt out of WhatsApp messages? 
Your users can opt out in two ways:
1. Set up an inbound WhatsApp message with a specific opt-out word and use a webhook to update the user subscription status.
2. Add an opt-out quick reply within the WhatsApp template, with a corresponding webhook to update. 

### Messaging limits and quality rating

#### What are messaging limits? 
Messaging limits are a WhatsApp integrity building concept. They determine the maximum number of business-initiated conversations each phone number can start in a rolling 24-hour period. There are four messaging limit levels: 1k, 10k, 100k, and unlimited.

#### How do I increase my messaging limit? 
WhatsApp will increase your messaging limit if you meet the following conditions:
1. [Phone number status](https://www.facebook.com/business/help/896873687365001) is **Connected** 
2. [Phone number quality rating](https://www.facebook.com/business/help/896873687365001) is **Medium** or **High**
3. In the last seven days, you have initiated X or more conversations with unique users, where X is your current messaging limit divided by 2 

So, to go from 100k to unlimited, you must send at least 50,000 business-initiated conversations in a 7-day period. 

#### How long does it take to increase my messaging limits? 
If all of the previous conditions are met, you can increase your messaging limit from 1k to unlimited in 4 days. 

#### Where can I see my current messaging limit? 
You can check your current messaging limits in the **WhatsApp Manager > Overview Dashboard > Insights** tab. 

#### What happens if I attempt to send messages when I have already reached my messaging limit?
If you try to send a campaign or Canvas to more unique users than your current limit allows, the messages will fail to send. Braze will continue to attempt to resend the messages if/when your messaging limit increases for up to one day. 

#### Can my messaging limit decrease?
Yes, if your phone number quality rating drops too low, you are at risk of WhatsApp decreasing your messaging limit. Braze recommends you subscribe and be notified of quality-related updates from WhatsApp, including updates to your phone number status and messaging limit level. You can subscribe to notifications directly in the WhatsApp Manager dashboard. 

#### What factors affect phone number quality rating, and what happens when my quality rating drops too low? 
Factors that affect phone number quality rating include an end-user blocking a business (and the reasons they provide when they block a business) and an end-user reporting a business. 

When a quality rating is low, the phone number status changes from **Connected** to **Flagged**. If the quality doesn't improve over seven days, the status returns to **Connected**. However, the messaging limit will decrease to the next level. For example, a phone number that used to have a 100,000 messaging limit now has a 10,000 messaging limit.

#### What is the Meta throughput limit?
Meta has their own throughput limit separate from the WABA messaging limit. The default limit the cloud API supports is 80 messages per second. If you think your campaigns will exceed this limit, you can [request](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) for your limit to be increased. Meta recommends that you submit this request at least three days in advance of campaign sends.

### WhatsApp templates and composer

#### What is a WhatsApp Template? 
WhatsApp requires that all business-initiated messages start using an approved template. The template includes the copy of the message, along with optional rich media like images, calls-to-action, and quick reply buttons. After WhatsApp approves templates, they can be used to compose a WhatsApp message in Braze. 

#### Where do I create, edit, and manage my WhatsApp templates? 
You can create and submit templates in Braze using the [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), or in Meta's WhatsApp Manager. Templates created in either location appear in the Braze dashboard with a status indicator. After submission, locked fields require Meta re-approval; see [editing limitations in the Template Builder FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder#can-i-edit-a-template-after-its-been-approved) for details.

#### How long does it take WhatsApp to review a template submission? 
The approval process can take up to 24 hours, but often templates get processed in a matter of hours or minutes. 

#### How many templates can I have at a given time? 
Your message template limit depends on your business verification status. You can check your limit on the **WhatsApp Manager > Message Templates** page. 

#### How do I personalize template copy and rich media in Braze? 
WhatsApp allows for variable parameters to be inserted into message templates. Messages cannot start or end with a variable parameter. Variable parameters can be populated with Liquid logic in the Braze platform. Refer to [composing a WhatsApp message in Braze]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) to learn more about variable parameters. 

#### My template got rejected. Can Braze help me get it approved? 
The Braze team does not have visibility into template rejections. You should work directly with your WhatsApp Business manager to edit and resubmit the template. Make sure to provide a sample template where necessary. Double-check that your template follows Meta's [business](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) or [commerce](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) policies.

#### Can the rich media be targeted or personalized in Braze? 
Images can be uploaded from the media library but cannot be dynamically targeted. For URLs, the last part of the link can be [dynamically populated using Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls). 

#### What kind of rich media is supported in WhatsApp templates?
You can add images, calls to action (URL or phone number), and quick reply buttons to WhatsApp templates. You can add these elements when you build templates directly in WhatsApp. 

#### What if my template was falsely flagged for violating WhatsApp's Commerce Policy?
If you believe Meta falsely flagged your template, use the review link in the email from WhatsApp to request a re-review. The WhatsApp Business team reviews the decision and reverses it if appropriate.

#### Why does my imported WhatsApp template show "Message Incomplete" in the composer?
The "Message Incomplete" warning appears when required template variable slots aren't filled with valid values in the composer.

When you create templates using the [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder), Braze renumbers variables into sequential placeholders ({% raw %}`{{1}}`, `{{2}}`, `{{3}}`{% endraw %}, and so on). Templates created externally in Meta's WhatsApp Manager may still include patterns that make variable mapping error-prone, such as:

- Non-sequential numbering (for example, {% raw %}`{{1}}`, `{{3}}`, `{{5}}`{% endraw %})
- Missing variables in the sequence (for example, skipping {% raw %}`{{2}}`{% endraw %})
- Variables that start at a number other than 1

To resolve this, edit your template in Meta's WhatsApp Manager to use sequential placeholder formatting, then re-import it into Braze. In Braze, confirm each required variable field is populated with a valid Liquid value.

#### Why is my WhatsApp campaign not sending despite template previewing?
If your template previews correctly but the processing ledger shows **Abort** with details "Param text cannot have new-line/tab characters or more than 4 consecutive spaces", check the Liquid-templated parameter values in your message. WhatsApp requires that parameter text values don't contain:

- New-line characters
- Tab characters
- More than 4 consecutive spaces

Confirm that any Liquid logic that populates template parameters removes these characters or formats the text accordingly before sending.

### Deliverability and billing

#### Why would a message not be delivered? 
There are various reasons a message would fail to be delivered, including network issues and the device being turned off. 

#### If a message is not delivered, will I be billed? 
No. If a message is not delivered, you are not billed. 

#### What happens if a user blocks my business? 
If a user blocks your business, subsequent messages you attempt to send don't deliver, and you aren't billed. The user's subscription status won't update.

#### What happens if a user reports a message? 
If a user reports a message, you can still send subsequent messages to them. However, reporting may affect your quality rating on the channel. The user's subscription status doesn't update.

#### How can I exclude users who report my WhatsApp account from upcoming launches?
Braze doesn't receive notifications from WhatsApp when your account is flagged or reported, so you can't automatically identify or exclude those users in Braze. Users who report your account may remain in your WhatsApp subscription group and continue to be eligible for future messages. 

You can, however, set up a campaign that triggers when a user responds with an opt-out keyword, which automatically unsubscribes them using the [`/subscription/status/set` endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). For more information, see [WhatsApp opt-in and opt-out process]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

#### Does Braze support automatic SMS fallback when WhatsApp delivery fails?

No. Braze doesn't offer a native WhatsApp-to-SMS fallback path. To retry on another channel, segment users with failed WhatsApp sends (for example, through Currents failure events) and target an SMS or email campaign.

#### Are WhatsApp response messages free? {#are-whatsapp-response-messages-free}

Response messages composed in the Braze campaign or Canvas editor (not approved WhatsApp templates) are treated as service messages by Meta. Service messages sent through Braze's native WhatsApp integration don't consume Action Credits when they are sent as [response messages]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#response-messages) within an open customer service window.

| Message type | Action Credits | Notes |
|---|---|---|
| Response message (inbound reply) | Not consumed | Composed in Braze; not a Meta-approved template. |
| Template message | Consumed | Marketing, utility, authentication, and limited time offer templates are billed per send. |
| Utility template in service window | Not consumed by Meta | Meta doesn't charge for utility templates sent within 24 hours of a user-initiated message. Action Credit consumption follows your contract. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Response message Action Credits" }

For Canvas flows where users tap quick replies after the original 24-hour window, see [Quick replies and inbound messages outside the 24-hour window]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### What happens if a user replies or taps a quick reply after the 24-hour window closes?
A new 24-hour customer service window opens. See [Quick replies and inbound messages outside the 24-hour window]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Do I need to set my Canvas Action Path to 31 days for WhatsApp quick replies?
No. The default Action Path duration is sufficient. See [Quick replies and inbound messages outside the 24-hour window]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies-and-inbound-messages-outside-the-24-hour-window).

#### Can I see how many WhatsApp credits a specific campaign or Canvas consumed?
Not in the Braze dashboard today. Campaign and Canvas analytics show sends, deliveries, and failures, but not credit consumption per message. Send counts do not align one-to-one with credit usage because template category and message type affect billing differently. For billing details, see [Are WhatsApp response messages free?](#are-whatsapp-response-messages-free).

### Integrations, data, and reporting

#### Does Braze support customer support use cases like chatbots and human-assisted chat for WhatsApp? 
We do not support chatbots or human-assisted chat within Braze or through direct integrations. 

If you already use WhatsApp as a customer support channel, we recommend you keep your current setup and create a new WABA via Braze for marketing messaging. This WABA will require a new phone number. 

#### How can I “bridge the gap” between my customer support messaging and my marketing messaging via Braze? 
You can use WhatsApp Liquid properties to forward inbound WhatsApp message content (including message body and media URLs) from Braze to other platforms, including any customer support tool. For details, see our [Supported personalization tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags). 

To send information into Braze, for example, to indicate that a user is in an active support conversation, you can log a custom attribute (such as a boolean "has existing support chat = true/false") and use that as segmentation criteria in their marketing campaigns. You can also deep link between two chat threads to direct users to the support thread from the marketing thread and the reverse. 

#### Does Braze store user responses? 
Messages are only stored long enough to process them. To access user messages, use Currents. 

#### What metrics are available in the Braze dashboard? 
You can see unique recipients, sends, deliveries, reads, and failures in the Braze dashboard. Note that a user's read receipts must be "On" for Braze to track reads. You can also set up conversion events to monitor campaign performance, similar to other channels.

#### What is a WhatsApp conversation? 
WhatsApp is a channel focused on 2-way messaging and thus anchors on conversations (instead of the number of individual messages). A conversation is a 24-hour thread between a business and an end-user.

- **Business-initiated conversation**: A conversation where the business starts by sending an approved template message to the end user. As soon as the business sends a message, it begins the 24-hour window.
- **User-initiated conversation**: A conversation where the end-user sends a message to the business. When the business sends a message in response, this begins the 24-hour window.

### Media and images

#### Why won't images load when sent as a WhatsApp message?
If users report that images in WhatsApp messages won't download or the download icon is unresponsive, this is likely due to a known issue in older WhatsApp app versions. This issue can usually be resolved by upgrading the device to the most recent version of WhatsApp.
