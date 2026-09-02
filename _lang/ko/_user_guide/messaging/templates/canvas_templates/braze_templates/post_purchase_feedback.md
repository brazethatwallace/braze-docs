---
nav_title: 구매 후 피드백
article_title: 구매 후 피드백
page_order: 6
page_type: reference
description: "이 문서에서는 BRAZE 캔버스 템플릿을 사용하여 피드백에 응답하고 사용자와의 관계를 구축할 수 있는 개인화된 경험을 오케스트레이션하는 방법을 설명합니다."
tool: Canvas
---

# 구매 후 피드백 {#post-purchase-feedback}

> 구매 후 피드백 템플릿을 사용하여 고객이 브랜드와 어떻게 상호작용하는지에 대한 중요한 인사이트를 얻고, 고객이 계속해서 긍정적인 경험을 할 수 있도록 보장하세요. 개인화된 커뮤니케이션과 체계적인 메시지 세트를 활용하여 고객 관계를 지속적으로 구축하고 발전시킬 수 있습니다.

이 문서에서는 사용자 라이프사이클의 전환 단계를 위해 설계된 **구매 후 피드백** 템플릿의 사용 사례를 안내합니다. 완료하면 사용자에게 앱에 대한 피드백을 제공하도록 유도하는 Canvas를 만들 수 있습니다.

## 필수 조건 {#prerequisites}

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 피드백 설문조사 결과를 참조할 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes).
- 사용하는 파트너 및 오디언스와 함께 구성된 [Braze 오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync).

## 필요에 맞게 템플릿 조정하기 {#tailoring-the-template-to-your-needs}

모바일 비디오 게임 개발사인 Decorumsoft에서 일하고 있다고 가정해 보겠습니다. 구매 후 피드백 템플릿을 사용하여 최신 비디오 게임 출시작인 Proxy War 3: War of Thirst에 대한 피드백을 수집할 것입니다. 이 피드백을 활용하여 확장팩 Liquid Mirage의 개발 계획을 수립할 것입니다.

Canvas를 생성하기 전에, 행동 트리거, 세분화 등을 기반으로 광고를 전송할 수 있도록 Braze의 사용자 데이터를 Google Audiences에 추가할 수 있는 [Braze 오디언스 동기화 to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) 통합을 설정합니다.

구매 후 피드백 템플릿에 접근하려면, 새 Canvas를 생성할 때 **Use a Canvas template** > **Braze templates**를 선택합니다. 그런 다음 **Post-Purchase Feedback** 옆에 있는 **Apply Template**을 선택합니다. 이제 템플릿을 필요에 맞게 조정할 수 있습니다.

### 1단계: Canvas 세부 정보 설정 {#step-1-set-up-canvas-details}

Canvas 세부 정보를 목표에 맞게 조정해 보겠습니다.

1. 템플릿 이름 옆의 **Edit**을 선택합니다.

![Canvas의 현재 제목과 설명.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2. Canvas 이름을 업데이트하여 최근 사용자를 타겟팅하기 위한 Canvas임을 명시합니다.
3. 설명을 업데이트하여 사용자에게 피드백 제출을 유도하기 위한 Canvas임을 명시합니다.
4. Canvas 홈 페이지에서 필터링할 수 있도록 **Feedback** 태그를 추가합니다.

![Canvas의 새 이름과 설명. 새 설명에는 'PWD3의 향후 확장팩 Liquid Mirage에 대한 관심도를 측정하기 위한 구매 후 피드백 Canvas.'라고 명시되어 있습니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### 2단계: 전환 이벤트 할당 {#step-2-assign-conversion-events}

다음으로 전환 이벤트를 할당해 보겠습니다. **주요 전환 Event - A**를 **Make a specific purchase**로 업데이트하고 **Proxy War**를 선택합니다.

![Proxy War 게임 제품 구매의 전환 이벤트 유형에 대한 "전환 이벤트 할당" 섹션.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

가장 최근 사용자를 타겟팅하고 싶으므로 템플릿의 전환 기한인 3일을 유지합니다.

### 3단계: 진입 스케줄 설정 {#step-3-set-an-entry-schedule}

1. 진입 스케줄 유형을 **Action-Based**로 유지합니다.
2. 진입 기간의 **Start Time**을 게임 출시 날짜로 설정합니다.

### 4단계: Canvas에 진입할 사용자 결정 {#step-4-determine-who-enters-the-canvas}

피드백 대상 오디언스는 최근 Proxy War 3를 구매한 사용자입니다.

1. 게임을 구매한 사용자로 구성된 타겟 Segment "Purchased Proxy War 3"를 선택합니다.
2. "Proxy War 3"를 "0"회 이상 구매한 사용자를 포함하는 필터를 선택합니다.

!["Purchased Proxy War 3"라는 이름의 Segment로, 게임을 구매한 사용자를 세분화합니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3. Canvas의 최대 기간이 지난 후 사용자가 Canvas에 다시 진입하지 못하도록 진입 제어를 업데이트합니다.

### 5단계: 발송 설정 선택 {#step-5-select-your-send-settings}

기본 구독 설정을 유지하여 메시지나 알림 수신에 가입하거나 옵트인한 사용자에게만 발송합니다.

발송에 신중을 기하기 위해 **Enable Quiet Hours**를 선택하여 사용자의 시간대 기준 오후 11시에서 오전 10시 사이에는 피드백을 요청하지 않고, 다음 가능한 시간에만 발송합니다.

![가입하거나 옵트인한 사용자를 타겟팅하는 "발송 설정" 단계. 방해금지 시간이 켜져 있습니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

이 예시에서는 다른 설정(최대 게재빈도 설정 및 시드 그룹)은 건너뜁니다.

### 6단계: Canvas 커스터마이즈 {#step-6-customize-your-canvas}

다음으로 사용자에게 발송할 메시징 채널과 콘텐츠를 커스터마이즈하여 Canvas를 구축합니다. 이메일, 인앱 메시지, 웹훅 채널만 사용하여 피드백을 수집하므로, 템플릿을 살펴보고 메시지 단계에서 단문 메시지 서비스 배리언트를 제거합니다.

각 메시징 구성요소를 살펴보며 콘텐츠를 업데이트하는 것으로 커스터마이즈를 시작합니다. 참조할 커스텀 속성은 `Experience Feedback`입니다.

1. Canvas 빌더에서 사용자 여정의 첫 번째 메시지 단계를 선택합니다.
2. **Email** 배리언트를 선택합니다.
3. 사용자 피드백을 유도하는 제목으로 **Sending info**를 작성합니다.
4. **Edit message**를 선택하여 템플릿의 이메일 메시지를 피드백 설문조사 메시지로 교체합니다. 여기에는 각 행동 유도 링크를 교체하여 어떤 옵션이 선택되었는지 캡처하는 것이 포함되며, 이는 사용자 여정의 행동 경로 단계에서 참조됩니다.

{% alert tip %}
[Canvas 진입 속성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)을 사용하여 참조하는 제품에 따라 Canvas의 메시지를 커스터마이즈할 수 있습니다.
{% endalert %}

#### 피드백 설문조사 설정 {#set-up-feedback-survey}

다음으로 **In-App Message** 배리언트의 세부 정보를 작성해야 합니다. 여기서 사용자 피드백의 감정을 나타내는 `Experience Feedback` 커스텀 속성을 지정해야 합니다. (이후 행동 경로 단계에서도 이를 참조합니다.)

1. 동일한 첫 번째 메시지 단계에서 **In-App Messages** 배리언트를 선택합니다. 메시지 제어는 그대로 유지합니다.
2. 헤더와 본문에는 사용자가 Proxy War 3 경험에 대해 솔직하게 답변하도록 유도하는 문구를 사용합니다.
3. 설문조사 응답이 프로필에 기록되도록 설문조사를 **Single-choice selection**으로 유지하고 **Log attributes upon submission**을 설정합니다.
4. 세 가지 설문조사 선택지 각각에 대해 커스텀 속성으로 **Experience Feedback**을 선택합니다.
5. 이 값들이 커스텀 속성과 일치하므로 고객 프로필의 속성 값은 그대로 유지합니다.

![사용자에게 최근 Proxy War 3 구매를 즐겼는지 묻는 설문조사로, "Loved it", "It was OK", "Not for me" 세 가지 옵션이 있습니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### 행동 경로 구축 {#build-out-the-action-path}

커스텀 속성 `Experience Feedback`과 이전 섹션의 속성 값을 사용하여 템플릿의 행동 경로를 속성 및 값에 맞게 업데이트합니다.

![설문조사에서 "Loved it"이라고 응답한 사용자를 포함하는 행동 경로 단계의 "긍정적 피드백" 그룹.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### 광고 리타겟팅 설정 {#set-up-ad-retargeting}

**Ad Retargeting** 단계에서 Google 오디언스 동기화가 설정되어 있는지 확인합니다. 여기에는 광고 계정, 기존 오디언스를 선택하고 오디언스에 사용자를 추가하는 옵션이 포함됩니다.

### 웹훅 지원 케이스 설정 {#set-up-webhook-support-cases}

다음으로 잠재적인 지원 케이스를 트리거하는 웹훅을 설정해 보겠습니다. 이는 사용자 피드백 분석과 결합하면 특히 유용한 인사이트를 제공할 수 있습니다.

**Support Case Creation**이라는 이름의 메시지 단계에서, 구매에 불만족하고 환불을 원하는 사용자를 위한 웹훅을 작성하도록 템플릿을 업데이트합니다.

![Proxy War 3 구매에 대해 부정적인 감정을 가지고 환불을 원하는 고객을 위한 지원 케이스를 생성하는 웹훅.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### 7단계: Canvas 테스트 및 시작 {#step-6-test-and-launch-the-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후, **Launch Canvas**를 선택하여 Canvas를 시작합니다. 이제 Proxy War 3의 최근 구매를 기반으로 피드백 설문조사에 응답하도록 유도하는 개인화된 사용자 여정으로 사용자를 세심하게 타겟팅할 수 있습니다!

{% alert tip %}
Canvas를 시작하기 전후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)를 확인하세요.
{% endalert %}