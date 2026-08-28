---
nav_title: "POST: 사용자 삭제"
article_title: "사용자 삭제"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 삭제 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 사용자 삭제 {#delete-users}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/delete
{% endapimethod %}

> 이 엔드포인트를 사용하여 알려진 사용자 식별자를 지정하여 고객 프로필을 삭제할 수 있습니다.

하나의 요청에 최대 50개의 `external_ids`, `user_aliases`, `braze_ids`, `email_addresses` 또는 `phone_numbers`를 포함할 수 있습니다. `external_ids`, `user_aliases`, `braze_ids`, `email_addresses`, `phone_numbers` 중 하나만 하나의 요청에 포함할 수 있습니다.

API를 통한 대량 사용자 삭제로 해결할 수 없는 사용 사례가 있는 경우 [Braze 고객지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하여 도움을 받으세요.

{% alert warning %}
고객 프로필 삭제는 되돌릴 수 없습니다. 삭제 작업은 사용자를 영구적으로 제거하며, 데이터에 불일치가 발생할 수 있습니다. 자세한 내용은 [고객 프로필 삭제의 영향](#effects-of-deleting-user-profiles)을 참조하세요.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.delete` 권한이 있는 [API 키]({{site.baseurl}}/api/basics)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users delete' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_ids" : (optional, array of string) External IDs to be deleted,
  "user_aliases" : (optional, array of user alias objects) User aliases to be deleted,
  "braze_ids" : (optional, array of string) Braze user identifiers to be deleted,
  "email_addresses": (optional, array of string) User emails to be deleted,
  "phone_numbers": (optional, array of string) User phone numbers to be deleted
}
```
### 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|-------------------|----------|----------------------------|--------------------------------------------------------------------------------------------------|
| `external_ids` | 선택 사항 | 문자열 배열 | 삭제할 외부 식별자. |
| `user_aliases` | 선택 사항 | 사용자 별칭 오브젝트 배열 | 삭제할 [사용자 별칭]({{site.baseurl}}/api/objects_filters/user_alias_object). |
| `braze_ids` | 선택 사항 | 문자열 배열 | 삭제할 Braze 사용자 식별자. |
| `email_addresses` | 선택 사항 | 문자열 배열 | 삭제할 사용자 이메일. 자세한 내용은 [이메일로 사용자 삭제하기](#deleting-users-by-email)를 참조하세요. |
| `phone_numbers` | 선택 사항 | 문자열 배열 | 삭제할 사용자 전화번호. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

### 이메일 주소 및 전화번호로 사용자 삭제하기 {#deleting-users-by-email-addresses-and-phone-numbers}

이메일 주소 또는 전화번호를 식별자로 지정하는 경우 식별자에 `prioritization` 값을 추가로 입력해야 합니다. `prioritization`은 정렬된 배열이어야 하며, 여러 사용자가 일치하는 경우 삭제할 사용자를 지정해야 합니다. 즉, 우선순위와 일치하는 사용자가 두 명 이상일 경우 삭제가 수행되지 않습니다.

배열에 허용되는 값은 다음과 같습니다:

- `identified`
- `unidentified`
- `most_recently_updated` (가장 최근에 업데이트된 사용자에게 우선순위를 부여하는 것을 의미함)

`prioritization` 배열에는 한 번에 다음 옵션 중 하나만 존재할 수 있습니다:

- `identified`는 `external_id`가 있는 사용자에게 우선순위를 지정하는 것을 의미합니다.
- `unidentified`는 `external_id`가 없는 사용자에게 우선순위를 지정하는 것을 의미합니다.

## 예시 요청 {#example-request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ],
  "email_addresses": [
    {
      "email": "john.smith@example.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

## 응답 {#response}

```json
{
  "deleted" : (required, integer) number of user IDs queued for deletion
}
```

## 고객 프로필 삭제의 영향 {#effects-of-deleting-user-profiles}

이 엔드포인트로 사용자를 제거하면 다음과 같은 결과가 발생합니다:

- 고객 프로필이 삭제(무효화)됩니다.
- 워크스페이스 사용자 수([분석 홈]({{site.baseurl}}/user_guide/analytics/dashboards/home)의 총 사용자 수 등)가 제거된 사용자를 반영하여 업데이트됩니다.
- 제거된 사용자는 여전히 집계된 전환율에 포함됩니다. 커스텀 이벤트 수와 구매 수는 제거된 사용자에 대해 업데이트되지 않습니다.

### 동일한 이메일 주소를 공유하는 여러 프로필 {#multiple-profiles-with-a-shared-email-address}

동일한 이메일 주소를 공유하는 고객 프로필을 병합하려면 [`/users/merge` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)를 호출하세요.

## 문제 해결 {#troubleshooting}

### 성공 응답이 반환되었지만 사용자가 여전히 표시됩니다 {#a-success-response-was-returned-but-the-user-still-appears}

성공 응답은 요청이 대기줄에 추가되었음을 확인하는 것이지, 삭제가 완료되었음을 의미하지 않습니다. 삭제는 일반적으로 1초 이내에 완료되지만, 모든 캐시에 변경 사항이 전파되기까지 최대 5분이 걸릴 수 있습니다. 삭제 직후 대시보드에서 사용자를 검색하거나 API를 통해 데이터를 내보내면 이 전파 기간 동안 여전히 결과가 표시될 수 있습니다.

몇 분이 지난 후에도 사용자가 여전히 존재하는 경우, 요청의 식별자가 사용자의 실제 프로필과 일치하는지 확인하세요:

- **`external_ids` 배열:** 각 값이 사용자의 외부 ID와 정확히 일치하는지 확인하세요.
- **`braze_id`:** [`/users/export/ids` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)를 사용하여 사용자 데이터를 내보내거나 세그먼트를 CSV로 내보내면(`braze_id`가 "Appboy ID"로 표시됨) 사용자의 `braze_id`를 확인할 수 있습니다.
- **별칭 전용 또는 이메일 전용 프로필:** 프로필에 `external_id`가 없는 경우, **외부 사용자 ID가 비어 있음** 필터와 알려진 이메일 또는 전화번호를 결합하여 세그먼트를 생성한 다음 CSV로 내보내 `braze_id`를 확인하세요.

사용자가 삭제되었는지 확인하려면 삭제 요청에서 사용한 것과 동일한 식별자 유형을 사용하여 [`/users/export/ids` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)를 호출하세요(예: `external_ids`, `braze_id` 또는 `user_aliases`에 값을 포함). 사용자가 더 이상 존재하지 않으면 응답에 `"users": []`가 포함되며, 해당 식별자를 나열하는 `"invalid_user_ids"`가 포함될 수 있습니다.

{% endapi %}