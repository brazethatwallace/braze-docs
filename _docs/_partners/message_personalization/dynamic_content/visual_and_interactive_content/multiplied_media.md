---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Learn how to use Multiplied Media with Braze to send personalized images, GIFs, and video through email, push notifications, in-app messages, Content Cards, and WhatsApp."
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> [Multiplied Media](https://multiplied.media) is a creative and automation studio that uses your CRM data to create personalized images, GIFs, and video—a unique asset for each customer. The Multiplied Media and Braze integration lets you send this media through email, push notifications, in-app messages, Content Cards, and WhatsApp.
>
> Multiplied Media is a managed service, not a software tool. The Multiplied Media team handles concept, design, animation, data connection, and rendering. To use this integration, insert a media URL with a [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) merge tag into your campaign or Canvas.

_This integration is maintained by Multiplied Media._

## About this integration

The Multiplied Media team works with you from first concept to launch. They design and animate media for your brand, connect your data, and automate rendering. You do not need to learn new software.

The integration connects your Braze data—customer attributes and segments—to Multiplied Media. Multiplied Media renders a unique media asset for each customer and hosts it at a URL that contains that customer's identifier. You reference that URL in your Braze message with a Liquid merge tag. Each customer then sees their own image, GIF, or video.

The integration supports two flows:

- **Batch campaigns:** Send data by CSV, S3, or API. Multiplied Media renders and hosts all media before send.
- **Real-time Canvas automations:** A [webhook]({{site.baseurl}}/user_guide/channels/webhooks/) step in your Canvas triggers rendering when a customer reaches that step.

## Use cases

- **Personalized campaigns:** Product launches, "wrapped" and year-in-review campaigns, seasonal promotions, and personal data visualizations.
- **Always-on automations:** Welcome flows, onboarding, milestone celebrations, win-back emails, abandoned cart, shipping notifications, back-in-stock alerts, and loyalty updates.
- **Omnichannel journeys:** One concept, rendered for every channel. The same customer data can become an email hero image, a push image, an in-app visual, and a WhatsApp video—so a journey keeps one visual identity across every touchpoint.

## Prerequisites

The Multiplied Media architecture supports batch-based campaigns through S3 or API and real-time Canvas automation through webhooks. By pre-generating and hosting unique media assets ahead of delivery, Multiplied Media ensures seamless one-to-one visual experiences are ready to merge into your templates with Liquid tags or custom attributes the moment your message triggers.

Before you start, confirm you have the following:

| Requirement | Description |
| --- | --- |
| Active Multiplied Media engagement | Multiplied Media is a managed service. Before you begin in Braze, the Multiplied Media team scopes your campaign, designs and builds your media templates, and sets up rendering. To start, visit [multiplied.media](https://multiplied.media) or email [hello@multiplied.media](mailto:hello@multiplied.media). |
| Data source | Connect your customer data to Multiplied Media by CSV, S3, API, or Braze webhooks. The Multiplied Media team sets this up with you during onboarding. |
| Unifying identifier | Your data must include an identifier shared between Braze and Multiplied Media, such as `external_id`. This identifier forms part of each customer's media URL, and your Braze message references it with Liquid. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Use Multiplied Media with Braze

Multiplied Media designs, builds, and renders your personalized media and helps you connect your data. The following steps are what remains to do in Braze.

### Step 1: Confirm your media is ready

Before launch, the Multiplied Media team confirms that your media is rendered (batch campaigns) or that your rendering endpoint is live (real-time Canvas flows). They then provide your campaign's media URL. For example:

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

The identifier in the URL path is the unifying identifier agreed during setup.

### Step 2: Insert the URL into your campaign or Canvas

Paste the Multiplied Media URL—with the Liquid merge tag—into the field for your channel:

- **Email:** The image source in your email template.
- **Push notifications:** The image field of your push message.
- **In-app messages and Content Cards:** The media field.
- **WhatsApp:** The media header field.

For real-time Canvas automations, add the Multiplied Media webhook step (set up with you during onboarding) along with a delay node before your message step. This ensures the media is rendered for each customer before delivery.

### Step 3: Preview, test, and launch

Use Braze previews and test sends to confirm that the Liquid tag resolves and that each test user sees their own media. The Multiplied Media team reviews test sends with you before launch.

## Considerations

- Each customer's media asset is unique. If a customer is not in the connected data source, the URL serves a default (fallback) version of the media instead. Multiplied Media designs the fallback as part of every engagement.
- Multiplied Media renders and hosts assets before delivery; it does not render them at open time. The media loads immediately at open and shows the customer's data as of render time. If the data must be current at the moment of send—for example, in triggered Canvas flows—use the real-time webhook step.
- For scheduled batch campaigns, your data must reach Multiplied Media before send time so they can render all assets. Your Multiplied Media team agrees the cut-off time with you during setup.

## Troubleshooting

Multiplied Media is a managed service, so your Multiplied Media team is your first line of support. Contact them at [hello@multiplied.media](mailto:hello@multiplied.media).

Refer to the following table if your dynamic image does not display.

| Issue | Resolution |
| --- | --- |
| Dynamic image does not display | Confirm the Liquid tag in the URL matches the unifying identifier agreed during setup (for example, `user_id` versus a custom attribute). Confirm the customer exists in the connected data source. If the identifier resolves but no personalized asset exists, the fallback media is displayed. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }
