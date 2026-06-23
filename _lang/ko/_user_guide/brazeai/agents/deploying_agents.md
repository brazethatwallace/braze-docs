---
nav_title: 에이전트 배포
article_title: 커스텀 에이전트 배포
description: "에이전트를 생성한 후 Braze에서 커스텀 에이전트를 사용하는 방법을 알아보세요."
alias: /deploying-agents/
page_order: 2
---

# 커스텀 에이전트 배포 {#deploy-custom-agents}

> [에이전트를 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)한 후, 이 페이지에서 Braze에서 에이전트를 배포하는 위치와 방법을 알아보세요. 생성 시 선택한 에이전트 유형(Canvas 에이전트 또는 카탈로그 에이전트)에 따라 에이전트가 실행될 수 있는 위치가 결정됩니다. 소개는 [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/)를 참조하세요.

## 커스텀 에이전트 유형 {#types-of-custom-agents}

커스텀 에이전트는 유형에 따라 Braze의 서로 다른 부분에 배포됩니다. 아래 표를 참고하여 에이전트에 맞는 배포 경로를 찾으세요.

| 에이전트 유형 | 배포 위치 | 실행 시점 | 섹션 |
| --- | --- | --- | --- |
| 캔버스 단계 에이전트 | Canvas의 [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/) | 사용자가 해당 단계에 진입할 때 | [캔버스 단계 에이전트 사용](#use-canvas-step-agents) |
| 카탈로그 에이전트 | 카탈로그 필드 | 카탈로그 행이 생성되거나 업데이트될 때 | [카탈로그 에이전트 사용](#use-catalog-agents) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="커스텀 에이전트 유형" }

에이전트를 생성할 때 **에이전트 콘솔**에서 에이전트 유형을 선택합니다. 설정 단계는 [커스텀 에이전트 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#step-1-choose-an-agent-type)을 참조하세요.

## 모범 사례 {#best-practices}

에이전트가 가장 큰 투자수익률(ROI)을 이끌어낼 수 있는 고가치 사용 사례를 타겟팅하고, 반응할 가능성이 높은 오디언스를 선택하세요. 규모가 작지만 기회가 높은 오디언스가 기회가 낮은 대규모 오디언스보다 더 나은 성과를 내는 경우가 많습니다.

Canvas 에이전트의 경우, 최근 검색, 높은 참여도 또는 풍부한 프로필 데이터 등 강한 신호를 가진 사용자부터 시작한 후 더 넓은 Segments로 확장하세요. 카탈로그 에이전트의 경우, 필요한 입력 열이 이미 채워져 있는 행을 우선시하여 각 호출이 유용한 출력을 생성할 수 있는 충분한 컨텍스트를 갖도록 하세요.

에이전트를 광범위하게 배포하기 전에 소규모로 ROI를 테스트하려면, [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) 단계를 사용하여 오디언스의 일부만 에이전트 단계가 포함된 분기에 진입하도록 하세요.

## 캔버스 단계 에이전트 사용 {#use-canvas-step-agents}

Canvas 에이전트를 생성한 후, Canvas에 에이전트 단계로 추가하여 메시지를 개인화하거나 실시간으로 의사 결정을 안내할 수 있습니다.

### 작동 방식 {#how-it-works}

사용자가 Canvas의 에이전트 단계에 도달하면, Braze는 구성한 입력 데이터를 에이전트에 전송합니다. 에이전트는 모델과 지침을 사용하여 입력을 처리한 다음, 단계에서 정의한 출력 변수에 저장되는 출력을 반환합니다. 이 출력을 의사 결정, 개인화 또는 다운스트림 처리에 사용할 수 있습니다.

에이전트 단계는 [Canvas 컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)를 사용하여 관련 컨텍스트를 수집하고, Canvas에서 사용할 수 있는 변수를 출력합니다. 필수 조건과 전체 참조는 [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)를 참조하세요.

### 에이전트 단계 추가 {#add-an-agent-step}

Canvas에 에이전트를 추가하려면:

1. 사이드바에서 **에이전트** 구성요소를 드래그 앤 드롭하거나, 단계 하단의 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택한 후 **에이전트**를 선택합니다.
2. 이 단계에서 데이터를 처리할 에이전트를 선택합니다.
3. 출력 변수 이름을 정의합니다. 출력 데이터 유형은 [에이전트 콘솔]({{site.baseurl}}/user_guide/brazeai/agents/)에서 설정합니다.
4. (선택 사항) 에이전트가 실행될 때 참조할 추가 컨텍스트 값을 추가합니다. 여기에는 에이전트 설정에서 아직 바인딩하지 않은 추가 Liquid 변수나 Canvas 컨텍스트가 포함될 수 있습니다. 예를 들어, 이 단계에서 전송 시점에만 전달하려는 값이 해당됩니다.
5. 단계 미리보기에서 에이전트 출력을 테스트하고 미리봅니다.

출력 데이터 유형, Liquid 템플릿 및 스크린샷은 [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)를 참조하세요.

### 활용 사례 {#use-cases}

| 활용 사례 | 설명 |
| --- | --- |
| 리드 스코어링 및 자격 평가 | 에이전트 단계를 사용하여 유입되는 리드를 척도(예: 1-10)로 평가합니다. 기준 점수를 초과하는 사용자를 육성 경로로 라우팅하고, 적합하지 않은 리드는 제외합니다. |
| 동적 메시지 개인화 | 에이전트가 사용자 속성이나 최근 동작을 기반으로 제목란, 제품 추천 또는 메시지 문구를 생성하도록 합니다. 응답은 메시지 단계에 직접 삽입할 수 있습니다. |
| 고객 피드백 처리 | 고객 의견을 에이전트에 전달하여 감정을 분석하고 공감하는 후속 메시지를 생성합니다. 고가치 사용자의 경우 에이전트가 응답을 에스컬레이션하거나 특전을 포함할 수 있습니다. |
| 지능형 라우팅 | 에이전트 출력(부울 또는 숫자)을 사용하여 사용자를 서로 다른 Canvas 경로로 분할합니다. 예를 들어, 사용자를 "위험" 또는 "건강"으로 분류하고 메시징 주기를 그에 맞게 조정합니다. |
| 설문조사 또는 응답 해석 | 에이전트가 개방형 설문조사 응답이나 자유 텍스트 필드를 구문 분석하여 다운스트림 경로를 유도하는 구조화된 값(예: 의도 또는 필요 분류)을 반환하도록 합니다. |
| 다단계 추론 | 에이전트가 컨텍스트 필드를 결합하고 여러 사용자 속성을 기반으로 다음 최선의 동작(이메일, SMS 또는 담당자 연결)을 추천하는 등 복잡한 결정을 내리도록 구성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="활용 사례" }

### 에이전트 출력 사용 {#use-the-agent-output}

에이전트가 실행된 후, Canvas에서 출력 변수를 사용합니다:

- **여정 라우팅:** 에이전트의 응답을 기반으로 사용자를 서로 다른 Canvas 경로로 라우팅합니다. 숫자, 부울 또는 구조화된 출력과 함께 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) 또는 [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)을 사용합니다.
- **개인화:** Liquid를 사용하여 에이전트의 응답을 메시지 단계에 직접 삽입합니다.
- **사용자 데이터 처리:** 사용자 데이터를 분석하고 표준화한 다음, 고객 프로필에 저장하거나(예: [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) 단계 사용) 웹훅을 사용하여 전송합니다.

예시는 에이전트 단계의 [작동 방식]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/#how-it-works)을 참조하세요.

### 오류 처리 및 대체 동작 {#fallback-behavior}

다음은 [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)의 **캔버스 단계 에이전트**에 적용됩니다.

- 연결된 모델이 LLM 제공자로부터 [사용량 제한 오류]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors)를 반환하면, Braze는 호출이 성공하거나 완료할 수 없다고 판단할 때까지 지수 백오프를 사용하여 요청을 지속적으로 재시도합니다. 이후 사용자는 다음 캔버스 단계로 진행합니다.
- 다른 실패(예: 타임아웃 또는 잘못된 API 키)의 경우, 에이전트에 에이전트 콘솔에서 [대체 값이 구성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#configure-fallback-values)되어 있지 않으면 출력 변수가 `null`로 설정됩니다.
- 에이전트가 일일 호출 한도에 도달하면, Braze는 구성된 대체 값이 있을 때 이를 적용합니다. 그렇지 않으면 출력 변수가 `null`로 설정됩니다.

대체 값이 구성된 경우, Braze는 재시도 불가능한 오류와 일일 한도 실패에 대해 대체 값을 적용합니다. Braze는 사용자별로 Liquid를 사용하여 대체 값을 렌더링하고 결과를 에이전트 단계 출력 변수에 저장합니다. 대체 값이 없으면 해당 실패 시 출력 변수가 `null`로 설정됩니다. 에이전트 콘솔 대체 값 대신 메시지 단계에서 단계별 기본값을 구성하려면, 에이전트 설정의 **출력** 섹션에서 대체 값을 비워 두어 에이전트가 null을 반환할 때 Liquid 기본값이 적용되도록 할 수 있습니다. 다운스트림에서 [기본 Liquid 값]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/)을 사용하면 됩니다.

- 동일한 입력에 대한 응답은 캐시되며, 몇 분 이내에 반복되는 동일한 호출에 재사용될 수 있습니다. 캐시된 응답도 총 호출 수와 일일 호출 수에 포함됩니다.
- 에이전트 단계는 대량의 사용자를 처리하는 데 시간이 걸릴 수 있습니다. Braze는 [호출 흐름 제어]({{site.baseurl}}/user_guide/brazeai/agents/reference/#invocation-flow-controls)에 따라 호출을 대기줄에 넣으므로, 대량 전송 시 사용자가 대기 상태로 남아 있을 수 있습니다.

에이전트 단계 설정 및 런타임 세부 정보는 에이전트 단계의 [오류 처리]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/#error-handling)를 참조하세요. 자세한 내용은 Braze Agents의 [오류 처리]({{site.baseurl}}/user_guide/brazeai/agents/#error-handling)를 참조하세요.

## 카탈로그 에이전트 사용 {#use-catalog-agents}

카탈로그 에이전트를 생성한 후, 카탈로그 필드에 적용하여 각 행의 값을 자동으로 생성하거나 계산할 수 있습니다. 에이전트는 향후 카탈로그에 추가되는 새로운 행에서도 실행됩니다.

### 작동 방식

시작 후 에이전트는 각 행을 실행하고 평가하며, 선택된 열을 컨텍스트에 포함시켜 출력을 생성합니다. 에이전트를 배포한 후 추가된 모든 새 행에서 에이전트가 실행됩니다. **카탈로그 행 업데이트 시 재계산**을 선택한 경우, 기존 소스 필드가 변경되면 이 필드의 모든 값이 업데이트됩니다.

카탈로그 에이전트의 입력 열을 구성할 때, 에이전트가 호출되기 전에 선택된 열 중 **실행에 필수인** 열을 표시하는 제품 내 제어를 활성화하세요(워크스페이스에 따라 레이블이 약간 다를 수 있습니다). 해당 제어를 활성화한 후, 값이 포함되어야 하는 열의 하위 집합을 선택합니다. 선택된 열은 기본적으로 필수로 시작되지만, 에이전트를 차단하지 않고 비어 있어도 되는 열은 제거할 수 있습니다. 에이전트는 필수로 남겨둔 열이 비어 있거나 누락된 경우에만 해당 행을 건너뜁니다. 예를 들어, 아직 채워지지 않은 `gender` 필드가 해당됩니다. 필수 컨텍스트 없이 실행하면 토큰이 낭비되고 품질이 낮은 출력이 생성될 수 있습니다.

카탈로그 에이전트는 열 간의 종속성도 준수합니다. 열 D가 열 B와 C에서 생성되는 경우, 에이전트는 해당 행에 B와 C에 값이 포함될 때까지 열 D에 대해 실행하지 않습니다.

에이전트를 사용하는 카탈로그의 필드를 새로고침하고 편집할 수 있습니다. 열에서 에이전트를 제거하려면 **Apply AI agent**를 선택 해제합니다. 이렇게 하면 열이 비에이전트 열로 되돌아가며, 필드는 에이전트가 카탈로그에서 마지막으로 실행했을 때 적용한 최신 값을 유지합니다.

카탈로그에서 순환 참조는 지원되지 않으며, 다음 시나리오는 발생할 수 없습니다:

- 에이전트 열 1이 에이전트 열 2를 입력으로 사용
- 에이전트 열 2가 에이전트 열 1을 입력으로 사용

### 카탈로그 필드에 에이전트 추가 {#add-an-agent-to-a-catalog-field}

![카탈로그 필드의 에이전트 단계.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

카탈로그 필드에 에이전트를 추가하려면:

1. 카탈로그에서 새 필드를 추가합니다.
2. **Apply AI agent**를 선택합니다.
3. 이 필드에 에이전트를 할당합니다.
4. 입력으로 전달할 열을 선택합니다. 선택하지 않으면 에이전트가 카탈로그의 모든 열에 접근할 수 있습니다.
5. (선택 사항) **필수 열에 값이 있을 때만 실행**을 활성화하여 하나 이상의 선택된 입력 열이 비어 있는 행을 건너뜁니다. 이 옵션이 켜져 있으면, 에이전트가 실행되기 위해 채워져야 하는 입력 열을 선택합니다. 선택된 모든 열은 기본적으로 필수로 시작되지만, 실행을 차단하지 않고 비어 있어도 되는 열은 제거할 수 있습니다.
6. 카탈로그 행이 업데이트될 때 에이전트가 필드를 재계산할지 결정합니다. 이 옵션을 선택하지 않으면 에이전트는 행당 한 번만 실행됩니다.
7. **필드 추가**를 선택하여 에이전트를 배포하고 비용 추정치를 검토합니다. **비용 추정** 모달은 이 카탈로그에서 에이전트가 실행될 횟수를 보여주며, 대략 총 행 수와 같습니다. 계속하려면 **확인**을 선택합니다.

![카탈로그 필드에 대해 "Apply AI agent"를 선택하는 옵션.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

### 카탈로그 에이전트 모범 사례 {#catalog-agent-best-practices}

에이전트를 카탈로그 필드에 적용하기 전에 에이전트가 필요로 하는 열을 계획하세요. 필드에 대해 필수 입력 제어를 활성화한 후, 에이전트가 읽어야 하는 데이터가 포함된 열을 선택한 다음, 실행을 차단하지 않고 비어 있어도 되는 열은 선택을 해제하세요. 에이전트는 필수로 표시된 열이 비어 있는 경우에만 해당 행을 건너뜁니다.

일부 행에서 비어 있을 것으로 예상되지만 에이전트가 여전히 실행되기를 원하는 열은 필수로 표시하지 마세요. 대신 필수 집합에서 제거하세요. 불완전한 행을 건너뛰면 잘못된 토큰 사용을 방지하고 출력 품질을 높게 유지할 수 있습니다.

| 시나리오 | 결과 |
| --- | --- |
| 플레이스홀더가 미리 채워진 행 | ID와 펀드 이름만으로 카탈로그 행을 추가한 후 나중에 다른 열을 채우면, 필수 입력 열에 값이 채워질 때까지 에이전트가 해당 행을 건너뜁니다. |
| 행이 존재한 후 에이전트 적용 | 이미 행이 있는 카탈로그의 필드에 에이전트를 적용하면, 에이전트는 모든 행을 평가하지만 필수 입력 열이 채워진 행에서만 실행됩니다. |
| 부분적으로 완성된 카탈로그 | 예를 들어, 100개의 행이 있는 카탈로그에서 `leader`가 2026 항목에 대해 채워져 있지만 다른 행에는 ID와 펀드 이름만 있고 나머지 필드가 비어 있는 경우입니다. 에이전트는 `leader` 값이 있는 행에서 실행되고, `leader`가 필수로 남아 있을 때 해당 값이 없는 행은 건너뜁니다. |
| 종속 열 | 열 3이 열 1과 2에 종속되는 경우, 에이전트는 해당 행에 열 1과 2에 값이 있을 때까지 열 3에 쓰지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="카탈로그 에이전트 모범 사례" }

### 활용 사례

| 활용 사례 | 설명 |
| --- | --- |
| 제품 설명 생성 | 새로운 카탈로그 항목에 대한 짧은 마케팅 문구를 자동으로 생성합니다. 예를 들어, 이름, 카테고리, 기능 등 구조화된 제품 데이터에서 매력적인 설명을 생성합니다. |
| 제품 속성 보강 | 제품 이름과 세부 정보를 기반으로 색상 계열, 스타일 또는 시즌 등 누락된 값을 채웁니다. 예를 들어, 제품 이름이 "Laguna Polarized Sunglasses"인 경우 에이전트가 스타일을 "스포츠"로, 색상 계열을 "블루"로 지정할 수 있습니다. |
| 파생 필드 계산 | 기존 필드를 사용하여 속성 기반의 "적합 점수"나 판매 및 리뷰 수에서 파생된 "인기 태그" 등 새로운 데이터를 생성합니다. |
| 항목 분류 또는 태그 지정 | 개인화 모델이 제품을 더 효과적으로 세분화할 수 있도록 추천 로직용 태그를 할당합니다. 예를 들어, 제품에 "아웃도어", "페스티벌 준비 완료" 또는 "프리미엄" 태그를 지정합니다. |
| 콘텐츠 현지화 | 글로벌 Campaign(캠페인)을 위해 카탈로그 텍스트를 다른 언어로 번역하거나, 지역별 채널에 맞게 톤과 길이를 조정합니다. 예를 들어, "Classic Clubmaster Sunglasses"를 스페인어로 "Gafas de sol Classic Clubmaster"로 번역하거나, SMS Campaign을 위해 설명을 단축합니다. |
| 리뷰 또는 피드백 요약 | 감정이나 피드백을 새로운 필드로 요약합니다. 예를 들어, 긍정적, 중립적 또는 부정적 감정 점수를 할당하거나 "대부분의 고객이 좋은 핏을 언급하지만 느린 배송을 지적합니다."와 같은 짧은 텍스트 요약을 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="활용 사례" }

### 응답 필드 정의 {#define-response-fields}

에이전트가 [필드]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas)를 출력 형식으로 사용하는 경우, 카탈로그 필드에서 사용할 에이전트의 해당 필드를 **Response Field**로 선택할 수 있습니다.

다음 필드로 출력 형식을 구조화하여 카탈로그에 제품 설명을 추가하는 에이전트가 있다고 가정해 보겠습니다:

| 필드 이름 | 값 |
| --- | --- |
| **description** | 텍스트 |
| **confidence_score_out_of_ten** | 숫자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="응답 필드 정의" }

카탈로그에 **product_description**이라는 필드를 추가하고 **description**을 **Response Field**로 선택하여 에이전트의 설명으로 열을 채울 수 있습니다.

!["Descriptor" 에이전트가 적용된 "product_description" 필드. "description" 출력이 응답 필드로 선택되어 있습니다.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

에이전트가 생성한 셀을 수동으로 재정의하려면 **Edit Item**을 선택하고 에이전트가 생성한 설명을 직접 수정합니다. 에이전트가 생성한 설명으로 되돌리려면 셀에서 새로고침 기호를 선택하세요.

### 오류 처리 {#error-handling}

- 실패한 카탈로그 호출은 LLM 제공자가 [사용량 제한 오류]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors)를 반환하는 경우를 포함하여 재시도되지 않습니다.
- 기반 모델 제공자에 대한 API 호출이 잘못된 API 키 오류 등 다른 오류를 반환하면 필드 값이 업데이트되지 않습니다. 카탈로그 에이전트는 에이전트 콘솔에서 대체 값 구성을 지원하지 않습니다.
- 실패한 실행에 대한 세부 정보는 에이전트의 로그에서 확인할 수 있습니다.
- 카탈로그 에이전트는 행당 최대 25KB의 입력 값을 처리할 수 있습니다.

## 에이전트 모니터링 {#monitor-your-agent}

모니터링은 에이전트가 Canvas에서 실행되든 카탈로그에서 실행되든 동일하게 작동합니다.

에이전트의 **사용량** 섹션에서 카탈로그와 Canvases에서 에이전트가 활발히 사용되고 있는 위치를 참조하고 탐색할 수 있습니다.

![Canvases에 대해 두 개의 활성 에이전트와 하나의 비활성 에이전트를 보여주는 에이전트 사용량 섹션.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

에이전트의 **로그** 섹션에서 Canvases와 카탈로그에서 발생하는 실제 에이전트 호출을 모니터링할 수 있습니다. 날짜 범위, 결과(성공 또는 실패), 호출 위치 등의 정보로 필터링할 수 있습니다. 현재 페이지에 표시된 로그만 내보내려면 **CSV 내보내기**를 선택할 수도 있습니다.

{% alert tip %}
[메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)에서 일일 호출 한도 오류를 모니터링할 수도 있습니다.
{% endalert %}

![에이전트 AI Sentiment Score에 대한 로그.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

특정 에이전트 호출에 대해 **보기**를 선택하여 입력, 출력 및 사용자 ID를 확인합니다.

![입력 프롬프트, 출력 응답 및 관련 사용자 ID를 보여주는 에이전트 Random Sports Assignment의 세부 정보 패널.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Currents 사용 {#use-currents}

다음 Currents 이벤트를 사용하여 Kafka 레코드 스키마에 접근할 수도 있습니다:

- 에이전트 실행 이벤트
- 도구 호출 이벤트

자세한 내용은 [메시지 참여 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)을 참조하세요.

## 관련 문서 {#related-articles}

- [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)
- [에이전트 참조]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [자주 묻는 질문]({{site.baseurl}}/user_guide/brazeai/agents/faq/)