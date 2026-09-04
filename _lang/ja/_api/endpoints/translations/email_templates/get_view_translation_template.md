---
nav_title: "GET: メールテンプレートのすべての翻訳とロケールを表示"
article_title: "GET: メールテンプレートのすべての翻訳とロケールを表示"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートのすべての翻訳とロケールを表示」エンドポイントについて詳しく説明します。"
---

{% api %}
# メールテンプレートのすべての翻訳とロケールを表示 {#view-all-translations-and-locales-for-an-email-template}
{% apimethod get %}
/templates/email/translations/
{% endapimethod %}

> このエンドポイントを使用して、[メールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates)のすべての翻訳とロケールを表示します。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`templates.translations.get` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 必須 | 文字列 | メールテンプレートのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="クエリパラメーター" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子 (UUID) と見なされ、GETエンドポイントのレスポンスで確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
--- template_id: "6ad1507f-ca10-44c4-95bf-6e4gay901kc5"
```

## レスポンス {#response}

このエンドポイントには、`200`、`400`、`404`、`429` の4つのステータスコードレスポンスがあります。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、次のレスポンスヘッダーと本文を返す可能性があります。

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        },
        {
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            },
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            }
        }
    ]
}
```

### エラーレスポンスの例 {#example-error-response}

ステータスコード `400` は、次のレスポンス本文を返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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