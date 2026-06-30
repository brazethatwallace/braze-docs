{% multi_lang_include developer_guide/prerequisites/swift.md %}

{% alert tip %}
カスタムスキームのディープリンク、ユニバーサルリンク、「アプリ内でWeb URLを開く」の選択方法については、[iOSディープリンクガイド]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/)を参照してください。トラブルシューティングについては、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/)を参照してください。
{% endalert %}

## ディープリンクの処理 {#handling-deep-links}

### ステップ 1:スキームを登録する {#register-a-scheme}

ディープリンクを処理するには、`Info.plist` ファイルにカスタムスキームを記述する必要があります。ナビゲーション構造はディクショナリの配列によって定義されます。これらの各ディクショナリには、文字列の配列が含まれています。

Xcodeを使用して `Info.plist` ファイルを編集します。

1. 新しいキー `URL types` を追加します。Xcodeでは、これが自動的に `Item 0` というディクショナリを含む配列になります。
2. `Item 0` 内に、キー `URL identifier` を追加します。カスタムスキームに値を設定します。
3. `Item 0` 内に、キー `URL Schemes` を追加します。これは、自動的に `Item 0` 文字列を含む配列になります。
4. `URL Schemes` >> `Item 0` をカスタムスキームに設定します。

また、`Info.plist` ファイルを直接編集する場合は、次の仕様に従うこともできます。

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

### ステップ 2:スキームの許可リストを追加する {#step-2-add-a-scheme-allowlist}

`LSApplicationQueriesSchemes` キーをアプリの Info.plist ファイルに追加して、`canOpenURL(_:)` に渡すURLスキームを宣言する必要があります。この許可リストに含まれないスキームを呼び出そうとすると、デバイスのログにエラーが記録され、ディープリンクは開かれません。以下はこのエラーの例です。

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

たとえば、アプリ内メッセージをタップしたときにFacebookアプリが開かれるようにするには、アプリの許可リストにFacebookカスタムスキーム (`fb`) が含まれている必要があります。含まれていないと、ディープリンクが拒否されます。自分のアプリ内のページやビューに誘導するディープリンクでも、アプリのカスタムスキームがアプリの `Info.plist` に含まれている必要があります。

以下は許可リストの例です。

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

詳細については、`LSApplicationQueriesSchemes` キーに関する[Appleのドキュメント](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14)を参照してください。

### ステップ 3:ハンドラを実装する {#step-3-implement-a-handler}

アプリをアクティブにすると、iOSでメソッド [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) が呼び出されます。重要な引数は [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL) オブジェクトです。

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% endtabs %}

## App Transport Security (ATS)

[Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14)の定義によれば、「App Transport Securityは、アプリとWebサービス間の接続のセキュリティを向上させる機能です。この機能は、安全な接続のベストプラクティスに準拠したデフォルトの接続要件で構成されています。アプリでこのデフォルト動作をオーバーライドして、トランスポートセキュリティを無効にできます。」

ATSはデフォルトで適用されます。すべての接続がHTTPSを使用し、TLS 1.2で暗号化され、前方秘匿性が確保される必要があります。詳細については、[ATSを使用して接続するための要件](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35)を参照してください。Brazeによりエンドデバイスに提供されるすべての画像は、TLS 1.2をサポートし、ATSと互換性のあるコンテンツ配信ネットワーク（「CDN」）によって処理されます。

アプリケーションの `Info.plist` で例外として明示的に指定されていない限り、これらの要件を満たさない接続は、以下のようなエラーで失敗します。

**エラー例 1：**

```bash
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

**エラー例 2：**

```bash
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

ATSコンプライアンスは、モバイルアプリ内で開かれたリンク（クリックされたリンクのデフォルト処理）に適用され、Webブラウザーから外部で開かれたサイトには適用されません。

### ATSへの対応 {#working-with-ats}

ATSは次のいずれかの方法で処理できますが、**ATSの要件に準拠すること**を推奨します。

{% tabs local %}
{% tab Comply %}
Brazeの統合では、（アプリ内メッセージやプッシュキャンペーンなどから）ユーザーを誘導する既存のリンクがATSの要件を満たすようにすることで、ATS要件を満たすことができます。ATSの制限を回避する方法はありますが、リンクされたすべてのURLがATSに準拠するようにすることをお勧めします。Appleがアプリケーションのセキュリティをこれまで以上に重視していることを考えると、ATSの例外を許可する以下のアプローチがAppleによってサポートされる保証はありません。
{% endtab %}

{% tab Partially disable %}
特定のドメインやスキームのリンクのサブセットをATSルールの例外として処理することを許可できます。Brazeメッセージングチャネルで使用するすべてのリンクがATSに準拠しているか、例外として処理されている場合、Brazeの統合はATS要件を満たします。

ATSの例外としてドメインを追加するには、アプリの `Info.plist` ファイルに以下を追加します。

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

詳細については、[App Transport Securityのキー](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33)に関するAppleの記事を参照してください。
{% endtab %}

{% tab Fully disable %}
ATSを完全に無効にできます。ただし、セキュリティ保護が失われることと、将来のiOSとの互換性の両方を考慮して、この処理は推奨されないことに注意してください。ATSを無効にするには、アプリの `Info.plist` ファイルに以下を挿入します。

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
{% endtab %}
{% endtabs %}

## URLのデコード {#decoding-urls}

SDKでは、有効な `URL` を作成するためにリンクをパーセントエンコードします。適切な形式のURLで使用できないリンク文字（Unicode文字など）は、すべてパーセントエスケープされます。

エンコードされたリンクをデコードするには、`String` プロパティ [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding) を使用します。また、`BrazeDelegate.braze(_:shouldOpenURL:)` で `true` を返す必要があります。アプリによるURLの処理をトリガーするには、アクションの呼び出しが必要です。例：

{% tabs %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% endtabs %}

## アプリ設定へのディープリンク {#deep-linking-to-app-settings}

Brazeのプッシュ通知やアプリ内メッセージから `UIApplicationOpenSettingsURLString` を活用して、ユーザーをアプリの設定画面にディープリンクできます。

ユーザーをアプリからiOS設定に移動させる手順は以下のとおりです。
1. まず、アプリケーションが[スキームベースのディープリンク](#swift_register-a-scheme)または[ユニバーサルリンク](#swift_universal-links)用に設定されていることを確認します。
2. **設定**ページへのディープリンクのURI（`myapp://settings` や `https://www.braze.com/settings` など）を決定します。
3. カスタムスキームベースのディープリンクを使用している場合は、`application:openURL:options:` メソッドに次のコードを追加します。

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path  = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## カスタマイズオプション {#customization-options}

### デフォルトWebViewのカスタマイズ {#default-webview-customization}

`Braze.WebViewController` クラスは、Webディープリンクに対して「アプリ内でWeb URLを開く」が選択されている場合に、SDKによって開かれるWeb URLを表示します。

`Braze.WebViewController` は、[`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/) デリゲートメソッドを使用してカスタマイズできます。

### リンク処理のカスタマイズ {#linking-handling-customization}

`BrazeDelegate` プロトコルを使用して、ディープリンク、Web URL、ユニバーサルリンクなどのURLの処理をカスタマイズできます。Brazeの初期化中にデリゲートを設定するには、`Braze` インスタンスにデリゲートオブジェクトを設定します。その後、URIを処理する前にBrazeがデリゲートの `shouldOpenURL` 実装を呼び出します。

プッシュ通知やアプリ内メッセージで**アプリ内でWeb URLを開く**を使用すると、Brazeは [`Braze.URLContext`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/urlcontext) で `context.useWebView == true` を渡します。メッセージがシステムブラウザーでURLを開く場合、`useWebView` は `false` になります。`braze(_:shouldOpenURL:)` で `context.useWebView` を確認して、カスタム処理を分岐させます。たとえば、キャンペーンがアプリ内表示をリクエストした場合にのみアプリ内の `WebViewController` を開くことができます。

#### ユニバーサルリンク {#universal-links}

Brazeでは、プッシュ通知、アプリ内メッセージ、Content Cardsでユニバーサルリンクがサポートされています。ユニバーサルリンクのサポートを有効にするには、[`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) を `true` に設定する必要があります。

有効にすると、Brazeは [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) メソッドを介してアプリの `AppDelegate` にユニバーサルリンクを転送します。

また、ユニバーサルリンクを処理するようアプリケーションを設定する必要があります。[Appleのドキュメント](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)を参照し、アプリケーションがユニバーサルリンクに関して正しく設定されていることを確認してください。

{% alert warning %}
ユニバーサルリンクの転送には、アプリケーション権限へのアクセスが必要です。アプリケーションをシミュレーターで実行している場合、これらの権限は直接使用できず、ユニバーサルリンクはシステムハンドラに転送されません。
シミュレータービルドのサポートを追加するには、アプリケーションの `.entitlements` ファイルを _Copy Bundle Resources_ ビルドフェーズに追加します。詳細については、[`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) のドキュメントを参照してください。
{% endalert %}

{% alert note %}
SDKでは、ドメインの `apple-app-site-association` ファイルに対してクエリは実行されません。ドメイン名のみを確認することで、ユニバーサルリンクと通常のURLを区別します。そのため、SDKでは[関連ドメインのサポート](https://developer.apple.com/documentation/xcode/supporting-associated-domains)ごとに `apple-app-site-association` で定義される除外ルールは考慮されません。
{% endalert %}

## 例 {#examples}

### BrazeDelegate

以下は `BrazeDelegate` の使用例です。詳細については、[Braze Swift SDKリファレンス](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate)を参照してください。

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}