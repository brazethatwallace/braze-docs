---
nav_title: エラー処理とリトライ
article_title: Device Messaging APIのエラー処理とリトライ
page_order: 2
page_type: reference
description: "Device Messaging APIのレスポンス、エラー、リトライの処理方法について説明します。"
hidden: true
---

# Device Messaging APIのエラー処理とリトライ {#device-messaging-api-error-handling-and-retries}

Device Messaging APIのレスポンスボディと成功のセマンティクスはエンドポイントによって異なります。各エンドポイントのレスポンススキーマとステータスコード表を正式な仕様として使用してください。

{% alert important %}
このページはベータ版です。Device Messaging APIの機能とドキュメントは変更される可能性があります。アクセスをリクエストするには、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 成功レスポンス {#success-responses}

Bannerエンドポイントは異なる成功レスポンスを使用します。

- `POST /v1/device-messaging/banners/sync`は`banners`オブジェクトを含む`200`ステータスコードを返します。
- `POST /v1/device-messaging/banners/track`は`events_processed`と`message`を含む`202`ステータスコードを返します。Brazeが個別のイベントをスキップした場合、レスポンスには`errors`配列も含まれます。

トラッキングエンドポイントからの`202`レスポンスは、Brazeが少なくとも1つの有効なイベントを受け入れたことを意味します。スキップされたイベントを特定するには、`errors`配列を確認してください。

## エラーレスポンス {#error-responses}

エラーレスポンスのフィールドも異なります。

- バナー取得エラーでは`error`フィールドが使用されます。
- バナートラッキングエラーでは`message`フィールドが使用され、インデックス付きの`errors`配列が含まれる場合があります。

アプリケーションの動作を判断するためにエラーメッセージのテキストを解析しないでください。代わりに、HTTPステータスコードとエンドポイント固有のフィールドを使用してください。

## リトライのガイダンス {#retry-guidance}

リトライするかどうかを判断する際には、以下のガイダンスを参考にしてください。

| ステータスコード | リトライのガイダンス |
|---|---|
| `400` | リトライする前にリクエストを修正してください。バナートラッキングの場合は、スキップされたイベントを修正してからリトライしてください。 |
| `401`または`403` | リトライする前に、クライアントサイドのREST APIキーとその権限を確認してください。 |
| `404` | ワークスペースでDevice Messaging APIが有効になっていること、およびエンドポイントURLが正しいことを確認してください。 |
| `429` | リクエストレートを下げ、エクスポネンシャルバックオフでリトライしてください。利用可能な場合は、レートリミットのレスポンスヘッダーを使用してください。 |
| `5XX` | エクスポネンシャルバックオフと最大リトライ回数を設定してリトライしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Device Messaging APIのリトライガイダンス" }

正確なレスポンスボディとサポートされているステータスコードについては、関連するエンドポイントを参照してください。

- [ユーザーのバナーを取得する]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)
- [バナー分析イベントを追跡する]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)