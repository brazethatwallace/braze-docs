---
nav_title: 수집 모범 사례
article_title: 수집 모범 사례
page_order: 4
page_type: reference
description: "이 문서에서는 신규 및 기존 사용자 데이터를 수집하는 다양한 방법과 모범 사례를 명확히 설명합니다."

---

# 수집 모범 사례 {#collection-best-practices}

> 고객의 사용자 프로필 수명주기를 구상할 때 알려진 사용자와 알려지지 않은 사용자의 사용자 데이터를 언제, 어떻게 수집해야 하는지 파악하는 것은 어려울 수 있습니다. 이 문서에서는 사용 사례를 안내하여 신규 및 기존 사용자 데이터를 수집하는 다양한 방법과 모범 사례를 명확히 설명합니다.

다음 예는 이메일 수집 사용 사례이지만, 이 로직은 다양한 데이터 수집 시나리오에 적용될 수 있습니다. 이 예에서는 이미 가입 양식이나 사용자 정보를 수집하는 방법을 통합했다고 가정합니다.

사용자가 기록할 정보를 제공한 후에는 해당 데이터가 데이터베이스에 이미 존재하는지 확인하고, 필요한 경우 사용자 별칭 프로필을 만들거나 기존 사용자 프로필을 업데이트하는 것이 좋습니다.

알 수 없는 사용자가 사이트를 방문한 후 나중에 계정을 만들거나 이메일 가입을 통해 신원을 확인하는 경우, 프로필 병합을 신중하게 처리해야 합니다. 병합하는 방법에 따라 별칭 전용 사용자 정보 또는 익명 데이터가 덮어쓰여질 수 있습니다.

## 웹 양식을 통한 사용자 데이터 수집 {#capturing-user-data-through-a-web-form}

### 1단계: 사용자 존재 여부 확인 {#step-1-check-if-the-user-exists}

사용자가 웹 양식을 통해 콘텐츠를 입력하면, 해당 이메일을 가진 사용자가 데이터베이스에 이미 존재하는지 확인합니다. 다음 방법 중 하나를 사용할 수 있습니다:

- **내부 데이터베이스 확인(권장):** Braze 외부에 제공된 사용자 정보를 포함하는 외부 기록이나 데이터베이스가 있는 경우, 이메일 제출 또는 계정 생성 시 해당 정보가 이미 수집되지 않았는지 확인하세요.
- **[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track):** `email`을 식별자로 사용하면, 해당 이메일 주소가 아직 존재하지 않을 경우 새 고객 프로필이 생성됩니다.
- **[`/subscription/status/get` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status):** 커스텀 양식을 통해 이메일을 수집한 다음 REST API로 구독 그룹 멤버십을 설정하는 경우, 먼저 이 엔드포인트를 호출하세요. 일치하는 프로필이 없으면 [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 사용하여 사용자를 생성하거나 구독 처리합니다. 그렇지 않으면 중복 프로필을 만들지 않고 기존 프로필을 업데이트하세요.

### 2단계: 사용자 기록 또는 업데이트 {#step-2-log-or-update-user}

- **사용자가 존재하는 경우:**
  - 새 프로필을 생성하지 마세요.
  - 사용자의 프로필에 커스텀 속성(예: `newsletter_subscribed: true`)을 기록하여 해당 사용자가 뉴스레터 구독을 통해 이메일을 제출했음을 나타냅니다. 동일한 이메일 주소를 가진 Braze 고객 프로필이 여러 개 있는 경우, 모든 프로필이 내보내기됩니다.<br><br>
- **사용자가 존재하지 않는 경우:**
  - [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 별칭 전용 프로필을 생성합니다. 이 엔드포인트는 [`user_alias` 객체]({{site.baseurl}}/api/objects_filters/user_alias_object)를 수락하며, `update_existing_only`가 `false`로 설정된 경우 별칭 전용 프로필을 생성합니다. 사용자의 이메일을 사용자 별칭으로 설정하여 향후 해당 사용자를 참조할 수 있도록 합니다(사용자에게 `external_id`가 없으므로).

![별칭 전용 고객 프로필 업데이트 프로세스를 보여주는 다이어그램. 사용자가 마케팅 랜딩 페이지에서 이메일 주소와 커스텀 속성인 우편번호를 제출합니다. 랜딩 페이지 수집에서 별칭 전용 고객 프로필로 향하는 화살표는 사용자 추적 엔드포인트에 대한 Braze API 요청을 나타내며, 요청 본문에는 사용자의 별칭 이름, 별칭 라벨, 이메일, 우편번호가 포함되어 있습니다. 프로필에는 요청 본문의 속성과 함께 "Braze에서 생성된 별칭 전용 사용자"라는 라벨이 표시되어 새로 생성된 프로필에 데이터가 반영되었음을 보여줍니다.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## 이메일 캡처 양식을 통한 사용자 이메일 수집 {#capturing-user-emails-through-an-email-capture-form}

이메일 캡처 양식을 사용하여 사용자에게 이메일 주소를 제출하도록 안내하면, 해당 주소가 고객 프로필에 추가됩니다. 이 양식을 설정하는 방법에 대한 자세한 내용은 [이메일 캡처 양식]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form)을 참조하세요.

커스텀 양식을 사용하고 REST API를 통해 구독 그룹 멤버십을 설정하는 경우, 사용자를 생성하기 전에 프로필이 이미 존재하는지 확인하세요. [1단계: 사용자 존재 여부 확인](#step-1-check-if-user-exists)을 참조하세요.

## 별칭 전용 사용자 식별 {#identifying-alias-only-users}

계정 생성 시 사용자를 식별할 때, 별칭 전용 사용자는 [`/users/identify` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 통해 별칭 전용 사용자를 알려진 프로필과 병합하여 식별하고 외부 ID를 할당할 수 있습니다.

사용자가 별칭 전용인지 확인하려면, 데이터베이스 내에 [사용자가 존재하는지 확인](#step-1-check-if-user-exists)하세요.
- 외부 레코드가 존재하면 `/users/identify/` 엔드포인트를 호출할 수 있습니다.
- [`/users/export/id` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)가 `external_id`를 반환하면 `/users/identify/` 엔드포인트를 호출할 수 있습니다.
- 엔드포인트가 아무것도 반환하지 않으면 `/users/identify/` 호출을 하지 않아야 합니다.

## 별칭 전용 사용자 정보가 이미 존재할 때 사용자 데이터 캡처하기 {#capturing-user-data-when-alias-only-user-information-is-already-present}

사용자가 계정을 만들거나 이메일 가입을 통해 자신을 식별하면 프로필을 병합할 수 있습니다. 병합할 수 있는 필드 목록은 [병합 업데이트 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)을 참조하세요.

### 중복 사용자 프로필 병합하기 {#merging-duplicate-user-profiles}

사용자 데이터가 늘어남에 따라 Braze 대시보드에서 중복된 사용자 프로필을 병합할 수 있습니다. 이러한 중복 프로필은 동일한 검색 쿼리를 사용하여 찾아야 합니다. 사용자 프로필을 중복 처리하는 방법에 대한 자세한 내용은 [중복 사용자 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)을 확인하세요.

또한 [사용자 병합 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)를 사용하여 하나의 사용자 프로필을 다른 프로필로 병합할 수도 있습니다.

{% alert note %}
사용자 프로필이 병합된 후에는 이 작업을 되돌릴 수 없습니다.
{% endalert %}

## 추가 리소스 {#additional-resources}
- 추가적인 맥락을 위해 Braze [사용자 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) 문서를 참조하세요.<br>
- 사용자 ID 설정 및 `changeUser()` 메서드 호출에 대한 설명서를 확인하세요: [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#suggested-user-id-naming-convention), [웹]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).