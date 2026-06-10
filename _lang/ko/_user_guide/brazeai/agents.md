---
nav_title: 에이전트 콘솔
article_title: Braze 에이전트
page_order: 1
description: "Braze 에이전트는 콘텐츠를 생성하고, 지능적인 결정을 내리며, 데이터를 보강하여 보다 개인화된 고객 경험을 제공할 수 있도록 합니다."
---

# 에이전트 콘솔의 Braze 에이전트 {#braze-agents-in-agent-console}

> Braze 에이전트는 Braze 내에서 생성할 수 있는 AI 기반 도우미입니다. 에이전트는 콘텐츠를 생성하고, 지능적인 결정을 내리며, 데이터를 보강하여 보다 개인화된 고객 경험을 제공할 수 있도록 합니다.

{% alert important %}
Braze 에이전트에 접근하고 사용하려면 메시지 또는 동작 크레딧이 필요합니다. 현재 동작 크레딧이 없고 Braze 에이전트를 사용하고 싶다면, 다음 단계를 위해 계정 매니저에게 문의하세요.
{% endalert %}

에이전트 콘솔의 Braze 에이전트에 대한 개요를 보려면 이 동영상을 시청하세요.

{% multi_lang_include video.html id="afd0hp0vrh" source="wistia" title="Braze Agents in Agent Console overview" %}

## Braze 에이전트를 사용하는 이유 {#why-use-braze-agents}

Braze 에이전트는 추가 작업 없이도 팀이 더 스마트하고 개인화된 경험을 제공할 수 있도록 도와줍니다. 에이전트는 단순히 프롬프트에 응답하는 것이 아니라, 컨텍스트를 이해하고, 결정을 내리며, 목표를 향해 행동하는 자율 에이전트로 작동합니다.

실제로 에이전트는 제목란이나 제품 내 텍스트와 같은 메시지 카피를 자동으로 생성할 수 있어, 모든 고객이 자신에게 맞춤화된 커뮤니케이션을 받을 수 있습니다. 또한 실시간으로 적응하여 선호도, 동작 또는 기타 데이터를 기반으로 사용자를 다양한 Canvas 경로로 라우팅할 수 있습니다.

메시징을 넘어, 에이전트는 제품 및 프로필 필드 값을 계산하거나 생성하여 카탈로그를 보강하고 데이터를 최신 상태로 동적으로 유지할 수 있습니다. 반복적이거나 복잡한 작업을 맡아 팀이 수동 설정 대신 전략과 창의성에 집중할 수 있도록 합니다. Braze 에이전트는 백그라운드 프로세스가 아닌 협력자처럼 작동하여 문제를 해결하고 대규모로 영향을 전달하는 데 도움을 줍니다.

### Braze 에이전트와 다른 BrazeAI 기능의 사용 시점 {#when-to-use-braze-agents-versus-other-brazeai-features}

사용자의 특정 컨텍스트를 활용하여 콘텐츠를 즉석에서 개인화할 때 에이전트를 사용하세요. 예를 들어, 에이전트가 특정 사용자의 좋아하는 아이스크림 맛이 초콜릿이고 좋아하는 토핑이 젤리곰이라는 것을 알고 있다면, 해당 사용자가 Canvas를 통과할 때 그 조합에 맞는 푸시 카피를 작성할 수 있습니다.

그러나 에이전트는 시행착오를 통해 학습하지 않으며, 측정하고 극대화하려는 궁극적인 마케팅 목표에 대한 개념이 없습니다. 전환을 유도하는 카피를 일반적으로 작성하라고 지시하더라도, 에이전트가 작성한 카피의 전환 영향을 "모니터링"하고 그 데이터를 향후 에이전트 호출에 통합하는 메커니즘이 없습니다. 이것은 보상 기반 인공지능 의사 결정이 아닌 "감각적" 의사 결정이라고 생각할 수 있습니다.

반면, 다른 BrazeAI 도구는 측정 중인 측정기준을 극대화하도록 설계되었습니다. 예를 들어, 에이전트는 사용자의 특성이 특정 이벤트를 수행하거나 특정 제품을 좋아할 가능성에 어떻게 영향을 미치는지 정성적으로 평가하는 데 매우 뛰어납니다. 그러나 에이전트는 시행착오를 통해 학습하지 않기 때문에, 가능성 예측의 정확성을 측정하고 시간이 지남에 따라 신호를 개선하는 방법을 알지 못합니다. 따라서 예측의 정확성과 시간에 따른 개선 측면에서 Predictive Suite를 사용하는 것이 에이전트 단계보다 더 우수한 성과를 보입니다.

## 기능 {#features}

Braze 에이전트의 기능은 다음과 같습니다:

- **유연한 설정:** Braze에서 제공하는 LLM을 사용하거나 OpenAI, Anthropic, Google Gemini 또는 Databricks Mosaic과 같은 자체 [AI 모델 제공업체]({{site.baseurl}}/partners/ai_model_providers/)를 연결하세요.
- **원활한 통합:** 에이전트를 캔버스 단계나 카탈로그 필드에 직접 배포하세요.
- **테스트 및 로깅 도구:** 시작 전에 샘플 입력으로 테스트하여 에이전트의 출력을 미리보기하세요. 에이전트가 실행될 때마다 해당 실행의 입력 및 출력을 포함한 로그를 확인하세요.
- **사용량 제어:** 일일 한도로 성능과 비용을 관리할 수 있습니다.

## Braze 에이전트에 대하여 {#about-braze-agents}

에이전트는 동작 방식을 정의하는 지침(시스템 프롬프트)으로 구성됩니다. 에이전트가 실행되면 전달된 데이터와 함께 지침을 사용하여 응답을 생성합니다. 에이전트는 선택된 컨텍스트와 지침에서 제공되는 것 이외의 사용자 데이터에는 접근할 수 없습니다.

### 핵심 개념 {#key-concepts}

| 용어 | 정의 |
| --- | --- |
| [모델]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) | 에이전트의 "두뇌"로, 이 경우 대규모 언어 모델(LLM)입니다. 입력을 해석하고, 응답을 생성하며, 추론을 수행합니다. 더 강력한 모델(더 관련성 높은 데이터로 훈련됨)은 에이전트를 더 유능하고 다재다능하게 만듭니다. |
| [지침]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) | 에이전트에게 제공하는 규칙이나 가이드라인(시스템 프롬프트)입니다. 에이전트가 실행될 때마다 어떻게 동작해야 하는지를 정의합니다. 명확한 지침은 에이전트를 더 신뢰할 수 있고 예측 가능하게 만듭니다. |
| 컨텍스트 | 에이전트가 배포된 곳에서 런타임에 전달되는 데이터로, 고객 프로필 필드나 카탈로그 행 등이 있습니다. 이 입력은 에이전트가 출력을 생성하는 데 사용하는 정보를 제공합니다. |
| [Canvas 컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#how-context-variables-work) | 특정 Canvas를 통한 사용자 여정 내에서 생성하고 사용할 수 있는 임시 데이터입니다. |
| [출력 변수]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/#define-the-output-variable) | 캔버스 단계에서 사용될 때 에이전트가 생성하는 출력입니다. 출력 변수는 콘텐츠를 개인화하거나 워크플로 경로를 안내하기 위해 에이전트의 결과를 저장합니다. 출력 변수는 문자열, 숫자 또는 부울 데이터 유형일 수 있습니다. |
| [실행](#limitations) | 에이전트의 단일 실행입니다. 일일 한도에 포함됩니다. |
| [출력 형식]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#select-output) | 에이전트 응답의 미리 정의된 데이터 구조입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="핵심 개념" }

## 제한 사항 {#limitations}

다음 제한 사항이 적용됩니다:

- 각 에이전트는 기본적으로 하루 250,000회의 실행 한도가 있으며, 하루 최대 1,000,000회까지 늘릴 수 있습니다. 이 한도를 늘리고 싶다면 고객 성공 매니저에게 문의하세요.
- 기본적으로 각 실행은 20초 이내에 완료되어야 합니다. 20초가 지나면 에이전트는 사용된 곳에서 `null` 응답을 반환합니다.
    - 에이전트가 지속적으로 시간 초과되는 경우 Braze 계정 매니저에게 문의하여 이 한도를 늘리세요.
- 입력 데이터는 요청당 25KB로 제한됩니다. 더 긴 입력은 잘립니다.

## 오류 처리 {#error-handling}

Canvas 에이전트 단계에서 연결된 모델이 LLM 제공업체로부터 [사용량 제한 오류]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors)를 반환하면, Braze는 지수 백오프를 사용하여 최대 5회까지 요청을 재시도합니다. 시간 초과나 잘못된 API 키와 같은 기타 실패의 경우, 에이전트 출력은 `null`로 설정됩니다. 에이전트가 일일 실행 한도에 도달한 경우에도 출력은 `null`로 설정됩니다.

많은 사용자가 동시에 에이전트 단계에 진입하면, [실행 흐름 제어]({{site.baseurl}}/user_guide/brazeai/agents/reference/#invocation-flow-controls)로 인해 처리 시간이 더 오래 걸릴 수 있습니다. 메시지에서 null 출력에 대비하려면 [기본 Liquid 값]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/)을 사용하세요.

## 내 데이터는 어떻게 사용되고 Braze 제공 LLM에 전송되나요? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Braze가 Braze 제공 LLM을 활용하는 것으로 식별한 Braze AI 기능을 통해 AI 출력("출력")을 생성하기 위해, Braze는 시스템 프롬프트 또는 해당되는 경우 기타 입력("입력")을 Braze 제공 LLM에 전송합니다. 해당 Braze 제공 LLM에 전송된 데이터는 Braze 제공 LLM을 훈련하거나 개선하는 데 사용되지 않습니다. 귀하와 Braze 간의 관계에서 출력은 귀하의 지적 재산입니다. Braze는 해당 출력에 대한 저작권 소유권 주장을 하지 않습니다. Braze는 출력을 포함한 AI 생성 콘텐츠 전반에 대해 어떠한 종류의 보증도 하지 않습니다.

Braze 에이전트를 위한 Braze 제공 LLM은 "Auto"로 식별되며, Google Gemini 모델을 사용합니다. Google은 Braze를 통해 제출된 입력 및 출력을 55일 동안 보관하며, 그 후 데이터는 삭제됩니다.

## 다음 단계 {#next-steps}

이제 Braze 에이전트에 대해 알게 되었으니, 다음 단계를 진행할 준비가 되었습니다:

- [커스텀 에이전트 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [커스텀 에이전트 배포]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)