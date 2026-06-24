---
nav_title: WhatsApp Pricing Updates
permalink: "/whatsapp_pricing_updates/"
hidden: true
noindex: true
hide_toc: true
---

# WhatsApp pricing updates

## Additional WhatsApp Pricing Changes in October 2025
*Last Updated September 3, 2025*

### Pricing Changes in Some Regions

Effective **October 1**, Meta is updating rates in specific markets.

- **For utility and authentication messages:** Rates are being lowered in Argentina, Egypt, Mexico, and North America to ensure pricing remains compelling.
- **For marketing messages:** Rates are being lowered in Mexico to ensure pricing continues to motivate adoption and foster a healthy messaging ecosystem.

| Country and message type | % change |
| --- | --- |
| Argentina - Authentication                | -10.04%  |
| Argentina - Utility                       | -10.04%  |
| Egypt - Authentication                    | -30.43%  |
| Egypt - Authentication - International    | -0.58%   |
| Egypt - Utility                           | -30.43%  |
| Mexico - Marketing                        | -30.08%  |
| North America - Authentication            | -70.39%  |
| Saudi Arabia - Authentication             | -6.89%   |
| Saudi Arabia - Utility                    | -6.89%   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Additional WhatsApp Pricing Changes in July 2025
*Last Updated June 12, 2025*

In addition to the previously announced July pricing updates, Meta is rolling out a couple of additional updates that will also take effect on July 1, 2025. 

Here’s a quick summary of the previously announced changes: 
- WhatsApp pricing will shift to a "per message" model instead of a "per conversation" model. **The "per message" rates will be the same as the current "per conversation" rates.** 
- Utility templates sent in response to user messages (thus within an open [customer service window](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows)) will be free.

*For more details on these changes, see the previous post dated March 12th below.*

Additional July 1 changes (announced by Meta on May 15th): 
- Meta is updating utility and authentication rates across several markets as part of continued efforts to ensure pricing is on-par with alternative channels.
    - Pricing for utility and authentication messaging is dropping in all markets except Indonesia. In Indonesia, utility pricing is increasing and authentication pricing is decreasing. 
- Meta is refining their definition of utility, based on user engagement and sentiment, thus shifting specific use cases to and from the utility category. See their new definition for utility templates [here](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing#updates-to-template-category-guidelines).

For most customers, these updates will take effect automatically on July 1.

## Upcoming WhatsApp Pricing Changes in July 2025 

*Last Updated March 12th, 2025 (Originally Posted December 13th, 2024)*

WhatsApp is making two more updates to their pricing starting on July 1, 2025. Braze will update our pricing to reflect these changes on the same day. A summary of the changes and best practices to account for them are below.

### Update 1: WhatsApp pricing will shift to a "per message" model instead of a "per conversation" model. 

**The "per message" rates will be the same as the current "per conversation" rates.**

#### Why are they making this change?

Meta is shifting to a "per message" model to help brands simplify return-on-investment (ROI) calculations. This change will also make it easier for brands to do direct ROI comparisons with other channels that are priced per message. 

#### How will this affect my current WhatsApp usage? 

- Current conversations being sent with one message template in the 24-hour window will be unaffected.  
- **Current conversations being sent with two or more message templates of the _same type_ in the 24-hour window will increase in cost.** For example, sending two marketing templates in the 24-hour period will have twice the cost because you will be charged per message template.  

| Example scenario | Pricing before April 2025 | Pricing after April 2025|
| --- | --- | --- |
| Brand sends one marketing template message in the 24-hour window | Charged for one marketing conversation | Charged for one marketing message |
| Brand sends two marketing template messages in the 24-hour window | Charged for one marketing conversation | Charged for two marketing messages |
| Brand sends one utility template message in the 24-hour window  | Charged for one utility conversation | Charged for one utility message |
| Brand sends two utility template messages in the 24-hour window | Charged for one utility conversation | Charged for two utility messages |
| Brand sends one marketing template message and one utility template message in the 24-hour window | Charged for one marketing conversation and one utility conversation | Charged for one marketing message and one utility message |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

This update applies to marketing, utility, and authentication templates. Service conversations are free of charge as of November 1, 2024. 

*Note: This update was originally slated for April 1, May 1, and now **July 1**.* 

### Update 2: Utility templates sent during a 24-hour customer service window will be free of charge. 

#### How does this work? 

A [24-hour customer service window](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) is created when an end-user messages a brand. If your brand replies with a utility template, it will be free of charge. 

Utility templates sent outside of a 24-hour customer service window (for example, utility templates proactively sent by a brand for things like account reminders and order status updates) will still be charged. 

We recommend the following best practices to account for these changes and maximize your WhatsApp marketing budget: 

- Limit sending of multiple message templates of the same type (without a user response) in the 24-hour period. You won't be charged more than you previously were under the "per conversation" model. This is also a best practice to provide quality experiences for your customers and limit message fatigue. 
- Use [response messaging]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages/) when responding to end-user messages. Response messaging is free of charge. 

| Example scenario | Pricing before April 2025 | Pricing after April 2025|
| --- | --- | --- |
| - Brand sends marketing template <br>- User responds <br>- Brand replies with a response message | Charged for one marketing conversation | Charged for one marketing message |
| - User sends message to brand <br>- Brand replies with a response message | Free of charge <br> _Classified as a service conversation_ | Free of charge <br> _Classified as a service conversation_ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

We recommend the following best practices to account for these changes and maximize your WhatsApp marketing budget: 

- Limit sending multiple message templates of the same type (without a user response) in the 24-hour period. This prevents you from being charged more than you previously were under the "per conversation" model. This is also a best practice to provide quality experiences for your customers and limit message fatigue. 
- Use [response messaging]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) when responding to end-user messages. Response messaging is free of charge. 

*Note: This update was originally slated for April 1 and **now July 1**.* 

## WhatsApp pricing changes from August 2024 - November 2024

*Last updated October 29th, 2024*

### Utility conversations 

On August 1, 2024, Meta lowered rates on utility conversations to encourage brands to facilitate more post-purchase customer journeys on the platform. We have passed through these cost reductions to your Message Credits or WhatsApp Credits entitlements in equal proportions. This update went into effect on the same day as Meta’s (August 1). 

#### What are utility conversations? 

Utility conversations enable you to follow-up on specific customer actions or requests. Examples include opt-in confirmation, order updates and confirmations, account updates or alerts (e.g. payment reminders), or feedback surveys.

#### How can you benefit from this update? 

We encourage you to take advantage of this update by using WhatsApp for transactional messaging. You can also consider shifting some of your transactional SMS messages to WhatsApp if it makes sense for your brand (based on your audience reach and engagement on each channel). For example, this may be a good option for customers in Asia, Latin America, and Europe where WhatsApp is a heavily used channel. 

### Marketing conversations

On October 1, 2024, Meta decreased pricing on United Kingdom marketing conversations by 25% to reflect current demand. We have passed through these cost reductions to your Message Credits or WhatsApp Credits entitlements in equal proportions. This update went into effect on the same day as Meta’s (October 1).

#### What are marketing conversations? 

Marketing conversations enable you to achieve a wide range of goals, from generating awareness to driving sales and retargeting customers. Examples include new product announcements, targeted promotions/offers, and cart abandonment campaigns.

### Service conversations

On November 1, 2024, all service conversations are free of charge. Service conversations will no longer consume Message Credits or WhatsApp Credits entitlements. This change will go into effect on the same day as Meta’s (November 1).

#### What are service conversations? 

Service conversations enable you to respond to customer inquiries. This includes conversations started by an end-user where the brand replies with a [response message]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) instead of a template message.

#### How can you benefit from this update? 

Some conversations that were previously charged as "service" will now be free. These include: 

- [Unrecognized response campaigns]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) where an end-user sends a message that is unrecognized and the brand replies with a generic message using [response messaging]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages). For example, an end-user sends a message without a keyword and the brand responds with “We don’t recognize your message, please reach out to customer support."
- Conversations that start when an end-user messages the brand a promoted keyword and the brand replies using a [response message]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages). Common examples are opting into WhatsApp messaging or participating in a specific promotion.

<br>

Detailed information on the utility conversations decrease below:

| Billing region                             | Utility percent decrease |
|--------------------------------------------|--------------------------|
| Argentina                                  | 16.7%                    |
| Brazil                                     | 77.1%                    |
| Chile                                      | 65.9%                    |
| Colombia                                   | 97.6%                    |
| Egypt                                      | 92.4%                    |
| France                                     | 60.9%                    |
| Germany                                    | 35.5%                    |
| India                                       | 66.7%                    |
| Indonesia                                  | 0.0%                     |
| Israel                                     | 71.8%                    |
| Italy                                      | 28.6%                    |
| Malaysia                                   | 30.0%                    |
| Mexico                                     | 62.4%                    |
| Netherlands                                | 37.5%                    |
| Nigeria                                    | 79.0%                    |
| North America                              | 73.3%                    |
| Other                                      | 77.2%                    |
| Pakistan                                   | 78.7%                    |
| Peru                                       | 52.3%                    |
| Rest of Africa                             | 61.9%                    |
| Rest of Asia Pacific                       | 66.7%                    |
| Rest of Central & Eastern Europe          | 43.0%                    |
| Rest of Latin America                      | 77.1%                    |
| Rest of Middle East                        | 20.7%                    |
| Rest of Western Europe                     | 28.6%                    |
| Russia                                     | 16.1%                    |
| Saudi Arabia                               | 54.4%                    |
| South Africa                               | 62.0%                    |
| Spain                                      | 47.4%                    |
| Turkey                                     | 43.0%                    |
| United Arab Emirates                       | 20.7%                    |
| United Kingdom                             | 44.7%                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

To get a better understanding of how you can take advantage of these updates, reach out to your customer success manager. 
