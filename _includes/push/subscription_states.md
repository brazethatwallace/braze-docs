## Push subscription states {#push-sub-states}

A "Push Subscription State" in Braze identifies a **user's** global preference for their desire to receive push notifications. Because the subscription state is user-based, it is not specific to any individual app. Subscription states become helpful flags when deciding which users to target for push notifications.

{% alert note %}
A user's push subscription state applies to their entire user profile, which includes all of the user's devices. 
{% endalert %}

The following subscription state options exist: `Subscribed`, `Opted-In`, and `Unsubscribed`.

By default, for your user to receive your messages through push, their push subscription state must be either `Subscribed` or `Opted-In`, and they must have foreground push enabled. You can override this setting if needed when composing a message.

|Opt-in State|Description|
|---|---|
|`Subscribed`| Default push subscription state when a user profile is created in Braze. |
|`Opted-In`| A user has explicitly expressed a preference to receive push notifications. Braze automatically moves a user's opt-in state to `Opted-In` if the user accepts an OS-level push prompt.<br><br>This does not apply to Android 12 or earlier users.|
|`Unsubscribed`| A user explicitly unsubscribed from push through your application or other methods your brand provides. By default, Braze push campaigns target only users that are `Subscribed` or `Opted-in` for push.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push subscription states #push-sub-states" }

{% alert important %}
Braze does not automatically change a user's push subscription state to `Unsubscribed`. Remember that if a user's push subscription state is `Unsubscribed`, then the user's `Foreground Push Enabled` filter in segmentation is `false`.
{% endalert %}

### Push registration and reachable users

Push subscription state reflects a user's preference, but whether they count as **reachable** for push in the dashboard also depends on [push registration]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/)—that is, a valid foreground push token on their profile. For how Braze calculates channel-level counts, see [Measure segment size]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/).

- **Push campaigns and Canvases:** Users who aren't push registered aren't included in **Reachable users** for Android Push or iOS Push in audience statistics, even when their push subscription state is `Subscribed` or `Opted-In`.
- **Other channels:** The same users can still count as reachable for other channels they qualify for (for example, email or in-app messages).
- **Segments:** Segment membership follows your filters. Users without push registration remain in the segment unless a filter excludes them (for example, **Foreground Push Enabled**). Total segment membership can be higher than the sum of users shown in push-specific **Reachable users** rows.

A user profile can show push subscription state `Subscribed` while no push token is assigned. Those users still don't count toward **Reachable users** for Android Push or iOS Push until Braze records a valid token.

For filter definitions, see [Segmentation filters]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

### Updating push subscription states {#update-push-subscription-state}

Review the following ways to update a user's push subscription state:

#### Automatic opt-in (default)

By default, Braze sets a user's push subscription state to `Opted-In` when they first authorize push notifications for your app. Braze also does this when a user re-enables push permissions in their system settings after previously disabling them.

{% tabs local %}
{% tab android %}
To disable this default behavior, add the following property to your Android Studio project's `braze.xml` file:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
On iOS, a new install typically shows push subscription state **`Subscribed`** until the user allows notifications. After the user selects **Allow** on the OS prompt, Braze sets the state to **`Opted-In`** when automatic opt-in is enabled. If the user selects **Don't Allow** and later turns push on in iOS Settings, the state updates after the user logs a session—not at the moment they change Settings.

Starting with [Braze Swift SDK version 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), you can disable or further customize this behavior by adding the `optInWhenPushAuthorized` configuration to your Xcode project's `AppDelegate.swift` file:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK integration

You can update a user's subscription state with the Braze SDK using the `setPushNotificationSubscriptionType` method on [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html), or [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). For example, you can use this method to create a settings page in your app where users can manually enable or disable push notifications.

#### REST API

You can update a user's subscription state with the Braze REST API using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update their [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) attribute.

### Differences between push enablement and push subscription status

Push enablement refers to whether a user has granted OS- or browser-level permission to receive notifications on a specific device. Push subscription state is a Braze-level setting that represents a user's global preference for receiving push across their profile.

When automatic opt-in is enabled (the default), Braze updates a user's push subscription state to `Opted-In` when they authorize push notifications for your app or re-enable permissions in their system settings (for example, on iOS, Android 13+, and supported web browsers). Otherwise, the user's push subscription state remains `Subscribed` until you explicitly change it using an SDK method or REST API call.

Braze does not automatically change a user's push subscription state to `Unsubscribed` when they opt out of notifications at the OS, browser, or app level. To update a user's push subscription state, you must update it in Braze. For example, if a user disables push from an in-app preference center, update the push subscription state to `Unsubscribed` in Braze. Braze does not update user profiles based on your preference center. To align subscription states with a user's in-app preferences, call the appropriate methods using the [SDK]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) (iOS or Android) or [REST API]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

### Imported push tokens (iOS)

When you [import iOS push tokens]({{site.baseurl}}/api/objects_filters/user_attributes_object#push-token-import) with `push_token_import`, the user's push subscription state is typically **`Subscribed`** until they log a session in your Braze-integrated app. After the first session, Braze may update the state to **`Opted-In`** if [automatic opt-in](#automatic-opt-in-default) applies (for example, when the user authorizes push on iOS and `optInWhenPushAuthorized` is enabled).

Review **Contact Settings** on the user's profile after import and again after the user's first in-app session to confirm the expected state.

### Checking push subscription state

![User profile for John Doe with their push subscription state set to Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

You can check a user's push subscription state with Braze in any of the following ways:

* **User profile:** You can access individual user profiles through the Braze dashboard on the **[User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** page. After finding a user's profile (via email address, phone number, or external user ID), you can select the **Engagement** tab to view and manually adjust a user's subscription state.
* **REST API export:** You can export individual user profiles in JSON format using the export [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) or [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoints. Braze returns a push tokens object that contains push enablement information per device.