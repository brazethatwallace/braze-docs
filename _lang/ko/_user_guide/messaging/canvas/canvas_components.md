---
nav_title: 캔버스 구성요소
article_title: 캔버스 구성요소
page_order: 3
alias: "/user_guide/messaging/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "캔버스 구성요소"
guide_top_text: "캔버스 구성요소로 캔버스 여정을 강화하세요. 캔버스 구성요소를 사용하면 과도한 전체 단계를 하나의 단계로 대체하여 캔버스의 효과를 판단하는 프로세스를 간소화할 수 있습니다. 캔버스의 구성요소는 캔버스 브랜치에서 개인화된 사용자 여정을 의미합니다."

page_type: landing
description: "이 랜딩 페이지에는 더 고급 캔버스를 만드는 데 도움이 되는 캔버스 구성요소 문서가 있습니다. 이러한 구성요소에는 메시지 단계, 지연 단계, 결정 분할 단계 등이 포함됩니다."
tool: Canvas

guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: 행동 경로 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/action_paths
    image: /assets/img/braze_icons/zap.svg
  - name: 에이전트 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/agent_step
    image: /assets/img/braze_icons/briefcase-01.svg
  - name: 오디언스 경로 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/audience_paths
    image: /assets/img/braze_icons/users-01.svg 
  - name: 오디언스 동기화 단계
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: 콘텐츠 최적화 프로그램 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step
    image: /assets/img/braze_icons/target-04.svg
  - name: 컨텍스트 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/context
    image: /assets/img/braze_icons/file-search-02.svg
  - name: 결정 분할 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/decision_split
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: 지연 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/delay_step
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: 실험 경로 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step
    image: /assets/img/braze_icons/columns-01.svg
  - name: 기능 플래그
    link: /docs/user_guide/messaging/canvas/canvas_components/feature_flags
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: 메시지 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/message_step
    image: /assets/img/braze_icons/message-square-02.svg
  - name: 대상으로 보내기 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/send_to_destination
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: 사용자 업데이트 단계
    link: /docs/user_guide/messaging/canvas/canvas_components/user_update
    image: /assets/img/braze_icons/user-check-01.svg
---

## 캔버스 구성요소 소개

캔버스 구성요소를 사용하면 새로운 사용자 여정을 열어 프로세스를 개선하고 오디언스 도달 효과를 높일 수 있습니다.

### 사용자 여정 커스터마이징

![결정 분할 단계 뒤에 지연 단계와 메시지 단계가 이어지는 캔버스 사용자 여정 예시.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

[행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)를 사용하면 구매와 같은 행동 및 참여 이벤트를 기반으로 사용자 여정을 분할할 수 있습니다. 오디언스를 필터링하고 타겟팅하려면 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)를 사용하여 오디언스 기준에 따라 사용자를 다른 캔버스 경로로 보내 사용자 타겟팅을 간소화할 수 있습니다.

[결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) 구성요소는 간단한 "예 또는 아니오" 로직을 사용하여 행동이나 사용자 속성을 기반으로 상호 배타적인 두 개의 경로를 만듭니다. 이를 통해 사용자 그룹을 식별하고 타겟팅할 수 있습니다.

[지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) 구성요소를 사용하면 캔버스의 단일 단계를 지연시킬 수 있습니다. 캔버스의 이 독립형 지연 단계는 특정 시간에 사용자에게 메시지를 전달하는 데 가장 적합합니다. 또한 지연 구성요소는 오디언스가 구성요소의 기준을 충족할 수 있는 시간을 더 많이 제공하여 오디언스 도달 범위를 늘릴 수도 있습니다.

### 테스트

사용자 여정을 만들 때 가장 효과적인 캔버스 경로를 테스트하고 싶을 수도 있습니다. [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)를 사용하면 모든 단계에서 여러 캔버스 경로를 테스트할 수 있습니다. 또한 단계 간의 연결을 상위 수준 미리보기로 활용할 수 있습니다. 주황색 연결은 이전 단계가 사용자를 다음 단계로 즉시 진행시킨다는 것을 나타냅니다.

### 통합

브랜드의 퍼스트파티 사용자 데이터와 동기화하고 싶으신가요? [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) 및 [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/)에 사용 가능한 오디언스 동기화 옵션을 활용하세요.