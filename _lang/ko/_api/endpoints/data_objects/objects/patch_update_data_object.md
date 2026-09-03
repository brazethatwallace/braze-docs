---
nav_title: "PATCH: 데이터 객체 업데이트"
article_title: "PATCH: 데이터 객체 업데이트"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 데이터 객체 업데이트 엔드포인트에 대한 세부 사항을 설명합니다."
---
{% api %}
# 데이터 객체 업데이트 {#update-data-object}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 기존 데이터 객체에 속성을 병합할 수 있습니다.

{% alert important %}
데이터 객체는 현재 얼리 액세스 단계에 있습니다. 데이터 객체 API 키 권한이 **설정** > **API 키**에 표시되려면 먼저 워크스페이스가 활성화되어야 합니다.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 객체 쓰기 버킷에 포함되어 있으며, 기본값은 분당 50회 요청으로 제한됩니다.

## 경로 매개변수 {#path-parameters}

다음 표는 `/data_objects/objects/{type_name}/{external_id}` 엔드포인트의 경로 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 데이터 객체 유형 머신 이름 |
| `external_id` | 필수 | 문자열 | 객체 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 객체 업데이트 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표는 `/data_objects/objects/{type_name}/{external_id}` 엔드포인트의 JSON 요청 본문 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `attributes` | 필수 | 객체 | 병합할 최상위 필드 |
| `display_name` | 선택 사항 | 문자열 | 객체의 표시 레이블. 유형에 표시 이름 원본 필드가 있는 경우 해당 필드의 값이 우선합니다. 생략하면 기존 표시 이름이 유지됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 객체 업데이트 요청 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 샘플 JSON 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시는 `acct-123`의 `credits` 속성을 업데이트하고 레코드의 다른 속성은 변경하지 않습니다.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## 응답 {#response}

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음 응답 본문을 반환할 수 있습니다. `attributes` 객체는 병합 결과를 반영합니다.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### 응답 매개변수 {#response-parameters}

다음 표는 성공 응답의 필드를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `data_object` | 필수 | 객체 | 업데이트된 데이터 객체 레코드 |
| `data_object.type_name` | 필수 | 문자열 | 데이터 객체 유형 머신 이름 |
| `data_object.external_id` | 필수 | 문자열 | 데이터 객체 식별자 |
| `data_object.attributes` | 필수 | 객체 | 병합 후 객체 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 객체 업데이트 응답 매개변수" }

## 오류 {#errors}

다음 표는 이 엔드포인트의 일반적인 오류와 해결 방법을 나열합니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 유효성 검사 오류 | `attributes`의 모든 필드가 유형 스키마에 존재하고 올바른 데이터 유형을 사용하는지 확인하세요. |
| `404` | 유형 또는 객체를 찾을 수 없음 | `type_name`과 `external_id`가 모두 워크스페이스에 존재하는지 확인하세요. |
| `401` | REST API 키 누락 또는 유효하지 않음 | `Authorization` 헤더가 `Bearer YOUR_REST_API_KEY`를 사용하고 있으며 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.update` 권한이 있고 허용 목록이 구성된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="데이터 객체 업데이트 오류" }
{% endapi %}