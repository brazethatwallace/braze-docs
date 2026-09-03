---
nav_title: 더블 옵트인을 통한 이메일 가입
article_title: 더블 옵트인을 통한 이메일 가입
page_order: 2
page_type: reference
description: "이 문서에서는 BRAZE 캔버스 템플릿을 사용하여 인증된 이메일 가입으로 도달 범위를 확장하는 방법을 설명합니다."
tool: Canvas
---

# 더블 옵트인을 통한 이메일 가입 {#email-sign-up-with-double-opt-in}

> 더블 옵트인을 통한 이메일 가입 템플릿을 사용하여 인증된 이메일 가입으로 도달 범위를 확장하세요. 신규 사용자를 타겟팅하여 이메일을 수집하고, 구독을 확인하며, 프로모션 코드를 받을 수 있도록 하나의 매끄러운 여정으로 안내합니다.

이 문서에서는 사용자 라이프사이클의 고려 단계를 위해 설계된 **더블 옵트인을 통한 이메일 가입** 템플릿의 사용 사례를 안내합니다. 이 과정을 마치면 사용자가 세션을 시작하거나 온보딩을 완료하지 않았을 때 이메일과 인앱 메시지를 발송하는 Canvas를 만들 수 있습니다.

## 필수 조건 {#prerequisites}

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 사용자의 이메일을 수집하는 페이지와 성공 메시지를 전달하는 페이지가 포함된 [멀티 페이지 인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page).
- 사용자가 이메일 주소를 인증할 수 있는 확인 이메일.
- 더블 옵트인한 사용자를 위한 독점 프로모션 코드가 포함된 환영 이메일.

## 필요에 맞게 템플릿 조정하기 {#tailoring-the-template-to-your-needs}

칼로리 추적, 디지털 운동 수업, 플래시몹 마라톤 등의 기능으로 유명한 건강 앱 Steppington에서 일하고 있다고 가정해 보겠습니다. Canvas를 만들기 전에, 사용자가 앱을 처음 사용한 경험과 인상을 파악하기 위한 일련의 흥미로운 질문이 포함된 [멀티 페이지 인앱 및 인브라우저 메시지를 설정]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page)합니다.

템플릿에 접근하려면 새 Canvas를 만들 때 **Use a Canvas template** > **Braze templates**를 선택합니다. 그런 다음 **Email sign-up with double opt-in** 옆에 있는 **Apply Template**을 선택합니다. 이제 필요에 맞게 템플릿을 살펴보겠습니다.

### 1단계: 세부 정보 설정하기 {#step-1-set-up-the-details}

목표에 맞게 Canvas 세부 정보를 조정합니다.

1. 템플릿 이름 옆의 **Edit**를 선택합니다.

![Canvas의 현재 제목과 설명.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Canvas 이름을 업데이트하여 사용자가 앱을 처음 사용할 때 신규 사용자를 타겟팅하기 위한 Canvas임을 명시합니다.
3. 설명을 업데이트하여 이 Canvas에 사용자가 더블 옵트인할 수 있는 개인화된 메시지가 포함되어 있음을 설명합니다.
4. Canvas 홈 페이지에서 필터링할 수 있도록 **Email** 태그를 추가합니다.

![Canvas의 새 이름, 설명 및 태그.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### 2단계: 전환 이벤트 할당하기 {#step-2-assign-conversion-events}

다음으로 전환 이벤트를 할당합니다. 전환 이벤트는 Canvas의 성공을 측정하는 데 사용할 수 있는 측정기준 유형입니다. **Conversion event type**에서 **Performs Custom Event**를 선택합니다. 그런 다음 **Custom event name**에서 **email_opt_in**을 선택합니다.

![이메일 옵트인 전환 이벤트 유형에 대한 "전환 이벤트 할당" 섹션.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

가장 최근 사용자를 타겟팅하려면 템플릿의 전환 기한을 3일로 유지합니다.

### 3단계: 진입 스케줄 조정하기 {#step-3-tailor-the-entry-schedule}

사용자가 앱에서 세션을 시작할 때 Canvas에 진입하도록 진입 스케줄을 **Action-Based**로 유지합니다. 이렇게 하면 적시에 참여를 유도하여 관계를 구축할 수 있습니다.

또한 사용자가 세션을 시작할 때만 Canvas에 진입하도록 **Action Based Options**를 그대로 유지하는 것을 고려하세요.

![세션을 시작하는 사용자를 Canvas에 진입시키는 액션 기반 진입 스케줄.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

**항목 Window**에서 **Started Time (Required)**을 원하는 날짜와 시간으로 업데이트합니다.

![시작 시간이 2025년 1월 16일 오후 12:30인 진입 기간. 사용자는 현지 시간대에 따라 이 메시지에 진입합니다.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### 4단계: 타겟 오디언스 선택하기 {#step-4-select-the-target-audience}

고객 프로필에 이메일 주소가 없는 Steppington 사용자를 타겟 오디언스로 정의합니다. 템플릿의 기본 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)인 `Email Available is false`를 유지합니다.

!["Email Available is false" 필터가 적용된 진입 오디언스.]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### 5단계: 발송 설정 선택하기 {#step-5-select-your-send-settings}

기본 구독 설정을 유지하여 메시지나 알림 수신에 가입했거나 옵트인한 사용자에게만 발송하고, 나머지 설정(최대 게재빈도 설정, 방해금지 시간, 시드 그룹)은 건너뜁니다.

![가입했거나 옵트인한 사용자에게만 발송하는 기본 발송 옵션.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### 6단계: Canvas 커스터마이즈하기 {#step-6-customize-your-canvas}

다음으로 사용자에게 발송할 채널과 콘텐츠를 커스터마이즈하여 Canvas를 구축합니다. 이메일 가입 인증에 집중하고 있으므로 템플릿의 캔버스 단계와 채널을 추가하거나 제거할 필요가 없습니다.

1. **Email Sign-up**이라는 이름의 첫 번째 메시지 단계를 선택합니다. 여기에서 멀티 페이지 인앱(및 인브라우저) 메시지를 사용하도록 템플릿을 업데이트합니다.

- 페이지 1은 이메일을 수집합니다.
- 페이지 2는 확인 메시지를 표시합니다.

![사용자 이메일을 수집하고 성공 메시지를 표시하는 인앱 메시지의 두 페이지.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2. 여기에서 **Subscribed** 행동 경로 단계를 그대로 유지합니다. 이 단계는 1일 기간 내에 사용자를 두 그룹으로 나눕니다:

- 이메일로 Steppington에 가입한 사용자
- 이메일로 Steppington에 가입하지 않은 사용자

{:start="3"}
3. 다음으로 **Verify Email** 메시지 단계의 이메일 본문을 브랜드 확인 이메일로 교체합니다. 이렇게 하면 가입한 사용자에게 이메일을 발송하여 이메일 주소를 확인하고 메시지 수신에 옵트인하도록 안내합니다.
4. **Confirm Subscription** 행동 경로 단계를 그대로 유지합니다. 이 단계는 1주일 기간 내에 이메일을 확인한 사용자와 확인하지 않은 사용자로 추가 분류합니다.
5. 마지막으로 독점 프로모션 코드가 포함된 확인 이메일로 **Welcome + Discount** 메시지 단계를 업데이트합니다.

{% alert note %}
**Verify Email** 메시지 단계는 사용자의 두 번째 세션에서 트리거됩니다. 첫 번째 세션 시작 이벤트가 Canvas를 트리거하지만, 사용자가 두 번째 인앱 메시지를 트리거할 자격을 얻으려면 첫 번째 **Email Sign-up** 메시지 단계에 도달한 후 두 번째 세션 시작이 필요하기 때문입니다.
{% endalert %}

### 7단계: Canvas 테스트 및 시작하기 {#step-7-test-and-launch-your-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **Launch Canvas**를 선택하여 시작합니다.

{% alert tip %}
Canvas를 시작하기 전후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)를 확인하세요.
{% endalert %}