---
nav_title: "POST:ユーザーを作成および更新する（同期処理）"
article_title: "POST:ユーザーの作成と更新（同期処理）"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "この記事では、同期処理のユーザー追跡Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを作成および更新する（同期処理） {#create-and-update-users-synchronous}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> このエンドポイントを使用して、カスタムイベントと購入を記録し、ユーザープロファイル属性を同期的に更新します。このエンドポイントは、ユーザープロファイルを非同期に更新する[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)と同様に機能します。

{% alert important %}
このエンドポイントは現在、**限定ベータ版**です。現在ベータ版への新規顧客の追加は行っていませんが、この機能がBrazeとの連携に有用だと思われる場合は、担当のBrazeアカウントマネージャーにお知らせください。
{% endalert %}

## 同期APIコールと非同期APIコール {#synchronous-and-asynchronous-api-calls}

非同期呼び出しでは、APIはステータスコード`201`を返します。これはリクエストが正常に受信され、理解され、受理されたことを示します。ただし、これはリクエストが完全に完了したことを意味するわけではありません。

同期呼び出しでは、APIはステータスコード`201`を返します。これはリクエストが正常に受信され、理解され、受け入れられ、完了したことを示します。呼び出し応答には、操作の結果として選択されたユーザープロファイルフィールドが表示されます。

このエンドポイントは、`/users/track`エンドポイントよりも低いレート制限を持っています（[レート制限](#rate-limit)を参照）。各`/users/track/sync`リクエストには、1つのイベントオブジェクト、1つの属性オブジェクト、**または**1つの購入オブジェクトのみを含めることができます。このエンドポイントは、同期呼び出しが必要なユーザープロファイルの更新用に予約してください。健全な実装のためには、`/users/track/sync`と`/users/track`を併用することをお勧めします。

例えば、同じユーザーに対して短時間に連続してリクエストを送信する場合、非同期の`/users/track`エンドポイントでは競合が発生する可能性がありますが、`/users/track/sync`エンドポイントでは、`2XX`レスポンスを受信した後にそれらのリクエストを順番に送信できます。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.track.sync`権限を持つ[APIキー]({{site.baseurl}}/api/api_key)が必要です。

サーバー間の呼び出しにAPIを使用する顧客がファイアウォールの内側にいる場合には、`rest.iad-01.braze.com`を許可リストに登録する必要が生じることがあります。

## レート制限 {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/sync" %}

すべての顧客に対して、このエンドポイントには1分あたり500リクエストの基本スピード制限を適用します。各`/users/track/sync`リクエストには、最大1つのイベントオブジェクト、1つの属性オブジェクト、または1つの購入オブジェクトを含めることができます。それぞれのオブジェクト（イベント、属性、および購入配列）は、それぞれ1人のユーザーを更新できます。

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### リクエストパラメーター {#request-parameters}

{% alert important %}
以下の表に記載されている各リクエストコンポーネントに対して、`external_id`、`user_alias`、`braze_id`、`email`、または`phone`のいずれかを含める必要があります。
{% endalert %}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `attributes` | オプション | 1つの属性オブジェクト | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)を参照してください |
| `events` | オプション | 1つのイベントオブジェクト | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object)を参照してください |
| `purchases` | オプション | 1つの購入オブジェクト | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)を参照してください |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## 応答 {#responses}

このエンドポイントの[リクエストパラメーター](#request-parameters)を使用すると、成功メッセージ、または致命的なエラーを含むメッセージのいずれかの応答を受け取ります。

### 成功メッセージ {#successful-message}

成功メッセージは以下の応答を返します。これには、Brazeが更新したユーザープロファイルデータに関する情報が含まれます。

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
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

## リクエストとレスポンスの例 {#example-requests-and-responses}

### external IDでカスタム属性を更新する {#update-a-custom-attribute-by-external-id}

#### リクエスト {#request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### 応答 {#response}

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### メールでカスタムイベントを更新する {#update-a-custom-event-by-email}

#### リクエスト

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "events": [
        {
            "email": "test@example.com",
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

#### 応答

```
{
    "users": [
        {
            "email": "test@example.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### ユーザーエイリアスで購入イベントを更新する {#update-a-purchase-event-by-user-alias}

#### リクエスト

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### 応答

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## よくある質問 {#frequently-asked-questions}

### 非同期エンドポイントと同期エンドポイントのどちらを使うべきですか？ {#should-i-use-the-asynchronous-or-synchronous-endpoint}

ほとんどのプロファイル更新では、`/users/track`エンドポイントが最適です。レート制限が高く、リクエストをバッチ処理できる柔軟性があるためです。ただし、`/users/track/sync`エンドポイントは、同じユーザーに対する短時間の連続リクエストによって競合が発生している場合に便利です。

### レスポンスタイムは`/users/track`エンドポイントと異なりますか？ {#does-the-response-time-differ-from-the-userstrack-endpoint}

同期呼び出しでは、APIはBrazeがリクエストを完了するまで待機してから応答を返します。その結果、同期リクエストは`/users/track`への非同期リクエストよりも平均的に時間がかかります。大半のリクエストでは、数秒以内にレスポンスが返ってきます。

### 複数のリクエストを同時に送信できますか？ {#can-i-send-multiple-requests-at-the-same-time}

はい、リクエストが異なるユーザーに対するものであるか、各リクエストが1人のユーザーに対して異なる属性、イベント、購入を更新する場合は可能です。

同じユーザーに対して、同じ属性、イベント、または購入のために複数のリクエストを送信する場合、Brazeは競合の発生を防ぐために、各リクエストの間に成功した応答を待つことを推奨します。

同じユーザーに対して`/users/track`を短時間に連続して呼び出してもプロファイルの状態が一貫しない場合は、それらの更新を`/users/track/sync`に切り替え、一度に1つのリクエストを発行し、次のリクエストの前に各`2XX`レスポンスを待ってください。この順序付けは、タイトなループや並列ワーカー間での読み取り後書き込みの競合を回避するためにサポートされている方法です。

### なぜレスポンスの値が元のリクエストの値と一致しないのですか？ {#why-doesnt-the-response-value-match-the-one-in-my-original-request}

リクエストは完了しましたが、カスタム属性の値が更新されなかった可能性があります。これは、カスタム属性の更新が最大文字数を超えている場合、配列の制限を超えている場合、またはユーザーがBrazeに存在せず`_update_existing_only = true`が設定されている場合に発生する可能性があります。

このような場合、リクエストは完了したものの、希望する更新が行われなかったことを示すものとして応答を処理してください。[なぜレスポンスの値が元のリクエストの値と一致しないのですか？](#why-doesnt-the-response-value-match-the-one-in-my-original-request)に記載されている理由を参考にトラブルシューティングを行ってください。

{% endapi %}