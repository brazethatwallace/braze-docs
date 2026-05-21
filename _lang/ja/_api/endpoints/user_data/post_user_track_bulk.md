---
nav_title: "POST: ユーザーの作成と更新（一括）"
article_title: "POST: ユーザーの作成と更新（一括）"
search_tag: Endpoint
page_order: 4.25
layout: api_page
page_type: reference
alias:
  - /unlisted_docs/track_users_bulk_partners/
  - /api/endpoints/user_data/post_user_track_bulk_partners/
description: "この記事では、一括ユーザートラッキングエンドポイントの詳細について説明します。"
---
{% api %}
# ユーザーの作成と更新（一括） {#create-and-update-users-bulk}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

このエンドポイントを使用して、カスタムイベントと購入を記録し、ユーザープロファイル属性を一括で更新します。

{% alert important %}
このエンドポイントは現在**限定ベータ版**です。現時点ではベータ版に新規顧客を追加していませんが、この機能がBraze統合に役立つと思われる場合は、Brazeアカウントマネージャーにお知らせください。
{% endalert %}

## このエンドポイントを使用するタイミング {#when-to-use-this-endpoint}

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)と同様に、このエンドポイントを使用してユーザープロファイルを更新できます。このエンドポイントは一括更新に適しています。

- **より大きなリクエスト:** 1リクエストあたり最大1,000ユーザーを送信できるため、大規模なバックフィルや同期に必要なリクエスト数を減らせます。
- **優先順位付け:** ピークトラフィック時には、`/users/track`へのリクエストが`/users/track/bulk`へのリクエストよりも優先されます。

オンボーディング中に多数のユーザープロファイルをバックフィルする場合や、日次同期の一部として大量のプロファイルを同期する場合に、このエンドポイントを使用してください。

{% alert note %}
`/users/track`エンドポイントのリクエストオブジェクト制限は、料金モデルと設定によって異なります。一括取り込みには`/users/track/bulk`を使用してください。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.track.bulk`権限を持つ[APIキー]({{site.baseurl}}/api/api_key/)が必要です。

ファイアウォールの背後でサーバー間呼び出しを行う場合は、Braze RESTエンドポイント（例: `rest.iad-01.braze.com`）を許可リストに追加する必要がある場合があります。詳細については、[APIエンドポイント]({{site.baseurl}}/api/basics/#api-definitions)を参照してください。

## レート制限 {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/bulk" %}

ほとんどの顧客の場合、このエンドポイントの基本速度制限は1秒あたり50リクエストです。

新しい契約の顧客は、契約された月間アクティブユーザー数に基づくバースト（秒単位）およびステディ（時間単位）の制限が適用される場合があります。

各`/users/track/bulk`リクエストのペイロード制限は2 MBで、アカウントの一括レート制限ポリシーに応じて、属性、イベント、購入全体で最大1,000オブジェクトを含めることができます。

各オブジェクトは1人のユーザーを更新できるため、1回のリクエストでアカウントのリクエストオブジェクト制限までの異なるユーザーを更新できます。さらに、各リクエストには、属性、イベント、購入全体でユーザープロファイルあたり最大100オブジェクトを含めることができます。

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object)
}
```

### リクエストパラメーター {#request-parameters}

{% alert important %}
各リクエストオブジェクトには、`external_id`、`user_alias`、`braze_id`、`email`、または`phone`のいずれかを含める必要があります。
{% endalert %}

| パラメーター | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `attributes` | オプション | 属性オブジェクトの配列 | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照 |
| `events` | オプション | イベントオブジェクトの配列 | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照 |
| `purchases` | オプション | 購入オブジェクトの配列 | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-requests}

### 1回のリクエストでユーザープロファイルを一括更新する {#bulk-update-user-profiles-in-one-request}

1回のリクエストで、アカウントのリクエストオブジェクト制限までのユーザープロファイルを更新します。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    },
    {
      "external_id": "user2",
      "string_attribute": "vegetables",
      "boolean_attribute_1": false,
      "integer_attribute": 25,
      "array_attribute": [
        "broccoli",
        "asparagus"
      ]
    }
  ]
}'
```

### 1回のリクエストで属性とイベントを送信する {#send-attributes-and-events-in-one-request}

アカウントの合計オブジェクト制限まで、同じリクエストに属性とイベントを含めます。

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    }
  ],
  "events": [
    {
      "external_id": "user2",
      "app_id": "your_app_identifier",
      "name": "rented_movie",
      "time": "2022-12-06T19:20:45+01:00",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}'
```

## 応答 {#responses}

### 成功メッセージ {#successful-message}

成功メッセージは次の応答を返します。

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}
```

### 非致命的エラーを含む成功メッセージ {#successful-message-with-non-fatal-errors}

リクエストが成功したが非致命的エラーがある場合（例: 大きなバッチ内の1つの無効なイベントオブジェクト）、次の応答を受け取ります。

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### 致命的エラーを含むメッセージ {#message-with-fatal-errors}

リクエストに致命的エラーがある場合、次の応答を受け取ります。

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### 致命的エラーの応答コード {#fatal-error-response-codes}

リクエストに致命的エラーがある場合にBrazeが返すステータスコードと関連するエラーメッセージについては、[致命的エラーと応答]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

「provided external_id is blacklisted and disallowed」というエラーを受け取った場合、リクエストに「ダミーユーザー」が含まれている可能性があります。詳細については、[スパムブロック]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)を参照してください。

## よくある質問 {#frequently-asked-questions}

### このエンドポイントと`/users/track`のどちらを使用すべきですか？ {#should-i-use-this-endpoint-or-userstrack}

ユースケースに基づいて両方のエンドポイントを使用してください。

- 大規模なバックフィルや同期には、`/users/track/bulk`を使用します。
- リアルタイムのユースケースには、`/users/track`を使用します。

### `/users/track/bulk`で使用できる識別子は何ですか？ {#what-identifiers-can-i-use-in-userstrackbulk}

各リクエストオブジェクトに、`external_id`、`braze_id`、`user_alias`、`email`、または`phone`のいずれかを含めてください。

### 1回のリクエストに属性、イベント、購入を含めることはできますか？ {#can-i-include-attributes-events-and-purchases-in-one-request}

はい。アカウントの合計リクエストオブジェクト制限まで、属性、イベント、購入を任意に組み合わせて含めることができます。

{% endapi %}