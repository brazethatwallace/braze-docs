---
nav_title: "GET: ユーザー設定センターのURLの生成"
article_title: "GET: ユーザー設定センターのURLの生成"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「ユーザー設定センターのURLの生成」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ユーザー設定センターのURLの生成 {#generate-preference-center-url}
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> このエンドポイントを使用して、ユーザー設定センターのURLを生成します。

ユーザー設定センターのURLはユーザーごとにユニークです。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`preference_center.user.get` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='get preference center' %} このレート制限は固定であり、変更できません。

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| 必須 | 文字列 | ユーザー設定センターのID。 |
|`userID`| 必須 | 文字列 | ユーザー ID。 |
{: aria-label="パスパラメーター" }

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `preference_center_api_id`| 必須 | 文字列 | ユーザー設定センターのID。 |
| `external_id`| 必須 | 文字列 | ユーザーのexternal ID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答 {#response}

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
このエンドポイントは、新しいユーザー設定センター（APIまたはドラッグアンドドロップエディターを使用して作成されたユーザー設定センターなど）のURLのみを生成します。
{% endalert %}