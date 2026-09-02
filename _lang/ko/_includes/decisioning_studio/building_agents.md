# AI 의사결정 에이전트 구축 {#building-ai-decisioning-agents}

> BrazeAI Decisioning Studio™를 위한 에이전트를 구축하여 수동 A/B 테스트 없이도 개인화된 실험을 자동화하고 전환, 리텐션, 매출 등의 결과를 최적화하는 방법을 알아보세요.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## 에이전트 정보 {#about-agents}

AI 의사결정 에이전트는 특정 비즈니스 목표를 달성하기 위해 맞춤 구성된 BrazeAI<sup>TM</sup> 의사결정 엔진의 커스텀 설정입니다.

예를 들어, 초기 구매 후 후속 전환을 높이기 위한 재구매 에이전트를 구축할 수 있습니다. Braze에서 오디언스와 메시지를 정의하면, 의사결정 에이전트가 매일 실험을 실행하여 각 고객에게 제품 오퍼, 메시지 타이밍, 빈도의 다양한 조합을 자동으로 테스트합니다. 시간이 지나면서 BrazeAI<sup>TM</sup>는 가장 효과적인 방법을 학습하고, 재구매율을 극대화하기 위해 Braze를 통해 개인화된 발송을 조율합니다.

좋은 에이전트를 구축하려면 다음을 수행합니다:

- BrazeAI<sup>TM</sup>가 최적화할 성공 지표(예: 매출, 전환, ARPU)를 선택합니다.
- 테스트할 차원(예: 오퍼, 제목란, 크리에이티브, 채널, 발송 시간)을 정의합니다.
- 각 차원의 옵션(예: 이메일 대 SMS, 또는 일일 대 주간 빈도)을 선택합니다.

![추천 이메일을 위한 Decisioning Studio 에이전트 예시 다이어그램]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## 샘플 에이전트 {#sample-agents}

다음은 BrazeAI Decisioning Studio™로 구축할 수 있는 에이전트의 몇 가지 예시입니다. AI 의사결정 에이전트는 모든 고객 상호작용에서 학습하고 그 인사이트를 다음 날의 액션에 적용합니다.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## 에이전트 구축 {#building-an-agent}

### 전제 조건 {#prerequisites}

에이전트를 구축하기 전에 [BrazeAI Decisioning Studio™를 통합]({{site.baseurl}}/developer_guide/decisioning_studio/integration)해야 합니다.

### 1단계: AI Expert Services에 문의하기 {#step-1-contact-ai-expert-services}

AI Expert Services 팀이 여러분과 긴밀하게 협력하여 의사결정 에이전트의 범위를 정하고, 설계하고, 구축합니다. 아직 문의하지 않으셨다면 [문의하기](https://www.braze.com/get-started/)를 통해 시작하세요.

여러분에게 적합한 커스텀 에이전트를 구축하기 위해 다음 단계를 함께 완료하게 됩니다.

### 2단계: 에이전트 설계하기 {#step-2-design-your-agent}

AI Expert Services 팀과 함께 다음 사항을 정의합니다:

- 타겟 오디언스,
- 최적화할 비즈니스 지표,
- BrazeAI<sup>TM</sup> 의사결정 에이전트의 액션,
- 비즈니스 성과를 달성하기 위해 에이전트가 레버리지해야 할 퍼스트파티 고객 데이터.

설계가 완료되면, 팀은 여러분과 함께 추가 통합 요구 사항을 파악하고 완료합니다.

### 3단계: 전달 플랫폼 설정하기 {#step-3-set-up-your-delivery-platform}

다음으로, AI Expert Service 팀이 고객 인게이지먼트 플랫폼 설정을 도와드립니다. Decisioning Studio는 Braze와 가장 잘 작동하지만, 다양한 다른 플랫폼도 지원됩니다&#8212;추가 리소스는 AI Expert Service 팀에 문의하세요.

{% tabs local %}
{% tab Braze %}
Braze를 설정하려면:

1. [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) 또는 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=api-triggered%20delivery#step-12-determine-your-canvas-entry-schedule)를 생성합니다. BrazeAI Decisioning Studio™는 이 전달 방법을 사용하여 정의된 오디언스의 사용자에게 1:1 개인화된 활성화 이벤트를 전송합니다.
2. Braze [대조군]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)은 포함하지 않도록 합니다. 대신 BrazeAI<sup>TM</sup>가 전용 대조군 역할을 합니다.
3. 사용하는 차원에 따라 크리에이티브 콘텐츠에 Liquid 태그를 구성하여 BrazeAI<sup>TM</sup> 추천으로 메시징을 동적으로 채울 수 있습니다. BrazeAI<sup>TM</sup>는 Braze API를 사용하여 고객별 콘텐츠를 템플릿의 Liquid 태그에 전달합니다.
{% endtab %}
{% endtabs %}

### 4단계: 출시 및 모니터링 {#step-4-launch-and-monitor}

에이전트를 출시한 후, AI Expert Services 팀이 합의된 설계에 맞게 계속해서 모니터링하고 튜닝합니다. 필요한 경우 에이전트에 대한 조정, 확장 또는 수정도 도와드립니다.