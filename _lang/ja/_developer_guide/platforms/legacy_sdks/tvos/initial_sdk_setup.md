---
nav_title: SDKの初期設定
article_title: tvOS の初期 SDK セットアップ
platform: tvOS
page_order: 0
page_type: reference
description: "このページでは、tvOS Braze SDKの初期セットアップ手順について説明します。"
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SDKの初期セットアップ {#initial-sdk-setup}

> この参照記事では、tvOS 用 Braze SDKをインストールする方法について説明します。Braze SDKをインストールすると、基本的な分析機能が提供されます。

{% alert note %}
当社の tvOS SDKは現在、分析機能をサポートしています。ダッシュボードに tvOS アプリを追加するには、[サポートチケット]({{site.baseurl}}/braze_support/)を開いてください。
{% endalert %}

tvOS Braze SDKは、Objective-C および Swift プロジェクトの依存関係マネージャーである [CocoaPods](http://cocoapods.org/) を使用してインストールまたは更新する必要があります。CocoaPods を使用すると、統合と更新がさらに簡単になります。

## tvOS SDK CocoaPods の統合 {#tvos-sdk-cocoapods-integration}

### ステップ1:CocoaPods をインストールする {#step-1-install-cocoapods}

tvOS [CocoaPods](http://cocoapods.org/) を介して SDKをインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、[Ruby バージョン 2.0.0](https://www.ruby-lang.org/en/installation/) 以降を使用していることを確認してください。

開始するには、次のコマンドを実行します。

```bash
$ sudo gem install cocoapods
```

- `rake` 実行可能ファイルを上書きするプロンプトが表示された場合、詳細については CocoaPods.org の [Getting started](http://guides.cocoapods.org/using/getting-started.html) を参照してください。
- CocoaPods に関する問題がある場合は、[CocoaPods トラブルシューティングガイド](http://guides.cocoapods.org/using/troubleshooting.html)を参照してください。

### ステップ2:Podfile の構築 {#step-2-constructing-the-podfile}

CocoaPods Ruby Gem をインストールしたら、Xcode プロジェクトディレクトリに `Podfile` という名前のファイルを作成する必要があります。

次の行を Podfile に追加します。

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

ポッドの更新がマイナーバージョンの更新よりも小さいものを自動的に取得するように、Braze をバージョン管理することをお勧めします。これは `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build` のようになります。メジャーな変更があっても最新の Braze SDK バージョンを自動的に統合する場合は、Podfile で `pod 'Appboy-tvOS-SDK'` を使用できます。

### ステップ3:Braze SDKのインストール {#step-3-installing-the-braze-sdk}

Braze SDK CocoaPods をインストールするには、ターミナル内で Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。
```
pod install
```

この時点で、CocoaPods によって作成された新しい Xcode プロジェクトワークスペースを開くことができるはずです。Xcode プロジェクトの代わりに、必ずこの Xcode ワークスペースを使用してください。

![]({% image_buster /assets/img_archive/podsworkspace.png %})

### ステップ4:アプリデリゲートの更新 {#step-4-updating-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

次のコード行を `AppDelegate.m` ファイルに追加します。

`````````objc
#import <AppboyTVOSKit/AppboyKit.h>
```

`AppDelegate.m` ファイル内で、`application:didFinishLaunchingWithOptions` メソッド内に次のスニペットを追加します。

`````````objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

最後に、**設定の管理**ページの正しい値で `YOUR-API-KEY` を更新します。

{% endtab %}
{% tab swift %}

Braze SDKを CocoaPods または Carthage と統合する場合は、次のコード行を `AppDelegate.swift` ファイルに追加します。

`````````swift
import AppboyTVOSKit
```

Swift プロジェクトでの Objective-C コードの使用方法について詳しくは、[Apple 開発者ガイド](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)を参照してください。

`AppDelegate.swift` で、次のスニペットを `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に追加します。

`````````swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

次に、**設定の管理**ページの正しい値で `YOUR-API-KEY` を更新します。

`sharedInstance` シングルトンは、Braze 機能を使用するための前提条件である `startWithApiKey:` が呼び出される前は nil になります。

{% endtab %}
{% endtabs %}

{% alert warning %}
必ずアプリケーションのメインスレッドで Braze を初期化してください。非同期で初期化すると、機能が破損する可能性があります。
{% endalert %}

### ステップ5:カスタムエンドポイントまたはデータクラスターを指定する {#step-5-specify-your-custom-endpoint-or-data-cluster}

{% alert note %}
2019年12月をもって、カスタムエンドポイントは提供されなくなりました。既存のカスタムエンドポイントがある場合は、それを引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a> を参照してください。
{% endalert %}

Braze 担当者から、[正しいエンドポイント]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/)についてすでに案内があったはずです。

#### コンパイル時のエンドポイント構成（推奨） {#compile-time-endpoint-configuration-recommended}
既存のカスタムエンドポイントが指定されている場合:
- Braze iOS SDK v3.0.2 以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。`Appboy` ディクショナリを Info.plist ファイルに追加します。`Appboy` ディクショナリ内で、`Endpoint` 文字列サブエントリを追加し、値をカスタムエンドポイント URL のオーソリティに設定します（例: `https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`）。

#### ランタイムエンドポイント構成 {#runtime-endpoint-configuration}
既存のカスタムエンドポイントが指定されている場合:
- Braze iOS SDK v3.17.0 以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントの設定をオーバーライドできます。値をカスタムエンドポイント URL のオーソリティに設定します（例: `https://sdk.iad-01.braze.com` ではなく `sdk.iad-01.braze.com`）。

{% alert note %}
`ABKAppboyEndpointDelegate` を使用した実行時のエンドポイント設定サポートは、Braze iOS SDK v3.17.0 で削除されました。すでに `ABKAppboyEndpointDelegate` を使用している場合は、Braze iOS SDK バージョン v3.14.1 から v3.16.0 では、`getApiEndpoint()` メソッドの `dev.appboy.com` への参照を `sdk.iad-01.braze.com` への参照に置き換える必要があります。
{% endalert %}

### SDKの統合が完了 {#sdk-integration-complete}

これで、Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。tvOS アプリおよびその他のサードパーティライブラリをコンパイルするときは、Bitcode を有効にする必要があることに注意してください。

### CocoaPods 経由で Braze SDKを更新する {#updating-the-braze-sdk-via-cocoapods}

CocoaPod を更新するには、プロジェクトディレクトリ内で次のコマンドを実行するだけです。

```
pod update
```

## 起動時の Braze のカスタマイズ {#customizing-braze-on-startup}

起動時に Braze をカスタマイズする場合は、代わりに Braze 初期化メソッド `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` を使用し、オプションの Braze 起動キーの `NSDictionary` を渡すことができます。
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` ファイルの `application:didFinishLaunchingWithOptions` メソッド内に、次の Braze メソッドを追加します。

`````````objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

`AppDelegate.swift` の `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` メソッド内に、次の Braze メソッドを追加します。

`````````swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

ここで、`appboyOptions` はスタートアップ構成値の `Dictionary` です。

{% endtab %}
{% endtabs %}

このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドを置き換え、次のパラメーターで呼び出されます。

- `YOUR-API-KEY`: アプリケーションの API キーは、Braze ダッシュボードの**設定の管理**にあります。
- `application`: 現在のアプリ。
- `launchOptions`: `application:didFinishLaunchingWithOptions:` から取得するオプション `NSDictionary`。
- `appboyOptions`: Braze のスタートアップ構成値を持つオプションの `NSDictionary`。

Braze 起動キーの一覧については、[Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) を参照してください。

## Appboy.sharedInstance() および Swift の nullability {#appboysharedinstance-and-swift-nullability}
一般的な慣例とは多少異なりますが、`Appboy.sharedInstance()` シングルトンはオプションです。これは、`startWithApiKey:` が呼び出される前は `sharedInstance` が `nil` であり、遅延初期化を使用できる非標準だが無効ではない実装がいくつかあるためです。

Appboy の `sharedInstance`（標準実装）にアクセスする前に `didFinishLaunchingWithOptions:` デリゲートで `startWithApiKey:` を呼び出すと、`Appboy.sharedInstance()?.changeUser("testUser")` のようなオプショナルチェーンを使用して、煩雑なチェックを回避できます。これは、非 null の `sharedInstance` を想定した Objective-C 実装と同等になります。

## 手動統合オプション {#manual-integration-options}

tvOS SDKを手動で統合することもできます。[パブリックリポジトリ](https://github.com/appboy/appboy-ios-sdk)からフレームワークを取得し、前のセクションで説明したように Braze を初期化するだけです。

## ユーザーの特定と分析レポート {#identifying-users-and-reporting-analytics}
ユーザー ID の設定、カスタムイベントのログ記録、ユーザー属性の設定については、[iOS ドキュメント]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift)を参照してください。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/)についてもよく理解しておくことをお勧めします。