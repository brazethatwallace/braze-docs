---
nav_title: Flutter SDK
article_title: Flutter SDKリポジトリガイド
page_order: 6
description: "GitHubからミラーリングされたBraze Flutter SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
# Flutter SDKリポジトリガイド {#flutter-sdk-repository-guide}

## Braze Flutter SDKについて {#about-the-braze-flutter-sdk}

Braze Flutter SDKは、Brazeのメッセージング、分析、ユーザーエンゲージメント機能をアプリケーションに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド](https://www.braze.com/docs/user_guide/introduction/)
- [Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter)

## クイックスタート {#quickstart}

以下のスニペットは、Braze Flutter SDKをアプリに追加するために必要な最小限の設定を示しています。

``` bash
flutter pub add braze_plugin
```

### Android

``` xml
<!-- android/res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### iOS

``` swift
// AppDelegate.swift
import BrazeKit
import braze_plugin

class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
  ) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
      apiKey: "<BRAZE_API_KEY>",
      endpoint: "<BRAZE_ENDPOINT>"
    )
    // - Enable logging or customize configuration here
    configuration.logger.level = .info
    let braze = BrazePlugin.initBraze(configuration)
    AppDelegate.braze = braze

    return true
  }
}
```

### Dart

``` dart
import 'package:braze_plugin/braze_plugin.dart';

// ...
_braze = new BrazePlugin();

// ...
_braze.changeUser("Jane Doe");
```

高度な統合オプションについては、[Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter)を参照してください。

## バージョンサポート {#version-support}

以下の表は、Braze Flutter SDKで使用されるツールのサポートされる最小バージョンを示しています。

| ツール                                                        | サポートされる最小バージョン |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter（CocoaPods経由の統合）                                 | 1.10.0+                   |
| Flutter（CocoaPodsまたはSwift Package Manager経由の統合）       | 3.24.0+                   |
| iOSデプロイメントターゲット                                     | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="バージョンサポート" }

このSDKは、基盤となるBrazeネイティブSDKの要件も継承します。詳細については、[braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk)および[braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk)を参照してください。

## サンプルアプリ {#sample-app}

[`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)フォルダには、このパッケージのAPIを統合して使用する方法を示すサンプルアプリが含まれています。

## お問い合わせ {#contact}

ご質問がある場合は、Brazeテクニカルサポートまでお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk)を参照してください。