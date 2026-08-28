---
nav_title: 概要
article_title: デバイスメッセージング API の概要
page_order: 0
page_type: reference
description: "Braze デバイスメッセージング API とその早期アクセス機能について説明します。"
hidden: true
---

# デバイスメッセージング API の概要 {#device-messaging-api-overview}

Braze デバイスメッセージング API は、Braze SDKを使用せずに Braze のメッセージング機能を統合するための REST エンドポイントのセットです。これらのエンドポイントは、クライアントアプリケーションまたはサーバーアプリケーションから呼び出すことができます。

{% alert important %}
このページはベータ版です。デバイスメッセージング API の機能とドキュメントは変更される可能性があります。アクセスをリクエストするには、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## サポートされている機能 {#supported-capabilities}

早期アクセス期間中、Device Messaging APIを使用して以下のことが可能です。

- 外部ユーザーIDとプレースメントのセットに対して[適格なBannerを取得する]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)
- [Bannerのインプレッションおよびクリックイベントをレポートする]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)

Device Messaging APIは構造化されたBannerプロパティを返すため、カスタムインターフェイスを構築できます。レンダリングされたHTMLは返しません。

## 統合要件 {#integration-requirements}

Device Messaging APIを統合するには、以下が必要です。

- Device Messaging APIが有効になっているワークスペース
- そのワークスペースのクライアント側REST APIキー
- そのワークスペースのRESTエンドポイント
- ユーザーの外部ユーザー ID
- アプリのAPI識別子

認証情報の詳細については、[認証とセキュリティ]({{site.baseurl}}/api/device_messaging_api/authentication)を参照してください。

## デバイスメッセージング API と REST APIのガイダンス {#device-messaging-api-and-rest-api-guidance}

デバイスメッセージング APIは、Braze REST APIと同じリージョン別 REST エンドポイントを使用しますが、認証とレスポンスの仕様は別になっています。プライベートなサーバーサイドキー、レスポンスボディ、エラー、レート制限に関する一般的な REST API ガイダンスは、デバイスメッセージング APIの記事で明示的に言及されていない限り適用されません。

リクエストフィールド、レスポンスボディ、ステータスコード、制限については、デバイスメッセージング APIのエンドポイントドキュメントを正式な情報源としてご利用ください。