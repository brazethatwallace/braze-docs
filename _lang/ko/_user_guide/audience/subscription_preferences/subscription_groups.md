---
nav_title: 구독 그룹
article_title: 구독 그룹
page_order: 4
description: "Braze 채널 전반에서 구독 그룹이 어떻게 작동하는지, 구독 그룹을 생성하고 관리하는 방법, 이메일, WhatsApp, 단문 메시지 서비스, MMS, RCS, LINE의 채널별 동작에 대해 알아보세요."
---

# 구독 그룹 {#subscription-groups}

> Braze 채널 전반에서 구독 그룹이 어떻게 작동하는지, 대시보드에서 구독 그룹을 생성하고 관리하는 방법, 채널별 규칙이 적용되는 곳에 대해 알아보세요.

구독 그룹은 채널 내 특정 발송 리소스 세트로부터 메시지를 수신할 수 있는 사용자를 제어합니다.

이메일의 경우, 구독 그룹은 글로벌 가입 상태 위에 적용되는 선택적 카테고리 필터입니다. 단문 메시지 서비스, WhatsApp, LINE의 경우, 구독 그룹은 모든 발송에 필수적인 오디언스 필터입니다. 이를 통해 뉴스레터 대 프로모션, 트랜잭션 단문 메시지 서비스 대 마케팅 단문 메시지 서비스 등 세분화된 옵트인 및 옵트아웃 옵션을 제공할 수 있으며, 글로벌 채널 가입 상태가 있는 경우 해당 상태를 변경하지 않습니다.

[구독 그룹 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups)를 사용하여 Braze 워크스페이스에 저장된 구독 그룹을 프로그래밍 방식으로 관리할 수 있습니다.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## 글로벌 가입 상태 대 구독 그룹 {#global-subscription-state-versus-subscription-groups}

일부 채널에는 글로벌 가입 상태와 구독 그룹이 모두 있습니다.

| 채널 | 글로벌 가입 상태 | 구독 그룹 |
| --- | --- | --- |
| 이메일 | 모든 이메일에 대해 옵트인, 가입됨 또는 가입 취소됨 | 이메일 내 선택적 카테고리(예: 뉴스레터 또는 프로모션) |
| 단문 메시지 서비스, MMS, RCS | 글로벌 단문 메시지 서비스 상태 없음; 가입은 그룹별로 관리 | 모든 발송에 필수; 각 그룹에 발송 전화번호 또는 RCS 발신자 포함 |
| WhatsApp | 글로벌 WhatsApp 상태 없음; 가입은 그룹별로 관리 | WhatsApp 통합 시 생성; 각 그룹이 발송 전화번호에 매핑됨 |
| LINE | 글로벌 LINE 상태 없음; 가입은 그룹별로 관리 | LINE 채널 통합별로 생성; LINE 앱에서의 팔로우 또는 언팔로우가 상태를 결정 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="글로벌 가입 상태 대 구독 그룹" }

사용자가 이메일에 글로벌로 가입되어 있으면서 특정 이메일 구독 그룹에서는 가입 취소된 상태일 수 있습니다. 단문 메시지 서비스의 경우, 사용자가 트랜잭션 그룹에는 가입되어 있으면서 프로모션 그룹에는 가입 취소된 상태일 수 있습니다.

## 구독 그룹 생성하기 {#create-a-subscription-group}

구독 그룹을 얻는 방법은 채널에 따라 다릅니다. 이메일 그룹은 대시보드에서 생성하고, 단문 메시지 서비스, MMS, RCS 그룹은 온보딩 중에 프로비저닝되며, WhatsApp과 LINE 그룹은 채널 통합 중에 생성됩니다. 채널별 프로비저닝 세부 정보는 [채널별 동작](#channel-specific-behavior)을 참조하세요.

### 이메일 {#email}

1. **오디언스** > **구독 그룹 관리**로 이동합니다.
2. **이메일 구독 그룹 만들기**를 선택합니다.
3. 이름과 설명을 입력합니다. 워크스페이스의 각 구독 그룹은 고유한 이름을 가져야 합니다. 이미 존재하는 이름을 입력하면 대시보드에 오류가 표시되고 그룹이 저장되지 않습니다.
4. **저장**을 선택합니다.

![구독 그룹 생성 필드.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

## 구독 그룹으로 세그먼팅하기 {#segment-with-subscription-groups}

Segment를 구성할 때 구독 그룹 필터를 추가하여 해당 그룹에 옵트인한 사용자를 타겟팅할 수 있습니다. 월간 뉴스레터, 쿠폰 프로그램, 멤버십 등급 및 기타 카테고리 기반 발송에 유용합니다.

!["Lapsed Users" Segment에서 "Weekly Emails" 구독 그룹에 속한 사용자를 필터링하여 타겟팅하는 예시.]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

## 구독 그룹 보관하기 {#archive-subscription-groups}

보관된 구독 그룹은 편집할 수 없으며 Segment 필터나 환경설정 센터에 더 이상 표시되지 않습니다. 활성 Campaign, Canvas 또는 Segment에서 Segment 필터로 사용 중인 그룹을 보관하면, 해당 참조를 제거할 때까지 오류가 표시됩니다.

**구독 그룹 관리**에서 그룹을 보관하려면 해당 그룹을 찾아 <i class="fa-solid fa-ellipsis-vertical" aria-label="더보기 메뉴 열기"></i> 메뉴에서 **보관**을 선택합니다.

Braze는 보관된 그룹으로의 메시징을 차단하므로, 보관된 구독 그룹을 신규 또는 활성 발송에 사용할 수 없습니다.

일부 채널에는 추가적인 보관 규칙이 있습니다. 워크스페이스 및 재통합 동작에 대해서는 [LINE 구독 그룹](#line-subscription-groups)을 참조하세요.

## 사용자의 구독 그룹 확인하기 {#check-a-users-subscription-groups}

- **고객 프로필:** [사용자 검색]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles)에서 프로필을 엽니다. **인게이지먼트** 탭에서 이메일, 단문 메시지 서비스, WhatsApp 및 관련 채널의 구독 그룹과 상태를 확인할 수 있습니다.
- **REST API:** [사용자의 구독 그룹 목록]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) 또는 [사용자의 구독 그룹 상태 목록]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) 엔드포인트를 사용합니다.

### 구독 그룹 상태 업데이트하기 {#update-subscription-group-status}

REST API, SDK, 사용자 가져오기, 고객 프로필, 이메일 환경설정 센터, Canvas의 User Update 단계 및 기타 채널별 플로우를 통해 사용자의 구독 그룹 멤버십을 업데이트할 수 있습니다. 정확한 방법은 채널에 따라 다릅니다. 각 [채널 섹션](#channel-specific-behavior) 및 단문 메시지 서비스 관련 타이밍 가이드는 [단문 메시지 서비스, MMS, RCS 구독 그룹]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#set-a-users-state)을 참조하세요.

## 환경설정 센터 {#preference-centers}

이메일 구독 그룹은 [이메일 환경설정 센터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)에 표시되어 사용자가 카테고리 수준의 이메일 옵트인을 한 곳에서 관리할 수 있습니다. 환경설정 센터를 구축할 때 활성 이메일 구독 그룹을 추가할 수 있으며, 레거시 환경설정 센터는 모든 활성 이메일 그룹을 자동으로 나열합니다.

단문 메시지 서비스 및 WhatsApp의 경우, REST API, 옵트인 플로우, 키워드(단문 메시지 서비스), 고객 프로필 및 각 [채널 섹션](#channel-specific-behavior)의 기타 채널별 방법을 통해 가입 상태를 관리합니다.

## 채널별 동작 {#channel-specific-behavior}

### 이메일 구독 그룹 {#email-subscription-groups}

이메일 구독 그룹은 [글로벌 이메일 가입 상태]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)(옵트인, 가입됨, 가입 취소됨) 위에 위치합니다. 글로벌 `unsubscribed` 상태의 사용자는 구독 그룹 멤버십에 관계없이 이메일을 수신하지 않습니다.

이메일 관련 세부 정보:

- **환경설정 센터:** 생성한 모든 이메일 구독 그룹을 환경설정 센터에 추가할 수 있습니다.
- **Campaign 분석:** Campaign의 **Email Message Performance** 페이지에서 **Subscription Groups**를 열어 해당 발송의 집계 가입 및 가입 취소 수를 확인할 수 있습니다.

#### 구독 그룹 크기 확인하기 {#viewing-subscription-group-sizes}

**구독 그룹 관리**에서 시계열 차트는 다음을 보고합니다.

- **구독 그룹 크기:** 특정 날짜에 해당 그룹에 가입된 사용자 수
- **구독 그룹 가입 취소 크기:** 특정 날짜에 해당 그룹에서 가입 취소된 사용자 수

이 수치는 글로벌 이메일 가입 상태가 아닌 해당 그룹 내 멤버십을 반영합니다. **Email Subscription Status is Unsubscribed** 필터를 사용하는 Segment와는 다를 수 있으며, 이 필터는 [글로벌 이메일 가입 상태]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)를 반영합니다.

오늘의 구독 그룹 크기는 기본적으로 계산되지 않습니다. 날짜 범위에 오늘이 포함된 경우 **Calculate today's statistics**를 선택하여 오늘의 값을 시계열에 추가합니다. 매우 큰 워크스페이스의 경우 Braze가 정확한 수치 대신 추정치를 표시할 수 있습니다.

푸터, 탈퇴 페이지 및 글로벌 이메일 가입 관리에 대해서는 [이메일 구독]({{site.baseurl}}/user_guide/channels/email/subscriptions)을 참조하세요.

### WhatsApp 구독 그룹 {#whatsapp-subscription-groups}

WhatsApp 구독 그룹은 기술 파트너 포털을 통해 워크스페이스에 [WhatsApp을 통합]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)할 때 생성됩니다.

| 상태 | 정의 |
| --- | --- |
| 가입됨 | 사용자가 비즈니스로부터 WhatsApp 메시지를 수신하겠다고 명시적으로 확인한 상태입니다. Braze 구독 API 또는 옵트인 플로우를 통해 가입할 수 있습니다. |
| 가입 취소됨 | 사용자가 옵트인하지 않았거나 그룹에서 제거된 상태입니다. 가입 취소된 사용자는 해당 그룹의 전화번호로부터 WhatsApp 메시지를 수신하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp 가입 상태" }

WhatsApp은 명시적 옵트인을 요구합니다. 이 채널에서는 옵트인 키워드가 지원되지 않으므로, 동의 및 가입 상태를 직접 관리해야 합니다. 옵트인 및 옵트아웃 플로우에 대해서는 [WhatsApp 옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)을 참조하세요.

보관 단계, Canvas 업데이트, REST API 예시에 대해서는 [WhatsApp 구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)을 참조하세요.

### 단문 메시지 서비스, MMS, RCS 구독 그룹 {#sms-mms-and-rcs-subscription-groups}

단문 메시지 서비스, MMS, RCS 구독 그룹은 해당 채널에서 발송하기 위한 기반입니다. 각 그룹은 짧은 코드, 긴 코드, 영숫자 발신자 ID 또는 RCS 인증 발신자와 같은 [발송 엔티티]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)의 모음이며, 특정 메시징 목적(예: 트랜잭션 대 프로모션)에 사용됩니다.

| 상태 | 정의 |
| --- | --- |
| 가입됨 | 사용자가 구독 API, 옵트인 키워드 또는 기타 지원되는 플로우를 통해 해당 구독 그룹에서 메시지를 수신하도록 가입한 상태입니다. [이중 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)이 활성화된 경우, 사용자는 가입 상태로 업데이트되기 전에 확인해야 합니다. |
| 가입 취소됨 | 사용자가 키워드 또는 API 업데이트를 통해 옵트아웃한 상태입니다. 가입 취소된 사용자는 해당 그룹의 발신자로부터 단문 메시지 서비스, MMS 또는 RCS를 수신하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="단문 메시지 서비스 및 RCS 가입 상태" }

단문 메시지 서비스 또는 RCS 메시지를 발송할 때 작성기에서 구독 그룹을 선택합니다. Braze는 가입된 사용자만 타겟팅되도록 오디언스 필터를 추가합니다. Braze는 선택한 그룹에 가입되지 않은 사용자에게 단문 메시지 서비스 또는 RCS를 발송하지 않습니다. 단문 메시지 서비스 테스트 메시지를 수신하려면 수신자가 테스트용으로 선택한 구독 그룹에 속해 있어야 합니다. 자세한 내용은 [단문 메시지 서비스 FAQ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages)를 참조하세요.

단문 메시지 서비스 구독 그룹은 온보딩 중에 프로비저닝됩니다. MMS 태그, RCS 발신자 설정, 지리적 권한, RCS 마이그레이션 및 고급 옵트아웃 처리에 대해서는 [단문 메시지 서비스, MMS, RCS 구독 그룹]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)을 참조하세요.

### LINE 구독 그룹 {#line-subscription-groups}

각 LINE 구독 그룹은 하나의 LINE 채널 통합에 연결됩니다.

| 상태 | 정의 |
| --- | --- |
| 가입됨 | 사용자가 LINE 앱에서 LINE 채널을 팔로우한 상태입니다. 통합 후 사용자가 팔로우하면 Braze가 자동으로 가입 처리합니다. |
| 가입 취소됨 | 사용자가 채널을 팔로우하지 않았거나 언팔로우한 상태입니다. 가입 취소된 사용자는 해당 그룹으로부터 LINE 메시지를 수신하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE 가입 상태" }

LINE이 가입 상태의 원본 소스입니다. Braze는 팔로우 및 언팔로우 이벤트를 처리하여 프로필을 업데이트합니다.

LINE 구독 그룹은 워크스페이스 간에 이동할 수 없습니다. 구독 그룹을 보관하고 다른 워크스페이스에서 채널을 다시 통합하면, Braze는 대상 워크스페이스에 새 구독 그룹을 생성합니다.

보관 동작, 사용자 매칭 및 통합 단계에 대해서는 [LINE 구독 그룹]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups) 및 [LINE 설정]({{site.baseurl}}/user_guide/channels/line/line_setup)을 참조하세요.