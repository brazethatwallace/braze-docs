---
nav_title: 概要
article_title: メッセージング API の概要
page_order: 0
page_type: reference
description: "Braze メッセージング API とその早期アクセス機能について説明します。"
hidden: true
---

# メッセージング API の概要 {#messaging-api-overview}

Braze メッセージング API は、Braze SDKを使用せずに Braze のメッセージング機能を統合するための REST エンドポイントのセットです。これらのエンドポイントは、クライアントアプリケーションまたはサーバーアプリケーションから呼び出すことができます。

{% alert important %}
このページはベータ版です。メッセージング API の機能とドキュメントは変更される可能性があります。アクセスをリクエストするには、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## サポートされている機能 {#supported-capabilities}

早期アクセス期間中は、メッセージング API を使用して以下のことができます。

- 外部ユーザー ID とプレースメントのセットに対して[対象となるバナーを取得する]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners)
- [バナーのインプレッションおよびクリックイベントをレポートする]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)

メッセージング API は構造化されたバナープロパティを返すため、カスタムインターフェイスを構築できます。レンダリングされた HTML は返しません。

## 統合要件 {#integration-requirements}

メッセージング API を統合するには、以下が必要です。

- メッセージング API が有効になっているワークスペース
- そのワークスペースのクライアントサイド REST APIキー
- そのワークスペースの REST エンドポイント
- ユーザーの外部ユーザー ID
- アプリの API 識別子

認証情報の詳細については、[認証とセキュリティ]({{site.baseurl}}/api/messaging_api/authentication)を参照してください。

## メッセージング API と REST APIのガイダンス {#messaging-api-and-rest-api-guidance}

メッセージング API は Braze REST APIと同じリージョン別 REST エンドポイントを使用しますが、認証とレスポンスの仕様は異なります。プライベートなサーバーサイドキー、レスポンスボディ、エラー、レート制限に関する一般的な REST API ガイダンスは、メッセージング API の記事で明示的に参照されていない限り適用されません。

リクエストフィールド、レスポンスボディ、ステータスコード、制限については、メッセージング API エンドポイントのドキュメントを信頼できる情報源としてご利用ください。