---
nav_title: 중복 사용자 병합
article_title: 중복 사용자 병합
description: "Braze 대시보드에서 중복 사용자를 찾고 병합하는 방법을 알아봅니다."
page_order: 4
---

# 중복 사용자 병합 {#merge-duplicate-users}

> Campaign(캠페인)과 Canvases의 효과를 극대화할 수 있도록 중복 사용자를 찾고 병합하는 방법을 알아봅니다.

{% alert tip %}
Braze REST API를 사용하여 중복 사용자를 병합하려면 [POST: 사용자 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)을 참조하세요.
{% endalert %}

## 개별 병합 {#individual-merging}

사용자 검색에서 중복 프로필이 반환되면 Braze 대시보드의 사용자 프로필에서 각 프로필을 개별적으로 병합할 수 있습니다.

### 1단계: 중복 프로필 검색 {#step-1-search-for-a-duplicate-profile}

Braze에서 **오디언스** > **사용자 검색**을 선택합니다.

![내비게이션 메뉴에서 강조 표시된 사용자 검색 타일.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

중복 프로필의 이메일 주소나 전화번호와 같은 고유 식별자를 입력한 다음 **Search**를 선택합니다.

![Braze 대시보드의 사용자 검색 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### 2단계: 중복 항목 병합 {#step-2-merge-duplicates}

병합 프로세스를 시작하려면 **Merge duplicates**를 선택합니다.

![중복 사용자 프로필 중 하나.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

유지할 사용자 프로필과 병합할 프로필을 선택한 다음 **Merge profiles**를 선택합니다. 모든 중복 프로필이 병합될 때까지 이 과정을 반복합니다.

![중복 프로필의 개별 병합 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}

## 일괄 병합 {#bulk-merging}

중복 사용자를 일괄 병합하면 Braze가 일치하는 식별자(예: 이메일 주소)를 가진 프로필을 찾아 하나의 프로필을 유지합니다. Braze는 먼저 `external_id`가 있는 프로필을 우선시한 다음 **Resolving ties** 설정인 **Resolve ties using** 및 **Prioritization**을 적용합니다. `external_id`가 있는 프로필이 없는 경우 Braze는 `external_id`가 없는 프로필 전체에 **Resolve ties using** 및 **Prioritization**을 사용합니다. Braze는 이러한 설정이 유지할 프로필 하나를 식별하는 경우에만 사용자를 병합합니다. 예를 들어, **Resolve ties using**이 **Updated date**이고 두 프로필의 마지막 업데이트 타임스탬프가 동일한 경우 Braze는 동점을 해결할 수 없으므로 해당 사용자는 병합되지 않습니다.

### 1단계: 오디언스 관리로 이동 {#step-1-go-to-manage-audience}

Braze 대시보드에서 **오디언스** > **오디언스 관리**를 선택합니다.

![내비게이션 메뉴에서 강조 표시된 오디언스 관리 타일.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### 2단계: 결과 미리보기(선택 사항) {#step-2-preview-the-results-optional}

중복 항목을 병합하기 전에 결과를 미리 보려면 **Generate list of duplicates**를 선택합니다.

![Generate list of duplicates가 강조 표시된 오디언스 관리 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze가 미리보기를 생성하여 이메일 주소로 CSV 파일로 전송합니다.

![생성된 CSV 파일 링크가 포함된 Braze 이메일.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

다음 예시에서 Braze는 사용자의 외부 ID를 사용하여 중복 프로필을 표시하고 유지할 프로필을 식별합니다. 이러한 프로필이 일괄 병합되면 Braze는 외부 ID가 있는 프로필을 사용자의 새 기본 프로필로 사용합니다.

{% tabs local %}
{% tab example csv file %}
| 이메일 주소 | 외부 ID | 전화번호 | Braze ID | 규칙 식별자 | 유지할 프로필 | 병합할 프로필 |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### 병합 동작 {#merge-behavior}

Braze는 유지되는 프로필의 비어 있는 필드를 병합된 프로필의 값으로 채웁니다. 채워지는 필드 목록은 [병합 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)을 참조하세요.

### 3단계: 중복 항목 병합 {#step-3-merge-your-duplicates}

미리보기 결과에 만족하면 **Merge all duplicates**를 선택합니다.

{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}

![Merge all duplicates가 강조 표시된 오디언스 관리 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## 규칙 기반 병합 {#rules-based-merging}

병합 실행 시 중복 프로필이 해결되는 방식을 제어하는 규칙을 사용하여 가장 관련성 높은 사용자 프로필을 유지할 수 있습니다. 규칙이 설정되면 Braze는 기준에 맞는 프로필을 유지합니다.

### 1단계: 규칙 정의 {#step-1-define-your-rules}

1. **오디언스** > **오디언스 관리** > **Edit rules**로 이동합니다.
2. **Edit rules** 패널의 **Profile to keep** 섹션에서 중복 항목 병합 시 유지할 프로필의 **Identifier**를 선택합니다. 이메일 주소 또는 전화번호를 선택할 수 있습니다.
3. **Resolving ties** 섹션에서 **Profile to keep**의 일치하는 기준을 가진 프로필 간의 동점을 해결하는 기준을 선택합니다. 다음을 선택할 수 있습니다:<br>
- **Resolve ties using**: Created date, Updated date, Last session
- **Prioritization**: Newest, Oldest

![Profile to keep과 Resolving ties 옵션을 선택하는 섹션이 있는 Edit rules 패널.]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

예를 들어, 전화번호가 있는 프로필을 유지할 수 있습니다. 여러 사용자가 동일한 전화번호를 가진 경우 **Updated date** 필드를 사용하여 동점을 해결하고 가장 최근에 업데이트된 사용자를 우선시할 수 있습니다.

### 2단계: 결과 미리보기(선택 사항)

규칙을 저장한 후 **Generate a list of duplicates**를 선택하여 규칙이 어떻게 작동하는지 미리 볼 수 있습니다. Braze가 미리보기를 생성하여 이메일 주소로 CSV 파일로 전송하며, 규칙이 적용될 경우 유지 및 병합될 사용자를 보여줍니다.

### 3단계: 중복 항목 병합 {#step-3-merge-duplicates}

미리보기 결과에 만족하면 **오디언스 관리** 페이지로 돌아가서 **Merge all duplicates**를 선택합니다.

{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}

## 예약 병합 {#scheduled-merging}

규칙 기반 병합과 유사하게, 예약 병합을 사용하면 사전 구성된 규칙을 사용하여 매일 사용자 프로필 병합을 자동화할 수 있습니다.

![schedule 버튼이 있는 오디언스 관리 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

기능이 활성화되면 Braze가 자동으로 시간대를 할당하여 사용자의 회사 시간대 기준 매일 약 오전 12시에 병합 프로세스를 수행합니다. 예약 병합은 언제든지 비활성화할 수 있습니다. Braze는 예약된 병합이 실행되기 24시간 전에 워크스페이스 관리자에게 알림을 보내 구성을 검토할 시간을 제공합니다.

{% alert warning %}
중복 사용자 프로필은 병합 후 복구할 수 없습니다.
{% endalert %}