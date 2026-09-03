---
nav_title: "PUT: 데이터 오브젝트 교체"
article_title: "PUT: 데이터 오브젝트 교체"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 데이터 오브젝트 교체 엔드포인트에 대해 설명합니다."
---
{% api %}
# 데이터 오브젝트 교체 {#replace-data-object}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 전체 속성 교체 방식으로 데이터 오브젝트를 생성하거나 교체할 수 있습니다.

{% alert important %}
데이터 오브젝트는 현재 얼리 액세스 단계에 있습니다. 데이터 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 오브젝트 쓰기 버킷에 속하며, 기본 제한은 분당 50건의 요청입니다.

## 경로 매개변수 {#path-parameters}

다음 표에는 `/data_objects/objects/{type_name}/{external_id}` 엔드포인트의 경로 매개변수가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 데이터 오브젝트 유형 머신 이름 |
| `external_id` | 필수 | 문자열 | 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 오브젝트 교체 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표에는 `/data_objects/objects/{type_name}/{external_id}` 엔드포인트의 JSON 요청 본문 매개변수가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `attributes` | 필수 | 오브젝트 | 전체 오브젝트 속성. 생략된 필드는 제거됩니다. |
| `display_name` | 선택 사항 | 문자열 | 오브젝트의 표시 레이블. 유형에 표시 이름 소스 필드가 있는 경우 해당 필드의 값이 우선합니다. 기본값은 `external_id`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 오브젝트 교체 요청 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 샘플 JSON 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시는 `acct-123`에 저장된 속성을 페이로드의 속성으로 교체합니다. 해당 식별자를 가진 레코드가 없는 경우 이 요청이 새로 생성합니다.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## 응답 {#response}

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 본문을 반환할 수 있습니다. 이 엔드포인트는 요청이 오브젝트를 생성했는지 교체했는지에 관계없이 `200`을 반환합니다.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### 응답 매개변수 {#response-parameters}

다음 표에는 성공 응답의 필드가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `data_object` | 필수 | 오브젝트 | 생성 또는 교체된 데이터 오브젝트 레코드 |
| `data_object.type_name` | 필수 | 문자열 | 데이터 오브젝트 유형 머신 이름 |
| `data_object.external_id` | 필수 | 문자열 | 데이터 오브젝트 식별자 |
| `data_object.attributes` | 필수 | 오브젝트 | 필드 이름을 키로 하는 저장된 오브젝트 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 오브젝트 교체 응답 매개변수" }

## 오류 {#errors}

다음 표에는 이 엔드포인트의 일반적인 오류와 해결 방법이 나열되어 있습니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 유효성 검사 오류 | `attributes`의 모든 필드가 유형 스키마에 존재하며 올바른 데이터 유형을 사용하는지 확인하세요. |
| `404` | 유형을 찾을 수 없음(`data-object-type-not-found`) | `type_name`이 워크스페이스에 존재하며 머신 이름과 정확히 일치하는지 확인하세요. |
| `422` | 이 요청이 새 오브젝트를 생성하려 할 때 레코드 제한에 도달함(`data-object-record-limit-exceeded`) | 해당 유형의 오브젝트 수를 줄이거나 워크스페이스 제한에 대해 Braze 지원팀에 문의하세요. |
| `401` | REST API 키가 누락되었거나 유효하지 않음 | `Authorization` 헤더에 `Bearer YOUR_REST_API_KEY`가 사용되고 있으며 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.update` 권한이 있고, 허용 목록이 구성된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="데이터 오브젝트 교체 오류" }
{% endapi %}