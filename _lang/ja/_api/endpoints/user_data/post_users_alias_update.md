---
nav_title: "POST:ユーザーエイリアスを更新する"
article_title: "POST:ユーザーエイリアスを更新する"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、「ユーザーエイリアスの更新」Brazeエンドポイントの詳細について説明します。"
---
{% api %}
# ユーザーエイリアスを更新する {#update-user-alias}
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> このエンドポイントを使用して、既存のユーザーエイリアスを更新します。

リクエストごとに最大50個のユーザーエイリアスを指定できます。

ユーザーエイリアスを更新するには、ユーザーエイリアス更新オブジェクトに `alias_label`、`old_alias_name`、`new_alias_name` を含める必要があります。`alias_label`と`old_alias_name`に関連付けられたユーザーエイリアスがない場合、エイリアスは更新されません。指定された`alias_label`と`old_alias_name`が見つかった場合、`old_alias_name`は`new_alias_name`に更新されます。

{% alert note %}
このエンドポイントは、`alias_updates`オブジェクトの更新順序を保証するものではありません。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.alias.update`権限を持つ[API キー]({{site.baseurl}}/api/api_key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | 必須 | ユーザーエイリアス更新オブジェクトの配列 | [ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)を参照してください。<br><br>`old_alias_name`、`new_alias_name`、`alias_label`の詳細については、[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

### ユーザーエイリアス更新オブジェクト指定のエンドポイントリクエスト本文 {#endpoint-request-body-with-update-user-alias-object-specification}

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}