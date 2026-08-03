## Troubleshooting

### Tapping push notification doesn't open the app

On Android, whether tapping a push notification automatically brings your app to the foreground and opens its deep link is controlled by the native `com_braze_handle_push_deep_links_automatically` flag, which defaults to `false`.

With the default of `false`:

- The native SDK still sends a `BRAZE_PUSH_CLICKED` broadcast and your Dart `push_opened` listener still fires as expected.
- The native SDK does not call `startActivity()`, so your app is not brought to the foreground and the deep link isn't followed automatically.

If these two behaviors match what you're seeing, the flag setting is likely the cause.
To confirm, check your device logs for a `BrazePushReceiver` entry handling `com.braze.action.BRAZE_PUSH_CLICKED`, followed by a `push_opened` event in your Flutter logs, with no corresponding app launch.

To fix this, set `com_braze_handle_push_deep_links_automatically` to `true` in your `braze.xml`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

For more information, see [Add deep links (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android) in the Flutter push notifications guide.

### Other push delivery and registration issues

Since the Braze Flutter SDK for Android is built on top of the native Braze Android SDK, most other push delivery, registration, and logging issues (such as sender ID mismatches, missing Google Play Services, or `BrazeFirebaseMessagingService` not being registered) also apply to Flutter apps. For more information, see the [native Android troubleshooting guide]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android).
