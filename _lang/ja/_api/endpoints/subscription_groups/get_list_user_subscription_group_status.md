---
nav_title: "GET: ユーザーの購読グループステータスを一覧表示する"
article_title: "GET: ユーザーの購読グループステータスを一覧表示する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ユーザーの購読グループステータスを一覧表示するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーの購読グループステータスを一覧表示する {#list-users-subscription-group-status}
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> このエンドポイントを使用して、購読グループ内のユーザーの購読ステートを取得します。

これらのグループは、**購読グループ**ページで利用できます。このエンドポイントからのレスポンスには、external IDと、API呼び出しでリクエストされた特定の購読グループに対する購読中、購読解除、または不明のいずれかが含まれます。これは、後続のAPI呼び出しで購読グループステートを更新したり、ホストされたWebページに表示したりするために使用できます。

**メール購読グループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

**SMS購読グループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

**WhatsAppグループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`subscription.status.get` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types?tab=subscription%20group%20ids) | 必須 | 文字列 | 購読グループの`id`。 |
| `external_id` | 必須* | 文字列 | ユーザーの`external_id`（少なくとも1つ、最大50の`external_ids`を含める必要があります）。<br><br>`external_id`と`email`/`phone`の両方が送信された場合、指定された`external_id`のみが結果クエリに適用されます。 |
| `email` | 必須* | 文字列 | ユーザーのメールアドレス。最大50個の文字列の配列として渡すことができます。<br><br>メールアドレスと電話番号の両方を送信した場合（`external_id`なし）、エラーが発生します。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164) 形式の文字列 | ユーザーの電話番号。メールが含まれていない場合は、少なくとも1つの電話番号を含める必要があります（最大50）。<br><br>メールアドレスと電話番号の両方を送信した場合（`external_id`なし）、エラーが発生します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

*ユーザーごとに`external_id`または`email`または`phone`のいずれかが必須です。

- SMSおよびWhatsApp購読グループの場合、`external_id`または`phone`のいずれかが必須です。両方が送信された場合、`external_id`のみがクエリに使用され、電話番号はそのユーザーに適用されます。
- メール購読グループの場合、`external_id`または`email`のいずれかが必須です。両方が送信された場合、`external_id`のみがクエリに使用され、メールアドレスはそのユーザーに適用されます。

## リクエスト例 {#example-request}

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## レスポンス {#response}

すべての成功したレスポンスは、購読グループのステータスとユーザー履歴に応じて、`Subscribed`、`Unsubscribed`、または`Unknown`を返します。

```json
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% alert important %}
このエンドポイントは、ユーザーのグローバルな購読状態とは独立して、購読グループのステータスを返します。ユーザーがグローバルに購読解除された場合、Brazeダッシュボードでは各購読グループから購読解除された状態として表示されます。ただし、このエンドポイントは依然として最後に保存された購読グループのステータス（例: `Subscribed`）を返します。これは、グローバルな購読状態が個々の購読グループを上書きすることなく優先されるためです。<br><br>Brazeは個々の購読グループのステータスを保持します。そのため、ユーザーがグローバルに再購読した場合、各購読グループは以前に保存されたステータスに戻ります。ユーザーの有効な購読状態を判断するには、グローバルな購読ステータスと、このエンドポイントが返す購読グループのステータスの両方を確認してください。
{% endalert %}

{% endapi %}