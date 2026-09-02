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

## Content Optimizer 단계 만들기 {#create-a-content-optimizer-step}

최상의 결과를 얻으려면 사용자가 시간이 지남에 따라 점진적으로 단계에 진입하는 Canvases에서 Content Optimizer를 사용하세요. 모든 사용자가 한꺼번에 단계에 진입하면 Content Optimizer가 초기 결과를 학습할 시간이 부족합니다.

### 1단계: 단계 추가하기 {#step-1-add-a-step}

사이드바에서 **Content Optimizer** 구성 요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택한 다음 **Content Optimizer**를 선택합니다.

### 2단계: 기본 메시지 만들기 {#step-2-create-your-base-message}

기본 메시지는 단계의 시작점입니다. 각 콘텐츠 구성 요소의 배리언트는 **Content Optimizer 설정** 탭에 정의된 조합에 따라 동적으로 삽입됩니다.

{% alert note %}
베타 기간 동안 지원되는 채널은 이메일, 푸시 알림, 단문 메시지 서비스/MMS/RCS입니다.
{% endalert %}

{% tabs local %}
{% tab 이메일 %}

**메시징 채널** 탭에서 **이메일**을 선택하고 기본 이메일 메시지를 만드세요. 도움이 필요하면 전용 [이메일]({{site.baseurl}}/user_guide/channels/email) 섹션을 참고하세요.

Content Optimizer는 이 배리언트에 지정된 발송 설정(이메일 도메인, 회신 주소 등)을 사용하여 모든 메시지를 발송합니다. 새 디자인으로 시작하거나 이 메시지에 기존 템플릿을 선택할 수 있습니다. 이 단계에서 메시지의 어떤 구성 요소를 최적화할지 고려하세요. 이는 [4단계](#step-4)에서 정의합니다.

최적화 가능한 구성 요소:

- 제목
- 본문 헤더
- 본문 콘텐츠
- 기본 CTA

{% endtab %}
{% tab 푸시 알림 %}

**메시징 채널** 탭에서 **푸시 알림**을 선택하고 기본 푸시 알림을 만드세요. 도움이 필요하면 전용 [푸시]({{site.baseurl}}/user_guide/channels/push) 섹션을 참고하세요.

Content Optimizer는 이 배리언트에 지정된 선택된 푸시 플랫폼을 사용하여 모든 메시지를 발송합니다. 새 디자인으로 시작하거나 이 메시지에 기존 템플릿을 선택할 수 있습니다. 이 단계에서 메시지의 어떤 구성 요소를 최적화할지 고려하세요. 이는 [4단계](#step-4)에서 정의합니다.

최적화 가능한 구성 요소:

- 타이틀
- 메시지

{% endtab %}
{% tab 단문 메시지 서비스/MMS/RCS %}

**메시징 채널** 탭에서 **단문 메시지 서비스/MMS/RCS**를 선택하고 기본 메시지를 만드세요. 도움이 필요하면 전용 [단문 메시지 서비스/MMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) 섹션을 참고하세요.

Content Optimizer는 이 배리언트에 지정된 **콘텐츠** 및 **메시지** 세부 정보를 사용하여 모든 메시지를 발송합니다. 새 디자인으로 시작하거나 이 메시지에 기존 템플릿을 선택할 수 있습니다. 이 단계에서 메시지의 어떤 구성 요소를 최적화할지 고려하세요. 이는 [4단계](#step-4)에서 정의합니다.

최적화 가능한 구성 요소:

- 훅
- 본문
- CTA

{% endtab %}
{% endtabs %}

### 3단계: 전달 설정 지정하기 {#step-3-specify-delivery-settings}

**전달 설정** 탭에서 단계에 Intelligent Timing 또는 전달 유효성 검사를 사용할지 지정할 수 있습니다. 자세한 내용은 메시지 단계의 [전달 설정 편집]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings)을 참고하세요.

### 4단계: 콘텐츠 구성 요소 및 배리언트 추가하기 {#step-4}

콘텐츠 구성 요소는 다른 제목이나 타이틀과 같이 테스트하려는 메시지의 개별 요소입니다. 이러한 구성 요소를 통해 메시지의 여러 버전을 생성하고 시간이 지남에 따라 성능을 기반으로 자동 최적화할 수 있습니다.

- **이메일:** 단계당 최대 3개의 콘텐츠 구성 요소와 구성 요소당 최대 5개의 배리언트를 추가할 수 있으며, 총 125개의 고유 콘텐츠 조합이 가능합니다.
- **푸시 알림:** 단계당 최대 2개의 구성 요소와 구성 요소당 최대 5개의 배리언트를 추가할 수 있으며, 총 25개의 고유 콘텐츠 조합이 가능합니다.
- **단문 메시지 서비스/MMS/RCS:** 단계당 최대 2개의 콘텐츠 구성 요소와 구성 요소당 최대 5개의 배리언트를 추가할 수 있으며, 총 25개의 고유 콘텐츠 조합이 가능합니다.

**AI 제안 생성**을 사용하면 Braze가 배리언트 아이디어를 생성하기 위해 콘텐츠를 OpenAI로 전송합니다. 발송 시점 트래픽 할당은 OpenAI를 사용하지 않습니다. 어떤 데이터가 전송되고 어떻게 사용되는지에 대한 자세한 내용은 [OpenAI 및 Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer#openai-and-content-optimizer)를 참고하세요.

![Content Optimizer 인터페이스에서 콘텐츠 구성 요소를 추가하고 구성하는 옵션. 인터페이스에 제목, 본문 헤더, 본문 콘텐츠, 기본 CTA와 같은 선택 가능한 구성 요소가 표시되며, 각 구성 요소에는 다양한 배리언트를 입력할 수 있는 필드가 있습니다.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### 4.1단계: 콘텐츠 구성 요소 구성하기 {#step-41-configure-content-components}

구성 요소를 구성하려면 **Content Optimizer 설정** 탭으로 이동합니다.

{% tabs local %}
{% tab 이메일 %}

이메일 메시지에 대해 최적화할 구성 요소를 선택합니다. 지원되는 옵션:

- 제목
- 본문 헤더
- 본문 콘텐츠
- 기본 CTA

선택한 각 구성 요소에 대해 해당 콘텐츠의 대안 버전(배리언트) 세트를 정의합니다. 톤, 구조 또는 콘텐츠가 다른 명확하고 구별되는 배리언트를 사용하세요. 이렇게 하면 Content Optimizer가 최고 성과를 내는 배리언트를 더 효과적으로 식별할 수 있습니다. 다음을 수행할 수 있습니다:
  - 수동으로 직접 배리언트를 작성합니다.
  - AI 생성 제안을 사용하여 새로운 옵션을 빠르게 탐색합니다.

![이메일 최적화를 위해 콘텐츠 구성 요소를 추가하고 구성하는 옵션을 보여주는 Content Optimizer 설정 인터페이스. 각 구성 요소에는 다양한 배리언트를 입력할 수 있는 필드가 있습니다. 구성 요소 이름과 배리언트 텍스트를 입력하는 필드가 표시됩니다.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

{% endtab %}
{% tab 푸시 알림 %}

푸시 알림에 대해 최적화할 구성 요소를 선택합니다. 지원되는 옵션:
- 타이틀
- 메시지

선택한 각 구성 요소에 대해 해당 콘텐츠의 대안 버전(배리언트) 세트를 정의합니다. 톤, 구조 또는 콘텐츠가 다른 명확하고 구별되는 배리언트를 사용하세요. 이렇게 하면 Content Optimizer가 최고 성과를 내는 배리언트를 더 효과적으로 식별할 수 있습니다. 다음을 수행할 수 있습니다:
  - 수동으로 직접 배리언트를 작성합니다.
  - AI 생성 제안을 사용하여 새로운 옵션을 빠르게 탐색합니다.

![푸시 최적화를 위해 콘텐츠 구성 요소를 추가하고 구성하는 옵션을 보여주는 Content Optimizer 설정.]({% image_buster /assets/img/content_optimizer/add_content_components_push.png %})

{% endtab %}
{% tab 단문 메시지 서비스/MMS/RCS %}

구독 그룹과 메시지 유형(해당하는 경우)을 선택한 후 단문 메시지 서비스/MMS/RCS에 대해 최적화할 구성 요소를 선택합니다. 지원되는 옵션:
- 훅
- 본문
- CTA
{% alert note %}
단문 메시지 서비스/MMS/RCS Content Optimizer 단계가 시작된 후에는 구독 그룹이나 메시지 유형을 업데이트할 수 없습니다.
{% endalert %}
선택한 각 구성 요소에 대해 해당 콘텐츠의 대안 버전(배리언트) 세트를 정의합니다. 톤, 구조 또는 콘텐츠가 다른 명확하고 구별되는 배리언트를 사용하세요. 이렇게 하면 Content Optimizer가 최고 성과를 내는 배리언트를 더 효과적으로 식별할 수 있습니다. 다음을 수행할 수 있습니다:
  - 수동으로 직접 배리언트를 작성합니다.
  - AI 생성 제안을 사용하여 새로운 옵션을 빠르게 탐색합니다.

![SMS/MMS/RCS 최적화를 위해 콘텐츠 구성 요소를 추가하고 구성하는 옵션을 보여주는 Content Optimizer 설정.]({% image_buster /assets/img/content_optimizer/add_content_components_sms_rcs_mms.png %})

{% endtab %}
{% endtabs %}

#### 4.2단계: 메시지에 Liquid 추가하기 {#step-42-add-liquid-to-your-message}

각 구성 요소에 대해 최소 2개의 배리언트를 정의한 후, 각각에 연결된 Liquid 태그를 복사하여 기본 메시지의 해당 위치에 붙여넣습니다.

- 예를 들어, 제목을 최적화하는 경우 이메일 작성기의 제목 필드에 {% raw %}`{% message_component "Subject" %}`{% endraw %} 태그를 붙여넣습니다.
- 구성 요소 태그를 더 긴 텍스트 안에 포함하여 구성 요소의 일부만 테스트할 수도 있습니다. 예: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![제목, 본문 헤더, 본문 콘텐츠, 기본 CTA와 같은 콘텐츠 구성 요소를 추가하고 구성하는 옵션. 각 구성 요소에는 다양한 배리언트를 입력할 수 있는 필드가 있습니다.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

선택한 콘텐츠 구성 요소에 Liquid 태그를 추가하지 않으면 **Content Optimizer 설정** 탭에 경고가 표시되고 **메시징 채널** 탭에 오류가 표시됩니다. 선택한 모든 구성 요소가 기본 메시지에 올바르게 추가되어야 Canvas를 시작할 수 있습니다.

Canvas가 실행되면 Content Optimizer는 구성 요소 간의 배리언트를 조합하여 다양한 콘텐츠 조합을 생성합니다. 시간이 지남에 따라 더 높은 성과를 보이는 조합이 전달에 우선 적용되어 수동 개입 없이 성능을 개선할 수 있습니다.

#### Liquid 참조 {#liquid-references}

| 채널 | 구성 요소 | Liquid 스니펫 |
| --- | --- | --- |
| 이메일 | 제목 | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| 이메일 | 본문 헤더 | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| 이메일 | 본문 콘텐츠 | {% raw %}`{% message_component "Body Content" %}`{% endraw %} |
| 이메일 | 기본 CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} |
| 푸시 | 타이틀 | {% raw %}`{% message_component "Title" %}`{% endraw %} |
| 푸시 | 메시지 | {% raw %}`{% message_component "Message" %}`{% endraw %} |
| 단문 메시지 서비스/MMS/RCS | 훅 | {% raw %}`{% message_component "Hook" %}`{% endraw %} |
| 단문 메시지 서비스/MMS/RCS | 본문 | {% raw %}`{% message_component "Body" %}`{% endraw %} |
| 단문 메시지 서비스/MMS/RCS | CTA | {% raw %}`{% message_component "CTA" %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid 참조" }

#### 조합 토큰 {#combination-token}

조합 토큰을 사용하여 사용자가 수신한 배리언트 조합을 기록할 수 있습니다. 기본 메시지의 링크에 {% raw %}`{{component_combination_token}}`{% endraw %} Liquid 태그를 추가한 다음, 자체 분석 도구에서 해당 값을 사용하여 다운스트림 행동을 특정 조합에 귀속시킬 수 있습니다.

예를 들어, UTM 매개변수로 링크에 토큰을 추가합니다:

{% raw %}
```liquid
https://www.example.com/summer-sale?utm_content={{component_combination_token}}
```
{% endraw %}

태그는 `3_2_8`과 같이 밑줄로 구분된 숫자 문자열을 렌더링합니다:

- 각 위치는 **Content Optimizer 설정** 탭에 구성 요소가 나타나는 순서대로 하나의 콘텐츠 구성 요소에 해당합니다.
- 각 숫자는 해당 구성 요소에 대해 사용자가 수신한 배리언트의 인덱스입니다. 인덱스는 0부터 시작하므로, `0`은 해당 구성 요소에 대해 만들어진 첫 번째 배리언트이고, `1`은 두 번째입니다.

Braze는 배리언트를 만들 때 인덱스를 할당하며, 해당 단계의 수명 동안 인덱스를 유지합니다. 배리언트를 비활성화할 수는 있지만 삭제할 수는 없으며, 인덱스는 재사용되거나 재번호가 매겨지지 않습니다. 인덱스는 현재 활성화된 배리언트 중에서의 위치를 반영하지 않습니다.

이 때문에 인덱스는 구성 요소당 5개 배리언트 제한이 시사하는 것보다 높아질 수 있습니다. 해당 제한은 활성 배리언트에만 적용되므로, 여러 배리언트를 비활성화하고 새 배리언트를 추가하면 새 배리언트는 5, 6, 7, 8과 같은 인덱스를 가질 수 있습니다.

예를 들어, 이메일 단계에서 제목과 기본 CTA를 최적화합니다. 제목 구성 요소는 5개의 배리언트로 시작했습니다. 이후 3개가 비활성화되고 3개의 새 배리언트가 추가되었습니다:

| 제목 배리언트 | 인덱스 | 상태 |
| --- | --- | --- |
| Your summer sale starts now | 0 | 비활성화됨 |
| Summer sale: 20% off | 1 | 비활성화됨 |
| 20% off, this week only | 2 | 비활성화됨 |
| Save 20% on summer picks | 3 | 활성 |
| Your 20% off code is inside | 4 | 활성 |
| Summer picks, 20% off | 5 | 활성 |
| Don't miss 20% off | 6 | 활성 |
| Last chance: 20% off summer | 7 | 활성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="제목 배리언트 인덱스" }

기본 CTA 구성 요소에는 인덱스 0과 1의 두 배리언트가 있습니다. 이 단계에서 `6_1` 토큰은 사용자가 인덱스 6의 제목 배리언트("Don't miss 20% off")와 인덱스 1의 기본 CTA 배리언트를 수신했음을 의미합니다.

### 5단계: 최적화 이벤트 선택하기 {#step-5-select-optimization-event}

최적화 이벤트는 Content Optimizer가 성능을 평가하고 시간이 지남에 따라 콘텐츠 조합에 트래픽을 할당하는 방법을 결정합니다.

선택한 최적화 이벤트는 이 단계의 모든 콘텐츠 구성 요소에 적용됩니다.

{% tabs local %}
{% tab 이메일 %}

이메일의 경우 다음 이벤트 중 하나에 대해 최적화할 수 있습니다. Content Optimizer는 메시지 발송 후 7일 이내에 등록된 열람 및 클릭을 사용하여 더 높은 성과를 보이는 콘텐츠 조합으로 전달을 전환합니다.

| 이벤트 | 설명 | 사용 사례 |
| --- | --- | --- |
| 열람 | 수신자가 이메일을 열도록 유도하는 조합에 최적화합니다. | 제목 테스트 또는 가시성 향상 목적 |
| 클릭 | 링크 참여를 유도하는 조합에 최적화합니다. 봇 클릭 또는 Braze가 인식한 수신 거부 클릭은 포함되지 않습니다. | 링크에서의 트래픽, 참여 또는 전환 유도 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="5단계: 최적화 이벤트 선택" }

#### 최적화에서 링크 제외하기 {#exclude-links-from-optimization}

클릭에 대해 최적화할 때 하나 이상의 링크를 최적화에서 제외할 수 있습니다. 환경 설정 센터나 매장 찾기와 같이 테스트 중인 콘텐츠에 대한 참여를 나타내지 않는 링크에 사용합니다.

링크를 제외하려면 **Content Optimizer 설정** 탭으로 이동하여 링크 URL을 추가합니다. Braze는 접두사로 매칭하므로, 메시지 내 URL 중 지정한 URL로 시작하는 모든 URL에 대한 클릭이 제외됩니다.

제외된 클릭은 최적화 이벤트에 포함되지 않으므로 Content Optimizer가 선호하는 조합에 영향을 미치지 않습니다. 제외된 클릭은 여전히 단계의 전체 분석에 포함되며, [구성 요소별 성능](#performance-by-component) 또는 [조합별 성능](#performance-by-combination) 표에는 포함되지 않습니다.

{% endtab %}
{% tab 푸시 알림 %}

푸시 알림의 경우 **열람**에 대해 최적화할 수 있습니다. 이는 수신자가 푸시 알림을 열도록 유도하는 조합에 최적화합니다. 이 최적화 이벤트를 사용하여 타이틀이나 메시지 카피의 변형을 테스트할 수 있습니다.

{% endtab %}
{% tab 단문 메시지 서비스/MMS/RCS %}

단문 메시지 서비스 및 MMS 메시지의 경우 **클릭**에 대해 최적화할 수 있습니다. RCS 메시지의 경우 **읽음** 또는 **클릭**에 대해 최적화할 수 있습니다.

단계에 최적화할 이벤트가 있으려면:
- 단문 메시지 서비스 및 MMS 메시지에는 링크가 포함되어야 합니다.
- RCS 메시지에는 링크 또는 제안된 답장이 포함되어야 합니다.

{% alert note %}
현재 Content Optimizer를 사용한 RCS 메시징은 단문 메시지 서비스 대체를 지원하지 않습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 단계 상태 {#step-states}

Content Optimizer 단계가 실행되면, Braze는 콘텐츠 배리언트 성능을 평가하고 Canvas에서 볼 수 있는 세 가지 상태 중 하나를 단계에 할당합니다.

| 상태 | 의미 |
| --- | --- |
| 학습 중 | Content Optimizer가 콘텐츠 배리언트 전반의 성능 데이터를 수집하는 중이며, 아직 일관되고 신뢰할 수 있는 우승자를 찾지 못한 상태입니다. |
| 최적화 중 | Content Optimizer가 지속적으로 다른 배리언트보다 우수한 성능을 보이는 배리언트를 찾았으며, 우승 조합을 향해 발송을 전환하고 있습니다. |
| 조치 권장 | 명확한 우승자가 나타나지 않은 채로 단계가 일정 시간 동안 실행되었습니다. Content Optimizer가 우승자를 찾을 수 있도록 단계 설정을 검토하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Optimizer 단계 상태" }

### 고려할 조치 {#actions-to-consider}

단계가 조치 권장 상태에 진입하면 다음 사항을 고려하세요.

- 가능하다면 Canvas에 진입하는 사용자 수를 늘리세요. 더 많은 발송이 이루어질수록 Content Optimizer가 학습할 수 있는 데이터가 더 많아집니다.
- 일반적으로 조합 수를 줄이기보다는 더 많이 테스트하세요([모범 사례](#best-practices) 참조). 이렇게 하면 Content Optimizer가 무엇이 우수한지 더 명확한 신호를 얻을 수 있습니다. 오디언스 볼륨이 적은 경우(하루 평균 약 3,000건 미만의 발송), 볼륨 대비 조합이 너무 많으면 학습이 느려질 수 있으므로 배리언트 수를 약간 줄이는 것을 고려하세요.
- 콘텐츠 배리언트의 톤, 구조 또는 콘텐츠를 서로 더 명확하게 구별되도록 만드세요.
- 오디언스를 늘릴 수 없고 배리언트 수와 콘텐츠 다양성이 이미 적절해 보인다면, 단계에 우승자를 찾기 위해 단순히 더 많은 시간이 필요할 수 있습니다.

## 런칭된 단계 편집하기 {#edit-a-launched-step}

Canvas가 런칭된 후에도 Canvas 편집기에서 실행 중인 콘텐츠 옵티마이저 단계를 열어 업데이트할 수 있습니다. 다음 작업이 가능합니다:

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

{% alert note %}
Braze는 사용자가 콘텐츠 옵티마이저 단계에 진입할 때 각 사용자에게 콘텐츠 조합을 할당합니다. 사용량 제한, Intelligent Timing 또는 방해금지 시간과 같은 전송 제어로 인해 발송이 지연되는 경우, 비활성화한 배리언트를 여전히 수신할 수 있습니다. 이러한 발송을 긴급하게 중지하려면 메시지 단계와 동일한 절차를 따르세요. 자세한 내용은 [Canvases 중지하기]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases)를 참조하세요.
{% endalert %}

변경 사항을 게시하면 옵티마이저가 초기화되고 모든 활성 배리언트 및 조합에 대해 트래픽을 처음부터 다시 할당하기 시작합니다. 단계가 학습 상태에 있는 동안에는 배리언트를 업데이트하지 마세요. 편집 이전의 히스토리 데이터는 유지되며 **Content Analytics** 탭에서 확인할 수 있습니다.

런칭 후에는 다음 설정을 변경할 수 없습니다:

- 기존 활성 배리언트의 콘텐츠
- 테스트 중인 구성 요소
- 최적화 이벤트

단문 메시지 서비스/MMS/RCS 단계의 경우, 구독 그룹과 메시지 유형도 런칭 후에는 변경할 수 없습니다.

## 모범 사례 {#best-practices}

- 일반적으로 Content Optimizer 단계에서는 테스트하는 구성 요소가 적은 것보다 많은 것이 좋습니다. 예를 들어, 이메일에서 두 개의 구성 요소를 테스트하는 대신 세 개를 테스트하세요.
- 최소 10개 이상의 조합을 테스트하면 더 나은 결과를 얻을 수 있습니다.
- 이메일의 경우, 클릭을 최적화하는 단계가 열람을 최적화하는 단계보다 더 나은 성과를 보이는 경향이 있습니다. 클릭이 사용 사례에 적합하다면 최적화 이벤트로 클릭을 선택하세요.
- Content Optimizer를 처음 사용하는 경우, [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) 단계를 사용하여 오디언스의 일부만 Content Optimizer 단계가 포함된 분기로 진입하도록 하는 것이 좋습니다. 예를 들어, 사용자의 절반은 Content Optimizer 단계가 있는 경로로 보내고, 나머지 절반은 현재 기존 콘텐츠를 담은 메시지 단계를 전송하는 대조 경로로 보낼 수 있습니다. 그런 다음 2~3주간 데이터를 수집하고, Content Optimizer 단계가 있는 경로로 트래픽을 늘리기 전에 KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or 핵심 성과 지표(KPI or 핵심 성과 지표(KPI)) 또는 반대 측정기준을 비교하세요.
  - 효과적인 일대일 비교를 위해, Content Optimizer 단계의 각 구성 요소에서 배리언트 중 하나로 기존 콘텐츠를 포함하세요.
- Content Optimizer 단계가 일정 기간 동안 최적화 상태에 있은 후 업데이트할 준비가 되면, 성과가 낮은 배리언트를 비활성화하고 최고 성과 배리언트의 특성을 기반으로 한 새로운 배리언트를 추가하세요.

## 고려 사항 {#considerations}

- Content Optimizer 단계에서는 다국어 설정이 지원되지 않습니다. 대신 언어별로 하나의 Content Optimizer 단계를 사용하고 경로를 개별적으로 분기하세요.
- Content Optimizer 구성 요소의 Liquid 태그는 메시지 단계에서 지원되지 않으므로, 메시지 단계에서 Liquid가 중단됩니다.
- Content Optimizer 단계가 시작된 후에는 테스트 중인 구성 요소, 기존 활성 배리언트의 콘텐츠 또는 최적화 이벤트를 변경할 수 없습니다. 단문 메시지 서비스/MMS/RCS 단계의 경우 구독 그룹과 메시지 유형도 변경할 수 없습니다.

## 분석 {#analytics}

성과를 확인하려면 단계 수준 분석 패널을 열어 콘텐츠 배리언트별 측정기준과 전체 조합 성과를 확인하세요. Content Optimizer 단계는 [메시지 단계와 동일한 분석]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#analytics)을 사용합니다.

출시 후 단계를 업데이트한 경우, 발송 할당 차트에 각 콘텐츠 편집이 발생한 시점이 표시됩니다. 비활성화된 배리언트의 데이터는 유지되며 분석 패널에서 계속 확인할 수 있으므로, 단계의 전체 기간에 걸쳐 성과를 비교할 수 있습니다.

![세 가지 버튼과 발송 할당 비율이 상승 추세를 보이는 Content Optimizer 분석.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

### 구성 요소별 성과 {#performance-by-component}

**구성 요소별 성과** 섹션에는 Content Optimizer 단계의 각 구성 요소별 성과가 표시됩니다. **구성 요소** 열은 테스트 중인 콘텐츠 구성 요소(예: **제목란** 또는 **기본 CTA**)와 일치합니다. **식별자** 열은 **Content Optimizer 설정** 탭에서 해당 배리언트의 식별자와 일치합니다.

고유 열람 및 클릭은 메시지 발송 후 7일 이내에 수집됩니다. 표시되는 열은 채널 및 선택한 최적화 이벤트에 따라 다릅니다.

| 측정기준 | 설명 |
| --- | --- |
| 발송 | 이 단계에서 해당 구성 요소의 이 배리언트에 귀속된 발송 수로, [구성 조합별 성과](#performance-by-combination) 표의 [*발송*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends)과 동일한 단계 수준 발송 카운트를 사용합니다. |
| 열람 | 채널에 이 열이 표시되는 경우, 발송 후 7일 이내에 이 배리언트에 대한 **고유** 열람 수입니다. [*고유 열람*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens)을 참조하세요. |
| 열람율 | 이 열이 표시되는 경우, 7일 이내에 최소 1회 이상의 유효한 고유 열람을 기록한 이 배리언트의 발송 비율입니다. |
| 클릭 | 발송 후 7일 이내에 이 배리언트에 대한 **고유** 클릭 수입니다. [*총 클릭*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks), [*고유 클릭*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks), [5단계: 최적화 이벤트 선택](#step-5-select-optimization-event)을 참조하세요. |
| 클릭률 | 7일 이내에 최소 1회 이상의 유효한 고유 클릭을 기록한 이 배리언트의 발송 비율로, [구성 조합별 성과](#performance-by-combination) 표와 동일한 단계 기간을 사용합니다. 자세한 내용은 [단계 분석이 일반 분석과 다른 이유](#why-step-analytics-differ-from-general-analytics)를 참조하세요. |
| 읽음 | 이 열이 표시되는 경우(예: 읽음 최적화 시 RCS), 읽음 확인이 활성화된 소비자가 메시지를 읽은 횟수입니다. [*읽음*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads)을 참조하세요. |
| 읽음율 | 읽음 확인이 활성화된 사용자 중 이 배리언트의 발송에서 읽음이 발생한 비율입니다. [*읽음율*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="구성 요소별 성과 측정기준" }

![구성 요소별로 별도의 표에 각 배리언트의 발송, 클릭, 클릭률이 나열된 Content Optimizer 구성 요소별 성과 분석.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_component.png %})

### 구성 조합별 성과 {#performance-by-combination}

**구성 조합별 성과** 섹션에는 Content Optimizer 단계의 각 조합별 성과가 표시됩니다. 조합은 이 행을 정의하는 배리언트의 구성입니다—테스트 중인 각 콘텐츠 구성 요소에서 선택된 배리언트 하나씩(예: 제목란과 기본 CTA의 조합).

고유 열람 및 클릭은 메시지 발송 후 7일 이내에 수집됩니다. 표시되는 열은 채널 및 선택한 최적화 이벤트에 따라 다릅니다.

| 측정기준 | 설명 |
| --- | --- |
| 발송 | 이 조합을 사용하여 이 단계에서 발송된 총 메시지 수입니다. 카운트는 각 조합으로 범위가 지정된 [*발송*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#sends)과 동일한 일반적 의미를 따릅니다. |
| 열람 | 발송 후 7일 이내에 이 조합에 대한 고유 열람 수입니다. 이메일의 고유 열람 정의 방법은 [*고유 열람*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-opens)을 참조하세요. |
| 열람율 | 7일 이내에 최소 1회 이상의 유효한 고유 열람을 기록한 이 조합의 발송 비율입니다. |
| 클릭 | 발송 후 7일 이내에 이 조합에 대한 고유 클릭 수입니다. Braze에서 채널별 클릭을 정의하는 방법은 [*총 클릭*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#total-clicks) 및 [*고유 클릭*]({{site.baseurl}}/user_guide/analytics/metrics_glossary#unique-clicks)을 참조하세요. |
| 클릭률 | 7일 이내에 최소 1회 이상의 유효한 고유 클릭을 기록한 이 조합의 발송 비율입니다. Content Optimizer는 단계의 7일 중복 제거 카운트를 사용하므로, 이 비율은 일반 Campaign 분석의 클릭률과 일치하지 않을 수 있습니다. 자세한 내용은 [단계 분석이 일반 분석과 다른 이유](#why-step-analytics-differ-from-general-analytics)를 참조하세요. |
| [읽음]({{site.baseurl}}/user_guide/analytics/metrics_glossary#reads) | 이 열이 표시되는 경우(예: 읽음 최적화 시 RCS), 읽음 확인이 활성화된 소비자가 메시지를 읽은 횟수입니다. |
| [읽음율]({{site.baseurl}}/user_guide/analytics/metrics_glossary#read-rate) | 이 열이 표시되는 경우, 읽음 확인이 활성화된 사용자 중 이 조합의 발송에서 읽음이 발생한 비율입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="구성 조합별 성과 측정기준" }

![각 콘텐츠 조합의 발송, 클릭, 클릭률이 포함된 Content Optimizer 구성 조합별 성과 분석 표.]({% image_buster /assets/img/content_optimizer/analytics_performance_by_combination.png %})

### 단계 분석이 일반 분석과 다른 이유 {#why-step-analytics-differ-from-general-analytics}

Content Optimizer 단계의 분석이 **Analytics** 섹션과 다른 이유는 다음과 같습니다.

- 푸시 발송은 동일한 사용자에게 여러 기기로 보낸 발송에 대해 중복 제거됩니다.
- 일반적으로 클릭과 열람은 각 사용자에 대해 고유하게 중복 제거됩니다.
- Content Optimizer 단계에서는 메시지 발송 후 7일 이내에 발생한 클릭과 열람만 집계됩니다.
- 제외된 링크 클릭은 단계의 전체 분석에는 집계되지만 **구성 요소별 성과** 또는 **구성 조합별 성과** 표에는 집계되지 않습니다. 자세한 내용은 [최적화에서 링크 제외](#exclude-links-from-optimization)를 참조하세요.

### 사용자 프로필에서 배리언트 확인 {#view-variants-on-a-user-profile}

개별 사용자가 수신한 배리언트를 확인하려면 해당 사용자 프로필을 열고 **메시지 기록** 탭으로 이동하세요. Content Optimizer 단계의 발송 이벤트 행에서, 표에 해당 사용자에게 발송된 구성 요소 배리언트가 표시됩니다. 자세한 내용은 [메시지 기록 탭]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)을 참조하세요.

### 보고서 빌더에서 단계 비교 {#compare-steps-in-report-builder}

둘 이상의 Content Optimizer 단계에 걸쳐 성과를 비교하려면 보고서를 생성하고 **Canvas Step with Canvas Optimizer**를 선택하세요. 보고서에는 포함된 단계의 구성 요소별 및 조합별 단계 성과가 표시되며, 해당 단계가 동일한 Canvas에 있든 서로 다른 Canvases에 있든 상관없습니다. 자세한 내용은 [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder)를 참조하세요.

## 문제 해결 {#troubleshooting}

| 문제 | 설명 | 해결 방법 |
| --- | --- | --- |
| 누락된 Liquid 태그 | 콘텐츠 구성요소(예: 제목 또는 CTA)를 추가했지만 기본 메시지에 해당 Liquid 태그를 삽입하지 않으면 다음과 같은 문제가 발생합니다: <br>- **Content Optimizer Settings** 탭에 경고 표시 <br>- **메시징 채널** 탭에 오류 표시 | **Content Optimizer Settings** 탭에서 각 구성요소 아래에 표시된 Liquid 스니펫을 복사하여 메시지의 적절한 위치에 붙여넣으세요. |
| 고아 Liquid 태그 | 콘텐츠 구성요소를 삭제했지만 기본 메시지에 해당 Liquid 태그가 남아 있으면 발송 시 메시지가 예상대로 렌더링되지 않을 수 있습니다. | 실행 전에 기본 메시지에서 사용하지 않는 `message_component` 태그를 모두 제거하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="문제 해결" }