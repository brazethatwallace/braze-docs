---
nav_title: "GET: 既存のダッシュボードユーザーアカウントをメールで検索"
article_title: "GET: 既存のダッシュボードユーザーアカウントをメールで検索"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、メールによる既存のダッシュボードユーザーアカウントの検索Brazeエンドポイントについて詳しく説明します。"
---

{% api %}
# 既存のダッシュボードユーザーアカウントをメールで検索 {#search-existing-dashboard-user-account-by-email}
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> このエンドポイントを使用して、フィルタークエリパラメーターにメールアドレスを指定し、既存のダッシュボードユーザーアカウントを検索します。

クエリパラメーターがURLエンコードされている場合、次のようになります。

`/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、SCIMトークンが必要です。`X-Request-Origin`ヘッダーとしてサービスOriginを使用します。詳細については、[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning)を参照してください。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## クエリパラメーター {#query-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `filter` | 必須 | 文字列 | メールアドレスで検索するためのSCIMフィルター式。Brazeは `userName eq "user@example.com"` のみをサポートしています。メールの値はダブルクォーテーションで囲む必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="クエリパラメーター" }

{% alert important %}
Brazeは `eq` 演算子を使用した `userName` の完全一致フィルターのみをサポートしています。他のSCIMフィルターフィールドや演算子を使用すると、`400` レスポンスが返されます。
{% endalert %}

## リクエストパラメーター {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
`401` レスポンスを受け取った場合は、SCIMトークン（REST APIキーではなく）を使用していること、`X-Request-Origin` がサービスOriginと一致していること、およびIPアドレスがSCIM許可リストに登録されていることを確認してください。詳細については、[自動ユーザープロビジョニング]({{site.baseurl}}/scim/automated_user_provisioning)を参照してください。
{% endalert %}

## リクエスト例 {#example-request}
```bash
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## レスポンス {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@example.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
            "name": {
                "givenName": "Test",
                "familyName": "User"
            },
            "department": "finance",
            "createdAt": "2024 Nov 11, 4:20 PM",
            "lastSignInAt": "N/A",
            "permissions": {
                "companyPermissions": ["manage_company_settings"],
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
    ]
}
```

## レスポンスパラメーター {#response-parameters}

| パラメーター | データタイプ | 説明 |
|---|---|---|
| `schemas` | 文字列の配列 | SCIMリストレスポンススキーマ。 |
| `totalResults` | 整数 | 一致するダッシュボードユーザーの数（一致しない場合は0）。 |
| `Resources` | 配列 | ユーザーオブジェクトの配列。各オブジェクトは[GET: 既存のダッシュボードユーザーアカウントの検索]({{site.baseurl}}/get_see_user_account_information)と同じフィールドを使用します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスパラメーター" }

### ユーザーオブジェクトフィールド {#user-object-fields}

| パラメーター | データタイプ | 説明 |
|---|---|---|
| `id` | 文字列 | ユーザーのリソースID。 |
| `userName` | 文字列 | ユーザーのメールアドレス。 |
| `name` | オブジェクト | `givenName` と `familyName` を含みます。 |
| `department` | 文字列 | ユーザーの部署（設定されている場合）。 |
| `createdAt` | 文字列 | ユーザーアカウントが作成された日時。未設定の場合は `N/A` を返します。それ以外は `YYYY Mon DD, H:MM AM/PM` の形式です。 |
| `lastSignInAt` | 文字列 | ユーザーが最後にサインインした日時。ユーザーがサインインしたことがない場合は `N/A` を返します。それ以外は `YYYY Mon DD, H:MM AM/PM` の形式です。 |
| `permissions` | オブジェクト | 会社、ワークスペース、チーム、およびロールの権限。[権限オブジェクト]({{site.baseurl}}/scim_api_appendix)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーオブジェクトフィールド" }

### エラーステータス {#error-states}

`filter` パラメーターが欠落しているか不正な形式の場合、エンドポイントは以下を返します。

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 400,
  "detail": "Request is unparsable, syntactically incorrect, or violates schema."
}
```

{% endapi %}