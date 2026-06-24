---
nav_title: "GET: セグメント分析のエクスポート"
article_title: "GET: セグメント分析のエクスポート"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、セグメント分析のエクスポートBrazeエンドポイントについて詳しく説明します。"

---
{% api %}
# セグメント分析のエクスポート {#export-segment-analytics}
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> このエンドポイントを使用して、セグメントの推定サイズの日次データを時系列で取得します。<br><br>セグメントの正確なサイズが必要な場合は、[`/users/export/segment` エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)でユーザーをエクスポートし、エクスポートされたプロファイル数をカウントしてください。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`segments.data_series` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `segment_id` | 必須 | 文字列 | [セグメントAPI識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。<br><br>特定のセグメントの`segment_id`は、Brazeアカウントの[APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/)ページで確認できます。また、[セグメント一覧エクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)を使用することもできます。 |
| `length` | 必須 | 整数 | 返されるシリーズに含める`ending_at`までの最大日数。1以上100以下（両端を含む）でなければなりません。 |
| `ending_at` | オプション | 日時 <br>（[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 文字列） | データシリーズが終了する日付。デフォルトはリクエスト時刻です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
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
            "size" : (int) the size of the segment on that date
        },
        ...
    ]
}
```

{% alert tip %}
CSVおよびAPIエクスポートに関するヘルプについては、[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)を参照してください。
{% endalert %}

{% endapi %}