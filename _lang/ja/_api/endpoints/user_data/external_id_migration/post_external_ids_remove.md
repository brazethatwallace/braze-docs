---
nav_title: "POST:外部IDを削除する"
article_title: "POST:外部IDを削除する"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、外部IDの削除エンドポイントについて詳しく説明します。"
---
{% api %}
# 外部IDを削除する {#remove-external-id}
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> このエンドポイントを使用して、ユーザーの古い非推奨のexternal IDを削除します。

1回のリクエストで送信できるexternal IDは最大50個です。

{% alert warning %}
このエンドポイントは非推奨IDを完全に削除し、元に戻すことはできません。このエンドポイントを使用して、システム内でまだユーザーに関連付けられている非推奨の`external_ids`を削除すると、それらのユーザーのデータを永久に見つけることができなくなる可能性があります。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.external_ids.remove`権限を持つ[APIキー]({{site.baseurl}}/api/basics)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `external_ids` | 必須 | 文字列の配列 | 削除するユーザーの外部識別子。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#request-example}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```

{% alert important %}
削除できるのは非推奨IDのみです。プライマリexternal IDを削除しようとするとエラーになります。
{% endalert %}

## レスポンス {#response}

レスポンスでは、成功したすべての削除と、関連するエラーを伴う失敗した削除が確認されます。`removal_errors`フィールドのエラーメッセージは、元のリクエストの配列内のインデックスを参照します。

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

`message`フィールドは、有効なリクエストに対して`success`を返します。より具体的なエラーは`removal_errors`配列に格納されます。`message`フィールドは、以下の場合にエラーを返します：
- 無効なAPIキー
- 空の`external_ids`配列
- 50を超える項目を持つ`external_ids`配列
- レート制限超過（1,000リクエスト/分超）

{% endapi %}