---
nav_title: 중복 사용자 병합
article_title: 중복 사용자 병합
description: "Braze 대시보드에서 중복 사용자를 찾고 병합하는 방법을 알아보세요."
page_order: 4
---

# 중복 사용자 병합 {#merge-duplicate-users}

> Campaign과 Canvases의 효과를 극대화할 수 있도록 중복 사용자를 찾고 병합하는 방법을 알아보세요.

## REST API: 사용자 식별 및 병합 {#rest-api-identify-and-merge-users}

이 페이지의 도구는 대시보드에서 중복 프로필을 병합합니다. Braze의 [사용자 데이터 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/)를 통해 프로필을 결합하거나 다시 연결할 수도 있습니다.

- [POST: 사용자 식별]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) (`/users/identify`): 별칭 전용, 이메일 전용 또는 전화번호 전용 프로필을 `external_id`가 있는 프로필과 결합합니다.
- [POST: 사용자 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) (`/users/merge`): 하나의 고객 프로필을 다른 프로필에 병합합니다. 두 프로필 모두 이미 `external_id`가 있는 경우에도 가능합니다. 이 엔드포인트를 호출하기 전에 [필수 조건]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#prerequisites) 및 [병합 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)을 검토하세요.

익명 프로필이 기존 식별된 프로필과 매칭되면(예: SDK `changeUser()` 호출 또는 `/users/identify`를 통해), Braze는 익명 프로필을 분리하고 특정 필드만 식별된 프로필에 복사합니다. 자세한 내용은 [익명 사용자를 식별할 때 발생하는 일]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users)을 참조하세요.

사용자 병합은 되돌리기 어렵습니다. 여러 `external_id` 값에 걸친 복잡한 병합이나 대규모 프로필 마이그레이션을 계획하고 있다면, `/users/merge`에 의존하기 전에 Braze 고객 성공 매니저에게 안내를 요청하세요.

Braze는 병합 시 삭제 예정 사용자, 테스트 사용자, 전역 제어 그룹 사용자의 세 가지 사용자 유형을 다르게 처리합니다. 자세한 내용은 [사용자 병합 동작]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/)을 참조하세요.

## 개별 병합 {#individual-merging}

사용자 검색에서 중복 프로필이 반환되면 Braze 대시보드의 고객 프로필에서 각 프로필을 개별적으로 병합할 수 있습니다.

### 1단계: 중복 프로필 검색 {#step-1-search-for-a-duplicate-profile}

Braze에서 **오디언스** > **사용자 검색**을 선택합니다.

![내비게이션 메뉴에서 강조 표시된 "사용자 검색" 타일.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

중복 프로필의 이메일 주소나 전화번호와 같은 고유 식별자를 입력한 다음 **검색**을 선택합니다.

![Braze 대시보드의 "사용자 검색" 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### 2단계: 중복 항목 병합 {#step-2-merge-duplicates}

병합 프로세스를 시작하려면 **Merge duplicates**를 선택합니다.

![중복 사용자 프로필 중 하나.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

유지할 고객 프로필과 병합할 프로필을 선택한 다음 **Merge profiles**를 선택합니다. 모든 중복 프로필이 병합될 때까지 이 과정을 반복합니다.


{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}

## 일괄 병합 {#bulk-merging}

중복 사용자를 일괄 병합하면 Braze가 일치하는 식별자(예: 이메일 주소)를 가진 프로필을 찾아 하나의 프로필을 유지합니다. Braze는 먼저 `external_id`가 있는 프로필을 우선시한 다음 **동점 해결** 설정인 **Resolve ties using** 및 **Prioritization**을 적용합니다. `external_id`가 있는 프로필이 없는 경우 Braze는 `external_id`가 없는 프로필 전체에 **Resolve ties using** 및 **Prioritization**을 사용합니다. Braze는 이러한 설정이 유지할 프로필 하나를 식별하는 경우에만 사용자를 병합합니다. 예를 들어, **Resolve ties using**이 **Updated date**이고 두 프로필의 마지막 업데이트 타임스탬프가 동일한 경우 Braze는 동점을 해결할 수 없으므로 해당 사용자는 병합되지 않습니다.

### 1단계: 오디언스 관리로 이동 {#step-1-go-to-manage-audience}

Braze 대시보드에서 **오디언스** > **오디언스 관리**를 선택합니다.

![내비게이션 메뉴에서 강조 표시된 "오디언스 관리" 타일.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### 2단계: 결과 미리보기(선택 사항) {#step-2-preview-the-results-optional}

중복 항목을 병합하기 전에 결과를 미리 보려면 **Generate list of duplicates**를 선택합니다.

![**Generate list of duplicates**가 강조 표시된 "오디언스 관리" 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze가 미리보기를 생성하여 이메일 주소로 CSV 파일로 전송합니다.


다음 예시에서 Braze는 사용자의 외부 ID를 사용하여 중복 프로필을 표시하고 유지할 프로필을 식별합니다. 이러한 프로필이 일괄 병합되면 Braze는 외부 ID가 있는 프로필을 사용자의 새 기본 프로필로 사용합니다.

{% tabs local %}
{% tab example csv file %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2단계: 결과 미리보기(선택 사항)" }
{% endtab %}
{% endtabs %}

#### 병합 동작 {#merge-behavior}

Braze는 유지되는 프로필의 비어 있는 필드를 병합된 프로필의 값으로 채웁니다. 채워지는 필드 목록은 [병합 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)을 참조하세요.

### 3단계: 중복 항목 병합 {#step-3-merge-your-duplicates}

미리보기 결과에 만족하면 **Merge all duplicates**를 선택합니다.

{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}


## 규칙 기반 병합 {#rules-based-merging}

병합 실행 시 중복 프로필이 해결되는 방식을 제어하는 규칙을 사용하여 가장 관련성 높은 고객 프로필을 유지할 수 있습니다. 규칙이 설정되면 Braze는 기준에 맞는 프로필을 유지합니다.

### 1단계: 규칙 정의 {#step-1-define-your-rules}

1. **오디언스** > **오디언스 관리** > **Edit rules**로 이동합니다.
2. **Edit rules** 패널의 **Profile to keep** 섹션에서 중복 항목 병합 시 유지할 프로필의 **Identifier**를 선택합니다. 이메일 주소 또는 전화번호를 선택할 수 있습니다.
3. **Resolving ties** 섹션에서 **Profile to keep**의 일치하는 기준을 가진 프로필 간의 동점을 해결하는 기준을 선택합니다. 다음을 선택할 수 있습니다:<br>
- **Resolve ties using**: Created date, Updated date, Last session
- **Prioritization**: Newest, Oldest

![**Profile to keep**과 **Resolving ties** 옵션을 선택하는 섹션이 있는 **Edit rules** 패널.]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

예를 들어, 전화번호가 있는 프로필을 유지할 수 있습니다. 여러 사용자가 동일한 전화번호를 가진 경우 **Updated date** 필드를 사용하여 동점을 해결하고 가장 최근에 업데이트된 사용자를 우선시할 수 있습니다.

### 2단계: 결과 미리보기(선택 사항)

규칙을 저장한 후 **Generate a list of duplicates**를 선택하여 규칙이 어떻게 작동하는지 미리 볼 수 있습니다. Braze가 미리보기를 생성하여 이메일 주소로 CSV 파일로 전송하며, 규칙이 적용될 경우 유지 및 병합될 사용자를 보여줍니다.

### 3단계: 중복 항목 병합 {#step-3-merge-duplicates}

미리보기 결과에 만족하면 **오디언스 관리** 페이지로 돌아가서 **Merge all duplicates**를 선택합니다.

{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}

## 예약 병합 {#scheduled-merging}

규칙 기반 병합과 유사하게, 예약 병합을 사용하면 사전 구성된 규칙을 사용하여 매일 고객 프로필 병합을 자동화할 수 있습니다.

![schedule 버튼이 있는 "오디언스 관리" 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

기능이 활성화되면 Braze가 자동으로 시간대를 할당하여 사용자의 회사 시간대 기준 매일 약 오전 12시에 병합 프로세스를 수행합니다. 예약 병합은 언제든지 비활성화할 수 있습니다. Braze는 예약된 병합이 실행되기 24시간 전에 워크스페이스 관리자에게 알림을 보내 구성을 검토할 시간을 제공합니다.

{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}

## 동일한 이메일 주소에 여러 고객 프로필이 연결되는 이유 {#why-are-multiple-user-profiles-associated-with-the-same-email-address}

Braze는 서로 다른 식별자, 가져오기 또는 식별 전 익명 세션을 통해 프로필이 생성된 경우 동일한 이메일 주소를 공유하는 여러 고객 프로필을 저장합니다. 이는 사용자가 단일 `external_id`를 공유하지 않을 때 예상되는 동작입니다.

중복 항목을 병합하기 전에 [식별자별 사용자 프로필 내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)를 사용하여 이메일 주소에 어떤 프로필이 존재하는지, 각 프로필에 어떤 필드가 포함되어 있는지 확인하세요. **오디언스** > **사용자 검색**에서 이메일로 검색하여 대시보드에서 중복 항목을 검토할 수도 있습니다.

## 관련 문서 {#related-articles}

- [사용자 병합 동작]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/)
- [POST: 사용자 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [사용자 삭제]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)