---
nav_title: "PUT: キャンペーンの翻訳を更新"
article_title: "PUT: キャンペーンの翻訳を更新"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「キャンペーンの翻訳を更新」エンドポイントの詳細について説明します。"
---

{% api %}
# キャンペーンの翻訳を更新 {#update-translation-in-a-campaign}
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> このエンドポイントを使用して、キャンペーンの複数の翻訳を更新できます。翻訳機能の詳細については、[メッセージ内のロケール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を参照してください。

キャンペーンを起動した後に翻訳を更新したい場合は、まず[メッセージを下書きとして保存]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch)する必要があります。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`campaigns.translations.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## パスパラメーター {#path-parameters}

このエンドポイントにはパスパラメーターはありません。

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | キャンペーンのID。 |
| `message_variation_id` | 必須 | 文字列 | メッセージバリエーションのID。 |
| `locale_id` | 必須 | 文字列 | ロケールのID（UUID）。 |
| `translation_map` | 必須 | オブジェクト | 新しい翻訳を含むオブジェクト。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

{% alert note %}
すべての翻訳IDはユニバーサル一意識別子（UUID）と見なされ、GETエンドポイントの応答で確認できます。
{% endalert %}

## リクエスト例 {#example-request}

```json
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
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