---
nav_title: "POST: 사용자 관계 생성"
article_title: "POST: 사용자 관계 생성"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 관계 생성 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 사용자 관계 생성 {#create-user-relationship}
{% apimethod post %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> 이 엔드포인트를 사용하여 하나의 Braze 사용자를 하나의 커스텀 오브젝트에 연결할 수 있습니다.

{% alert important %}
커스텀 오브젝트는 현재 얼리 액세스 중입니다. 커스텀 오브젝트 API 키 권한이 **설정** > **API 키**에 표시되려면 워크스페이스가 활성화되어 있어야 합니다.
{% endalert %}

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `custom_objects.user_relationships.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

이 엔드포인트는 커스텀 오브젝트 쓰기 버킷에 속하며 기본 제한은 분당 50건의 요청입니다.

## 경로 매개변수 {#path-parameters}

다음 표에는 `/custom_objects/objects/{type_name}/{external_id}/users` 엔드포인트의 경로 매개변수가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `type_name` | 필수 | 문자열 | 오브젝트 유형 |
| `external_id` | 필수 | 문자열 | 오브젝트 식별자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 생성 경로 매개변수" }

## 요청 매개변수 {#request-parameters}

다음 표에는 `/custom_objects/objects/{type_name}/{external_id}/users` 엔드포인트의 JSON 요청 본문 매개변수가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `braze_id` | 필수 | 문자열 | Braze 사용자 ID |
| `rel_kind` | 필수 | 문자열 | 관계 유형 |
| `attributes` | 선택 사항 | 오브젝트 | 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 생성 요청 매개변수" }

## 요청 예시 {#example-request}

이 섹션에는 샘플 JSON 페이로드와 샘플 cURL 요청이 포함되어 있습니다.

### 샘플 요청 페이로드 {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}
```

### 샘플 cURL 요청 {#sample-curl-request}

이 예시에서는 사용자를 `account_user`로서 `acct-123`에 연결하고, 해당 사용자의 `role`을 `owner`로 기록합니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}'
```

## 응답 {#response}

이 섹션에는 샘플 성공 응답과 응답 필드가 포함되어 있습니다.

### 성공 응답 예시 {#example-success-response}

상태 코드 `201`은 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "owner" }
  }
}
```

### 응답 매개변수 {#response-parameters}

다음 표에는 성공 응답의 필드가 나열 및 설명되어 있습니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `user_relationship` | 필수 | 오브젝트 | 생성된 사용자 관계 레코드 |
| `user_relationship.type_name` | 필수 | 문자열 | 커스텀 오브젝트 유형 머신 이름 |
| `user_relationship.external_id` | 필수 | 문자열 | 커스텀 오브젝트 식별자 |
| `user_relationship.rel_kind` | 필수 | 문자열 | 관계 유형 값 |
| `user_relationship.user` | 필수 | 오브젝트 | 연결된 사용자 오브젝트 |
| `user_relationship.user.braze_id` | 필수 | 문자열 | Braze 사용자 식별자 |
| `user_relationship.attributes` | 필수 | 오브젝트 | 관계 속성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="사용자 관계 생성 응답 매개변수" }

## 오류 {#errors}

다음 표에는 이 엔드포인트의 일반적인 오류와 해결 방법이 나열되어 있습니다.

| 상태 | 원인 | 안내 |
|---|---|---|
| `400` | 해당 유형에 대해 알 수 없는 `rel_kind`이거나 스키마 유효성 검사 오류 | `rel_kind`가 해당 오브젝트 유형에 유효한지, `attributes`가 관계 스키마와 일치하는지 확인하세요. |
| `404` | 유형 또는 오브젝트를 찾을 수 없음 | `type_name`과 `external_id`가 모두 워크스페이스에 존재하는지 확인하세요. |
| `409` | 중복 관계(`duplicate-user-relationship`) | `PUT`을 사용하여 기존 관계를 대체하거나, 다시 생성하기 전에 삭제하세요. |
| `422` | 사용자당 오브젝트 제한 초과(`custom-objects-per-user-limit-exceeded`) 또는 오브젝트당 사용자 제한 초과(`users-per-custom-object-limit-exceeded`) | 해당 사용자 또는 오브젝트의 관계 수를 줄이거나, 워크스페이스 제한에 대해 Braze 지원팀에 문의하세요. |
| `401` | REST API 키가 없거나 유효하지 않음 | `Authorization` 헤더에서 `Bearer YOUR_REST_API_KEY`를 사용하고 있는지, 해당 키가 활성 상태인지 확인하세요. |
| `403` | API 키에 권한이 없거나 허용 목록에 의해 요청이 차단됨 | 해당 키에 `custom_objects.user_relationships.create` 권한이 있는지, 허용 목록이 구성된 경우 소스 IP가 키 허용 목록에 포함되어 있는지 확인하세요. |
| `429` | 사용량 제한 초과 | `X-RateLimit-Reset` 이후에 재시도하고 요청 빈도를 줄이세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용자 관계 생성 오류" }
{% endapi %}