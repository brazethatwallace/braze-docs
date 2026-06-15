---
nav_title: "GET: メールテンプレートのソース翻訳を表示"
article_title: "GET: メールテンプレートのソース翻訳を表示"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、メールテンプレートのソース翻訳を表示するエンドポイントについて詳しく説明します。"
---

{% api %}
# メールテンプレートのソース翻訳を表示 {#view-the-source-translations-for-an-email-template}
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> このエンドポイントを使用して、[メールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/)のソース翻訳を表示します。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`templates.email.info` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 必須 | 文字列 | メールテンプレートのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## 応答 {#response}

このエンドポイントには、`200`、`400`、`404`、`429` の4つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `400` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

{% endapi %}