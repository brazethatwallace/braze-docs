---
nav_title: Swift SDK
article_title: Swift SDKリポジトリガイド
page_order: 3
description: "GitHubからミラーリングされたBraze Swift SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Swift SDKについて {#about-the-braze-swift-sdk}

Braze Swift SDKは、Brazeのメッセージング、分析、ユーザーエンゲージメント機能をアプリに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド](https://www.braze.com/docs/user_guide/introduction/)
- [Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)

## クイックスタート {#quickstart}

以下のスニペットは、Braze Swift SDKをアプリに追加するために必要な最小限の設定を示しています。

``` swift
// AppDelegate.swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  // ...
  static var braze: Braze? = nil

  // ...
   func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // ...
        let configuration = Braze.Configuration(
            apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
            endpoint: "YOUR-BRAZE-ENDPOINT"
        )
        let braze = Braze(configuration: configuration)

        AppDelegate.braze = braze
        // ...
    }
}
```

``` swift
AppDelegate.braze?.changeUser(userId: "Jane Doe")
```

高度な統合オプションについては、[Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)を参照してください。

## バージョンサポート {#version-support}

以下の表は、Braze Swift SDKで使用されるツールのサポートされる最小バージョンを示しています。

ツール | サポートされる最小バージョン
:----|:----
iOS|12.0+
Mac Catalyst|16.0+
tvOS|12.0+
visionOS|1.0+
Xcode|26.0+ (17A324)

## パッケージマネージャー {#package-managers}
- Swift Package Manager
- CocoaPods

## ライブラリー {#libraries}

以下の表は、Braze Swift SDKの各ライブラリーについて説明しています。

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                             | iOS |     tvOS      | macCatalyst |   visionOS    |
|-----------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _[分析]と[プッシュ通知]をサポートするメインSDKライブラリー。_                            |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _[In-App Messages]と[Content Cards]のためのBraze提供UIライブラリー。_                         |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _[ロケーション分析とジオフェンスモニタリング]をサポートするロケーションライブラリー。_               |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _[リッチプッシュ通知]をサポートする通知サービス拡張ライブラリー。_ |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _[Push Stories]をサポートする通知コンテンツ拡張ライブラリー。_                      |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="ライブラリー" }

<sup>1</sup> _tvOSではプッシュ通知はサポートされていません_<br/>
<sup>2</sup> _tvOSおよびvisionOSではジオフェンスモニタリングはサポートされていません_

[分析]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[プッシュ通知]: https://www.braze.com/docs/user_guide/message_building_by_channel/push
[In-App Messages]: https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards
[ロケーション分析とジオフェンスモニタリング]: https://www.braze.com/docs/user_guide/engagement_tools/locations_and_geofences
[リッチプッシュ通知]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## サンプル {#examples}

複数の機能の統合を紹介する[サンプルプロジェクト](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples)をご覧ください。

## 代替リポジトリ {#alternative-repositories}

| バリアント                               |                                     リポジトリ | GH Issues、SDK情報 |
|---------------------------------------|-----------------------------------------------:|--------------------:|
| → **ソースおよびスタティックXCFrameworks** |                    [braze-inc/braze-swift-sdk] |                   ✓ |
| スタティックXCFrameworks                   |    [braze-inc/braze-swift-sdk-prebuilt-static] |                   ✗ |
| ダイナミックXCFrameworks                  |   [braze-inc/braze-swift-sdk-prebuilt-dynamic] |                   ✗ |
| マージ可能なXCFrameworks（早期アクセス） | [braze-inc/braze-swift-sdk-prebuilt-mergeable] |                   ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="代替リポジトリ" }

## お問い合わせ {#contact}

ご質問がある場合は、Brazeテクニカルサポートまでお問い合わせください。

[braze-inc/braze-swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-sdk-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-sdk-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-sdk-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk)を参照してください。