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

これらの手順に従う前に、[Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration/)、[CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/)、[Swift Package Manager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager/)、または[手動]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)統合のいずれかを使用してSDKを統合していることを確認してください。

## ステップ1:アプリデリゲートを更新する {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Braze SDKをCocoaPods、Carthage、または[ダイナミックな手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)で統合している場合は、次のコード行を `AppDelegate.m` ファイルに追加します。

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Swift Package Managerまたは[静的な手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)を使用して統合している場合は、代わりに次の行を使用します。

`````````objc
#import "AppboyKit.h"
```

次に、`AppDelegate.m` ファイル内の `application:didFinishLaunchingWithOptions:` メソッド内に以下のスニペットを追加します。

`````````objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

**設定の管理**ページの正しい値で `YOUR-APP-IDENTIFIER-API-KEY` を更新してください。アプリ識別子APIキーの場所について詳しくは、[APIドキュメント]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)をご覧ください。

{% endtab %}
{% tab swift %}

Braze SDKをCocoaPods、Carthage、または[ダイナミックな手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)で統合している場合は、次のコード行を `AppDelegate.swift` ファイルに追加します。

`````````swift
import Appboy_iOS_SDK
```

Swift Package Managerまたは[静的な手動統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/)を使用して統合している場合は、代わりに次の行を使用します。

`````````swift
import AppboyKit
```
SwiftプロジェクトでのObjective-Cコードの使用の詳細については、[Apple開発者ドキュメント](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)を参照してください。

次に、`AppDelegate.swift` で、次のスニペットを `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に追加します。

`````````swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**設定の管理**ページの正しい値で `YOUR-APP-IDENTIFIER-API-KEY` を更新してください。アプリ識別子APIキーの場所について詳しくは、[APIドキュメント]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)をご覧ください。

{% endtab %}
{% endtabs %}

{% alert note %}
`sharedInstance` シングルトンは、`startWithApiKey:` が呼び出される前はnilになります。これはBraze機能を使用するための前提条件です。
{% endalert %}

{% alert warning %}
必ずアプリケーションのメインスレッドでBrazeを初期化してください。非同期で初期化すると、機能が破損する可能性があります。
{% endalert %}


## ステップ2:データクラスターを指定する {#step-2-specify-your-data-cluster}

{% alert note %}
2019年12月の時点で、カスタムエンドポイントは提供されなくなっていることに注意してください。既存のカスタムエンドポイントがある場合は、それを引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a> を参照してください。
{% endalert %}

### コンパイル時のエンドポイント設定（推奨） {#compile-time-endpoint-configuration-recommended}

既存のカスタムエンドポイントが指定されている場合:
- Braze iOS SDK v3.0.2以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。`Braze` ディクショナリを `Info.plist` ファイルに追加します。`Braze` ディクショナリ内で、`Endpoint` 文字列サブエントリを追加し、値をカスタムエンドポイントURLのオーソリティ（たとえば、`https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`）に設定します。Braze iOS SDK v4.0.2より前では、ディクショナリキー `Appboy` を `Braze` の代わりに使用する必要があります。

Braze担当者は、[正しいエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)についてすでに通知しているはずです。

### ランタイムエンドポイント設定 {#runtime-endpoint-configuration}

既存のカスタムエンドポイントが指定されている場合:
- Braze iOS SDK v3.17.0以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントの設定をオーバーライドできます。値をカスタムエンドポイントURLのオーソリティ（たとえば、`https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`）に設定します。

## SDKの統合が完了 {#sdk-integration-complete}

これでBrazeはアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。[カスタムイベントトラッキング]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)、[プッシュメッセージング]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/)、およびBraze機能の完全なスイートを有効にするには、次の記事を参照してください。

## 起動時のBrazeのカスタマイズ {#customizing-braze-on-startup}

起動時にBrazeをカスタマイズする場合は、代わりにBraze初期化メソッド `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` を使用し、オプションのBraze起動キーの `NSDictionary` を渡すことができます。
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` ファイルの `application:didFinishLaunchingWithOptions:` メソッド内に、次のBrazeメソッドを追加します。

`````````objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドを置き換えることに注意してください。

{% endtab %}
{% tab swift %}

`AppDelegate.swift` の `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` メソッド内に、次のBrazeメソッドを追加します。`appboyOptions` はスタートアップ設定値の `Dictionary` です。

`````````swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドを置き換えることに注意してください。

{% endtab %}
{% endtabs %}

このメソッドは、次のパラメーターを使用して呼び出されます。

- `YOUR-APP-IDENTIFIER-API-KEY` – Brazeダッシュボードの[アプリ識別子]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key)APIキー。
- `application` – 現在のアプリ。
- `launchOptions` – `application:didFinishLaunchingWithOptions:` から取得するオプション `NSDictionary`。
- `appboyOptions` – Brazeのスタートアップ設定値を持つオプションの `NSDictionary`。

Brazeのスタートアップキーのリストについては、[Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) を参照してください。

## Appboy.sharedInstance() およびSwiftのnullability {#appboysharedinstance-and-swift-nullability}
一般的な慣例とは多少異なりますが、`Appboy.sharedInstance()` シングルトンはオプショナルです。これは、`startWithApiKey:` が呼び出される前は `sharedInstance` が `nil` であり、遅延初期化を使用できる非標準だが無効ではない実装がいくつかあるためです。

Appboyの `sharedInstance`（標準実装）にアクセスする前に `didFinishLaunchingWithOptions:` デリゲートで `startWithApiKey:` を呼び出すと、`Appboy.sharedInstance()?.changeUser("testUser")` のようなオプショナルチェーンを使用して、煩雑なチェックを回避できます。これは、非nullの `sharedInstance` を想定したObjective-C実装と同等になります。

## その他のリソース {#additional-resources}

[iOSクラスの完全なドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html)を参照して、SDKメソッドに関する追加のガイダンスを得ることができます。