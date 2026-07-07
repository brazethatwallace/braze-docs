---
nav_title: "GET: コンテンツブロックの全翻訳を表示する"
article_title: "GET: コンテンツブロックの全翻訳を表示する"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、コンテンツブロックの全翻訳を表示するエンドポイントについて詳しく説明します。"
---

{% api %}
# コンテンツブロックの全翻訳を表示する {#view-all-translations-for-a-content-block}
{% apimethod get %}
/content_blocks/translations
{% endapimethod %}

> このエンドポイントを使用して、[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)の全翻訳を表示します。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`content_blocks.translations.get` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | 必須 | 文字列 | コンテンツブロックのID。|
| `locale_id` | オプション | 文字列 | 応答をフィルタリングするためのロケールUUID。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="クエリパラメーター" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子（UUID）とみなされ、GETエンドポイントの応答で確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations?content_block_id={content_block_id}&locale_id={locale_uuid}' \
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
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            }
        }
    ]
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `400` は、次の応答本文を返す可能性があります。

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