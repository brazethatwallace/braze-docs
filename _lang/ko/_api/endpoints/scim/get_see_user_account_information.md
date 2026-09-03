---
nav_title: "GET: 기존 대시보드 사용자 계정 조회"
article_title: "GET: 기존 대시보드 사용자 계정 조회"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 기존 대시보드 사용자 계정 리소스 ID 조회 Braze 엔드포인트에 대해 자세히 설명합니다."
---

{% api %}
# 리소스 ID로 기존 대시보드 사용자 계정 조회하기 {#look-up-an-existing-dashboard-user-account-by-resource-id}
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account) 메서드에서 반환된 리소스 `id`를 지정하여 기존 대시보드 사용자 계정을 조회할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 SCIM 토큰이 필요합니다. 서비스 Origin을 `X-Request-Origin` 헤더로 사용합니다. 자세한 내용은 [자동화된 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning)을 참조하세요.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## 경로 매개변수 {#path-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `id` | 필수 | 문자열 | 사용자의 리소스 ID입니다. 이 매개변수는 `POST` `/scim/v2/Users/` 또는 `GET` `/scim/v2/Users?filter=userName eq "user@example.com"` 메서드에서 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="경로 매개변수" }

## 요청 매개변수 {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
`401` 응답을 받은 경우, SCIM 토큰(REST API 키가 아님)을 사용하고 있는지, `X-Request-Origin`이 서비스 Origin과 일치하는지, IP 주소가 SCIM 허용 목록에 있는지 확인하세요. 자세한 내용은 [자동화된 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning)을 참조하세요.
{% endalert %}

## 요청 예시 {#example-request}
```bash
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## 응답 {#response}
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

## 응답 매개변수 {#response-parameters}

| 매개변수 | 데이터 유형 | 설명 |
|---|---|---|
| `schemas` | 문자열 배열 | SCIM 사용자 스키마입니다. |
| `id` | 문자열 | 사용자의 리소스 ID입니다. |
| `userName` | 문자열 | 사용자의 이메일 주소입니다. |
| `name` | 객체 | `givenName`과 `familyName`을 포함합니다. |
| `department` | 문자열 | 설정된 경우 사용자의 부서입니다. |
| `createdAt` | 문자열 | 사용자 계정이 생성된 시점입니다. 설정되지 않은 경우 `N/A`를 반환하며, 그렇지 않으면 `YYYY Mon DD, H:MM AM/PM` 형식으로 표시됩니다. |
| `lastSignInAt` | 문자열 | 사용자가 마지막으로 로그인한 시점입니다. 사용자가 로그인한 적이 없으면 `N/A`를 반환하며, 그렇지 않으면 `YYYY Mon DD, H:MM AM/PM` 형식으로 표시됩니다. |
| `permissions` | 객체 | 사용자의 회사, 워크스페이스, 팀 및 역할 권한입니다. [권한 객체]({{site.baseurl}}/api/objects_filters/scim_api_appendix)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="응답 매개변수" }

### 오류 상태 {#error-states}

제공된 리소스 `id`에 해당하는 사용자가 없는 경우 엔드포인트는 다음을 반환합니다:

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