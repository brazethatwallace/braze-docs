---
nav_title: 에이전트 시작하기
article_title: 에이전트 시작하기
page_order: 4
description: "BrazeAI Decisioning Studio Go 에이전트를 시작하고 성능 비교를 위한 BAU(Business as Usual) 보고를 설정하는 방법을 알아봅니다."
---

# 에이전트 시작하기 {#launch-your-agent}

> 데이터 소스를 연결하고, 오케스트레이션을 설정하고, 에이전트를 설계한 후에는 시작할 준비가 된 것입니다. 이 문서에서는 에이전트를 활성화하고 선택적 BAU 보고를 설정하는 방법을 다룹니다.

## 시작 단계 {#launch-steps}

Decisioning Studio Go 포털에서 모든 구성 단계를 완료한 후:

1. 모든 설정이 올바른지 에이전트 구성을 검토합니다.
2. CEP 통합이 활성 상태이고 오케스트레이션이 준비되었는지 확인합니다.
3. Decisioning Studio Go 포털에서 **Launch**(또는 동등한 동작)를 선택하여 에이전트를 활성화합니다.

시작되면 에이전트는 다음을 수행합니다:
- CEP로부터 오디언스 데이터 수신을 시작합니다
- 각 고객에 대해 개인화된 추천을 제공하기 시작합니다
- 구성된 CEP를 통해 발송을 오케스트레이션합니다
- 참여 데이터를 수집하여 시간이 지남에 따라 학습하고 개선합니다

## BAU 보고 설정하기 {#set-up-bau-reporting}

기본적으로 Decisioning Studio Go 포털 보고는 Decisioning Studio Go 그룹을 무작위 대조군과 비교합니다. 비교하고 싶은 기존 BAU(Business as Usual) Campaign이 있는 경우, BAU 보고를 설정하여 세 그룹을 한 곳에서 확인할 수 있습니다.

### BAU 보고의 이점 {#benefits-of-bau-reporting}

BAU 보고를 설정하는 주요 이점은 Decisioning Studio Go의 무효 클릭 필터링을 적용할 수 있다는 것입니다. 세 실험 그룹 모두에 적용하면 다음의 노이즈를 제거하여 가장 정확하고 공정한("동일 조건") 클릭 성과 비교가 가능합니다:
- 기계에 의한 것으로 의심되는 클릭
- 구독 취소 링크 클릭

### BAU 보고 요구 사항 {#requirements-for-bau-reporting}

BAU 보고를 설정하기 전에 BAU 처리 그룹, Decisioning Studio Go 그룹, 무작위 대조군 간의 동일 조건 비교를 보장해야 합니다:

- **중복 없음:** 실험 전체 기간 동안 어떤 수신자도 둘 이상의 그룹에 속할 수 없습니다
- **무작위 배정:** 수신자는 편향 없이 그룹에 무작위로 배정됩니다
- **동등한 옵션:** BAU 그룹에 제공되는 모든 옵션(크리에이티브, 빈도, 시간, 인센티브 또는 오퍼)이 Decisioning Studio Go 및 무작위 대조군에도 제공됩니다

{% alert warning %}
"동일 조건" 실험 설계가 없으면 BAU 보고가 혼란스럽거나 오해의 소지가 있을 수 있습니다.
{% endalert %}

### 필요한 정보 {#required-information}

실험 설계를 검증한 후, BAU 보고를 설정하기 위해 다음 세부 정보를 수집합니다:

**CEP의 Campaign ID:**

| CEP | 허용되는 유형 |
|-----|---------------|
| **Braze** | Campaigns 및 Canvases |
| **Salesforce Marketing Cloud** | 여정만 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required information" }

**CEP의 오디언스 ID:**

| CEP | 허용되는 유형 |
|-----|---------------|
| **Braze** | Segments만 |
| **Salesforce Marketing Cloud** | 데이터 확장만 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required information" }

BAU 오디언스를 추적하는 기존 오디언스가 없다면 새로 생성해야 합니다.

### 고려 사항 {#considerations}

- **클릭 KPI만 해당:** Decisioning Studio Go와 마찬가지로 BAU 보고는 클릭 KPI만 다루며 전환 KPI는 포함하지 않습니다.
- **Canvas 제한 사항:** 현재 특정 캔버스 단계 ID로 필터링하는 기능은 지원하지 않습니다. 모든 캔버스 단계의 이벤트가 BAU 데이터에 포함됩니다. 특정 캔버스 단계만 포함해야 하는 경우 BAU와의 비교가 무효화될 수 있습니다.

### BAU 보고 설정하기

Decisioning Studio Go 포털의 안내를 따릅니다. 다음이 필요합니다:
- 모든 커뮤니케이션이 BAU 커뮤니케이션인 하나 이상의 Campaign ID
- 매일 BAU 오디언스의 수신자를 추적하는 하나의 오디언스 ID

## 에이전트 모니터링 {#monitor-your-agent}

시작 후 Decisioning Studio Go 포털에서 에이전트의 성과를 모니터링합니다:

- **참여 측정기준:** 실험 그룹 간 클릭률을 추적합니다
- **학습 진행 상황:** 에이전트의 추천이 시간이 지남에 따라 어떻게 발전하는지 관찰합니다
- **그룹 비교:** Decisioning Studio Go 성과를 무작위 대조군 및 BAU(구성된 경우)와 비교합니다

{% alert tip %}
성과에 대한 결론을 도출하기 전에 최소 2~4주간의 데이터 수집 기간을 확보하세요. 에이전트가 효과적으로 학습하고 최적화하려면 충분한 상호작용이 필요합니다.
{% endalert %}

## 문제 해결 {#troubleshooting}

에이전트가 예상대로 작동하지 않는 경우:

1. **오케스트레이션 확인:** CEP 통합이 활성 상태이고, Campaigns와 여정이 실행 중이며, 글로벌 한도나 유사한 규칙이 오케스트레이션에 간섭하지 않는지 확인합니다.
2. **데이터 흐름 확인:** 오디언스 데이터와 참여 데이터가 올바르게 수집되고 있는지 확인합니다.
3. **실험 그룹 검토:** 적절한 무작위 배정이 이루어졌는지, 그룹 간 중복이 없는지 확인합니다.
4. **고객지원 문의:** 추가 지원이 필요하면 Braze 고객지원팀에 문의합니다.