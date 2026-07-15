---
nav_title: Canvas 기본 사항
article_title: Canvas 기본 사항
page_order: 0
page_type: reference
description: "이 참조 문서에서는 첫 번째 Canvas를 설정할 때 스스로에게 물어봐야 할 다양한 질문을 다루며 Canvas의 기본 사항을 설명합니다."
tool: Canvas

---

# Canvas 기본 사항 {#canvas-basics}

> 이 참조 문서에서는 첫 번째 Canvas를 설정할 때 스스로에게 물어봐야 할 다양한 질문을 다루며 Canvas의 기본 사항을 설명합니다. 또한 시각화의 5W(무엇을, 언제, 누구에게, 왜, 어디서)를 설명하고, 이를 통해 Canvas를 어떻게 구축할 수 있는지 그 형태와 방향을 잡는 방법을 알아봅니다.

## Canvas 구조 이해하기 {#understanding-canvas-structure}

[Canvas 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)의 세부 사항을 살펴보기 전에, Canvas를 구성하는 핵심 요소를 파악해 보겠습니다.

{% tabs %}
  {% tab Canvas %}
  Canvas는 마케터가 여러 메시지로 캠페인을 구성할 수 있는 통합 인터페이스입니다. 시각적 프로그래밍 도구와 비슷하게, 일련의 단계로 구성된 일관된 사용자 여정을 구축할 수 있습니다.

  ![사용자가 푸시를 활성화했는지 여부에 따라 두 가지 다른 사용자 여정으로 분기하는 결정 분할 단계가 포함된 Canvas 예시.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab 여정 %}

  여정, 또는 일반적으로 사용자 여정이라고 불리는 것은 Canvas 내에서 개별 사용자의 경험입니다.<br><br> ![신규 사용자의 고객 여정을 보여주는 차트. 익명 사용자가 앱을 설치하고, Kat이 계정을 생성하고, Kat이 일주일 동안 앱을 열지 않고, 푸시 알림이 Kat을 앱으로 다시 불러오고, 그 후 Kat이 앱을 정기적으로 사용합니다.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Canvas 빌더 %}
  Canvas 빌더는 Canvas를 생성할 때 수행할 단계를 매핑합니다. 여기에는 Canvas 이름 지정 및 Teams 추가와 같은 기본 사항이 포함됩니다. 기본적으로 Canvas 빌더는 Canvas 구축을 시작하기 전에 필요한 핵심 설정입니다. 여기에서 [진입 스케줄]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule), [타겟 오디언스]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-13-set-your-target-entry-audience), [발송 설정]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings)을 편집하는 옵션을 통해 사용자가 고객 여정을 시작하고 완료하는 방식을 제어할 수 있습니다.<br><br> !["New Canvas"라는 이름의 Canvas에 대한 기본설정 섹션의 Canvas 빌더.]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab 배리언트 %}
  배리언트는 각 고객이 여정에서 따르는 경로입니다. Canvas는 대조군과 함께 최대 8개의 배리언트를 지원합니다. 오디언스의 어떤 Segment가 각 배리언트를 따를지 제어할 수 있습니다.<br><br> !["배리언트 추가" 버튼을 선택하는 모습.]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab 단계 %}
  Canvas의 단계는 마케팅 의사결정 지점입니다: "이것이면, 저것을." [Canvas 구성요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components#about-canvas-components)를 활용하여 사용자 여정의 단계를 구축하세요.<br><br> ![Canvas에 지연 단계를 추가하는 예시.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> 사용자가 Canvas에 진입하면 첫 번째 단계부터 시작합니다. 각 단계에는 사용자가 다음 단계로 이동할 수 있는지 결정하는 조건이 있습니다. 단계 내에서 트리거를 설정하거나 전달을 스케줄하고, 필터를 추가하거나 예외 이벤트를 지정하여 타겟팅을 세분화하고, 푸시 알림이나 웹훅 이벤트와 같은 다양한 채널을 지정할 수 있습니다. Canvas에서 단계는 순차적으로 발생하므로, 첫 번째 단계가 완료된 후에 두 번째 단계가 발생합니다. 다음과 같은 단계가 있는 Canvas가 있다고 가정해 보겠습니다: 24시간 지연이 있는 지연 단계 A, 푸시 메시지가 있는 메시지 단계 A, 인앱 메시지가 있는 메시지 단계 B. 사용자 A는 24시간 지연 상태에 놓이고, 24시간 후에 푸시 메시지를 받은 다음 인앱 메시지를 받게 됩니다.

  {% endtab %}
{% endtabs %}

## 고객 여정 구축하기 {#building-the-customer-journey}

시각화의 5W(무엇을, 언제, 누구에게, 왜, 어디서)를 활용하면 각 사용자에게 개인화된 메시지 여정을 만들기 위한 고객 참여 전략을 파악하는 데 도움이 됩니다.

### "무엇을": Canvas 이름 짓기 {#the-what-name-your-canvas}

*사용자가 무엇을 하거나 이해하도록 도우려고 하나요?*

이름의 힘을 과소평가하지 마세요. Braze는 협업을 위해 만들어졌으므로, 팀과 목표를 어떻게 소통할지 기반을 다지기에 좋은 시점입니다.

Canvas에 태그를 추가하고 단계와 배리언트에 이름을 지정할 수 있습니다. 고객 여정에 대해 더 알아보려면 [사용자 라이프사이클 매핑](https://learning.braze.com/mapping-customer-lifecycles)에 대한 Braze 학습 과정을 확인하세요.

### "왜": 전환 이벤트 식별하기 {#the-why-identify-conversion-events}

*"무엇을"을 기반으로, 왜 이 Canvas를 구축하나요?*

명확한 목표를 염두에 두는 것은 항상 중요하며, Canvas는 세션 참여, 구매, 커스텀 이벤트와 같은 핵심 성과 지표(KPI)에 대한 성과를 파악하는 데 도움을 줍니다.

하나 이상의 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)를 선택하면 Canvas 내에서 성과를 최적화하는 방법을 이해할 수 있습니다. Canvas에 여러 배리언트 또는 대조군이 있는 경우, Braze는 전환 이벤트를 사용하여 이 목표를 달성하기 위한 최적의 배리에이션을 결정합니다.

* **세션 시작**: 사용자가 다시 돌아와서 앱에 참여하기를 원합니다.
* **구매하기**: 사용자가 구매하기를 원합니다.
* **커스텀 이벤트 수행**: 사용자가 커스텀 이벤트로 추적하고 있는 특정 동작을 수행하기를 원합니다.
* **앱 업그레이드**: 사용자가 앱 버전을 업그레이드하기를 원합니다.

### "언제": 시작 조건 만들기 {#the-when-create-starting-conditions}

*사용자가 언제 이 경험을 시작하나요?*

이 질문에 대한 답변이 Canvas가 고객에게 전달되는 시기와 방법의 세부 사항을 결정합니다. 사용자는 스케줄 기반 또는 동작 기반 트리거의 두 가지 방법 중 하나로 Canvas에 진입할 수 있습니다.

{% alert tip %}
Canvas의 [시간 기반 기능]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types)에서 더 많은 전략과 자주 묻는 질문에 대한 답변을 확인하세요.
{% endalert %}

스케줄 전달을 사용하면 타겟 오디언스에게 Canvas를 즉시 발송할 수 있습니다. 정기적으로 발송하거나 미래의 특정 시간에 스케줄할 수도 있습니다. 동작 기반 Canvas는 특정 고객 행동이 발생할 때 이에 반응합니다. 예를 들어, 동작 기반 트리거에는 앱 열기, 구매하기, 다른 Campaign과 상호작용하기, 또는 커스텀 이벤트 트리거가 포함될 수 있습니다. 동작이 발생하는 시점에 사용자에게 Canvas를 발송할 수 있습니다.

### "누구에게": 오디언스 선택하기 {#the-who-select-an-audience}

*누구에게 도달하려고 하나요?*

"누구에게"를 정의하려면 Canvas에서 사용 가능한 사전 정의된 Segments를 사용할 수 있습니다. 또한 필터를 추가하여 타겟 오디언스와의 연결을 더욱 세분화할 수 있습니다. 이러한 Segments를 구축한 후에는 타겟 오디언스 기준에 맞는 사용자만 Canvas 여정에 진입할 수 있어 더욱 개인화된 경험을 제공할 수 있습니다. 사용 가능한 필터와 이를 통해 사용 사례에 맞게 사용자를 세분화하는 방법은 아래 표를 참조하세요.

| 필터 | 설명 |
|---|---|
| 커스텀 데이터 | 정의한 이벤트와 속성을 기반으로 사용자를 세분화합니다. 제품에 특화된 기능을 사용할 수 있습니다. |
| 사용자 활동 | 사용자의 동작과 구매를 기반으로 고객을 세분화합니다. |
| 리타겟팅 | 이전 Canvases를 발송받았거나, 수신했거나, 상호작용한 고객을 세분화합니다. |
| 마케팅 활동 | 마지막 참여와 같은 범용 행동을 기반으로 고객을 세분화합니다. |
| 사용자 속성 | 고객의 고정 속성과 특성을 기반으로 세분화합니다. |
| 설치 경로 | 최초 소스, 광고 그룹, Campaign 또는 광고를 기반으로 고객을 세분화합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="\"누구에게\": 오디언스 선택하기" }

### "어디서": 오디언스 찾기 {#the-where-find-my-audience}

*오디언스에게 가장 효과적으로 도달할 수 있는 곳은 어디인가요?*

여기에서 사용자 여정에 가장 적합한 메시징 채널을 결정합니다. 이상적으로는 사용자가 가장 접근하기 쉬운 곳에서 도달하고 싶을 것입니다. 이를 염두에 두고, Canvas에서 다음 채널을 사용할 수 있습니다:
* [이메일]({{site.baseurl}}/user_guide/channels/email)
* [푸시]({{site.baseurl}}/user_guide/channels/push)
* [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages)
* [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
* [SMS 또는 MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
* [웹훅]({{site.baseurl}}/user_guide/channels/webhooks)

### "어떻게": 완전한 경험 구축하기 {#the-how-build-the-complete-experience}

*5W를 파악한 후 Canvas 여정을 어떻게 구축하나요?*

"어떻게"는 Canvas를 어떻게 만들고 메시지로 사용자에게 어떻게 도달할지를 종합적으로 요약합니다. 예를 들어, 메시지가 효과적이려면 다양한 사용자의 시간대를 고려하여 메시징 타이밍을 최적화해야 합니다.

"어떻게"에 대한 답변은 또한 오디언스에게 Canvas를 발송하는 주기(예: 주 1회 또는 격주)와 "어디서"에서 설명한 대로 구축하는 각 Canvas에 활용할 메시징 채널을 결정합니다.

## 사용 사례: 고객 온보딩 플로우 {#use-case-customer-onboarding-flow}

예를 들어, 온라인 스트리밍 서비스 회사인 MovieCanon의 마케터이고 앱의 신규 사용자를 위한 온보딩 플로우를 만드는 업무를 담당하고 있다고 가정해 보겠습니다. 5W를 참조하여 다음과 같은 방식으로 Canvas를 구축할 수 있습니다.

* **무엇을**: Canvas 이름은 "New Onboarding Journey"입니다.
* **왜**: Canvas의 목표는 사용자를 환영하고 앱에 계속 참여하도록 하는 것입니다.
* **언제**: 사용자가 처음 앱을 열면 환영 이메일을 보내고 싶습니다.
* **누구에게**: 처음으로 앱을 사용하는 신규 사용자를 타겟팅합니다.
* **어디서**: 이메일을 통해 신규 사용자에게 도달할 수 있다고 확신합니다. 이는 과거 모든 메시징에서 사용한 방법입니다.
* **어떻게**: 신규 사용자에게 알림이 과도하지 않도록 1일 지연을 설정하고 싶습니다. 이 지연 후에 가장 인기 있는 영화와 TV 프로그램 목록이 포함된 이메일을 보내 앱을 계속 사용하도록 유도합니다.

## 일반 팁 {#general-tips}

### 단계와 배리언트를 언제, 어떻게 사용할지 결정하기 {#determine-when-and-how-to-use-steps-and-variants}

각 Canvas에는 최소 하나의 배리언트와 최소 하나의 단계가 있어야 합니다. 그 이후로는 가능성이 무한합니다. 그렇다면 Canvas의 형태를 어떻게 결정할까요? 바로 목표, 데이터, 가설이 중요한 역할을 합니다. "어떻게"와 "어디서" 브레인스토밍이 Canvas의 올바른 형태와 구조를 매핑하는 데 도움이 됩니다.

### 역순으로 작업하기 {#work-backwards}

일부 목표에는 더 작은 하위 목표가 있습니다. 예를 들어, 무료 사용자를 구독자로 전환하는 것이 목표라면 구독 서비스가 설명된 페이지가 필요할 수 있습니다. 방문자가 구매하기 전에 옵션을 확인해야 할 수 있습니다. 결제 페이지 전에 이 페이지를 보여주는 데 메시징 노력을 집중할 수 있습니다. 고객이 목표에 도달하기 위해 거쳐야 하는 여정을 역순으로 이해하는 것이 전환으로 안내하는 핵심입니다.

### 메시징 방식 다양화하기 {#mix-up-your-messaging}

과거에 유사한 Campaign을 실행한 적이 있나요? 또는 현재 실행 중인 Campaign이 있나요? 해당 메시지를 활용하여 더 많은 개인화를 추가해 보세요. 새로운 필터를 시도하거나 후속 메시지를 추가해 보세요. 메시징 기법을 다양화하면서 성과를 모니터링하고 점진적인 변경을 통해 계속 최적화하세요.