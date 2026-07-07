---
nav_title: "GET: カスタムイベントリストのエクスポート"
article_title: "GET: カスタムイベントリストのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、カスタムイベントリストのエクスポートBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# カスタムイベントリストのエクスポート {#export-custom-events-list}
{% apimethod get %}
/events/list
{% endapimethod %}

> このエンドポイントを使用して、アプリに記録されたカスタムイベントのリストをエクスポートします。イベント名はアルファベット順にソートされ、250件ずつのグループで返されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`events.list` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='events list' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -------- | -------- | --------- | ----------- |
| `page` | オプション | 整数 | 返されるイベント名のページ。デフォルトは0です（最大250件の最初のセットを返します）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### 致命的なエラーの応答コード {#fatal-export}

リクエストで致命的なエラーが発生した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラーと応答]({{site.baseurl}}/api/errors#fatal-errors)を参照してください。

{% alert tip %}
CSVおよびAPIエクスポートに関するヘルプについては、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)を参照してください。
{% endalert %}

{% endapi %}