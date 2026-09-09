---
nav_title: SDKの初期セットアップ
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

> この参照記事では、tvOS用のBraze SDKをインストールする方法について説明します。Braze SDKをインストールすると、基本的な分析機能が提供されます。

{% alert note %}
当社のtvOS SDKは現在、分析機能をサポートしています。ダッシュボードにtvOSアプリを追加するには、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開いてください。
{% endalert %}

tvOS Braze SDKは、Objective-CおよびSwiftプロジェクトの依存関係マネージャーである[CocoaPods](http://cocoapods.org/)を使用してインストールまたは更新する必要があります。CocoaPodsを使用すると、統合と更新がさらに簡単になります。

## tvOS SDK CocoaPods統合

### ステップ1: CocoaPodsをインストールする

tvOS [CocoaPods](http://cocoapods.org/) を使用してSDKをインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、[Ruby バージョン 2.0.0](https://www.ruby-lang.org/en/installation/) 以上を使用していることを確認してください。

以下のコマンドを実行して開始します：

```bash
$ sudo gem install cocoapods
```

- `rake` 実行ファイルの上書きを求められた場合は、CocoaPods.orgの[Getting started](http://guides.cocoapods.org/using/getting-started.html)を参照してください。
- CocoaPodsに関する問題がある場合は、[CocoaPods troubleshooting guide](http://guides.cocoapods.org/using/troubleshooting.html)を参照してください。

### ステップ2: Podfileを構成する

CocoaPods Ruby Gemをインストールしたら、Xcodeプロジェクトディレクトリに `Podfile` という名前のファイルを作成する必要があります。

Podfileに以下の行を追加します：

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

マイナーバージョン更新未満のものをpod更新で自動的に取得するように、Brazeのバージョンを指定することをお勧めします。これは `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build` のようになります。メジャー変更を含む最新のBraze SDKバージョンを自動的に統合したい場合は、Podfileで `pod 'Appboy-tvOS-SDK'` を使用できます。

### ステップ3: Braze SDKをインストールする

Braze SDK CocoaPodsをインストールするには、ターミナル内でXcodeアプリプロジェクトのディレクトリに移動し、以下のコマンドを実行します：
```
pod install
```

この時点で、CocoaPodsによって作成された新しいXcodeプロジェクトワークスペースを開けるはずです。Xcodeプロジェクトではなく、このXcodeワークスペースを使用してください。

![CocoaPodsによって作成された新しいXcodeプロジェクトワークスペースを開けるはずです。Xcodeプロジェクトではなく、このXcodeワークスペースを使用してください。]({% image_buster /assets/img_archive/podsworkspace.png %})

### ステップ4: アプリデリゲートを更新する

{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` ファイルに以下のコード行を追加します：

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

`AppDelegate.m` ファイル内の `application:didFinishLaunchingWithOptions` メソッド内に以下のスニペットを追加します：

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

最後に、`YOUR-API-KEY` を**設定の管理**ページの正しい値に更新します。

{% endtab %}
{% tab swift %}

Braze SDKをCocoaPodsまたはCarthageで統合する場合は、`AppDelegate.swift` ファイルに以下のコード行を追加します：

```swift
import AppboyTVOSKit
```

SwiftプロジェクトでObjective-Cコードを使用する方法の詳細については、[Apple Developer Docs](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)を参照してください。

`AppDelegate.swift` で、`application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に以下のスニペットを追加します：

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

次に、`YOUR-API-KEY` を**設定の管理**ページの正しい値に更新します。

`sharedInstance` シングルトンは `startWithApiKey:` が呼び出されるまで nil になります。これはBrazeの機能を使用するための前提条件です。

{% endtab %}
{% endtabs %}

{% alert warning %}
アプリケーションのメインスレッドでBrazeを初期化してください。非同期で初期化すると、機能が正しく動作しなくなる可能性があります。
{% endalert %}

### ステップ5: カスタムエンドポイントまたはデータクラスターを指定する

{% alert note %}
2019年12月現在、カスタムエンドポイントは新たに提供されなくなりました。既存のカスタムエンドポイントをお持ちの場合は、引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics#endpoints">利用可能なエンドポイントのリスト</a> を参照してください。
{% endalert %}

Brazeの担当者が、[正しいエンドポイント]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/)についてすでにアドバイスしているはずです。

#### コンパイル時のエンドポイント設定（推奨）
既存のカスタムエンドポイントが提供されている場合：
- Braze iOS SDK v3.0.2以降では、`Info.plist` ファイルを使用してカスタムエンドポイントを設定できます。Info.plistファイルに `Appboy` ディクショナリを追加します。`Appboy` ディクショナリ内に `Endpoint` 文字列サブエントリを追加し、カスタムエンドポイントURLのオーソリティに値を設定します（例：`sdk.iad-01.braze.com`、`https://sdk.iad-01.braze.com` ではありません）。

#### ランタイムのエンドポイント設定
既存のカスタムエンドポイントが提供されている場合：
- Braze iOS SDK v3.17.0以降では、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKEndpointKey` を使用してエンドポイントをオーバーライドして設定できます。カスタムエンドポイントURLのオーソリティに値を設定します（例：`sdk.iad-01.braze.com`、`https://sdk.iad-01.braze.com` ではありません）。

{% alert note %}
`ABKAppboyEndpointDelegate` を使用したランタイムでのエンドポイント設定のサポートは、Braze iOS SDK v3.17.0で削除されました。すでに `ABKAppboyEndpointDelegate` を使用している場合、Braze iOS SDKバージョン v3.14.1 から v3.16.0 では、`getApiEndpoint()` メソッド内の `dev.appboy.com` への参照を `sdk.iad-01.braze.com` への参照に置き換える必要があることに注意してください。
{% endalert %}

### SDKの統合完了

Brazeがアプリケーションからデータを収集するようになり、基本的な統合が完了したはずです。tvOSアプリおよびその他のサードパーティライブラリをコンパイルする際、Bitcodeを有効にする必要があることに注意してください。

### CocoaPodsを使用してBraze SDKを更新する

CocoaPodを更新するには、プロジェクトディレクトリ内で以下のコマンドを実行するだけです：

```
pod update
```

## 起動時のBrazeカスタマイズ

起動時にBrazeをカスタマイズしたい場合は、代わりにBrazeの初期化メソッド `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` を使用し、Braze起動キーのオプション `NSDictionary` を渡すことができます。
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` ファイル内の `application:didFinishLaunchingWithOptions` メソッドに、以下のBrazeメソッドを追加してください：

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

`AppDelegate.swift` 内の `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` メソッドに、以下のBrazeメソッドを追加してください：

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

ここで `appboyOptions` は起動設定値の `Dictionary` です。

{% endtab %}
{% endtabs %}

このメソッドは `startWithApiKey:inApplication:withLaunchOptions:` 初期化メソッドの代わりに使用され、以下のパラメータで呼び出されます：

- `YOUR-API-KEY`：アプリケーションのAPIキーは、Brazeダッシュボードの**設定の管理**にあります。
- `application`：現在のアプリです。
- `launchOptions`：`application:didFinishLaunchingWithOptions:` から取得するオプション `NSDictionary` です。
- `appboyOptions`：Brazeの起動設定値を含むオプション `NSDictionary` です。

Braze起動キーの一覧については、[Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) を参照してください。

## Appboy.sharedInstance()とSwiftのnull許容性
一般的なプラクティスとは多少異なり、`Appboy.sharedInstance()`シングルトンはオプショナルです。これは、`startWithApiKey:`が呼び出される前は`sharedInstance`が`nil`であり、遅延初期化を使用する非標準ではあるものの無効ではない実装が存在するためです。

Appboyの`sharedInstance`への任意のアクセスよりも前に`didFinishLaunchingWithOptions:`デリゲートで`startWithApiKey:`を呼び出す場合（標準的な実装）、`Appboy.sharedInstance()?.changeUser("testUser")`のようにオプショナルチェーンを使用することで、煩雑なチェックを回避できます。これは、非nullの`sharedInstance`を前提としたObjective-C実装と同等の動作になります。

tvOS SDKを手動で統合することもできます。[パブリックリポジトリ](https://github.com/appboy/appboy-ios-sdk)からFrameworkを取得し、前のセクションで説明した手順に従ってBrazeを初期化してください。

## ユーザーの識別と分析レポート
ユーザーIDの設定、カスタムイベントのログ記録、ユーザー属性の設定については、[iOSドキュメント]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift)を参照してください。また、[イベント命名規則]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)についても理解しておくことをお勧めします。