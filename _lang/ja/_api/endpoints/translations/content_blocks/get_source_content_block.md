---
nav_title: "GET: コンテンツブロックの翻訳タグのデフォルトソース値を表示"
article_title: "GET: コンテンツブロックの翻訳タグのデフォルトソース値を表示"
search_tag: Endpoint
page_order: 0

layout: api_page
page_type: reference
description: "この記事では、コンテンツブロックの翻訳ソースエンドポイントについて詳しく説明します。"
---

{% api %}
# コンテンツブロックの翻訳タグのデフォルトソース値を表示 {#view-default-source-values-for-a-content-blocks-translation-tags}
{% apimethod get %}
/content_blocks/translations/source
{% endapimethod %}

> このエンドポイントを使用して、コンテンツブロックの翻訳タグのデフォルト翻訳ソースをすべて表示します。これらは {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %} 内の値です。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`content_blocks.translations.get` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | 必須 | 文字列 | コンテンツブロックのID。 |
| `locale_id` | オプション | 文字列 | レスポンスをフィルタリングするためのロケールUUID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子（UUID）とみなされ、GETエンドポイントのレスポンスで確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations/source?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

このエンドポイントには、`200`、`400`、`404`、`429` の4つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次のレスポンスヘッダーとボディを返す可能性があります。

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Welcome!",
           "id_1": "Thank you for joining our program"
       }
   },
   "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `400` は、次のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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