---
nav_title: 배치 관리
article_title: Braze SDK의 배너 배치 관리
description: "Braze SDK에서 배너 배치를 생성하고 관리하는 방법을 알아보세요. 고유 속성에 접근하고 노출을 기록하는 방법도 포함됩니다."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# 배너 배치 관리 {#manage-banner-placements}

> Braze SDK에서 배너 배치를 생성하고 관리하는 방법을 알아보세요. 고유 속성에 접근하고 노출을 기록하는 방법도 포함됩니다. 보다 일반적인 정보는 [배너 정보]({{site.baseurl}}/developer_guide/banners/)를 참조하세요.

## 배치 요청에 대하여 {#requests}

{% multi_lang_include banners/placement_requests.md %}

## 배치 생성 {#create-a-placement}

### 필수 조건 {#prerequisites}

배너 배치를 생성하는 데 필요한 최소 SDK 버전은 다음과 같습니다:

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### 2단계: 앱에서 배치 새로고침 {#requestBannersRefresh}

아래에 설명된 새로고침 메서드를 호출하여 배치를 새로고침할 수 있습니다. `subscribeToBannersUpdates`가 활성 상태인 경우, SDK는 새 세션이 시작될 때와 `changeUser`를 호출할 때 캐시된 배치 ID를 자동으로 다시 게시합니다. 이 자동 새로고침은 사용량 제한 토큰을 소비하지 않습니다.

{% alert tip %}
배너 다운로드 또는 표시 지연을 방지하려면 가능한 한 빨리 배치를 새로고침하세요.
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

### 3단계: 업데이트 수신 대기 {#subscribeToBannersUpdates}

{% alert tip %}
이 가이드의 SDK 메서드를 사용하여 배너를 삽입하면 모든 분석 이벤트(노출 및 클릭 등)가 자동으로 처리되며, 배너가 보일 때만 노출이 기록됩니다.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Web Braze SDK와 함께 일반 JavaScript를 사용하는 경우 [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)를 사용하여 배치 업데이트를 수신한 다음 [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)를 호출하여 가져옵니다.

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
Web Braze SDK와 함께 React를 사용하는 경우 `useEffect` 훅 내에서 [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)를 설정하고 리스너를 등록한 후 [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)를 호출합니다.

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
배너 업데이트 리스너는 SDK의 인메모리 배너 상태를 반영합니다. 단일 업데이트에는 가장 최근 `requestRefresh` 호출의 배치 ID뿐만 아니라 이미 캐시된 배치(예: 이전 새로고침, 다른 화면 또는 자동 SDK 작업에서)도 포함될 수 있습니다. 특정 배치에만 관심이 있는 경우 리스너에서 각 배너의 배치 ID를 확인하고 나머지는 건너뛰세요. 리스너를 등록한 후 Braze에서 동기화하려는 배치에 대해 `requestRefresh`를 호출하세요.
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
배너 업데이트 리스너는 SDK의 인메모리 배너 상태를 반영합니다. 단일 업데이트에는 가장 최근 `requestBannersRefresh` 호출의 배치 ID뿐만 아니라 이미 캐시된 배치(예: 이전 새로고침, 다른 화면 또는 자동 SDK 작업에서)도 포함될 수 있습니다. 특정 배치에만 관심이 있는 경우 리스너에서 각 배너의 배치 ID를 확인하고 나머지는 건너뛰세요. 리스너를 등록한 후 Braze에서 동기화하려는 배치에 대해 `requestBannersRefresh`를 호출하세요.
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

### 4단계: 배치 ID를 사용하여 삽입 {#insertBanner}

{% alert tip %}
전체 단계별 튜토리얼은 [배치 ID로 배너 표시하기]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners/)를 확인하세요.
{% endalert %}

{% tabs %}
{% tab Web %}

배너의 컨테이너 요소를 만듭니다. 너비와 높이를 설정해야 합니다.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Web Braze SDK와 함께 일반 JavaScript를 사용하는 경우 [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) 메서드를 호출하여 컨테이너 요소의 내부 HTML을 교체합니다.

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
Web Braze SDK와 함께 React를 사용하는 경우 `ref`와 함께 [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) 메서드를 호출하여 컨테이너 요소의 내부 HTML을 교체합니다.

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
노출을 추적하려면 `isControl`에 대해서도 `insertBanner`를 호출해야 합니다. 그런 다음 컨테이너를 숨기거나 접을 수 있습니다.
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
Java 코드에서 배너를 가져오려면 다음을 사용합니다:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

다음 XML을 포함하여 Android 뷰 레이아웃에 배너를 만들 수 있습니다:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Android 뷰를 사용하는 경우 다음 XML을 사용하세요:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Jetpack Compose를 사용하려면 앱 모듈에 `com.braze:android-sdk-jetpack-compose` 아티팩트를 추가하세요. 다른 Braze Android SDK 종속성과 동일한 버전을 사용합니다. 이 모듈은 `android-sdk-ui`와 별도이며 `com.braze.jetpackcompose.banners` 아래에 [`Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html) 컴포저블을 제공합니다.

{% alert note %}
일부 Compose UI 라이브러리는 자체 `Banner` 컴포저블을 정의합니다. Braze의 API를 호출하려면 `com.braze.jetpackcompose.banners.Banner`를 명시적으로 임포트하세요.
{% endalert %}

```kotlin
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
    Banner(placementId = "global_banner")
}
```

선택적으로 `heightCallback`을 전달하여 배너 크기가 변경될 때 렌더링된 높이를 dp 단위로 받을 수 있습니다. 참조는 [`Banner`에 대한 KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html)을 확인하세요.

Jetpack Compose 모듈을 추가하지 않는 경우 [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html)를 [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView)로 래핑하세요:

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

Kotlin에서 배너를 가져오려면 다음을 사용하세요:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

[React Native의 새 아키텍처](https://reactnative.dev/architecture/landing-page)를 사용하는 경우 `AppDelegate.mm`에 `BrazeBannerView`를 Fabric 구성요소로 등록해야 합니다.

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
가장 간단한 통합을 위해 배치 ID만 제공하는 다음 JavaScript XML(JSX) 스니펫을 뷰 계층 구조에 추가합니다.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

React Native에서 배너의 데이터 모델을 가져오거나 사용자 캐시에 해당 배치가 있는지 확인하려면 다음을 사용하세요:

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
가장 간단한 통합을 위해 다음 위젯을 뷰 계층 구조에 추가하고 배치 ID만 제공하면 됩니다.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

`getBanner` 메서드를 사용하여 사용자 캐시에 해당 배치가 있는지 확인할 수 있습니다.

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

### 5단계: 테스트 배너 보내기(선택 사항) {#handling-test-cards}

배너 Campaign을 시작하기 전에 [테스트 배너를 전송]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=banners)하여 통합을 확인할 수 있습니다. 테스트 배너는 별도의 인메모리 캐시에 저장되며 앱 재시작 시 유지되지 않습니다. 추가 설정은 필요하지 않지만, 테스트를 표시할 수 있도록 테스트 기기가 포그라운드 푸시 알림을 수신할 수 있어야 합니다.

{% alert note %}
테스트 배너는 다음 앱 세션에서 제거된다는 점을 제외하면 다른 배너와 동일합니다.
{% endalert %}

## 노출 기록 {#log-impressions}

Braze는 SDK 메서드를 사용하여 배너를 삽입할 때 보이는 배너에 대해 자동으로 노출을 기록하므로&#8212;수동으로 노출을 추적할 필요가 없습니다.

## 클릭 기록 {#logging-clicks}

배너 클릭을 기록하는 데 사용되는 메서드는 배너가 렌더링되는 방식과 클릭 핸들러의 위치에 따라 다릅니다.

### 표준 배너 콘텐츠(자동) {#standard-banner-content-automatic}

기본 제공 SDK 메서드를 사용하여 배너를 삽입하고 배너가 표준 편집기 구성요소(이미지, 버튼, 텍스트)를 사용하는 경우 클릭이 자동으로 추적됩니다. SDK는 이러한 요소에 클릭 리스너를 연결하며 추가 코드가 필요하지 않습니다.

### 커스텀 코드 블록 {#custom-code-blocks}

배너가 Braze 대시보드의 **커스텀 코드** 편집기 블록을 사용하는 경우, 해당 커스텀 HTML 내에서 클릭을 기록하기 위해 `brazeBridge.logClick()`을 사용해야 합니다. SDK 메서드를 사용하여 배너를 렌더링하는 경우에도 마찬가지입니다. SDK는 커스텀 코드 내의 요소에 리스너를 자동으로 연결할 수 없기 때문입니다.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

전체 참조는 [배너를 위한 커스텀 코드 및 JavaScript 브리지]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#custom-code)를 참조하세요. `brazeBridge`는 배너의 내부 HTML과 상위 Braze SDK 간의 통신 계층을 제공합니다.

### 커스텀 UI 구현(헤드리스) {#custom-ui-implementations-headless}

배너의 [커스텀 속성](#custom-properties)을 사용하여 배너 HTML을 렌더링하는 대신 완전히 커스텀 UI를 구축하는 경우, 애플리케이션 코드에서 클릭과 노출을 수동으로 기록해야 합니다. SDK가 배너를 렌더링하지 않기 때문에 커스텀 UI 요소와의 상호작용을 자동으로 추적할 방법이 없습니다.

메서드 시그니처 및 전체 세부 정보는 [Braze SDK 참조 문서]({{site.baseurl}}/developer_guide/references/)를 참조하세요.

#### 노출 기록 {#logging-impressions}

커스텀 UI에서 배너가 "조회됨"으로 간주될 때 플랫폼의 배너 노출 메서드를 호출하세요. 중복 이벤트를 방지하기 위해 노출로 간주되는 기준에 대한 견고한 로직을 구축하세요. 예를 들어, 배너가 뷰포트에 진입할 때(또는 이에 상응하는 시점에)만 기록하고, 동일한 배너가 다시 스크롤되어 보이거나 새로운 뷰 이벤트 없이 구성요소가 다시 렌더링될 때는 다시 기록하지 마세요.

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
[Web SDK 참조](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions)
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
[Android SDK 참조](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-impression.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logImpression()
}
```
[Swift SDK 참조](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logimpression())
{% endtab %}
{% tab React Native %}
```javascript
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");
```
최신 메서드 시그니처는 [React Native SDK 리포지토리](https://github.com/braze-inc/braze-react-native-sdk)를 참조하세요.
{% endtab %}
{% tab Flutter %}
```dart
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");
```
[Flutter SDK 참조](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerImpression.html)
{% endtab %}
{% endtabs %}

#### 클릭 기록

사용자가 커스텀 배너(또는 특정 버튼)를 탭할 때 플랫폼의 배너 클릭 메서드를 호출하세요. 클릭이 특정 버튼에 대한 것인 경우 선택적 `buttonId`를 전달하여 분석에서 클릭을 올바르게 귀속시킬 수 있습니다.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
[Web SDK 참조](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick)
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
[Android SDK 참조](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-click.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logClick(buttonId: buttonId)  // buttonID is optional
}
```
[Swift SDK 참조](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logclick(buttonid:))
{% endtab %}
{% tab React Native %}
```javascript
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
최신 메서드 시그니처는 [React Native SDK 리포지토리](https://github.com/braze-inc/braze-react-native-sdk)를 참조하세요.
{% endtab %}
{% tab Flutter %}
```dart
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
[Flutter SDK 참조](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerClicked.html)
{% endtab %}
{% endtabs %}

## 해제 기록 {#log-dismissals}

배너 해제는 사용자가 적극적으로 배너를 해제할 때 배치에서 배너를 프로그래밍 방식으로 제거합니다. 해제되면 해당 사용자에 대해 배너가 억제됩니다. 다음에 배치 목록이 새로고침될 때 사용자가 자격이 있는 경우 새 배너가 반환됩니다.

### 필수 조건

배너 해제를 기록하는 데 필요한 최소 SDK 버전은 다음과 같습니다:

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### 통합 {#integrations}

#### 표준 배너 통합(드래그 앤 드롭 편집기) {#standard-banner-integrations-drag-and-drop-editor}

배너가 드래그 앤 드롭 편집기를 사용하고 해제 버튼 구성요소를 포함하는 경우 추가 코드가 필요하지 않습니다. 사용자가 해제 버튼을 클릭하면 메시지가 숨겨지고, 해제가 트리거된 후 분석을 위한 해제 이벤트가 기록됩니다.

#### 커스텀 코드 블록

배너가 **커스텀 코드** 편집기 블록을 사용하는 경우 배너의 HTML 내에서 `brazeBridge.closeMessage()`를 사용하여 직접 해제를 트리거할 수 있습니다.

```html
<button onclick="brazeBridge.closeMessage()">
  Dismiss
</button>
```

### 배너 해제 시 커스텀 분석 기록 {#log-custom-analytics-on-banner-dismissal}

배너 해제 시 커스텀 분석 기록과 같은 추가 로직을 실행하려면 배너 뷰에서 선택적 `onDismiss` 콜백을 재정의하세요. 기본적으로 이 콜백은 비어 있습니다.

{% tabs %}
{% tab Web %}
Web SDK에는 `insertBanner`에 전용 `onDismiss` 콜백이 없습니다. 대신 `subscribeToBannersUpdates`를 사용하여 업데이트된 배너 맵에 배너가 더 이상 존재하지 않는지 확인하여 배너가 해제되었는지 감지하세요.

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
[`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html)에서 선택적 [`onDismissCallback`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/on-dismiss-callback.html) 속성을 설정하세요.

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

### 보류 중인 해제 저장 한도 {#pending-dismissal-storage-cap}

해제 이벤트는 다음 `requestBannersRefresh` 호출 시 Braze 서버에 동기화될 때까지 보류 항목으로 로컬에 저장됩니다.

{% alert warning %}
드문 경우지만 성공적인 동기화 없이 많은 수의 해제가 누적되면 오래된 보류 해제가 삭제될 수 있습니다. 이 경우 이전에 해제된 배너가 다음 성공적인 동기화가 완료될 때까지 다시 나타날 수 있습니다. 이 위험을 최소화하려면 앱이 네트워크 연결을 다시 확보할 때마다 `requestBannersRefresh`를 호출하세요.
{% endalert %}

## 크기 및 크기 조정 {#dimensions-and-sizing}

배너 크기 및 크기 조정에 대해 알아야 할 사항은 다음과 같습니다:

- 컴포저에서 다양한 크기로 배너를 미리 볼 수 있지만, 해당 정보는 SDK에 저장되거나 전송되지 않습니다.
- HTML은 렌더링되는 컨테이너의 전체 너비를 차지합니다.
- 고정 크기 요소를 만들고 컴포저에서 해당 크기를 테스트하는 것을 권장합니다.

## 커스텀 속성 {#custom-properties}

배너 Campaign의 커스텀 속성을 사용하여 SDK를 통해 키-값 데이터를 검색하고 앱의 동작이나 외관을 수정할 수 있습니다. 예를 들어 다음과 같은 작업을 수행할 수 있습니다:

- 서드파티 분석 또는 통합을 위한 메타데이터를 전송합니다.
- `timestamp` 또는 JSON 오브젝트와 같은 메타데이터를 사용하여 조건 로직을 트리거합니다.
- `ratio` 또는 `format`과 같은 포함된 메타데이터를 기반으로 배너의 동작을 제어합니다.

### 필수 조건

배너 Campaign에 [커스텀 속성을 추가]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#custom-properties)해야 합니다. 또한 커스텀 속성에 접근하기 위해 필요한 최소 SDK 버전은 다음과 같습니다:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### 커스텀 속성에 접근하기 {#access-custom-properties}

배너의 커스텀 속성에 접근하려면 대시보드에서 정의된 속성 유형에 따라 다음 메서드 중 하나를 사용하세요. 키가 해당 유형의 속성과 일치하지 않거나 존재하지 않으면 메서드는 `null`을 반환합니다.

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