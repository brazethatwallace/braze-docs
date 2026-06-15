---
nav_title: 시작하기
article_title: Decisioning Studio 시작하기
layout: dev_guide
guide_top_header: "Decisioning Studio 시작하기"
guide_top_text: ""
page_order: 0
search_rank: 2
page_type: landing
description: "이 섹션에서는 Decisioning Studio에 대한 소개와 비즈니스 측정기준을 최적화하는 의사 결정 에이전트를 설계하고 배포하는 방법을 안내합니다."

guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: 에이전트 설계하기
    link: /docs/user_guide/brazeai/decisioning_studio/design_agents/
    image: /assets/img/braze_icons/settings-01.svg
  - name: 데이터 준비하기
    link: /docs/user_guide/brazeai/decisioning_studio/prepare_data/
    image: /assets/img/braze_icons/database-01.svg
  - name: 오디언스 정의하기
    link: /docs/user_guide/brazeai/decisioning_studio/audience/
    image: /assets/img/braze_icons/users-01.svg
  - name: 오케스트레이션 설정하기
    link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup/
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "추가 리소스"
guide_menu_list:
  - name: Decisioning Studio 소개
    link: /docs/user_guide/brazeai/decisioning_studio/
    image: /assets/img/braze_icons/info-circle.svg
  - name: Decisioning Studio FAQ
    link: /docs/user_guide/brazeai/decisioning_studio/faq/
    image: /assets/img/braze_icons/annotation-question.svg
---

BrazeAI Decisioning Studio™를 사용하면 비즈니스 측정기준을 최적화하는 의사 결정 에이전트를 설계하고 배포할 수 있습니다.

이 참조 문서에서는 에이전트 설계, 데이터 소스 구성 및 연결, 오케스트레이션 설정, 성과 평가 등 Decisioning Studio를 설정하는 데 필요한 단계를 개요로 안내합니다.

## 주요 설계 결정 사항 {#key-design-decisions}

AI Decisioning Services 팀과 협력하여 다음 사항을 결정하세요:

| 결정 사항 | 설명 | 예시 |
|----------|-------------|----------|
| **성공 측정기준** | 고객 참여를 개인화할 때 에이전트가 무엇을 극대화할 것인가? | 매출, LTV, ARPU, 전환, 리텐션 |
| **오디언스** | Decisioning Studio 에이전트가 누구를 대상으로 고객 참여 결정을 내릴 것인가? | 전체 고객, 로열티 회원, 이탈 위험 가입자 |
| **실험 그룹** | Decisioning Studio의 무작위 대조 시험을 어떻게 구성할 것인가? | Decisioning Studio, Random Control, BAU, Holdout |
| **차원** | 에이전트가 어떤 결정을 개인화해야 하는가? | 시간대, 제목란, 빈도, 오퍼, 채널 |
| **옵션** | 에이전트가 활용할 수 있는 옵션은 무엇인가? | 특정 템플릿, 오퍼, 시간 기간 |
| **제약 조건** | 에이전트가 절대 내려서는 안 되는 결정은 무엇인가? | 지역 제한, 예산 한도, 자격 규칙 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Key design decisions" }

이러한 각 결정 사항은 에이전트가 생성할 수 있는 점진적 향상의 크기와 속도에 영향을 미칩니다. AI Decisioning Services 팀이 모든 비즈니스 규칙을 준수하면서 최대 가치를 창출하는 에이전트를 설계할 수 있도록 함께 협력합니다.

![성공 측정기준, 오디언스, 실험 그룹, 차원, 옵션, 제약 조건이 Decisioning Studio 에이전트 설계에 어떻게 반영되는지 보여주는 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Decisioning Studio 기능 {#decisioning-studio-capabilities}

| 기능 | 세부 정보 |
|------------|---------|
| **모든 성공 측정기준** | 매출, 전환, ARPU, LTV 또는 모든 비즈니스 KPI에 대해 최적화 |
| **무제한 차원** | 오퍼, 채널, 타이밍, 빈도, 크리에이티브 등 다양한 항목에 걸쳐 개인화 |
| **모든 CEP** | Braze, Salesforce Marketing Cloud와의 네이티브 통합 또는 모든 플랫폼에 대한 커스텀 통합 |
| **AI Decisioning Services** | Braze 데이터 사이언스 팀의 전담 지원 |
| **고급 실험 설계** | 완전히 커스텀 가능한 처리 그룹 및 홀드아웃 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio capabilities" }

## 모범 사례 {#best-practices}

Decisioning Studio 에이전트를 설계할 때 참고할 몇 가지 모범 사례입니다:

- **데이터 풍부성을 극대화하세요:** 에이전트가 고객에 대해 더 많은 정보를 가질수록 더 나은 성과를 발휘합니다.
- **동작을 다양화하세요:** 에이전트가 취할 수 있는 동작의 집합이 다양할수록 각 사용자에 맞게 전략을 더 잘 개인화할 수 있습니다.
- **제약 조건을 최소화하세요:** 에이전트에 대한 제약 조건이 적을수록 좋습니다. 제약 조건은 비즈니스 규칙을 준수하면서도 에이전트 주도의 실험을 최대한 자유롭게 허용하도록 설계해야 합니다.