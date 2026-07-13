---
nav_title: "DELETE: カタログを削除する"
article_title: "DELETE: カタログの削除"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、「カタログの削除」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログを削除する {#delete-catalog}
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> このエンドポイントを使用して、カタログを削除します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.delete` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="パスパラメーター" }

## リクエスト例 {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 応答 {#response}

このエンドポイントには、`200` と `404` の2つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `404` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング {#troubleshooting}

次の表に、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}