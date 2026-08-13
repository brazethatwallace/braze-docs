---
nav_title: "POST:メール購読ステータスの変更"
article_title: "POST:メール購読ステータスの変更"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、ユーザーのメール購読ステータスを変更するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# メール購読ステータスの変更 {#change-email-subscription-status}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/status
{% endapimethod %}

> このエンドポイントを使用して、ユーザーのグローバルなメール購読状態を設定します。

ユーザーは`opted_in`、`unsubscribed`、または`subscribed`（特にオプトインまたはオプトアウトされていない状態）に設定できます。

{% alert note %}
このエンドポイントはユーザーのグローバルなメール購読状態を更新するもので、購読グループのステータスとは異なります。グローバル購読状態はすべてのメールに適用されますが、[購読グループ]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)を使用すると、特定の種類のメールに対してより細かい制御が可能です。ユーザーがグローバルに購読解除されている場合、購読グループのステータスに関係なくメールを受信しません。購読グループのステータスを照会するには、[ユーザーの購読グループステータス一覧エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)を使用してください。
{% endalert %}

Braze内のどのユーザーにもまだ関連付けられていないメールアドレスのメール購読状態を設定できます。その後、そのメールアドレスがユーザーに関連付けられると、アップロードしたメール購読状態が自動的に設定されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`email.status`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `email` | 必須 | 文字列または配列 | 変更するメールアドレスの文字列、または最大50件のメールアドレスの配列。 |
| `subscription_state` | 必須 | 文字列 | "subscribed"、"unsubscribed"、または"opted_in"のいずれか。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## SendGridメールブロックのトラブルシューティング {#troubleshooting-sendgrid-email-blocks}

SendGridが受信者をブロックした場合、このエンドポイントで購読ステータスを更新し、セグメントフィルターでエンゲージメントを確認してください。配信到達性の監視には[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)のソフトバウンスイベントを使用し、再送信前に購読状態を確認してください。

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}