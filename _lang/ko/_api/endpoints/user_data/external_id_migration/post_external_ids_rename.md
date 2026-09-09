---
nav_title: "POST: 외부 ID 이름 바꾸기"
article_title: "POST: 외부 ID 이름 바꾸기"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 외부 ID 이름 바꾸기 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 외부 ID 이름 바꾸기 {#rename-external-id}
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자의 외부 ID 이름을 변경할 수 있습니다.

요청당 최대 50개의 이름 바꾸기 오브젝트를 보낼 수 있습니다.

이 엔드포인트는 사용자에 대해 새(기본) `external_id`를 설정하고 기존 `external_id`를 더 이상 사용하지 않도록 설정합니다. 즉, 더 이상 사용되지 않는 ID가 제거될 때까지 두 `external_id` 중 하나로 사용자를 식별할 수 있습니다. 여러 개의 외부 ID를 사용하면 이전 외부 ID 명명 스키마를 사용하는 앱의 레거시 버전이 중단되지 않도록 마이그레이션 기간을 가질 수 있습니다. 마이그레이션 기간 동안 프로필은 두 식별자 모두에서 완전히 작동합니다. Braze SDK, REST API, 메시징 파이프라인은 더 이상 사용되지 않는 ID가 명시적으로 제거될 때까지 두 ID 중 하나로 사용자를 계속 참조할 수 있습니다.

이전 명명 스키마를 더 이상 사용하지 않는 경우 [`/users/external_ids/remove` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)를 사용하여 더 이상 사용되지 않는 외부 ID를 제거하는 것을 적극 권장합니다.

{% alert warning %}
더 이상 사용되지 않는 외부 ID는 `/users/delete`가 아닌 `/users/external_ids/remove` 엔드포인트를 사용하여 제거해야 합니다. 더 이상 사용되지 않는 외부 ID로 `/users/delete`에 요청을 보내면 고객 프로필이 완전히 삭제되며 되돌릴 수 없습니다.
{% endalert %}

## 이름 바꾸기 작동 방식 {#how-renaming-works}

이 엔드포인트를 호출하면 사용자 프로필에 새 기본 `external_id`를 할당하는 동시에 이전 기본 `external_id`를 더 이상 사용되지 않는 외부 ID로 변환합니다. 이름 바꾸기가 성공하면 사용자 프로필에는 정확히 하나의 기본 `external_id`(새 값)와 하나의 더 이상 사용되지 않는 외부 ID(이전 값)가 포함됩니다.

동일한 프로필에 대한 후속 이름 바꾸기 호출이 허용됩니다. 각 이름 바꾸기는 추가적인 더 이상 사용되지 않는 외부 ID를 생성하므로, 프로필에는 시간이 지남에 따라 하나의 기본 `external_id`와 여러 개의 더 이상 사용되지 않는 외부 ID가 누적될 수 있습니다. 그러나 `new_external_id` 값은 기본 또는 더 이상 사용되지 않는 외부 ID로서 어떤 Braze 프로필에도 이미 존재하지 않아야 합니다.

이 엔드포인트는 데이터 포인트를 기록하지 않으며 MAU 수에 영향을 미치지 않습니다. 이벤트, 구매, 속성, Campaign 인게이지먼트 등 모든 과거 사용자 데이터는 동일한 프로필에 연결된 상태로 유지됩니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.external_ids.rename` 권한이 있는 [API 키]({{site.baseurl}}/api/basics)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | 필수 | 외부 식별자 이름 변경 오브젝트 배열 | 외부 식별자 이름 바꾸기 오브젝트의 구조에 대한 요청 예시와 다음 제한 사항을 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

다음 사항에 유의하세요:

- `current_external_id`는 사용자의 기본 ID여야 하며 더 이상 사용되지 않는 ID일 수 없습니다. `current_external_id`로 전달된 값이 프로필에서 이미 더 이상 사용되지 않는 ID인 경우 호출이 실패합니다. 실패한 이름 바꾸기를 재시도하기 전에 [`/users/export/ids` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)를 사용하여 현재 기본 ID가 무엇인지 확인하세요.
- `new_external_id`는 이미 기본 ID 또는 더 이상 사용되지 않는 ID로 사용 중이 아니어야 합니다. 이미 더 이상 사용되지 않는 ID로 저장된 ID로 이름을 바꾸려고 하면 "new_external_id is already in use" 오류가 반환됩니다.
- `current_external_id`와 `new_external_id`는 동일할 수 없습니다.

## 요청 예시 {#request-example}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## 응답 {#response}

응답은 모든 성공적인 이름 변경과 실패한 이름 변경 및 관련 오류를 확인합니다. `rename_errors` 필드의 오류 메시지는 원래 요청 배열에 있는 오브젝트의 인덱스를 참조합니다.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

유효한 요청의 경우 `message` 필드는 `success`를 반환합니다. 보다 구체적인 오류는 `rename_errors` 배열에 캡처됩니다. `message` 필드는 다음과 같은 경우 오류를 반환합니다:

- 잘못된 API 키
- 빈 `external_id_renames` 배열
- 50개 이상의 오브젝트가 포함된 `external_id_renames` 배열
- 사용량 제한 도달(분당 1,000건 이상의 요청)

## 대량 마이그레이션 {#bulk-migrations}

대규모 사용자 집단을 포함하는 마이그레이션의 경우, 사용자를 최대 50명씩 그룹으로 나누어 각 배치를 별도의 API 호출로 전송합니다. 이 엔드포인트에는 분당 1,000건의 요청이라는 사용량 제한이 적용됩니다. 최대 배치 크기(요청당 50개 오브젝트)에서는 분당 최대 50,000건의 사용자 이름 바꾸기가 가능합니다.

배치 내의 각 이름 바꾸기 오브젝트는 독립적으로 처리됩니다. 하나의 오브젝트에서 실패가 발생해도 동일한 요청의 다른 오브젝트는 차단되지 않습니다. 응답 본문은 성공한 이름 바꾸기(`external_ids` 배열에 나열)와 실패한 이름 바꾸기(`rename_errors` 배열에 요청 배열 내 실패한 오브젝트의 위치에 대한 인덱스 참조와 함께 나열)를 구분합니다.

대량 마이그레이션을 실행할 때:

1. 전체 사용자 집단을 최대 50쌍의 배치로 Iterate하여 처리합니다.
2. 각 응답에서 `external_ids`(성공)와 `rename_errors`(실패)를 모두 검사하여 재시도가 필요한 사용자를 식별합니다.
3. 실패한 오브젝트를 수집하고 재시도 배치를 별도로 예약합니다. 일반적인 실패 원인으로는 `new_external_id`가 이미 사용 중이거나 `current_external_id`가 기본 ID가 아닌 더 이상 사용되지 않는 ID인 경우가 있습니다.
4. 마이그레이션 상태가 Braze 외부에서 추적될 수 있도록 성공과 실패를 자체 기록에 로깅합니다.

## 현재 외부 ID 확인 {#verifying-the-current-external-id}

마이그레이션 중에 특정 프로필에서 어떤 외부 ID가 활성 기본 식별자인지 확인해야 할 수 있습니다. 예를 들어, 특정 사용자가 이미 마이그레이션되었는지 확인하거나 실패한 이름 바꾸기를 문제 해결할 때 유용합니다. 이 목적으로 [`/users/export/ids` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)를 사용하세요.

내보내기 엔드포인트는 기본 및 더 이상 사용되지 않는 외부 ID를 모두 동일한 기본 프로필로 확인하며, 응답에서 항상 현재 기본 `external_id`를 반환합니다. 즉, 사용자에 대해 알려진 모든 식별자(이전 또는 새 식별자)로 쿼리할 수 있으며, 응답에는 정식 기본 ID가 포함됩니다. 이는 마이그레이션 상태를 확인하는 신뢰할 수 있는 방법입니다.

전체 프로필을 가져오지 않고 외부 ID만 확인하려면 `fields_to_export`에 `external_id` 필드만 전달하세요.

## 권장 마이그레이션 워크플로 {#recommended-migration-workflow}

대부분의 마이그레이션 사용 사례에서 권장되는 순서는 다음과 같습니다:

1. **스테이징에서 테스트** — 프로덕션에 적용하기 전에 개발 또는 스테이징 워크스페이스에서 전체 이름 바꾸기 및 확인 흐름을 실행합니다.
2. **배치로 이름 바꾸기** — `/users/external_ids/rename` 엔드포인트를 사용하여 최대 50개씩 배치로 처리하고, 각 응답에서 `rename_errors`를 처리하며 실패한 쌍을 재시도 대기열에 추가합니다.
3. **확인** — 각 배치 후(또는 마이그레이션 종료 시) `/users/export/ids`를 사용하여 프로필을 샘플 확인하고 예상되는 기본 `external_id`가 설정되었는지 확인합니다.
4. **사용 중단 기간 유지** — 이전 ID를 참조할 수 있는 시스템(현장의 레거시 앱 버전 포함)이 있는 한 더 이상 사용되지 않는 외부 ID를 활성 상태로 유지합니다. 이 단계를 서두르지 마세요.
5. **더 이상 사용되지 않는 ID 제거** — 모든 시스템이 새 ID를 사용하고 있음이 확인되면 [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)를 사용하여 최대 50개씩 배치로 정리합니다.

SDK 통합도 함께 마이그레이션하는 경우(예: `changeUser`에 전달되는 값을 변경하는 경우), 더 이상 사용되지 않는 ID가 제거되기 전에 서버와 클라이언트 모두에서 새 외부 ID가 사용되도록 API 측 이름 바꾸기와 앱 릴리스 일정을 조율하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### MAU에 영향을 미치나요? {#does-this-impact-mau}
아니요, 사용자 수는 동일하게 유지되며 새 `external_id`만 부여됩니다.

### 사용자 행동이 과거 기록에서 변경되나요? {#does-user-behavior-change-historically}
아니요, 사용자는 여전히 동일하며 모든 과거 행동이 여전히 해당 사용자와 연결되어 있기 때문입니다.

### 개발 또는 스테이징 워크스페이스에서 실행할 수 있나요? {#can-it-be-run-on-development-or-staging-workspaces}
예. 실제로 스테이징 또는 개발 워크스페이스에서 테스트 마이그레이션을 실행하고, 프로덕션 데이터에서 실행하기 전에 모든 것이 원활하게 진행되었는지 확인하는 것을 적극 권장합니다.

### 데이터 포인트를 기록하나요? {#does-this-log-data-points}
이 기능은 데이터 포인트를 기록하지 않습니다.

### 권장 사용 중단 기간은 어떻게 되나요? {#what-is-the-recommended-deprecation-period}
사용되지 않는 외부 ID를 얼마나 오래 보관할 수 있는지에 대한 엄격한 제한은 없지만, 더 이상 사용되지 않는 ID로 사용자를 참조할 필요가 없어진 후에는 제거하는 것을 적극 권장합니다.

### 프로필에 더 이상 사용되지 않는 외부 ID를 몇 개까지 보유할 수 있나요? {#how-many-deprecated-external-ids-can-a-profile-have}
사용자 프로필은 하나의 기본 `external_id`와 연속적인 이름 바꾸기 작업을 통해 누적된 임의 개수의 더 이상 사용되지 않는 외부 ID를 보유할 수 있습니다. 단일 프로필이 보유할 수 있는 더 이상 사용되지 않는 ID 수에 대한 문서화된 상한은 없지만, Braze에서는 더 이상 필요하지 않은 경우 가능한 한 빨리 제거할 것을 권장합니다.

{% endapi %}