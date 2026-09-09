---
nav_title: "GET: 無効な電話番号を照会する"
article_title: "GET: 無効な電話番号を照会する"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「無効な電話番号を照会する」Brazeエンドポイントの詳細について説明します。"
---
{% api %}
# 無効な電話番号を照会する {#query-invalid-phone-numbers}
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> このエンドポイントを使用して、一定期間内に「無効」とマークされた電話番号のリストを取得します。詳細については、[無効な電話番号の処理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers)を参照してください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`sms.invalid_phone_numbers` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------|-----------| ----------|----- |
| `start_date` | オプション <br>(注を参照) | YYYY-MM-DD 形式の文字列 | 無効な電話番号を取得する範囲の開始日。`end_date` より前である必要があります。APIではUTC時間の午前0時として扱われます。 |
| `end_date` | オプション <br>(注を参照) | YYYY-MM-DD 形式の文字列 | 無効な電話番号を取得する範囲の終了日。APIではUTC時間の午前0時として扱われます。結果には、UTCのこの暦日の終わりまでに検出された無効な番号が含まれます（その日を含む）。 |
| `limit` | オプション | 整数 | 返される結果の数を制限するオプションフィールドです。デフォルトは100、最大は500です。 |
| `offset` | オプション | 整数 | リスト内の取得開始位置を指定するオプションフィールドです。 |
| `phone_numbers` | オプション <br>(注を参照) | e.164 形式の文字列の配列 | 指定された場合、Brazeは無効であることが判明した電話番号を返します。 |
| `reason` | オプション <br>(注を参照) | 文字列 | 使用可能な値は `provider_error`（プロバイダーがその電話でSMSを受信できないことを示す）、`deactivated`（電話番号が無効化されている）、または `invalid_format`（E.164以外の値など、フォーマット検証に失敗した番号）です。省略した場合、すべての理由が返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert note %}
`start_date` と `end_date`、または `phone_numbers` のいずれかを指定する必要があります。`start_date`、`end_date`、`phone_numbers` の3つすべてを指定した場合、指定された電話番号が優先され、日付範囲は無視されます。
{% endalert %}

日付範囲に `limit` の数を超える無効な電話番号がある場合、複数回のAPI呼び出しが必要になります。呼び出しで返される結果が `limit` を下回るか、ゼロになるまで、その都度 `offset` を増やしてください。

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## レスポンス {#response}
エントリは降順で表示されます。

```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "invalid_format"
    }
  ],
  "message": "success"
}
```
{% endapi %}