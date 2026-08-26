---
nav_title: Chord
article_title: Chord
description: "Connect the Chord customer data platform (CDP) to Braze to forward eCommerce events and identity updates for messaging, segmentation, and journeys."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> [Chord](https://www.chord.co/) provides a customer data platform that captures and standardizes events from your eCommerce storefront. When you connect Chord to Braze, purchase activity, behavioral events, and identity updates flow into Braze so you can trigger campaigns and keep profiles current without building those pipelines yourself.

_This integration is maintained by Chord._

For more information about setup, connection options, and field lists, see [Chord Braze integration](https://docs.chord.co/braze#chord-x-braze-integration).

## About the integration

Chord acts as the data layer between your store and Braze. After you connect Braze as a destination in the Chord CDP, Chord maps events from its tracking plan to Braze. Use that data in segments, Canvases, and message personalization to reflect what your consumers are doing on your site.

## Prerequisites

Before you connect Chord and Braze, confirm you have the following:

| Requirement | Description |
| ----------- | ----------- |
| Chord account | A Chord account is required to use this integration. |
| Braze API credentials | The credentials you need depends on your [connection mode](#connection-modes). Cloud mode uses a Braze REST API key. Device mode uses the Web channel API key for the Braze SDK, which is separate from your REST API key. |
| Braze REST endpoint | Chord sends server-side data to the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) and [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoints. Your base URL follows your Braze instance, for example, `https://rest.iad-01.braze.com`. For more information, see [Braze REST API endpoints]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Connection modes

Chord supports cloud mode (server-to-server calls through the Braze REST APIs) and device mode (Chord initializes the Braze Web SDK and forwards mapped calls). Choose the mode that fits whether you need full web SDK features (for example, in-app messages) or only server-side event forwarding.

### Cloud mode

1. In the Chord data platform, open the CDP and go to **Destinations**.
2. Select **Add** next to destinations, choose **Braze** from the catalog, then enter a destination name and your Braze REST API key.
3. Create the destination to finish connecting.

Create the REST API key in the Braze dashboard from **Settings** > **API Keys**. If you use the older navigation, go to **Developer Console** > **API Settings**. Unless Chord documents different requirements for your workspace, the key needs the `users.track` and `users.identify` permissions. For more information, see [API keys]({{site.baseurl}}/api/api_key).

### Device mode

1. In the Chord data platform, open the CDP and go to **Destinations**.
2. Select **Add** next to destinations, choose **Braze (device mode)** from the catalog, then enter a destination name and your Web channel API key.
3. Create the destination to finish connecting.

Use the Web channel API key from **Settings** > **App Settings** > **Web** > **API Key** in the Braze dashboard. Do not use your REST API key for device mode.

### Device mode configuration

In the Chord destination settings, configure the following:

- **Braze Web SDK version:** Chord exposes selectable SDK versions in the CDP; confirm the available range in Chord's documentation.
- **SDK endpoint:** Must match your Braze instance. For more information, see [API and SDK endpoints]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/).
- **Event and SDK options:** For example, which track or identify behaviors to send, page event handling, in-app message behavior, SDK initialization timing, and consent-related settings.

## Event mapping (device mode)

When you use device mode, Chord maps events to Braze as shown in this table:

| Chord | Braze |
| ----- | ----- |
| Order completed | `logPurchase` |
| Other `track` events | `logCustomEvent` |
| Identify | User updates (for example, attributes through the SDK user object) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Only events included in your Chord tracking plan and configured for the Braze destination are forwarded.

## Using the integration

### Step 1: Confirm events in Braze

After data flows, open user profiles or your event tooling in Braze to confirm events and attributes arrive as you expect.

### Step 2: Build audiences and journeys

Use synced events and attributes in [segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), [Canvases]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), and campaigns to target consumers based on store behavior.

## Use cases

- **Post-purchase messaging:** Trigger confirmations, cross-sell, or review requests when Chord receives completed orders.
- **Profile enrichment:** Keep Braze attributes aligned with the latest consumer profile data from Chord for cleaner segmentation.
- **Behavioral retargeting:** Re-engage consumers who have not purchased or converted recently using Chord behavioral events.

## Considerations

{% alert important %}
If another tool already sends the same events to Braze, coordinate with the owners of that integration before you connect Braze through the Chord CDP. Running parallel destinations can create duplicate events downstream.
{% endalert %}

## Troubleshooting

If events do not appear in Braze:

1. In the Chord CDP, confirm live events are arriving from your sources.
2. Verify the Braze destination uses the correct API key, SDK version (device mode), and REST or SDK endpoint for your instance.
3. Confirm the destination is attached to the expected source in Chord.
4. In Chord, review API destination or function logs for successful calls to `/users/track` and `/users/identify`, then check again in Braze.

For Chord-specific log locations and UI steps, see [Chord Braze integration](https://docs.chord.co/braze#chord-x-braze-integration).
