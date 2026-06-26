---
nav_title: 配置の管理
article_title: Braze SDKのバナー配置を管理する
description: "Braze SDKでバナー配置の作成と管理方法を学びます。配置固有のプロパティへのアクセスやインプレッションの記録についても説明します。"
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# バナー配置を管理する {#manage-banner-placements}

> Braze SDKでバナー配置の作成と管理方法を学びます。配置固有のプロパティへのアクセスやインプレッションの記録についても説明します。一般的な情報については、[バナーについて]({{site.baseurl}}/developer_guide/banners/)を参照してください。

## 配置リクエストについて {#requests}

{% multi_lang_include banners/placement_requests.md %}

## 配置を作成する {#create-a-placement}

### 前提条件 {#prerequisites}

バナー配置を作成するために必要な最小SDKバージョンは以下の通りです。

{% multi_lang_include sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### ステップ2:アプリの配置を更新する {#requestBannersRefresh}

配置は、以下に説明する更新メソッドを呼び出すことで更新できます。`subscribeToBannersUpdates`がアクティブな場合、SDKは新しいセッションの開始時および`changeUser`を呼び出したときに、キャッシュされた配置IDを自動的に再パブリッシュします。この自動更新はレート制限トークンを消費しません。

{% alert tip %}
バナーのダウンロードや表示の遅延を避けるため、できるだけ早く配置を更新してください。
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

### ステップ3:更新をリッスンする {#subscribeToBannersUpdates}

{% alert tip %}
このガイドのSDKメソッドを使ってバナーを挿入する場合、すべての分析イベント（インプレッションやクリックなど）は自動的に処理され、インプレッションはバナーが表示されているときのみ記録されます。
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Web Braze SDKでvanilla JavaScriptを使用している場合、[`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)を使って配置の更新をリッスンし、[`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)を呼び出してフェッチします。

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
Web Braze SDKでReactを使用している場合、`useEffect`フック内で[`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates)を設定し、リスナーを登録した後に[`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh)を呼び出します。

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
バナー更新リスナーは、SDKのインメモリバナー状態を反映します。1回の更新には、最新の`requestRefresh`呼び出しの配置IDだけでなく、すでにキャッシュされている配置（たとえば、以前の更新、別の画面、またはSDKの自動処理によるもの）も含まれる場合があります。特定の配置のみに関心がある場合は、リスナー内で各バナーの配置IDを確認し、それ以外はスキップしてください。リスナーを登録したら、Brazeから同期したい配置に対して`requestRefresh`を呼び出します。
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
バナー更新リスナーは、SDKのインメモリバナー状態を反映します。1回の更新には、最新の`requestBannersRefresh`呼び出しの配置IDだけでなく、すでにキャッシュされている配置（たとえば、以前の更新、別の画面、またはSDKの自動処理によるもの）も含まれる場合があります。特定の配置のみに関心がある場合は、リスナー内で各バナーの配置IDを確認し、それ以外はスキップしてください。リスナーを登録したら、Brazeから同期したい配置に対して`requestBannersRefresh`を呼び出します。
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

### ステップ4:配置IDを使って挿入する {#insertBanner}

{% alert tip %}
完全なステップバイステップのチュートリアルについては、[配置IDによるバナーの表示]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners/)を参照してください。
{% endalert %}

{% tabs %}
{% tab Web %}

バナーのコンテナ要素を作成します。幅と高さを必ず設定してください。

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Web Braze SDKでvanilla JavaScriptを使用している場合、[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)メソッドを呼び出してコンテナ要素の内部HTMLを置き換えます。

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
Web Braze SDKでReactを使用している場合、[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)メソッドを`ref`と共に呼び出してコンテナ要素の内部HTMLを置き換えます。

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
インプレッションをトラッキングするには、`isControl`の場合でも必ず`insertBanner`を呼び出してください。その後、コンテナを非表示にしたり折りたたんだりできます。
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
Javaコードでバナーを取得するには、以下を使用します。

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

次のXMLを含めることで、Androidビューレイアウトでバナーを作成できます。

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Android Viewsを使用している場合は、次のXMLを使用します。

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Jetpack Composeを使用するには、アプリモジュールに`com.braze:android-sdk-jetpack-compose`アーティファクトを追加します。他のBraze Android SDK依存関係と同じバージョンを使用してください。このモジュールは`android-sdk-ui`とは別で、`com.braze.jetpackcompose.banners`配下の[`Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html)コンポーザブルを提供します。

{% alert note %}
一部のCompose UIライブラリは独自の`Banner`コンポーザブルを定義しています。BrazeのAPIを呼び出すには、`com.braze.jetpackcompose.banners.Banner`を明示的にインポートしてください。
{% endalert %}

```kotlin
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
    Banner(placementId = "global_banner")
}
```

オプションで`heightCallback`を渡すと、バナーサイズが変更されたときにレンダリングされた高さ（dp単位）を受け取ることができます。詳細については、[`Banner`のKDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html)を参照してください。

Jetpack Composeモジュールを追加しない場合は、[`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html)を[`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView)でラップします。

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

Kotlinでバナーを取得するには、以下を使用します。
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

[React Nativeの新しいアーキテクチャ](https://reactnative.dev/architecture/landing-page)を使用している場合は、`BrazeBannerView`をFabricコンポーネントとして`AppDelegate.mm`に登録する必要があります。

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
最もシンプルな統合方法として、以下のJavaScript XML（JSX）スニペットをビュー階層に追加し、配置IDだけを指定します。

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

React Nativeでバナーのデータモデルを取得したり、ユーザーのキャッシュにその配置が存在するかどうかを確認するには、以下を使用します。

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
最もシンプルな統合方法として、以下のウィジェットをビュー階層に追加し、配置IDだけを指定します。

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

`getBanner`メソッドを使って、ユーザーのキャッシュにその配置が存在するかどうかを確認できます。

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

### ステップ5:テストバナーを送信する（オプション） {#handling-test-cards}

バナーCampaignを開始する前に、[テストバナーを送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=banners)して統合を確認できます。テストバナーは別のインメモリキャッシュに保存され、アプリの再起動後は保持されません。追加のセットアップは不要ですが、テストを表示できるようにテストデバイスがフォアグラウンドのプッシュ通知を受信できる必要があります。

{% alert note %}
テストバナーは他のバナーと同じですが、次のアプリセッションで削除される点が異なります。
{% endalert %}

## インプレッションを記録する {#log-impressions}

Brazeは、SDKメソッドを使ってバナーを挿入する際に、表示されているバナーのインプレッションを自動的に記録します&#8212;そのため、インプレッションを手動でトラッキングする必要はありません。

## クリックを記録する {#logging-clicks}

バナーのクリックを記録するために使用するメソッドは、バナーのレンダリング方法とクリックハンドラーの配置場所によって異なります。

### 標準バナーコンテンツ（自動） {#standard-banner-content-automatic}

デフォルトの標準SDKメソッドを使ってバナーを挿入しており、バナーが標準のエディターコンポーネント（画像、ボタン、テキスト）を使用している場合、クリックは自動的にトラッキングされます。SDKがこれらの要素にクリックリスナーをアタッチするため、追加のコードは不要です。

### カスタムコードブロック {#custom-code-blocks}

バナーがBrazeダッシュボードの**カスタムコード**エディターブロックを使用している場合、そのカスタムHTML内からクリックを記録するには`brazeBridge.logClick()`を使用する必要があります。これは、SDKメソッドを使ってバナーをレンダリングする場合でも同様です。SDKはカスタムコード内の要素にリスナーを自動的にアタッチできないためです。

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

完全なリファレンスについては、[バナー用のカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#custom-code)を参照してください。`brazeBridge`は、バナーの内部HTMLと親Braze SDKの間の通信レイヤーを提供します。

### カスタムUI実装（ヘッドレス） {#custom-ui-implementations-headless}

バナーのHTMLをレンダリングする代わりに、バナーの[カスタムプロパティ](#custom-properties)を使って完全にカスタムのUIを構築する場合、アプリケーションコードからクリックとインプレッションを手動で記録する必要があります。SDKがバナーをレンダリングしていないため、カスタムUI要素とのインタラクションを自動的にトラッキングする方法がありません。

メソッドシグネチャと詳細については、[Braze SDKリファレンスドキュメント]({{site.baseurl}}/developer_guide/references/)を参照してください。

#### インプレッションを記録する {#logging-impressions}

カスタムUIがバナーを「閲覧済み」と見なしたときに、プラットフォームのバナーインプレッションメソッドを呼び出します。重複イベントを避けるために、インプレッションとしてカウントする条件について堅牢なロジックを構築してください。たとえば、バナーがビューポートに入ったとき（または同等のタイミング）にのみ記録し、同じバナーがスクロールで再び表示されたときやコンポーネントが新しいビューイベントなしに再レンダリングされたときには再度記録しないようにします。

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
[Web SDKリファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions)
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
[Android SDKリファレンス](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-impression.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logImpression()
}
```
[Swift SDKリファレンス](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logimpression())
{% endtab %}
{% tab React Native %}
```javascript
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");
```
最新のメソッドシグネチャについては、[React Native SDKリポジトリ](https://github.com/braze-inc/braze-react-native-sdk)を参照してください。
{% endtab %}
{% tab Flutter %}
```dart
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");
```
[Flutter SDKリファレンス](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerImpression.html)
{% endtab %}
{% endtabs %}

#### クリックを記録する

ユーザーがカスタムバナー（または特定のボタン）をタップしたときに、プラットフォームのバナークリックメソッドを呼び出します。クリックが特定のボタンに対するものである場合は、オプションの`buttonId`を渡して、分析がクリックを正しく帰属できるようにします。

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
[Web SDKリファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick)
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
[Android SDKリファレンス](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-click.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logClick(buttonId: buttonId)  // buttonID is optional
}
```
[Swift SDKリファレンス](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logclick(buttonid:))
{% endtab %}
{% tab React Native %}
```javascript
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
最新のメソッドシグネチャについては、[React Native SDKリポジトリ](https://github.com/braze-inc/braze-react-native-sdk)を参照してください。
{% endtab %}
{% tab Flutter %}
```dart
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
[Flutter SDKリファレンス](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerClicked.html)
{% endtab %}
{% endtabs %}

## 非表示を記録する {#log-dismissals}

バナーの非表示は、ユーザーが能動的にバナーを閉じたときに、プログラムで配置からバナーを削除します。一度非表示にすると、そのユーザーに対してバナーは抑制されます。次に配置リストが更新されたとき、ユーザーが対象であれば新しいバナーが返されます。

### 前提条件

バナーの非表示を記録するために必要な最小SDKバージョンは以下の通りです。

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### 統合 {#integrations}

#### 標準バナー統合（ドラッグ＆ドロップエディター） {#standard-banner-integrations-drag-and-drop-editor}

バナーがドラッグ＆ドロップエディターを使用しており、非表示ボタンコンポーネントが含まれている場合、追加のコードは不要です。ユーザーが非表示ボタンをクリックすると、メッセージが非表示になり、非表示がトリガーされ、分析用の非表示イベントが記録されます。

#### カスタムコードブロック

バナーが**カスタムコード**エディターブロックを使用している場合、バナーのHTML内から`brazeBridge.closeMessage()`を使って直接非表示をトリガーできます。

```html
<button onclick="brazeBridge.closeMessage()">
  Dismiss
</button>
```

### バナー非表示時にカスタム分析を記録する {#log-custom-analytics-on-banner-dismissal}

バナーの非表示時にカスタム分析の記録などの追加ロジックを実行するには、バナービューのオプションの`onDismiss`コールバックをオーバーライドします。デフォルトでは、このコールバックは空です。

{% tabs %}
{% tab Web %}
Web SDKには`insertBanner`に専用の`onDismiss`コールバックがありません。代わりに、`subscribeToBannersUpdates`を使用して、更新されたバナーマップにバナーが存在しなくなったかどうかを確認することで、バナーが非表示にされたことを検出します。

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
[`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html)のオプションの[`onDismissCallback`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/on-dismiss-callback.html)プロパティを設定します。

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

### 保留中の非表示のストレージ上限 {#pending-dismissal-storage-cap}

非表示イベントは、次の`requestBannersRefresh`呼び出し時にBrazeサーバーに同期されるまで、保留中のエントリとしてローカルに保存されます。

{% alert warning %}
まれに、同期が成功しないまま大量の非表示が蓄積された場合、古い保留中の非表示が削除されることがあります。この場合、以前に非表示にしたバナーが次の同期が成功するまで再表示される可能性があります。このリスクを最小限に抑えるには、アプリがネットワーク接続を回復するたびに`requestBannersRefresh`を呼び出してください。
{% endalert %}

## サイズと寸法 {#dimensions-and-sizing}

バナーのサイズと寸法について知っておくべきことは以下の通りです。

- コンポーザーではさまざまなサイズでバナーをプレビューできますが、その情報は保存されず、SDKに送信されません。
- HTMLは、レンダリングされるコンテナの全幅を使用します。
- 固定サイズの要素を作成し、そのサイズをコンポーザーでテストすることをお勧めします。

## カスタムプロパティ {#custom-properties}

バナーCampaignのカスタムプロパティを使って、SDKを通じてキーと値のデータを取得し、アプリの動作や外観を変更できます。たとえば、以下のようなことが可能です。

- サードパーティの分析ツールや統合サービス向けにメタデータを送信する。
- `timestamp`やJSONオブジェクトなどのメタデータを使って条件分岐ロジックをトリガーする。
- `ratio`や`format`などのメタデータに基づいてバナーの動作をコントロールする。

### 前提条件

バナーCampaignに[カスタムプロパティを追加]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#custom-properties)する必要があります。さらに、カスタムプロパティにアクセスするために必要な最小SDKバージョンは以下の通りです。

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### カスタムプロパティにアクセスする {#access-custom-properties}

バナーのカスタムプロパティにアクセスするには、ダッシュボードで定義されたプロパティの型に基づいて、以下のいずれかのメソッドを使用します。キーがその型のプロパティと一致しない場合、またはキーが存在しない場合、メソッドは`null`を返します。

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