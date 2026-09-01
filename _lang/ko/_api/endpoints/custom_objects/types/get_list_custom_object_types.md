---
nav_title: "GET: 커스텀 오브젝트 유형 목록"
article_title: "GET: 커스텀 오브젝트 유형 목록"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 커스텀 오브젝트 유형 목록 엔드포인트에 대해 자세히 설명합니다."
---
{% api %}
# 커스텀 오브젝트 유형 목록 {#list-custom-object-types}
{% apimethod get %}
/custom_objects/types
{% endapimethod %}

> 이 엔드포인트를 사용하여 워크스페이스의 커스텀 오브젝트 유형을 나열할 수 있습니다.

{% alert important %}
커스텀 오브젝트는 현재 얼리 액세스 단계입니다. 커스텀 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 먼저 워크스페이스가 활성화되어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `custom_objects.read` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 커스텀 오브젝트 읽기 버킷에 포함되어 있으며, 기본값으로 분당 50건의 요청으로 제한됩니다.

## 쿼리 매개변수 {#query-parameters}

다음 표는 `/custom_objects/types` 엔드포인트의 쿼리 매개변수를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `search_term` | 선택 사항 | 문자열 | 유형 이름에 대한 대소문자 구분 없는 접두사 필터 |
| `limit` | 선택 사항 | 정수 | 페이지 크기. 기본값 `100`. `1`에서 `250` 사이로 제한됩니다 |
| `offset` | 선택 사항 | 정수 | 오프셋. 기본값 `0`. 음수 값은 `0`으로 내림됩니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="커스텀 오브젝트 유형 목록 쿼리 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 쿼리 매개변수 페이로드 샘플과 cURL 요청 샘플이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

이 JSON 오브젝트를 이 요청의 쿼리 매개변수에 대한 참조로 사용하세요.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시는 검색어 `acc`에 일치하는 커스텀 오브젝트 유형을 나열하며, 페이지당 두 개의 결과를 반환합니다.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 응답 {#response}

이 섹션에는 성공 응답 샘플과 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "items": [
    {
      "type_name": "account",
      "metadata": { "display_name_source": "name" }
    },
    {
      "type_name": "contact",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`metadata.display_name_source`는 해당 유형에 표시 이름 필드가 설정되어 있을 때 표시됩니다.

### 응답 매개변수 {#response-parameters}

다음 표는 성공 응답의 필드를 나열하고 설명합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `items` | 필수 | 배열 | 커스텀 오브젝트 유형 레코드 목록 |
| `items[].type_name` | 필수 | 문자열 | 커스텀 오브젝트 유형의 머신 이름 |
| `items[].metadata` | 필수 | 오브젝트 | 유형 메타데이터 오브젝트 |
| `total_count` | 필수 | 정수 | 일치하는 레코드의 총 수 |
| `has_more` | 필수 | 불리언 | 추가 결과 페이지가 있는지 여부 |
| `next_offset` | 선택 사항 | 정수 | `has_more`가 `true`일 때 다음 페이지의 오프셋 |
| `offset` | 필수 | 정수 | 현재 페이지 오프셋 |
| `limit` | 필수 | 정수 | 요청에 사용된 페이지 크기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="커스텀 오브젝트 유형 목록 응답 매개변수" }

## 오류 {#errors}

다음 표는 이 엔드포인트의 일반적인 오류와 해결 방법을 나열합니다.

| 상태 | 원인 | 해결 방법 |
|---|---|---|
| `400` | 잘못된 쿼리 매개변수 유형 또는 값 | `limit`과 `offset`이 정수인지, 모든 매개변수 값이 유효한지 확인하세요. |
| `401` | REST API 키가 누락되었거나 유효하지 않음 | `Authorization` 헤더가 `Bearer YOUR_REST_API_KEY`를 사용하고 있는지, 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `custom_objects.read` 권한이 있는지, 허용 목록이 설정된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="커스텀 오브젝트 유형 목록 오류" }
{% endapi %}