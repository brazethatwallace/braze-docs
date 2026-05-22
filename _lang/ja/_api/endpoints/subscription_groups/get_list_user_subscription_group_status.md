---
nav_title: "GET: ユーザーのサブスクリプショングループステータスを一覧表示する"
article_title: "GET: ユーザーのサブスクリプショングループステータスを一覧表示する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ユーザーのサブスクリプショングループステータスを一覧表示するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーのサブスクリプショングループステータスを一覧表示する {#list-users-subscription-group-status}
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> このエンドポイントを使用して、サブスクリプショングループ内のユーザーのサブスクリプションステートを取得します。

これらのグループは、**サブスクリプショングループ**ページで利用できます。このエンドポイントからの応答には、external IDと、API呼び出しで要求された特定のサブスクリプショングループに対する購読中、配信停止、または不明のいずれかが含まれます。これは、後続のAPI呼び出しでサブスクリプショングループステートを更新したり、ホストされたWebページに表示したりするために使用できます。

**メールサブスクリプショングループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

**SMSサブスクリプショングループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

**WhatsAppグループ**の例を確認したり、このエンドポイントをテストしたりする場合:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`subscription.status.get` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | 必須 | 文字列 | サブスクリプショングループの`id`。 |
| `external_id` | 必須* | 文字列 | ユーザーの`external_id`（少なくとも1つ、最大50の`external_ids`を含める必要があります）。<br><br>`external_id`と`email`/`phone`の両方が送信された場合、指定された`external_id`のみが結果クエリに適用されます。 |
| `email` | 必須* | 文字列 | ユーザーのメールアドレス。最大50個の文字列の配列として渡すことができます。<br><br>メールアドレスと電話番号の両方を送信した場合（`external_id`なし）、エラーが発生します。 |
| `phone` | 必須* | [E.164](https://en.wikipedia.org/wiki/E.164) 形式の文字列 | ユーザーの電話番号。メールが含まれていない場合は、少なくとも1つの電話番号を含める必要があります（最大50）。<br><br>メールアドレスと電話番号の両方を送信した場合（`external_id`なし）、エラーが発生します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

*ユーザーごとに`external_id`または`email`または`phone`のいずれかが必要です。

- SMSおよびWhatsAppサブスクリプショングループの場合、`external_id`または`phone`のいずれかが必要です。両方が送信された場合、`external_id`のみがクエリに使用され、電話番号はそのユーザーに適用されます。
- メールサブスクリプショングループの場合、`external_id`または`email`のいずれかが必要です。両方が送信された場合、`external_id`のみがクエリに使用され、メールアドレスはそのユーザーに適用されます。

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
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 応答 {#response}

すべての成功した応答は、サブスクリプショングループのステータスとユーザー履歴に応じて、`Subscribed`、`Unsubscribed`、または`Unknown`を返します。

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
このエンドポイントは、ユーザーのグローバルなサブスクリプション状態とは独立して、サブスクリプショングループのステータスを返します。ユーザーがグローバルに配信停止された場合、Brazeダッシュボードでは各サブスクリプショングループから配信停止された状態として表示されます。ただし、このエンドポイントは依然として最後に保存されたサブスクリプショングループのステータス（例: `Subscribed`）を返します。これは、グローバルなサブスクリプション状態が個々のサブスクリプショングループを上書きすることなく優先されるためです。<br><br>Brazeは個々のサブスクリプショングループのステータスを保持します。そのため、ユーザーがグローバルに再登録した場合、各サブスクリプショングループは以前に保存されたステータスに戻ります。ユーザーの有効なサブスクリプション状態を判断するには、グローバルなサブスクリプションステータスと、このエンドポイントが返すサブスクリプショングループのステータスの両方を確認してください。
{% endalert %}

{% endapi %}