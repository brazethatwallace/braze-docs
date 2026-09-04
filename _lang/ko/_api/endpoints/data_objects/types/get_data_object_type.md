---
nav_title: "GET: 데이터 객체 유형 가져오기"
article_title: "GET: 데이터 객체 유형 가져오기"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 데이터 객체 유형 가져오기 엔드포인트에 대한 세부 정보를 설명합니다."
---
{% api %}
# 데이터 객체 유형 가져오기 {#get-data-object-type}
{% apimethod get %}
/data_objects/types/{type_name}
{% endapimethod %}

> 이 엔드포인트를 사용하여 하나의 데이터 객체 유형과 해당 스키마 정의를 반환할 수 있습니다.

{% alert important %}
데이터 객체는 현재 얼리 액세스 중입니다. 데이터 객체 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.read` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 객체 읽기 버킷에 속하며, 기본값으로 분당 50건의 요청이 제한됩니다.

## 경로 매개변수 {#path-parameters}

다음 표에는 `/data_objects/types/{type_name}` 엔드포인트의 경로 매개변수가 나열되어 있으며 각 매개변수에 대한 설명이 포함되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 데이터 객체 유형의 머신 이름 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 객체 유형 가져오기 경로 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 샘플 경로 매개변수 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

이 요청의 경로 매개변수에 대한 참조로 다음 JSON 객체를 사용하세요.

```json
{
  "type_name": "account"
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시에서는 `account` 데이터 객체 유형의 정의를 가져옵니다.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## 응답 {#response}

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `200`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "data_object_type": {
    "type_name": "account",
    "metadata": { "display_name_source": "name" },
    "schema_def": {
      "type": "object",
      "properties": {
        "name": { "type": "string", "title": "Name" },
        "industry": { "type": "string", "title": "Industry" },
        "renewal_date": { "type": "string", "format": "date-time", "title": "Renewal date" }
      },
      "required": ["name"]
    }
  }
}
```

`schema_def`는 허용되는 객체 필드를 설명합니다. 이 응답 스키마는 설명용이지만, 쓰기 작업 시에는 선언되지 않은 필드가 여전히 거부됩니다.

### 응답 매개변수 {#response-parameters}

다음 표에는 성공 응답의 필드가 나열되어 있으며 각 필드에 대한 설명이 포함되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `data_object_type` | 필수 | 객체 | 반환된 데이터 객체 유형 레코드 |
| `data_object_type.type_name` | 필수 | 문자열 | 데이터 객체 유형의 머신 이름 |
| `data_object_type.metadata` | 필수 | 객체 | 유형 메타데이터 객체 |
| `data_object_type.schema_def` | 필수 | 객체 | 객체 속성에 대한 JSON 스키마 정의 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 객체 유형 가져오기 응답 매개변수" }

## 오류 {#errors}

다음 표에는 이 엔드포인트의 일반적인 오류와 해결 방법이 나열되어 있습니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `404` | 유형을 찾을 수 없음(`data-object-type-not-found`) | `type_name`이 워크스페이스에 존재하며 머신 이름과 정확히 일치하는지 확인하세요. |
| `401` | REST API 키가 누락되었거나 유효하지 않음 | `Authorization` 헤더가 `Bearer YOUR_REST_API_KEY`를 사용하고 있으며 해당 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 해당 키에 `data_objects.read` 권한이 있는지, 허용 목록이 구성된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="데이터 객체 유형 가져오기 오류" }
{% endapi %}