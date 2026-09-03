---
nav_title: 位置情報とジオフェンス
article_title: iOSの位置情報とジオフェンス
platform: iOS
page_order: 6
description: "このリファレンス記事では、iOSアプリケーションに位置情報とジオフェンスを実装する方法について説明します。"
tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 位置情報とジオフェンス {#locations-and-geofences}

iOSのジオフェンスをサポートするには:

1. 統合がバックグラウンドプッシュ通知に対応している必要があります。
2. Brazeジオフェンスを、SDKを通じて[有効にする]({{site.baseurl}}/developer_guide/geofences?sdktab=swift)必要があります。位置情報の収集を有効にする（暗黙的）か、ジオフェンスの収集を明示的に有効にすることで設定できます。デフォルトでは有効になっていません。

{% alert important %}
iOS 14の時点では、おおよその位置情報の提供許可を選択しているユーザーの場合、ジオフェンスが確実に機能しないことがあります。
{% endalert %}

## ステップ1: バックグラウンドプッシュを有効にする {#step-1-enable-background-push}

ジオフェンスの同期戦略を十分に活用するには、標準的なプッシュ統合の完了に加えて、[バックグラウンドプッシュ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications#use-silent-push-notifications-to-trigger-background-work)を有効にする必要があります。

## ステップ2: ジオフェンスを有効にする {#step-2-enable-geofences}

デフォルトでは、ジオフェンスは自動位置情報の収集が有効かどうかに基づいて有効になります。`Info.plist`ファイルを使用してジオフェンスを有効にできます。`Info.plist`ファイルに`Braze`ディクショナリを追加します。`Braze`ディクショナリ内に、`EnableGeofences`ブールサブエントリを追加し、値を`YES`に設定します。なお、Braze iOS SDK v4.0.2より前のバージョンでは、`Braze`の代わりにディクショナリキー`Appboy`を使用する必要があります。

アプリ起動時に[`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24)メソッドを使用してジオフェンスを有効にすることもできます。`appboyOptions`ディクショナリで、`ABKEnableGeofencesKey`を`YES`に設定します。例:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## ステップ3: Brazeのバックグラウンドプッシュを確認する {#step-3-check-for-braze-background-push}

Brazeはバックグラウンドプッシュ通知を使用してジオフェンスをデバイスに同期します。[iOSカスタマイズ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push)の記事に従って、Brazeのジオフェンス同期通知を受信した際にアプリが意図しないアクションを実行しないようにしてください。

## ステップ4: Info.plistにNSLocationAlwaysUsageDescriptionを追加する {#step-4-add-nslocationalwaysusagedescription-to-your-infoplist}

`info.plist`に`NSLocationAlwaysUsageDescription`キーと`NSLocationAlwaysAndWhenInUseUsageDescription`キーを追加し、アプリが位置情報を追跡する必要がある理由を説明する`String`値を設定します。iOS 11以降では両方のキーが必須です。
この説明は、システムの位置情報プロンプトが認可をリクエストする際に表示されるため、位置情報の追跡のメリットをユーザーに明確に伝える内容にしてください。

## ステップ5: ユーザーからの認証リクエスト {#step-5-request-authorization-from-the-user}

ジオフェンス機能は、`Always`の位置情報認証が許可されている場合にのみ動作します。

`Always`の位置情報認証をリクエストするには、以下のコードを使用します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## ステップ6: ダッシュボードでジオフェンスを有効にする {#step-6-enable-geofences-on-the-dashboard}

iOSでは、特定のアプリに対して最大20個のジオフェンスしか保存できません。位置情報を使用すると、利用可能な20個のジオフェンススロットの一部が使用されます。アプリ内の他のジオフェンス関連機能への意図しない中断を防ぐために、位置情報ジオフェンスはダッシュボードで個々のアプリに対して有効にする必要があります。

位置情報が正しく機能するには、アプリが利用可能なジオフェンススポットをすべて使い切っていないことも確認してください。

### 位置情報ページからジオフェンスを有効にする: {#enable-geofences-from-the-locations-page}

![Brazeの位置情報ページのジオフェンスオプション。]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### 設定ページからジオフェンスを有効にする: {#enable-geofences-from-the-settings-page}

![Brazeの設定ページにあるジオフェンスのチェックボックス。]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## 自動ジオフェンスリクエストの無効化 {#disabling-automatic-geofence-requests}

iOS SDKバージョン3.21.3以降では、ジオフェンスの自動リクエストを無効にできます。`Info.plist`ファイルを使用してこれを行うことができます。`Info.plist`ファイルに`Braze`ディクショナリを追加します。`Braze`ディクショナリ内に`DisableAutomaticGeofenceRequests`ブールサブエントリを追加し、値を`YES`に設定します。

また、[`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24)メソッドを使用して、アプリ起動時に自動ジオフェンスリクエストを無効にすることもできます。`appboyOptions`ディクショナリで、`ABKDisableAutomaticGeofenceRequestsKey`を`YES`に設定します。以下に例を示します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

このオプションを使用する場合は、機能を動作させるためにジオフェンスを手動でリクエストする必要があります。

## ジオフェンスの手動リクエスト {#manually-requesting-geofences}

Braze SDKがバックエンドから監視対象のジオフェンスをリクエストする際、ユーザーの現在の位置情報を報告し、報告された位置情報に基づいて最適と判断されたジオフェンスを受信します。ジオフェンスの更新にはセッションごとに1回のレート制限があります。

最も関連性の高いジオフェンスを受信するためにSDKが報告する位置情報を制御するには、iOS SDKバージョン3.21.3以降で、位置情報の緯度と経度を指定してジオフェンスを手動でリクエストできます。この方法を使用する場合は、自動ジオフェンスリクエストを無効にすることをお勧めします。無効にするには、以下のコードを使用してください。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}