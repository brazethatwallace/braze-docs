---
nav_title: トラックセッション
article_title: トラックセッション
page_order: 3.3
description: "Braze SDKを使用してセッションを追跡する方法について説明します。"
---

# トラックセッション {#track-sessions}

> Braze SDKを使用してセッションを追跡する方法について説明します。

{% alert note %}
リストされていないラッパーSDKの場合は、代わりに関連するネイティブAndroidまたはSwiftメソッドを使用してください。
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## 非アクティブ状態の定義 {#defining-inactivity}

Web SDKでセッションライフサイクルを効果的に管理するには、非アクティブ状態がどのように定義され、測定されるかを理解することが重要です。非アクティブ状態とは、Braze Web SDKがユーザーからのトラッキングイベントを検出しない期間のことを指します。

### 非アクティブ状態の測定方法 {#how-inactivity-is-measured}

Web SDKは、[SDKトラッキングイベント]({{site.baseurl}}/user_guide/data/activation/events/events_overview)に基づいて非アクティブ状態を追跡します。SDKは内部タイマーを管理しており、トラッキングイベントが送信されるたびにリセットされます。設定されたタイムアウト期間内にSDKトラッキングイベントが発生しない場合、セッションは非アクティブとみなされ終了します。

Web SDKにおけるセッションライフサイクルの実装方法の詳細については、[Braze Web SDK GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts)のセッション管理ソースコードを参照してください。

**デフォルトでアクティビティとしてカウントされるもの：**
- Webアプリの起動またはリフレッシュ
- Brazeが制御するUI要素との操作（[In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages)や[Content Cards]({{site.baseurl}}/developer_guide/content_cards)など）
- トラッキングイベントを送信するSDKメソッドの呼び出し（[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events)や[ユーザー属性の更新]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)など）

**デフォルトでアクティビティとしてカウントされないもの：**
- 別のブラウザタブへの切り替え
- ブラウザウィンドウの最小化
- ブラウザのフォーカスまたはブライベント
- ページ上のスクロールやマウスの動き

{% alert note %}
Web SDKは、ブラウザの可視性の変化、タブの切り替え、またはユーザーフォーカスを自動的に追跡しません。ただし、ブラウザの[Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)を使用してカスタムイベントリスナーを実装し、[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)をBrazeに送信することで、これらのブラウザレベルの操作を追跡できます。実装例については、[カスタム非アクティブ状態のトラッキング](#tracking-custom-inactivity)を参照してください。
{% endalert %}

### セッションタイムアウトの設定 {#session-timeout-configuration}

デフォルトでは、Web SDKはトラッキングイベントが30分間発生しない場合にセッションを非アクティブとみなします。SDKの初期化時に`sessionTimeoutInSeconds`パラメーターを使用して、このしきい値をカスタマイズできます。このパラメーターの設定方法（コード例を含む）の詳細については、[デフォルトセッションタイムアウトの変更](#changing-the-default-session-timeout)を参照してください。

### 例：非アクティブ状態のシナリオを理解する {#example-understanding-inactivity-scenarios}

以下のシナリオを考えてみましょう：

1. ユーザーがWebサイトを開くと、SDKが[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)を呼び出してセッションを開始します。
2. ユーザーが別のブラウザタブに切り替えて、別のWebサイトを30分間閲覧します。
3. この間、あなたのWebサイト上ではSDKトラッキングイベントは発生しません。
4. 30分間の非アクティブ状態の後、セッションは自動的に終了します。
5. ユーザーがあなたのWebサイトのタブに戻り、SDKイベント（ページの表示やコンテンツとの操作など）をトリガーすると、新しいセッションが開始されます。

### カスタム非アクティブ状態のトラッキング {#tracking-custom-inactivity}

ブラウザの可視性やタブの切り替えに基づいて非アクティブ状態を追跡する必要がある場合は、JavaScriptコードにカスタムイベントリスナーを実装してください。`visibilitychange`などのブラウザイベントを使用してユーザーがページを離れたことを検出し、手動で[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events)をBrazeに送信するか、適切なタイミングで[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)を呼び出します。

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

カスタムイベントのログ記録の詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events)を参照してください。セッションライフサイクルとタイムアウト設定の詳細については、[デフォルトセッションタイムアウトの変更](#change-session-timeout)を参照してください。

## セッション更新の配信登録 {#subscribing-to-session-updates}

### ステップ1: 更新を配信登録する {#step-1-subscribe-to-updates}

セッション更新を配信登録するには、`subscribeToSessionUpdates()` メソッドを使用します。

{% tabs %}
{% tab web %}
現時点では、Web Braze SDKではセッション更新の配信登録はサポートされていません。
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
セッション終了コールバックを登録すると、アプリがフォアグラウンドに戻ったときに発火します。セッション時間は、アプリが開かれるかフォアグラウンドに入った時点から、閉じられるかバックグラウンドに移行した時点までで計測されます。

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

非同期ストリームを配信登録するには、代わりに [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) を使用できます。

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
React Native SDKでは、セッション更新を直接配信登録するメソッドは公開されていません。セッションライフサイクルは基盤となるネイティブSDKによって管理されるため、更新を配信登録するには、**Android** または **Swift** タブのネイティブプラットフォームのアプローチを使用してください。
{% endtab %}
{% endtabs %}

### ステップ2: セッショントラッキングをテストする（任意） {#step-2-test-session-tracking-optional}

セッショントラッキングをテストするには、デバイスでセッションを開始し、Brazeダッシュボードを開いて該当するユーザーを検索します。ユーザープロファイルで **Sessions Overview** を選択します。メトリクスが期待どおりに更新されていれば、セッショントラッキングは正しく機能しています。

![ユーザープロファイルのセッション概要セクション。セッション数、最終使用日、初回使用日が表示されている。]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
アプリ固有の詳細は、複数のアプリを使用したことがあるユーザーにのみ表示されます。
{% endalert %}

## デフォルトのセッションタイムアウトの変更 {#change-session-timeout}

セッションが自動的にタイムアウトするまでの時間を変更できます。

{% tabs %}
{% tab web %}
デフォルトでは、セッションタイムアウトは`30`分に設定されています。これを変更するには、`sessionTimeoutInSeconds`オプションを[`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)関数に渡します。`1`以上の任意の整数に設定できます。

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
デフォルトでは、セッションタイムアウトは`10`秒に設定されています。これを変更するには、`braze.xml`ファイルを開き、`com_braze_session_timeout`パラメータを追加します。`1`以上の任意の整数に設定できます。

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
デフォルトでは、セッションタイムアウトは`10`秒に設定されています。これを変更するには、[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class)に渡される`configuration`オブジェクトで`sessionTimeout`を設定します。`1`以上の任意の整数に設定できます。

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
React Native SDKはセッション管理のためにネイティブSDKに依存しています。デフォルトのセッションタイムアウトを変更するには、ネイティブレイヤーで設定してください。

- **Android：**`braze.xml`ファイルで`com_braze_session_timeout`を設定します。詳細は、**Android**タブを選択してください。
- **iOS：**`Braze.Configuration`オブジェクトで`sessionTimeout`を設定します。詳細は、**Swift**タブを選択してください。
{% endtab %}
{% endtabs %}

{% alert note %}
セッションタイムアウトを設定すると、すべてのセッションセマンティクスが設定されたタイムアウトに自動的に拡張されます。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### ユーザープロファイルのセッション数が0 {#user-profile-has-0-sessions}

ユーザーがSDKの外部で作成された場合、ユーザープロファイルのセッション数が0になることがあります。

- **REST APIによる作成:** [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを通じてリクエストに`app_id`を含めてユーザーを作成した場合、プロファイルはそのアプリに関連付けられますが、そのユーザーに対してSDKが初期化されていないためセッションデータはありません。
- **CSVインポートによる作成:** 最初のセッションや最後のセッションのフィールドに値を設定せずに[CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)でユーザーをインポートした場合、プロファイルはセッション数0で作成されます。

### 一部のユーザーのセッションが記録されない {#some-users-are-not-logging-sessions}

セッションはSDKの初期化後にのみトラッキングされるため、SDKの初期化をトリガーしないユーザーはセッションを記録しません。これは通常、ログインフロー、同意プロンプト、またはフィーチャーフラグの後に初期化を遅延させるなど、SDKの初期化前に条件付きロジックを使用している場合に発生します。実装ガイダンスについては、[遅延初期化]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#step-2-set-up-delayed-initialization-optional)を参照してください。このような場合、条件を満たさないユーザーはセッションを開始しません。

一部のユーザーがセッションを記録し、他のユーザーが記録していない場合は、以下の点を確認してください。

- **初期化ロジックを確認する。** 一部のユーザーやアプリのエントリポイントだけでなく、すべてのユーザーとアプリのエントリポイントに対してSDKが初期化されていることを確認してください。
- **最近のアプリの変更を確認する。** SDKの初期化に関する新しい条件付きロジックが、セッション数の急激な減少を引き起こしている可能性があります。
- **影響を受けているユーザーと受けていないユーザーを比較する。** アプリのバージョン、デバイスの種類、ユーザーフローの違いを特定し、特定のユーザーに対して初期化がスキップされている理由を明らかにしてください。

実装を確認しても問題が解決しない場合は、問題を再現し、サポートに連絡する前に以下の情報を収集してください。

- 問題を再現する手順
- 影響を受けるアプリのバージョン
- 問題発生時にキャプチャした[詳細SDKログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)（またはプラットフォーム別: [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_enabling-logs)、[Swift]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#swift_setting-the-log-level)、[Web]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web#web_logging)）
- SDKの初期化に使用するコードスニペット
- 初期化前に適用される条件付きロジックの概要