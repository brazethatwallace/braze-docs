Effective July 1, 2025, WhatsApp now bills per-message. Message rates are based on both the country code of the recipient's phone number and the type of message you're sending. The message type is determined from the [message template](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) you submit for approval in WhatsApp Manager.

{% alert note %}
All business-initiated conversations on the platform must start with an approved template message. 
{% endalert %}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Message template definitions

These are the message templates you can submit for approval in WhatsApp Manager:

| Template | Definition |
|----------|------------|
| **Marketing template**     | This template let's you to achieve a wide range of goals, from generating awareness to driving sales and retargeting customers. Examples include new product, service, or feature announcements, targeted promotions or offers, and cart abandonment reminders. |
| **Utility template**       | This template let's you to follow up on user actions or requests, since these messages are typically triggered by user actions. Examples include opt-in confirmation, order or delivery management (such as delivery updates), account updates or alerts (such as payment reminders), or feedback surveys.<br><br>Effective July 1, 2025:<br>• Utility templates must be non-promotional without any persuasive intent.<br>• Utility templates must be either (1) specific to or requested by the user or (2) essential or critical to the user. |
| **Authentication template** | This template let's you to verify a user’s identity, potentially at various steps of the customer journey (such as account verification, account recovery, and integrity challenges).<br><br>Authentication conversations will only be supported on a case-by-case basis and Braze cannot guarantee specific SLAs. Additionally, Braze does not support PIN generation. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Types of free messages

Here's a few different scenarios when your WhatsApp message will be free of charge:

|Message|Details|
|-------|-------|
|All service conversations|_Effective November 1, 2024_<br><br>When a user messages your brand (starting the 24-hour customer service window), non-templated response messages are not charged. Note: If your brand responds to the user with a template, however, you will still be charged based on the template type.|
|Utility templates sent during a 24-hour customer service window|_Effective July 1, 2025_<br><br>A 24-hour customer service window is created when an end user messages your brand. If your brand replies with a utility template, it will be free of charge. Utility templates sent outside of a 24-hour customer service window (e.g. utility templates proactively sent by your brand for things like account reminders and order status updates) will still be charged.|
|Free entry point conversations|A free entry point conversation is opened if 1) a user messages your brand via a Click to WhatsApp Ad or Facebook Page Call-to-Action button and 2) your brand responds within 24 hours. The free entry point conversation is opened as soon as your brand responds and lasts 72 hours. Within the 72-hour window, your brand can send message templates to users free of charge. However, your brand can only send non-templated messages if there is an open 24-hour customer service window.|
|Response messages|Response messaging allows your brand to send non-templated messages in response to user messages. Response messages can be sent when there is an open 24-hour customer service window, like when a user messages your brand on WhatsApp.<br><br>Keep in mind, the template message that starts the conversation will still be charged, but subsequent response messages will be free of charge.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}