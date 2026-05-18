---
nav_title: "POST: Segmentによるエクスポートのキャンセル"
article_title: "POST: Segmentによるエクスポートのキャンセル"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Segmentによるエクスポートのキャンセル Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# Segmentによるエクスポートのキャンセル {#cancel-exports-by-segment}
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> このエンドポイントを使用して、指定されたSegment IDで進行中のすべてのエクスポートをキャンセルします。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`segments.list` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `segment_id` | 必須 | 文字列 | 進行中のエクスポートをキャンセルするための `segment_id`。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}