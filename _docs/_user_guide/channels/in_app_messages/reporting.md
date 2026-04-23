---
nav_title: Reporting
article_title: In-App Message Reporting
page_order: 21
description: "This reference article covers in-app message reporting and analytics including campaign details, message performance, and historical performance."
channel:
  - in-app messages
tool:
  - Reports

---

# In-app message reporting {#iam-reporting}

> This reference article covers in-app message reporting and analytics including campaign details, message performance, and historical performance.

{% multi_lang_include analytics/campaign_analytics.md channel="in-app message" %}

## In-app message metrics

Here are the key in-app message metrics you may see in your analytics. For definitions of all metrics used in Braze, refer to the [Report Metrics Glossary]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

| Term | Definition |
| --- | --- |
| Unique impressions | The total number of people who actually received and viewed the in-app message. If a user receives the message more than once on the same calendar day in your workspace's time zone, only one unique impression counts that day. <br><br> **If re-eligibility is on:** Unique impressions can increment again on a new calendar day in your workspace's time zone if the user performs the trigger action again. For in-app messages, *Unique Impressions* equals *Unique Recipients* because both increment on a new calendar day. |
| Impressions | The number of users whose devices reported that the message had been delivered. If a user receives the message twice, they are counted twice. <br><br> **If there are multiple devices and re-eligibility is off:** The user only sees the in-app message once. Even if the user uses multiple devices, they only see it on the first device targeted. This assumes the profile has consolidated devices and the user has one user ID logged in across devices. <br><br> **If re-eligibility is on:** An impression is logged for every time the user sees the in-app message. <br><br> **Note:** *Total Impressions* counts each view. *Unique Recipients* is a separate metric tracked using a calendar-day boundary in your workspace's time zone. |
| Conversions | Conversion tracking starts after a user logs an impression of an in-app message. A conversion is counted if the user has received and viewed the in-app message campaign and subsequently performs the specific conversion event within the defined conversion window, regardless of whether they clicked on the message or not. <br><br> Conversions are attributed to the most recently received message. If re-eligibility is enabled, the conversion is assigned to the latest in-app message received, provided it occurs within the defined conversion window. However, if the in-app message has already been assigned a conversion, a new conversion cannot be logged for that specific message. This ensures that each in-app message delivery is associated with only one conversion. |
| Total conversions | When a user views an in-app message campaign only once, only one conversion is counted, even if they perform the conversion event multiple times later on. However, if re-eligibility is turned on and the user sees the in-app message campaign multiple times, *Total Conversions* can increase once for each time the user logs an impression for a new instance of the in-app message campaign. <br><br> For example, if a user triggers an in-app message twice and converts after each impression (resulting in two conversions), *Total Conversions* increases by two. However, if there was only one impression followed by two conversion events, only one conversion is logged and *Total Conversions* increases by one. |
| Conversion rate | The metric of total daily unique impressions (*Unique Impressions*) is used to calculate the conversion rate. <br><br> Conversion Rate = (Primary Conversions) / (Unique Impressions) <br><br> Impressions for in-app messages can only be counted once per day. The number of times a user completes a desired action (a "conversion") can increase within a 24-hour period. While conversions can happen more than once per day, impressions cannot. Therefore, if a user completes a conversion multiple times within a day, the *Conversion Rate* can increase accordingly, but impressions are only counted once. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## How do conversions increment with re-eligibility?

Each in-app message delivery can only have one conversion event assigned to it, and the conversion is attributed to the last received message.

If a user converts five times after seeing an in-app message, only one conversion event is counted for that message. However, if a user sees the same in-app message five times in a single day and converts after each impression, five conversions are counted. The conversion event is attributed to the most recent in-app message sent.

If a user sees an in-app message on two separate days but only converts on the third day, the conversion is logged for the second day's impression. Only one conversion can be assigned to each step in a Canvas after the user has received that step.

{% details Expand for example scenarios %}

#### Scenario 1

*A user receives the same in-app message five times in a single day and converts five times that same day.*

Sarah receives an in-app message from a shopping app about a limited-time sale on her favorite brand of shoes. She clicks on the message and purchases two pairs of shoes.

A few hours later, she receives the same in-app message again and decides to buy another pair of shoes. This happens a total of five times in a single day, and Sarah ends up making five separate purchases, each time after clicking on the in-app message.

**Results:** *Total Conversions* for Sarah increments by five for that single day. Because in-app message impressions can only increment after a calendar day boundary in the workspace's time zone, *Total Impressions* remains the same. This causes the *Conversion Rate* to increase within that period.

{% alert note %}
Each impression and conversion in this scenario is processed as a separate SDK event. If your SDK batches an impression and a conversion event together, the conversion count may differ.
{% endalert %}

#### Scenario 2

*A user receives one in-app message and converts in a single day.*

Lena receives an in-app message about a new learning course. She clicks on the message and starts the course. While in the app, she also signs up for four more courses. This all happens on the same day after receiving only one message.

**Results:** *Total Conversions* and *Total Impressions* for Lena each increment by one.

#### Scenario 3

*A user receives an in-app message and converts one day later.*

Tom is a regular customer of an eCommerce app. He receives an in-app message promoting a limited-time discount on a product he's been interested in. Tom clicks on the message but decides not to buy right away. The next day, Tom remembers the discount and makes the purchase, which is attributed to the in-app message he received the day before.

**Results:** *Total Conversions* and *Total Impressions* for Tom each increment by one.

#### Scenario 4

*A user receives an in-app message and converts twice one day later.*

Alex recently downloaded an arcade app. One day, Alex receives an in-app message encouraging them to complete a level in a new game. Alex clicks the message but gets distracted and doesn't complete a level. The next day, Alex completes two levels in the same game.

**Results:** Since completing a level is the conversion event, Alex converted twice on the second day. However, because they only received one in-app message, *Total Conversions* and *Total Impressions* for Alex each increment by one.

#### Scenario 5

*A user receives the same in-app message twice in a single day and converts twice the following day.*

John is a busy professional who relies on a delivery app to order food from his favorite restaurants. On his commute to work, he triggers a geofence and receives an in-app message promoting nearby restaurants. When he heads home later, he receives that same message again because re-eligibility is on. Although he likes the offers, he decides not to order anything that day.

The next day, John orders lunch and dinner through the app, performing the conversion event twice.

**Results:** *Total Conversions* for John increments by one, and *Total Impressions* increments by two. Because re-eligibility is on, the conversion is assigned to the latest in-app message John received (the second impression). A conversion can only be logged once for each in-app message delivery.

{% enddetails %}

