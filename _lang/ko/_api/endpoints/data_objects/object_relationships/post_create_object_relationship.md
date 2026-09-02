---
nav_title: "POST: 오브젝트 관계 생성"
article_title: "POST: 오브젝트 관계 생성"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 오브젝트 관계 생성 엔드포인트에 대해 자세히 설명합니다."
---
{% api %}
# 오브젝트 관계 생성 {#create-object-relationship}
{% apimethod post %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> 이 엔드포인트를 사용하여 두 데이터 오브젝트 간에 단방향 관계 엣지를 생성합니다.

{% alert important %}
데이터 오브젝트는 현재 얼리 액세스 중입니다. 데이터 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.object_relationships.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 오브젝트 쓰기 버킷에 포함되며, 기본값은 분당 50건의 요청으로 제한됩니다.

## 경로 매개변수 {#path-parameters}

다음 표에는 `/data_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 경로 매개변수가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | URL 오브젝트 유형 |
| `external_id` | 필수 | 문자열 | URL 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 생성 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표에는 `/data_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 JSON 요청 본문 매개변수가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `rel_kind` | 필수 | 문자열 | 관계 유형 |
| `related_type_name` | 필수 | 문자열 | 관련 오브젝트 유형 |
| `related_external_id` | 필수 | 문자열 | 관련 오브젝트 식별자 |
| `anchor` | 선택 사항 | 문자열 | `source`(기본값) 또는 `target` |
| `attributes` | 선택 사항 | 오브젝트 | 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 생성 요청 매개변수" }

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

이 예시에서는 `acct-123`을 `subaccount`로 `acct-456`에 연결하며, `acct-123`이 관계의 소스입니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
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

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `201`은 다음과 같은 응답 본문을 반환할 수 있습니다.

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

다음 표에는 성공 응답의 필드가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `object_relationship` | 필수 | 오브젝트 | 생성된 관계 레코드 |
| `object_relationship.rel_kind` | 필수 | 문자열 | 관계 유형 값 |
| `object_relationship.to_data_object` | 조건부 | 오브젝트 | `anchor=source`일 때 관련 오브젝트 |
| `object_relationship.from_data_object` | 조건부 | 오브젝트 | `anchor=target`일 때 관련 오브젝트 |
| `object_relationship.to_data_object.type_name` | 조건부 | 문자열 | 관련 오브젝트 유형 이름 |
| `object_relationship.to_data_object.external_id` | 조건부 | 문자열 | 관련 오브젝트 외부 ID |
| `object_relationship.to_data_object.attributes` | 조건부 | 오브젝트 | 관련 오브젝트 속성 |
| `object_relationship.from_data_object.type_name` | 조건부 | 문자열 | 관련 오브젝트 유형 이름 |
| `object_relationship.from_data_object.external_id` | 조건부 | 문자열 | 관련 오브젝트 외부 ID |
| `object_relationship.from_data_object.attributes` | 조건부 | 오브젝트 | 관련 오브젝트 속성 |
| `object_relationship.attributes` | 필수 | 오브젝트 | 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 생성 응답 매개변수" }

## 오류 {#errors}

다음 표에는 이 엔드포인트에서 발생할 수 있는 일반적인 오류와 해결 방법이 나열되어 있습니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 알 수 없는 `rel_kind`, 유효하지 않은 `anchor`, 관계 유형에 대해 유효하지 않은 관련 유형 또는 스키마 위반 | `rel_kind`가 해당 유형 쌍에 유효한지 확인하고, 유효한 `anchor`를 사용하며, `attributes`가 관계 스키마와 일치하는지 확인합니다. |
| `404` | URL 오브젝트, 관련 오브젝트, URL 유형 또는 관련 유형을 찾을 수 없음 | 두 오브젝트와 두 유형 이름이 모두 워크스페이스에 존재하는지 확인합니다. |
| `409` | 중복 엣지(`duplicate-object-relationship`) | `PUT`을 사용하여 기존 관계를 교체하거나, 다시 생성하기 전에 삭제합니다. |
| `422` | 오브젝트당 관계 제한 도달(`data-object-relationship-limit-exceeded`) | 해당 오브젝트의 관계 수를 줄이거나, 워크스페이스 제한에 대해 Braze 지원팀에 문의합니다. |
| `401` | REST API 키가 없거나 유효하지 않음 | `Authorization` 헤더에 `Bearer YOUR_REST_API_KEY`가 사용되었는지, 키가 활성 상태인지 확인합니다. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.object_relationships.create` 권한이 있는지, 허용 목록이 구성된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인합니다. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="오브젝트 관계 생성 오류" }
{% endapi %}