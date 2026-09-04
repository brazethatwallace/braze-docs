---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "BrazeAI Decisioning Studio<sup>TM</sup> Go를 Braze에 설정하고 통합하는 방법을 알아보세요."
---

# BrazeAI Decisioning Studio™ Go

> BrazeAI Decisioning Studio™ Go를 Braze에 설정하고 통합하는 방법을 알아보세요.

## Decisioning Studio Go 소개 {#about-decisioning-studio-go}

Decisioning Studio Go는 반복적인 이메일 프로그램을 위한 AI 의사 결정 에이전트입니다. 전체 오디언스에 대해 하나의 우승 제목란, 발송 시간 또는 이미지를 선택하는 대신, 에이전트가 각 수신자의 과거 인게이지먼트를 기반으로 최적의 조합을 선택합니다.

에이전트가 선택할 수 있는 배리언트(제목란, CTA, 이미지, 발송 요일, 발송 시간 등)를 정의합니다. Segment 내 각 사용자에 대해 에이전트가 설정한 제약 조건과 스케줄 내에서 인게이지먼트를 유도할 가능성이 가장 높은 옵션을 선택합니다.

이는 오디언스 수준에서 배리언트를 최적화하는 [BrazeAI<sup>TM</sup>로 최적화]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)를 활용한 Campaign 수준 A/B 테스트와 다릅니다. Decisioning Studio Go는 프로그램의 모든 발송에 걸쳐 개인 수준에서 개인화합니다.

### 작동 방식 {#how-it-works}

에이전트는 Braze Segment를 두 그룹으로 나눕니다: AI로 최적화된 이메일 콘텐츠를 받는 Decisioning Studio 그룹과 동일한 옵션의 무작위 조합을 받는 무작위 대조군(최소 5%)입니다. 무작위 대조군은 에이전트의 리프트를 지속적으로 동등하게 측정할 수 있게 해주므로, 개인화된 경험이 개인화 없이 동일한 콘텐츠를 발송한 경우와 비교하여 어떤 성과를 보이는지 항상 확인할 수 있습니다.

Decisioning Studio 그룹의 각 사용자에 대해, 에이전트는 제공한 옵션 중에서 선택합니다: 어떤 크리에이티브를 보낼지(크리에이티브 내의 특정 제목란, CTA, 이미지 포함), 그리고 언제 보낼지(요일 및 시간대, 방해금지 시간과 사용자의 현지 시간대 준수). [Decisioning Studio Go 에이전트 설정]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)에서 각 항목을 자세히 다룹니다.

사용자가 참여하거나 참여하지 않으면 에이전트가 학습합니다. 리포팅에서는 에이전트가 아직 학습 기간에 있는지 아니면 적극적으로 개인화하고 있는지를 표시하므로, 에이전트가 어떤 단계에 있는지 항상 알 수 있습니다.

### 구성 항목 {#what-you-configure}

| 구성 | 설명 |
|---|---|
| **오디언스** | 진입 오디언스로 사용할 단일 Braze Segment입니다. 에이전트가 자동으로 Segment를 의사 결정 그룹과 무작위 대조군으로 나눕니다. |
| **스케줄** | 발송 빈도(예: 주 3회 단일 선택), 허용 요일, 사용자 현지 시간대의 방해금지 시간, 에이전트 수준의 최대 게재빈도 설정 규칙 준수 등입니다. |
| **크리에이티브** | Braze 작성기에서 만든 하나 이상의 베이스 크리에이티브입니다. 각 베이스 크리에이티브 내에서 Liquid 태그를 사용하여 제목란, CTA, 이미지를 개인화 포인트로 지정한 다음, 각각에 대한 배리언트 목록을 제공할 수 있습니다. 에이전트가 각 수신자에게 어떤 베이스 크리에이티브와 배리언트를 사용할지 결정합니다. |
| **제약 조건** | 정의한 기간 내에 에이전트가 동일한 베이스 크리에이티브 또는 동일한 제목란을 사용자에게 두 번 이상 보내는 것을 방지하는 제한입니다. |
| **검토 및 시작** | 시작 전에 확인해야 할 경고를 표시하는 최종 검증 화면입니다. 에이전트가 **Draft**에서 **Active**로 전환되어 발송을 시작합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Go 구성" }

### Decisioning Studio Go 사용 시기 {#when-to-use-decisioning-studio-go}

안정적인 오디언스와 클릭 가능한 콘텐츠를 갖춘 반복적인 이메일 프로그램에 가장 적합합니다. 예를 들어 상시 캘린더(리워드, 콘텐츠 드롭, 라이프사이클 넛지), 에버그린 프로그램(윈백, 재참여), 멀티 이메일 프로모션 등이 있습니다. 이러한 프로그램은 에이전트가 의미 있게 학습할 수 있는 충분한 볼륨과 다양성을 제공합니다.

프로그램 유형별 상세 적합도 가이드는 [Decisioning Studio Go 예제]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples)를 참조하세요.

### Decisioning Studio 스위트 내 Decisioning Studio Go의 위치 {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Go는 BrazeAI Decisioning Studio의 엔트리 티어입니다. 풀 서비스 Decisioning Studio Pro 구현의 설정 부담 없이 일대일 이메일 개인화를 원하는 마케터를 위해 설계되었습니다.

Decisioning Studio Pro는 다음을 추가로 제공합니다:
- 모든 비즈니스 측정기준에 대한 최적화(클릭뿐만 아니라)
- 모든 퍼스트파티 데이터 소스에 연결
- 멀티 채널 의사 결정
- 확장된 오케스트레이션 패턴
- Braze AI Decisioning 서비스 팀의 전담 지원

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: Decisioning Studio Go 에이전트 설정
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup/
- name: Decisioning Studio Go 예제 검토
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples/
- name: FAQ
  link: /docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq/
{% endarticle_tiles %}