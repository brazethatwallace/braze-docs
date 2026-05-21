---
nav_title: "GET: 購入数をエクスポート"
article_title: "GET: 購入数をエクスポート"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、購入数のエクスポートに関するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 購入数をエクスポート {#export-number-of-purchases}
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> このエンドポイントを使用して、指定した期間におけるアプリ内の購入総数を返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`purchases.quantity_series` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `ending_at` | オプション | 日時 ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データエクスポートを終了する日付。デフォルトはリクエストの時刻です。 |
| `length` | 必須 | 整数 | 返されるシリーズに含める `ending_at` までの最大日数。1以上100以下（両端を含む）でなければなりません。 |
| `unit` | オプション | 文字列 | データポイント間の時間の単位。日または時間を指定でき、デフォルトは日です。 |
| `app_id` | オプション | 文字列 | [API Keys]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/)ページから取得したアプリAPI識別子。除外された場合、ワークスペース内のすべてのアプリの結果が返されます。 |
| `product` | オプション | 文字列 | 応答をフィルターする製品の名前。除外された場合、すべてのアプリの結果が返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

```json
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}