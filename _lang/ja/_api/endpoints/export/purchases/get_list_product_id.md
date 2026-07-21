---
nav_title: "GET: 製品IDをエクスポートする"
article_title: "GET: 製品IDをエクスポートする"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「製品IDをエクスポートする」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 製品IDをエクスポートする {#export-product-ids}
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> このエンドポイントを使用して、製品IDのページ分割されたリストを返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`purchases.product_list` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `page` | オプション | 文字列 | 表示したい製品リストのページ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## レスポンス {#response}

```json
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)」を参照してください。
{% endalert %}