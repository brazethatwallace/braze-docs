---
nav_title: "取得:日別の新規ユーザーの日次エクスポート"
article_title: "取得:日別の新規ユーザーの日次エクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「新規ユーザーの日次エクスポート」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 日別の新規ユーザーの日次エクスポート {#export-daily-new-users-by-date}
{% apimethod get %}
/kpi/new_users/data_series
{% endapimethod %}

> このエンドポイントを使用して、各日付の新規ユーザーの総数の日次データを取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`kpi.new_users.data_series` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -------- | -------- | --------- | ----------- |
| `length` | 必須 | 整数 | 返されるシリーズに含める `ending_at` までの最大日数。1以上100以下でなければなりません。 |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。デフォルトはリクエストの時刻です。 |
| `app_id` | オプション | 文字列 | [APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/)ページから取得したアプリAPI識別子。除外した場合、ワークスペース内のすべてのアプリの結果が返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/new_users/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 応答 {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "new_users" : (int) the number of daily new users
        },
        ...
    ]
}
```

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}