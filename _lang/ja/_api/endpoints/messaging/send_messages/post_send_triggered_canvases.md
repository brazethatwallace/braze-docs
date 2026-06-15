---
nav_title: "POST: APIトリガー配信を使用したCanvasメッセージの送信"
article_title: "POST: APIトリガー配信を使用したCanvasメッセージの送信"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIトリガー配信を使用したCanvas送信Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# APIトリガー配信を使用したCanvasメッセージの送信 {#send-canvas-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、APIトリガー配信でCanvasメッセージを送信します。

APIトリガー配信を使用すると、メッセージのコンテンツをBrazeダッシュボードに保存しながら、APIを使用してメッセージの送信タイミングと送信先を指定できます。

このエンドポイントでメッセージを送信するには、[Canvas ID]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)（Canvasの構築時に作成されます）が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`canvas.trigger.send` 権限を持つAPIキーを生成する必要があります。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) Canvas context properties that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) Canvas context properties for this user; key-value pairs override any keys that conflict with the parent `context`,
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an `attributes` object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | 必須 | 文字列 | [Canvas識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `context` | オプション | オブジェクト | このリクエストのすべての受信者に対するCanvasコンテキストプロパティです。パーソナライゼーションのキーと値のペアは、受信者ごとの`context`でキーが上書きされない限り、すべてのユーザーに適用されます。`context`オブジェクトは最大50KBです。 |
| `broadcast` | オプション | ブール値 | BrazeダッシュボードでCanvasのターゲットオーディエンスとして設定されたSegment全体にメッセージを送信する場合、`broadcast`をtrueに設定する必要があります。このパラメーターのデフォルトはfalseです（2017年8月31日現在）。<br><br>`broadcast`がtrueに設定されている場合、`recipients`リストを含めることはできません。ただし、`broadcast: true`を設定する際は注意が必要です。意図せずこのフラグを設定すると、想定よりも大きなオーディエンスにメッセージが送信される可能性があります。 |
| `audience` | オプション | 接続オーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。`audience`を含めると、メッセージはカスタム属性やサブスクリプションステータスなど、定義されたフィルターに一致するユーザーにのみ送信されます。 |
| `recipients` | オプション | 配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。<br><br>`send_to_existing_only`が`false`の場合、受信者に`attributes`オブジェクトを含める必要があります。<br><br>指定されておらず、`broadcast`が`true`に設定されている場合、メッセージはBrazeダッシュボードでCanvasのターゲットオーディエンスとして設定されたSegment全体に送信されます。<br><br>`recipients`配列には最大50個のオブジェクトを含めることができます。各オブジェクトには`external_user_id`、`user_alias`、または`email`のいずれか1つを正確に含める必要があり、Canvasコンテキストプロパティ用の受信者ごとの`context`オブジェクトを含めることもできます（受信者ごとのキーは競合する場合に親レベルの`context`を上書きします）。<br><br>`email`が識別子の場合、受信者オブジェクトに[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)を含める必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## レスポンスの詳細 {#response-details}

メッセージ送信エンドポイントのレスポンスには、メッセージのディスパッチを参照するための`dispatch_id`が含まれます。`dispatch_id`はメッセージディスパッチのIDです（Brazeプラットフォームから送信される各「送信」に固有のID）。詳細については、[ディスパッチIDの動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/)を参照してください。

### 成功レスポンスの例 {#example-success-response}

ステータスコード`201`は、次のレスポンス本文を返す可能性があります。Canvasがアーカイブ、停止、または一時停止されている場合、このエンドポイントを通じてCanvasは送信されません。

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Canvasがアーカイブされている場合、次の`notice`メッセージが表示されます：「The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect.」Canvasがアクティブでない場合、次の`notice`メッセージが表示されます：「The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.」

リクエストで致命的なエラーが発生した場合は、エラーコードと説明について[エラーとレスポンス]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

## 考慮事項 {#considerations}

APIトリガー配信を使用してCanvasメッセージを送信するAPI呼び出しを行う際には、以下の点を考慮してください。

- **既存ユーザーへの送信**：`send_to_existing_only`が`true`（デフォルト値）に設定されている場合、メッセージはBrazeの既存ユーザーにのみ送信されます。
- **新規ユーザーの作成**：`send_to_existing_only`が`false`に設定されている場合、`attributes`オブジェクトを含める必要があります。指定されたIDのユーザーが存在しない場合、BrazeはそのIDと属性でユーザーを作成してからメッセージを送信します。
- **新規プロファイルには`send_to_existing_only: false`と`attributes`が必要です。** Brazeは同じ受信者内の`attributes`オブジェクトから送信前の作成または更新を実行します。`send_to_existing_only`を`false`に設定しても`attributes`を省略した場合（または空のオブジェクトを送信した場合）、Brazeは同じ方法でプロファイルデータをハイドレートしないため、このパターンが意図する「ユーザーを作成または更新してから送信する」動作は得られません。
- **メールとSMSのアドレス指定：** まだBrazeに存在しないユーザーへのメールまたはSMSのAPIトリガー送信のほとんどでは、`attributes`内に必要な配信フィールド（例：`email`、またはワークスペースがSMSに使用する電話属性）を含めてください。同じ呼び出しでオプトイン状態を変更する必要がある場合は、サブスクリプショングループのメンバーシップやサブスクリプションステータスもそこで設定できます。
- **Canvasの適格性：** プロファイルが存在または更新された後も、そのユーザーはCanvasのダッシュボードターゲットオーディエンスとチャネル送信ルール（例：メールのオプトイン済み）に一致する必要があります。一致しない場合、Brazeはメッセージを送信しません。
- **ユーザーエイリアスの制限**：`send_to_existing_only`フラグはユーザーエイリアスでは使用できません。エイリアスのみのユーザーに送信するには、そのユーザーがすでにBrazeに存在している必要があります。
- **Segmentターゲティング**：このエンドポイントでは`segment_id`パラメーターはサポートされていません。Segmentをターゲットにするには、BrazeダッシュボードのCanvasのターゲットオーディエンス設定でSegmentを設定し、`broadcast: true`を使用するか、[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)フィルターで`audience`パラメーターを使用します。
- **複合ターゲティング**：`recipients`パラメーターを含め、かつダッシュボードでターゲットSegmentを設定した場合、メッセージはAPI呼び出しで指定されたユーザープロファイルのうち、Segmentのフィルターにも一致するものにのみ送信されます。
- **サーバー間通信**：サーバー間通信を行う場合、ファイアウォールの内側にいるときは適切なAPI URLを許可リストに追加する必要がある場合があります。

## Canvasの属性オブジェクト {#attributes-object-for-canvas}

メッセージングオブジェクト`attributes`を使用して、`canvas/trigger/send`エンドポイントでAPIトリガーCanvasを送信する前に、ユーザーの属性と値を追加、作成、または更新します。このAPI呼び出しは、Canvasを処理して送信する前にユーザー属性オブジェクトを処理します。これにより、[競合]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/)によって発生する問題のリスクを最小限に抑えることができます。ただし、デフォルトでは、サブスクリプショングループをこの方法で更新することはできません。

{% alert note %}
このエンドポイントのCampaignバージョンをお探しですか？[APIトリガー配信を使用したCampaignメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)を確認してください。
{% endalert %}

{% endapi %}