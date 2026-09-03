---
nav_title: "GET: ユーザーの購読グループを一覧表示"
article_title: "GET: ユーザーの購読グループを一覧表示"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ユーザーの購読グループを一覧表示するBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# ユーザーの購読グループを一覧表示 {#list-users-subscription-groups}
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> このエンドポイントを使用して、特定のユーザーの履歴を含む購読グループを一覧表示し、取得します。

**メール購読グループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

**SMS購読グループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

**WhatsAppグループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`subscription.groups.get`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `external_id` | 必須 | 文字列 | ユーザーの`external_id`（少なくとも1つ、最大50の`external_ids`を含める必要があります）。 |
| `email` | 必須* | 文字列 | ユーザーのメールアドレス。文字列の配列として渡すことができます。少なくとも1件のメールアドレス（最大50件）を含める必要があります。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164)形式の文字列 | ユーザーの電話番号。少なくとも1つの電話番号（最大50）を含める必要があります。 |
| `limit` | オプション | 整数 | 返される結果の最大数の制限。デフォルト（および最大）の`limit`は100です。 |
| `offset` | オプション | 整数 | 検索条件に一致する残りのテンプレートを返す前にスキップするテンプレートの数。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert tip %}
同じメールアドレスを共有する複数のユーザー（複数の`external_ids`）がいる場合、すべてのユーザーは別々のユーザーとして返されます（同じメールアドレスや購読グループを持っていても同様です）。
{% endalert %}

## リクエスト例 {#example-request}

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@example.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## レスポンス例 {#example-response}

ユーザーの履歴で購読ステータスが更新された購読グループのみが、成功レスポンスに含まれます。つまり、新しく作成された購読グループは一覧に表示されません。

```json
{
    "users": [
        {
            "email": "test@example.com",
            "phone": "+11112223333",
            "external_id": "external_identifier",
            "subscription_groups": [
                {
                  "id": "ec2fcc919fca",
                  "name": "ActivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "7d7af9dd5556",
                  "name": "ReactivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "a5e84fd16220",
                  "name": "MarketingGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "64d8cad9176c",
                  "name": "TransactionalGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "b2134cd63942",
                  "name": "BankerMarketingGroup",
                  "channel": "sms",
                  "status": "Subscribed"
                }
            ]
        }
    ],
    "total_count": 1,
    "message": "success"
}
```

{% endapi %}