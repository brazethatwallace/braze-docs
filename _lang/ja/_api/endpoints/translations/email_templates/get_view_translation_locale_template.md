---
nav_title: "GET: メールテンプレートの特定の翻訳とロケールを表示する"
article_title: "GET: メールテンプレートの特定の翻訳とロケールを表示する"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、メールテンプレートの特定の翻訳とロケールを表示するエンドポイントについて詳しく説明します。"
---

{% api %}
# メールテンプレートの特定の翻訳とロケールを表示するエンドポイント {#view-a-specific-translation-and-locale-for-email-template-endpoint}
{% apimethod get %}
/templates/translations/email
{% endapimethod %}

> このエンドポイントを使用して、[メールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/)の特定の翻訳とロケールを表示します。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`templates.translations.get` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---------------|----------|-----------|---------------------------------|
| `template_id` | 必須 | 文字列 | メールテンプレートのID。 |
| `locale_id` | オプション | 文字列 | ロケールのID（UUID）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子（UUID）とみなされ、GETエンドポイントの応答で確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

このエンドポイントには、`200`、`400`、`404`、`429` の4つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

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
        }
    ]
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