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

早期アクセス期間中、デバイスメッセージング API を使用して以下のことが可能です。

- 外部ユーザー ID とプレースメントのセットに対して[適格なバナーを取得する]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)
- [バナーのインプレッションおよびクリックイベントをレポートする]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)

デバイスメッセージング API は構造化されたバナープロパティを返すため、カスタムインターフェイスを構築できます。レンダリングされた HTML は返しません。

## 統合要件 {#integration-requirements}

デバイスメッセージング API を統合するには、以下が必要です。

- デバイスメッセージング API が有効になっているワークスペース
- そのワークスペースのクライアント側 REST APIキー
- そのワークスペースの REST エンドポイント
- ユーザーの外部ユーザー ID
- アプリの API 識別子

認証情報の詳細については、[認証とセキュリティ]({{site.baseurl}}/api/device_messaging_api/authentication)を参照してください。

## デバイスメッセージング API と REST APIのガイダンス {#device-messaging-api-and-rest-api-guidance}

デバイスメッセージング API は、Braze REST APIと同じリージョン別 REST エンドポイントを使用しますが、認証とレスポンスの仕様は別になっています。プライベートなサーバーサイドキー、レスポンスボディ、エラー、レート制限に関する一般的な REST API ガイダンスは、デバイスメッセージング API の記事で明示的に言及されていない限り適用されません。

リクエストフィールド、レスポンスボディ、ステータスコード、制限については、デバイスメッセージング API のエンドポイントドキュメントを正式な情報源としてご利用ください。