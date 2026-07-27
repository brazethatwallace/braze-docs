---
nav_title: Cordova SDK
article_title: Cordova SDKリポジトリガイド
page_order: 5
description: "GitHubからミラーされたBraze Cordova SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
# Cordova SDKリポジトリガイド {#cordova-sdk-repository-guide}

## Braze Cordova SDKについて {#about-the-braze-cordova-sdk}

Braze Cordova SDKは、Brazeのメッセージング、分析、ユーザーエンゲージメント機能をアプリに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド](https://www.braze.com/docs/user_guide/introduction/)
- [Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## 最小バージョン要件 {#minimum-version-requirements}

| Braze プラグイン | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="最小バージョン要件" }

このSDKは、基盤となるBrazeネイティブSDKの要件も継承します。以下のリストにも準拠してください。
* [Android SDKの要件](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [SWIFT SDKの要件](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## SDKのインストール {#installing-the-sdk}
{% alert warning %}
Braze Cordova SDKは、以下の方法のみを使用して追加してください。他の方法でインストールしようとすると、セキュリティ上の問題が発生する可能性があります。
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## サンプルアプリケーションの実行 {#running-the-sample-application}
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk)を参照してください。