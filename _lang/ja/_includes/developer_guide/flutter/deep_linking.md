## 前提条件 {#prerequisites}

{% tabs local %}
{% tab iOS %}
Flutter iOSアプリにディープリンクを実装する前に、`Info.plist`ファイルでURLスキームを設定してください。詳細については、[iOSのディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#url-schemes)を参照してください。
{% endtab %}

{% tab Android %}
Flutter Androidの場合、Dartレイヤーでディープリンクを処理するのであれば、ネイティブ側の追加設定は不要です。この記事で紹介する最小限の実装で、ほとんどのFlutterアプリには十分です。

{% alert warning %}
Brazeのネイティブ`com_braze_handle_push_deep_links_automatically`フラグは、Androidではデフォルトで`false`に設定されています。`braze.xml`でこれを`true`に設定しない場合、ユーザーがプッシュ通知をタップしても、`push_opened`イベントはDartリスナーに届きますが、アプリが自動的にフォアグラウンドに表示されたり、ディープリンク先にルーティングされたりしません。詳細については、[ディープリンクを追加する（Android）]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android)を参照してください。
{% endalert %}

高度なネイティブレイヤーのリンク処理（カスタム`IBrazeDeeplinkHandler`の実装など）が必要な場合は、[Androidのディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android)を参照してください。
{% endtab %}
{% endtabs %}

## ディープリンクの実装 {#implementing-deep-linking}

### ステップ1:Flutterの組み込みハンドリングを設定する {#step-1-set-up-flutters-built-in-handling}

{% tabs %}
{% tab iOS %}
1. Xcodeプロジェクトで、`Info.plist`ファイルを開きます。
2. 新しいキーと値のペアを追加します。
3. キーを`FlutterDeepLinkingEnabled`に設定します。
4. タイプを`Boolean`に設定します。
5. 値を`YES`に設定します。
    ![キーと値のペアが追加されたプロジェクトの`Info.plist`ファイルの例。]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File"){: width="501" height="118"}
{% endtab %}

{% tab Android %}
1. Android Studioプロジェクトで、`AndroidManifest.xml`ファイルを開きます。
2. `activity`タグ内の`.MainActivity`を見つけます。
3. `activity`タグ内に、以下の`meta-data`タグを追加します。
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### ステップ2:Dartレイヤーにデータを転送する（オプション） {#step-2-forward-data-to-the-dart-layer-optional}

ネイティブ、ファーストパーティ、またはサードパーティのリンクハンドリングを使用して、ユーザーをアプリ内の特定の場所に誘導したり、特定の関数を呼び出したりするなどの複雑なユースケースに対応できます。

#### 例:アラートダイアログへのディープリンク {#example-deep-linking-to-an-alert-dialog}

{% alert note %}
以下の例は追加のパッケージに依存していませんが、同様のアプローチを使用してネイティブ、ファーストパーティ、またはサードパーティのパッケージ（[`go_router`](https://pub.dev/packages/go_router)など）を実装できます。追加のDartコードが必要になる場合があります。
{% endalert %}

まず、ネイティブレイヤーでメソッドチャネルを使用して、ディープリンクのURL文字列データをDartレイヤーに転送します。

{% tabs %}
{% tab iOS %}
```swift
extension AppDelegate {

  // Delegate method for handling custom scheme links.
  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    forwardURL(url)
    return true
  }

  // Delegate method for handling universal links.
  override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
      return false
    }
    forwardURL(url)
    return true
  }

  private func forwardURL(_ url: URL) {
    guard let controller: FlutterViewController = window?.rootViewController as? FlutterViewController else { return }
    let deepLinkChannel = FlutterMethodChannel(name: "deepLinkChannel", binaryMessenger: controller.binaryMessenger)
    deepLinkChannel.invokeMethod("receiveDeepLink", arguments: url.absoluteString)
  }

}
```
{% endtab %}

{% tab Android %}
```kotlin
class MainActivity : FlutterActivity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    handleDeepLink(intent)
  }

  override fun onNewIntent(intent: Intent) {
      super.onNewIntent(intent)
    handleDeepLink(intent)
  }

  private fun handleDeepLink(intent: Intent) {
    val binaryMessenger = flutterEngine?.dartExecutor?.binaryMessenger
    if (intent?.action == Intent.ACTION_VIEW && binaryMessenger != null) {
      MethodChannel(binaryMessenger, "deepLinkChannel")
        .invokeMethod("receivedDeepLink", intent?.data.toString())
    }
  }

}
```
{% endtab %}
{% endtabs %}

次に、Dartレイヤーでコールバック関数を使用して、前に送信されたURL文字列データを使用してアラートダイアログを表示します。

```dart
MethodChannel('deepLinkChannel').setMethodCallHandler((call) async {
  deepLinkAlert(call.arguments, context);
});

void deepLinkAlert(String link, BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("Deep Link Alert"),
        content: Text("Opened with deep link: $link"),
        actions: <Widget>[
          TextButton(
            child: Text("Close"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}
```
