---
nav_title: "PUT: コンテンツブロック内の翻訳を更新する"
article_title: "PUT: コンテンツブロック内の翻訳を更新する"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、コンテンツブロック内の翻訳を更新するエンドポイントについて詳しく説明します。"
---

{% api %}
# コンテンツブロック内の翻訳を更新する {#update-translation-in-a-content-block}
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> このエンドポイントを使用して、[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)の複数の翻訳を更新します。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`content_blocks.translations.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター {#path-parameters}

このエンドポイントにはパスパラメーターはありません。

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | 必須 | 文字列 | コンテンツブロックのID。 |
| `locale_id`| 必須 | 文字列 | ロケールのID（UUID）。 |
| `translation_map` | 必須 | オブジェクト | 新しい翻訳を含むオブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子（UUID）とみなされ、GETエンドポイントの応答で確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## 応答 {#response}

このエンドポイントには、`200`、`400`、`404`、`429` の4つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

```json
{
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