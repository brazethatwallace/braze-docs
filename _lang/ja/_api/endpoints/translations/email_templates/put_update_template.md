---
nav_title: "PUT: メールテンプレートの翻訳を更新"
article_title: "PUT: メールテンプレートの翻訳を更新"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、「メールテンプレートの翻訳を更新」エンドポイントについて詳しく説明します。"
---

{% api %}
# メールテンプレートの翻訳を更新 {#update-translations-for-an-email-template}
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> このエンドポイントを使用して、[メールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates)の翻訳を更新します。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`templates.translations.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター {#path-parameters}

このエンドポイントにはパスパラメーターはありません。

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `template_id` | 必須 | 文字列 | メールテンプレートのID。|
| `locale_id` | 必須 | 文字列 | ロケールのID。|
| `translations_map` | 必須 | 文字列 | メールテンプレートの翻訳のマップ。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子（UUID）と見なされ、GETエンドポイントのレスポンスで確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
    }
}
```

## レスポンス {#response}

このエンドポイントには、`200`、`400`、`404`、`429` の4つのステータスコードレスポンスがあります。

### 成功レスポンスの例 {#example-success-response}

```json
{
    "message": "success"
}
```

### エラーレスポンスの例 {#example-error-response}

ステータスコード `400` は、次のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

```json
{
	"errors": [
		{
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}