---
nav_title: API campaigns
article_title: API Campaigns
page_order: 5
description: "This reference article covers how to generate a campaign_id to include in your API calls and how to configure that campaign."
page_type: reference
tool: Campaigns
---

# API campaigns

> This reference article covers how to generate a `campaign_id` to include in your API calls and how to configure that campaign.

API campaigns are typically used for transactional messaging. When creating API campaigns (not [API-triggered campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)), the Braze dashboard is only used to generate a `campaign_id`, which lets you track analytics for campaign reporting. You can also generate a message variation ID, which is different for each variant in your campaign.

Send that information to your development team to use in the API request, along with:
- Campaign copy
- Audience membership
- Assets

After the campaign begins, you can view the results in the dashboard. API campaigns use the Braze [messaging APIs]({{site.baseurl}}/api/endpoints/messaging), which have the same detailed reporting and retargeting options as campaigns created completely through the dashboard.

{% alert warning %}
Because API campaigns are typically transactional, all users are eligible for API campaigns, even those in your Global Control Group. A [one-click list-unsubscribe]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe) header is not added to these sends by default. To add a one-click list-unsubscribe header to an API campaign, see [Add one-click list-unsubscribe to API campaigns](#add-one-click-list-unsubscribe-to-api-campaigns). To add a one-click list-unsubscribe header to all API campaigns, contact your customer success manager.
{% endalert %}

## Create a new campaign

Go to **Messaging** > **Campaigns** and select **Create Campaign**, then select **API Campaigns**. Now, you can move on to configuring your API campaign.

An [API-triggered campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) is different from an API campaign.

## Configure your campaign

To configure your campaign, perform the following steps:

1. Add a descriptive title so you can find the results on the campaigns page after you send your messages.
2. Select **Add Message** and add the message types included in your API campaign. This allows you to generate a `campaign_id` and a message variation ID, which differs for each channel you include.
3. Optionally, you can add a conversion event to track user conversions on a specific action or campaign goal.
4. Select **Save Campaign** to begin your API campaign.

## API calls

After you save your API campaign, include the following in your API request:

- The generated `campaign_id` fields with your API request where noted in the [Send Messages Endpoints]({{site.baseurl}}/api/endpoints/messaging).
- A [message object]({{site.baseurl}}/api/objects_filters#messaging-objects) for each platform included in the campaign. In the message object, provide the message variation ID. This specifies that statistics should be collected and displayed under that variant. The following message objects are supported: Android, Content Cards, email, iOS, Kindle, SMS/MMS, web push, and webhook.

## Add one-click list-unsubscribe to API campaigns

{% raw %}
By default, Braze does not add the one-click list-unsubscribe header to API campaigns. You can add this header to individual API campaign sends by including the `{{${set_user_to_one_click_list_unsubscribe}}}` Liquid tag in the email headers field of your API request.
{% endraw %}

To comply with [RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058) for one-click list-unsubscribe, include both the `List-Unsubscribe` and `List-Unsubscribe-Post` headers in your API request:

{% raw %}
```json
{
  "external_user_ids": ["user_id"],
  "messages": {
    "email": {
      "app_id": "your_app_id",
      "subject": "Your Subject",
      "from": "Sender Name <sender@example.com>",
      "body": "<p>Email body content</p>",
      "headers": {
        "List-Unsubscribe": "<{{${set_user_to_one_click_list_unsubscribe}}}>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
      }
    }
  }
}
```
{% endraw %}

{% alert note %}
The inclusion of these headers does not guarantee that the email client displays an unsubscribe button. Email clients decide whether to show the unsubscribe option based on factors such as sender reputation and message content.
{% endalert %}

### Add email attachments

To add attachments to API campaign emails, include an `attachments` array in the [email object]({{site.baseurl}}/api/objects_filters/messaging/email_object). You can reference an email template created in the drag-and-drop or HTML editor by providing its `email_template_id` in the email object, then add attachments through the API call.

For attachment details, size limits, and best practices, see [Example email object with attachment]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).


