---
nav_title: "GET: 既存のダッシュボードユーザーアカウントの検索"
article_title: "GET: 既存のダッシュボードユーザーアカウントの検索"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、リソースIDによる既存のダッシュボードユーザーアカウントの検索Brazeエンドポイントの詳細について説明します。"
---

{% api %}
# リソースIDで既存のダッシュボードユーザーアカウントを検索する {#look-up-an-existing-dashboard-user-account-by-resource-id}
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> このエンドポイントを使用して、SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account)メソッドによって返されるリソース`id`を指定し、既存のダッシュボードユーザーアカウントを検索します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、SCIMトークンが必要です。`X-Request-Origin`ヘッダーとしてサービスOriginを使用します。詳細については、[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning)を参照してください。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `id` | 必須 | 文字列 | ユーザーのリソースID。このパラメーターは、`POST` `/scim/v2/Users/`または`GET` `/scim/v2/Users?filter=userName eq "user@example.com"`メソッドによって返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="パスパラメーター" }

## リクエストパラメーター {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
`401`レスポンスを受け取った場合は、SCIMトークン（REST APIキーではない）を使用していること、`X-Request-Origin`がサービスOriginと一致していること、およびIPアドレスがSCIM許可リストに含まれていることを確認してください。詳細については、[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning)を参照してください。
{% endalert %}

## リクエスト例 {#example-request}
```bash
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## レスポンス {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@example.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "2024 Nov 11, 4:20 PM",
    "createdAt": "2024 Nov 11, 4:20 PM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7",
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    }
                ]
            }
        ],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "241adcd25789fabcded",
                         "teamName": "Test Team",
                         "teamPermissions": ["admin"]
                    }
                ]
            }
        ]
    }
}
```

## レスポンスパラメーター {#response-parameters}

| パラメーター | データタイプ | 説明 |
|---|---|---|
| `schemas` | 文字列の配列 | SCIMユーザースキーマ。 |
| `id` | 文字列 | ユーザーのリソースID。 |
| `userName` | 文字列 | ユーザーのメールアドレス。 |
| `name` | オブジェクト | `givenName`と`familyName`を含みます。 |
| `department` | 文字列 | ユーザーの部署（設定されている場合）。 |
| `createdAt` | 文字列 | ユーザーアカウントが作成された日時。未設定の場合は`N/A`を返します。それ以外の場合は`YYYY Mon DD, H:MM AM/PM`の形式で返されます。 |
| `lastSignInAt` | 文字列 | ユーザーが最後にサインインした日時。ユーザーがサインインしたことがない場合は`N/A`を返します。それ以外の場合は`YYYY Mon DD, H:MM AM/PM`の形式で返されます。 |
| `permissions` | オブジェクト | ユーザーの会社、ワークスペース、チーム、およびロールの権限。[権限オブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスパラメーター" }

### エラーステート {#error-states}

指定されたリソース`id`に該当するユーザーが存在しない場合、エンドポイントは以下を返します:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 404,
  "detail": "Resource not found"
}
```

{% endapi %}