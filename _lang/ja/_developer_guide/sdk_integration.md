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
{% multi_lang_include developer_guide/roku/sdk_integration.md %}
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