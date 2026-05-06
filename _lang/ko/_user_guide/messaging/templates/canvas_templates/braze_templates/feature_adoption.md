---
nav_title: 기능 도입
article_title: 기능 도입
page_order: 3
page_type: reference
description: "이 문서에서는 Braze Canvas 템플릿을 사용하여 혜택과 사용 팁을 강조하는 시의적절한 개인화된 메시지를 전달하는 방법을 설명합니다."
tool: Canvas
---

# 기능 도입 {#feature-adoption}

> 이 템플릿은 새로운 기능, 기존 제품, 추가 서비스 또는 고객이 경험하기를 원하는 기타 영역의 사용을 촉진하기 위해 설계되었습니다. 개인화된 커뮤니케이션과 체계적인 메시지 세트를 활용하여 사용자에게 새로운 기능을 원활하게 소개하고 귀중한 피드백을 수집할 수 있습니다.

이 문서에서는 사용자 라이프사이클의 리텐션 및 로열티 단계를 위한 **기능 도입** 템플릿의 사용 사례를 안내합니다. 이 문서를 마치면 사용자가 새로운 기능을 사용하도록 유도하고 사용자 감정을 수집하는 사용자 여정을 커스텀할 수 있습니다.

## 필수 조건 {#prerequisites}

이 템플릿을 성공적으로 사용하려면 사용자가 기능을 사용한 시점을 참조하는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)가 필요합니다.

## 필요에 맞게 템플릿 조정하기 {#tailoring-the-template-to-your-needs}

Calorie Rocket이라는 음식 배달 앱에서 일하고 있으며, 최근 반복 음식 배달을 예약하는 기능인 Cruise Control을 출시했고, 더 많은 사용자가 이 새로운 기능을 도입하도록 유도하고 싶다고 가정해 보겠습니다. 이 예시에서는 사용자가 Cruise Control 기능을 사용한 시점을 추적하기 위해 커스텀 이벤트 `scheduled_delivery`를 사용합니다.

재입고 템플릿에 액세스하려면 새 Canvas를 생성할 때 **Canvas 템플릿 사용** > **Braze 템플릿**을 선택합니다. 그런 다음 **기능 도입** 옆에 있는 **템플릿 적용**을 선택합니다. 이제 필요에 맞게 템플릿을 살펴보겠습니다.

### 1단계: 세부 정보 설정 {#step-1-set-up-the-details}

Canvas 세부 정보를 목표에 맞게 조정해 보겠습니다.

1. 템플릿 이름 옆에 있는 **편집**을 선택합니다.

![Canvas의 현재 제목과 설명.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2. Canvas 이름을 업데이트하여 사용자 피드백을 수집하기 위해 사용자를 타겟팅하는 Canvas임을 명시합니다.
3. 설명을 업데이트하여 새로운 Cruise Control 기능에 대한 사용자 피드백 제출을 유도하고 사용자 감정을 추적하기 위한 Canvas임을 명시합니다.
4. Canvas 홈 페이지에서 필터링할 수 있도록 **기능 도입** 태그를 추가합니다.

![Canvas의 새 이름과 설명. 새 설명에는 'Cruise Control(반복 음식 배달 예약 기능)의 도입 및 사용자 감정을 추적하기 위한 기능 도입 Canvas'라고 명시되어 있습니다.]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### 2단계: 전환 이벤트 할당 {#step-2-assign-a-conversion-event}

다음으로, 기능 도입을 나타내는 전환 이벤트를 Canvas에 추가해 보겠습니다. 이를 통해 나중에 사용자 여정에서 실험 경로를 맞춤 설정할 수 있습니다.

1. **전환 이벤트 할당**에서 **전환 이벤트 추가**를 선택합니다.
2. **주요 전환 이벤트 - A**에서 **전환 이벤트 유형**으로 **커스텀 이벤트 수행**을 선택합니다.
3. 커스텀 이벤트 `scheduled_delivery`를 선택합니다.
4. 전환 기한은 3일로 유지합니다.

![Canvas의 전환 이벤트 창.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### 3단계: 진입 스케줄 조정 {#step-3-tailor-the-entry-schedule}

사용자가 Cruise Control을 도입하도록 유도하는 것이 목표이지만, 메시지가 너무 빈번하지 않기를 원합니다. 따라서 이 Canvas를 스케줄 전달로 유지하고 **시간 기반 옵션** 섹션을 다음과 같이 조정합니다.

1. **진입 빈도**를 **주간**으로 업데이트합니다.
2. 반복 설정은 그대로 유지합니다.
3. 주 초에 사용자를 타겟팅하기 위해 **월요일**을 선택합니다.
4. Canvas의 시작 시간을 선택합니다.
5. **종료 매개변수**를 업데이트하여 연말에 Canvas를 종료합니다.

사용자가 현지 시간대에 Canvas에 진입할 수 있도록 하는 옵션은 유지합니다.

### 4단계: 타겟 오디언스 선택 {#step-4-select-the-target-audience}

이제 템플릿에서 다음 세부 정보를 업데이트하여 타겟 오디언스를 설정해 보겠습니다.

1. **모든 사용자** Segment를 선택합니다.
2. 템플릿의 추가 필터를 제거합니다.
3. 커스텀 이벤트를 사용하여 다음 필터를 생성합니다: `Has scheduled_delivery for exactly 0 times`. 이를 통해 이미 기능을 사용한 사용자가 Canvas에 진입하는 것을 제외할 수 있습니다.

![Cruise Control을 사용하지 않은 모든 사용자를 위한 Segment.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4. Calorie Rocket이 이전에 일부 사용자에게 새로운 기능 Cruise Control의 베타 테스트를 허용했음을 고려하여, 이러한 사용자가 Canvas에 진입하지 않도록 종료 기준을 업데이트합니다.

### 5단계: 발송 설정 선택 {#step-5-select-your-send-settings}

기본 구독 설정을 유지하여 메시지나 알림 수신에 가입하거나 옵트인한 사용자에게만 발송하고, 나머지 설정(최대 게재빈도 설정, 방해금지 시간, 시드 그룹)은 건너뜁니다.

### 6단계: Canvas 커스텀하기 {#step-6-customize-your-canvas}

#### 행동 경로 구축 {#build-out-the-action-path}

다음으로, 사용자가 새로운 기능에 관심이 있는지 나타내기 위한 첫 번째 행동 경로 단계를 구축해 보겠습니다. 템플릿을 다음과 같이 조정합니다.

1. Cruise Control 기능은 주문이 장바구니에 추가된 후에만 사용할 수 있으므로, 첫 번째 동작 그룹의 이름을 **Added to cart**로 지정하고 커스텀 이벤트로 `added_to_cart`를 선택합니다.

![동작 그룹 이름이 "Added to cart"로 설정되고 "Perform Custom Event"가 "added_to_cart"로 설정된 화면.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2. 두 번째 동작 그룹 **Taken Tour**는 사용자가 앱 투어를 완료했는지 평가하기 위한 것이므로 그대로 유지합니다. 완료한 경우 두 번째 경로로 진행됩니다.
3. 후속 행동 경로인 **Assess Usage**에서 **Used Feature >3x**를 **Viewed Cruise Control settings**로 교체합니다.
4. **Perform Custom Event** 드롭다운을 선택한 다음 커스텀 이벤트로 `scheduled_delivery`를 선택합니다.

![동작 그룹 이름이 'Used Feature >3x'로 설정되고 'Perform Custom Event'가 'scheduled_delivery'로 설정된 화면.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### 피드백 설문조사 설정 {#set-up-feedback-survey}

다음으로, **Feedback Survey**라는 메시지 단계로 이동하여 사용자가 Cruise Control을 처음 사용한 후 작성할 피드백 설문조사를 포함합니다. 사용자를 위한 설문조사 응답 옵션은 다음과 같습니다.

- **Loved it!**
- **Not for me.**

1. 두 가지 설문조사 선택지에 대해 Cruise Control에 대한 피드백을 캡처하고 추적하기 위한 커스텀 속성으로 **Experience Feedback**을 선택합니다. 이 커스텀 속성에는 설문조사 응답을 나타내는 두 가지 값(`good` 및 `bad`)이 있습니다.
2. 속성 값을 설문조사 옵션과 일치하도록 업데이트합니다. 이를 통해 사용자의 응답을 추적할 수 있습니다.

### 7단계: Canvas 테스트 및 시작 {#step-7-test-and-launch-your-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **Canvas 시작**을 선택하여 Canvas를 시작합니다. 이제 개인화된 사용자 여정으로 사용자를 타겟팅하여 새로운 기능 Cruise Control 도입을 유도할 수 있습니다.

{% alert tip %}
Canvas를 시작하기 전후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)를 확인하세요.
{% endalert %}