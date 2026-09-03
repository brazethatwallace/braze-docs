---
nav_title: "POST: ユーザーの追跡（一括）"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "この記事では、ユーザーの追跡（一括）エンドポイントの詳細について説明します。"
---

{% api %}
# ユーザーの追跡（一括） {#track-users-bulk}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> このエンドポイントを使用して、カスタムイベントと購入を記録し、ユーザープロファイル属性を一括で更新します。

{% alert important %}
このエンドポイントは現在ベータ版です。ベータへの参加に興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## このエンドポイントを使用するタイミング {#when-to-use-this-endpoint}

[POST: ユーザーの追跡エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites)と同様に、このエンドポイントを使用してユーザープロファイルを更新できます。ただし、このエンドポイントは一括更新に適しています。

- **より大きなリクエスト:** このエンドポイントでは、1リクエストあたり10,000ユーザーを処理できるため、一括更新のニーズを達成するために必要なリクエスト数が少なくなります。
- **優先順位付け:** ピークトラフィック時には、`/users/track`からのリクエストが`/users/track/bulk`からのリクエストよりも優先されます。両方のエンドポイントを使用することで、データ取り込みをより細かくコントロールできます。

オンボーディング中に多数のユーザープロファイルをバックフィルする場合や、日次同期の一環として大量のユーザープロファイルを同期する場合に、このエンドポイントの使用を検討してください。

{% alert note %}
2025年5月26日以降、このエンドポイントはコンバージョン指標の追跡、例外イベントのトリガー、またはアクションベースのキャンペーンやキャンバスのトリガーにも使用できます。この動作は、他のBrazeデータ取り込み方法と同様です。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.track.bulk`権限を持つAPIキーが必要です。

サーバー間呼び出しにAPIを使用している場合、ファイアウォールの内側にいる場合はエンドポイント（例: `rest.iad-01.braze.com`）を許可リストに追加する必要がある場合があります。詳細については、[インスタンスごとのエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を参照してください。

## レート制限 {#rate-limit}

このエンドポイントには、すべての顧客に対して毎秒5リクエストの基本速度制限が適用されます。

各`/users/sync/bulk`リクエストのペイロード制限は4&nbsp;MBで、最大10,000のイベント、属性、または購入オブジェクトを含めることができます。

各オブジェクト（イベント、属性、購入の配列）はそれぞれ1ユーザーを更新できるため、1回のリクエストで最大10,000の異なるユーザーを更新できます。1つのユーザープロファイルは、1回のリクエストで最大100オブジェクトで更新できます。

{% alert note %}
レート制限の引き上げが必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}


## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### リクエストパラメーター {#request-parameters}

{% alert important %}
以下の表に記載されている各リクエストコンポーネントには、`external_id`、`user_alias`、`braze_id`、`email`、または`phone`のいずれかが必須です。
{% endalert %}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `attributes` | オプション | 属性オブジェクトの配列 | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照 |
| `events` | オプション | イベントオブジェクトの配列 | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照 |
| `purchases` | オプション | 購入オブジェクトの配列 | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## リクエスト例 {#example-requests}

### 1回のリクエストで10,000ユーザープロファイルを一括更新 {#bulk-update-10000-user-profiles-in-one-request}

最大10,000のユーザープロファイルを更新できます。以下は、リクエストが10,000の属性オブジェクトで構成される場合の省略された例です。

```json
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
                "asparagus",
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

以下は、リクエストが属性オブジェクトとイベントオブジェクトの両方で構成される場合の例です。

```json
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
        },
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

### 成功メッセージ {#successful-messages}

成功メッセージには以下の応答が返されます。

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### 致命的でないエラーを含む成功メッセージ {#successful-message-with-non-fatal-errors}

メッセージは成功したものの、長いイベントリストの中に1つの無効なイベントオブジェクトがあるなど、致命的でないエラーがある場合、以下の応答が返されます。

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

### 致命的なエラーを含むメッセージ {#message-with-fatal-errors}

メッセージに致命的なエラーがある場合、以下の応答が返されます。

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

#### 致命的なエラーの応答コード {#fatal-error-response-codes}

リクエストで致命的なエラーが発生した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラーと応答]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

`provided external_id is blacklisted and disallowed`というエラーが表示された場合、リクエストに「ダミーユーザー」が含まれている可能性があります。詳細については、[スパムブロック]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)を参照してください。

## よくある質問 {#frequently-asked-questions}

### このエンドポイントと通常の`/users/track`のどちらを使用すべきですか？ {#should-i-use-this-endpoint-or-regular-userstrack}

両方を使用することをお勧めします。

- 大規模なユーザープロファイルのバックフィルと同期には、`/users/track/bulk`エンドポイントを使用してください。
- リアルタイムのユースケースには、`/users/track`エンドポイントを使用してください。

### /users/track/bulkで使用できる識別子は何ですか？ {#what-identifiers-can-i-use-in-userstrackbulk}

`external_id`、`braze_id`、`user_alias`、`email`、または`phone`のいずれかが必須です。その他の例については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)、[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)、または[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)のドキュメントを参照してください。

### 1つのリクエストに属性、イベント、購入を含めることはできますか？ {#can-i-include-attributes-events-and-purchases-in-one-request}

はい。1リクエストあたり最大10,000オブジェクトまで、任意の数の属性、イベント、購入オブジェクトでリクエストを構成できます。


{% endapi %}