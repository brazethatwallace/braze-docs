---
nav_title: "GET: 配信停止メールアドレスのリストを照会"
article_title: "GET: 配信停止メールアドレスのリストを照会"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、配信停止メールのリストの取得または照会を行うBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 配信停止メールアドレスのリストを照会 {#query-list-of-unsubscribed-email-addresses}
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> このエンドポイントを使用して、`start_date`から`end_date`までの期間に配信停止された最新のメールを返します。完全なサブスクリプション状態の履歴については、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を使用してこのデータを追跡してください。

このエンドポイントを使用して、Brazeと他のメールシステムまたは独自のデータベースとの間で双方向同期を設定できます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`email.unsubscribe`権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------|-----------| ---------|------ |
| `start_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列 | 配信停止を取得する範囲の開始日。end_dateより前でなければなりません。APIではUTC時間の午前0時として扱われます。 |
| `end_date` | オプション <br>(注を参照) | YYYY-MM-DD形式の文字列 | 配信停止を取得する範囲の終了日。APIではUTC時間の午前0時として扱われます。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するためのオプションフィールドです。デフォルトは100で、最大は500です。 |
| `offset` | オプション | 整数 | 取得を開始するリスト内のオプションの開始点です。 |
| `sort_direction` | オプション | 文字列 | 値`asc`を渡すと、配信停止を古いものから新しいものへ並べ替えます。`desc`を渡すと、新しいものから古いものへ並べ替えます。`sort_direction`が含まれていない場合、デフォルトの順序は新しいものから古いものです。 |
| `email` | オプション <br>(注を参照) | 文字列 | 指定すると、そのユーザーが配信停止しているかどうかを返します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert note %}
`end_date`と、`email`または`start_date`のいずれかを指定する必要があります。
{% endalert %}

日付範囲に`limit`を超える配信停止がある場合、複数のAPI呼び出しを行う必要があります。そのたびに`offset`を増やし、呼び出しが`limit`未満またはゼロの結果を返すまで繰り返します。

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@example.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答 {#response}

エントリは降順で表示されます。

```json
{
  "emails": [
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}