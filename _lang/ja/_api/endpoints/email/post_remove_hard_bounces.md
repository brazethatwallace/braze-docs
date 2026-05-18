---
nav_title: "POST:ハードバウンスメールを削除"
article_title: "POST:ハードバウンスメールを削除"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、「ハードバウンスメールアドレスを削除」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ハードバウンスメールを削除 {#remove-hard-bounced-emails}
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> このエンドポイントを使用して、Brazeのバウンスリストとメールプロバイダーが管理するバウンスリストからメールアドレスを削除します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`email.bounce.remove` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストボディ {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------|-----------| ---------|------ |
| `email` | 必須 | 文字列または配列 | 変更するメールアドレスの文字列、または変更する最大50個のメールアドレスの配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}