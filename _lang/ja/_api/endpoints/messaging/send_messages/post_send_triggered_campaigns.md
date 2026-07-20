---
nav_title: "POST:APIトリガーによる配信でキャンペーンを送信する"
article_title: "POST:APIトリガー配信でキャンペーンを送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIトリガー配信を使用したキャンペーンの送信Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# APIトリガー配信を使用したキャンペーンメッセージの送信 {#send-campaign-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、APIトリガー配信により、指定したユーザーに即時の1回限りのメッセージを送信します。

APIトリガー配信を使用すると、メッセージのコンテンツをBrazeダッシュボード内に保存しながら、メッセージの送信タイミングと送信先をAPIを使用して指定できます。

セグメントをターゲットにしている場合、リクエストの記録は[開発者コンソール](https://dashboard.braze.com/app_settings/developer_console/activitylog/)に保存されます。このエンドポイントを使用してメッセージを送信するには、[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)を構築する際に作成した[キャンペーンID]({{site.baseurl}}/api/identifier_types)が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`campaigns.trigger.send` 権限を持つAPIキーを生成する必要があります。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | [キャンペーン識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `send_id` | オプション | 文字列 | [送信識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| `trigger_properties` | オプション | オブジェクト | [トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object)を参照してください。パーソナライゼーションのキーと値のペアは、このリクエストの全ユーザーに適用されます。 |
| `broadcast` | オプション | ブール値 | Brazeダッシュボードでキャンペーンのターゲットオーディエンスとして設定されたセグメント全体にメッセージを送信する場合は、`broadcast`をtrueに設定する必要があります。このパラメーターのデフォルトはfalseです（2017年8月31日現在）。<br><br>`broadcast`がtrueに設定されている場合、`recipients`リストを含めることはできません。ただし、`broadcast: true`を設定する際は注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きなオーディエンスにメッセージが送信される可能性があります。 |
| `audience` | オプション | 接続オーディエンスオブジェクト | [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience)を参照してください。`audience`を含めると、メッセージはカスタム属性や購読ステータスなど、定義されたフィルターに一致するユーザーにのみ送信されます。 |
| `recipients` | オプション | 配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object)を参照してください。<br><br>`send_to_existing_only`が`false`の場合、`attributes`オブジェクトを含める必要があります。<br><br>ネストされた`attributes`オブジェクト内に`subscription_groups`を含めることで、ユーザーの購読グループのステータスを更新できます。詳細については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)を参照してください。<br><br>`recipients`が指定されず、`broadcast`がtrueに設定されている場合、メッセージはBrazeダッシュボードでキャンペーンのターゲットオーディエンスとして設定されたセグメント全体に送信されます。<br><br>`email`が識別子の場合、受信者オブジェクトに[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers)を含める必要があります。 |
| `attachments` | オプション | 配列 | `broadcast`がtrueに設定されている場合、`attachments`リストを含めることはできません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

### 受信者の解決動作 {#recipient-resolution-behavior}

このセクションでは、Brazeが送信先のユーザープロファイルをどのように選択するか、および1つのプロファイルが選択されなかった場合に何が起こるかについて説明します。

ユーザーの購読グループのステータスは、`attributes`オブジェクト内に`subscription_groups`パラメーターを含めることで更新できます。詳細については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)を参照してください。

#### 受信者の制限とプロファイル作成 {#recipient-limits-and-profile-creation}

このエンドポイントにおける受信者の制限とプロファイル作成の仕組みについて説明します。

- `recipients`配列には最大50個のオブジェクトを含めることができ、各オブジェクトには単一の`external_user_id`文字列と`trigger_properties`オブジェクトが含まれます。
- `send_to_existing_only`が`true`（デフォルト）の場合、Brazeは既存ユーザーにのみメッセージを送信します。
- `send_to_existing_only`が`false`で`attributes`オブジェクトが提供されている場合、Brazeはユーザーが存在しない場合に新規ユーザーを作成します。
- **新規プロファイルには`send_to_existing_only: false`と`attributes`が必要です。** Brazeは同じ受信者内の`attributes`オブジェクトから送信前の作成または更新を実行します。`send_to_existing_only`を`false`に設定しても`attributes`を省略した場合（または空のオブジェクトを送信した場合）、Brazeは同じ方法でプロファイルデータをハイドレートしないため、このパターンが意図する「ユーザーの作成または更新後に送信」という動作は得られません。
- **メールおよびSMSのアドレス指定。** まだBrazeに存在しないユーザーへのメールまたはSMSのAPIトリガー送信のほとんどの場合、`attributes`内に必要な配信フィールド（例：`email`、またはワークスペースがSMSに使用する電話属性）を含めてください。同じ呼び出しでオプトイン状態を変更する必要がある場合は、購読グループのメンバーシップや購読ステータスもそこで設定できます。
- **キャンペーンの適格性。** プロファイルが存在または更新された後も、そのユーザーはキャンペーンのダッシュボードターゲットオーディエンスとチャネル送信ルール（例：メールのオプトイン済み）に一致する必要があります。一致しない場合、Brazeはメッセージを送信しません。
- `send_to_existing_only`を`false`に設定することはユーザーエイリアスではサポートされていません。このエンドポイントを通じてエイリアスのみの新規ユーザーを作成することはできません。エイリアスのみのユーザーに送信するには、そのユーザーが既にBrazeに存在している必要があります。

#### メール識別子と優先順位の同点 {#email-identifier-and-prioritization-ties}

メールで受信者を識別する場合、Brazeは`prioritization`を使用します。Brazeは`prioritization`が1つのプロファイルを返した場合にのみ送信します。

- `email`を識別子として使用する場合、Brazeは`prioritization`を使用して受信者を解決します。
- `prioritization`が同点を返した場合、Brazeは送信しません。
- 同点が解消され、`prioritization`が1つのプロファイルを返した後にBrazeは送信します。たとえば、プロファイルの更新によってあるユーザーの順序フィールドが変更された場合、`prioritization`がプロファイルを一意に識別できるようになった時点でBrazeは送信します（[リトライ動作と`send_to_existing_only`](#retry-behavior-and-send_to_existing_only)を参照）。
- `prioritization`がプロファイルを返さない場合も、Brazeは送信しません。

#### リトライ動作とsend_to_existing_only {#retry-behavior-and-send_to_existing_only}

`prioritization`が正確に1つのプロファイルを返さない場合に何が起こるかについて説明します。

- `prioritization`が正確に1つのユーザープロファイルを返さない場合、Brazeは最大40回まで解決をリトライします。このリトライ動作は想定されたものです。
- `send_to_existing_only`の設定は`prioritization`の同点動作を変更しません。この設定が`true`でも`false`でも、同じ同点およびリトライ動作が適用されます。

`external_user_id`または`user_alias`で識別された受信者に対してメール専用キャンペーンをトリガーし、そのユーザープロファイルに呼び出し時点でメールアドレスがない場合、Brazeは約2時間まで送信をリトライします。これは、ユーザーの作成とメールアドレスの設定が短い間隔で行われる一般的なパターンに対応しています。遅延なく送信するには、`recipients[].attributes`内に`email`属性を含めて、トリガーと同じ呼び出しでアドレスを設定してください。

{% alert note %}
このエンドポイントでは`segment_id`パラメーターはサポートされていません。セグメントをターゲットにするには、Brazeダッシュボードのキャンペーンのターゲットオーディエンス設定でセグメントを設定し、`"broadcast": true`を使用するか、[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience)フィルターで`audience`パラメーターを使用してください。
{% endalert %}

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## 応答の詳細 {#response-details}

メッセージ送信エンドポイントの応答には、メッセージのディスパッチを参照するための`dispatch_id`が含まれます。`dispatch_id`はメッセージディスパッチのIDで、Brazeから送信される各送信に固有のIDです。このエンドポイントを使用すると、バッチ処理されたユーザーセット全体に対して単一の`dispatch_id`を受け取ります。`dispatch_id`の詳細については、[ディスパッチIDの動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)に関するドキュメントを参照してください。

リクエストで致命的なエラーが発生した場合のエラーコードと説明については、[エラーとレスポンス]({{site.baseurl}}/api/errors#fatal-errors)を参照してください。

## キャンペーンの属性オブジェクト {#attributes-object-for-campaigns}

Brazeには`attributes`というメッセージングオブジェクトがあり、APIトリガーキャンペーンを送信する前に、ユーザーの属性や値を追加・作成・更新できます。このAPI呼び出しとして`campaign/trigger/send`エンドポイントを使用すると、キャンペーンを処理して送信する前にユーザー属性オブジェクトが処理されます。これにより、[競合]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)による問題が発生するリスクを最小限に抑えることができます。

{% alert tip %}
このエンドポイントのキャンバスバージョンをお探しですか？[APIトリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)をご確認ください。
{% endalert %}

### JSONボディにLiquidを直接記述してもレンダリングされないのはなぜですか？ {#why-doesnt-liquid-render-when-i-put-it-directly-in-my-json-body}

リクエストボディが有効なJSONの場合、Brazeはペイロード内のLiquidをサーバー上で評価します。Liquidを生の文字列として埋め込む場合は、ボディが有効なJSONのままになるよう、文字列を引用符で囲みエスケープしてください。たとえば、文字列内のダブルクォートをエスケープします。ボディがJSONの解析に失敗した場合、BrazeはLiquidを評価する前に`400`を返します。サポートされている場合は、ペイロードにLiquidを直接埋め込む代わりに、[`trigger_properties`]({{site.baseurl}}/api/objects_filters/trigger_properties_object)を通じてダイナミックな値を渡してください。

{% endapi %}