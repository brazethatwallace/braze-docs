---
nav_title: 고객 프로필 수명주기
article_title: 고객 프로필 수명주기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze 고객 프로필 수명주기와 고객 프로필을 식별하고 참조할 수 있는 다양한 방법에 대해 설명합니다."

---

# 고객 프로필 수명주기 {#user-profile-lifecycle}

> 이 문서에서는 Braze 고객 프로필 수명주기와 고객 프로필을 식별하고 참조하는 다양한 방법에 대해 설명합니다. 고객 생애주기를 더 잘 이해하고 싶다면 [사용자 라이프사이클 매핑](https://learning.braze.com/mapping-customer-lifecycles)에 대한 Braze 학습 과정을 확인해 보세요.

사용자와 관련된 모든 영구 데이터는 고객 프로필에 저장됩니다. API를 통해 고객 프로필을 생성하거나 SDK에서 사용자를 인식한 후, 해당 프로필에 여러 매개변수를 할당하여 사용자를 식별하고 참조할 수 있습니다.

이러한 매개변수에는 다음이 포함됩니다:

* `braze_id` (Braze에서 할당)
* `external_id`
* `email`
* `phone`
* 설정한 커스텀 사용자 별칭(개수 제한 없음)

## 익명 사용자 프로필 {#anonymous-user-profiles}

지정된 `external_id`가 없는 사용자는 [익명 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)라고 합니다. 예를 들어, 웹사이트를 방문했지만 가입하지 않은 사용자나 모바일 앱을 다운로드했지만 프로필을 생성하지 않은 사용자가 이에 해당합니다.

처음에 SDK가 사용자를 인식하면 연결된 `braze_id`와 함께 익명 고객 프로필이 생성됩니다. `braze_id`는 Braze가 자동으로 할당하는 고유 식별자로, 편집할 수 없으며 기기별로 고유합니다. 이 식별자를 사용하여 [API]({{site.baseurl}}/api/endpoints/user_data)를 통해 고객 프로필을 업데이트할 수 있습니다.

## 식별된 사용자 프로필 {#identified-user-profiles}

앱에서 사용자를 인식할 수 있게 되면(사용자 ID 또는 이메일 주소 형태를 제공하여), `changeUser` 메서드([웹](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html))를 사용하여 해당 사용자의 프로필에 `external_id`를 할당하는 것을 권장합니다. `external_id`를 사용하면 여러 기기에서 동일한 고객 프로필을 식별할 수 있습니다.

`external_id`를 사용하면 다음과 같은 추가적인 이점이 있습니다:

- 여러 기기와 플랫폼에서 일관된 사용자 경험을 제공합니다(예: iPhone 앱의 충성 사용자에게 Android 태블릿에서 이탈 사용자 알림을 보내지 않음).
- 사용자가 앱을 삭제하고 다시 설치하거나 다른 기기에 앱을 설치할 때마다 새 고객 프로필을 생성하지 않도록 하여 분석의 정확성을 향상시킵니다.
- [사용자 데이터 엔드포인트]({{site.baseurl}}/api/endpoints/user_data)를 사용하여 앱 외부 소스에서 사용자 데이터를 가져오고, [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 사용하여 트랜잭션 메시지로 사용자를 타겟팅할 수 있습니다.
- 세그먼터 내의 "테스트" [필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) 및 [**사용자 검색**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) 페이지에서 개별 사용자를 검색할 수 있습니다.

### 외부 ID 관련 고려 사항 {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### 이메일 또는 해시된 이메일을 외부 ID로 사용할 때의 위험 {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에서 ID 관리를 간소화할 수 있지만, 사용자 개인정보 보호 및 데이터 보안에 대한 잠재적 위험을 고려하는 것이 중요합니다.

- **추측 가능한 정보:** 이메일 주소는 쉽게 추측할 수 있어 공격에 취약합니다.
- **악용 위험:** 악의적인 사용자가 웹 브라우저를 변조하여 다른 사람의 이메일 주소를 자신의 외부 ID로 전송하면, 민감한 메시지나 계정 정보에 접근할 수 있는 가능성이 있습니다.

### 익명 사용자를 식별할 때 발생하는 상황 {#what-happens-when-you-identify-anonymous-users}

익명 사용자를 식별할 때 다음 두 가지 시나리오 중 하나가 발생할 수 있습니다:

1) **익명 사용자가 새로운 식별된 사용자가 되는 경우:** <br>해당 `external_id`가 Braze에 아직 존재하지 않으면, 익명 사용자는 새로운 식별된 사용자가 되며 익명 사용자의 모든 속성과 기록을 그대로 유지합니다.

2) **익명 사용자가 이미 존재하는 사용자로 식별되는 경우:** <br>해당 `external_id`가 이미 Braze에 존재하면, 이 사용자는 다른 기기(예: 태블릿)를 통하거나 가져온 사용자 데이터 등 다른 방법으로 시스템에서 이전에 식별된 사용자입니다.

즉, 이 사용자에 대한 고객 프로필이 이미 존재합니다. 이 경우 Braze는 다음을 수행합니다:
1. 익명 사용자를 분리(orphan)합니다
2. 익명 프로필에서 식별된 고객 프로필에 아직 존재하지 않는 [특정 고객 프로필 필드]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)를 병합합니다
3. 사용자 수가 부풀려지지 않도록 사용자 기반에서 익명 프로필을 제거합니다

익명 사용자와 알려진 사용자 모두 이름이 있는 경우, 알려진 사용자의 이름이 유지됩니다. 알려진 사용자의 값이 null이고 익명 사용자에게 값이 있는 경우, 해당 값이 이 [특정 고객 프로필 필드]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)에 해당하면 익명 사용자의 값이 알려진 사용자의 프로필에 병합됩니다.

{% alert important %}
익명 프로필의 모든 데이터가 병합되는 것은 아닙니다. 푸시 토큰과 메시징 기록은 이전되며, 익명 프로필의 커스텀 속성, 커스텀 이벤트, 구매 기록은 해당 필드가 식별된 고객 프로필에 아직 존재하지 않는 경우에만 식별된 사용자에게 병합됩니다. 데이터가 충돌하는 경우 식별된 사용자의 값이 유지됩니다. 이전되는 필드와 이전되지 않는 필드의 전체 목록은 [병합 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)을 참조하세요.
{% endalert %}

고객 프로필에 `external_id`를 설정하는 방법에 대한 자세한 내용은 설명서([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [웹]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web))를 참조하세요.

{% alert note %}
분리(orphan)된 사용자는 메시지를 수신할 수 없습니다.
{% endalert %}

### 중복 사용자 병합하기 {#merging-duplicate-users}

워크스페이스에서 중복된 고객 프로필을 발견하면 REST API를 사용하여 병합할 수 있습니다. 사용자 병합 및 사용 가능한 방법에 대한 자세한 내용은 [중복 사용자 병합하기]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)를 참조하세요.

## 사용자 별칭 {#user-aliases}

Braze `external_id` 이외의 식별자로 사용자를 참조하려면 고객 프로필에 사용자 별칭을 설정하세요. 고객 프로필에 설정된 별칭은 사용자의 `braze_id` 또는 `external_id`를 대체하는 것이 아니라 추가로 작동합니다. 고객 프로필에 설정할 수 있는 별칭의 수에는 제한이 없습니다.

각 별칭은 두 부분으로 구성된 키-값 페어로 작동합니다. 별칭의 키를 정의하는 `alias_label`과 값을 정의하는 `alias_name`입니다. 단일 라벨에 대한 `alias_name`은 사용자 기반 전체에서 고유해야 합니다(`external_id`와 마찬가지). 이미 존재하는 라벨과 이름 조합으로 두 번째 고객 프로필을 업데이트하려고 하면 해당 고객 프로필은 업데이트되지 않습니다.

### 사용자 별칭 업데이트 {#updating-user-aliases}

별칭이 설정된 후에는 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint)를 사용하거나 SDK를 통해 새 이름을 전달하여 지정된 라벨에 대한 새 이름으로 업데이트할 수 있습니다. 그러면 해당 사용자의 데이터를 내보낼 때 사용자 별칭이 표시됩니다.

![동일한 사용자 별칭 라벨을 가지지만 별칭 이름이 다른 별도의 사용자에 대한 두 개의 서로 다른 고객 프로필]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### 익명 사용자 태깅 {#tagging-anonymous-users}

사용자 별칭을 사용하면 익명 사용자에게 식별자를 태깅할 수도 있습니다. 예를 들어, 사용자가 이커머스 사이트에 이메일 주소를 제공했지만 아직 가입하지 않은 경우, 해당 이메일 주소를 익명 사용자의 별칭으로 사용할 수 있습니다. 이러한 사용자는 별칭을 사용하여 내보내거나 API에서 참조할 수 있습니다.

### 익명 사용자 프로필에서의 별칭 동작 {#behavior-of-aliases-on-anonymous-user-profiles}

별칭이 있는 익명 사용자 프로필이 나중에 `external_id`로 식별되면 일반 식별된 고객 프로필로 처리되지만, 기존 별칭은 유지되며 해당 별칭으로 계속 참조할 수 있습니다.

### 사용자 별칭 검색 {#searching-for-a-user-alias}

사용자의 별칭 이름과 라벨을 알고 있다면 **사용자 검색**에서 `alias_label:alias_name` 형식으로 사용자를 찾을 수 있습니다. 예를 들어, 이름이 `alias_name: bobby_alias`이고 라벨이 `alias_label: m4pzOndtA-CnO0u`인 별칭 전용 프로필이 있는 경우, `m4pzOndtA-CnO0u:bobby_alias`를 입력하여 이 사용자를 찾을 수 있습니다.

이 정보를 모르는 경우 [`Export user profile by identifier` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)를 호출하여 API 응답에서 사용자 별칭을 찾을 수 있습니다.

### 알려진 고객 프로필에 별칭 설정 {#setting-aliases-on-known-user-profiles}

사용자 별칭은 알려진 고객 프로필에도 설정하여 외부에서 알려진 다른 ID로 알려진 사용자를 참조할 수 있습니다. 예를 들어, 사용자에게 Braze 내에서 참조하고자 하는 비즈니스 인텔리전스 도구 ID(예: Amplitude ID)가 있을 수 있습니다.

사용자 별칭을 설정하는 방법에 대한 자세한 내용은 각 플랫폼의 설명서를 참조하세요([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#aliasing-users), [웹]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#aliasing-users)).

![Braze에서 고객 프로필 수명주기의 흐름도. 익명 사용자에 대해 changeUser()가 호출되면 해당 사용자는 식별된 사용자가 되고 데이터가 식별된 고객 프로필로 마이그레이션됩니다. 식별된 사용자는 Braze ID와 외부 ID를 갖습니다. 이 시점에서 두 번째 익명 사용자에 대해 changeUser()가 호출되면, 식별된 사용자에 아직 존재하지 않는 사용자 데이터 필드가 병합됩니다. 식별된 사용자의 기존 고객 프로필에 별칭이 추가되면 데이터에는 영향이 없지만 별칭이 있는 식별된 사용자가 됩니다. 식별된 사용자와 동일한 별칭 라벨을 가지지만 다른 별칭 이름을 가진 세 번째 익명 사용자에 대해 changeUser()가 호출되면, 식별된 사용자에 존재하지 않는 필드가 병합되고 식별된 고객 프로필의 별칭 라벨은 유지됩니다.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
고객의 고객 프로필 수명주기에서 이것이 어떻게 보이는지 잘 그려지지 않나요? [모범 사례]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)를 방문하여 사용자 데이터 수집 모범 사례를 확인하세요.
{% endalert %}

## 고급 사용 사례 {#advanced-use-case}

SDK 및 API의 [사용자 데이터 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint)를 통해 기존 식별된 고객 프로필에 새 사용자 별칭을 설정할 수 있습니다. 그러나 기존의 알 수 없는 고객 프로필에 대해서는 API를 통해 사용자 별칭을 설정할 수 없습니다.

사용자 별칭도 이 과정에서 병합됩니다. 그러나 분리될 사용자와 대상 사용자 모두 동일한 라벨의 별칭을 가지고 있는 경우, 대상 사용자의 별칭만 유지됩니다.

앱을 삭제하고 다시 설치하면 해당 사용자에 대해 새로운 익명 `braze_id`가 생성됩니다.

### 사용자 ID를 활용한 문제 해결 {#troubleshooting-with-user-ids}

모든 사용자 ID를 사용하여 대시보드에서 테스트 목적으로 사용자를 찾고 식별할 수 있습니다. Braze 대시보드에서 사용자를 찾으려면 [테스트 사용자 추가]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)를 참조하세요.

{% alert important %}
Braze는 비정상적으로 커진 고객 프로필("더미 사용자")을 차단합니다. 이러한 프로필은 일반적으로 잘못된 통합의 결과입니다. 프로필이 다음 임계값 중 하나를 초과하면 차단됩니다:

- 5,000,000개 이상의 세션
- 20,000개 이상의 고유 커스텀 이벤트 이름
- 20,000개 이상의 고유 구매 제품 이름

프로필이 차단되면 Braze는 SDK와 REST API 모두에서 해당 프로필에 대한 모든 수신 데이터 수집을 중단합니다. 정상적인 사용자에게 이런 일이 발생한 경우 Braze 계정 매니저에게 문의하세요. 자세한 내용은 [스팸 차단]({{site.baseurl}}/user_archival)을 참조하세요.
{% endalert %}