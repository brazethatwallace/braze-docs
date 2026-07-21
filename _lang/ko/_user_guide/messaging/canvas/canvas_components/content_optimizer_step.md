---
nav_title: 콘텐츠 최적화 프로그램
article_title: 콘텐츠 최적화 프로그램 단계
alias: "/content_optimizer_step/"
page_order: 5
description: "콘텐츠 최적화 프로그램 단계를 사용하면 단일 단계 내에서 콘텐츠 구성요소의 여러 버전을 구성하고 테스트할 수 있습니다. 콘텐츠 변형을 실험하고 시간이 지남에 따라 가장 성과가 좋은 조합으로 자동 최적화할 수 있습니다."
page_type: reference

---

# 콘텐츠 최적화 프로그램 단계 {#content-optimizer-step}

> 콘텐츠 최적화 프로그램 단계를 사용하면 단일 단계 내에서 콘텐츠 구성요소의 여러 버전을 구성하고 테스트할 수 있습니다. 콘텐츠 변형을 실험하고 시간이 지남에 따라 가장 성과가 좋은 조합으로 자동 최적화할 수 있습니다. 소개는 [콘텐츠 최적화 프로그램]({{site.baseurl}}/user_guide/brazeai/content_optimizer)을 참조하세요.

{% alert important %}
콘텐츠 최적화 프로그램은 현재 베타 버전입니다. 시작하는 데 도움이 필요하면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 콘텐츠 최적화 프로그램 단계 생성 {#create-a-content-optimizer-step}

최상의 결과를 얻으려면 사용자가 시간이 지남에 따라 점진적으로 단계에 진입하는 Canvas에서 콘텐츠 최적화 프로그램을 사용하세요. 모든 사용자가 한꺼번에 단계에 진입하면 콘텐츠 최적화 프로그램이 초기 결과에서 학습할 시간이 없습니다.

### 1단계: 단계 추가 {#step-1-add-a-step}

사이드바에서 **콘텐츠 최적화 프로그램** 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 후 **콘텐츠 최적화 프로그램**을 선택합니다.

### 2단계: 기본 메시지 생성 {#step-2-create-your-base-message}

기본 메시지는 단계의 시작점입니다. 각 콘텐츠 구성요소의 배리언트는 **Content Optimizer Settings** 탭에서 정의된 조합에 따라 동적으로 삽입됩니다.

{% alert note %}
베타 기간 동안 지원되는 채널은 이메일, 푸시 알림, SMS/MMS/RCS입니다.
{% endalert %}

{% tabs local %}
{% tab 이메일 %}

**Messaging Channels** 탭에서 **Email**을 선택하고 기본 이메일 메시지를 생성합니다. 도움이 필요하면 전용 [이메일]({{site.baseurl}}/user_guide/channels/email) 섹션을 참조하세요.

콘텐츠 최적화 프로그램은 이 배리언트에 지정된 발송 설정(이메일 도메인 및 회신 주소 등)을 사용하여 모든 메시지를 발송합니다. 새 디자인으로 시작하거나 이 메시지에 대한 기존 템플릿을 선택할 수 있습니다. 이 단계에서 메시지의 어떤 구성요소를 최적화할지 고려하세요. 이는 [4단계](#step-4)에서 정의합니다.

최적화할 수 있는 지원 구성요소는 다음과 같습니다:

- Subject
- Body Header
- Body Content
- Primary CTA

{% endtab %}
{% tab 푸시 알림 %}

**Messaging Channels** 탭에서 **Push notifications**를 선택하고 기본 푸시 알림을 생성합니다. 도움이 필요하면 전용 [푸시]({{site.baseurl}}/user_guide/channels/push) 섹션을 참조하세요.

콘텐츠 최적화 프로그램은 이 배리언트에 지정된 선택된 푸시 플랫폼을 사용하여 모든 메시지를 발송합니다. 새 디자인으로 시작하거나 이 메시지에 대한 기존 템플릿을 선택할 수 있습니다. 이 단계에서 메시지의 어떤 구성요소를 최적화할지 고려하세요. 이는 [4단계](#step-4)에서 정의합니다.

최적화할 수 있는 지원 구성요소는 다음과 같습니다:

- Title
- Message

{% endtab %}
{% tab SMS/MMS/RCS %}

**Messaging Channels** 탭에서 **SMS/MMS/RCS**를 선택하고 기본 메시지를 생성합니다. 도움이 필요하면 전용 [SMS/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) 섹션을 참조하세요.

콘텐츠 최적화 프로그램은 이 배리언트에 지정된 **Content** 및 **Message** 세부 정보를 사용하여 모든 메시지를 발송합니다. 새 디자인으로 시작하거나 이 메시지에 대한 기존 템플릿을 선택할 수 있습니다. 이 단계에서 메시지의 어떤 구성요소를 최적화할지 고려하세요. 이는 [4단계](#step-4)에서 정의합니다.

최적화할 수 있는 지원 구성요소는 다음과 같습니다:

- Hook
- Body
- CTA

{% endtab %}
{% endtabs %}

### 3단계: 전달 설정 지정 {#step-3-specify-delivery-settings}

**Delivery Settings** 탭에서 단계에 Intelligent Timing 또는 전달 유효성 검사를 사용할지 지정할 수 있습니다. 자세한 내용은 메시지 단계의 [전달 설정 편집]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings)을 참조하세요.

### 4단계: 콘텐츠 구성요소 및 배리언트 추가 {#step-4}

콘텐츠 구성요소는 다양한 제목란이나 타이틀 등 테스트하려는 메시지의 개별 요소입니다. 이러한 구성요소를 사용하면 메시지의 여러 버전을 생성하고 시간이 지남에 따라 성과를 기반으로 자동 최적화할 수 있습니다.

- **이메일:** 단계당 최대 3개의 콘텐츠 구성요소와 구성요소당 최대 5개의 배리언트를 추가할 수 있으며, 총 125개의 고유 콘텐츠 조합이 가능합니다.
- **푸시 알림:** 단계당 최대 2개의 구성요소와 구성요소당 최대 5개의 배리언트를 추가할 수 있으며, 총 25개의 고유 콘텐츠 조합이 가능합니다.
- **SMS/MMS/RCS:** 단계당 최대 2개의 콘텐츠 구성요소와 구성요소당 최대 5개의 배리언트를 추가할 수 있으며, 총 25개의 고유 콘텐츠 조합이 가능합니다.

**AI 제안 생성**을 사용하면 Braze가 배리언트 아이디어를 생성하기 위해 콘텐츠를 OpenAI에 전송합니다. 발송 시 트래픽 할당에는 OpenAI가 사용되지 않습니다. 전송되는 데이터와 사용 방법에 대한 자세한 내용은 [OpenAI와 콘텐츠 최적화 프로그램]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer)을 참조하세요.

![콘텐츠 최적화 프로그램 인터페이스에서 콘텐츠 구성요소를 추가하고 구성하는 옵션. Subject, Body Header, Body Content, Primary CTA 등 선택 가능한 구성요소가 표시되며, 각각 다른 배리언트를 입력할 수 있는 필드가 있습니다.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### 4.1단계: 콘텐츠 구성요소 구성 {#step-41-configure-content-components}

구성요소를 구성하려면 **Content Optimizer Settings** 탭으로 이동합니다.

{% tabs local %}
{% tab 이메일 %}

이메일 메시지에 대해 최적화할 구성요소를 선택합니다. 지원되는 옵션은 다음과 같습니다:

- Subject
- Body Header
- Body Content
- Primary CTA

선택한 각 구성요소에 대해 해당 콘텐츠의 대체 버전(배리언트) 세트를 정의합니다. 톤, 구조 또는 콘텐츠가 다른 명확하고 구별되는 배리언트를 사용하세요. 이렇게 하면 콘텐츠 최적화 프로그램이 최고 성과 조합을 더 효과적으로 식별할 수 있습니다. 다음을 수행할 수 있습니다:
  - 배리언트를 직접 수동으로 작성합니다.
  - AI 생성 제안을 사용하여 새로운 옵션을 빠르게 탐색합니다.

![이메일 최적화를 위한 콘텐츠 구성요소를 추가하고 구성하는 옵션을 보여주는 콘텐츠 최적화 프로그램 설정 인터페이스. 각 구성요소에는 다른 배리언트를 입력할 수 있는 입력 필드가 있습니다. 구성요소 이름과 배리언트 텍스트를 입력하는 필드가 표시됩니다.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab 푸시 알림 %}

푸시 알림에 대해 최적화할 구성요소를 선택합니다. 지원되는 옵션은 다음과 같습니다:
- Title
- Message

선택한 각 구성요소에 대해 해당 콘텐츠의 대체 버전(배리언트) 세트를 정의합니다. 톤, 구조 또는 콘텐츠가 다른 명확하고 구별되는 배리언트를 사용하세요. 이렇게 하면 콘텐츠 최적화 프로그램이 최고 성과 조합을 더 효과적으로 식별할 수 있습니다. 다음을 수행할 수 있습니다:
  - 배리언트를 직접 수동으로 작성합니다.
  - AI 생성 제안을 사용하여 새로운 옵션을 빠르게 탐색합니다.

![푸시 최적화를 위한 콘텐츠 구성요소를 추가하고 구성하는 옵션을 보여주는 콘텐츠 최적화 프로그램 설정.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab SMS/MMS/RCS %}

구독 그룹과 메시지 유형(해당하는 경우)을 선택한 후, SMS/MMS/RCS에 대해 최적화할 구성요소를 선택합니다. 지원되는 옵션은 다음과 같습니다:
- Hook
- Body
- CTA
{% alert note %}
SMS/MMS/RCS 콘텐츠 최적화 프로그램 단계가 시작된 후에는 구독 그룹이나 메시지 유형을 업데이트할 수 없습니다.
{% endalert %}
선택한 각 구성요소에 대해 해당 콘텐츠의 대체 버전(배리언트) 세트를 정의합니다. 톤, 구조 또는 콘텐츠가 다른 명확하고 구별되는 배리언트를 사용하세요. 이렇게 하면 콘텐츠 최적화 프로그램이 최고 성과 조합을 더 효과적으로 식별할 수 있습니다. 다음을 수행할 수 있습니다:
  - 배리언트를 직접 수동으로 작성합니다.
  - AI 생성 제안을 사용하여 새로운 옵션을 빠르게 탐색합니다.

![SMS/MMS/RCS 최적화를 위한 콘텐츠 구성요소를 추가하고 구성하는 옵션을 보여주는 콘텐츠 최적화 프로그램 설정.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### 4.2단계: 메시지에 Liquid 추가 {#step-42-add-liquid-to-your-message}

각 구성요소에 대해 최소 두 개의 배리언트를 정의한 후, 각각에 연결된 Liquid 태그를 복사하여 기본 메시지의 해당 위치에 붙여넣습니다.

- 예를 들어, 제목란을 최적화하는 경우 이메일 작성기의 제목 필드에 {% raw %}`{% message_component "Subject" %}`{% endraw %} 태그를 붙여넣습니다.
- 구성요소의 일부만 테스트하기 위해 더 긴 텍스트 안에 구성요소 태그를 포함할 수도 있습니다. 예: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Subject, Body Header, Body Content, Primary CTA 등의 콘텐츠 구성요소를 추가하고 구성하는 옵션. 각 구성요소에는 다른 배리언트를 입력할 수 있는 필드가 있습니다.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

선택한 콘텐츠 구성요소에 대해 Liquid 태그를 추가하지 않으면 **Content Optimizer Settings** 탭에 경고가 표시되고 **Messaging Channels** 탭에 오류가 표시됩니다. 선택한 모든 구성요소가 기본 메시지에 올바르게 추가될 때까지 Canvas를 시작할 수 없습니다.

Canvas가 실행되면 콘텐츠 최적화 프로그램이 구성요소 간의 배리언트를 혼합하고 매칭하여 다양한 콘텐츠 조합을 생성합니다. 시간이 지남에 따라 성과가 높은 조합이 전달에 우선적으로 배정되어 수동 개입 없이 성과를 개선할 수 있습니다.

#### Liquid 참조 {#liquid-references}

| 채널 | 구성요소 | Liquid 스니펫 |
| --- | --- | --- |
| 이메일 | Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| 이메일 | Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| 이메일 | Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| 이메일 | Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| 푸시 | Title | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| 푸시 | Message | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| SMS/MMS/RCS | Hook | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| SMS/MMS/RCS | Body | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| SMS/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid 참조" }

### 5단계: 최적화 이벤트 선택 {#step-5-select-optimization-event}

최적화 이벤트는 콘텐츠 최적화 프로그램이 성과를 평가하고 시간이 지남에 따라 콘텐츠 조합에 트래픽을 할당하는 방법을 결정합니다.

선택한 최적화 이벤트는 이 단계의 모든 콘텐츠 구성요소에 적용됩니다.

{% tabs local %}
{% tab 이메일 %}

이메일의 경우 다음 이벤트 중 하나에 대해 최적화할 수 있습니다. 콘텐츠 최적화 프로그램은 메시지 발송 후 7일 이내에 등록된 열람 및 클릭을 사용하여 성과가 높은 콘텐츠 조합으로 전달을 전환합니다.

| 이벤트 | 설명 | 사용 사례 |
| --- | --- | --- |
| 열람 | 수신자가 이메일을 열도록 하는 조합에 최적화합니다. | 제목란 테스트 또는 가시성 향상 목표 |
| 클릭 | 링크와의 인게이지먼트를 유도하는 조합에 최적화합니다. 봇 클릭이나 Braze가 인식한 탈퇴 클릭은 포함되지 않습니다. | 링크에서 트래픽, 인게이지먼트 또는 전환 유도 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="5단계: 최적화 이벤트 선택" }

{% endtab %}
{% tab 푸시 알림 %}

푸시 알림의 경우 **열람**에 대해 최적화할 수 있습니다. 이는 수신자가 푸시 알림을 열도록 하는 조합에 최적화합니다. 이 최적화 이벤트를 사용하여 제목이나 메시지 문구의 변형을 테스트할 수 있습니다.

{% endtab %}
{% tab SMS/MMS/RCS %}

SMS 및 MMS 메시지의 경우 **클릭**에 대해 최적화할 수 있습니다. RCS 메시지의 경우 **읽기** 또는 **클릭**에 대해 최적화할 수 있습니다.

단계에 최적화할 이벤트가 있으려면:
- SMS 및 MMS 메시지에 링크가 포함되어 있어야 합니다.
- RCS 메시지에 링크 또는 추천 답장이 포함되어 있어야 합니다.

{% alert note %}
현재 콘텐츠 최적화 프로그램을 사용하는 RCS 메시징은 SMS 대체를 지원하지 않습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 단계 상태 {#step-states}

콘텐츠 최적화 프로그램 단계가 실행되면 Braze가 콘텐츠 배리언트 성과를 평가하고 Canvas에서 볼 수 있는 세 가지 상태 중 하나를 단계에 할당합니다.

| 상태 | 의미 |
| --- | --- |
| 학습 중 | 콘텐츠 최적화 프로그램이 콘텐츠 배리언트 전반에 걸쳐 성과 데이터를 수집 중이며 아직 일관되고 신뢰할 수 있는 우승자를 찾지 못했습니다. |
| 최적화 중 | 콘텐츠 최적화 프로그램이 다른 배리언트보다 일관되게 우수한 성과를 보이는 배리언트를 찾았으며 우승 조합으로 전달을 전환하고 있습니다. |
| 조치 권장 | 단계가 한동안 실행되었지만 명확한 우승자가 나타나지 않았습니다. 콘텐츠 최적화 프로그램이 우승자를 찾을 수 있도록 단계 설정을 검토하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="콘텐츠 최적화 프로그램 단계 상태" }

### 고려할 조치 {#actions-to-consider}

단계가 조치 권장 상태에 진입하면 다음을 고려하세요:

- 가능하다면 Canvas에 진입하는 사용자 수를 늘리세요. 더 많은 발송은 콘텐츠 최적화 프로그램에 학습할 더 많은 데이터를 제공합니다.
- 일반적으로 적은 수보다 많은 수의 조합을 테스트하세요([모범 사례](#best-practices) 참조). 이렇게 하면 콘텐츠 최적화 프로그램이 무엇이 우승하고 있는지에 대해 더 명확한 신호를 얻을 수 있습니다. 오디언스 볼륨이 적은 경우(하루 평균 약 3,000건 미만의 발송), 볼륨 대비 너무 많은 조합이 학습을 늦출 수 있으므로 배리언트 수를 약간 줄이는 것을 고려하세요.
- 콘텐츠 배리언트를 톤, 구조 또는 콘텐츠 면에서 서로 더 명확하게 구별되도록 만드세요.
- 오디언스를 늘릴 수 없고 배리언트 수와 콘텐츠 다양성이 이미 적절해 보인다면, 단계가 우승자를 찾기 위해 더 많은 시간이 필요할 수 있습니다.

## 시작된 단계 편집 {#edit-a-launched-step}

Canvas가 시작된 후 Canvas 편집기에서 실행 중인 콘텐츠 최적화 프로그램 단계를 열어 업데이트할 수 있습니다. 다음을 수행할 수 있습니다:

- 기존 구성요소에 수동으로 또는 AI 생성 제안을 사용하여 새 배리언트를 추가합니다(구성요소당 5개 배리언트 제한까지).
- 배리언트를 비활성화하여 사용자에게 발송을 중지합니다.
- 이전에 비활성화된 배리언트를 다시 활성화합니다(해당 구성요소가 5개 배리언트 제한 이하를 유지하는 경우).

변경 사항을 게시하면 최적화 프로그램이 초기화되고 모든 활성 배리언트 및 조합에 대해 처음부터 트래픽을 재할당하기 시작합니다. 단계가 학습 중 상태일 때는 배리언트를 업데이트하지 마세요. 편집 이전의 과거 데이터는 유지되며 **Content Analytics** 탭에서 확인할 수 있습니다.

시작 후 변경할 수 없는 설정은 다음과 같습니다:

- 기존 활성 배리언트의 콘텐츠
- 테스트 중인 구성요소
- 최적화 이벤트

SMS/MMS/RCS 단계의 경우 구독 그룹과 메시지 유형도 시작 후 변경할 수 없습니다.

## 모범 사례 {#best-practices}

- 일반적으로 콘텐츠 최적화 프로그램 단계에서는 적은 수보다 많은 수의 구성요소를 테스트하는 것을 권장합니다. 예를 들어, 이메일에 대해 두 개의 구성요소를 테스트하는 대신 세 개를 테스트하세요.
- 최상의 결과를 위해 총 10개 이상의 조합을 테스트하세요.
- 콘텐츠 최적화 프로그램을 처음 사용하는 경우 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) 단계를 사용하여 오디언스의 일부만 콘텐츠 최적화 프로그램 단계가 포함된 분기에 진입하도록 하는 것을 고려하세요. 예를 들어, 사용자의 절반은 콘텐츠 최적화 프로그램 단계가 있는 경로로 보내고 나머지 절반은 현재 일반 콘텐츠가 포함된 메시지 단계를 발송하는 대조 경로로 보낼 수 있습니다. 그런 다음 2~3주 동안 데이터를 수집하고 핵심 성과 지표(KPI) 또는 반대 측정기준을 비교한 후 콘텐츠 최적화 프로그램 단계가 있는 경로로의 트래픽을 늘리세요.
  - 효과적인 일대일 비교를 위해 콘텐츠 최적화 프로그램 단계에 각 구성요소의 배리언트 중 하나로 현재 일반 콘텐츠를 포함하세요.
- 콘텐츠 최적화 프로그램 단계가 한동안 최적화 중 상태를 유지한 후 업데이트할 준비가 되면, 성과가 낮은 배리언트를 비활성화하고 최고 성과 배리언트의 특성을 기반으로 새 배리언트를 추가하세요.

## 고려 사항 {#considerations}

- 콘텐츠 최적화 프로그램 단계에서는 다국어 설정이 지원되지 않습니다. 대신 언어별로 하나의 콘텐츠 최적화 프로그램 단계를 사용하고 경로를 개별적으로 분기하세요.
- 콘텐츠 최적화 프로그램 구성요소의 Liquid 태그는 메시지 단계에서 지원되지 않으므로 메시지 단계에서 Liquid가 중단됩니다.
- 콘텐츠 최적화 프로그램 단계가 시작된 후에는 테스트 중인 구성요소, 기존 활성 배리언트의 콘텐츠 또는 최적화 이벤트를 변경할 수 없습니다. SMS/MMS/RCS 단계의 경우 구독 그룹과 메시지 유형도 변경할 수 없습니다.

## 분석 {#analytics}

성과를 검토하려면 단계 수준 분석 패널을 열어 콘텐츠 배리언트별 측정기준과 전체 조합 성과를 확인하세요. 콘텐츠 최적화 프로그램 단계는 [메시지 단계와 동일한 분석]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics)을 사용합니다.

시작 후 단계를 업데이트한 경우 발송 할당 차트에 각 콘텐츠 편집이 발생한 시점이 표시됩니다. 비활성화된 배리언트의 데이터는 유지되며 분석 패널에서 계속 확인할 수 있으므로 단계의 전체 수명 동안의 성과를 비교할 수 있습니다.

![세 개의 버튼에 대한 콘텐츠 최적화 프로그램 분석과 상승 추세를 보이는 발송 할당 비율.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### 구성요소별 성과 {#performance-by-component}

**구성요소별 성과** 섹션은 콘텐츠 최적화 프로그램 단계의 각 구성요소에 대한 성과를 표시합니다. **구성요소** 열은 테스트 중인 콘텐츠 구성요소(예: **Subject line** 또는 **Primary CTA**)와 일치합니다. **식별자** 열은 **Content Optimizer Settings** 탭에서 이 배리언트의 식별자와 일치합니다.

고유 열람 및 클릭은 메시지 발송 후 7일 이내에 캡처됩니다. 표시되는 열은 채널 및 선택한 최적화 이벤트에 따라 다릅니다.

| 측정기준 | 설명 |
| --- | --- |
| 발송 수 | 이 단계에서 해당 구성요소의 이 배리언트에 귀속된 발송 수로, [조합별 성과](#performance-by-combination) 테이블의 [*발송 수*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends)와 동일한 단계 수준 발송 집계를 사용합니다. |
| 열람 | 이 열이 채널에 표시되는 경우, 발송 후 7일 이내에 이 배리언트의 **고유** 열람 수입니다. [*고유 열람*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens)을 참조하세요. |
| 열람율 | 이 열이 표시되는 경우, 7일 이내에 최소 한 번의 적격 고유 열람을 기록한 이 배리언트 발송의 비율입니다. |
| 클릭 수 | 발송 후 7일 이내에 이 배리언트의 **고유** 클릭 수입니다. [*총 클릭 수*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*고유 클릭 수*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks), [5단계: 최적화 이벤트 선택](#step-5-select-optimization-event)을 참조하세요. |
| 클릭률 | 7일 이내에 최소 한 번의 적격 고유 클릭을 기록한 이 배리언트 발송의 비율로, [조합별 성과](#performance-by-combination) 테이블과 동일한 단계 기간을 사용합니다. 자세한 내용은 [단계 분석이 일반 분석과 다른 이유](#why-step-analytics-differ-from-general-analytics)를 참조하세요. |
| 읽기 | 이 열이 표시되는 경우(예: 읽기에 대해 최적화하는 RCS의 경우), 읽음 확인이 활성화된 상태에서 소비자가 메시지를 읽은 횟수입니다. [*읽기*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads)를 참조하세요. |
| 읽기율 | 읽음 확인이 활성화된 사용자 중 이 배리언트 발송에서 읽기가 발생한 비율입니다. [*읽기율*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="구성요소별 성과 측정기준" }

![구성요소별 콘텐츠 최적화 프로그램 성과 분석으로, 구성요소별 개별 테이블에 각 배리언트의 발송 수, 클릭 수, 클릭률이 나열되어 있습니다.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### 조합별 성과 {#performance-by-combination}

**조합별 성과** 섹션은 콘텐츠 최적화 프로그램 단계의 각 조합에 대한 성과를 표시합니다. 조합은 이 행을 정의하는 배리언트의 혼합으로, 테스트 중인 각 콘텐츠 구성요소에서 선택된 하나의 배리언트입니다(예: 제목란과 Primary CTA의 조합).

고유 열람 및 클릭은 메시지 발송 후 7일 이내에 캡처됩니다. 표시되는 열은 채널 및 선택한 최적화 이벤트에 따라 다릅니다.

| 측정기준 | 설명 |
| --- | --- |
| 발송 수 | 이 조합을 사용하여 이 단계에서 발송된 총 메시지 수입니다. 집계는 각 조합에 범위가 지정된 [*발송 수*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends)와 동일한 일반적인 의미를 따릅니다. |
| 열람 | 발송 후 7일 이내에 이 조합의 고유 열람 수입니다. 이메일의 고유 열람 정의 방법은 [*고유 열람*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens)을 참조하세요. |
| 열람율 | 7일 이내에 최소 한 번의 적격 고유 열람을 기록한 이 조합 발송의 비율입니다. |
| 클릭 수 | 발송 후 7일 이내에 이 조합의 고유 클릭 수입니다. Braze가 채널별로 클릭을 정의하는 방법은 [*총 클릭 수*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) 및 [*고유 클릭 수*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks)를 참조하세요. |
| 클릭률 | 7일 이내에 최소 한 번의 적격 고유 클릭을 기록한 이 조합 발송의 비율입니다. 콘텐츠 최적화 프로그램은 단계의 7일 중복 제거 집계를 사용하므로 이 비율은 일반 Campaign 분석의 클릭률과 일치하지 않을 수 있습니다. 자세한 내용은 [단계 분석이 일반 분석과 다른 이유](#why-step-analytics-differ-from-general-analytics)를 참조하세요. |
| [읽기]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | 이 열이 표시되는 경우(예: 읽기에 대해 최적화하는 RCS의 경우), 읽음 확인이 활성화된 상태에서 소비자가 메시지를 읽은 횟수입니다. |
| [읽기율]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | 이 열이 표시되는 경우, 읽음 확인이 활성화된 사용자 중 이 조합 발송에서 읽기가 발생한 비율입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="조합별 성과 측정기준" }

![각 콘텐츠 조합의 발송 수, 클릭 수, 클릭률이 포함된 콘텐츠 최적화 프로그램 조합별 성과 분석 테이블.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### 단계 분석이 일반 분석과 다른 이유 {#why-step-analytics-differ-from-general-analytics}

콘텐츠 최적화 프로그램 단계의 분석이 **Analytics** 섹션과 다른 이유는 다음과 같습니다:

- 푸시 발송은 동일한 사용자에게 다른 기기로 발송된 경우 중복이 제거됩니다.
- 일반적으로 클릭과 열람은 각 사용자에 대해 고유하게 중복이 제거됩니다.
- 메시지 발송 후 7일 이내에 발생한 클릭과 열람만 콘텐츠 최적화 프로그램 단계에서 집계됩니다.

## 문제 해결 {#troubleshooting}

| 문제 | 설명 | 해결 방법 |
| --- | --- | --- |
| 누락된 Liquid 태그 | 콘텐츠 구성요소(예: Subject 또는 CTA)를 추가했지만 해당 Liquid 태그를 기본 메시지에 삽입하지 않은 경우 다음이 표시됩니다: <br>- **Content Optimizer Settings** 탭에 경고 <br>- **Messaging Channels** 탭에 오류 | **Content Optimizer Settings** 탭에서 각 구성요소 아래에 표시된 Liquid 스니펫을 복사하여 메시지의 적절한 위치에 붙여넣으세요. |
| 고아 Liquid 태그 | 콘텐츠 구성요소를 삭제했지만 기본 메시지에 해당 Liquid 태그를 남겨둔 경우 발송 시 메시지가 예상대로 렌더링되지 않을 수 있습니다. | 시작하기 전에 기본 메시지에서 사용하지 않는 `message_component` 태그를 모두 제거하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="문제 해결" }