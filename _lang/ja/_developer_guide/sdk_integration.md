---
nav_title: SDKを統合する
article_title: Braze SDKを統合する
description: "Braze SDKの統合方法について説明します。"
page_order: 2.0
---

# ![Brazeロゴ]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Braze SDKを統合する {#braze-logo-image_buster-assetsbraze_primary_icon_blacksvg-stylefloatrightwidth120pxborder0-classnoimgborderintegrate-the-braze-sdk}

> Braze SDKの統合方法について説明します。各SDKは独自のGitHub公開リポジトリでホストされており、Brazeの機能をテストしたり、独自のアプリケーションと一緒に実装したりするために使用できる、完全にビルド可能なサンプルアプリが含まれています。詳しくは、[参照資料、リポジトリ、サンプルアプリ]({{site.baseurl}}/developer_guide/references)を参照してください。SDKに関する一般的な情報については、[はじめに：統合の概要]({{site.baseurl}}/developer_guide/getting_started/integration_overview)を参照してください。

ドキュメント内のミラーされたSDK READMEコンテンツについては、[リポジトリガイド]({{site.baseurl}}/developer_guide/sdk_repository_guides)を参照してください。

{% alert tip %}
SDKを統合した後、[SDK認証]({{site.baseurl}}/developer_guide/sdk_integration/authentication)を有効にすることで、不正なSDKリクエストを防止し、セキュリティをさらに強化できます。SDK認証は、Web、Android、Swift、React Native、Flutter、Unity、Cordova、.NET MAUI（Xamarin）、Expoで利用可能です。
{% endalert %}

{% alert note %}
SDKの初期化がHTTPS証明書の信頼エラー（例：`SSLHandshakeException`で`Trust anchor for certification path not found`）で失敗する場合は、[SDK証明書信頼エラーのトラブルシューティング]({{site.baseurl}}/developer_guide/sdk_integration/troubleshooting_certificate_errors)を参照してください。
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
## Roku SDKを統合する {#integrating-the-roku-sdk}

### ステップ1:ファイルを追加する {#step-1-add-files}

Braze SDKファイルは、[Braze Roku SDKリポジトリ](https://github.com/braze-inc/braze-roku-sdk)の`sdk_files`ディレクトリにあります。

1. `BrazeSDK.brs`をアプリの`source`ディレクトリに追加します。
2. `BrazeTask.brs`と`BrazeTask.xml`をアプリの`components`ディレクトリに追加します。

### ステップ2:参照を追加する {#step-2-add-references}

以下の`script`要素を使用して、メインシーンに`BrazeSDK.brs`への参照を追加します：

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### ステップ3:設定する {#step-3-configure}

`main.brs`内で、グローバルノードにBrazeの設定を行います：

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

[SDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)とAPIキーは、Brazeダッシュボードで確認できます。

### ステップ4:Brazeを初期化する {#step-4-initialize-braze}

Brazeインスタンスを初期化します：

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## オプション設定 {#optional-configurations}

### ログ {#logging}

Brazeの統合をデバッグするには、Rokuデバッグコンソールでログを確認できます。詳しくは、Roku Developersの[コードのデバッグ](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md)を参照してください。

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
SDK統合のQAを行う際は、[SDKデバッガー]({{site.baseurl}}/developer_guide/sdk_integration/debugging)を使用すると、アプリの詳細ログを有効にすることなく問題をトラブルシューティングできます。
{% endalert %}