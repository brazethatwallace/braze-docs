---
nav_title: "GET: カスタム属性をエクスポートする"
article_title: "GET: カスタム属性をエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Brazeのカスタム属性エクスポートエンドポイントの詳細について説明します。"

---
{% api %}
# カスタム属性をエクスポートする {#export-custom-attributes}
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> このエンドポイントを使用して、アプリに記録されたカスタム属性のリストをエクスポートできます。属性は50件ずつのグループに分けられ、アルファベット順にソートされて返されます。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_attributes.get` 権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## クエリパラメーター {#query-parameters}

このエンドポイントへの各コールでは50件の属性が返されます。50件を超える属性については、次のレスポンス例に示すように、`Link` ヘッダーを使用して次のページのデータを取得します。

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | カスタム属性のページネーションを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="クエリパラメーター" }

## リクエスト例 {#example-requests}

### カーソルなし {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
        },
        ...
    ]
}
```

### 致命的なエラーの応答コード {#fatal-export}

リクエストで致命的なエラーが発生した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラー]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

{% alert tip %}
CSVおよびAPIのエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}