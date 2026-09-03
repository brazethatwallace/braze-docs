---
nav_title: "PATCH: 사용자 관계 업데이트"
article_title: "PATCH: 사용자 관계 업데이트"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 관계 업데이트 엔드포인트에 대한 세부 정보를 설명합니다."
---
{% api %}
# 사용자 관계 업데이트 {#update-user-relationship}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> 이 엔드포인트를 사용하여 기존 사용자 관계에 속성을 병합할 수 있습니다.

{% alert important %}
데이터 오브젝트는 현재 얼리 액세스 단계입니다. 데이터 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.user_relationships.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 오브젝트 쓰기 버킷에 포함되며 기본 제한은 분당 50건의 요청입니다.

## 경로 매개변수 {#path-parameters}

다음 표에서는 `/data_objects/objects/{type_name}/{external_id}/users` 엔드포인트의 경로 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 오브젝트 유형 |
| `external_id` | 필수 | 문자열 | 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 업데이트 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표에서는 `/data_objects/objects/{type_name}/{external_id}/users` 엔드포인트의 JSON 요청 본문 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `braze_id` | 필수 | 문자열 | Braze 사용자 ID |
| `rel_kind` | 필수 | 문자열 | 관계 종류 |
| `attributes` | 선택 사항 | 오브젝트 | 병합할 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 업데이트 요청 매개변수" }

## 요청 예시 {#example-request}

이 섹션에서는 샘플 JSON 페이로드와 샘플 cURL 요청을 제공합니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "billing_admin"
  }
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시에서는 기존 `account_user` 관계의 `role` 속성을 `billing_admin`으로 변경하며, 관계의 다른 속성은 변경되지 않습니다.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "billing_admin"
  }
}'
```

## 응답 {#response}

이 섹션에서는 샘플 성공 응답과 응답 필드를 제공합니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "billing_admin" }
  }
}
```

### 응답 매개변수 {#response-parameters}

다음 표에서는 성공 응답의 필드를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `user_relationship` | 필수 | 오브젝트 | 업데이트된 사용자 관계 레코드 |
| `user_relationship.type_name` | 필수 | 문자열 | 데이터 오브젝트 유형 머신 이름 |
| `user_relationship.external_id` | 필수 | 문자열 | 데이터 오브젝트 식별자 |
| `user_relationship.rel_kind` | 필수 | 문자열 | 관계 종류 값 |
| `user_relationship.user` | 필수 | 오브젝트 | 연결된 사용자 오브젝트 |
| `user_relationship.user.braze_id` | 필수 | 문자열 | Braze 사용자 식별자 |
| `user_relationship.attributes` | 필수 | 오브젝트 | 병합 후 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 업데이트 응답 매개변수" }

## 오류 {#errors}

다음 표에서는 이 엔드포인트의 일반적인 오류와 해결 방법을 나열합니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 유효성 검사 오류 | `rel_kind`가 오브젝트 유형에 유효한지, `attributes`가 관계 스키마와 일치하는지 확인합니다. |
| `404` | 관계를 찾을 수 없음 (`data-object-relationship-not-found`) | 오브젝트, 사용자, 관계 키 값이 모두 존재하는지 확인합니다. |
| `401` | REST API 키 누락 또는 유효하지 않음 | `Authorization` 헤더가 `Bearer YOUR_REST_API_KEY`를 사용하고 해당 키가 활성 상태인지 확인합니다. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.user_relationships.update` 권한이 있는지, 허용 목록이 설정된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인합니다. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 다시 시도하고 요청 빈도를 줄입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용자 관계 업데이트 오류" }
{% endapi %}