---
nav_title: "DELETE: 오브젝트 관계 삭제"
article_title: "DELETE: 오브젝트 관계 삭제"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 오브젝트 관계 삭제 엔드포인트에 대해 자세히 설명합니다."
---
{% api %}
# 오브젝트 관계 삭제 {#delete-object-relationship}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> 이 엔드포인트를 사용하여 하나의 오브젝트 간 관계 엣지를 삭제합니다.

{% alert important %}
커스텀 오브젝트는 현재 얼리 액세스 단계입니다. 커스텀 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `custom_objects.object_relationships.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 커스텀 오브젝트 쓰기 버킷에 포함되며 기본 제한은 분당 50회 요청입니다.

## 경로 매개변수 {#path-parameters}

다음 표는 `/custom_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 경로 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | URL 오브젝트 유형 |
| `external_id` | 필수 | 문자열 | URL 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 삭제 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표는 `/custom_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 JSON 요청 본문 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `rel_kind` | 필수 | 문자열 | 관계 유형 |
| `related_type_name` | 필수 | 문자열 | 관련 오브젝트 유형 |
| `related_external_id` | 필수 | 문자열 | 관련 오브젝트 식별자 |
| `anchor` | 선택 사항 | 문자열 | `source`(기본값) 또는 `target` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 삭제 요청 매개변수" }

{% alert note %}
이 `DELETE` 엔드포인트는 JSON 요청 본문을 필요로 합니다. HTTP 클라이언트가 `DELETE` 호출 시 요청 본문을 전송하는지 확인하세요.
{% endalert %}

## 요청 예시 {#example-request}

이 섹션에는 샘플 JSON 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시는 `acct-123`과 `acct-456` 사이의 `subaccount` 관계를 제거합니다. 두 계정 레코드는 그대로 유지됩니다.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}'
```

## 응답 {#response}

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음 응답 본문을 반환할 수 있습니다.

```json
{ "deleted": true }
```

### 응답 매개변수 {#response-parameters}

다음 표는 성공 응답의 필드를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `deleted` | 필수 | Boolean | 관계 삭제 성공 여부 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 삭제 응답 매개변수" }

## 오류 {#errors}

다음 표는 이 엔드포인트의 일반적인 오류와 해결 방법을 나열합니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 유효성 검사 오류 | 요청 본문에 유효한 `rel_kind`, `related_type_name`, `related_external_id`, `anchor` 값이 포함되어 있는지 확인하세요. |
| `404` | 관계 또는 엔드포인트 오브젝트를 찾을 수 없음 | 두 오브젝트가 모두 존재하고 관계 키 값이 기존 엣지와 일치하는지 확인하세요. |
| `401` | REST API 키가 누락되었거나 유효하지 않음 | `Authorization` 헤더에 `Bearer YOUR_REST_API_KEY`가 사용되고 있는지, 그리고 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `custom_objects.object_relationships.delete` 권한이 있는지, 그리고 허용 목록이 구성되어 있는 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="오브젝트 관계 삭제 오류" }
{% endapi %}