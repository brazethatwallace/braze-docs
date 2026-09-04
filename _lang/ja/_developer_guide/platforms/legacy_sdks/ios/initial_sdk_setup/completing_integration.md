---
nav_title: 統合の完了
article_title: iOS SDKの統合を完了する
platform: iOS
description: "この参考記事では、統合オプションの1つを使用してBraze SDKをインストールした後に統合を完了する方法を示します。"
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 統合を完了する {#complete-the-integration}

これらの手順に従う前に、[Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration)、[CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods)、[Swift Package マネージャー]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager)、または[手動]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)統合のいずれかを使用してSDKを統合していることを確認してください。

## ステップ1: アプリデリゲートを更新する {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Braze SDKをCocoaPods、Carthage、または[ダイナミック手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)で統合する場合は、`AppDelegate.m` ファイルに以下のコード行を追加してください：

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Swift Package マネージャーまたは[スタティック手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)で統合する場合は、代わりに以下の行を使用してください：

```objc
#import "AppboyKit.h"
```

次に、`AppDelegate.m` ファイル内の `application:didFinishLaunchingWithOptions:` メソッドに以下のスニペットを追加してください：

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

`YOUR-APP-IDENTIFIER-API-KEY` を**設定の管理**ページの正しい値に更新してください。アプリ識別子APIキーの場所についての詳細は、[APIドキュメント]({{site.baseurl}}/api/identifier_types#app-identifier)を参照してください。

{% endtab %}
{% tab swift %}

Braze SDKをCocoaPods、Carthage、または[ダイナミック手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)で統合する場合は、`AppDelegate.swift` ファイルに以下のコード行を追加してください：

```swift
import Appboy_iOS_SDK
```

Swift Package マネージャーまたは[スタティック手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)で統合する場合は、代わりに以下の行を使用してください：

```swift
import AppboyKit
```
SwiftプロジェクトでObjective-Cコードを使用する方法については、[Apple開発者ドキュメント](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)を参照してください。

次に、`AppDelegate.swift` の `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に以下のスニペットを追加してください：

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

`YOUR-APP-IDENTIFIER-API-KEY` を**設定の管理**ページの正しい値に更新してください。アプリ識別子APIキーの場所についての詳細は、[APIドキュメント]({{site.baseurl}}/api/identifier_types#app-identifier)を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
`sharedInstance` シングルトンは、`startWithApiKey:` が呼び出される前は nil になります。これは、Brazeの機能を使用するための前提条件です。
{% endalert %}

{% alert warning %}
Brazeはアプリケーションのメインスレッドで初期化してください。非同期で初期化すると、機能が正しく動作しなくなる可能性があります。
{% endalert %}

## ステップ2: データクラスターを指定する {#step-2-specify-your-data-cluster}

{% alert note %}
2019年12月以降、カスタムエンドポイントは新規に提供されていません。既存のカスタムエンドポイントをお持ちの場合は、引き続きご使用いただけます。詳細については、<a href="{{site.baseurl}}/api/basics#endpoints">利用可能なエンドポイントの一覧</a> を参照してください。
{% endalert %}

### コンパイル時のエンドポイント設定（推奨） {#compile-time-endpoint-configuration-recommended}

既存のカスタムエンドポイントが提供されている場合:
- Braze iOS SDK v3.0.2以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。`Info.plist` ファイルに `Braze` ディクショナリを追加します。`Braze` ディクショナリ内に、`Endpoint` 文字列サブエントリを追加し、カスタムエンドポイントURLのオーソリティを値として設定します（例: `sdk.iad-01.braze.com`、`https://sdk.iad-01.braze.com` ではありません）。Braze iOS SDK v4.0.2より前のバージョンでは、`Braze` の代わりにディクショナリキー `Appboy` を使用する必要があります。

Brazeの担当者から、[正しいエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)についてすでにご案内があるはずです。

### ランタイムのエンドポイント設定 {#runtime-endpoint-configuration}

既存のカスタムエンドポイントが提供されている場合:
- Braze iOS SDK v3.17.0以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡す `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントをオーバーライドできます。カスタムエンドポイントURLのオーソリティを値として設定します（例: `sdk.iad-01.braze.com`、`https://sdk.iad-01.braze.com` ではありません）。

## SDK統合の完了 {#sdk-integration-complete}

Brazeがアプリケーションからデータを収集し、基本的な統合が完了しました。[カスタムイベントのトラッキング]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)、[プッシュメッセージング]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)、およびBrazeの全機能を有効にするには、以下の記事を参照してください。

## 起動時のBrazeカスタマイズ {#customizing-braze-on-startup}

起動時にBrazeをカスタマイズしたい場合は、Brazeの初期化メソッド`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`を使用し、Braze起動キーのオプション`NSDictionary`を渡すことができます。
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m`ファイルの`application:didFinishLaunchingWithOptions:`メソッド内に、以下のBrazeメソッドを追加します。

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

このメソッドは`startWithApiKey:inApplication:withLaunchOptions:`初期化メソッドの代わりに使用されます。

{% endtab %}
{% tab swift %}

`AppDelegate.swift`の`application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`メソッド内に、以下のBrazeメソッドを追加します。`appboyOptions`は起動設定値の`Dictionary`です。

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

このメソッドは`startWithApiKey:inApplication:withLaunchOptions:`初期化メソッドの代わりに使用されます。

{% endtab %}
{% endtabs %}

このメソッドは以下のパラメーターで呼び出されます。

- `YOUR-APP-IDENTIFIER-API-KEY` – Brazeダッシュボードの[アプリ識別子]({{site.baseurl}}/api/identifier_types#app-identifier)APIキーです。
- `application` – 現在のアプリです。
- `launchOptions` – `application:didFinishLaunchingWithOptions:`から取得するオプション`NSDictionary`です。
- `appboyOptions` – Brazeの起動設定値を含むオプションの`NSDictionary`です。

Braze起動キーの一覧については、[Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h)を参照してください。

## Appboy.sharedInstance()とSwiftのnull許容性 {#appboysharedinstance-and-swift-nullability}
一般的な慣例とはやや異なり、`Appboy.sharedInstance()`シングルトンはオプショナルです。これは、`startWithApiKey:`が呼び出される前は`sharedInstance`が`nil`であり、遅延初期化を使用する非標準ではあるものの無効ではない実装が存在するためです。

`didFinishLaunchingWithOptions:`デリゲート内でAppboyの`sharedInstance`へのアクセスよりも前に`startWithApiKey:`を呼び出す場合（標準的な実装）、`Appboy.sharedInstance()?.changeUser("testUser")`のようにオプショナルチェーンを使用することで、煩雑なチェックを回避できます。これは、非nullの`sharedInstance`を前提としたObjective-Cの実装と同等の動作になります。

## その他のリソース {#additional-resources}

SDKメソッドに関する追加のガイダンスとして、[iOSクラスドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html)の全文を参照できます。