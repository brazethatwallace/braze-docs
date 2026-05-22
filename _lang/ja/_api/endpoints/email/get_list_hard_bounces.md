---
nav_title: "取得:ハードバウンスメールの照会"
article_title: "取得:ハードバウンスメールの照会"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「ハードバウンスメールアドレスの照会またはリスト」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ハードバウンスメールの照会 {#query-hard-bounced-emails}
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> このエンドポイントを使用して、一定期間内にメールメッセージを「ハードバウンス」したメールアドレスのリストを取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`email.hard_bounces` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------|-----------| ----------|----- |
| `start_date` | オプション* | YYYY-MM-DD 形式の文字列 | *`start_date` または `email` のいずれかが必須です。これはハードバウンスを取得する範囲の開始日であり、`end_date` より前である必要があります。APIによって UTC 時間の午前 0 時として扱われます。 |
| `end_date` | 必須 | YYYY-MM-DD 形式の文字列 | ハードバウンスを取得する範囲の終了日です。APIによって UTC 時間の午前 0 時として扱われます。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するオプションフィールドです。デフォルトは 100、最大は 500 です。 |
| `offset` | オプション | 整数 | リスト内の取得開始位置を指定するオプションです。 |
| `email` | オプション* | 文字列 | *`start_date` または `email` のいずれかが必須です。指定した場合、そのユーザーがハードバウンスしたかどうかを返します。メール文字列が正しくフォーマットされていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
`end_date` と、`email` または `start_date` のいずれかを指定する必要があります。`start_date`、`end_date`、`email` の 3 つすべてを指定した場合、指定されたメールが優先され、日付範囲は無視されます。
{% endalert %}

日付範囲に `limit` の数を超えるハードバウンスがある場合、複数回の API 呼び出しが必要になります。呼び出しで返される結果が `limit` を下回るか、ゼロになるまで、その都度 `offset` を増やしてください。`email` とともに `offset` および `limit` パラメーターを含めると、空の応答が返されることがあります。

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答 {#response}
エントリは降順で表示されます。

```json
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}