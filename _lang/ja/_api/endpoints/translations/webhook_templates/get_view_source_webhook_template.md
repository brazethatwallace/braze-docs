---
nav_title: "GET: Webhookテンプレートのソース翻訳を表示"
article_title: "GET: Webhookテンプレートのソース翻訳を表示"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、Webhookテンプレートのソース翻訳を表示するエンドポイントについて詳しく説明します。"
---

{% api %}
# Webhookテンプレートのソース翻訳を表示 {#view-source-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations/source
{% endapimethod %}

> このエンドポイントを使用して、[Webhookテンプレート]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)のデフォルトのソース翻訳を表示します。翻訳機能の詳細については、[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`templates.translations.get` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `template_id` | 必須 | 文字列 | WebhookテンプレートのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="クエリパラメーター" }

## リクエスト例 {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

*`TEMPLATE_ID`* をWebhookテンプレートのIDに置き換えてください。

## レスポンス {#response}

このエンドポイントには、`200`、`400`、`403`、`404`、`429` の5つのステータスコードレスポンスがあります。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、次のレスポンスボディを返す可能性があります。

```json
{
  "translations": {
    "translation_map": {
      "id_0": "Hello!",
      "id_1": "Would you like to buy this?"
    }
  }
}
```

### エラーレスポンス例 {#example-error-response}

ステータスコード `400` は、次のレスポンスボディを返す可能性があります。

```json
{
  "message": "This template does not have multi-language setup"
}
```

{% endapi %}