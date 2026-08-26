---
nav_title: Create a Content Card
article_title: Create a Content Card
page_order: 1
description: "This reference article covers how to create, compose, configure, and send Content Cards using Braze campaigns and Canvases."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Create a Content Card

> This article covers how to create a Content Card in Braze when you build campaigns and Canvases. Here, we'll walk you through choosing a messaging type, composing your card, and scheduling your message delivery.

## Step 1: Choose where to build your message

Use campaigns for single, simple messaging (such as informing users about a product with one message). Use Canvases for multi-step user journeys (such as sending tailored product suggestions based on user behavior over time).

{% tabs %}
{% tab Campaign %}

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **Content Cards** or, for campaigns targeting multiple channels, select **Multichannel**.
3. Name your campaign something clear and meaningful.
4. Add [teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) and [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder), you can filter by the relevant tags.
5. Add and name as many variants as you like for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on variants, see [Multivariate and A/B testing]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
If all messages in your campaign are similar or have the same content, compose your message before adding additional variants. You can then select **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Create your Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) using the Canvas composer.
2. After setting up your Canvas, add a Message step in the Canvas builder. Name your step something clear and meaningful.
3. Select **Content Cards** as your messaging channel.
4. Choose when Braze calculates audience eligibility and personalization for the Content Card. This can be at step entry or at first impression (recommended). Steps containing Content Cards can be scheduled or action-based.
5. Choose whether to remove Content Cards when users complete a purchase or perform a custom event.
6. Set an expiration for the Content Card (time in feed). This can be after a duration of time or at a specific time.
7. Filter your audience, or the recipients, for this step as necessary in the **Delivery Settings**. You can further refine your audience by specifying segments and adding additional filters. Audience options are checked after the delay, at the time messages are sent.
8. Choose any other messaging channels that you want to pair with your message.

{% endtab %}
{% endtabs %}

## Step 2: Specify your message types

Select one of three essential Content Card types: **Classic**, **Captioned Image**, and **Image Only**. 

To learn more about the expected behavior and look of each type, see [Creative Details]({{site.baseurl}}/user_guide/channels/content_cards/creative_details), or check out the links in the following table. These Content Card types are accepted by both mobile apps and web applications.

| Message Type | Example | Description |
|---|---|---|
|[Classic]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![A Classic Content Card with a small icon and text to encourage booking a workout class.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |The Classic Card has a straightforward layout with a bolded title, message text, and an optional image that sits to the start of the title and text. It's best to use a square image or icon with the Classic Card. |
|[Captioned Image]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![A Captioned Content Card with a image of a weightlifter and text to encourage booking a workout class.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | The Captioned Image Card showcases your content with copy and an attention-grabbing image. |
|[Image Only]({{site.baseurl}}/user_guide/channels/content_cards/creative_details#content-card-types)| ![An Image Only Content Card with text only.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | The Image Only Card commands attention with space for images, GIFs, and other creative non-text content. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Specify your message types" }

## Step 3: Compose a Content Card

You can edit all aspects of your message's content and behavior in the **Compose** tab of the message editor.

![Sample Content Card details in the Compose tab of the message editor.]({% image_buster /assets/img/content_card_compose.png %})

The content here varies based on the **Card Type** chosen in the previous step, but may include any of the following options:

### Language

Select **Add Languages** to add your desired languages from the provided list. This inserts [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. For our full list of available languages you can use, see [Languages supported]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

![A window with English, Spanish, and French selected for the languages, and title, description, and link text selected for fields to internationalize.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

#### Create right-to-left messages

The final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, see [Creating right-to-left messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Title and message

Write anything you want. There are no limits, but the faster you can get your message across and get your customer clicking, the better! We recommend clear and concise titles and message content. Note that these fields aren't provided for Image Only Cards.

#### Image

To add an image to your Content Card, you can select **Add Image** or provide an image URL. Selecting **Add Image** opens the **Media Library**, where you can select a previously uploaded image or add a new one. 

Each message type and platform may have its own suggested proportions and requirements, so be sure to check what those are before commissioning or making an image from scratch. Keep in mind that Content Card message fields are limited to 2&nbsp;KB in total size.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Pin to top

Braze displays a pinned card at the top of a user's feed and the user can't dismiss it. If a user's feed has multiple pinned cards, Braze orders them chronologically. When Braze delivers a Content Card, it is either pinned or unpinned, and that status does not change for the lifetime of the card. If you change the pinned setting on a campaign, the update applies only to cards sent after the modification. It does not change the pinned status of cards already in a user's feed.

![Side-by-side of the Content Card preview in Braze for Mobile and Web with the option "Pin this card to the top of the feed" selected.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### On-click behavior

When your customer clicks on a presented link in the card, your link can either lead them deeper into your app or to another site. If you choose an on-click behavior for your Content Card, remember to update your **Link Text** accordingly.

The following actions are available for Content Card links:

| Action | Description |
|---|---|
| Redirect to Web URL | Open a non-native web page. |
| [Deep Link into App]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Deep link into an existing screen in your app. |
| Log Custom Event | Choose a [custom event]({{site.baseurl}}/user_guide/data/activation/events/custom_events) to trigger. Can be used to display another Content Card or trigger additional messaging. |
| Log Custom Attribute | Choose a [custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) to set for the current user. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="On-click behavior" }

The **Log Custom Event** and **Log Custom Attribute** options require the following SDK version compatibility:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Step 4: Configure additional settings (optional)

You can use [key-value pairs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) to create categories for your Cards, create [multiple Content Card feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds), and customize how cards are sorted.

To add key-value pairs to your message, go to the **Settings** tab and select **Add New Pair**.

## Step 5: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

Build the remainder of your campaign. Continue to the next sections for additional details on how to best use our tools to build Content Cards.

### Choose a delivery schedule or trigger

Content Cards can be delivered based on a scheduled time, an action, or an API trigger. For more, see [Scheduling your campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

You can also set the campaign's duration and [Quiet hours]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) and determine the Content Card's expiration. Set a specific expiration date or the days until a Card expires, up to 30 days. All variants must use the same expiration (duration or specific time).

The expiration countdown starts from the card's send time:

- **Scheduled campaigns:** The countdown begins at the scheduled launch time.
- **Action-based campaigns:** The countdown begins when the user performs the triggering action.

For example, if an action-based Content Card is sent at 2 pm today with a 1-day expiration, it expires at 2 pm the following day.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

For action-based delivery, there is an expected short delay before the Content Card appears. For details on why this happens and how to minimize it, see [Why don't Content Cards appear immediately after a trigger event?]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#why-dont-content-cards-appear-immediately-after-a-trigger-event).

#### Scheduled delivery

For Content Card campaigns with scheduled delivery, you can choose when Braze evaluates audience eligibility and personalization for new Content Card campaigns by specifying when the card is created. For more, see [card creation]({{site.baseurl}}/card_creation).

#### Choose users to target

Next, [target users]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) by choosing segments or filters to narrow your audience. You automatically receive a preview of what that approximate segment population looks like. Keep in mind that exact segment membership is always calculated before the message is sent.

{% multi_lang_include audience/target_audiences.md %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion is counted if the user takes the specified action.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For further details on how to build out the rest of your Canvas, implement [multivariate testing]({{site.baseurl}}/user_guide/messaging/ab_testing) and [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection), and more, see the [Build your Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) step of our Canvas documentation.

{% endtab %}
{% endtabs %}

## Step 6: Review and deploy

After you finish building your campaign or Canvas, review its details, [test it]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), then send it. For more information, see [Send test messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=content%20card).

{% alert note %}
While Content Cards do not require push notifications in production, test sends require push to be enabled on your test devices because the card is delivered in the push payload. Test Content Cards expire approximately five minutes after they are sent.
{% endalert %}

{% alert warning %}
After a Content Card is launched, it can't be edited. It can only be stopped from sending to new users and removed from users' feeds. Refer to [Updating sent cards]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) to understand how you can approach this scenario.
{% endalert %}

Next, check out [Content Card reporting]({{site.baseurl}}/user_guide/channels/content_cards/reporting) to learn how you can access the results of your Content Card campaigns.

## Things to know

### Payload and feed limitations

To support performance, Content Cards have two key constraints: a limit on the payload size for each card and a maximum number of cards that can appear in a feed.

#### Size limitations for Content Cards

The entire data payload for a single Content Card cannot exceed 2 KB **after** any Liquid personalization is rendered. This includes:

* Title
* Message
* Image URL (the length of the URL string itself, not the image file size)
* Link text
* Link URLs for all specified platforms (separate URLs for iOS, Android, and Web all count towards the total)
* Key-value pairs (both the key names and their values)

Using Liquid to pull in long strings of text (such as from custom attributes) can cause you to exceed the limit. 

The campaign composer displays a warning if your static content exceeds the limit. We do not predict the size for dynamic content using Liquid. If the message size exceeds 2 KB, it is aborted at send time. You can see these aborts in the Message Activity Log with the reason `Content card maximum size exceeded`.

{% alert important %}
During test sends, Content Cards that exceed 2 KB can still be delivered and displayed properly.
{% endalert %}

Here are some best practices for managing Content Card payload size:

* Use URL shorteners for long links. URLs, especially those with extensive tracking parameters, can run into size limit issues. Using a URL shortening service can dramatically reduce the character count and free up space in the payload.
* Truncate dynamic content with Liquid. When personalizing cards with dynamic text from user attributes or API calls, the length of the content can be unpredictable. Proactively use Liquid filters like `truncate` to cap the length of any dynamic text.
* Be efficient with multi-platform URLs. The 2 KB limit includes the URLs for all platforms you define. Using long, unique URLs for each platform can multiply the size of the payload. If possible, use a single link that works across all platforms, or use URL shorteners as needed.
* Consider Banners for richer content. For use cases that consistently require large amounts of content, Content Cards may not be the right channel. Banners do not have the same 2 KB payload limitation and are better suited for embedding richer content directly into an app or website experience.

#### Number of cards in feed

Each user can have up to 250 non-expired Content Cards in their feed at any given time. When this limit is exceeded, Braze stops returning the oldest cards, even if they are unread. Dismissed cards also count toward this limit, meaning a high number of dismissed cards can reduce the space available for older ones.

To prevent issues with the card limit, we advise the following best practices:

- **Use shorter expiration dates:** For campaigns that are time sensitive (such as a weekend sale), set a specific expiration date. This way, cards are automatically removed from the feed and no longer count toward the limit after they are no longer relevant.
- **Leverage action-based removal:** Set up removal events for transactional or goal-based cards. For example, a card prompting a user to complete their profile should be removed as soon as a `profile_completed` event is logged.
- **Audit long-running campaigns:** Review recurring or ongoing campaigns to ensure they aren't creating a poor experience for your users by filling the feed with too many cards over time.

### Understanding re-eligibility for Content Cards

Re-eligibility determines if and when a user can receive a message from the same campaign more than once. For Content Cards, understanding how this works is critical for managing recurring campaigns and ensuring users don't receive duplicate or stale messages.

{% alert tip %}
Do you want your content to last longer than 30 days? Try [Banners]({{site.baseurl}}/user_guide/channels/banners).
{% endalert %}

#### How re-eligibility is calculated

If you turn on re-eligibility, the countdown for when a user can "re-enter" a campaign begins after they are sent the message. The specific moment this countdown starts depends on your card creation settings:

- Content Cards using [at first impression]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences) use impression time to calculate re-eligibility.
- Content Cards created at campaign launch, in multichannel campaigns, or at Canvas step entry use whichever send time or impression time is latest.

#### The 30-day expiration and re-eligibility

A common source of confusion is the interaction between campaign re-eligibility and the automatic 30-day expiration of all Content Cards. 

All Content Cards are automatically purged from Braze's systems 30 days after they are sent or removed. If you have a long-running, recurring campaign with re-eligibility turned **off**, a user may still receive the same card again after 30 days. When the original card is purged, the system no longer sees a record of that user having received the campaign, making them eligible again on their next session. 

For users to only receive a message from a specific campaign once, add an audience filter to your campaign or Canvas step for users who have not received a message from this campaign. This filter is the most reliable way to prevent duplicate sends from long-running campaigns.

### Managing live Content Cards

After Content Cards have been sent, they sit waiting in an "inbox" ready to be delivered to the user (similar to what happens for emails). After content is pulled into the Content Card (at the time of display), it cannot be changed during its lifespan. This applies even if you're calling an API through Connected Content, and the data from the endpoint changes. This data is not updated. It can only be stopped from sending to new users and removed from users' feeds. If you modify a campaign, only cards sent after the modification include the update.

#### Updating launched cards

To change a card for users who have already received it, you must use one of the following methods:

##### Option 1: Duplicate the campaign (recommended for immediate changes)

{% alert tip %}
We recommend this option for messages where you are showing the latest content in the card, changes must be shown immediately, or when re-eligibility is turned off.
{% endalert %}

The first approach is to archive the campaign and launch a new, duplicated campaign:

1. Stop the original campaign and, when prompted, select `Remove card after the next sync`.
2. Duplicate the campaign, make your edits, and launch the new version.

When you duplicate the campaign, you need to define the audience for the new version. Use segmentation filters to control who receives the updated card:
* If users should never be re-eligible for a Content Card, you can filter for users who haven't received the previous version of the Content Card by setting the filter `Received Message from Campaign` to the condition to `Has Not`.
* If users who received the prior card should be re-eligible in X days, you can set the filter for `Last Received Message from specific campaign` to more than X days ago **OR** `Received Message from Campaign` with the `Has Not` condition.

###### Impact

- **Existing recipients:** New and existing recipients see the updated card at the next feed refresh if they are eligible.
- **Reporting:** Each version of the card has separate analytics.

Let's say you set a campaign to be triggered by a session start, and it has re-eligibility set to 30 days. A user received the campaign two days ago, and you want to change the copy. First, archive the campaign and remove the cards from the feed. Second, duplicate the campaign and re-launch with the new copy. If the user has another session, they immediately receive the new card.

##### Option 2: Stop and relaunch the same campaign

{% alert tip %}
We recommend using this option for unique messages in a notification center or message inbox (such as promotions), when it’s important for analytics to be unified, or when the timeliness of the message isn't a concern (such as existing recipients can wait for the eligibility window before seeing the updated cards).
{% endalert %}

This approach keeps all your analytics unified in a single campaign. Newly eligible users receive the new card, but it delays the update for existing recipients until they are re-eligible:

1. Stop your campaign and, when prompted, select **Remove card after the next sync**.
2. Edit your campaign as needed.
3. Restart your campaign.

###### Impact

* **Existing recipients:** Users who have already received the card do not receive the updated cards until they become re-eligible. If re-eligibility is turned off, they never receive the new card.
* **Reporting:** One campaign contains all reporting analytics for the card versions launched. Braze does not differentiate between the versions launched.

Let's say you have a campaign that's triggered by a session start and has re-eligibility set to 30 days. A user received the campaign two days ago, and you want to change the copy. First, stop the campaign and remove the card from the feed. Second, re-publish the campaign with the new copy. If the user has another session, they receive the new card in 28 days.

{% alert note %}
If you stop a campaign, edit the removal event settings, and restart the campaign without removing cards from the feed, any existing cards in users' feeds use the updated removal event settings. The cards don't retain the original removal event configuration from when they were first sent.
{% endalert %}

#### Removing and expiring cards

##### Manual card removal

You can manually remove cards for all users' feeds at any time by stopping the campaign.

1. Open the Content Card campaign and select Stop Campaign.
2. When prompted, select **Remove card after the next sync**. The card is removed on the next feed refresh.

##### Automated card removal {#action-based-card-removal}

You can automatically remove a card when a user performs a specific action, such as completing a purchase or activating a feature.

In your campaign or Canvas step, specify a removal event. When a user performs that event, the card is removed from their feed on a subsequent refresh after Braze processes the event. 

{% alert note %}
This removal is not instantaneous. There is a processing delay, so it may take several minutes and more than one feed refresh for the card to disappear.
{% endalert %}

{% alert tip %}
You can specify multiple custom events and purchases that should remove a card from a user's feed. When any of those actions are performed by the user, any existing cards sent by the campaign's cards are removed. Eligible cards continue to be sent according to the message's schedule.
{% endalert %}

![Content Card Removal Conditions panel with Content Card Removal Event option.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Card expiration

Content Cards remain available for up to 30 days from when they are sent; after 30 days, Braze removes them from user feeds and purges them from Braze's systems.

#### Making cards last longer than 30 days

{% alert tip %}
For use cases requiring messages to persist longer than the 30-day Content Card limit, consider using Banners. Banners are designed for persistence and do not have a mandatory expiration date, allowing them to stay visible as long as they are needed.
{% endalert %}

If you want a card to seem like it's always available, you can create a recurring campaign that effectively replaces the card every 30 days:

1. Set the duration of the Content Card for 30 days.
2. Set the campaign re-eligibility to 30 days.
3. Set the campaign to trigger on "Session Start."

### Content Card sync and refresh

Content Cards sync on a schedule and when your app refreshes the feed. Sync behavior differs between full and partial syncs, and your SDK integration affects when cards refresh at session start. For implementation details, see [Customize the Content Card feed]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) and [Creating Content Cards]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

### Impact of stopping Content Cards campaigns

When you stop a campaign and select **Remove card after the next sync**, Braze removes the card from user feeds on the next refresh. Impression counts may be lower than send counts because users cannot impress cards that are removed before they view them.

## Troubleshooting

### Why don't Content Cards appear immediately after a trigger event?

For action-based delivery campaigns (such as session start), there is an expected short delay between the trigger event and the card becoming available. This delay occurs because:

- The trigger event is flushed to Braze's servers
- The campaign is triggered and the user's eligibility is recorded
- The Content Card is created in the database for that user
- The SDK syncs and pulls all available cards to the device

If the SDK sync happens before the user's eligibility is recorded, the user does not receive the card.

For new users in their first session, this delay is unavoidable. For existing users who need instant availability, consider using scheduled delivery instead.

If you need to minimize delays for both new and existing users, you can create two campaigns:

- **Existing users with session count greater than 0:** Use a scheduled delivery campaign. Cards are pre-created and immediately available.
- **New users with session count equal to 0:** Use an action-triggered campaign. Cards are created after the first session trigger.

This approach ensures existing users see cards instantly while still reaching new users after a brief delay in their first session. For additional strategies to improve latency, see [Improve low latency for Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements).

### Why do impression or dismiss timestamps fall outside the campaign schedule?

Impression and dismiss timestamps in analytics and Currents reflect when a user views or dismisses a Content Card, not when Braze creates or sends the card. A card can remain in a user's feed until Content Cards are refreshed, so impression and dismiss timestamps can fall after the campaign's send window.

If times still look unexpected:

- Confirm whether you're viewing analytics in your company time zone versus the user's time zone in Currents.
- Check that the user actually viewed or dismissed the card after receiving it, rather than comparing against send time alone.

For more on Content Card metrics, see [Content Card reporting]({{site.baseurl}}/user_guide/channels/content_cards/reporting).

### "All expiration values for a campaign must match" error

This error appears when a multi-variant Content Card campaign uses different expiration settings across variants. Set the same expiration (duration or specific time) on every variant, or reduce the campaign to a single variant, then save again. For how to set expiration when building a campaign, refer to [Choose a delivery schedule or trigger](#choose-a-delivery-schedule-or-trigger).
