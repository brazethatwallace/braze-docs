---
nav_title: 오디언스
article_title: Braze 오디언스
page_order: 0
page_type: reference
description: "Braze가 사용자를 정의하고 관리하는 방법, 사용자를 식별하는 방법, 그리고 사용자 데이터를 활용하여 채널 전반에서 세분화, 개인화, 메시징을 지원하는 방법을 알아보세요."

---

# Braze 오디언스 {#your-braze-audience}

> Braze가 사용자를 정의하고 관리하는 방법, 사용자를 식별하는 방법, 그리고 사용자 데이터를 활용하여 채널 전반에서 세분화, 개인화, 메시징을 지원하는 방법을 알아보세요.

Braze에서 사용자(및 해당 고객 프로필)는 메시지를 보내고 분석할 수 있는 개별 인물을 나타냅니다.

## 고객 프로필 {#user-profiles}

[고객 프로필]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)은 Braze가 해당 사용자에 대해 알고 있는 모든 정보의 단일 소스 역할을 하며, 다음을 포함합니다:

- 식별자(사용자 ID 또는 외부 ID 등)
- 기기 및 메시징 채널
- 행동 데이터 및 이벤트
- 속성 및 기본 설정
- 메시지 인게이지먼트 기록

하나의 고객 프로필은 여러 기기 및 채널과 연결될 수 있으므로, 플랫폼 전반에 걸쳐 사용자를 종합적으로 이해하고 메시지를 보낼 수 있습니다.

## 익명 사용자와 식별된 사용자 {#anonymous-users-and-identified-users}

Braze의 사용자는 일반적으로 두 가지 상태 중 하나에 해당합니다.

### 익명 사용자 {#anonymous-users}

[익명 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)란 앱이나 웹사이트와 상호작용했지만 아직 시스템에서 식별자(`external_id` 등)가 할당되지 않은 사용자를 말합니다.

- 익명 사용자는 Braze SDK가 초기화될 때 자동으로 생성됩니다
- 이벤트, 속성 및 메시지 인게이지먼트를 계속 추적할 수 있습니다
- 이 사용자는 채널 및 옵트인 상태에 따라 메시지를 받을 수 있습니다

#### 익명 사용자와 동의 {#anonymous-users-and-consent}

동의 정책을 준수하기 위해 Braze SDK를 동의 래퍼로 감싸야 하는 경우, 사용자가 동의하기 전에 익명 데이터를 수집할 수 있습니다. SDK가 초기화되면 익명 사용자 프로필이 생성되어 동의 요구 사항을 준수하면서 행동을 추적할 수 있습니다.

**익명 사용자에게 메시지 보내기:**
익명 사용자는 Braze SDK가 초기화된 상태인 한 메시지를 트리거하고 수신할 수 있습니다. 여기에는 다음이 포함됩니다:

- [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [푸시 알림]({{site.baseurl}}/user_guide/channels/push)(푸시 토큰이 등록된 경우)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)

그러나 사용자가 동의하지 않거나 동의를 철회할 때 SDK 초기화를 비활성화하거나 차단하면 해당 사용자에게는 SDK 트리거 채널이 작동하지 않습니다.

**동의 상태에 따라 사용자 타겟팅:**
동의 상태에 따라 사용자에게 메시지를 보내려면 프로필에 커스텀 사용자 속성(`has_marketing_consent` 등)을 설정합니다. 그런 다음 이 속성을 기반으로 Segments를 생성하고, 사용자가 Braze 외부에서 동의 설정을 변경하는 경우 이 값을 동기화 상태로 유지할 수 있습니다. 익명 사용자 타겟팅에 대한 자세한 내용은 [사용 사례]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#use-cases)를 참조하세요.

### 식별된 사용자 {#identified-users}

[식별된 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles)란 사용자가 제공한 `external_id`(예: 고객 ID 또는 계정 ID)와 연결된 사용자를 말합니다.

사용자를 식별하면 다음을 수행할 수 있습니다:

- 기기 및 세션 간 활동 병합
- 채널 전반에 걸쳐 일관된 메시지 전송
- 장기 사용자 데이터를 사용한 세분화 및 개인화
- API 및 통합을 통한 프로필 관리

익명 사용자가 나중에 식별되면 Braze는 [이 병합 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)에 따라 적격 데이터를 식별된 프로필에 병합합니다. 예를 들어 푸시 토큰과 메시징 기록이 이전되며, 익명 프로필의 많은 필드는 식별된 프로필에 아직 설정되지 않은 경우에만 병합됩니다. 값이 충돌하는 경우에는 식별된 프로필의 값이 유지됩니다.

## 채널을 통해 사용자에게 메시지 보내기 {#message-users-through-channels}

[채널]({{site.baseurl}}/user_guide/channels)은 Braze가 사용자에게 메시지를 전달하는 특정 방식입니다. 일반적인 채널에는 다음이 포함됩니다:

- [푸시 (웹 또는 모바일)]({{site.baseurl}}/user_guide/channels/push)
- [이메일]({{site.baseurl}}/user_guide/channels/email)
- [SMS, MMS, RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [배너]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [웹훅]({{site.baseurl}}/user_guide/channels/webhooks)

하나의 고객 프로필에는 이메일 주소와 모바일 기기 등 여러 채널이 연결될 수 있습니다. Braze는 이 모델을 활용하여 사용자에 대한 통합된 뷰를 유지하면서 여러 채널에 걸쳐 메시징을 조율합니다.

각 채널에는 고유한 전달 규칙, 옵트인 요구사항, 메타데이터가 있지만, 모두 동일한 고객 프로필에 연결됩니다.

## 사용자가 Braze에 진입하는 방법 {#ways-users-enter-braze}

사용자는 지원되는 통합 또는 채널을 통해 브랜드와 상호작용할 때마다 Braze에서 생성됩니다. 사용자가 추가되는 방식은 Braze를 어떻게 구현했는지에 따라 달라집니다.

{% tabs %}
{% tab 모바일 앱 %}
- 사용자가 앱을 처음 열면 Braze SDK가 사용자 프로필을 생성합니다.
- 기기와 푸시 토큰이 자동으로 등록됩니다.
- 이벤트와 속성을 즉시 기록할 수 있습니다.
{% endtab %}

{% tab 웹 %}
- 웹 SDK가 초기화될 때 사용자가 생성됩니다.
- 웹 푸시 구독은 브라우저를 메시징 채널로 등록합니다.
{% endtab %}

{% tab 이메일 및 SMS %}
- 데이터를 업로드하거나, API를 호출하거나, 옵트인을 수집할 때 사용자가 생성될 수 있습니다.
- 이메일 주소와 전화번호는 채널 식별자로 저장됩니다.
- 옵트인 상태는 채널별 및 지역별로 추적됩니다.
{% endtab %}

{% tab API 및 통합 %}
- [REST API]({{site.baseurl}}/api/endpoints/user_data) 또는 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)를 통해 사용자를 직접 생성하거나 업데이트할 수 있습니다.
- 외부 도구(고객 데이터 플랫폼, CRM, 데이터 웨어하우스 등)를 사용하여 사용자를 Braze에 자동으로 동기화할 수 있습니다.
{% endtab %}
{% endtabs %}

## 오디언스 데이터 소스 {#audience-data-sources}

Braze의 사용자 데이터는 일반적으로 여러 소스의 조합에서 수집됩니다.

{% tabs %}
{% tab 자동 수집 %}
Braze SDK는 다음과 같은 상황별 데이터를 자동으로 수집합니다:

- 기기 유형 및 OS
- 언어 및 시간대
- 앱 버전 및 세션 활동
{% endtab %}

{% tab 사용자 행동 %}
사용자가 앱이나 메시지와 상호작용하면, Braze는 다음을 기록합니다:

- [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events) (예: 구매 또는 기능 사용)
- 메시지 열람, 클릭 및 전환
- 세션 활동 및 인게이지먼트 추세
{% endtab %}

{% tab 자체 시스템 %}
다음을 사용하여 자체 도구의 데이터를 Braze로 전송할 수 있습니다:

- [REST API]({{site.baseurl}}/api/endpoints/user_data)
- [CSV 업로드]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- 예약된 데이터 동기화

여기에는 일반적으로 식별자, 계정 데이터 또는 과거 컨텍스트가 포함됩니다.
{% endtab %}
{% endtabs %}

### 사용자 제공 입력 {#user-provided-input}

사용자는 다음을 통해 직접 데이터를 제공할 수 있습니다:

- [환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- 양식 또는 설문조사 (SDK 또는 통합)
- 인앱 경험

### 통합 {#integrations}

Braze는 통합을 통해 [Segment]({{site.baseurl}}/partners/segment), 데이터 웨어하우스, 분석 기술 파트너와 같은 플랫폼과 연동되어 사용자 데이터가 고객 프로필로 자동으로 전달됩니다.

## 사용자 데이터 관리 {#manage-user-data}

여러 가지 방법으로 사용자 데이터를 추가, 업데이트 또는 삭제할 수 있습니다.

- **대시보드 도구**를 사용하여 수동 편집 또는 CSV 업로드
- **API**를 사용하여 실시간 또는 프로그래밍 방식으로 업데이트
- **SDK**를 사용하여 앱이나 사이트에서 직접 행동 데이터 수집
- **통합**을 사용하여 지속적인 데이터 동기화

다음과 같은 방법으로 데이터를 삭제할 수 있습니다.

- 속성 값 초기화
- 태그 제거
- 구독 상태 업데이트
- 로그아웃 시 사용자 초기화(익명 사용자 사용 사례)

## 오디언스 데이터 기능 {#audience-data-features}

사용자 데이터가 Braze에 들어오면 거의 모든 인게이지먼트 기능을 지원합니다. 사용자 데이터가 완전하고 정확할수록 다음 기능을 더욱 효과적으로 활용할 수 있습니다.

| 기능 | 설명 |
| ---- | ---- |
| [세분화]({{site.baseurl}}/user_guide/audience/segments) | 다음을 기반으로 오디언스를 생성합니다: {::nomarkdown}<ul><li>속성 및 커스텀 필드</li> <li>이벤트 및 행동</li> <li>메시지 인게이지먼트</li> <li>기기 및 채널 속성</li></ul>{:/} <br>Segments는 Campaigns 및 Canvases에서 재사용할 수 있습니다. |
| [개인화]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | 사용자 데이터를 활용하여 콘텐츠를 맞춤화합니다. 예: {::nomarkdown}<ul><li>메시지 본문의 이름 및 선호도</li> <li>동적 추천</li> <li>위치 또는 언어별 콘텐츠</li></ul>{:/} |
| 자동화 및 오케스트레이션 | 다음을 기반으로 메시지와 여정을 트리거합니다: {::nomarkdown}<ul><li>사용자 행동</li> <li>속성 변경</li> <li>시간 기반 조건</li></ul>{:/} |
| 크로스채널 조정 | 다음을 준수하면서 가장 적합한 채널로 사용자에게 도달합니다: {::nomarkdown}<ul><li>옵트인 상태</li> <li>빈도 제한</li> <li>채널 선호도</li></ul>{:/} |
| [분석 및 인사이트]({{site.baseurl}}/user_guide/analytics) | 다양한 오디언스의 행동을 다음 항목을 분석하여 파악합니다: {::nomarkdown}<ul><li>참여율</li> <li>전환 경로</li> <li>시간 경과에 따른 Segment 성과</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="오디언스 데이터 기능" }