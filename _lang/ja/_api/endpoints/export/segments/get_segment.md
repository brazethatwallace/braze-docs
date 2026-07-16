---
nav_title: "GET: セグメントリストをエクスポートする"
article_title: "GET: セグメントリストをエクスポートする"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、セグメントリストのエクスポートBrazeエンドポイントについての詳細を説明します。"

---
{% api %}
# セグメントリストをエクスポートする {#export-segment-list}
{% apimethod get %}
/segments/list
{% endapimethod %}

> このエンドポイントを使用して、セグメントのリストをエクスポートします。各セグメントには、名前、セグメントAPI識別子、分析トラッキングが有効かどうかが含まれます。

セグメントは100件ずつのグループで、作成日時順にソートされて返されます（デフォルトでは古いものから新しいものへ）。アーカイブされたセグメントは含まれません。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`segments.list` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -------- | -------- | --------- | ----------- |
| `page` | オプション | 整数 | 返すセグメントのページ。デフォルトは0（最大100件の最初のセットを返します）。 |
| `sort_direction` | オプション | 文字列 | - 作成日時を新しいものから古いものへソートする場合: 値 `desc` を渡します。<br> - 作成日時を古いものから新しいものへソートする場合: 値 `asc` を渡します。<br><br>`sort_direction` が含まれていない場合、デフォルトの順序は古いものから新しいものになります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)」を参照してください。
{% endalert %}

{% endapi %}