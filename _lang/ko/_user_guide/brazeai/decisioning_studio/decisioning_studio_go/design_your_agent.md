---
nav_title: 에이전트 설계
article_title: 에이전트 설계
page_order: 3
description: "오디언스 정의, 차원, Go 관련 제한 사항을 포함하여 BrazeAI Decisioning Studio Go 에이전트를 설계하는 방법을 알아봅니다."
---

# 에이전트 설계 {#design-your-agent}

> 이 문서에서는 오디언스 정의, 차원 선택, Go 관련 기능 및 제한 사항 이해를 포함하여 Decisioning Studio Go 에이전트를 설계하는 방법을 다룹니다.

의사결정 에이전트에 대한 기본 개념(성공 측정기준, 차원, 액션 뱅크, 제약 조건 등)은 [의사결정 에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)를 참조하세요.

## Go와 Pro 기능 비교 {#go-versus-pro-capabilities}

Decisioning Studio Go는 Decisioning Studio Pro에 비해 간소화된 기능을 갖춘 셀프 서비스 플랫폼입니다. 이러한 차이를 이해하면 Go의 범위 내에서 효과적인 에이전트를 설계하는 데 도움이 됩니다.

| 기능 | Decisioning Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **성공 측정기준** | 클릭만 | 모든 비즈니스 측정기준(매출, 전환 또는 ARPU) |
| **차원** | 제한된 액션 뱅크 | 무제한 차원 |
| **지원되는 CEP** | Braze, SFMC | 모든 CEP(네이티브 및 커스텀) |
| **고객 데이터** | 인게이지먼트만 | 모든 1P 데이터 |
| **설정** | 셀프 서비스 | AI Decisioning 서비스 지원 |
| **실험 그룹** | Go + 랜덤 제어 + 선택적 BAU | 완전 맞춤형 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Go와 Pro 기능 비교" }

## Go 에이전트 설계 {#design-your-go-agent}

Decisioning Studio Go 에이전트를 설계할 때 다음 영역에서 결정을 내리게 됩니다.

### 1단계: 오디언스 정의 {#step-1-define-your-audience}

오디언스는 에이전트가 참여시킬 고객 집합입니다. Go에서 오디언스는 CEP에서 정의됩니다.

{% tabs %}
{% tab Braze %}

**Braze에서 오디언스 정의:**

1. 에이전트가 타겟으로 삼을 고객을 정의하는 Segment를 Braze에서 생성합니다.
2. Decisioning Studio Go 포털에서 실험자를 구성할 때 이 Segment를 타겟 오디언스로 선택합니다.

{% alert tip %}
테스트를 격리하고 측정 가능하게 유지하기 위해 Decisioning Studio Go 실험자 전용 Segment를 만드는 것을 고려하세요.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**SFMC에서 오디언스 정의:**

1. 타겟 오디언스를 포함하는 Data Extension을 구성합니다.
2. 이 Data Extension을 최신 고객 데이터로 매일 새로고침합니다.
3. 실험자를 구성할 때 Decisioning Studio Go 포털에서 이 Data Extension을 참조합니다.

{% endtab %}
{% endtabs %}

### 2단계: 차원 선택 {#step-2-select-your-dimensions}

차원은 에이전트가 고객 경험을 개인화하기 위해 조작할 수 있는 "레버"입니다. 여기에는 제목란 및 히어로 이미지와 같은 크리에이티브 차원과 이메일 빈도 또는 발송 시간과 같은 발송 유형 차원이 포함됩니다.

{% alert note %}
사용 가능한 특정 차원은 CEP 및 Campaign 구성 방식에 따라 다릅니다. CEP에서 이미 설정된 템플릿과 콘텐츠를 사용하세요.
{% endalert %}

### 3단계: 액션 뱅크 구성 {#step-3-configure-your-action-bank}

액션 뱅크는 에이전트가 각 차원에 대해 선택할 수 있는 특정 옵션을 정의합니다. 예를 들어:

- **이메일 템플릿:** 에이전트가 사용할 수 있는 템플릿을 선택합니다(이 템플릿은 먼저 CEP에서 구성되어야 합니다).
- **제목란:** 에이전트가 테스트할 수 있는 제목란 배리언트를 정의합니다.
- **발송 시간:** 에이전트가 선택할 수 있는 시간 범위를 지정합니다.

### 4단계: 실험 그룹 설정 {#step-4-set-up-experiment-groups}

Decisioning Studio Go는 성과를 측정하기 위해 자동으로 실험 그룹을 생성합니다.

| 그룹 | 설명 |
|-------|-------------|
| **Decisioning Studio Go** | 인공지능 최적화 추천을 받는 고객 |
| **랜덤 제어** | 무작위로 선택된 옵션을 받는 고객(기준 비교) |
| **일상적인 비즈니스(선택 사항)** | 현재 성과와 비교하는 경우 기존 Campaign을 받는 고객 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4단계: 실험 그룹 설정" }

{% alert important %}
정확한 비교를 위해 고객은 하나의 실험 그룹에만 속할 수 있으며, 편향 없이 무작위로 그룹에 배정됩니다.
{% endalert %}

## 고려해야 할 제한 사항 {#limitations-to-consider}

Go 에이전트를 설계할 때 다음 제한 사항을 염두에 두세요.

- **클릭만 해당:** Go는 클릭률을 최적화합니다. 매출, 전환 또는 기타 비즈니스 측정기준을 최적화해야 하는 경우 Decisioning Studio Pro를 고려하세요.
- **제한된 차원:** Go는 미리 정의된 차원 집합을 지원합니다. 커스텀 차원이나 복잡한 개인화를 위해서는 Decisioning Studio Pro를 고려하세요.
- **제한된 CEP 지원:** Go는 Braze 및 Salesforce Marketing Cloud와만 통합됩니다. 다른 플랫폼의 경우 Decisioning Studio Pro를 고려하세요.

## 모범 사례 {#best-practices}

- **좁은 범위로 시작하세요:** 2~3개의 템플릿 또는 제목란 배리언트로 시작하세요. 이렇게 하면 에이전트가 학습할 수 있는 충분한 옵션을 제공하면서 실험을 관리 가능하게 유지할 수 있습니다.
- **시간을 주세요:** 에이전트는 학습하기 위해 충분한 데이터가 필요합니다. 성과에 대한 결론을 내리기 전에 최소 2~4주를 허용하세요.
- **콘텐츠를 다양하게 유지하세요:** 의미 있게 다른 옵션을 사용하세요. 사소한 변형을 테스트하면 유의미한 인사이트를 얻지 못할 수 있습니다.
- **정기적으로 모니터링하세요:** Decisioning Studio Go 포털에서 실험 진행 상황 및 인게이지먼트 측정기준을 확인하세요.

## 다음 단계 {#next-steps}

에이전트를 설계한 후 Braze 대시보드에서 구성하고 시작하세요.

- [Decisioning Studio Go 에이전트 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)