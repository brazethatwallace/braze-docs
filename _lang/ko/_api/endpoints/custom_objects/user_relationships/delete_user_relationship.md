---
nav_title: "DELETE: 사용자 관계 삭제"
article_title: "DELETE: 사용자 관계 삭제"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 관계 삭제 엔드포인트에 대해 설명합니다."
---
{% api %}
# 사용자 관계 삭제 {#delete-user-relationship}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> 이 엔드포인트를 사용하여 하나의 사용자-오브젝트 관계를 제거할 수 있습니다.

{% alert important %}
커스텀 오브젝트는 현재 얼리 액세스 중입니다. 커스텀 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `custom_objects.user_relationships.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 커스텀 오브젝트 쓰기 버킷에 포함되며, 기본값으로 분당 50회 요청으로 제한됩니다.

## 경로 매개변수 {#path-parameters}

다음 표에서는 `/custom_objects/objects/{type_name}/{external_id}/users` 엔드포인트의 경로 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 오브젝트 유형 |
| `external_id` | 필수 | 문자열 | 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 삭제 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표에서는 `/custom_objects/objects/{type_name}/{external_id}/users` 엔드포인트의 JSON 요청 본문 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `braze_id` | 필수 | 문자열 | Braze 사용자 ID |
| `rel_kind` | 필수 | 문자열 | 관계 종류 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 삭제 요청 매개변수" }

{% alert note %}
이 `DELETE` 엔드포인트는 JSON 요청 본문을 필요로 합니다. HTTP 클라이언트가 `DELETE` 호출 시 요청 본문을 전송하는지 확인하세요.
{% endalert %}

## 요청 예시 {#example-request}

이 섹션에는 샘플 JSON 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시에서는 지정된 사용자와 `acct-123` 간의 `account_user` 관계를 제거합니다. 고객 프로필과 계정 레코드는 모두 그대로 유지됩니다.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}'
```

## 응답 {#response}

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{ "deleted": true }
```

### 응답 매개변수 {#response-parameters}

다음 표에서는 성공 응답의 필드를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `deleted` | 필수 | 불리언 | 관계 삭제 성공 여부 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 삭제 응답 매개변수" }

## 오류 {#errors}

다음 표에서는 이 엔드포인트의 일반적인 오류와 해결 방법을 나열합니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 유효성 검사 오류 | 요청 본문에 유효한 `braze_id` 및 `rel_kind` 값이 포함되어 있는지 확인하세요. |
| `404` | 관계 또는 오브젝트를 찾을 수 없음 | 오브젝트, 사용자, 관계 키 값이 모두 존재하는지 확인하세요. |
| `401` | REST API 키가 누락되었거나 유효하지 않음 | `Authorization` 헤더에 `Bearer YOUR_REST_API_KEY`가 사용되고 있는지, 해당 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `custom_objects.user_relationships.delete` 권한이 있는지, 허용 목록이 설정된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용자 관계 삭제 오류" }
{% endapi %}