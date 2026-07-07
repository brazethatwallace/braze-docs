---
nav_title: 데이터 소스 연결
article_title: 데이터 소스 연결
page_order: 1
description: "BrazeAI Decisioning Studio Go가 고객 참여 플랫폼을 통해 고객 데이터에 연결되는 방법을 알아보세요."
---

# 데이터 소스 연결 {#connect-data-sources}

> BrazeAI Decisioning Studio™ Go는 고객 참여 플랫폼(CEP)을 통해 고객 데이터에 연결합니다. 이 문서에서는 어떤 데이터가 사용되며 연결이 어떻게 작동하는지 설명합니다.

## Go가 고객 데이터에 접근하는 방법 {#how-go-accesses-customer-data}

다양한 소스와의 직접적인 데이터 통합을 지원하는 Decisioning Studio Pro와 달리, Decisioning Studio Go는 CEP를 통해 고객 데이터에 접근합니다. 이는 다음과 같은 의미입니다:

- **오디언스 데이터**는 CEP(Braze 또는 Salesforce Marketing Cloud)에서 정의된 Segments 또는 리스트에서 직접 가져오며, 특정 사전 정의된 속성(1P 데이터 제외)만 포함할 수 있습니다.
- **참여 데이터**(열람, 클릭, 발송)는 자동화된 쿼리 또는 CEP와의 네이티브 통합을 통해 수집됩니다.
- CEP에서 구성하는 것 외에 **추가적인 데이터 파이프라인 설정은** 필요하지 않습니다.

## 지원되는 통합 패턴 {#supported-integration-patterns}

Decisioning Studio Go는 데이터 접근을 위해 다음 CEP를 지원합니다:

| CEP | 오디언스 소스 | 참여 데이터 |
|-----|-----------------|-----------------|
| **Braze** | Segments | Braze 커런츠 내보내기 |
| **Salesforce Marketing Cloud** | 데이터 확장 | SQL 쿼리 자동화 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 통합 패턴" }

## CEP별 데이터 요구사항 {#data-requirements-by-cep}

{% tabs %}
{% tab Braze %}

### Braze 데이터 요구사항 {#braze-data-requirements}

Braze 통합을 위해 Decisioning Studio Go에는 다음이 필요합니다:

1. **Braze 커런츠:** Braze 커런츠를 활성화하고 구성하여 참여 데이터를 Decisioning Studio Go로 내보내야 합니다. 이를 통해 에이전트가 고객 응답으로부터 학습할 수 있습니다.

2. **Segment 접근:** 생성하는 API 키는 타겟 오디언스를 정의하는 Segments에 접근할 수 있는 권한을 가져야 합니다.

3. **고객 프로필 데이터:** 에이전트가 고려해야 하는 모든 고객 프로필 속성 또는 커스텀 속성은 Braze API를 통해 접근 가능해야 합니다.

{% alert important %}
Braze 커런츠 내보내기에 비교 대상 Campaigns(BAU Campaigns 포함)의 데이터가 반드시 포함되어 있는지 확인하세요.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMC 데이터 요구사항 {#sfmc-data-requirements}

Salesforce Marketing Cloud 통합을 위해 Decisioning Studio Go에는 다음이 필요합니다:

1. **데이터 확장:** 오디언스는 Decisioning Studio Go가 접근할 수 있는 데이터 확장에 정의되어야 합니다. SubscriberKey를 기본 사용자 식별자로 사용하세요.
2. **추적 이벤트 접근:** 설치된 앱 패키지가 종단 간 자동화 설정을 지원하는 한, 추가 구성은 필요하지 않습니다.

데이터 확장 및 SQL 쿼리는 [오케스트레이션 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration)의 일부로 구성됩니다.

{% endtab %}
{% endtabs %}

## 모범 사례 {#best-practices}

- **데이터를 최신 상태로 유지하세요:** 오디언스 Segments와 고객 데이터를 정기적으로(최소 매일) 업데이트하여 에이전트가 최신 정보로 작동할 수 있도록 하세요.
- **관련 속성을 포함하세요:** 어떤 고객 특성이 메시지 공감에 영향을 미칠 수 있는지 고려해 보세요. 인구통계학적 특성, 참여 이력, 구매 행동, 라이프사이클 단계 등이 모두 유용한 신호입니다.

## 다음 단계 {#next-steps}

Go가 데이터에 연결되는 방식을 이해하셨으니, 이제 CEP 통합 설정을 진행하세요:

- [오케스트레이션 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration)