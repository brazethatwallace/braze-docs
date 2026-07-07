---
nav_title: "GET: カスタムイベントをエクスポート"
article_title: "GET: カスタムイベントのエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、カスタムイベントのエクスポートBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# カスタムイベントをエクスポート {#export-custom-events}
{% apimethod get %}
/events
{% endapimethod %}

> このエンドポイントを使用して、アプリ用に記録されたカスタムイベントのリストをエクスポートします。イベントはアルファベット順に並べ替えられ、50件ずつのグループで返されます。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`events.get` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='events' %}

## クエリパラメーター {#query-parameters}

このエンドポイントへの各呼び出しは50件のイベントを返します。50件を超えるイベントについては、以下のレスポンス例に示すように、`Link` ヘッダーを使用して次のページのデータを取得してください。

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | カスタムイベントのページネーションを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="クエリパラメーター" }

## リクエスト例 {#example-requests}

### カーソルなし {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### 致命的なエラーの応答コード {#fatal-export}

リクエストで致命的なエラーが発生した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラー]({{site.baseurl}}/api/errors#fatal-errors)を参照してください。

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)を参照してください。
{% endalert %}

{% endapi %}