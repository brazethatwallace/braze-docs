---
nav_title: "GET: 오브젝트 관계 유형 목록"
article_title: "GET: 오브젝트 관계 유형 목록"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 오브젝트 관계 유형 목록 엔드포인트에 대해 자세히 설명합니다."
---
{% api %}
# 오브젝트 관계 유형 목록 {#list-object-relationship-types}
{% apimethod get %}
/data_objects/types/{type_name}/object_relationship_types
{% endapimethod %}

> 이 엔드포인트를 사용하면 주어진 앵커 방향에 대해 오브젝트 간 연결에 사용할 수 있는 관계 종류를 나열할 수 있습니다.

{% alert important %}
데이터 오브젝트는 현재 얼리 액세스 단계입니다. 데이터 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.read` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 오브젝트 읽기 버킷에 포함되며 기본 제한은 분당 50회 요청입니다.

## 경로 매개변수 {#path-parameters}

다음 표는 `/data_objects/types/{type_name}/object_relationship_types` 엔드포인트의 경로 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 데이터 오브젝트 유형 머신 이름 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 유형 목록 경로 매개변수" }

## 쿼리 매개변수 {#query-parameters}

다음 표는 `/data_objects/types/{type_name}/object_relationship_types` 엔드포인트의 쿼리 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `anchor` | 선택 사항 | 문자열 | `source`(기본값) 또는 `target` |
| `limit` | 선택 사항 | 정수 | 페이지 크기. 기본값 `100`. `1`에서 `250` 사이로 제한 |
| `offset` | 선택 사항 | 정수 | 오프셋. 기본값 `0`. 음수 값은 `0`으로 처리됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 유형 목록 쿼리 매개변수" }

## 요청 예시 {#example-request}

이 섹션에서는 샘플 매개변수 페이로드와 샘플 cURL 요청을 제공합니다.

### 샘플 요청 페이로드 {#sample-request-payload}

요청 매개변수에 대한 참조로 다음 JSON 오브젝트를 사용합니다.

```json
{
  "type_name": "account",
  "anchor": "source",
  "limit": 10,
  "offset": 0
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시에서는 `account` 유형이 관계의 소스일 때 `account` 유형에 사용 가능한 오브젝트 관계 종류를 나열합니다.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account/object_relationship_types?anchor=source&limit=10&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 응답 {#response}

이 섹션에서는 성공 응답 샘플과 응답 필드를 제공합니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "items": [
    {
      "from_type_name": "account",
      "to_type_name": "account",
      "rel_kind": "subaccount",
      "display_name": "subaccount",
      "related_type_name": "account"
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 10
}
```

`related_type_name`은 선택한 `anchor`에 대한 관계의 반대편 유형입니다.

### 응답 매개변수 {#response-parameters}

다음 표는 성공 응답의 필드를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | 사용 가능한 오브젝트 관계 유형 목록 |
| `items[].from_type_name` | 필수 | 문자열 | 소스 데이터 오브젝트 유형 이름 |
| `items[].to_type_name` | 필수 | 문자열 | 대상 데이터 오브젝트 유형 이름 |
| `items[].rel_kind` | 필수 | 문자열 | 관계 종류 값 |
| `items[].display_name` | 필수 | 문자열 | 관계 종류의 표시 레이블 |
| `items[].related_type_name` | 필수 | 문자열 | 요청된 `anchor`에 대한 반대편 유형 |
| `total_count` | 필수 | 정수 | 일치하는 레코드의 총 수 |
| `has_more` | 필수 | 부울 | 다음 페이지의 결과가 있는지 여부 |
| `next_offset` | 선택 사항 | 정수 | `has_more`가 `true`일 때 다음 페이지의 오프셋 |
| `offset` | 필수 | 정수 | 현재 페이지 오프셋 |
| `limit` | 필수 | 정수 | 요청에 사용된 페이지 크기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="오브젝트 관계 유형 목록 응답 매개변수" }

## 오류 {#errors}

다음 표는 이 엔드포인트에서 발생할 수 있는 일반적인 오류와 해결 방법을 나열합니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 잘못된 `anchor` | `anchor`에 `source` 또는 `target`을 사용하세요. |
| `404` | 유형을 찾을 수 없음(`data-object-type-not-found`) | `type_name`이 워크스페이스에 존재하며 머신 이름과 정확히 일치하는지 확인하세요. |
| `401` | REST API 키가 없거나 유효하지 않음 | `Authorization` 헤더에서 `Bearer YOUR_REST_API_KEY`를 사용하고 있으며 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.read` 권한이 있으며, 구성된 경우 소스 IP가 키 허용 목록에 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="오브젝트 관계 유형 목록 오류" }
{% endapi %}