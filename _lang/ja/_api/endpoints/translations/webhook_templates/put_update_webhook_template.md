---
nav_title: "PUT: Webhookテンプレートの翻訳を更新する"
article_title: "PUT: Webhookテンプレートの翻訳を更新する"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、Webhookテンプレートの翻訳を更新するエンドポイントについて詳しく説明します。"
---

{% api %}
# Webhookテンプレートの翻訳を更新する {#update-translations-for-a-webhook-template}
{% apimethod put %}
/templates/webhook/translations
{% endapimethod %}

> このエンドポイントを使用して、[Webhookテンプレート]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)の翻訳を更新します。翻訳機能の詳細については、[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`templates.translations.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター {#path-parameters}

このエンドポイントにはパスパラメーターはありません。

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `template_id` | 必須 | 文字列 | Webhookテンプレートの ID。 |
| `locale_id` | 必須 | 文字列 | 更新するロケールの UUID。ロケールはWebhookテンプレートに設定されている必要があります。 |
| `translation_map` | 必須 | オブジェクト | 更新された翻訳を含むオブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```bash
curl --location --request PUT 'https://rest.iad-03.braze.com/templates/webhook/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
  "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
  "translation_map": {
    "id_0": "¡Hola!",
    "id_1": "¿Te gustaría comprar esto?"
  }
}'
```

## レスポンス {#response}

このエンドポイントには、`200`、`400`、`403`、`404`、`429` の5つのステータスコードレスポンスがあります。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、次の空のレスポンスボディを返します。

```json
{}
```

### エラーレスポンス例 {#example-error-response}

ステータスコード `400` は、次のレスポンスボディを返す可能性があります。

```json
{
  "message": "Locale not found"
}
```

{% endapi %}