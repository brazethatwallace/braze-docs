---
nav_title: "Subscription groups"
article_title: SMS and RCS Subscription Groups
page_order: 4
description: "This reference article covers subscription groups, subscription states, and the subscription group setup process for SMS, MMS, and RCS channels."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# SMS, MMS, and RCS subscription groups

> Subscription groups are the foundation for sending SMS, MMS, and RCS messages through Braze. A subscription group is a collection of [sending entities]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) (such RCS-verified senders, SMS short codes, SMS long codes, or SMS alphanumeric sender IDs) that are used for a specific type of messaging purpose. For example, if a brand has plans to send both transactional and promotional SMS messaging, two subscription groups with separate pools of sending phone numbers will need to be set up within your Braze dashboard.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Subscription group states

There are two subscription states for SMS and RCS users: `subscribed` and `unsubscribed`. A user's subscription state resides at the subscription group level and is not shared across subscription groups, meaning a user can be `subscribed` to a transactional subscription group but `unsubscribed` to a promotional one. For brands, this separation of states ensures that they can continue to send relevant SMS and RCS messages to their users.

| State | Definition |
| --------- | ---------- |
| Subscribed | User is subscribed to receive SMS and RCS from a specific subscription group. A user can be subscribed either by having their subscription state updated through the Braze subscription API or by texting an opt-in keyword response. A user must be subscribed to an SMS or RCS subscription group to receive SMS, RCS, or both. When [double opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) is enabled, users must confirm their opt-in intent before their subscription status updates to `Subscribed`. |
| Unsubscribed | User has explicitly opted out of messaging from your SMS and RCS subscription group and the sending phone numbers inside the subscription group. They can unsubscribe by texting an opt-out keyword response or you can unsubscribe users through the [Braze subscription API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Users unsubscribed from an SMS and RCS subscription group will no longer receive any SMS or RCS from sending phone numbers that belong to the subscription group.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription group states" }

### Set a user's state

When a phone number is updated on a user profile, the new phone number inherits the subscription group status of the user. If the phone number is updated to a number that already exists in Braze, the subscription status of that existing phone number is inherited.

For example, if User A has a phone number that is subscribed to several subscription groups and that phone number then gets added to User B, User B will be subscribed to the same subscription groups. To prevent a user from inheriting the existing subscriptions, you can reset the subscription groups of the old number through the Braze REST API whenever a user changes their number. If multiple users share this phone number, they will all be unsubscribed.

To set a user's subscription group state, use one of the following methods:

- **REST API:** User profiles can be programmatically set by the [`/subscription/status/set` endpoint]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) by using the Braze REST API.
- **SDK Integration** Users can be added to an email or SMS and RCS subscription group using the `addToSubscriptionGroup` method for [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)), or [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Phone Number Capture IAM Form:** User phone numbers can be collected through the phone number capture template in the in-app message drag-and-drop editor.
- **Automatically handled upon user opt-in/opt-out:** By users texting a default opt-in or opt-out [keyword]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout), Braze automatically sets and updates users' subscription state.
- **User import**: Users can be added into email or SMS and RCS subscription groups through **Import Users**. When updating subscription group status, you must have these two columns in your CSV: `subscription_group_id` and `subscription_state`. Refer to [User import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) for more information.

#### Update a user's state in a Canvas

When updating a user's subscription group status as part of a Canvas flow, use a [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) step instead of a webhook. The User Update step waits for processing to complete before advancing the user to the next step, so subsequent messaging steps use the updated subscription status.

If you use a webhook to update subscription groups, the user advances as soon as the webhook is sent—not when the subscription change finishes processing. This can create a race condition where a follow-up SMS step executes before the user is subscribed, causing the message to fail for a portion of users. If you must use a webhook, add a Delay step of at least 1 minute before the next messaging step.

#{% multi_lang_include api/orphaned_subscription_states.md %}

### Check a user's group

To check a user's subscription group, use one of the following methods:

- **User Profile:** Individual user profiles can be accessed through the Braze dashboard by selecting **User Search** from the sidebar. Here, you can look up user profiles by email address, phone number, or external user ID. When inside a user profile, under the Engagement tab, you can view a user's SMS and RCS subscription groups. 
- **Rest API:** Individual user profiles subscription group can be viewed by the [List user's subscription groups endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) or [List user's subscription group status endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) by using the Braze REST API. 

## Send messages with a subscription group

To launch an SMS or RCS campaign through Braze, select a subscription group from the **SMS/MMS/RCS Variants** dropdown. After it's selected, an audience filter will be added to your campaign or Canvas automatically, ensuring that only users `subscribed` to the selected subscription group are in the target audience.

{% alert important %}
In adherence with international [telecommunication compliance and guidelines]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), Braze will never send SMS or RCS to users that have not subscribed to the selected subscription group.  
{% endalert %}

![SMS composer with the subscription group dropdown open and "Messaging Service A for SMS" highlighted by the user.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## SMS subscription group best practices

Design separate SMS subscription groups for each messaging purpose (for example, transactional versus marketing) and for each workspace. When you operate in multiple countries, consider separate groups by region to support local compliance rules—for example, Brazil's restrictions on promotional send windows.

## Enable subscription groups

To enable subscription groups for SMS, MMS, or RCS, refer to the following:

{% tabs local %}
{% tab SMS %}
During your SMS onboarding process, a Braze onboarding manager will set up subscription groups for your dashboard account. They will work with you to determine how many subscription groups you need and add the appropriate sending phone numbers to your subscription groups. Timelines for setting up a subscription group will depend on the type of phone numbers you're adding. For example, short code applications can take anywhere between 8-12 weeks, while long codes can be set up within a day. If you have questions about your Braze dashboard setup, contact your Braze representative for support.  
{% endtab %}

{% tab MMS %}
In order to send an MMS message, at least one number within your subscription group has to be enabled to send MMS. This is indicated by a tag located next to the subscription group. 

![Subscription Group dropdown with "Messaging Service A for SMS" highlighted. The entry is prefixed with the tag "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
An RCS-verified sender must be present within your subscription group before you can send an RCS message. 

There are two ways to add an RCS-verified sender:
- Add it to an existing subscription group
- Create a new RCS subscription group
The choice largely depends on the RCS use cases you are interested in. 

Depending on your integration, Braze can add RCS-verified senders to your existing SMS subscription groups or set up new subscription groups for you. In either case, your customer success manager will guide you through a seamless and efficient SMS traffic upgrade.
{% endtab %}
{% endtabs %}

## Handle natural language opt-outs in the Agent Console

For comprehensive subscription management, you can capture opt-out intent that falls outside of standard or custom keywords (such as "Please don’t text me"). By creating an AI agent, you can use sentiment analysis to help identify and act on these requests automatically.

### Setup

1. In the [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents), create an "SMS Sentiment Analysis Agent".

{% alert tip %}
Use [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) to assist with the initial agent configuration.
{% endalert %}

{: start="2"}
2. Create an action-based Canvas triggered by **Send an SMS inbound message**, within the **Other** keyword category.
3. Add the [Agent step]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) to the Canvas to identify opt-out intent.
4. Add a subsequent SMS [Message step]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) to confirm the request: "It looks like you're trying to unsubscribe from SMS, so we are going to unsubscribe you. If this is a mistake, text START to opt back in."
5. Add a [User Update step]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) to change the user's status in the specific SMS subscription group to "Unsubscribed."

{% alert note %}
Using the Agent Console consumes Message or Action Credits.
{% endalert %}

## Migrate SMS traffic to RCS

If you have separate SMS and RCS subscription groups, you can migrate users from SMS to RCS using a one-step Canvas. 

Braze recommends that you test sending RCS to smaller volumes of users initially and migrate more users to the RCS subscription group over time. For example, if you have 1,000,000 users subscribed to an SMS subscription group, this could look like first migrating all users to the new subscription group and then segmenting on a smaller audience of 50,000 to 100,000 (5-10%) to test the RCS messages.

### Step 1: Create a Canvas and fill out the Entry Schedule

Create a Canvas and name it something easily identifiable (such as “SMS-RCS Subscription Group User Transfer”). Then, schedule the campaign whenever is convenient for you.

### Step 2: Define your audience
{: #step-2-define-your-audience}

Define your audience using one of the following methods. Next, go to the **Send Settings** step and select **Users who are subscribed or opted-in**.

| Method                          | Description                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Create a segment**         | Build a segment that includes all users in a subscription group or a subset using segmentation filters (such as a random 5-10%). Segments update before each send to reflect your current user base.        |
| **Apply campaign or Canvas filters** | Refine the audience in the **Target Audience** step of your campaign or Canvas. Adjust targeting options without leaving the page for added flexibility.                                         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Define your audience" }

### Step 3: Configure a User Update step

Add a User Update Step to your Canvas. In the step, open the **Advanced JSON Editor** and input the following (for the unique user identifier field, we recommend using the `braze_id` field):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

!["User Update Object" that contains the previously stated JSON code.]({% image_buster /assets/img/sms/user_update_object.png %})

### Step 4: Test the Canvas

We highly recommend [testing your Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) to confirm it works as expected before sending it to your broader audience.

### Step 5: Launch your Canvas

After you have successfully tested your Canvas, go ahead and launch it for your subset of users!

To confirm that your users were successfully migrated, we recommend checking a few individual user profiles that were updated. In the **Engagement** tab, look for **Contact Settings** and scroll to view the subscription groups the user is subscribed to. The RCS subscription group toggle should now be on.

For RCS sender and subscription group setup, also refer to [Set up RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Best practices

### Designate separate subscription groups

- **Messaging type:** Create distinct subscription groups for each type of messaging, such as Transactional and Marketing.
- **Workspace:** Create distinct subscription groups for each workspace to maintain clarity and organization.

Consider the following example with four subscription groups across two workspaces:

- **Production workspace**
  - Marketing - PROD for SMS
  - Transactional - PROD for SMS
- **Development Workspace (for testing)**
  - Marketing - DEV for SMS
  - Transactional - DEV for SMS

### Use clear naming conventions

Choose descriptive and clear subscription group names so that the correct group is selected when creating SMS campaigns.

### Separate groups by country

SMS regulations vary by country. We suggest separating SMS subscription groups by country. This helps you meet compliance standards in all regions where you send messages.

For each subscription group, you can also configure a country allowlist under **Geographic Permissions** so SMS, MMS, and RCS are only sent to approved regions. For more information, see [Geographic permissions]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

For example, in Brazil, sending marketing messages outside the hours of 9 am and 9 pm local time is prohibited, and the country spans three time zones. To comply with these regulations, you might set up separate groups for sending messages to Brazil and the United States. This prevents users in Brazil from receiving marketing messages during prohibited hours.
