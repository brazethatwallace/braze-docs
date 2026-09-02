---
nav_title: "POST: 데이터 오브젝트 생성"
article_title: "POST: 데이터 오브젝트 생성"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "이 문서에서는 데이터 오브젝트 생성 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 데이터 오브젝트 생성 {#create-data-object}
{% apimethod post %}
/data_objects/objects/{type_name}
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 유형에 대한 데이터 오브젝트 하나를 생성합니다.

{% alert important %}
데이터 오브젝트는 현재 얼리 액세스 단계입니다. 데이터 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `data_objects.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 데이터 오브젝트 쓰기 버킷에 속하며 기본값은 분당 50건의 요청으로 제한됩니다.

## 경로 매개변수 {#path-parameters}

다음 표에는 `/data_objects/objects/{type_name}` 엔드포인트의 경로 매개변수가 나열되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 데이터 오브젝트 유형 머신 이름 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 오브젝트 생성 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표에는 `/data_objects/objects/{type_name}` 엔드포인트의 JSON 요청 본문 매개변수가 나열되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `external_id` | 필수 | 문자열 | 해당 유형 내에서 고유한 오브젝트 식별자 |
| `attributes` | 필수 | 오브젝트 | 유형 스키마에 따라 검증되는 필드 이름-값 쌍 |
| `display_name` | 선택 사항 | 문자열 | 오브젝트의 표시 레이블. 유형에 표시 이름 소스 필드가 있으면 해당 필드 값이 우선 적용됩니다. 기본값은 `external_id`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 오브젝트 생성 요청 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 샘플 JSON 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시는 식별자가 `acct-new`인 `account` 레코드를 생성하고, `name` 및 `industry` 속성을 설정합니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}'
```

## 응답 {#response}

이 섹션에는 성공 응답 예시와 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `201`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### 응답 매개변수 {#response-parameters}

다음 표에는 성공 응답의 필드가 나열되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `data_object` | 필수 | 오브젝트 | 생성된 데이터 오브젝트 레코드 |
| `data_object.type_name` | 필수 | 문자열 | 데이터 오브젝트 유형 머신 이름 |
| `data_object.external_id` | 필수 | 문자열 | 데이터 오브젝트 식별자 |
| `data_object.attributes` | 필수 | 오브젝트 | 필드 이름으로 키가 지정된 저장된 오브젝트 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 오브젝트 생성 응답 매개변수" }

## 오류 {#errors}

다음 표에는 이 엔드포인트의 일반적인 오류와 해결 방법이 나열되어 있습니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 알 수 없는 속성 필드 또는 잘못된 속성 유형 | `attributes`의 모든 필드가 유형 스키마에 존재하며 올바른 데이터 유형을 사용하는지 확인하세요. |
| `404` | 유형을 찾을 수 없음(`data-object-type-not-found`) | `type_name`이 워크스페이스에 존재하며 머신 이름과 정확히 일치하는지 확인하세요. |
| `409` | 중복 오브젝트(`duplicate-data-object`) | 다른 `external_id`를 사용하거나, `PUT`을 사용하여 기존 오브젝트를 교체하세요. |
| `422` | 레코드 제한 도달(`data-object-record-limit-exceeded`) | 해당 유형의 오브젝트 수를 줄이거나, 워크스페이스 제한에 대해 Braze 지원팀에 문의하세요. |
| `401` | REST API 키가 누락되었거나 유효하지 않음 | `Authorization` 헤더가 `Bearer YOUR_REST_API_KEY`를 사용하고 있으며 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 키에 `data_objects.create` 권한이 있는지, 허용 목록이 설정되어 있는 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 다시 시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="데이터 오브젝트 생성 오류" }
{% endapi %}