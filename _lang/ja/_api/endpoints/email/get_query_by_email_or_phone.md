---
nav_title: "GET: メールアドレスまたは電話番号でサブスクリプションの状態をリストする"
article_title: "GET: メールアドレスまたは電話番号でサブスクリプションの状態をリストする"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "この記事では、メールアドレスまたは電話番号でサブスクリプションの状態をリストするBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# メールアドレスまたは電話番号でサブスクリプションの状態をリストする {#list-subscription-state-with-an-email-address-or-phone-number}
{% apimethod get %}
/users/subscription
{% endapimethod %}

> このエンドポイントを使用して、メールアドレスまたは電話番号に基づくサブスクリプションの状態の値を返します。

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `email` | はい | 文字列 | ユーザーのメールアドレス（最低1件、最大50件のアドレスを含める必要があります）。 |
| `phone` | はい | 文字列 | ユーザーの電話番号（最低1件、最大50件の電話番号を含める必要があります）。E.164形式で指定することをお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 応答 {#response}

エントリは降順で表示されます。

```json
{
  "emails": [
    {
      "email": "example@braze.com",
      "email_subscribe": {
        "email_subscription_event_date": "2019-11-20T19:58:04.825Z",
        "email_subscription_state": "Subscribed"
      },
      "subscription_group": [
        {
          "subscription_group_id": "5f5536d2a76e0f4e323a1234",
          "subscription_group_event_date": "2021-03-11T21:29:22.347Z",
          "subscription_group_state": "Unsubscribed"
        }
      ],
      "hard_bounced_at": null,
      "spam_at": null
    }
  ],
	"phone": [{
		"phone": "+12123355555",
		"subscription_group": [{
			"subscription_group_id": "3f5536d2a76e0f4e323a5555",
			"subscription_group_state": "Subsscribed",
			"subscription_group_event_date": "2021-03-11T21:29:22.347Z"
		}]
	}],
	"message": "success"
}
```

{% endapi %}