---
nav_title: "Create a Banner"
article_title: "Create a Banner"
page_order: 1
description: "This reference article covers how to create, compose, configure and send Banners using Braze campaigns and Canvases."
tool:
  - Campaigns
channel:
  - banners
---

# Create a Banner

> Learn how to create Banners when you build campaigns and Canvases in Braze. For more general information, see [About Banners]({{site.baseurl}}/user_guide/channels/banners).

## Prerequisites

Before you can launch your Banner, your development team must [set up placements in your app or website]({{site.baseurl}}/developer_guide/banners/placements). You can still draft your Banner campaign in the meantime, but you won't be able to launch the campaign until the placements are configured.

## Create a Banner message

{% multi_lang_include banners/creating_placements.md section="user" %}

### Step 2: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, targeted messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **Banner**.
3. Name your campaign something clear and meaningful.
4. Add [teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) and [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) as needed. Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by the relevant tags.
5. Select the placement you previously created to associate it with your campaign.
6. Add variants as needed. You can choose a different message type and layout for each one. For more information on variants, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/messaging/ab_testing).
7. Choose a start date and time for your Banner campaign. By default, Banners last indefinitely. You can change this by selecting **End Time** and specifying an end date and time.

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then select **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Create your Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) using the Canvas composer.
2. After setting up your Canvas, add a Message step in the Canvas builder. Name your step something clear and meaningful.
3. Select **Banner** as your messaging channel.
4. Select a placement for the Banner.
5. Set the priority. The [Banner priority]({{site.baseurl}}/user_guide/channels/banners#priority) determines the order in which Banners are displayed if they share the same placement.
6. Set an expiration for the Banner. This can be after a duration of time after the step is available or at a specific date and time. The maximum expiration duration is 31 days after the step becomes available to the user.

{% endtab %}
{% endtabs %}

### Step 3: Compose a Banner {#compose-a-banner}

Next, choose how you want to start building:

- **Drag-and-drop editor:** Start with a blank Banner and build visually with blocks and rows.
- **HTML editor:** Start with a blank Banner and work directly in HTML.
- **Templates:** Open the template library and select a design from **Braze Templates** or **Your Templates**. Templates open in the drag-and-drop editor for customization.

![Options to choose the drag-and-drop editor, HTML editor, or Templates for your Banner.]({% image_buster /assets/img/banners/choose_banner_editing_experience.png %})

#### Step 3.1: Style the Banner

{% tabs %}
{% tab Drag-and-drop editor %}

You can drag and drop blocks and rows into the canvas area to start building your message. For a reference of Banner editor blocks and links to shared property details, see [Editor blocks (Banners)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=banners).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

To customize your message's background properties, border settings, and more, select **Styles**. If you only want to customize the style for a specific block or row, select it to make changes.

![Style panel of the Banner composer.]({% image_buster /assets/img/banners/banner_card_styles.png %})

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='banner' %}

{% endtab %}
{% tab HTML editor %}

The HTML editor is best for teams that already maintain their own HTML templates or want full control over markup and styling. You can write or paste custom HTML directly into the editor. Liquid personalization tags are fully supported, so you can reference user attributes, custom attributes, catalog items, and more.

{% alert tip %}
Need help building your Banner HTML? Select **Ask Operator** in the HTML editor and describe the Banner you want. [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/) generates HTML you can review and insert into the editor. For more information, see [Generate messages]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-messages).
{% endalert %}

For click and dismissal tracking in your custom HTML, you must call JavaScript bridge methods explicitly. For the full reference, see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/).

{% endtab %}
{% endtabs %}

{% alert note %}
To target users in different languages within a single Banner campaign, see [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
{% endalert %}

#### Step 3.2: Define on-click behavior (optional)

{% tabs %}
{% tab Drag-and-drop editor %}

When a user clicks a link in the Banner, you can choose to navigate them deeper into your app or redirect them to another webpage. Additionally, you can choose to [log a custom attribute or event]({{site.baseurl}}/developer_guide/analytics/), which updates your user's profile with custom data when they click the Banner. For more granular click tracking, assign a custom identifier to each interactive element using the **Identifier for Reporting** field in its properties panel.

{% alert important %}
{::nomarkdown}
On-click behavior can be overridden if a specific element (such as a button, link, or image, of the Banner) has its own on-click behavior. For example, given the following on-click behaviors:<br><ul><li>A Banner has an on-click behavior that redirects to a website's homepage.</li><li>An image in the Banner has an on-click behavior that redirects to a website's product page.</li></ul>If a user clicks the image, they are redirected to the product page. However, clicking the surrounding area in the Banner redirects them to the homepage.
{:/}
{% endalert %}

{% endtab %}
{% tab HTML editor %}

In the HTML editor, click tracking is not automatic. You must call `brazeBridge.logClick()` from within your HTML for each clickable element you want to track. For example:

```html
<a href="https://example.com" onclick="brazeBridge.logClick()">Shop now</a>
```

For the full JavaScript bridge reference, see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Step 3.3: Configure dismissal behavior (optional) {#dismiss-behavior}

{% alert important %}
Banner dismissals require the following minimum SDK versions. Older SDK versions do not render Banners with dismissal enabled.
{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 reactnative:22.0.0 flutter:20.0.0 %}
{% endalert %}

{% tabs %}
{% tab Drag-and-drop editor %}

Select the **Banner can be dismissed** checkbox in the **Dismiss behavior** section to allow users to dismiss the Banner. This is useful when you want to promote a limited-time offer to a broad audience but still let uninterested users hide the message.

When dismissal is turned on, you can customize the dismiss button in the **Dismiss behavior** section:

| Setting | Description |
|---------|-------------|
| **Button size** | The size of the dismiss button displayed on the Banner. |
| **Button color** | The color of the dismiss button. |
| **ARIA label** | The accessible label for the dismiss button, used by screen readers. Defaults to "Close" if left blank. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dismiss button settings" }

When a user dismisses a Banner, it doesn't appear again for that user, even if they still qualify for the campaign's targeting criteria.

{% endtab %}
{% tab HTML editor %}

In the HTML editor, dismissal is handled in your HTML using `brazeBridge.closeMessage()`. Pair it with `brazeBridge.logClick()` to also track the dismiss action as a click event. For example:

```html
<a href="#" onclick="brazeBridge.logClick(); brazeBridge.closeMessage();">&#x2715; Close</a>
```

When a user dismisses a Banner this way, it doesn't appear again for that user, even if they still qualify for the campaign's targeting criteria.

For the full JavaScript bridge reference, see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code/#javascript-bridge).

{% endtab %}
{% endtabs %}

#### Step 3.4: Add custom properties (optional) {#custom-properties}

You can add custom properties to a Banner to attach structured metadata, such as strings or JSON objects. These properties don’t affect how the Banner is displayed but can be [accessed through the Braze SDK]({{site.baseurl}}/developer_guide/banners/placements) to modify your app’s behavior or appearance. For example, you could:

{% multi_lang_include banners/metadata_use_cases.md %}

Custom properties work the same way in both the drag-and-drop editor and the HTML editor. To add a custom property, select **Settings** > **Properties** > **Add property**.

![The properties page showing the option to add the first custom property to a Banner campaign.]({% image_buster /assets/img/banners/add_property.png %})

For each property you'd like to add, fill out the following:

| Field | Description | Example |
|-------|-------------|---------|
| Property type | The data type for the property. Supported types include string, boolean, number, timestamp, image URL, and JSON object. | String |
| Property key | The unique identifier for the property. This key is used in the SDK to access the property. | `color` |
| Value | The value assigned to the property. Must match the selected property type. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 3.4: Add custom properties (optional) #custom-properties" }

When you're finished, select **Done**.

![The properties page with a string property with a key of color and value of #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

#### Step 3.5: Personalize with Connected Content (optional)

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content for Banners' %}

Because Banners render inline during a session refresh, Connected Content in this channel works differently than in other channels:

- Only GET requests are supported.
- All placements in a single refresh (up to 10) share a rendering budget of approximately two seconds. If a call is slow, times out, or the budget is exceeded, the Connected Content result for that placement is treated as null. Banners don’t retry.

For best results:

- Keep your endpoints fast and [cache responses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/) whenever possible.
- Limit the number of unique Connected Content URLs across the placements that render together.
- Avoid chaining calls where one Connected Content response determines the URL for the next. Each additional call adds to the shared budget.
- Use Liquid guard statements or the [`default` filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) to handle null results and avoid blank Banners.

### Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}

#### Set Banner priority (optional)

[Banner priority]({{site.baseurl}}/user_guide/channels/banners#priority) determines the order in which Banners are displayed if they share the same placement. To manually set the priority:

1. Select **Set exact priority**.
2. Drag and drop the campaigns to order them with the correct priority.
3. Select **Apply Sort**.

{% alert tip %}
If you have multiple Banner campaigns using the same placement ID, we recommend using the drag-and-drop priority sorter to define the exact priority.
{% endalert %}

#### Configure re-eligibility (optional) {#re-eligibility}

By default, users who dismiss a Banner are never re-eligible for that campaign. To let dismissed users see the Banner again, go to the **Delivery Controls** step and select **Allow users to become re-eligible to receive campaign**. When enabled, set a cooldown window in minutes, hours, days, or weeks.

The countdown starts from when the user dismisses the Banner. After the window expires, the user is automatically re-eligible—no campaign restart required. Re-eligibility is tracked per user per campaign.

#### Choose your audience

1. In **Target Audiences**, choose segments or filters to narrow your audience. You automatically receive a preview of the approximate segment population. Exact segment membership is calculated before the message is sent.

{% multi_lang_include audience/target_audiences.md %}

{:start="2"}
2. In **Assign Conversions**, track how often users perform specific actions after receiving a campaign by defining conversion events with up to a 30-day window to count the action as a conversion.

#### Choose conversion events

Braze allows you to track [conversion events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), how often users perform specific actions, after receiving a campaign. You have the option of allowing up to a 30-day window during which a conversion is counted if the user takes the specified action.

{% endtab %}

{% tab Canvas %}

If you haven't done so already, complete the remaining sections of your Canvas component. For details about building the rest of your Canvas, including multivariate testing and **Optimize with BrazeAI™**, see [Build your Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

To control re-eligibility for Canvas Banner steps, use the Canvas re-entry settings. For more information, see [Re-eligibility for campaigns and Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

{% endtab %}
{% endtabs %}

### Step 5: Test your message (optional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Step 6: Review and deploy

After you've finished building your campaign or Canvas, review its details, [test it]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), then send it when you're ready.
