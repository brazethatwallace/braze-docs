---
nav_title: スマートTV対応
article_title: Web Braze SDKのスマートTV対応
platform: Web
page_order: 30
description: "この記事では、Braze Web SDKを使用してスマートTV（SamsungおよびLG）と統合する方法について説明します。"

---

# スマートTV対応 {#smart-tv-support}

> Braze Web SDKを使用すると、[Samsung Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)や[LG TV (webOS)](https://webostv.developer.lge.com/discover)を含むスマートTVユーザーに対して、分析データを収集し、リッチなアプリ内メッセージやContent Cardsメッセージを表示できます。この記事では、Braze Web SDKを使用してスマートTVと統合する方法について説明します。

{% alert tip %}
完全なテクニカルリファレンスについては、[JavaScriptドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)または[サンプルアプリ](https://github.com/Appboy/smart-tv-sample-apps)をチェックして、TV上で動作するWeb SDKをご確認ください。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Web Braze SDKの設定 {#configuring-the-web-braze-sdk}

スマートTVとの統合には、2つの変更が必要です。

1. Web SDKをダウンロードまたはインポートする際は、必ず「コア」バンドル（`https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js`で入手可能、`x.y`は任意のバージョン）を使用してください。NPMバージョンはネイティブESモジュールで記述されているのに対し、CDNバージョンはES5にトランスパイルされるため、Web SDKのCDNバージョンを使用することをおすすめします。[NPMバージョン](https://www.npmjs.com/package/@braze/web-sdk)を使用する場合は、webpackのようなバンドラーを使用して未使用のコードを削除し、コードがES5にトランスパイルされていることを確認してください。
2. Web SDKを初期化する際には、`disablePushTokenMaintenance`と`manageServiceWorkerExternally`の初期化オプションを`true`に設定する必要があります。

## 分析 {#analytics}

分析用のWeb SDKメソッドはすべて、スマートTVで使用できます。カスタムイベントやカスタム属性のトラッキングなど、詳細な手順については[分析]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)を参照してください。

## アプリ内メッセージとContent Cards {#in-app-messages-and-content-cards}

Braze Web SDKは、スマートTV上で[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=web)と[Content Cards]({{site.baseurl}}/developer_guide/content_cards?sdktab=web)の両方をサポートしています。アプリ内メッセージとContent Cardsのレンダリングは標準のUI表示ではサポートされていないため、[「Core」Web SDK](https://www.npmjs.com/package/@braze/web-sdk)を使用する必要があります。代わりに、TVアプリのエクスペリエンスに合わせてアプリでカスタマイズする必要があります。

スマートTVアプリがアプリ内メッセージを受信して表示する方法の詳細については、[メッセージのトリガー]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)を参照してください。