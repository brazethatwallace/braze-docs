---
nav_title: "GET: Webhookテンプレートの翻訳を表示"
article_title: "GET: Webhookテンプレートの翻訳を表示"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、Webhookテンプレートの翻訳を表示するエンドポイントについて説明します。"
---

{% api %}
# Webhookテンプレートの翻訳を表示 {#view-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations
{% endapimethod %}

> このエンドポイントを使用して、[Webhookテンプレート]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)の翻訳を表示します。設定されたすべてのロケールを返すことも、ロケールでレスポンスをフィルターすることもできます。翻訳機能の詳細については、[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`templates.translations.get` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `template_id` | 必須 | String | WebhookテンプレートのID。 |
| `locale_id` | オプション | String | 返すロケールのUUID。省略した場合、レスポンスにはWebhookテンプレートに設定されたすべてのロケールが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="クエリパラメーター" }

## リクエスト例 {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

*`TEMPLATE_ID`* をWebhookテンプレートのIDに、*`LOCALE_ID`* を返したいロケールのUUIDに置き換えてください。すべての設定済みロケールを返すには、`locale_id` を省略します。

## レスポンス {#response}

このエンドポイントには、`200`、`400`、`403`、`404`、`429` の5つのステータスコードレスポンスがあります。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、次のレスポンスボディを返す可能性があります。

```json
{
  "translations": [
    {
      "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "¿Te gustaría comprar esto?"
      },
      "locale": {
        "uuid": "c7c12345-de35-1234-5678-abcdefa99a3f",
        "name": "es-MX",
        "country": "MX",
        "language": "es",
        "locale_key": "es-mx"
      }
    },
    {
      "translation_map": {
        "id_0": "你好！",
        "id_1": "你想買這個嗎？"
      },
      "locale": {
        "uuid": "a1b12345-cd35-1234-5678-abcdefa99a3f",
        "name": "zh-HK",
        "country": "HK",
        "language": "zh",
        "locale_key": "zh-hk"
      }
    }
  ]
}
```

### エラーレスポンス例 {#example-error-response}

ステータスコード `400` は、次のレスポンスボディを返す可能性があります。

```json
{
  "message": "Invalid locale ID"
}
```

{% endapi %}