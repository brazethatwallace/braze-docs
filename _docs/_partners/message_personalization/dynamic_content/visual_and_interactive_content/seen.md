---
nav_title: Seen
article_title: Seen
description: "Seen enables personalized video experiences at scale, helping brands drive higher engagement across the customer journey."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io) enables brands to create and deliver personalized video experiences at scale. With Seen, you can design a video around your data, personalize it at scale in the cloud, then distribute it where it works best.
>
> This integration sends user data from Braze to Seen, generates personalized videos, and returns assets—such as a unique player URL and thumbnail—to Braze for use in campaigns and Canvases.


## Use cases

Seen supports automated, personalized video delivery across the customer lifecycle, including:

- **Onboarding**: Welcome new users with videos personalized to their profile or signup context
- **Conversion and activation**: Reinforce key actions with contextual video messaging
- **Loyalty and upsell**: Highlight personalized offers or usage milestones
- **Win-back and churn prevention**: Re-engage inactive users with tailored video content


## Prerequisites

Before you begin, make sure you have the access and data in the following table.

| Prerequisite | Description |
|--------------|-------------|
| Seen Platform access | You need a Seen Platform subscription with a published project, or an active Seen campaign. You also need access to your project to retrieve the project endpoint and generate an API token. |
| Braze Data Transformation webhook URL | Use Braze Data Transformation to reformat incoming data from Seen so it can be accepted by Braze’s [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). |
| Braze user data | Video personalization requires user-level data. Ensure the relevant attributes are available in Braze, and pass **`braze_id`** as the unique identifier. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }




## How Seen projects work

Seen uses the [Run](https://docs.seen.io/run) tab in a project to control how incoming data is processed and how video outputs are generated.

A project workflow:

- Receives data from external systems (such as Braze)
- Applies logic and personalization rules
- Generates a video and associated assets
- Returns a configurable response payload

The Run tab includes the following:

- **Create via API**: Opens the Projects API details.
- **Import CSV**: Imports personalization data manually (not used in this walkthrough).
- **Add webhook**: Defines the response payload sent back to Braze.
- **View videos**: Shows generated videos and the status of incoming data.

Webhook responses are configurable, so align the output fields Seen returns with the attributes your Braze Data Transformation expects.


## Rate limit

The Seen API accepts 100 calls per 10 seconds.


## Integration

In this example, Braze sends user data to Seen to generate a personalized video. Seen then returns a unique video player URL and thumbnail URL, which you store as [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) in Braze for use in [messaging]({{site.baseurl}}/user_guide/messaging/).

If you run multiple video campaigns with Seen, repeat this process for each campaign.

### Step 1: Create a webhook campaign to send data to Seen

Create a new [Webhook Campaign]({{site.baseurl}}/user_guide/channels/webhooks/) in Braze.

Configure the webhook as follows:

- **Webhook URL**:  
  `https://next.seen.io/v1/projects/{PROJECT_ID}/data`  
  Find your project endpoint on the Run tab of your Seen Platform project.

- **HTTP Method**: POST

- **Request body**: Raw Text  
  Start from the following example. For field options and limits, see [Seen’s data creation documentation](https://docs.seen.io/create-data).

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}

- **Request headers**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  Generate an [API token](https://docs.seen.io/authorization) on the Run tab of your Seen Platform project. Contact your Seen Customer Success Manager if you need help.

- Test the webhook with a user on the **Test** tab.
- After a successful test, finish the webhook setup.


### Step 2: Configure a project in the Seen Platform

In your Seen project, use the [Run](https://docs.seen.io/run) tab to publish your video and register the outbound webhook. For a conceptual overview of the Run tab, see [How Seen projects work](#how-seen-projects-work).

1. In the Seen Platform, create a project, build your video, then select **Publish**. Videos start generating from incoming data as soon as the project is published.
2. On the Run tab, select **Add a webhook**.

#### Webhook response requirements

The response payload is configurable. Return the fields in the following table so the Braze Data Transformation in the next step can map them.

| Field | Description |
|-------|-------------|
| `id` | Must match the `braze_id` sent from Braze |
| `player_url` | Unique URL for the personalized video player |
| `email_thumbnail_url` | URL of the personalized video thumbnail |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook response requirements" }

If you need additional attributes, add them to the response and map them in Braze.


### Step 3: Create a data transformation to receive data from Seen

Use Braze Data Transformations to process the Seen response and store video assets on the user profile.

1. Create the following [custom attributes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) in Braze:
   - `player_url`
   - `email_thumbnail_url`

2. Go to **Data Settings** > **Data Transformations**, then select **Create transformation**.

3. Configure the transformation:
   - **Start from scratch**
   - **Destination** > POST: Track users

4. Share the generated webhook URL with Seen, or add it to the **Webhook** on your project's Run tab.

5. Use the following transformation code:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. Send a test payload to the provided endpoint. You can send data to your Seen Platform project (publish the project first), or send a payload directly to Braze using [Postman](https://www.postman.com/) or a similar tool.
7. Select **Validate** to verify the transformation works as expected.
8. Select **Save** and **Activate**.
