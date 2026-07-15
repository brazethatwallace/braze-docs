---
nav_title: "GET: アプリのセッションを時間ごとにエクスポートする"
article_title: "GET: アプリのセッションを時間ごとにエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「アプリセッション分析の時間ごとのエクスポート」Brazeエンドポイントの詳細について概説します。"

---
{% api %}
# アプリのセッションを時間ごとにエクスポートする {#export-app-session-by-time}
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> このエンドポイントを使用して、指定された期間にわたるアプリのセッション数の系列を取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`sessions.data_series` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -------- | -------- | --------- | ----------- |
| `length` | 必須 | 整数 | 返されるシリーズに含める `ending_at` までの最大単位数（日または時間）。1以上100以下でなければなりません。 |
| `unit` | オプション | 文字列 | データポイント間の時間の単位。`day` または `hour` を指定でき、デフォルトは `day` です。 |
| `ending_at` | オプション | 日時 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列) | データシリーズが終了する日付。デフォルトはリクエストの時刻です。 |
| `app_id` | オプション | 文字列 | 特定のアプリに分析を限定するために、[APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)ページから取得したアプリAPI識別子。 |
| `segment_id` | オプション | 文字列 | [セグメントAPI識別子]({{site.baseurl}}/api/identifier_types)を参照してください。セッションを返す対象となる、分析が有効なセグメントを示すセグメントID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答 {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)」を参照してください。
{% endalert %}

{% endapi %}