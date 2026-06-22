---
nav_title: Manage placements
article_title: Manage Banner placements for the Braze SDK
description: "Learn how to create and manage Banner placements in the Braze SDK, including accessing their unique properties and logging impressions."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Manage Banner placements

> Learn how to create and manage Banner placements in the Braze SDK, including accessing their unique properties and logging impressions. For more general information, see [About Banners]({{site.baseurl}}/developer_guide/banners).

## About placement requests {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Create a placement

### Prerequisites

These are the minimum SDK versions needed to create Banner placements:

{% multi_lang_include sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Step 2: Refresh placements in your app {#requestBannersRefresh}

Placements can be refreshed by calling the refresh methods described below. If `subscribeToBannersUpdates` is active, the SDK automatically re-publishes your cached placement IDs at the start of each new session and when you call `changeUser`. This automatic refresh does not consume a rate limiting token.

{% alert tip %}
Refresh placements as soon as possible to avoid delays in downloading or displaying Banners.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Step 3: Listen for updates {#subscribeToBannersUpdates}

{% alert tip %}
If you insert Banners using the SDK methods in this guide, all analytics events (such as impressions and clicks) will be handled automatically, and impressions will only be logged when the banner is in view.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
If you're using vanilla JavaScript with the Web Braze SDK, use [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) to listen for placement updates and then call [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) to fetch them.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
If you're using React with the Web Braze SDK, set up [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) inside a `useEffect` hook and call [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) after registering your listener.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

{% alert note %}
Your banner update listener reflects the SDK's in-memory banner state. A single update can include placements that were already cached (for example, from an earlier refresh, another screen, or automatic SDK work), not only the placement IDs from your most recent `requestRefresh` call. If you care only about certain placements, check each banner's placement ID in your listener and skip the rest. When you've registered your listener, call `requestRefresh` for the placements you want to sync from Braze.
{% endalert %}

```swift
let placementIds = ["global_banner", "navigation_square_banner"]
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
// Always refresh after your subscriber is registered
brazeClient.braze()?.banners.requestRefresh(placementIds: placementIds)
```

{% endtab %}
{% tab Android %}

{% alert note %}
Your banner update listener reflects the SDK's in-memory banner state. A single update can include placements that were already cached (for example, from an earlier refresh, another screen, or automatic SDK work), not only the placement IDs from your most recent `requestBannersRefresh` call. If you care only about certain placements, check each banner's placement ID in your listener and skip the rest. When you've registered your listener, call `requestBannersRefresh` for the placements you want to sync from Braze.
{% endalert %}

{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> placementIds = new ArrayList<>();
placementIds.add("global_banner");
placementIds.add("navigation_square_banner");
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val placementIds = listOf("global_banner", "navigation_square_banner")
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Step 4: Insert using the placement ID {#insertBanner}

{% alert tip %}
For a complete step-by-step tutorial, check out [Displaying a Banner by Placement ID]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Create a container element for the Banner. Be sure to set its width and height.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
If you're using vanilla JavaScript with the Web Braze SDK, call the [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) method to replace the inner HTML of the container element.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
  baseUrl: "sdk-base-url",
  allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
  // get this placement's banner. If it's `null` the user did not qualify for one.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  // choose where in the DOM you want to insert the banner HTML
  const container = document.getElementById("global-banner-container");

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
If you're using React with the Web Braze SDK, call the [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) method with a `ref` to replace the inner HTML of the container element.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
To track impressions, be sure to call `insertBanner` for `isControl`. You can then hide or collapse your container afterwards.
{% endalert %}

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// UIKit implementation:
// If you simply want the Banner view, initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// SwiftUI implementation:
// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
To get the Banner in Java code, use:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

You can create Banners in your Android views layout by including this XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
If you're using Android Views, use this XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

To use Jetpack Compose, add the `com.braze:android-sdk-jetpack-compose` artifact to your app module. Use the same version as your other Braze Android SDK dependencies. This module is separate from `android-sdk-ui` and ships the [`Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html) composable under `com.braze.jetpackcompose.banners`.

{% alert note %}
Some Compose UI libraries define their own `Banner` composable. Import `com.braze.jetpackcompose.banners.Banner` explicitly so you call Braze's API.
{% endalert %}

```kotlin
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
    Banner(placementId = "global_banner")
}
```

Optionally pass `heightCallback` to receive the rendered height in dp when the banner size changes. For reference, see the [KDoc for `Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html).

If you don't add the Jetpack Compose module, wrap [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html) in [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView):

```kotlin
import android.view.ViewGroup
import androidx.compose.runtime.Composable
import androidx.compose.ui.viewinterop.AndroidView
import com.braze.ui.banners.BannerView

@Composable
fun myBannerSlot() {
    AndroidView(
        factory = { context ->
            BannerView(context, "global_banner").apply {
                layoutParams = ViewGroup.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
                )
            }
        },
        update = { it.placementId = "global_banner" }
    )
}
```

To get the Banner in Kotlin, use:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

If you're using [React Native's New Architecture](https://reactnative.dev/architecture/landing-page), you need to register `BrazeBannerView` as a Fabric component in your `AppDelegate.mm`.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```
For the simplest integration, add the following JavaScript XML (JSX) snippet into your view hierarchy, providing just the placement ID.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

To get the Banner's data model in React Native, or to check for the presence of that placement in your user's cache, use:

```javascript
const banner = await Braze.getBanner("global_banner");
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}
For the simplest integration, add the following widget into your view hierarchy, providing just the placement ID.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

You can use the `getBanner` method to check for the presence of that placement in your user's cache.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Step 5: Send a test Banner (optional) {#handling-test-cards}

Before you launch a Banner campaign, you can [send a test Banner]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=banners) to verify your integration. Test Banners are stored in a separate in-memory cache and don't persist across app restarts. While no extra setup is needed, your test device must be capable of receiving foreground push notifications so it can display the test.

{% alert note %}
Test Banners are like any other banners, except they're removed at the next app session.
{% endalert %}

## Log impressions

Braze automatically logs impressions for Banners that are in view when you use SDK methods to insert a Banner&#8212;so no need to track impressions manually.

## Logging clicks

The method used to log Banner clicks depends on how your Banner is rendered and where your click handler is located.

### Standard Banner content (automatic)

If you're using default, out-of-the-box SDK methods to insert Banners, and your Banner uses standard editor components (images, buttons, text), clicks are tracked automatically. The SDK attaches click listeners to these elements, and no additional code is needed.

### Custom Code Blocks

If your Banner uses the **Custom Code** editor block in the Braze dashboard, you must use `brazeBridge.logClick()` to log clicks from within that custom HTML. This applies even when using SDK methods to render the Banner, because the SDK cannot automatically attach listeners to elements inside your custom code.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

For the full reference, see [Custom code and JavaScript bridge for Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#custom-code). The `brazeBridge` provides a communication layer between the Banner's internal HTML and the parent Braze SDK.

### Custom UI implementations (headless)

If you're building a fully custom UI using the Banner's [custom properties](#custom-properties) rather than rendering the Banner HTML, you must manually log clicks and impressions from your application code. Because the SDK is not rendering the Banner, it has no way to automatically track interactions with your custom UI elements.

For method signatures and full details, see the [Braze SDK reference documentation]({{site.baseurl}}/developer_guide/references).

#### Logging impressions

Call the platform's Banner impression method when your custom UI considers the Banner "viewed." Build robust logic for what counts as an impression to avoid duplicate events—for example, log only when the Banner enters the viewport (or equivalent), and do not log again when the same Banner is scrolled back into view or when your component re-renders without a new view event.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
const banner = braze.getBanner("placement_id_homepage_top");
if (banner) {
  braze.logBannerImpressions([banner]);
}
```
[Web SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top")
```
{% endsubtab %}
{% subtab Java %}
```java
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top");
```
{% endsubtab %}
{% endsubtabs %}
[Android SDK reference](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-impression.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logImpression()
}
```
[Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logimpression())
{% endtab %}
{% tab React Native %}
```javascript
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");
```
See the [React Native SDK repository](https://github.com/braze-inc/braze-react-native-sdk) for the latest method signatures.
{% endtab %}
{% tab Flutter %}
```dart
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");
```
[Flutter SDK reference](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerImpression.html)
{% endtab %}
{% endtabs %}

#### Logging clicks

Call the platform's Banner click method when the user taps your custom Banner (or a specific button). Pass the optional `buttonId` when the click is on a specific button so analytics can attribute the click correctly.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
[Web SDK reference](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId)  // buttonID parameter can be null
```
{% endsubtab %}
{% subtab Java %}
```java
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
{% endsubtab %}
{% endsubtabs %}
[Android SDK reference](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-click.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logClick(buttonId: buttonId)  // buttonID is optional
}
```
[Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logclick(buttonid:))
{% endtab %}
{% tab React Native %}
```javascript
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
See the [React Native SDK repository](https://github.com/braze-inc/braze-react-native-sdk) for the latest method signatures.
{% endtab %}
{% tab Flutter %}
```dart
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
[Flutter SDK reference](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerClicked.html)
{% endtab %}
{% endtabs %}

## Log dismissals

Banner dismissals programmatically remove a Banner from a placement when a user actively dismisses it. When dismissed, the Banner is suppressed for that user. The next time the list of placements is refreshed, a new banner is returned if the user is eligible for one.

### Prerequisites

These are the minimum SDK versions required to log Banner dismissals:

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### Integrations

#### Standard Banner integrations (drag-and-drop editor)

If your Banner uses the drag-and-drop editor and includes a dismiss button component, no additional code is required. When a user taps the dismiss button, the SDK immediately collapses the Banner, records a dismissal event for analytics, and queues the dismissal for backend sync.

#### Custom Code Blocks

If your Banner uses the **Custom Code** editor block, you can trigger a dismissal directly from within the Banner's HTML using `brazeBridge.closeMessage()`.

```html
<button onclick="brazeBridge.closeMessage()">
  Dismiss
</button>
```

### Log custom analytics on banner dismissal

To run additional logic such as logging custom analytics upon dismissing a banner, override the optional `onDismiss` callback on your banner view. By default, this callback is empty.

{% tabs %}
{% tab Web %}
The Web SDK does not have a dedicated `onDismiss` callback on `insertBanner`. Instead, use `subscribeToBannersUpdates` to detect when a banner has been dismissed by checking if it is no longer present in the updated banners map.

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = banners["global_banner"];

  if (!globalBanner) {
    // The banner was dismissed or the user is no longer eligible.
    // Run any custom analytics here.
    console.log("Banner was dismissed");
    return;
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endsubtab %}
{% subtab React %}
```typescript
import { useEffect } from "react";
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    const globalBanner = banners["global_banner"];

    if (!globalBanner) {
      // The banner was dismissed or the user is no longer eligible.
      // Run any custom analytics here.
      console.log("Banner was dismissed");
      return;
    }
  });

  braze.requestBannersRefresh(["global_banner"]);

  return () => {
    braze.removeSubscription(subscriptionId);
  };
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
Set the optional [`onDismissCallback`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/on-dismiss-callback.html) property on [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html).

{% subtabs %}
{% subtab Java %}

```java
import android.util.Log;
import com.braze.ui.banners.BannerView;
import kotlin.Unit;

// After obtaining your BannerView instance (for example from XML via findViewById, or `new BannerView(context, "global_banner")`)

bannerView.setOnDismissCallback(() -> {
  Log.d(TAG, "Successfully dismissed banner with placementId: " + bannerView.getPlacementId());

  // Run any custom logic here, such as logging custom analytics
  return Unit.INSTANCE;
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
import android.util.Log
import com.braze.ui.banners.BannerView

// After obtaining your BannerView instance (for example via findViewById or `BannerView(context, "global_banner")`)

bannerView.onDismissCallback = {
  Log.d(TAG, "Successfully dismissed banner with placementId: ${bannerView.placementId}")

  // Run any custom logic here, such as logging custom analytics
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}
```swift
// After initializing your banner view instance using UIKit or SwiftUI

bannerView.onDismiss = { dismissedBanner in
  print("Successfully dismissed banner with placementId: \(dismissedBanner.placementId)")

  // Run any custom logic here, such as logging custom analytics
}
```
{% endtab %}
{% endtabs %}

### Pending dismissal storage cap

Dismissal events are stored locally as pending entries until they can be synced to the Braze server on the next `requestBannersRefresh` call.

{% alert warning %}
In rare cases where a large number of dismissals accumulate without a successful sync, older pending dismissals may be dropped. If this occurs, previously-dismissed Banners may reappear until the next successful sync completes. To minimize this risk, call `requestBannersRefresh` whenever your app regains network connectivity.
{% endalert %}

## Dimensions and sizing

Here's what you need to know about Banner dimensions and sizing:

- While the composer allows you to preview Banners in different dimensions, that information isn't saved or sent to the SDK.
- The HTML will take up the full width of the container it's rendered in.
- We recommend making a fixed dimension element and testing those dimensions in composer.

## Custom properties {#custom-properties}

You can use custom properties from your Banner campaign to retrieve key–value data through the SDK and modify your app’s behavior or appearance. For example, you could:

- Send metadata for your third-party analytics or integrations.
- Use metadata such as a `timestamp` or JSON object to trigger conditional logic.
- Control the behavior of a banner based on included metadata like `ratio` or `format`.

### Prerequisites

You must [add custom properties]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#custom-properties) to your Banner campaign. Additionally, these are the minimum SDK versions required to access custom properties:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Access custom properties

To access a banner's custom properties, use one of the following methods based on the property's type defined in the dashboard. If the key doesn't match a property of that type or does not exist, the method returns `null`.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");
  
  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");
  
  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");
  
  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");
  
  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");
  
  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');
  
  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');
  
  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');
  
  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');
  
  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');
  
  // Get the JSON object property
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');
  
  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}
