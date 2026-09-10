---
nav_title: "DELETE: ダッシュボードのユーザーアカウントを削除する"
article_title: "DELETE: ダッシュボードのユーザーアカウントを削除する"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、ダッシュボードのユーザーアカウントを削除するBrazeエンドポイントの詳細について説明します。"
---

{% api %}
# ダッシュボードのユーザーアカウントを削除する {#remove-dashboard-user-account}
{% apimethod delete %}
/scim/v2/Users/{id}
{% endapimethod %}

> このエンドポイントを使用して、SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account)メソッドによって返されるリソース`id`を指定することで、既存のダッシュボードユーザーを完全に削除できます。

これは、Brazeダッシュボードの**会社ユーザー**セクションでユーザーを削除するのと同様です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、SCIMトークンが必要です。`X-Request-Origin`ヘッダーとしてサービスOriginを使用します。詳細については、[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning)を参照してください。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `id` | 必須 | 文字列 | ユーザーのリソースIDです。このパラメーターは、`POST` `/scim/v2/Users/`または`GET` `/scim/v2/Users?filter=userName eq "user@example.com"`メソッドによって返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="パスパラメーター" }

## リクエスト本文 {#request-body}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

## リクエスト例 {#example-request}
```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## レスポンス {#response}

### 成功レスポンス例 {#example-success-response}

ユーザーが完全に削除されると、エンドポイントは以下を返します。

```http
HTTP/1.1 204 No Content
```

### エラーレスポンス例 {#example-error-responses}

このIDを持つ開発者がBrazeに存在しない場合、エンドポイントは次のように応答します。
```http
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
```

最後に残った会社ユーザーを削除しようとすると、エンドポイントは`500 Internal Server Error`レスポンスを返し、ユーザーは削除されません。

```http
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "Failed to delete user",
    "status": 500
}
```

{% endapi %}