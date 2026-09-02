---
nav_title: "GET: 오브젝트 관계 목록 조회"
article_title: "GET: 오브젝트 관계 목록 조회"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 오브젝트 관계 목록 조회 엔드포인트에 대한 세부 정보를 설명합니다."
---
{% api %}
# 오브젝트 관계 목록 조회 {#list-object-relationships}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> 이 엔드포인트를 사용하여 하나의 오브젝트 앵커에서 관련 데이터 오브젝트를 조회합니다.

{% alert important %}
데이터 오브젝트는 현재 얼리 액세스 중입니다. 데이터 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.read` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 오브젝트 읽기 버킷에 포함되며, 기본값으로 분당 50건의 요청으로 제한됩니다.

## 경로 매개변수 {#path-parameters}

다음 표에는 `/data_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 경로 매개변수가 나열되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 소스 오브젝트 유형 |
| `external_id` | 필수 | 문자열 | 소스 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 목록 조회 경로 매개변수" }

## 쿼리 매개변수 {#query-parameters}

다음 표에는 `/data_objects/objects/{type_name}/{external_id}/object_relationships` 엔드포인트의 쿼리 매개변수가 나열되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `anchor` | 선택 사항 | 문자열 | `source`(기본값) 또는 `target` |
| `rel_kind` | 선택 사항 | 문자열 | 하나의 관계 종류로 필터링 |
| `limit` | 선택 사항 | 정수 | 페이지 크기. 기본값 `100`. `1`에서 `250` 사이로 제한됩니다 |
| `offset` | 선택 사항 | 정수 | 오프셋. 기본값 `0`. 음수 값은 `0`으로 내림 처리됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 목록 조회 쿼리 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 샘플 매개변수 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

요청 매개변수 참조용으로 이 JSON 오브젝트를 사용하세요.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "anchor": "source",
  "rel_kind": "subaccount",
  "limit": 100,
  "offset": 0
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시에서는 `acct-123`이 연결하는 `subaccount` 레코드를 나열하며, 결과의 첫 페이지를 반환합니다.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 응답 {#response}

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "items": [
    {
      "rel_kind": "subaccount",
      "to_data_object": {
        "type_name": "account",
        "external_id": "acct-456",
        "attributes": { "name": "Child Account" }
      },
      "attributes": {}
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`anchor=target`을 사용하면 관련 오브젝트가 `from_data_object`로 반환됩니다.

### 응답 매개변수 {#response-parameters}

다음 표에는 성공 응답의 필드가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | 오브젝트 관계 레코드 목록 |
| `items[].rel_kind` | 필수 | 문자열 | 관계 종류 값 |
| `items[].to_data_object` | 조건부 | 오브젝트 | `anchor=source`일 때의 관련 오브젝트 |
| `items[].from_data_object` | 조건부 | 오브젝트 | `anchor=target`일 때의 관련 오브젝트 |
| `items[].to_data_object.type_name` | 조건부 | 문자열 | 관련 오브젝트 유형 이름 |
| `items[].to_data_object.external_id` | 조건부 | 문자열 | 관련 오브젝트 외부 ID |
| `items[].to_data_object.attributes` | 조건부 | 오브젝트 | 관련 오브젝트 속성 |
| `items[].from_data_object.type_name` | 조건부 | 문자열 | 관련 오브젝트 유형 이름 |
| `items[].from_data_object.external_id` | 조건부 | 문자열 | 관련 오브젝트 외부 ID |
| `items[].from_data_object.attributes` | 조건부 | 오브젝트 | 관련 오브젝트 속성 |
| `items[].attributes` | 필수 | 오브젝트 | 관계 속성 |
| `total_count` | 필수 | 정수 | 일치하는 레코드의 총 개수 |
| `has_more` | 필수 | 불리언 | 추가 결과 페이지가 있는지 여부 |
| `next_offset` | 선택 사항 | 정수 | `has_more`가 `true`일 때 다음 페이지의 오프셋 |
| `offset` | 필수 | 정수 | 현재 페이지 오프셋 |
| `limit` | 필수 | 정수 | 요청에 사용된 페이지 크기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 목록 조회 응답 매개변수" }

## 오류 {#errors}

다음 표에는 이 엔드포인트의 일반적인 오류와 해결 방법이 나열되어 있습니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 잘못된 `anchor` | `anchor`에 `source` 또는 `target`을 사용하세요. |
| `404` | 유형 또는 오브젝트를 찾을 수 없음 | `type_name`과 `external_id`가 워크스페이스에 존재하는지 확인하세요. |
| `401` | REST API 키 누락 또는 유효하지 않음 | `Authorization` 헤더에 `Bearer YOUR_REST_API_KEY`를 사용하고 있는지, 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.read` 권한이 있는지, 허용 목록이 설정된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="오브젝트 관계 목록 조회 오류" }
{% endapi %}