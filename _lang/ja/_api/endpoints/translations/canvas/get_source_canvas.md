---
nav_title: "GET: キャンバスの翻訳タグのデフォルトソース値を表示する"
article_title: "GET: キャンバスの翻訳タグのデフォルトソース値を表示する"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、キャンバスの翻訳ソースエンドポイントについて詳しく説明します。"
---

{% api %}
# キャンバスの翻訳タグのデフォルトソース値を表示する {#view-default-source-values-for-a-canvass-translation-tags}
{% apimethod get %}
/canvas/translations/source
{% endapimethod %}

> このエンドポイントを使用して、キャンバスの翻訳タグに対するすべてのデフォルト翻訳ソースを表示します。これらは {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %} が付いた値です。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`canvas.translations.get` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id` | 必須 | 文字列 | キャンバスのID。 |
| `step_id` | 必須 | 文字列 | キャンバスステップのID。 |
| `message_variation_id` | 必須 | 文字列 | メッセージバリエーションのID。 |
| `locale_id` | オプション | 文字列 | ロケールのID（UUID）。 |
| `post_launch_draft_version` | オプション | ブール値 | `true` の場合、最新の公開済みライブバージョンではなく、最新の下書きバージョンを返します。デフォルトは `false` で、最新のライブバージョンを返します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="クエリパラメーター" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子（UUID）と見なされ、GETエンドポイントの応答で確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

このエンドポイントには、`200`、`400`、`404`、`429` の4つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
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
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}