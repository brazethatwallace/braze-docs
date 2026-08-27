---
nav_title: "POST: バナー分析イベントのトラッキング"
article_title: "POST: バナー分析イベントのトラッキング"
permalink: /api/device_messaging_api/endpoints/banners/post_track_banner_events
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "このエンドポイントを使用して、バナーのインプレッションイベントとクリックイベントをトラッキングします。"
hidden: true
---

{% api %}
# バナー分析イベントのトラッキング {#track-banner-analytics-events}
{% apimethod post %}
/v1/device-messaging/banners/track
{% endapimethod %}

{% alert important %}
このページはベータ版です。Device Messaging APIの機能とドキュメントは変更される可能性があります。
{% endalert %}

> このエンドポイントを使用して、バナーのインプレッションイベントとクリックイベントを記録します。

Brazeは各イベントを個別に検証します。リクエストに有効なイベントと無効なイベントの両方が含まれている場合、Brazeは有効なイベントを処理し、スキップされたイベントの詳細を`errors`配列で返します。有効なイベントがない場合、Brazeは`400`ステータスコードを返します。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、以下が必要です。

- バナーが有効になっているワークスペース
- `banners.track`権限を持つ[クライアントサイドREST APIキー]({{site.baseurl}}/api/device_messaging_api/authentication)
- Brazeインスタンスの[RESTエンドポイント]({{site.baseurl}}/api/basics#endpoints)
- [ユーザーのバナー取得エンドポイント]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)から返されたバナー`id`

クライアントサイドREST APIキーを`Authorization`ヘッダーにBearerトークンとして含めてください。

## レート制限 {#rate-limit}

レート制限はワークスペースごとに適用されます。レート制限を超えた場合、Brazeは`429`ステータスコードを返します。利用可能な場合は、`X-RateLimit-Limit`、`X-RateLimit-Remaining`、`X-RateLimit-Reset`、`X-RateLimit-Retry-After`レスポンスヘッダーを使用して使用状況を監視し、リトライのタイミングを判断してください。

詳細については、[Device Messaging APIのレート制限]({{site.baseurl}}/api/device_messaging_api/rate_limits)を参照してください。

## リクエスト本文 {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "{BANNER_ID}",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    }
  ]
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データ型 | 説明 | 例 |
|---|---|---|---|---|
| `external_user_id` | 必須 | String | リクエスト内のすべてのイベントに関連付けられたユーザーのexternal ID。UTF-8エンコードされた値は987バイト未満である必要があります。 | `user_abc123` |
| `app_id` | 必須 | String | [アプリAPI識別子]({{site.baseurl}}/api/identifier_types#app-identifier)。認証されたワークスペース内のアプリを識別する必要があります。 | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | 必須 | String | ホストアプリのバージョン。255文字を超えてはなりません。 | `1.0.0` |
| `events` | 必須 | オブジェクトの配列 | 記録する1つ以上のバナー分析イベント。 | `[{"id":"bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E","event_type":"impression","timestamp":"2026-04-09T12:00:00Z"}]` |
| `events[].id` | 必須 | String | ユーザーのバナー取得エンドポイントから返されたバナー`id`。Brazeがイベントを正しいキャンペーンとバリアントに帰属させるために、`placement_id`ではなくバナーIDを使用してください。 | `bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E` |
| `events[].event_type` | 必須 | String | イベントタイプ。使用可能な値は`impression`と`click`です。 | `impression` |
| `events[].timestamp` | 必須 | String | イベントが発生した日時。[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式の文字列でフォーマットされます。 | `2026-04-09T12:00:00Z` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

*`YOUR_REST_API_URL`* をBrazeインスタンスの[RESTエンドポイント]({{site.baseurl}}/api/basics#endpoints)に置き換えてください。

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/track' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    },
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "click",
      "timestamp": "2026-04-09T12:00:05Z"
    }
  ]
}'
```

## レスポンスパラメーター {#response-parameters}

| パラメーター | データ型 | 説明 |
|---|---|---|
| `events_processed` | Integer | Brazeが検証してキューに入れたイベントの数。 |
| `message` | String | 受け入れられたイベントバッチのステータス。 |
| `errors` | オブジェクトの配列 | Brazeがスキップしたイベントの詳細。Brazeがすべてのイベントを処理した場合、この配列は存在しません。 |
| `errors[].type` | String | スキップされたイベントの検証エラー。 |
| `errors[].index` | Integer | リクエストの`events`配列内のスキップされたイベントのゼロベースインデックス。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスパラメーター" }

## レスポンス例 {#example-responses}

### すべてのイベントが処理された場合 {#all-events-processed}

Brazeがすべてのイベントを受け入れた場合、`202`ステータスコードを返します。

```json
{
  "events_processed": 2,
  "message": "success"
}
```

### 一部のイベントがスキップされた場合 {#some-events-skipped}

Brazeは、少なくとも1つの有効なイベントを受け入れた場合にも`202`ステータスコードを返します。レスポンスにはスキップされたイベントが示されます。

```json
{
  "events_processed": 2,
  "message": "success",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click.",
      "index": 2
    }
  ]
}
```

### 有効なイベントがない場合 {#no-valid-events}

Brazeがイベントを処理できない場合、`400`ステータスコードを返します。

```json
{
  "message": "No valid events provided.",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click.",
      "index": 0
    },
    {
      "type": "'timestamp' is required",
      "index": 1
    }
  ]
}
```

## ステータスコード {#status-codes}

| ステータスコード | 説明 |
|---|---|
| `202` | Brazeは少なくとも1つのイベントを受け入れました。レスポンスにはスキップされたイベントが一覧表示されます。 |
| `400` | リクエストの形式が不正であるか、必須フィールドが無効であるか、有効なイベントがありません。 |
| `401` | クライアントサイドREST APIキーが欠落しているか無効です。 |
| `403` | クライアントサイドREST APIキーに`banners.track`権限がありません。 |
| `404` | ワークスペースでバナー機能が有効になっていません。 |
| `429` | ワークスペースがレート制限を超えました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステータスコード" }

詳細については、[Device Messaging APIのエラー処理とリトライ]({{site.baseurl}}/api/device_messaging_api/error_handling)を参照してください。

{% endapi %}