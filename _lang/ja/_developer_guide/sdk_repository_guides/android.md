---
nav_title: Android SDK
article_title: Android SDKリポジトリガイド
page_order: 2
description: "GitHubからミラーリングされたBraze Android SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Android SDKについて {#about-the-braze-android-sdk}

Braze Android SDKは、Brazeのメッセージング、分析、ユーザーエンゲージメント機能をアプリケーションに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド]({{site.baseurl}}/user_guide/introduction)
- [Braze開発者ガイド]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android)

## クイックスタート {#quickstart}

以下のスニペットは、Braze Android SDKをアプリに追加するために必要な最小限の設定を示しています。

``` groovy
// build.gradle

// ...
repositories {
  mavenCentral()
}
// ...
dependencies {
  `implementation 'com.braze:android-sdk-ui:42.3.+'`
  `implementation 'com.braze:android-sdk-location:42.3.+'`
}
// ...
```

``` xml
<!-- res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` kotlin
Braze.getInstance(context).changeUser("Jane Doe");
```

高度な統合オプションの詳細については、[Braze開発者ガイド]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android)を参照してください。

## バージョンサポート {#version-support}

{% alert important %}
Braze Android SDKは`minSdkVersion`をAPI 21+として宣言しており、SDKはAPI 21以降をサポートするアプリにコンパイルできます。SDKはこれらのバージョン向けにコンパイルされますが、BrazeはAPI 25未満のバージョンに対して正式なサポートを提供しておらず、それらのバージョンを実行しているデバイスではSDKが意図どおりに動作しない場合があります。

アプリがこれらのバージョンをサポートしている場合は、以下を行ってください。

- 該当するAPIバージョンの物理デバイス（エミュレーターだけでなく）で、SDKの統合が意図どおりに動作することを検証してください。
- 期待どおりの動作を検証できない場合は、[disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html)を呼び出すか、それらのバージョンでSDKの初期化をスキップする必要があります。そうしないと、ユーザーのデバイスで意図しない副作用やパフォーマンスの低下が発生する可能性があります。
{% endalert %}
以下の表は、Braze Android SDKで使用されるツールの最小サポートバージョンを示しています。

ツール | 最小サポートバージョン
:----|:----
minSdk|5.0+ / API 21+（Lollipop以降）
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|24.1.2
Font Awesome|4.3.0

## モジュール {#modules}

以下の表は、Braze Android SDKの各モジュールについて説明しています。

モジュール | 説明
:----|:----
`android-sdk-base`|Braze SDKの基本分析ライブラリーです。
`android-sdk-ui`|アプリ内メッセージ、プッシュ、Content Cards、バナー用のBraze SDKユーザーインターフェイスライブラリーです。
`android-sdk-location`|ロケーションとジオフェンス用のBraze SDKロケーションライブラリーです。
`android-sdk-jetpack-compose`|Jetpack Composeサポート用のBraze SDKライブラリーです。
`droidboy`|Brazeの詳細な使用方法を示すサンプルアプリです。
`android-sdk-unity`|Unity上でのBraze SDK統合を可能にするライブラリーです。
`samples`|さまざまな統合オプションのサンプルアプリを含むフォルダーです。

## お問い合わせ {#contact}

ご質問がある場合は、Brazeテクニカルサポートにお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk)を参照してください。