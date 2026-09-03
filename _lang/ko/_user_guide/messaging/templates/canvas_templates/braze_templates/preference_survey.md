---
nav_title: 선호도 설문조사를 활용한 온보딩
article_title: 선호도 설문조사를 활용한 온보딩
page_order: 5.5
page_type: reference
description: "이 문서에서는 BRAZE 캔버스 템플릿을 사용하여 신규 사용자에게 브랜드를 소개하고 선호도를 수집하여 장기적으로 참여를 유지하는 가이드 온보딩 플로우를 통해 초기 도입을 촉진하는 방법을 설명합니다."
tool: Canvas
---

# 선호도 설문조사를 활용한 온보딩 {#onboarding-with-preferences-survey}

> 선호도 설문조사를 활용한 온보딩 템플릿을 사용하여 신규 사용자를 타겟팅하는 가이드 온보딩 워크플로우를 만들어 보세요. 사용자에게 브랜드를 소개하고, 시작을 도와주며, 선호도를 수집하여 장기적으로 참여를 유지할 수 있습니다.

이 문서에서는 사용자 라이프사이클의 고려 단계를 위해 설계된 **선호도 설문조사를 활용한 온보딩** 템플릿의 사용 사례를 안내합니다. 완료하면 사용자가 세션을 시작할 때와 온보딩을 완료하지 않았을 때 이메일과 인앱 메시지를 발송하는 Canvas를 만들 수 있습니다.

## 필수 조건 {#prerequisites}

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 사용자에게 온보딩을 시작하도록 안내하는 환영 이메일
- 온보딩을 완료한 사용자를 위한 앱 시작 팁이 포함된 후속 이메일
- 사용자에게 온보딩을 완료하도록 안내하는 후속 이메일
- 사용자 선호도를 파악하기 위한 여러 질문이 포함된 [설문조사]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/simple_survey)

## 필요에 맞게 템플릿 맞춤 설정하기 {#tailoring-the-template-to-your-needs}

사람들을 원하는 곳으로 데려다주는 온디맨드 차량 공유 앱인 StyleRyde에서 일하고 있다고 가정해 보겠습니다. Canvas를 만들기 전에, 사용자의 첫 번째 앱 탑승 경험과 인상을 파악하기 위한 일련의 흥미로운 질문이 포함된 [간단한 설문조사를 설정]({{site.baseurl}}/user_guide/data/activation/catalogs/create)합니다.

템플릿에 접근하려면 새 Canvas를 만들 때 **Use a Canvas template** > **Braze templates**를 선택합니다. 그런 다음 **Onboarding with preferences survey** 옆에 있는 **Apply Template**을 선택합니다. 이제 필요에 맞게 템플릿을 살펴보겠습니다.

### 1단계: 세부 정보 설정하기 {#step-1-set-up-the-details}

목표에 맞게 Canvas 세부 정보를 조정해 보겠습니다.

1. 템플릿 이름 옆의 **Edit**를 선택합니다.

![Canvas의 현재 제목과 설명.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Canvas 이름을 업데이트하여 신규 사용자가 앱을 처음 사용할 때 타겟팅하기 위한 Canvas임을 명시합니다.
3. 설명을 업데이트하여 이 Canvas에 개인화된 메시징이 포함되어 있음을 설명합니다.
4. Canvas 홈 페이지에서 필터링할 수 있도록 **Onboarding** 태그를 추가합니다.

![Canvas의 새 이름, 설명 및 태그.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### 2단계: 전환 이벤트 할당하기 {#step-2-assign-conversion-events}

**주요 전환 Event - A**를 **Performs Custom Event**로 업데이트합니다. 그런 다음 커스텀 이벤트로 **Last Used App**을 선택합니다.

![전환 이벤트의 선택된 커스텀 이벤트 이름으로 Last Used App이 표시됨.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### 3단계: 진입 스케줄 맞춤 설정하기 {#step-3-tailor-the-entry-schedule}

사용자가 앱에서 세션을 시작할 때 Canvas에 진입하도록 진입 스케줄을 **Action-Based**로 유지하겠습니다. 이렇게 하면 적시에 참여를 유도하며 관계를 구축할 수 있습니다.

이 섹션에서 **항목 Window**를 원하는 날짜와 시간으로 조정하는 한 가지 업데이트를 하겠습니다.

![시작 시간이 2025년 1월 30일 오후 12시로 설정된 "진입 기간" 섹션.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### 4단계: 타겟 오디언스 선택하기 {#step-4-select-the-target-audience}

StyleRyde 앱을 처음 사용한 지 1일 미만인 사용자를 타겟팅하도록 타겟 오디언스를 그대로 유지하겠습니다.

![진입 오디언스를 타겟팅하기 위해 "이 앱을 처음 사용한 지 1일 미만" 필터가 선택됨.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### 5단계: 발송 설정 선택하기 {#step-5-select-your-send-settings}

기본 구독 설정을 유지하여 메시지 또는 알림 수신에 가입하거나 옵트인한 사용자에게만 발송하고, 방해금지 시간을 켜둔 상태로 다른 설정(최대 게재빈도 설정 및 시드 그룹)은 건너뛰겠습니다.

![가입 또는 옵트인한 사용자에 대한 구독 설정과 오전 12시에서 오후 8시 사이의 방해금지 시간이 켜진 "발송 설정" 섹션.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### 6단계: Canvas 커스터마이즈하기 {#step-6-customize-your-canvas}

이제 사용자에게 발송할 콘텐츠를 커스터마이즈하여 Canvas를 구축하겠습니다.

1. 첫 번째 메시지 단계인 **Welcome Email**에서 StyleRyde 환영 이메일을 포함하도록 이 단계를 업데이트합니다.
2. 다음으로, 행동 경로 단계를 그대로 유지합니다. 이 단계는 3일 기간 내에 사용자를 두 그룹으로 나눕니다:

- 세션을 시작했거나 온보딩 이메일을 클릭한 사용자
- 세션을 시작하지 않았거나 온보딩 이메일을 클릭하지 않은 사용자

![세션을 시작한 사용자를 위한 경로와 다른 모든 사용자를 위한 경로로 나뉜 행동 경로 단계.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

여기서부터 앞서 언급한 그룹에 따라 사용자와 메시징을 타겟팅하겠습니다.

#### 참여한 사용자 타겟팅하기 {#target-your-engaged-users}

첫 번째 메시지 단계에서 세션을 시작했거나 온보딩 이메일에 참여한 사용자를 위해, **Getting Started Tips** 메시지 단계를 업데이트하여 신규 StyleRyde 사용자를 위한 필수 여행 및 안전 팁을 포함합니다.

사용자가 온보딩을 완료하면 Canvas에서 나가게 됩니다.

다음으로, **Content Preferences Survey** 메시지 단계를 업데이트하여 사용자가 향후 어떤 주제에 대한 정보를 받고 싶은지 선택하도록 안내하는 선호도 설문조사를 포함합니다.

![관심 있는 항목을 모두 선택하도록 안내하는 선호도 설문조사 미리보기.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### 온보딩을 시작하지 않은 사용자 넛지하기 {#nudge-users-who-havent-started-onboarding}

나머지 사용자를 위해, **Winback Nudge** 메시지 단계를 후속 이메일로 업데이트하여 사용자에게 온보딩을 완료하도록 안내합니다.

재참여를 위한 마지막 단계로, **Step 2**의 이름을 **Final Winback Nudge**로 변경하고 신규 사용자에게 온보딩을 완료하도록 안내하는 인앱 메시지로 단계를 업데이트합니다.

### 7단계: Canvas 테스트 및 시작하기 {#step-7-test-and-launch-your-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후, **Launch Canvas**를 선택하여 시작합니다.

{% alert tip %}
Canvas를 시작하기 전후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)를 확인하세요.
{% endalert %}