---
nav_title: "GET: キャンペーンリストをエクスポートする"
article_title: "GET: キャンペーンリストをエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「キャンペーンリストのエクスポート」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# キャンペーンリストをエクスポートする {#export-campaigns-list}
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> このエンドポイントを使用して、キャンペーンのリストをエクスポートします。各キャンペーンには、名前、キャンペーンAPI識別子、APIキャンペーンであるかどうか、およびキャンペーンに関連付けられたタグが含まれます。

キャンペーンは、作成時間順（デフォルトでは古いものから新しいもの）にソートされた100件のグループで返されます。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`campaigns.list` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ----------- |
| `page` | オプション | 整数 | 返すキャンペーンのページ。デフォルトは0です（最大100件の最初のセットを返します）。 |
| `include_archived` | オプション | ブール値 | アーカイブされたキャンペーンを含めるかどうか。デフォルトはfalseです。 |
| `sort_direction` | オプション | 文字列 | - 作成時刻を新しいものから古いものへ並べ替える場合：値`desc`を渡します。<br> - 作成時刻を古いものから新しいものへ並べ替える場合：値`asc`を渡します。<br><br>`sort_direction`が含まれていない場合、デフォルトの順序は古いものから新しいものになります。 |
| `last_edit.time[gt]` | オプション | 時刻 | 結果をフィルターし、指定された時刻以降に編集されたキャンペーンのみを返します。形式は`yyyy-MM-DDTHH:mm:ss`です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## レスポンス {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)」を参照してください。
{% endalert %}

{% endapi %}