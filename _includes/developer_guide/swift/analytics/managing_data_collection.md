## Apple's privacy manifest {#privacy-manifest}

### What is tracking data?

Apple defines "tracking data" as data collected in your app about an end user or device that's linked to third-party data (such as targeted advertising), or a data broker. For a complete definition with examples, see [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

By default, the Braze SDK does not collect tracking data. However, depending on your Braze SDK configuration, you may be required to list Braze-specific data in your app's privacy manifest.

### What is a privacy manifest?

A privacy manifest is a file in your Xcode project that describes the reason your app and third-party SDKs collect data, along with their data-collection methods. Each of your third-party SDKs that track data require its own privacy manifest. When you [create your app's privacy report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), these privacy manifest files are automatically aggregated into a single report.

### API tracking-data domains

Starting with iOS 17.2, Apple will block all declared tracking endpoints in your app until the end user accepts an [Ad Tracking Transparency (ATT) prompt](https://support.apple.com/en-us/HT212025). Braze provides tracking endpoints to route your tracking data, while still allowing you to route non-tracking first-party data to the original endpoint. 

## Declaring Braze tracking data

{% alert tip %}
For a full walkthrough, see the [Privacy Tracking Data tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Prerequisites

The following Braze SDK version is required to implement this feature:

{% sdk_min_versions swift:9.0.0 %}

### Step 1: Review your current policies

Review your Braze SDK's current data-collection policies with your legal team to determine whether your app collects tracking data [as defined by Apple](#what-is-tracking-data). If you're not collecting any tracking data, you don't need to customize your privacy manifest for the Braze SDK at this time. For more information about the Braze SDK's data-collection policies, see [SDK data collection]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).

{% alert important %}
If any of your non-Braze SDKs collect tracking data, you'll need to review those policies separately.
{% endalert %}

### Step 2: Create a privacy manifest

First, check if you already have a privacy manifest by searching for a `PrivacyInfo.xcprivacy` file in your Xcode project. If you already have this file, you can continue to the next step. Otherwise, see [Apple: Create a privacy manifest](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Step 3: Add your endpoint to the privacy manifest

In your Xcode project, open your app's `PrivacyInfo.xcprivacy` file, then right-click the table and check **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![An Xcode project with the context menu open and "Raw Keys and Values" highlighted.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Under **App Privacy Configuration**, choose **NSPrivacyTracking** and set its value to **YES**.

![The 'PrivacyInfo.xcprivacy' file open with "NSPrivacyTracking" set to "YES".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Under **App Privacy Configuration**, choose **NSPrivacyTrackingDomains**. In the domains array, add a new element and set its value to the endpoint you [previously added to your `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate) prefixed with `sdk-tracking`.

![The 'PrivacyInfo.xcprivacy' file open with a Braze tracking endpoint listed under "NSPrivacyTrackingDomains".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Step 4: Declare your tracking data

Next, open `AppDelegate.swift` then list each [tracking property](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) you want to declare by creating a static or dynamic tracking list. Keep in mind, Apple will block these properties until the end user accepts their ATT prompt, so only list the properties you and your legal team consider tracking. For example:

{% tabs %}
{% tab static example %}
In the following example, `dateOfBirth`, `customEvent`, and `customAttribute` are declared as tracking data within a static list. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab dynamic example %}
In the following example, the tracking list is automatically updated after the end user accepts the [App Tracking Transparency (ATT) prompt](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)). Requesting authorization on app activation is a per-scene event, so this code belongs in your `SceneDelegate.swift` file's `sceneDidBecomeActive(_:)` method rather than `AppDelegate.swift`'s `applicationDidBecomeActive(_:)` (required for apps that have adopted the [`UIScene` life cycle](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)). Your Braze instance remains reachable from `SceneDelegate` through the `AppDelegate.braze` static property configured in Step 1.

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze?.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Step 5: Prevent infinite retry loops

To prevent the SDK from entering an infinite retry loop, use the `set(adTrackingEnabled: enableAdTracking)` method to handle ATT permissions. The `adTrackingEnabled` property in your `SceneDelegate.swift` method should be handled similar to the following:

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Disabling data tracking

To disable data-tracking activity on the Swift SDK, set the [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) property to `false` on your Braze instance. When `enabled` is set to `false`, the Braze SDK ignores any calls to the public API. The SDK also cancels all in-flight actions, such as network requests, event processing, etc. 

## Wiping previously-stored data

You can use the [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) method to fully clear locally-stored SDK data on a user's device.

For Braze Swift versions 7.0.0 and later, the SDK and the `wipeData()` method randomly generates a UUID for their device ID. However, if your `useUUIDAsDeviceId` is set to `false` _or_ you're using Swift SDK version 5.7.0 or earlier, you'll also need to make a post request to [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) since your Identifier for Vendors (IDFV) will automatically be used as that user's device ID.

If you use manual push integration, and your app calls `wipeData()` and later re-enables the SDK in the same app run, call `registerForRemoteNotifications()` again so Braze can receive a refreshed device token. For more information, see [setting up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Resuming data tracking

To resume data collection, set [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) to `true`. Keep in mind, this will not restore any previously wiped data.

## Logout and Unregister Push

The Braze SDK provides methods to stop targeting a device when a user unregisters from push notifications or logs out. These methods remove push registration data from the current user on the Braze server and the SDK, so Braze no longer sends future push notification campaigns to that user.

### Logout {#logout}

When a user logs out from an application, call the SDK's `logout` method to remove the device's push registration from the current user and automatically perform cleanup actions on the SDK. The `logout` method performs the following:

- Unregisters the device's push token, and any Live Activities push-to-start tokens, from the current user on the Braze server.
- If the unregister call succeeds, the SDK wipes locally-stored SDK data and disables the SDK.
- On failure, raises an error and an `isRetriable` flag to allow the integrator to take action.

{% subtabs local %}
{% subtab Swift %}

The following completion-handler example shows `logout` success and failure handling. Use it for callback-based flows, and replace the logging with your app's retry or re-authentication logic.

```swift
// Completion handler
AppDelegate.braze?.logout { result in
  switch result {
  case .success:
    print("Logout successful")
  case .failure(let error):
    print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

The following async example shows the suspending `logout` API. Use it for async workflows and customize the success and failure branches for your app.

```swift
// Async/await
do {
  try await AppDelegate.braze?.logout()
  print("Logout successful")
} catch let error as Braze.LogoutErrorResult {
  print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

This Objective-C example shows completion-based `logout` handling. Use it in Objective-C integrations and replace the logging with your app flow.

```objc
[AppDelegate.braze logoutWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZLogoutErrorUserInfoKey.isRetriable];
    NSLog(@"Logout failed: %@, isRetriable=%@", error.localizedDescription, isRetriable);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

#### Re-enable tracking and push after `logout`

After a successful `logout`, set [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) back to `true`, then re-register for notifications with your operating system (OS) or push provider by following [Swift push setup]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

#### Avoid immediate unregister calls

Avoid calling `logout` or `unregisterPush` directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

### Unregister Push {#unregister-push}

To stop sending push to a device without additional automated cleanup, use the `unregisterPush` method. This removes the device's push token from the current user on Braze's server, and clears the locally-stored token.

{% subtabs local %}
{% subtab Swift %}

The following completion-handler example shows `unregisterPush` success and failure handling. Use it for callback-based flows, and replace the logging with your own retry logic.

```swift
// Completion handler
AppDelegate.braze?.notifications.unregisterPush { result in
  switch result {
  case .success:
    print("Push unregistered successfully")
  case .failure(let error):
    print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

The following async example shows the suspending `unregisterPush` API. Use it for async workflows and customize the success and failure branches for your app.

```swift
// Async/await
do {
  try await AppDelegate.braze?.notifications.unregisterPush()
  print("Push unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

This Objective-C example shows completion-based `unregisterPush` handling. Use it in Objective-C integrations and replace the logging with your app flow.

```objc
[AppDelegate.braze.notifications unregisterPushWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.isRetriable];
    NSNumber *statusCode = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.httpStatusCode];
    NSLog(@"Push unregistration failed: %@, isRetriable=%@ status=%@",
          error.localizedDescription, isRetriable, statusCode);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

#### Re-register push after `unregisterPush`

After calling `unregisterPush`, re-register for notifications with your OS or push provider by following [Swift push setup]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) before sending Braze push notifications again.

#### Avoid immediate unregister calls

Avoid calling `logout` or `unregisterPush` directly after registering for push notifications with the OS or push provider. Due to asynchronous server processing, this can rarely re-add the push token to the Braze user.

### Unregister push-to-start tokens for Live Activities {#unregister-push-to-start}

Live Activities can be started remotely using push-to-start tokens. To stop Braze from remotely starting Live Activities on a device, call the `unregisterPushToStart` method to unregister all currently-registered types (default) or a specified list of Activity types.

Note that currently-running Live Activities continue to receive updates and that this method will only remove the ability to start new activities remotely. For more information on Live Activities, see [Live Activities]({{site.baseurl}}/developer_guide/live_notifications/live_activities).

{% alert note %}
Avoid calling `logout` or `unregisterPushToStart` directly after calling `registerPushToStart` for a Live Activity. Due to the asynchronous nature of server processing, in rare cases, this can lead to the push-to-start token being re-added to the Braze user.
{% endalert %}

The following example shows how to unregister all push-to-start activity types. Use it when a signed-out user should no longer receive new remotely started Live Activities.

```swift
// Unregister all currently-registered activity types
// Completion handler
AppDelegate.braze?.liveActivities.unregisterPushToStart { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}

// Async/await
do {
  try await AppDelegate.braze?.liveActivities.unregisterPushToStart()
  print("Push-to-start unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

The following example shows how to unregister specific activity types. Use it when only selected Live Activities should stop being started remotely.

```swift
// Unregister specific activity types
AppDelegate.braze?.liveActivities.unregisterPushToStart(types: ["ActivityType1", "ActivityType2"]) { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

{% alert note %}
`unregisterPushToStart` doesn't have an Objective-C API, as Live Activities rely on Swift-only types.
{% endalert %}

## IDFV collection

In previous versions of the Braze iOS SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. Beginning in Swift SDK `v5.7.0`, the IDFV field was optionally disabled, and instead, Braze would set a random UUID as the device ID. Starting in Swift SDK `v7.0.0`, the IDFV field will not be collected by default, and a UUID will be set as the device ID instead.

The `useUUIDAsDeviceId` feature configures the [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) to set the device ID as a UUID. Traditionally, the iOS SDK would assign the device ID equal to the Apple-generated IDFV value. With this feature enabled by default on your iOS app, all new users created through the SDK would be assigned a device ID equal to a UUID.

If you still want to collect IDFV separately, you can use [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

{% alert note %}
Reading `braze.deviceId` blocks the calling thread until the SDK has completed its post-initialization operations. For main-thread or latency-sensitive contexts, use the non-blocking alternatives instead.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.getDeviceId { deviceId in
  print("Device ID:", deviceId)
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let deviceId = await AppDelegate.braze?.getDeviceId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze getDeviceIdWithCompletion:^(NSString *deviceId) {
  NSLog(@"Device ID: %@", deviceId);
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}

### Considerations

#### SDK Version

In Swift SDK `v7.0.0+`, when `useUUIDAsDeviceId` is enabled (default), all new users created will be assigned a random device ID. All previously existing users will maintain their same device ID value, which may have been IDFV.

When this feature is not enabled, devices will continue to be assigned IDFV upon creation.

#### Downstream 

**Technology partners**: When this feature is enabled, any technology partners that derive the IDFV value from the Braze device ID will no longer have access to this data. If the IDFV value derived from the device is needed for your partner integration, we recommend that you set this feature to `false`.

**Currents**: `useUUIDAsDeviceId` set to true means the device ID sent in Currents will no longer equal the IDFV value.

### Frequently asked questions

#### Will this change impact my existing users in Braze?

No. When enabled, this feature will not overwrite any user data in Braze. New UUID device IDs will only be created for new devices or when `wipedata()` is called.

#### Can I turn this feature off after turning it on?

Yes, this feature can be toggled on and off at your discretion. Previously stored device IDs will never be overwritten.

#### Can I still capture the IDFV value through Braze elsewhere?

Yes, you can still optionally collect the IDFV through the Swift SDK (collection is disabled by default). 
