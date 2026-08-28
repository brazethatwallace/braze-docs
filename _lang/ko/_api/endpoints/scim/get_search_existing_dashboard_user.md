---
nav_title: "GET: 이메일로 기존 대시보드 사용자 계정 검색"
article_title: "GET: 이메일로 기존 대시보드 사용자 계정 검색"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 이메일로 기존 대시보드 사용자 계정을 검색하는 Braze 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# 이메일로 기존 대시보드 사용자 계정 검색 {#search-existing-dashboard-user-account-by-email}
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> 이 엔드포인트를 사용하여 필터 쿼리 매개변수에 이메일을 지정하여 기존 대시보드 사용자 계정을 조회할 수 있습니다.

쿼리 매개변수가 URL 인코딩되면 다음과 같이 표시됩니다:

`/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 SCIM 토큰이 필요합니다. 서비스 Origin을 `X-Request-Origin` 헤더로 사용합니다. 자세한 내용은 [자동화된 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning)을 참조하세요.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## 쿼리 매개변수 {#query-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `filter` | 필수 | 문자열 | 이메일로 검색하기 위한 SCIM 필터 표현식입니다. Braze는 `userName eq "user@example.com"` 형식만 지원합니다. 이메일 값은 큰따옴표로 감싸야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="쿼리 매개변수" }

{% alert important %}
Braze는 `eq` 연산자를 사용한 `userName`에 대한 정확한 일치 필터만 지원합니다. 다른 SCIM 필터 필드나 연산자는 `400` 응답을 반환합니다.
{% endalert %}

## 요청 매개변수 {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
`401` 응답을 받는 경우 SCIM 토큰(REST API 키가 아님)을 사용하고 있는지, `X-Request-Origin`이 서비스 Origin과 일치하는지, IP 주소가 SCIM 허용 목록에 있는지 확인하세요. 자세한 내용은 [자동화된 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning)을 참조하세요.
{% endalert %}

## 요청 예시 {#example-request}
```bash
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## 응답 {#response}
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

## 응답 매개변수 {#response-parameters}

| 매개변수 | 데이터 유형 | 설명 |
|---|---|---|
| `schemas` | 문자열 배열 | SCIM 목록 응답 스키마입니다. |
| `totalResults` | 정수 | 일치하는 대시보드 사용자 수입니다(일치하는 항목이 없으면 0). |
| `Resources` | 배열 | 사용자 객체 배열입니다. 각 객체는 [GET: 기존 대시보드 사용자 계정 조회]({{site.baseurl}}/get_see_user_account_information)와 동일한 필드를 사용합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="응답 매개변수" }

### 사용자 객체 필드 {#user-object-fields}

| 매개변수 | 데이터 유형 | 설명 |
|---|---|---|
| `id` | 문자열 | 사용자의 리소스 ID입니다. |
| `userName` | 문자열 | 사용자의 이메일 주소입니다. |
| `name` | 객체 | `givenName`과 `familyName`을 포함합니다. |
| `department` | 문자열 | 설정된 경우 사용자의 부서입니다. |
| `createdAt` | 문자열 | 사용자 계정이 생성된 시점입니다. 설정되지 않은 경우 `N/A`를 반환하며, 그렇지 않으면 `YYYY Mon DD, H:MM AM/PM` 형식으로 표시됩니다. |
| `lastSignInAt` | 문자열 | 사용자가 마지막으로 로그인한 시점입니다. 사용자가 로그인한 적이 없으면 `N/A`를 반환하며, 그렇지 않으면 `YYYY Mon DD, H:MM AM/PM` 형식으로 표시됩니다. |
| `permissions` | 객체 | 회사, 워크스페이스, 팀 및 역할 권한입니다. [권한 객체]({{site.baseurl}}/scim_api_appendix)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용자 객체 필드" }

### 오류 상태 {#error-states}

`filter` 매개변수가 누락되었거나 형식이 잘못된 경우 엔드포인트는 다음을 반환합니다:

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