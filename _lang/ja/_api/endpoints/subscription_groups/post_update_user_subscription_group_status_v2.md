---
nav_title: "POST:ユーザーのサブスクリプショングループステータスを更新する v2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "この記事では、「ユーザーのサブスクリプショングループステータスの更新」Braze V2エンドポイントの詳細について説明します。"

platform: API
channel:
  - Email
---

{% api %}
# ユーザーのサブスクリプショングループステータスの更新 (V2) {#update-users-subscription-group-status-v2}
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> このエンドポイントを使用して、Brazeダッシュボード上で最大50ユーザーのサブスクリプション状態を一括更新します。

サブスクリプショングループの `subscription_group_id` にアクセスするには、**サブスクリプショングループ**ページに移動します。

**メールサブスクリプショングループ**の例を確認するか、このエンドポイントをテストするには：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

**SMSサブスクリプショングループ**の例を確認するか、このエンドポイントをテストするには：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

**WhatsAppグループ**の例を確認するか、このエンドポイントをテストするには：

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`subscription.status.set` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

{% alert note %}
このエンドポイントを[LINEサブスクリプショングループ]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups/)で使用したい場合は、カスタマーサクセスマネージャーにお問い合わせください。<br><br>LINEサブスクリプショングループの場合、Webサイトやアプリの同意を別途追跡するためにカスタム属性を使用し、そのカスタム属性とLINEサブスクリプション状態を組み合わせてCampaignsのターゲティングを行うことをお勧めします。このアプローチにより、サブスクリプション状態がLINEアプリで実際に購読したユーザーを正確に反映するようになります。APIを使用してLINEサブスクリプショングループにユーザーを手動で追加すると、BrazeはLINEアプリでユーザーを再購読させたり、LINEでアカウントをブロックしたユーザーにメッセージを送信したりできないため、状態の不一致や送信失敗が発生する可能性があります。
{% endalert %}

## V1との違い {#differences-from-v1}

V2エンドポイントは[V1エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)と以下の点で異なります。

- **複数のサブスクリプショングループ**：V2では、単一のAPIリクエストで複数のサブスクリプショングループを更新できます。一方、V1ではリクエストごとに1つのサブスクリプショングループしかサポートしていません。
- **1回の呼び出しでメールとSMSの両方を更新**：`external_ids`を使用する場合、同じユーザーに対してメールとSMSの両方のサブスクリプショングループを、単一のAPI呼び出しで更新できます。V1では、メールとSMSのサブスクリプショングループに対して、別々のAPI呼び出しを行う必要があります。
- **メールや電話の識別子を使用する場合**：`external_ids`の代わりに`emails`または`phones`を使用する場合、同じリクエストでメールとSMSのサブスクリプショングループの両方を更新することはできません。別々のAPI呼び出しを行う必要があります。メールサブスクリプショングループ用とSMSサブスクリプショングループ用でそれぞれ別々の呼び出しが必要です。

{% alert important %}
**電話番号の形式**：電話番号は[E.164形式](https://en.wikipedia.org/wiki/E.164)でなければなりません（例：`+12223334444`）。E.164形式に合わない電話番号は拒否されます。
{% endalert %}

{% multi_lang_include api/orphaned_subscription_states.md %}

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string),
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
      "use_double_opt_in_logic": (optional, boolean)
    }
  ]
}
```

{% alert tip %}
[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して新しいユーザーを作成する場合、ユーザー属性オブジェクト内にサブスクリプショングループを設定できます。これにより、1回のAPI呼び出しでユーザーの作成とサブスクリプショングループの状態の設定を同時に行えます。
{% endalert %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | 必須 | 文字列 | サブスクリプショングループの`id`。 |
| `subscription_state` | 必須 | 文字列 | 使用できる値は、`unsubscribed`（サブスクリプショングループに含まれない）または`subscribed`（サブスクリプショングループに含まれる）です。 |
| `external_ids` | 必須* | 文字列の配列 | ユーザーの`external_id`。最大50個の`id`を含めることができます。 |
| `emails` | 必須* | 文字列または文字列の配列 | ユーザーのメールアドレスは、文字列の配列として渡すことができます。少なくとも1件のメールアドレス（最大50件まで）を含める必要があります。<br><br>同じワークスペース内の複数のユーザー（`external_id`）が同じメールアドレスを共有している場合、そのメールアドレスを共有するすべてのユーザーがサブスクリプショングループの変更で更新されます。 |
| `phones` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号は文字列の配列として渡すことができます。少なくとも1つの電話番号を含める必要があります（最大50件）。電話番号はE.164形式でなければなりません（例：`+12223334444`）。<br><br>同じワークスペース内の複数のユーザー（`external_id`）が同じ電話番号を共有している場合、その電話番号を共有しているすべてのユーザーが同じサブスクリプショングループの変更で更新されます。 |
| `use_double_opt_in_logic` | オプション | ブール値 | 省略した場合、デフォルトは`false`です。SMSサブスクリプショングループの場合、`true`に設定すると、サブスクリプションステータスが`subscribed`に設定された際にユーザーが[SMSダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/)ワークフローに登録されます。この方法でダブルオプトインワークフローに登録されたユーザーは、ワークフローに登録された回数に関係なく、1日あたり最大1回のオプトインプロンプト返信メッセージを受信します。このパラメーターが省略されるか`false`に設定された場合、ユーザーはダブルオプトインワークフローに入ることなく購読されます。このパラメーターはメールサブスクリプショングループには適用されません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert important %}
**識別子の選択**：
- メールとSMSのサブスクリプショングループを単一のAPI呼び出しで更新するには、`external_ids`を使用してください。同じリクエストに`emails`と`phones`の両方を含めることはできません。
- `external_ids`の代わりに`emails`や`phones`を使用する場合、API呼び出しを分けて行ってください。メールサブスクリプショングループ用とSMSサブスクリプショングループ用で別々の呼び出しが必要です。
- `emails`、`phones`、`external_ids`はそれぞれ個別に送信できます。
{% endalert %}

### リクエスト例 {#example-requests}

次の例では、`external_ids`を使用して単一のAPI呼び出しでメールとSMSのサブスクリプショングループの両方を更新します。これは`external_ids`を使用する場合にのみ可能です。`emails`または`phones`を使用している場合、1回の呼び出しでメールとSMSのサブスクリプショングループの両方を更新することはできません。

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## メール {#email}

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
```

## SMSとWhatsApp {#sms-and-whatsapp}

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
```

{% endapi %}