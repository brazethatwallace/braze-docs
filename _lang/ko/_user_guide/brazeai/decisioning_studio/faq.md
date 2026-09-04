---
nav_title: FAQ
article_title: Decisioning Studio FAQ
page_order: 8
page_type: FAQ
description: "이 페이지는 Decisioning Studio에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 Decisioning Studio에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 의사 결정 에이전트란 무엇인가요? {#what-is-a-decisioning-agent}

의사 결정 에이전트는 특정 비즈니스 목표를 충족하기 위해 맞춤 구성된 BrazeAI Decisioning Studio™의 커스텀 구성입니다. 이는 성공 측정기준, 크기 및 위치, 그리고 선택한 옵션에 의해 정의됩니다. 의사 결정 에이전트는 선택한 비즈니스 측정기준을 극대화하기 위해 모든 고객에 대한 최적의 동작을 자동으로 발견합니다.

### 어떤 측정기준을 최적화할 수 있나요? {#what-metrics-can-i-optimize-for}

매출, 전환, 사용자당 평균 매출(ARPU), 고객 LTV(고객 생애주기 가치), 이익, 계약 갱신 또는 기타 비즈니스 KPI와 같은 목표에 맞는 모든 비즈니스 측정기준을 최적화할 수 있습니다.

### Decisioning Studio에서 크기 및 위치란 무엇인가요? {#what-are-dimensions-in-decisioning-studio}

크기 및 위치는 의사 결정 에이전트가 성공 측정기준을 극대화하기 위해 조작할 수 있는 *레버의 유형*으로 생각할 수 있습니다. 일반적인 크기 및 위치에는 오퍼, 제목란, 크리에이티브, 채널 또는 발송 시간이 포함됩니다.

### 액션 뱅크란 무엇인가요? {#what-is-an-action-bank}

액션 뱅크는 각 크기 및 위치 "레버"에 대해 의사 결정 에이전트가 접근할 수 있는 *특정 옵션*을 정의합니다. 예를 들어, 채널 크기 및 위치의 경우 의사 결정 에이전트가 접근할 수 있는 특정 채널을 정의합니다. 오퍼 크기 및 위치의 경우 의사 결정 에이전트가 테스트할 수 있는 특정 오퍼를 정의합니다.

### 의사 결정 에이전트가 구성하지 않은 동작을 취할 수 있나요? {#can-the-decisioning-agent-take-actions-i-havent-configured}

아니요. 의사 결정 에이전트는 구성하고 액션 뱅크에 추가한 동작만 취할 수 있습니다. 이는 모든 가능한 동작이 액션 뱅크에 넣은 조합에 의해 정의된다는 것을 의미합니다.

### 제약 조건이란 무엇인가요? {#what-are-constraints}

제약 조건은 의사 결정 에이전트의 동작을 제한하여 중요한 비즈니스 규칙을 준수하도록 합니다. 예를 들어, 자격이 없는 지역의 고객에게 특정 오퍼가 선택되지 않도록 하거나, 의사 결정 에이전트가 사용할 수 있는 최대 예산을 설정하는 것일 수 있습니다.

### Decisioning Studio Go와 Decisioning Studio Pro의 차이점은 무엇인가요? {#what-is-the-difference-between-decisioning-studio-go-and-decisioning-studio-pro}

Decisioning Studio Pro는 Braze의 전방 배치 데이터 과학 팀의 인공지능 의사 결정 서비스 지원을 포함하여, 비즈니스 결과를 극대화하기 위해 에이전트를 설계하고 구성하는 데 도움을 줍니다. 자세한 내용은 [Decisioning Studio Go 대 Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio#decisioning-studio-go-vs-decisioning-studio-pro)를 참조하세요.