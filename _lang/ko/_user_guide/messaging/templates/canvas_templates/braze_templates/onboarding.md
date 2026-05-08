---
nav_title: 온보딩
article_title: 온보딩
page_order: 5
page_type: reference
description: "이 문서에서는 Braze Canvas 템플릿을 사용하여 강력한 초기 도입을 촉진하고 사용자와의 지속적인 관계를 장려하는 온보딩 여정을 만드는 방법을 설명합니다."
tool: Canvas
---

# 온보딩 {#onboarding}

> 이 온보딩 템플릿으로 사용자의 여정을 시작하세요. 이 템플릿은 강력한 초기 도입을 촉진하고 사용자와의 지속적인 관계를 장려하도록 설계되었습니다. 개인화된 커뮤니케이션과 체계적인 메시지 세트를 활용하여 사용자에게 브랜드를 자연스럽게 소개하고 지속적인 관계의 시작을 열 수 있습니다.

이 문서에서는 사용자 라이프사이클의 고려 단계를 위한 **온보딩** 템플릿의 사용 사례를 안내하여 신규 사용자를 위한 원활한 온보딩 여정을 만드는 방법을 설명합니다. 이 문서를 마치면 이 Braze Canvas 템플릿을 신규 사용자를 위한 개인화된 메시지로 커스터마이즈할 수 있게 됩니다.

## 필수 조건 {#prerequisites}

이 템플릿을 사용하기 전에 Canvas에서 참조할 다음 [이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template/)을 만들어야 합니다:

- 앱의 모든 사용자에게 보내는 환영 이메일
- 앱 사용 팁이 포함된 이메일
- 사용자 설문조사가 포함된 피드백 이메일

## 필요에 맞게 템플릿 조정하기 {#tailoring-the-template-to-your-needs}

PantsLabyrinth에서 일하고 있으며, 사용자 참여를 높이고 사용자와의 신뢰와 로열티를 구축하며 지속적인 참여를 유도하는 것이 목표라고 가정해 보겠습니다. 이를 위해 아직 앱과 상호작용하지 않은 신규 사용자를 타겟팅하는 메시지를 작성하는 데 집중하려고 합니다.

온보딩 템플릿에 접근하려면 새 Canvas를 만들 때 **Canvas 템플릿 사용** > **Braze 템플릿**을 선택합니다. 그런 다음 **온보딩** 옆에 있는 **템플릿 적용**을 선택합니다. 이 템플릿을 사용 사례에 맞게 커스터마이즈해 보겠습니다.

### 1단계: 세부 정보 설정하기 {#step-1-set-up-the-details}

목표를 반영하도록 Canvas 세부 정보를 조정해 보겠습니다.

1. 템플릿 이름 옆의 **편집**을 선택합니다.

![Canvas의 현재 제목과 설명.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Canvas 이름을 업데이트하여 신규 사용자 온보딩용 Canvas임을 명시합니다.
3. 설명을 업데이트하여 사용자와의 신뢰와 로열티를 촉진하는 사용자 여정을 매핑하는 Canvas임을 명시합니다.
4. **온보딩** 태그를 추가하여 Canvas 홈 페이지에서 필터링할 수 있도록 합니다.

![Canvas의 새 이름, 설명 및 태그.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### 2단계: 전환 이벤트 할당하기 {#step-2-assign-your-conversion-events}

다음으로 전환 이벤트를 할당해 보겠습니다. 전환 이벤트는 Canvas의 성공을 측정하는 데 사용할 수 있는 측정기준 유형입니다. **커스텀 이벤트 이름**에서 커스텀 이벤트로 **Email Click**을 선택합니다.

![주요 전환 이벤트 - A, 전환 유형 "커스텀 이벤트 수행", 커스텀 이벤트 이름 "Email Click". 4일의 전환 기한이 있습니다.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

이는 신규 사용자가 환영 이메일을 클릭할 수 있는 기간이 최대 4일이라는 것을 의미합니다. 이 경우 신규 사용자가 PantsLabyrinth에 참여하고 시즌별 의류 정기 배송을 구독하도록 긴박감을 느끼게 하려고 합니다.

### 3단계: 진입 스케줄 설정하기 {#step-3-set-an-entry-schedule}

목표가 PantsLabyrinth의 신규 사용자를 타겟팅하는 것이므로 Canvas를 액션 기반으로 유지합니다. **세션 시작**에서 **모든 앱에서 세션 시작**을 선택하여 모든 앱에서 세션을 시작하는 사용자가 Canvas에 진입할 수 있도록 합니다.

다음으로 **진입 기간**을 조정하여 사용자가 Canvas에 진입할 수 있는 시기를 결정합니다. 10월 말에 PantsLabyrinth 구독 출시가 예정되어 있다고 가정해 보겠습니다. 여기서 시작 시간을 **2024/10/28 오전 8:00**으로 설정합니다. 선택적으로 사용자가 현지 시간대에 Canvas에 진입하도록 할 수도 있습니다.

![시작 시간이 2024년 10월 28일 오전 8시인 진입 기간. 사용자는 현지 시간대에 이 메시지에 진입합니다.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### 4단계: 오디언스 타겟팅하기 {#step-4-target-your-audience}

적절한 오디언스를 타겟팅하면 신규 사용자와 효과적으로 참여할 수 있습니다. 예를 들어, 이 템플릿은 1일 이내에 앱을 처음 사용한 모든 사용자를 타겟팅하며, 이는 우리의 사용 사례에 적합합니다. 따라서 이 섹션은 그대로 유지합니다.

### 5단계: 발송 설정 구성하기 {#step-5-set-send-settings}

기본값으로 이 Canvas는 가입되었거나 옵트인한 사용자에게 발송되며 최대 게재빈도 설정 규칙을 따릅니다. 이 설정은 그대로 유지합니다.

### 6단계: Canvas 커스터마이즈하기 {#step-6-customize-your-canvas}

이제 템플릿 단계를 커스터마이즈하여 Canvas를 구축해 보겠습니다.

#### 환영 이메일 설정하기 {#set-up-the-welcome-email}

1. "Welcome Email"이라는 메시지 단계를 선택합니다.
2. **메시지 편집**을 선택하여 템플릿의 이메일을 환영 이메일로 교체합니다.
3. **완료**를 선택합니다.

이제 사용자가 앱에서 세션을 시작한 후 이 환영 이메일을 받게 됩니다. 반복적인 메시지로 사용자에게 부담을 주지 않기 위해 사용자 여정의 일부로 지연 단계를 사용하는 것을 권장합니다.

#### 오디언스 경로 커스터마이즈하기 {#customize-the-audience-path}

**Audience Split**이라는 오디언스 경로 단계에서 참여 사용자에 대한 필터를 커스터마이즈할 수 있습니다. 템플릿에서 필터는 **Welcome Email 단계의 이메일을 클릭함**이며, 이는 사용자가 환영 이메일을 클릭한 사용자와 클릭하지 않은 사용자의 두 그룹으로 나뉜다는 것을 의미합니다.

![참여 사용자를 위한 경로와 다른 모든 사용자를 위한 경로가 있는 Audience Split 단계.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

온라인 의류 소매업체인 PantsLabyrinth에는 활발한 모바일 사용자 그룹도 있습니다. 따라서 별도의 온보딩 Canvas에서 다음 필터를 선택하여 모바일 사용자를 식별하고 이러한 Segments로 분류할 수도 있습니다:

- **Welcome Content Card 단계의 콘텐츠 카드를 클릭함**
- **다른 모든 사용자**

#### 오디언스 경로로 더 많은 사용자 타겟팅하기 {#target-more-users-with-audience-paths}

앱과 상호작용하지 않은 사용자 집합에서 "Check for Clicks" 단계와 "Winback Nudge" 단계를 편집하여 이러한 사용자를 추가로 타겟팅할 수 있습니다.

### 7단계: Canvas 테스트 및 시작하기 {#step-7-test-and-launch-your-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **Canvas 시작**을 선택하여 Canvas를 시작합니다. 이제 신규 사용자에게 개인화된 온보딩 경험을 제공하여 지속적인 관계를 장려할 수 있습니다!

{% alert tip %}
Canvas를 시작하기 전후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)를 확인하세요.
{% endalert %}