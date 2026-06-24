---
nav_title: "POST: 사용자 병합"
article_title: "POST: 사용자 병합"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 병합 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 병합 {#merge-users}
{% apimethod post %}
/users/merge
{% endapimethod %}

> 이 엔드포인트를 사용하여 한 사용자를 다른 사용자로 병합할 수 있습니다.

요청당 최대 50개의 병합을 지정할 수 있습니다. 이 엔드포인트는 비동기식입니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.merge` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `merge_updates` | 필수 | 배열 | 오브젝트 배열입니다. 각 오브젝트에는 `identifier_to_merge` 오브젝트와 `identifier_to_keep` 오브젝트가 포함되어야 하며, 각각 `external_id`, `user_alias`, `phone` 또는 `email`로 사용자를 참조해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요청 매개변수" }

### 병합 동작 {#merge-behavior}

아래에 설명된 동작은 Snowflake로 **구동되지 않는** 모든 Braze 기능에 적용됩니다. 사용자 병합은 **메시징 기록** 탭, 세그먼트 확장, 쿼리 빌더 및 Currents에 반영되지 않습니다.

{% alert important %}
엔드포인트는 `merge_updates` 오브젝트가 업데이트되는 순서를 보장하지 않습니다.
{% endalert %}

이 엔드포인트는 대상 사용자에게 해당 필드가 없는 경우 다음 필드를 병합합니다.

- 이름
- 성
- 이메일 주소([암호화]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/)되지 않은 경우)
- 성별
- 생년월일
- 전화번호
- 시간대
- 거주 도시
- 국가
- 언어
- 기기 정보
- 세션 수(두 프로필의 세션 합계)
- 첫 세션 날짜(Braze는 두 날짜 중 더 이른 날짜를 선택합니다)
- 마지막 세션 날짜(Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
- 커스텀 속성(Braze는 대상 프로필의 기존 커스텀 속성을 유지하고 대상 프로필에 존재하지 않는 커스텀 속성을 포함합니다)
- 커스텀 이벤트 및 구매 이벤트 데이터
- "Y일 동안 X회" 세분화를 위한 커스텀 이벤트 및 구매 이벤트 등록정보(X<=50 및 Y<=30)
- 세분화 가능한 커스텀 이벤트 요약
  - 이벤트 수(두 프로필의 합계)
  - 이벤트가 처음 발생한 날짜(Braze는 두 날짜 중 더 이른 날짜를 선택합니다)
  - 이벤트가 마지막으로 발생한 날짜(Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
- 인앱 구매 총액(센트 단위)(두 프로필의 합계)
- 총 구매 횟수(두 프로필의 합계)
- 첫 구매 날짜(Braze는 두 날짜 중 더 이른 날짜를 선택합니다)
- 마지막 구매 날짜(Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
- 앱 요약
- Last_X_at 필드(Braze는 고아 프로필 필드가 더 최근인 경우 필드를 업데이트합니다)
- Campaign 상호작용 데이터(Braze는 가장 최근 날짜 필드를 선택합니다)
- 워크플로우 요약(Braze는 가장 최근 날짜 필드를 선택합니다)
- 메시지 및 메시지 참여 내역
- Braze는 앱이 두 사용자 프로필 모두에 존재하는 경우에만 세션 데이터를 병합합니다.

{% alert note %}
사용자를 병합할 때 `/users/merge` 엔드포인트를 사용하는 것은 [`changeUser()` 메서드](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)를 사용하는 것과 동일한 방식으로 작동합니다.
{% endalert %}

Braze는 병합 시 삭제 표시된 사용자, 테스트 사용자, 글로벌 컨트롤 그룹 사용자의 세 가지 사용자 유형을 다르게 처리합니다. 자세한 내용은 [사용자 병합 동작]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/)을 참조하세요.

#### 커스텀 이벤트 날짜 및 구매 이벤트 날짜 동작 {#custom-event-date-and-purchase-event-date-behavior}

이 병합된 필드는 "Y일 동안 X회 이벤트" 필터를 업데이트합니다. 구매 이벤트의 경우 이러한 필터에는 "Y일 내 구매 횟수" 및 "지난 Y일 동안 지출한 금액"이 포함됩니다.

### 이메일 또는 전화번호로 사용자 병합하기 {#merging-users-by-email-or-phone-number}

식별자로 `email` 또는 `phone`이 지정된 경우, 식별자에 추가 `prioritization` 값을 포함해야 합니다. `prioritization`은 여러 사용자가 발견된 경우 병합할 사용자를 지정하는 정렬된 배열이어야 합니다. 이는 우선순위에서 하나 이상의 사용자가 일치하는 경우 병합이 발생하지 않음을 의미합니다.

배열에 허용되는 값은 다음과 같습니다:

- `identified`
- `unidentified`
- `most_recently_updated`(가장 최근에 업데이트된 사용자에게 우선순위를 부여하는 것을 의미함)
- `least_recently_updated`(가장 오래전에 업데이트된 사용자에게 우선순위를 부여하는 것을 의미함)

우선순위 배열에는 한 번에 다음 옵션 중 하나만 존재할 수 있습니다:

- `identified`는 `external_id`가 있는 사용자에게 우선순위를 지정하는 것을 의미합니다
- `unidentified`는 `external_id`가 없는 사용자에게 우선순위를 지정하는 것을 의미합니다

{% alert important %}
두 프로필 모두 유효하지 않은 전화번호를 가지고 있는 경우, Braze는 이를 병합하지 않습니다. 유효하지 않은 번호는 E.164 형식으로 저장되지 않으며, 병합 작업은 해당 프로필을 결합하지 않습니다. 엔드포인트는 여전히 성공 메시지와 함께 `202 Accepted`를 반환하므로, HTTP 응답은 병합이 건너뛰어졌음을 나타내지 않습니다. 병합하기 전에 하나 또는 두 프로필의 전화번호를 수정하세요.
{% endalert %}

## 요청 예시 {#example-requests}

### 기본 요청 {#basic-request}

요청의 패턴을 보여주기 위한 기본 요청 본문입니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### 식별되지 않은 사용자 병합하기 {#merging-unidentified-user}

다음 요청은 이메일 주소 `john.smith@braze.com`을 가진 가장 최근에 업데이트된 식별되지 않은 사용자를 외부 ID `john`을 가진 사용자로 병합합니다. 이 예시에서 `most_recently_updated`를 사용하면 쿼리가 하나의 식별되지 않은 사용자로 필터링됩니다. 따라서 이 이메일 주소를 가진 식별되지 않은 사용자가 두 명이라면, 외부 ID `john`을 가진 사용자로 병합되는 것은 단 한 명뿐입니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### 식별되지 않은 사용자를 식별된 사용자로 병합하기 {#merging-unidentified-user-into-identified-user}

다음 예시는 이메일 주소 `john.smith@braze.com`을 가진 가장 최근에 업데이트된 식별되지 않은 사용자를 이메일 주소 `john.smith@braze.com`을 가진 가장 최근에 업데이트된 식별된 사용자로 병합합니다.

`most_recently_updated`를 사용하면 쿼리가 한 사용자(`identifier_to_merge`의 경우 식별되지 않은 사용자 하나, `identifier_to_keep`의 경우 식별된 사용자 하나)로 필터링됩니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### most_recently_updated 우선순위를 포함하지 않고 식별되지 않은 사용자 병합하기 {#merging-an-unidentified-user-without-including-the-most_recently_updated-prioritization}

이메일 주소 `john.smith@braze.com`을 가진 식별되지 않은 사용자가 두 명인 경우, 이 예시 요청은 해당 이메일 주소를 가진 식별되지 않은 사용자가 두 명이므로 사용자를 병합하지 않습니다. 이 요청은 이메일 주소 `john.smith@braze.com`을 가진 식별되지 않은 사용자가 단 한 명일 때만 작동합니다.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `202`와 `400` 두 가지입니다.

### 성공 응답 예시 {#example-success-response}

`202` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답 예시 {#example-error-response}

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결](#troubleshooting)을 참조하세요.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## 문제 해결 {#troubleshooting}

### 성공 응답이 반환되었지만 병합된 사용자가 여전히 검색 가능한 경우 {#a-success-response-was-returned-but-the-merged-user-is-still-searchable}

성공 응답은 요청이 수락되었음을 확인하지만, 병합 작업은 프로필 병합과 소스 프로필 제거의 두 단계로 이루어집니다. 이 때문에 성공 응답 후 짧은 시간 동안 `identifier_to_merge` 프로필이 대시보드에서 검색 가능한 상태로 남아 있을 수 있습니다. 이는 예상되는 동작입니다. 몇 분 기다린 후 병합이 완료되었는지 확인하세요.

병합된 사용자가 몇 분 후에도 여전히 존재하는 경우, 요청의 식별자가 올바르고 요청에 사용된 API 키와 동일한 워크스페이스의 사용자에 속하는지 확인하세요.

### 오류 참조 {#error-reference}

다음 표에는 발생할 수 있는 오류 메시지가 나열되어 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `'merge_updates' must be an array of objects` | `merge_updates`가 오브젝트 배열인지 확인하세요. |
| `a single request may not contain more than 50 merge updates` | 한 요청에 병합 업데이트는 최대 50개까지만 지정할 수 있습니다. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | 요청에 포함된 식별자를 확인하세요. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | `merge_updates`에 `identifier_to_merge`와 `identifier_to_keep` 두 개의 오브젝트만 포함되어 있는지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }

{% endapi %}