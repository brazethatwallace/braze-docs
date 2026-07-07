---
nav_title: "GET:日次アプリアンインストールKPIを日付別にエクスポート"
article_title: "GET:日次アプリアンインストールKPIを日付別にエクスポート"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「日付別にアプリの日次アンインストール数をエクスポート」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 日次アプリアンインストールKPIを日付別にエクスポート {#export-kpis-for-daily-app-uninstalls-by-date}
{% apimethod get %}
/kpi/uninstalls/data_series
{% endapimethod %}

> このエンドポイントを使用して、各日付のアンインストールの総数を日次で取得します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`kpi.uninstalls.data_series` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -------- | -------- | --------- | ----------- |
| `length` | 必須 | 整数 | 返されるシリーズに含める `ending_at` までの最大日数。1以上100以下でなければなりません。 |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。デフォルトはリクエストの時刻です。 |
| `app_id` | オプション | 文字列 | [APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)ページから取得したアプリAPI識別子。除外した場合、ワークスペース内のすべてのアプリの結果が返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/uninstalls/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
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
            "uninstalls" : (int) the number of uninstalls
        },
        ...
    ]
}
```

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

{% endapi %}