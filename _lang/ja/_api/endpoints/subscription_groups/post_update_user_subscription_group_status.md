---
nav_title: "POST: ユーザーの購読グループステータスを更新する"
article_title: "POST: ユーザーの購読グループステータスを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「ユーザーの購読グループステータスの更新」Brazeエンドポイントの詳細について説明します。"
---

{% api %}
# ユーザーの購読グループステータスの更新 {#update-users-subscription-group-status}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> このエンドポイントを使用して、Brazeダッシュボード上で最大50ユーザーの購読状態を一括更新します。

購読グループの`subscription_group_id`にアクセスするには、**購読グループ**ページに移動します。

**メール購読グループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

**SMSとRCS購読グループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`subscription.status.set`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

{% alert note %}
このエンドポイントを[LINE購読グループ]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups)で使用することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% multi_lang_include api/orphaned_subscription_states.md %}

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## リクエスト本文 {#request-body}

{% tabs %}
{% tab SMS and RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   "use_double_opt_in_logic": (optional, boolean) defaults to `false`; when `subscription_state` is "subscribed", set to `true` to enter the user into the SMS double opt-in workflow,
   // SMS and RCS subscription group - you must include one of external_id or phone
 }
```
\* SMSとRCSの購読グループ: Brazeは`external_id`または`phone`のみを受け付けます。

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - you must include one of external_id or email
   // Note that sending an email address that is linked to multiple profiles updates all relevant profiles
 }
```
\* メール購読グループ: `email`または`external_id`のどちらかを含める必要があります。
{% endtab %}
{% endtabs %}

このプロパティは、ユーザーのプロファイル情報の更新には使用しないでください。代わりに[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)プロパティを使用してください。

{% alert tip %}
**既存ユーザーを購読グループに追加する:** このエンドポイントは、既存ユーザーの購読グループメンバーシップをバックフィルまたは一括更新するための推奨方法です。1回のリクエストで最大50件の`external_id`、メールアドレス、または電話番号を渡すことができます。ユーザーは[メールユーザー設定センター]({{site.baseurl}}/user_guide/channels/email/subscriptions)のリンクから、自分の購読ステータスを更新することもできます。

**購読グループ付きで新規ユーザーを作成する:** [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを使用して新規ユーザーを作成する際、ユーザー属性オブジェクト内に購読グループを設定できます。これにより、1回のAPIコールでユーザーの作成と購読グループの状態設定を同時に行えます。
{% endalert %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types?tab=subscription%20group%20ids) | 必須 | 文字列 | 購読グループの`id`。 |
| `subscription_state` | 必須 | 文字列 | 使用できる値は、`unsubscribed`（購読グループに含まれない）または`subscribed`（購読グループに含まれる）です。 |
| `external_id` | 必須* | 文字列の配列 | ユーザーの`external_id`。最大50件の`id`を含めることができます。 |
| `email` | 必須* | 文字列または文字列の配列 | ユーザーのメールアドレス。文字列の配列として渡すことができます。少なくとも1件のメールアドレス（最大50件）を含める必要があります。<br><br>同じワークスペース内の複数のユーザー（`external_id`）が同じメールアドレスを共有している場合、Brazeはそのメールアドレスを共有しているすべてのユーザーの購読グループを更新します。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号。文字列の配列として渡すことができます。少なくとも1件の電話番号（最大50件）を含める必要があります。<br><br>同じワークスペース内の複数のユーザー（`external_id`）が同じ電話番号を共有している場合、Brazeはその電話番号を共有しているすべてのユーザーを同じ購読グループの変更で更新します。 |
| `use_double_opt_in_logic` | オプション | ブール値 | SMS購読グループにのみ適用されます。メールやその他の購読グループタイプでは無視されます。省略した場合のデフォルトは`false`です。SMS購読グループの場合、購読ステータスが`subscribed`に設定されたときにユーザーを[SMSダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)ワークフローに入れるには`true`に設定します。この方法でダブルオプトインワークフローに入ったユーザーは、ワークフローに入った回数に関係なく、1日あたり最大1回のオプトインプロンプト返信メッセージを受信します。このパラメーターが省略されるか`false`に設定された場合、ユーザーはダブルオプトインワークフローを経ずに購読されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-requests}

### メール {#email}

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@example.com", "example2@example.com"]
}
'
```

### SMSとRCS {#sms-and-rcs}

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## 成功応答の例 {#example-success-response}

ステータスコード`201`は、次の応答本文を返す可能性があります。

```json
{
    "message": "success"
}
```

## 断続的な更新失敗のトラブルシューティング {#troubleshooting-intermittent-update-failures}

購読グループの更新が断続的に失敗したり、同期がずれているように見える場合は、更新リクエストの間に数分間待つか、別の更新を送信する前に[`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)を呼び出してユーザーの状態を確認してください。

{% alert important %}
このエンドポイントは`email`または`phone`の値のみを受け付け、両方を同時に受け付けることはできません。両方を指定した場合、次の応答が返されます: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

購読の更新を電話番号に適用するには、E.164形式の電話番号（例: `+15555550123`）を送信し、正しい`subscription_group_id`を使用し、同じリクエスト本文で`phone`のみ（`phone`と`email`の両方ではなく）を渡していることを確認してください。複数番号の更新には、[SMSとRCS](#sms-and-rcs)に示されている`phone`配列形式を使用してください。

{% endapi %}