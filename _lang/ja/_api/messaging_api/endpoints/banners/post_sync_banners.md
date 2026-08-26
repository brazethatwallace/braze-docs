---
nav_title: "POST: ユーザーのバナーを取得する"
article_title: "POST: ユーザーのバナーを取得する"
permalink: /api/device_messaging_api/endpoints/banners/post_sync_banners
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "このエンドポイントを使用して、ユーザーの対象バナーを取得します。"
hidden: true
---

{% api %}
# ユーザーのバナーを取得する {#retrieve-banners-for-a-user}
{% apimethod post %}
/v1/device-messaging/banners/sync
{% endapimethod %}

{% alert important %}
このページはベータ版です。Device Messaging APIの機能とドキュメントは変更される可能性があります。
{% endalert %}

> このエンドポイントを使用して、ユーザーのリクエストされた各プレースメントに対する対象バナーを取得します。

レスポンスには、カスタムインターフェイスの構築に使用できる構造化されたバナープロパティが含まれます。レンダリングされたHTMLは含まれません。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、以下が必要です。

- バナーが有効なワークスペース
- `banners.sync` 権限を持つ[クライアントサイドREST APIキー]({{site.baseurl}}/api/device_messaging_api/authentication)
- Brazeインスタンスの[RESTエンドポイント]({{site.baseurl}}/api/basics#endpoints)

クライアントサイドREST APIキーを `Authorization` ヘッダーにBearerトークンとして含めてください。

## レート制限 {#rate-limit}

レート制限はワークスペースごとに適用されます。レート制限を超えた場合、Brazeは `429` ステータスコードを返します。利用可能な場合は、`X-RateLimit-Limit`、`X-RateLimit-Remaining`、`X-RateLimit-Reset` レスポンスヘッダーを使用して使用状況を監視してください。

詳細については、[Device Messaging APIのレート制限]({{site.baseurl}}/api/device_messaging_api/rate_limits)を参照してください。

## リクエストボディ {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データ型 | 説明 | 例 |
|---|---|---|---|---|
| `external_user_id` | 必須 | String | ユーザーのexternal ID。 | `user_abc123` |
| `app_id` | 必須 | String | [アプリAPI識別子]({{site.baseurl}}/api/identifier_types#app-identifier)。認証されたワークスペース内のアプリを識別する必要があります。 | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | 必須 | String | ホストアプリのバージョン。255文字を超えてはなりません。 | `1.0.0` |
| `placements` | 必須 | Array of strings | バナーを取得する1つ以上のプレースメントID。少なくとも1つのプレースメントIDを含めてください。 | `["home_hero", "sidebar_promo"]` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

*`YOUR_REST_API_URL`* をBrazeインスタンスの[RESTエンドポイント]({{site.baseurl}}/api/basics#endpoints)に置き換えてください。

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/sync' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "placements": [
    "home_hero",
    "sidebar_promo"
  ]
}'
```

## レスポンスパラメーター {#response-parameters}

| パラメーター | データ型 | 説明 |
|---|---|---|
| `banners` | Object | リクエストされた各プレースメントIDとその解決済みバナーのマップです。プレースメントに対象バナーがない場合、値は `null` になります。 |
| `banners.{placement_id}.id` | String | 一意のバナー識別子です。この値を使用してインプレッションイベントとクリックイベントをレポートします。 |
| `banners.{placement_id}.placement_id` | String | バナーに一致したプレースメントIDです。 |
| `banners.{placement_id}.is_control` | Boolean | バナーがコントロールグループのバリアントかどうかを示します。 |
| `banners.{placement_id}.is_test_send` | Boolean | バナーがテスト送信からのものかどうかを示します。デフォルトは `false` です。 |
| `banners.{placement_id}.expires_at` | Integer | バナーを表示すべきでなくなるUnixタイムスタンプ（秒単位）です。値が `-1` の場合、バナーは期限切れになりません。 |
| `banners.{placement_id}.properties` | Object or null | マーケターが定義したバナーのプロパティです。各プロパティには `type` と `value` が含まれます。 |
| `banners.{placement_id}.properties.{property}.type` | String | プロパティの型です。使用可能な値は `number`、`string`、`boolean`、`image`、`jsonobject`、`datetime` です。 |
| `banners.{placement_id}.properties.{property}.value` | Number, string, Boolean, or object | プロパティの値です。そのJSON型は `type` に対応します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスパラメーター" }

## レスポンス例 {#example-response}

リクエストが成功すると、`200` ステータスコードと、リクエストされた各プレースメントの解決済みバナーが返されます。

```json
{
  "banners": {
    "home_hero": {
      "id": "this_banner_is_a_stub_01",
      "placement_id": "home_hero",
      "is_control": false,
      "is_test_send": false,
      "expires_at": 1735689600,
      "properties": {
        "headline": {
          "type": "string",
          "value": "Level Up Your Game"
        },
        "cta_label": {
          "type": "string",
          "value": "Shop Now"
        }
      }
    },
    "sidebar_promo": null
  }
}
```

## ステータスコード {#status-codes}

| ステータスコード | 説明 |
|---|---|
| `200` | Brazeはリクエストされた各プレースメントのバナーデータを解決しました。 |
| `400` | リクエストにパラメーターの不足または無効なパラメーターが含まれています。 |
| `401` | クライアントサイドREST APIキーが不足しているか、無効であるか、`banners.sync` 権限がありません。 |
| `404` | エンドポイントが利用できません。このレスポンスは、APIキーの不足や無効とバナー機能の無効を区別しません。 |
| `429` | ワークスペースがレート制限を超えました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステータスコード" }

詳細については、[Device Messaging APIのエラー処理とリトライ]({{site.baseurl}}/api/device_messaging_api/error_handling)を参照してください。

{% endapi %}