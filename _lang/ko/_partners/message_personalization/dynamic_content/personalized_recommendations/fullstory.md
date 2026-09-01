---
nav_title: Fullstory
article_title: Fullstory
description: "이 참고 문서에서는 Braze와 Fullstory의 파트너십에 대해 설명합니다."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Fullstory

> [Fullstory](https://www.fullstory.com/)의 행동 데이터 플랫폼은 기술 리더가 더 나은 정보에 기반한 의사 결정을 내릴 수 있도록 지원합니다. Fullstory의 특허 기술은 디지털 행동 데이터를 분석 스택에 주입하여 양질의 행동 데이터를 대규모로 활용함으로써 모든 디지털 방문을 유용한 인사이트로 전환합니다.

*이 통합은 Fullstory에서 유지 관리합니다.*

## 이 통합에 대하여 {#about-this-integration}

Braze에서 Fullstory 인사이트를 활용하여 사용자의 웹사이트 또는 앱 경험을 순간순간 파악하고, 상황별 맞춤 메시징을 전달할 수 있습니다. Fullstory의 Session Summary API를 사용하면 사용자의 브라우징 행동에 대한 상세한 메타데이터를 캡처하여 Braze 메시징에 활용할 수 있으며, 이는 Canvas와 같은 다단계 메시징 여정에서 특히 강력한 효과를 발휘합니다.

Fullstory의 세션 요약 데이터가 가진 실시간 가치는 연결된 콘텐츠를 통해 가장 잘 활용됩니다. Canvas Context 단계에서 연결된 콘텐츠를 사용하면 사용자의 Canvas 여정 전반에 걸쳐 Fullstory 데이터를 저장하고, 이후 모든 캔버스 단계에서 활용할 수 있습니다. 이를 통해 커스텀 이벤트나 속성을 사용하여 Braze 고객 프로필에 데이터를 기록할 필요도 없어집니다.

다음 예시에서는 Canvas Context 데이터를 Agent AI Canvas 단계에서 활용하여 사용자가 유기한 장바구니를 다시 확인하도록 유도하는 최적의 메시지를 생성합니다. 이 외에도 이 데이터를 활용하여 메시지를 직접 개인화하거나, 오디언스 경로를 통해 사용자의 여정을 결정하거나, 후속 메시징 단계에서 사용할 문구나 에셋을 결정할 수 있습니다.

## 사전 요구 사항 {#prerequisites}

시작하기 전에 다음이 필요합니다:

|요구 사항     | 설명 |
|-----------------------|-----------------|
| Fullstory Session API 인증 토큰   | 이 가이드의 1단계를 참조하세요. |
| Braze 연결된 콘텐츠 인증 토큰 활성화 | 이 섹션의 얼리 액세스 참고 사항을 확인하세요. |
| Braze Canvas 컨텍스트 단계 | 이 섹션의 얼리 액세스 참고 사항을 확인하세요. |
| Braze AI 에이전트 단계 활성화 | 이 섹션의 얼리 액세스 참고 사항을 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

{% alert important %}
Braze 에이전트, Canvas 컨텍스트, 연결된 콘텐츠 인증 토큰은 모두 얼리 액세스 단계에 있습니다. 이 솔루션을 활용하는 데 관심이 있으시면 Braze CSM에게 이러한 도구의 활성화에 대해 문의하세요.
{% endalert %}

## Fullstory 통합 {#integrate-fullstory}

### 1단계: 세션 요약 API 활성화를 위한 Fullstory 설정 {#step-1}

#### 1.1단계: 세션 요약 API 엔드포인트의 인증 토큰 검색 {#step-11-retrieve-the-authentication-token-for-the-session-summary-api-endpoint}

[Fullstory API 키](https://developer.fullstory.com/server/authentication/)를 생성하려면:

1. Fullstory에서 **Settings** > **API Keys**로 이동합니다.
2. **Standard** 권한 수준을 선택합니다.
3. 키 값은 한 번만 표시되므로 즉시 복사합니다.

#### 1.2단계: 세션 요약 프로필 ID 생성 {#step-12-create-a-session-summary-profile-id}

[Fullstory의 안내](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles)에 따라 전용 엔드포인트를 사용하여 세션 요약 프로필을 생성합니다. 이 단계에서 세션 요약 응답이 Braze에 제공할 데이터 유형을 정의합니다.

이 요청에 대한 응답에서 Fullstory는 세션 프로필 ID를 제공합니다. 이 프로필 ID는 다음 사용 사례에서 사용되는 연결된 콘텐츠 요청 본문의 핵심 구성 요소입니다.

### 2단계: 연결된 콘텐츠 토큰 인증 생성 {#step-2-create-the-connected-content-token-authentication}

1. Braze에서 **Settings** > **Workspace Settings** > **Connected Content** > **Add Credential** > **Token Authentication**으로 이동합니다.
2. 인증 이름을 `fullstory`로 지정합니다.
3. 헤더 키 "Authorization"을 추가합니다. 이전 단계에서 Fullstory가 제공한 헤더 값을 입력합니다.
4. **Allowed Domain**에 **api.fullstory.com**을 입력합니다.

![자격 증명 편집 필드를 보여주는 Braze 스크린샷]({% image_buster /assets/img/fullstory/1.png %}){: style="max-width:50%;"}

## 사용 사례 {#use-cases}

### 동적 메시지 여정 만들기 {#create-dynamic-message-journeys}

Fullstory의 [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams)를 사용하면 주요 사용자 상호작용 직후에 Braze Canvases를 트리거할 수 있습니다. 이 통합의 핵심은 고유한 `client_session_id`({% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}를 통해 접근 가능)에 있으며, 시스템이 Fullstory에서 Braze로 자동 전달합니다. 이 ID는 키 역할을 하여 Braze가 사용자가 경험한 내용의 전체 세션 요약을 정확히 가져올 수 있도록 합니다.

Canvas 컨텍스트 단계와 연결된 콘텐츠를 활용하면 이 ID를 사용하여 Fullstory에 API 요청을 보내고, 세션 데이터를 검색한 후 여정의 이후 단계에서 사용할 수 있도록 변수로 저장할 수 있습니다.

![Braze Canvas 컨텍스트 단계에서 컨텍스트 변수 "summary_result"가 생성되고 Fullstory에 대한 연결된 콘텐츠 호출로 채워져 세션 요약을 검색하는 모습]({% image_buster /assets/img/fullstory/2.png %})

앞서 생성한 인증 토큰을 사용하여 다음 요청 구조로 세션 요약 데이터를 가져옵니다.

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert note %}
응답은 Liquid 태그 {% raw %}`{{context.${summary_result}.response}}`{% endraw %}로 저장됩니다. 이후 캔버스 단계에서 이 컨텍스트 태그를 사용하세요.
{% endalert %}

이 단계에서 Canvas는 사용자 세션에 대한 전체 메시지 페이로드를 포함하는 연결된 콘텐츠 호출의 응답에 접근할 수 있습니다.

{% details 세션 요약 API의 페이로드 예시 %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

사용자의 Canvas 여정 후반부에서 컨텍스트 Liquid 태그를 사용하여 위 객체에서 사용 가능한 모든 데이터를 활용할 수 있습니다. 다음 단계에서는 [에이전트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) 단계에서 이 데이터를 사용하는 방법을 보여줍니다.

{% alert note %}
예기치 않은 동작을 방지하려면 컨텍스트 단계 뒤에 오디언스 경로 단계를 포함하세요. 이 단계에서 컨텍스트 태그가 비어 있는 사용자를 컨텍스트에서 제외할 수 있으며, 이는 연결된 콘텐츠 호출이 실패했거나 정보를 반환하지 않았음을 나타냅니다.

![Braze의 오디언스 경로 단계]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

### 적절한 메시지 문구 생성 {#produce-appropriate-copy}

Fullstory에 의해 트리거되는 Canvas에서 [에이전트 단계]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)를 만들고 이 섹션에서 설명한 컨텍스트 단계를 포함하면, 에이전트에서 Fullstory의 세션 요약 데이터를 참조할 수 있습니다.

이 예시에서는 이 데이터를 사용하여 Braze 에이전트가 콘텐츠 카드에 사용할 적절한 메시지 문구를 생성하도록 하며, 이를 통해 사용자가 유기한 장바구니로 돌아가도록 유도할 수 있습니다.

![프롬프트가 포함된 Braze 에이전트 컨텍스트 생성기의 스크린샷]({% image_buster /assets/img/fullstory/4.png %})

이 단계에서 생성한 컨텍스트 Liquid 태그에 앞서 만든 AI 에이전트 단계에서 사용한 컨텍스트 Liquid 태그와 동일한 이름을 사용하세요.

사용 사례에 따라 필요한 프롬프트는 달라집니다. 효과적인 에이전트 프롬프트 작성에 대한 모범 사례는 [지침 작성]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions)을 참조하세요.

Canvas에서 AI 에이전트 단계를 선택한 다음 드롭다운에서 **Session Context** 에이전트를 선택합니다. 출력을 변수로 저장합니다. 이 경우 "message"로 저장하며, Liquid 태그 {% raw %}`{{context.${message}.message}}`{% endraw %}를 사용하여 메시지 문구에 넣을 수 있습니다.

![프롬프트가 포함된 Braze 에이전트 컨텍스트 Canvas 단계의 스크린샷]({% image_buster /assets/img/fullstory/5.png %})

AI 에이전트가 생성한 문구를 활용하는 메시지 단계를 만듭니다. 이 단계에서 Liquid 태그를 사용하세요.

{% alert important %}
Fullstory의 세션 요약 API는 민감한 식별 가능 사용자 데이터를 반환할 수 있습니다. PII(개인 식별 정보)를 처리하는 동안 규정을 준수하려면, 이 사용 사례를 활용하기 전에 Fullstory 데이터 캡처 규칙에서 PII가 제외되어 있는지 확인하세요.
{% endalert %}