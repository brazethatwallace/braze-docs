---
nav_title: BrazeAI
article_title: BrazeAI
description: "고객 참여 전략 전반에 걸친 창의성, 개인화 및 최적화를 위한 BrazeAI 도구입니다."
page_order: 8
layout: dev_guide
search_rank: 12
tool:
  - Dashboard

guide_top_header: "BrazeAI<sup>TM</sup>"
guide_top_text: "BrazeAI<sup>TM</sup>은 인게이지먼트 전략의 창의성, 개인화 및 최적화를 위한 진입 장벽을 낮춰주는 접근하기 쉽고 사용하기 쉬운 도구 모음을 제공합니다. BrazeAI<sup>TM</sup> 기능을 사용하면 신뢰할 수 있는 조언자를 통해 창의력을 발휘하고, 더 나은 의사 결정을 내리고, 고객을 위한 사용자 경험을 최적화하는 데 도움을 받을 수 있습니다. 이 허브에서는 생성형 AI, Intelligence Suite, 아이템 추천, 에이전트 및 Campaigns와 Canvases에서 사용할 수 있는 기타 BrazeAI 기능에 대한 가이드를 확인할 수 있습니다."

guide_featured_title: "기능들"
guide_featured_list:
  - name: 에이전트
    link: /docs/user_guide/brazeai/agents
    image: /assets/img/braze_icons/star-06.svg
  - name: Braze MCP 서버
    link: /docs/user_guide/brazeai/mcp_server
    image: /assets/img/braze_icons/dataflow-01.svg
  - name: 콘텐츠 최적화 프로그램
    link: /docs/user_guide/brazeai/content_optimizer
    image: /assets/img/braze_icons/image-user-check.svg
  - name: 결정 스튜디오
    link: /docs/user_guide/brazeai/decisioning_studio
    image: /assets/img/braze_icons/stars-03.svg
  - name: 생성형 AI
    link: /docs/user_guide/brazeai/generative_ai
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: Intelligence Suite
    link: /docs/user_guide/brazeai/intelligence_suite
    image: /assets/img/braze_icons/clock.svg
  - name: 아이템 추천
    link: /docs/user_guide/brazeai/item_recommendations
    image: /assets/img/braze_icons/hearts.svg
  - name: Operator
    link: /docs/user_guide/brazeai/operator
    image: /assets/img/braze_icons/edit-05.svg
  - name: Predictive Suite
    link: /docs/user_guide/brazeai/predictive_suite
    image: /assets/img/braze_icons/stars-01.svg
  - name: 위닝 경로
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: BrazeAI<sup>TM</sup>로 최적화
    link: /docs/user_guide/brazeai/intelligence_suite/variant_selection
    image: /assets/img/braze_icons/trophy-01.svg
---

<br>

## 기능 개요 {#feature-overview}

| 목표 | 권장 기능 |
| --- | --- |
| 사용자의 맥락을 활용하여 사용자별로 메시지 카피를 개인화 | [Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents) ([Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) 또는 [카탈로그]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents)); 일회성 초안 카피의 경우 [생성형 AI]({{site.baseurl}}/user_guide/brazeai/generative_ai) |
| 시간이 지남에 따라 가장 효과적인 메시지 콘텐츠(제목란 또는 CTA 등)를 최적화 | [콘텐츠 최적화 프로그램]({{site.baseurl}}/user_guide/brazeai/content_optimizer) (이메일, 푸시 알림, 단문 메시지 서비스/MMS/RCS) 또는 [BrazeAI<sup>TM</sup>로 최적화]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) |
| 오퍼, 채널, 타이밍에 대한 1:1 의사결정으로 비즈니스 측정기준(매출, 전환) 극대화 | [Decisioning Studio]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) |
| 이탈 가능성이 높거나 특정 이벤트를 수행할 가능성이 있는 사용자 찾기 | [예측 이탈]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) 또는 [예측 이벤트]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) |
| 메시지에서 카탈로그의 특정 제품 추천 | [아이템 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations) |
| 사용자별로 가장 적절한 시간 또는 가장 적합한 채널로 전송 | [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) |
| 대시보드에서 직접 카피 및 크리에이티브를 생성하거나 다듬기 | [Operator]({{site.baseurl}}/user_guide/brazeai/operator) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="기능 개요" }

## 자주 묻는 질문 {#frequently-asked-questions}

### BrazeAI란 무엇인가요? {#what-is-brazeai}

BrazeAI는 생성형 카피, 개인화, 예측, 제품 추천, 의사결정을 위한 Braze의 AI 기반 도구 모음입니다. 이 페이지의 기능 링크를 사용하여 각 기능의 설정 가이드를 열어보세요.

### 어떤 BrazeAI 기능을 먼저 사용해야 하나요? {#which-brazeai-feature-should-i-use-first}

이 페이지의 [기능 개요](#feature-overview) 표를 참조하여 카피 생성, 발송 시간 최적화 또는 제품 추천 등 목표에 맞는 BrazeAI 기능을 찾아보세요.