---
nav_title: "GET: 워크스페이스 앱 목록"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "이 문서에서는 워크스페이스 앱 목록 Braze 엔드포인트에 대한 세부 정보를 설명합니다."
---
{% api %}
# 워크스페이스 앱 목록 {#list-workspace-apps}
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> 이 엔드포인트를 사용하여 워크스페이스에 있는 앱의 이름과 고유 식별자(`api_key`)를 나열할 수 있습니다.

이 엔드포인트를 호출하면 `apps`라는 오브젝트 배열이 반환됩니다. `apps`의 각 오브젝트에는 앱의 이름과 고유 식별자가 포함되어 있습니다.

{% apiref postman %}  {% endapiref %}

## 사용량 제한 {#rate-limit}

이 엔드포인트는 하루(24시간)에 100건의 요청으로 사용량이 제한됩니다.

## 요청 매개변수 {#request-parameters}

이 요청에는 매개변수가 필요하지 않습니다.

## 요청 예시 {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답 {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### 문제 해결 {#troubleshooting}

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나열되어 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `401: Unauthorized` | API 키에 필요한 권한이 없습니다. API 키에 `apps.get` 권한이 있는지 확인하세요. |
| `403: Forbidden` | 이 회사에 대해 기능 플리퍼가 활성화되어 있지 않습니다. 고객 성공 매니저에게 문의하여 도움을 받으세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}