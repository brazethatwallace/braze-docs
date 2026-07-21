---
nav_title: FAQ
article_title: Decisioning Studio Go FAQ
page_order: 8
page_type: FAQ
description: "이 페이지는 Decisioning Studio Go에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
---

# 자주 묻는 질문 {#frequently-asked-questions}

## 일반 {#general}

### Decisioning Studio Go란 무엇인가요? {#what-is-decisioning-studio-go}

Decisioning Studio Go는 Braze 대시보드에 내장된 AI 의사 결정 에이전트입니다. 크리에이티브 배리언트, 발송 시간, 요일 등의 옵션 메뉴를 큐레이트하면, 에이전트가 각 개별 사용자에게 적합한 조합을 선택하여 클릭을 최적화합니다. 데이터 사이언티스트나 커스텀 통합 없이도 일대일 개인화를 제공합니다. 첫 번째 릴리스는 이메일을 지원하며, 추가 채널은 별도의 베타로 제공되고 각 채널은 자체 에이전트가 처리합니다.

### A/B 테스트와 어떻게 다른가요? {#how-is-this-different-from-ab-testing}

A/B 테스트는 전체 오디언스 또는 Segment 내에서 평균적으로 가장 성과가 좋은 배리언트를 찾아 해당 그룹의 모든 사용자에게 하나의 배리언트를 적용합니다. Decisioning Studio Go는 각 사용자가 이전에 참여한 내용을 기반으로 개별 사용자에게 가장 적합한 배리언트를 선택합니다. 동일한 발송에서 서로 다른 사용자가 서로 다른 배리언트를 받을 수 있습니다. 하나의 우승 배리언트를 그룹에 적용하는 대신, Decisioning Studio Go는 개인 수준에서 콘텐츠를 개인화합니다.

### Decisioning Studio Pro와 어떻게 다른가요? {#how-is-this-different-from-decisioning-studio-pro}

Go는 셀프 서비스 티어입니다. 복잡한 구현 없이 일대일 이메일 개인화를 원하는 마케터에게 적합한 출발점입니다. 클릭을 최적화하며 Braze 내에서 직접 구성하는 옵션으로 작동합니다.

Pro는 풀 서비스 티어입니다. 모든 비즈니스 측정기준에 대해 최적화하고, 모든 퍼스트파티 데이터 소스에 연결하며, 여러 채널을 지원하고, Braze AI Decisioning 서비스 팀의 전담 지원이 제공됩니다.

### 어떤 종류의 AI인가요? 생성형인가요? {#what-kind-of-ai-is-this-is-it-generative}

아닙니다. 각 사용자에게 무엇을 보낼지 결정하는 에이전트는 생성형 에이전트가 아닌 의사 결정 에이전트입니다. 콘텐츠를 작성해 주지 않습니다. 옵션을 제공하면 에이전트가 각 개별 사용자에게 가장 적합한 옵션을 학습합니다.

Decisioning Studio Go는 강화 학습을 기반으로 구축되었습니다. 에이전트는 각 발송을 학습 기회로 취급합니다. 승인한 옵션의 조합을 시도하고, 각 사용자가 참여하는지 관찰하며, 누구에게 무엇이 효과적인지에 대한 이해를 업데이트합니다. 시간이 지남에 따라 각 개별 사용자를 클릭을 유도할 가능성이 가장 높은 메뉴 옵션과 매칭하는 정확도가 점점 높아집니다.

## 오디언스 및 대조군 {#audiences-and-control-groups}

### Decisioning Studio 그룹과 랜덤 대조군의 차이점은 무엇인가요? {#whats-the-difference-between-the-decisioning-studio-group-and-the-random-control-group}

Decisioning Studio 그룹은 AI 최적화된 이메일 콘텐츠를 받으며, 에이전트가 각 사용자에게 가장 적합한 배리언트를 선택합니다. 랜덤 대조군은 최적화 없이 동일한 옵션의 무작위 조합을 받습니다. 두 그룹 모두 구성한 제약 조건을 준수합니다(예: 15일 이내에 제목란을 반복하지 않도록 설정한 경우, 해당 규칙은 랜덤 대조군에도 적용됩니다). 두 그룹을 비교하면 에이전트의 성과 향상을 명확하게 측정할 수 있습니다.

### 랜덤 대조군은 이메일을 받지 않는 홀드아웃 그룹인가요? {#is-the-random-control-a-holdout-group-of-users-who-receive-no-email}

아닙니다. 랜덤 대조군 사용자도 이메일을 받습니다. 구성한 옵션의 무작위로 선택된 조합을 스케줄 내 무작위로 선택된 요일에 받습니다. 이를 통해 "이메일 없음"이 아닌 "동일한 콘텐츠를 무작위로 발송"과 "AI 개인화"를 비교할 수 있습니다.

### 랜덤 대조군이 필수인 이유는 무엇인가요? {#why-is-the-random-control-required}

두 가지 이유가 있습니다. 첫째, 에이전트가 무작위 기준선 대비 얼마나 우수한 성과를 내는지 지속적으로 실시간 측정할 수 있습니다. 둘째, 에이전트는 랜덤 대조군의 행동을 학습 신호의 일부로 사용합니다. 최소 랜덤 대조군 크기는 5%이며, 이는 에이전트가 안정적으로 학습하고 성과 측정이 의미 있기 위해 필요한 최소 기준입니다.

### 다른 Canvas나 Campaign에서 이미 사용 중인 Segment를 사용할 수 있나요? {#can-i-use-a-segment-thats-already-used-in-another-canvas-or-campaign}

가능하지만 강력히 권장하지 않으며 경고가 표시됩니다. 동일한 사용자가 Decisioning Studio Go와 다른 Canvases 또는 Campaigns에서 동시에 메시지를 받으면, 다른 메시지가 에이전트가 설명할 수 없는 방식으로 인게이지먼트에 영향을 미칩니다. 가장 깔끔한 설정은 에이전트 전용 Segment입니다.

## 구성 {#configuration}

### 무엇을 개인화할 수 있나요? {#what-can-i-personalize}

각 기본 크리에이티브 내에서 Liquid 태그를 사용하여 제목란, CTA, 이미지를 개인화 포인트로 지정할 수 있습니다. 그러면 에이전트가 각 구성 요소에 대해 제공한 배리언트 중에서 사용자별로 선택합니다. 여러 기본 크리에이티브를 가질 수도 있으며, 에이전트가 어떤 기본 크리에이티브를 사용할지도 선택합니다.

### 개인화된 구성 요소에 Content Blocks를 사용할 수 있나요? {#can-i-use-content-blocks-for-the-personalized-components}

아닙니다. 현재 Content Blocks는 크리에이티브 구성 요소 대체 포인트로 작동하지 않습니다. 개인화된 제목란, CTA, 이미지를 콘텐츠 블록 내부가 아닌 이메일 본문에 직접 배치하세요.

### 클릭 가능한 요소가 없는 이미지 기반 템플릿을 사용할 수 있나요? {#can-i-use-image-based-templates-with-no-clickable-elements}

이미지 기반 템플릿은 지원되지만, 에이전트가 최적화할 수 있는 범위가 제한됩니다. 전체 이메일이 하나의 이미지인 경우, 에이전트는 어떤 이미지를 보낼지 결정할 수 있지만 이메일 내의 제목란, CTA 또는 레이아웃을 최적화할 수 없습니다. 여러 개인화 포인트가 있는 HTML 기반 템플릿에서 더 높은 성과 향상을 얻을 수 있습니다.

### 전환 이벤트를 변경할 수 있나요? {#can-i-change-the-conversion-event}

셀프 서비스 티어에서 지원되는 전환 이벤트는 클릭입니다. Decisioning Studio Pro에서는 모든 커스텀 비즈니스 측정기준에 대해 최적화할 수 있습니다.

### 발송 빈도는 어떻게 작동하나요? {#how-does-send-frequency-work}

주 3회 발송과 같은 단일 빈도를 선택합니다. 에이전트는 빈도 간에 결정하지 않습니다. 해당 빈도 내에서 허용한 요일 중 어떤 요일에, 사용자의 현지 시간대 기준 방해금지 시간 내에서 어떤 시간에 발송할지 선택합니다.

### 최대 게재빈도 설정은 어떻게 작동하나요? {#how-do-frequency-caps-work}

설정 중에 워크스페이스의 최대 게재빈도 설정 규칙을 에이전트에 적용하고, 에이전트의 발송이 각 사용자의 글로벌 최대 게재빈도 설정에 포함될지 여부를 선택할 수 있습니다. 고객 성공 매니저 또는 솔루션 컨설턴트가 워크스페이스에서 최대 게재빈도 설정이 구성된 방식에 따라 프로그램에 적합한 접근 방식을 결정하는 데 도움을 줄 수 있습니다.

### 에이전트가 여러 채널에 걸쳐 발송할 수 있나요? {#can-the-agent-send-across-multiple-channels}

각 에이전트는 단일 채널이며, 현재 지원되는 채널은 이메일입니다. 서로 다른 프로그램에 대해 여러 에이전트를 병렬로 실행할 수 있지만, 각 에이전트는 하나의 채널을 처리합니다.

## 테스트 및 출시 {#testing-and-launch}

### 실시간 적용 전에 어떻게 테스트하나요? {#how-do-i-test-before-going-live}

Braze Composer의 기본 테스트 발송 기능을 사용하세요. 테스트 발송은 선택한 특정 배리언트 조합을 보여주며, 에이전트가 실제 사용자에게 실제로 무엇을 보낼지 예측하는 것이 아니라 이메일 자체를 검증하기 위한 것입니다. Composer의 동적 미리보기를 통해 다양한 배리언트 조합이 어떻게 렌더링되는지도 확인할 수 있습니다.

### 출시 직후에는 어떻게 되나요? {#what-happens-right-after-i-launch}

에이전트가 학습 기간에 진입합니다. 대기 기간 없이 첫날부터 이메일이 발송되지만, 에이전트가 조합을 탐색하는 동안 성과가 변동할 수 있습니다. 리포팅에서 에이전트가 아직 학습 중인지 활성 개인화로 전환되었는지 표시되므로, 항상 어떤 단계에 있는지 알 수 있습니다.

### 출시 후에 에이전트를 편집할 수 있나요? {#can-i-edit-the-agent-after-launch}

네. 오디언스, 스케줄, 크리에이티브, 제약 조건 모두 출시 후에 업데이트할 수 있습니다. 변경 사항이 적용되려면 프로모트해야 합니다.

### 출시 후에 콘텐츠 옵션을 업데이트하면 어떻게 되나요? {#what-if-i-update-content-options-after-launch}

처음 설정할 때와 동일한 방식으로 배리언트를 추가, 제거 또는 변경할 수 있습니다. 변경 사항이 적용되려면 프로모트해야 합니다. 새 배리언트를 추가해도 기존 배리언트에 대한 에이전트의 학습이 초기화되지 않습니다.

## 리포팅 및 결과 {#reporting-and-results}

### Decisioning Studio Go 리포팅이 Braze의 다른 이메일 분석에서 보이는 것과 일치하나요? {#does-decisioning-studio-go-reporting-match-what-i-see-in-my-email-analytics-elsewhere-in-braze}

수치가 다를 수 있습니다. Decisioning Studio는 표준 이메일 리포트보다 더 엄격한 클릭 필터링을 적용하므로 합계가 더 낮을 수 있습니다. Decisioning Studio 그룹과 랜덤 대조군 간의 상대적 비교는 Decisioning Studio 리포팅 내에서 일관되며, 클릭 필터링이 각 그룹에 동일하게 적용됩니다.

### 에이전트는 어떤 측정기준을 최적화하나요? {#what-metrics-does-the-agent-optimize-for}

사용자당 일일 고유 클릭입니다. 에이전트의 목표는 원시 클릭 볼륨이 아닌 클릭하는 고유 사용자 수를 극대화하는 것입니다.

### 어떤 조합이 가장 성과가 좋은지 확인할 수 있나요? {#can-i-see-which-combinations-are-performing-best}

네. 리포팅에는 에이전트가 발송하는 제목란, CTA, 이미지 등 개별 요소의 분포가 포함됩니다.

### 에이전트가 발송하는 콘텐츠에 대한 책임은 누구에게 있나요? {#whos-accountable-for-the-content-the-agent-sends}

사용자 본인에게 있습니다. 에이전트는 배리언트로 추가한 콘텐츠만 발송합니다. 에이전트가 각 사용자에 대한 조합을 결정하지만, 모든 개별 요소는 제공한 배리언트에서 가져옵니다.

## 지원 {#support}

### 에이전트에 대한 도움은 어디서 받을 수 있나요? {#where-do-i-get-help-with-my-agent}

구성, 성과 검토 또는 프로그램 설계에 대한 도움이 필요하면 Braze 고객 성공 매니저 또는 솔루션 컨설턴트에게 문의하세요.