{% alert important %}
iOS 14以降、おおよその位置情報の権限のみを選択したユーザーに対しては、ジオフェンスが確実に動作しません。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1: Brazeで有効にする {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### ステップ 2: アプリの位置情報サービスを有効にする {#step-2-enable-your-apps-location-services}

デフォルトでは、Brazeの位置情報サービスは有効になっていません。アプリで有効にするには、以下のステップを完了してください。ステップごとのチュートリアルについては、[チュートリアル: Brazeのロケーションとジオフェンス](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)を参照してください。

#### ステップ 2.1: `BrazeLocation`モジュールを追加する {#step-21-add-the-brazelocation-module}

Xcodeで、**General**タブを開きます。**Frameworks, Libraries, and Embedded Content**の下に、`BrazeLocation`モジュールを追加します。

![XcodeプロジェクトにBrazeLocationモジュールを追加する]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### ステップ 2.2: `Info.plist`を更新する {#step-22-update-your-infoplist}

`info.plist`で、アプリケーションが位置情報を追跡する必要がある理由を説明する`String`値を以下のキーのいずれかに割り当てます。この文字列は、ユーザーが位置情報サービスの許可を求められる際に表示されるため、この機能を有効にすることでアプリにどのような価値があるかを明確に説明してください。

- `NSLocationAlwaysAndWhenInUseUsageDescription`
- `NSLocationWhenInUseUsageDescription`

![XcodeでのInfo.plistの位置情報文字列]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Appleは`NSLocationAlwaysUsageDescription`を非推奨にしました。詳細については、[Appleの開発者ドキュメント](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)を参照してください。
{% endalert %}

### ステップ 3: コード内でジオフェンスを有効にする {#step-3-enable-geofences-in-your-code}

アプリのコード内で、[`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)インスタンスを初期化する`configuration`オブジェクトの`location.geofencesEnabled`を`true`に設定してジオフェンスを有効にします。その他の`location`設定オプションについては、[Braze Swift SDKリファレンス](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class)を参照してください。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Additional configuration customization...

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### ステップ 3.1: バックグラウンドレポートを有効にする（任意） {#step-31-enable-background-reporting-optional}

デフォルトでは、ジオフェンスイベントはアプリがフォアグラウンドにある場合、またはすべてのアプリケーション状態を監視する`Always`権限を持っている場合にのみ監視されます。

ただし、アプリがバックグラウンドにある場合や[`When In Use`権限](#swift_request-authorization)を持っている場合にも、ジオフェンスイベントを監視することを選択できます。

これらの追加のジオフェンスイベントを監視するには、Xcodeプロジェクトを開き、**Signing & Capabilities**に移動します。**Background Modes**で、**Location updates**にチェックを入れます。

![Xcodeで、Background Modes > Location updates]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

次に、アプリのコードで`allowBackgroundGeofenceUpdates`を有効にします。これにより、Brazeは位置情報の更新を継続的に監視することで、アプリの「When In Use」ステータスを延長できます。この設定は、アプリがバックグラウンドにある場合にのみ機能します。アプリが再度開かれると、既存のバックグラウンドプロセスはすべて一時停止され、代わりにフォアグラウンドプロセスが優先されます。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
バッテリーの消耗とレート制限を防ぐため、アプリの特定のニーズに合った値に`distanceFilter`を設定してください。`distanceFilter`をより高い値に設定すると、アプリがユーザーの位置情報を頻繁にリクエストしすぎるのを防ぐことができます。
{% endalert %}

### ステップ 4: 承認をリクエストする {#request-authorization}

ユーザーから承認をリクエストする際は、`When In Use`または`Always`のいずれかの承認をリクエストします。

{% tabs local %}
{% tab When In Use %}
`When In Use`承認をリクエストするには、`requestWhenInUseAuthorization()`メソッドを使用します。

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
デフォルトでは、`requestAlwaysAuthorization()`はアプリに`When In Use`承認のみを付与し、しばらく経過した後に`Always`承認をユーザーに再度リクエストします。

ただし、最初に`requestWhenInUseAuthorization()`を呼び出し、初回の`When In Use`承認を受け取った後に`requestAlwaysAuthorization()`を呼び出すことで、ユーザーに即座にプロンプトを表示することもできます。

{% alert important %}
`Always`承認を求める即時プロンプトを出せるのは一度のみです。
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 手動でジオフェンスをリクエストする {#manually-request-geofences}

Braze SDKがバックエンドにジオフェンスをリクエストすると、ユーザーの現在位置をレポートし、レポートされた位置に基づいて最適に関連性が高いと判断されたジオフェンスを受け取ります。

最も関連性の高いジオフェンスを受信するためにSDKがレポートする位置をコントロールするには、希望する座標を提供してジオフェンスを手動でリクエストできます。

### ステップ 1: `automaticGeofenceRequests`を`false`に設定する {#step-1-set-automaticgeofencerequests-to-false}

[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:))に渡される`configuration`オブジェクトで、自動ジオフェンスリクエストを無効にできます。`automaticGeofenceRequests`を`false`に設定します。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### ステップ 2: 手動で`requestGeofences`を呼び出す {#step-2-call-requestgeofences-manually}

コード内で、適切な緯度と経度を指定してジオフェンスをリクエストします。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

## よくある質問（FAQ） {#faq}

### デバイスでジオフェンスが受信されないのはなぜですか {#why-am-i-not-receiving-geofences-on-my-device}

デバイスでジオフェンスが受信されているかどうかを確認するには、まず[SDKデバッガーツール]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk)を使用してSDKのログを確認してください。サーバーからジオフェンスが正常に受信されているか、また顕著なエラーがあるかどうかを確認できます。

以下は、デバイスでジオフェンスが受信されないその他の考えられる理由です。

#### iOSオペレーティングシステムの制限 {#ios-operating-system-limitations}

iOSオペレーティングシステムでは、特定のアプリに対して最大20個のジオフェンスしか保存できません。ジオフェンスを有効にすると、Brazeはこれら20個の利用可能スロットの一部を使用します。

アプリ内の他のジオフェンス関連機能が誤って、または意図せず妨げられるのを防ぐには、ダッシュボードで個々のアプリに対して位置情報ジオフェンスを有効にする必要があります。位置情報サービスが正しく動作するには、アプリで利用可能なジオフェンススポットがすべて使用されていないことを確認してください。

#### レート制限 {#rate-limiting}

Brazeは不要なリクエストを避けるため、1セッションあたり1回のジオフェンス更新に制限しています。

### Brazeと非Brazeのジオフェンス機能を両方使っている場合、どのように動作しますか {#how-does-it-work-if-i-am-using-both-braze-and-non-braze-geofence-features}

前述の通り、iOSでは単一のアプリが最大20個のジオフェンスを保存できます。このストレージは、Brazeと非Brazeのジオフェンスの両方で共有され、[CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager)によって管理されます。

例えば、アプリに非Brazeのジオフェンスが20個含まれている場合、Brazeのジオフェンスを追跡するストレージは存在しません（逆も同様です）。新しいジオフェンスを受信するには、[Appleの位置情報API](https://developer.apple.com/documentation/corelocation)を使用して、デバイス上の既存のジオフェンスの一部の監視を停止する必要があります。

### ジオフェンス機能は、デバイスがオフラインの状態で使用できますか {#can-the-geofences-feature-be-used-while-a-device-is-offline}

デバイスは、更新が行われるときだけインターネットに接続する必要があります。サーバーからジオフェンスを正常に受信した後は、デバイスがオフライン状態であっても、ジオフェンスのエントリや退出を記録することが可能です。これは、デバイスの位置情報がインターネット接続とは別個に動作するためです。

例えば、あるデバイスがセッション開始時にジオフェンスを正常に受信・登録した後、オフライン状態になったとします。その後、登録済みのジオフェンスのいずれかに入ると、Brazeキャンペーンをトリガーできます。

### アプリがバックグラウンド状態になったり終了したりすると、なぜジオフェンスが監視されなくなるのですか {#why-are-geofences-not-monitored-when-my-app-is-backgroundedterminated}

`Always`権限がない場合、Appleはアプリが使用されていない間、位置情報サービスの動作を制限します。これはオペレーティングシステムによって強制されるものであり、Braze SDKのコントロール範囲外です。Brazeはアプリがバックグラウンドにある間もサービスを実行するための個別の設定を提供していますが、ユーザーからの明示的な承認を得ずに終了されたアプリについては、これらの制限を回避する方法はありません。