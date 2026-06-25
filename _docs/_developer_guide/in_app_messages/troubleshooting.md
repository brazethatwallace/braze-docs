---
nav_title: Troubleshooting
article_title: Troubleshoot in-app messages for the Braze SDK
page_order: 50
description: "Diagnose why in-app messages aren't delivered or displayed using a symptom index, standard investigation path, Canvas IAM callouts, and platform-specific SDK checks."
channel:
  - in-app messages

---

# Troubleshoot in-app messages

> Use this page to diagnose why in-app messages aren't delivered or displayed on a device. For dashboard setup (priority, triggers, segments, and re-eligibility), see the [In-App Message FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

Before you debug, add yourself as a [test user]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) and review [Sending test messages]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages).

## Start here: Match your symptom

| Symptom | Go to |
| --- | --- |
| In-app message didn't show for one user | [One user](#in-app-message-not-shown-for-one-user) |
| In-app message didn't show on one platform (Android, iOS, or Web) | [One platform](#in-app-message-not-shown-on-one-platform) |
| In-app message from a **Canvas** step didn't show | [Canvas in-app messages](#canvas-in-app-messages) |
| In-app message showed late or after a delay | [Timing and delayed display](#timing-and-delayed-display) |
| Impressions or clicks look wrong | [Impressions and analytics](#impressions-and-analytics) |
| `triggers` missing or empty in event user logs | [Delivery troubleshooting](#delivery-troubleshooting) |
| Triggers returned but nothing displays on the device | [Platform-specific display troubleshooting](#platform-specific-display-troubleshooting) |
| In-app message assets fail to load (iOS, `NSURLError` -1008) | [Asset loading (Swift tab)]({{site.baseurl}}/developer_guide/in_app_messages/troubleshooting?sdktab=swift#asset-loading) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="In-app message symptom" }

## Standard investigation path

Use this workflow for every incident. Start at step 1.

1. Confirm a **session start** is logged for the test device. In-app messages are requested on session start.
2. Open [event user logs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) and find the SDK request for that session start. In **Response Data**:
   - In the raw JSON, confirm `respond_with` includes `"triggers": true`.
   - The **Requested Responses** row should include **`triggers`**.
   - **Trigger In-App Message** rows list each in-app message returned for that request.
   - If there's no `triggers` key or no **Trigger In-App Message** rows, go to [Troubleshoot messages not being requested](#troubleshoot-messages-not-being-requested).
   - If `triggers` is present but empty (`[]`), go to [Troubleshoot messages not being returned](#troubleshoot-messages-not-being-returned).
   - If **Trigger In-App Message** rows are present but nothing displays, go to [Platform-specific display troubleshooting](#platform-specific-display-troubleshooting).
   - Each trigger payload includes a `type`: `inapp` (standard) or `templated_iam` (requires a template request before display). See [Types of in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
3. For dashboard-side eligibility (segment, re-eligibility, frequency caps, priority, control groups), see [Delivery troubleshooting](#delivery-troubleshooting) and the [In-App Message FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
4. For device-side display issues (delegates, rate limits, orientation, session timeout), select your SDK tab under [Platform-specific display troubleshooting](#platform-specific-display-troubleshooting).

## Canvas in-app messages {#canvas-in-app-messages}

**Symptom:** A user entered a Canvas in-app message step but didn't see the message when expected.

Three behaviors drive most Canvas and in-app message tickets:

1. **Next-session display:** Canvas in-app messages are eligible on the *next* session start after the step is processed—not immediately mid-session. See [When are in-app messages in Canvas sent?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) in the Canvas FAQ.
2. **Delivery validations at step entry:** If **Validate audience at message send** is enabled on the Message step, segment membership and frequency caps are evaluated when the user **enters the step**, not at display time. See [Delivery validations]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
3. **Delay and session timeout:** If a user enters a Delay step longer than your SDK session timeout, they may start a new session before the in-app message step. The message might not be fetched at the session start when you expect it to display.

For availability windows, expiration, and zero _Sends_ on Canvas analytics, see [In-app messages and delivery]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery) in the Canvas FAQ.

{% alert important %}
In-app messages in Canvas can only be triggered by events sent through the SDK, not the REST API.
{% endalert %}

## In-app message didn't show for one user {#in-app-message-not-shown-for-one-user}

**Symptom:** One user didn't receive an expected in-app message; other users may be unaffected.

Check the following:

- Was the user in the segment at **session start**, when the SDK requests new in-app messages?
- Was the user eligible or re-eligible per campaign or Canvas targeting rules? See [Re-eligibility for campaigns and Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Did a [frequency cap]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) apply?
- Was the user in a campaign control group? Check whether the campaign is configured for A/B testing.
- Did a higher-priority in-app message display instead? See [Can multiple in-app messages display in the same session?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session) in the In-App Message FAQ.
- Was the device in the orientation specified by the campaign?
- Was the message suppressed by the default 30-second minimum interval between triggers? See [Overriding the default rate limit]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#overriding-the-default-rate-limit).

Then follow the [standard investigation path](#standard-investigation-path).

## In-app message didn't show on one platform {#in-app-message-not-shown-on-one-platform}

**Symptom:** In-app messages don't show on Android, iOS, or Web, but may work on other platforms.

| Likely cause | What to check |
| --- | --- |
| Wrong **Send To** target | Confirm the campaign or Canvas step targets **Mobile Apps** or **Web Browsers** as appropriate. A Web-only campaign won't send to Android devices. |
| Custom UI or handler suppresses display | Review delegates (mobile) or [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) (Web). See [Customization]({{site.baseurl}}/developer_guide/in_app_messages/customization) and your SDK tab below. |
| Integration never worked on this platform | Confirm this platform and app version have shown in-app messages before. |
| Trigger didn't fire on the device | The trigger must occur locally through the SDK. A REST API call can't trigger an in-app message in the SDK. See [Triggering messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages). |
| Empty `triggers` in event user logs | Segment, re-eligibility, frequency cap, or control group. See [Troubleshoot messages not being returned](#troubleshoot-messages-not-being-returned). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Platform symptom cause" }

## In-app message didn't show for all users {#in-app-message-not-shown-for-all-users}

**Symptom:** No users or fewer users than expected received the in-app message.

Check the following:

- Is the trigger action configured correctly in the dashboard and in the app integration?
- Did a higher-priority in-app message intercept the campaign? See the [In-App Message FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).
- Are you on a recent SDK version? Some in-app message types have minimum SDK requirements.
- Are sessions integrated correctly? Confirm session analytics work for this app.
- Is a customized UI library interfering with display? See [Customization]({{site.baseurl}}/developer_guide/in_app_messages/customization).

Then follow the [standard investigation path](#standard-investigation-path).

## Timing and delayed display {#timing-and-delayed-display}

**Symptom:** The in-app message appeared later than expected or not until a new session.

Common causes:

- **Campaign session-start prefetch:** In-app messages are cached at session start and display when the trigger fires. A trigger that occurs before the next session start won't show until that session. See [Triggering messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).
- **Canvas next-session behavior:** See [Canvas in-app messages](#canvas-in-app-messages).
- **Scheduled dashboard delay:** Confirm whether a delay is configured on the campaign or step.
- **Trigger sync race:** If users log an event immediately after session start, triggers may not be synced yet. Consider triggering off session start and segmenting on the intended event so delivery happens on the next session after the event.
- **Sequential in-app messages:** If you're deferring or restoring messages in a tour, see [Deferring triggered in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
- **Large assets or slow CDN:** Optimize images and video for HTML in-app messages. On mobile, images may download before display on slow networks—select your SDK tab below for platform notes.

{% alert note %}
If your in-app message is triggered by session start and you've set an extended session timeout, closing and re-opening the app within that window won't refresh the session. For example, with a 300-second timeout, a session-start in-app message won't display until the session actually refreshes. Adjust the session timeout or trigger type if this affects your test.
{% endalert %}

## Delivery troubleshooting {#delivery-troubleshooting}

Most in-app message issues are **delivery** (the device didn't receive triggers) or **display** (triggers arrived but didn't show). Confirm [delivery](#troubleshooting-in-app-message-delivery) first, then check [display](#platform-specific-display-troubleshooting).

### Troubleshooting delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze servers on session start. Confirm the SDK is requesting triggers and Braze is returning them.

#### Check if messages are requested and returned

1. Add yourself as a [test user]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).
2. Set up an in-app message campaign targeted at your user.
3. Start a new session in your application.
4. In [event user logs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log), find the SDK request for the session start event. In **Response Data**:
   - In the raw JSON, confirm `respond_with` includes `"triggers": true`.
   - The **Requested Responses** row lists top-level keys in the response. For in-app messages, expect **`triggers`**.
   - **Trigger In-App Message** rows list each in-app message returned for that request.

   Then triage:
   - If there's no `triggers` key or **Trigger In-App Message** rows, see [Troubleshoot messages not being requested](#troubleshoot-messages-not-being-requested).
   - If `triggers` are present but empty (`[]`), see [Troubleshoot messages not being returned](#troubleshoot-messages-not-being-returned).
   - If **Trigger In-App Message** rows are present but nothing displays on the device, see [Platform-specific display troubleshooting](#platform-specific-display-troubleshooting).
   - Each trigger payload includes a `type`: `inapp` (standard) or `templated_iam` (requires a template request before display). See [Types of in-app messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
5. Confirm the correct in-app messages appear in the response data.

![Event user log with SDK requests and response data.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Troubleshoot messages not being requested {#troubleshoot-messages-not-being-requested}

If in-app messages aren't being requested, your app might not be tracking sessions correctly—in-app messages refresh on session start. Confirm the app is starting a session based on your session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Troubleshoot messages not being returned {#troubleshoot-messages-not-being-returned}

If in-app messages aren't being returned, you're likely hitting a targeting or eligibility issue:

1. Your segment doesn't contain your user.
   - Check the user's [**Engagement**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) tab for the expected segment.
2. Your user already received the message and wasn't re-eligible.
   - Check [re-eligibility settings]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) and the [In-App Message FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#campaigns).
3. Your user hit the frequency cap.
   - Check [frequency cap settings]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).
4. Your user fell into a control group.
   - Create a segment with a **Received campaign variant** filter set to **Control**, or opt out of control groups during integration testing.
5. A higher-priority in-app message took precedence. See the [In-App Message FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).

For archived campaigns, trigger configuration, and Quiet Hours, see the [In-App Message FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Impressions and analytics {#impressions-and-analytics}

**Symptom:** Impression or click counts don't match expectations.

- **_Impressions_ greater than _Unique Impressions_:** Expected when users have multiple devices or when a scheduled delay causes the same user to qualify more than once. See [Re-eligibility for campaigns and Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- **Impressions lower than expected:** Users may not have viewed the message (impressions log on display), multiple high-priority messages may intercept each other, or trigger sync races may apply. For Canvas in-app messages, see [Canvas in-app messages](#canvas-in-app-messages). For full metric definitions, see [In-app message reporting]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) and the [In-App Message FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
- **Impressions lower than before:** Review segment and campaign changelogs. Confirm you didn't reuse the same trigger event in a higher-priority campaign.

![Link to view changelog on the Campaign Details page with seven changes since the user has last viewed the campaign]({% image_buster /assets/img_archive/trouble4.png %})

If you use a delegate or custom handler to display in-app messages manually, you must log impressions and clicks yourself. See your SDK tab under [Platform-specific display troubleshooting](#platform-specific-display-troubleshooting) for Swift and Android details, or [Log in-app message data]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data) for Web.

## Platform-specific display troubleshooting {#platform-specific-display-troubleshooting}

If **Trigger In-App Message** rows appear in event user logs but nothing displays on the device, select your SDK tab for display checks (delegates, rate limits, orientation, and custom handlers).

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}
