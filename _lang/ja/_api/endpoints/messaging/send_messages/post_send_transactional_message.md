---
nav_title: "POST: APIトリガー配信を使用してトランザクションメールを送信する"
article_title: "POST: APIトリガー配信を使用してトランザクションメールを送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、APIトリガー配信を使用したトランザクションメールメッセージの送信に関するBrazeエンドポイントの詳細について説明します。"

---

{% api %}
# APIトリガー配信を使用してトランザクションメールを送信する {#send-transactional-emails-using-api-triggered-delivery}
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> このエンドポイントを使用して、指定したユーザーに即時の単発トランザクションメッセージを送信します。

このエンドポイントは、Brazeの[トランザクションメールキャンペーン]({{site.baseurl}}/api/api_campaigns/transactional_campaigns/)と対応するキャンペーン IDの作成と併せて使用されます。

{% alert important %}
トランザクションメールは現在、一部のBrazeパッケージで利用できます。詳細については、担当のBrazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

[送信トリガーキャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)と同様に、このキャンペーンタイプでは、Brazeダッシュボード内にメッセージコンテンツを格納しながら、API経由でメッセージの送信タイミングと送信先を指定できます。メッセージの送信先となるオーディエンスまたはセグメントを受け入れる送信トリガーキャンペーンエンドポイントとは異なり、このキャンペーンタイプは注文確認やパスワードリセットなどのアラートの1対1メッセージングに特化しているため、このエンドポイントへのリクエストでは`external_user_id`または`user_alias`で1人のユーザーを指定する必要があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`transactional.send`権限を持つAPIキーを生成する必要があります。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `campaign_id` | 必須 | 文字列 | CampaignのID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `external_send_id`| オプション | 文字列 | Base64互換の文字列です。以下の正規表現に対して検証されます。<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>このオプションフィールドを使用すると、この特定の送信に対する内部識別子を渡すことができます。この識別子は、トランザクションHTTPイベントポストバックから送信されるイベントに含まれます。渡された場合、この識別子は重複排除キーとしても使用され、Brazeは24時間保存します。<br><br>同じ識別子を別のリクエストで渡しても、Brazeは24時間以内に新たな送信インスタンスを生成しません。|
| `trigger_properties`|オプション|オブジェクト|[トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。このリクエストのユーザーに適用されるパーソナライゼーションのキーと値のペアです。|
|`recipient`|必須|オブジェクト| このメッセージの対象となるユーザーです。`attributes`と単一の`external_user_id`または`user_alias`を含めることができます。<br><br>Brazeにまだ存在しないexternal IDを指定した場合、`attributes`オブジェクトにフィールドを渡すと、Brazeにこのユーザープロファイルが作成され、新規作成されたユーザーにこのメッセージが送信されます。<br><br>同じユーザーに対して`attributes`オブジェクトに異なるデータを含む複数のリクエストを送信した場合、`first_name`、`last_name`、`email`属性は同期的に更新され、メッセージにテンプレートとして組み込まれます。カスタム属性にはこれと同じ保護がないため、このAPIを使用してユーザーを更新し、異なるカスタム属性値を連続して渡す場合は注意してください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## 応答 {#response}

トランザクションメール送信エンドポイントは、このメッセージ送信のインスタンスを表す`dispatch_id`を返します。この識別子は、トランザクションHTTPイベントポストバックのイベントと共に使用して、1人のユーザーに送信された個々のメールのステータスを追跡できます。

### 応答例 {#example-responses}

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## トラブルシューティング {#troubleshooting}

エンドポイントは、場合によってはエラーコードと人間が判読可能なメッセージを返すこともあります。そのほとんどは検証エラーです。以下は、無効なリクエストを行った場合によく発生するエラーです。

| エラー | トラブルシューティング |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | 指定されたキャンペーン IDはトランザクションキャンペーン用ではありません。 |
| `The external reference has been queued.  Please retry to obtain send_id.` | external_send_idは最近作成されたものです。新しいメッセージを送信する場合は、新しいexternal_send_idを試してください。 |
| `キャンペーン does not exist` | 指定されたキャンペーン IDが既存のキャンペーンに対応していません。 |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | 指定されたキャンペーン IDはアーカイブされたキャンペーンに対応しています。 |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | 指定されたキャンペーン IDは一時停止中のキャンペーンに対応しています。 |
| `campaign_id must be a string of the campaign api identifier` | 指定されたCampaign IDは有効なフォーマットではありません。 |
| `Error authenticating credentials` | 指定されたAPIキーが無効です。 |
| `Invalid whitelisted IPs `| リクエストを送信しているIPアドレスがIPホワイトリストに含まれていません（使用されている場合）。 |
| `You do not have permission to access this resource` | 使用されたAPIキーには、このアクションを実行する権限がありません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

Brazeのほとんどのエンドポイントにはレート制限が実装されており、リクエストが多すぎると429のレスポンスコードを返します。トランザクション送信エンドポイントには、有料の時間単位割り当てがあり、単位で測定されます（例：パッケージに応じて1時間あたり50,000単位）。このエンドポイントには個別のエンドポイントごとのレート制限はありません。割り当てられた量を超えて送信できますが、SLAの対象となるのは割り当て量のみです。割り当て量を超えるリクエストは送信されますが、SLAの対象外となります。このエンドポイントへのリクエストは[全体の外部APIレート制限]({{site.baseurl}}/api/api_limits/)にカウントされます。その制限（例：全エンドポイントで1時間あたり250,000リクエスト）を超過した場合、Brazeは429を返し、制限がリセットされるまでリクエストをスロットリングします。トランザクションボリュームのカウントは毎時リセットされます。この機能についてさらに情報が必要な場合は、Brazeサポートにお問い合わせください。

## トランザクションHTTPイベントポストバック {#transactional-http-event-postback}

{% multi_lang_include http_event_postback.md %}

{% endapi %}