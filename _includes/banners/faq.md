# Frequently asked questions

> These are answers to frequently asked questions about Banners in Braze. For more general information, see [About Banners]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## When do Banner updates appear for users?

Banners are refreshed with their latest data whenever you call the refresh method&#8212;there's no need to resend or update your Banner campaign.

## How many placements can I request in a session?

In a single refresh request, you can request a maximum of 10 placements. For each one you request, Braze returns the highest-priority Banner a user is eligible for. Additional requests return an error.

For more information, see [Placement requests]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## How many Banner campaigns can be active simultaneously?

Each workspace can support up to 200 active Banner campaigns. If this limit is reached, you'll need to [archive or deactivate]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) an existing campaign before creating a new one.

## For campaigns sharing a placement, which Banner is displayed first?

If a user qualifies for multiple Banner campaigns that share the same placement, the Banner with the highest priority is displayed. For more information, see [Banner priority]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Can I use Banners in my existing Content Card feed?

Banners are different from Content Cards, meaning you can’t use Banners and Content Cards in the same feed. To replace existing Content Card feeds with Banners, you’ll need to [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/placements/).

## How are Banners different from in-app messages?

Banners and [in-app messages]({{site.baseurl}}/user_guide/channels/in_app_messages/) both reach users inside your app or website, but they use different delivery models. If you're comparing Banners to an existing in-app message setup, expect differences in triggers, refresh timing, and testing, not a one-to-one swap.

| Topic | Banners | In-app messages |
| --- | --- | --- |
| Where messages appear | Inline at [placements]({{site.baseurl}}/developer_guide/banners/placements/) you define in your app or site | Full-screen, modal, or slide-up overlays managed by the SDK |
| When content updates | When your app or site calls a Banner refresh (for example at session start or mid-session) | Templated messages evaluate Liquid when the in-app message is triggered (for example on a custom event or session start), after the payload is cached on the device |
| Action-based triggers | No [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery); use segments, priority, and refresh timing instead | Supports action-based and API-triggered delivery |
| Testing | Preview a user, then confirm the placement refresh in your app or site shows the expected Banner | Use **Test Send** or in-app preview flows for trigger-based display |
| Reporting | Banner views and clicks follow Banner analytics | In-app impressions and clicks follow in-app message analytics |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="How are Banners different from in-app messages?" }


## Can Banners include video?

The standard Banner builder supports images, text, and buttons. To include a video in a Banner, you can use a **Custom Code** block in the builder, or build the entire Banner with the HTML editor and embed a video player directly in your HTML.

## Can I trigger a banner based on user actions?

While Banners do not support [action-based delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), you can target users based on their past actions using segmentation and priority.

For example, to show a special Banner only to users who have completed a `purchase` event:
1. **Targeting:** In your campaign, target a segment of users who have performed the custom event `purchase` at least once.
2. **Priority:** If you have a general Banner for all users and this specific Banner for purchasers targeting the same placement, set the specific Banner's priority to **High** and the general Banner to **Medium** or **Low**.

When the user starts a new session or refreshes Banners after performing the action, Braze evaluates their eligibility. If they match the "Purchase" segment, the high-priority Banner is displayed.


## Can users dismiss a Banner?

Yes. You can allow users to manually dismiss a Banner. See [Configure dismissal behavior]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) for details on how to configure dismissal in both the builder and the HTML editor.

Users can manually dismiss Banners only if dismissal behavior is enabled. If dismissal isn't enabled, you can control Banner visibility by managing user segment eligibility. When a user no longer meets the targeting criteria for a Banner campaign, they won't see it again on their next session.

When a user dismisses a Banner, they're ineligible for that campaign by default. To let dismissed users see the Banner again, [configure re-eligibility]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#re-eligibility) in the campaign's **Delivery Controls** step. Canvas Banner steps use Canvas re-entry settings to control re-eligibility instead.

For example, if you display a promotional Banner until a user makes a purchase, logging an event such as `purchase_completed` can remove that user from the targeted segment, effectively hiding the Banner in subsequent sessions.

## Can I export Banners campaign analytics using the Braze API?

Yes. You can use the [`/campaigns/data_series` endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) to get data on how many Banner campaigns were viewed, clicked, or converted.

## When are users segmented?

Users are segmented at the beginning of the session. If a campaign's targeted segments depend on custom attributes, custom events, or other targeting attributes, they must be present on the user at the beginning of the session.

## How can I compose Banners to ensure the lowest latency?

The simpler the messaging in your Banner, the faster it renders. It’s best to test your Banner campaign against the expected latency for your use case. For example, be sure to test Liquid attributes like `catalog_items`.

If you use [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) (in early access), be aware that each call counts against a shared rendering budget of approximately two seconds across all placements in a single refresh. If the budget is exceeded or a call times out, the Connected Content result is treated as null, and Banners don't retry. To minimize latency:

- Keep your endpoints fast and [cache responses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/) whenever possible.
- Limit the number of unique Connected Content URLs across placements that render together.
- Avoid chaining calls where one Connected Content response determines the URL for the next.
- Use Liquid guard statements or the [`default` filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) to handle null results and avoid blank Banners.

## Are all Liquid tags supported?

No. However, most Liquid tags are supported for Banner messages, except for `catalog_items` that are re-rendered using the [`:rerender` tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Can I capture click events?

Yes. How click events are captured depends on how your Banner is rendered:

- **Builder — standard components:** If your Banner uses standard editor components (images, buttons, text), clicks are tracked automatically when using the SDK's insertion methods.
- **Builder — Custom Code blocks:** If you want to track clicks for elements within a Custom Code editor block, you must call `brazeBridge.logClick()` from within your custom HTML. This applies even when using the SDK methods to insert and render the Banner.
- **HTML editor:** Click tracking is not automatic. You must call `brazeBridge.logClick()` for every clickable element you want to track. For the full reference, see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/#javascript-bridge).
- **Custom UI (headless):** If you're building a fully custom UI using the Banner's custom properties instead of rendering the Banner HTML, call `logClick()` on the Banner object from your application code.

For more information, see [Logging clicks]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).
