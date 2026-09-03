---
nav_title: "PUT: 오브젝트 관계 교체"
article_title: "PUT: 오브젝트 관계 교체"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "이 문서에서는 오브젝트 관계 교체 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 오브젝트 관계 교체 {#replace-object-relationship}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> 이 엔드포인트를 사용하여 오브젝트 관계를 생성하거나 교체할 수 있습니다.

{% alert important %}
데이터 오브젝트는 현재 얼리 액세스 단계입니다. 데이터 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.object_relationships.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 오브젝트 쓰기 버킷에 포함되며, 기본값으로 분당 50건의 요청으로 제한됩니다.

## 경로 매개변수 {#path-parameters}

다음 표에서는 `/data_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 경로 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | URL 오브젝트 유형 |
| `external_id` | 필수 | 문자열 | URL 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 교체 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표에서는 `/data_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 JSON 요청 본문 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `rel_kind` | 필수 | 문자열 | 관계 종류 |
| `related_type_name` | 필수 | 문자열 | 관련 오브젝트 유형 |
| `related_external_id` | 필수 | 문자열 | 관련 오브젝트 식별자 |
| `anchor` | 선택 사항 | 문자열 | `source`(기본값) 또는 `target` |
| `attributes` | 선택 사항 | 오브젝트 | 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 교체 요청 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 샘플 JSON 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시에서는 `acct-123`과 `acct-456` 간의 `subaccount` 관계를 교체하여 이전에 저장된 모든 속성을 덮어씁니다.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}'
```

## 응답 {#response}

이 섹션에는 성공적인 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_data_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### 응답 매개변수 {#response-parameters}

다음 표에서는 성공적인 응답의 필드를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `object_relationship` | 필수 | 오브젝트 | 생성 또는 교체된 관계 레코드 |
| `object_relationship.rel_kind` | 필수 | 문자열 | 관계 종류 값 |
| `object_relationship.to_data_object` | 조건부 | 오브젝트 | `anchor=source`인 경우 관련 오브젝트 |
| `object_relationship.from_data_object` | 조건부 | 오브젝트 | `anchor=target`인 경우 관련 오브젝트 |
| `object_relationship.attributes` | 필수 | 오브젝트 | 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 교체 응답 매개변수" }

## 오류 {#errors}

다음 표에서는 이 엔드포인트의 일반적인 오류와 해결 방법을 나열합니다.

| 상태 | 원인 | 해결 방법 |
|---|---|---|
| `400` | 유효성 검사 오류 | `rel_kind`, `anchor`, `attributes`가 관계 유형에 맞는 유효한 값인지 확인하세요. |
| `404` | 관계 또는 엔드포인트 오브젝트를 찾을 수 없음(`data-object-relationship-not-found`) | 두 오브젝트와 관련 유형 이름이 워크스페이스에 존재하는지 확인하세요. |
| `422` | 오브젝트별 관계 제한에 도달함(`data-object-relationship-limit-exceeded`) | 해당 오브젝트의 관계 수를 줄이거나, 워크스페이스 제한에 대해 Braze 지원팀에 문의하세요. |
| `401` | REST API 키가 누락되었거나 유효하지 않음 | `Authorization` 헤더에서 `Bearer YOUR_REST_API_KEY`를 사용하고 있으며 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.object_relationships.update` 권한이 있는지, 허용 목록이 구성된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="오브젝트 관계 교체 오류" }
{% endapi %}