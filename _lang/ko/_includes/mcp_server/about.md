# Braze MCP 서버 {#the-braze-mcp-server}

> Braze MCP 서버에 대해 알아보세요. 이는 Claude 및 Cursor와 같은 AI 도구가 비PII Braze 데이터에 접근하여 질문에 답하고, 트렌드를 분석하며, 인사이트를 제공할 수 있는 안전한 연결입니다.

{% multi_lang_include mcp_server/beta_alert.md %}

## 모델 컨텍스트 프로토콜(MCP)이란? {#what-is-model-context-protocol-mcp}

​​모델 컨텍스트 프로토콜 또는 MCP는 AI 에이전트가 다른 플랫폼의 데이터에 연결하고 작업할 수 있도록 하는 표준입니다. 주요 두 가지 부분이 있습니다:

- **MCP 클라이언트:** AI 에이전트가 실행되는 애플리케이션으로, Cursor 또는 Claude 등이 있습니다.
- **MCP 서버:** Braze와 같은 다른 플랫폼에서 제공하는 서비스로, AI가 사용할 수 있는 도구와 접근할 수 있는 데이터를 정의합니다.

## Braze MCP 서버에 대한 정보 {#about-the-braze-mcp-server}

[Braze MCP 서버를 설정한 후]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, 에이전트, 어시스턴트, 챗봇과 같은 AI 도구를 Braze에 직접 연결하여 Canvas 및 Campaign 분석, 커스텀 속성, Segments 등과 같은 집계된 데이터를 읽을 수 있습니다. Braze MCP 서버는 다음에 적합합니다:

- Braze 컨텍스트가 필요한 AI 기반 도구 구축.
- 다단계 에이전트 워크플로우를 만드는 CRM 엔지니어.
- 자연어 쿼리를 실험하는 기술 마케터.

Braze MCP 서버는 읽기 전용 및 쓰기 엔드포인트를 모두 포함합니다. Braze 고객 프로필에서 데이터를 반환하지 않습니다. Braze API 키에 할당할 엔드포인트를 선택할 수 있으며, 이 선택에 따라 에이전트가 읽거나 생성하거나 업데이트할 수 있는 항목이 결정됩니다. 사용 가능한 엔드포인트의 전체 목록과 필요한 권한에 대해서는 [사용 가능한 API 기능]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}을 참조하세요.

{% alert warning %}
에이전트에 부여하려는 API 키 권한만 할당하세요. 에이전트가 Braze에서 변경을 수행하지 않기를 원한다면 API 키를 생성할 때 쓰기 권한을 비활성화 상태로 두세요. 에이전트는 부여된 모든 쓰기 권한을 통해 데이터를 쓰려고 시도할 수 있습니다.
{% endalert %}

## 사용 예시 {#usage-example}

Claude나 Cursor와 같은 도구를 사용하여 자연어로 Braze와 상호작용할 수 있습니다. 다른 예시와 모범 사례는 [Braze MCP 서버 사용하기]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}를 참조하세요.

{% tabs %}
{% tab Claude %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Used `list_functions` and returned available Braze MCP function groups.
{% endtab %}

{% tab Cursor %}
**Example prompt:** `What are my available Braze functions?`  
**Example response:** Queried `list_functions` and listed sample functions such as `get_canvas_list`.
{% endtab %}
{% endtabs %}

## 자주 묻는 질문(FAQ) {#faq}

### 어떤 MCP 클라이언트가 지원되나요? {#which-mcp-clients-are-supported}

[Claude](https://claude.ai/)와 [Cursor](https://cursor.com/)만 공식적으로 지원됩니다. Braze MCP 서버를 사용하려면 이 클라이언트 중 하나의 계정이 있어야 합니다.

### 내 MCP 클라이언트가 어떤 Braze 데이터에 접근할 수 있나요? {#what-braze-data-can-my-mcp-client-access}

MCP 클라이언트는 PII를 반환하지 않는 엔드포인트에 접근할 수 있습니다. API 키에 할당하는 권한을 통해 에이전트가 사용할 수 있는 엔드포인트를 제어할 수 있습니다.

### 내 MCP 클라이언트가 Braze 데이터를 변경할 수 있나요? {#can-my-mcp-client-change-braze-data}

네. 서버는 에이전트가 워크스페이스에서 콘텐츠를 생성하거나 업데이트할 수 있도록 하는 제한된 쓰기 엔드포인트 세트를 노출합니다. 예를 들어 미디어 라이브러리 자산, 이메일 템플릿, Content Blocks 등이 있습니다. 각 쓰기 엔드포인트에는 고유한 API 키 권한이 필요합니다. 에이전트가 Braze에서 특정 변경을 수행하지 않기를 원한다면 API 키를 생성할 때 해당 권한을 비활성화 상태로 두세요. 쓰기 기능의 전체 목록과 필요한 권한에 대해서는 [사용 가능한 API 기능]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}을 참조하세요.

### Braze에 대해 서드파티 MCP 서버를 사용할 수 있나요? {#can-i-use-a-third-party-mcp-server-for-braze}

Braze 데이터에 대해 서드파티 MCP 서버를 사용하는 것은 권장되지 않습니다. [PyPi](https://pypi.org/project/braze-mcp-server/)에 호스팅된 공식 Braze MCP 서버만 사용하세요.

### Braze MCP 서버가 PII 접근을 제공하지 않는 이유는 무엇인가요? {#why-doesnt-the-braze-mcp-server-offer-pii-access}

유용한 사용 사례를 지원하면서 사용자 데이터를 보호하기 위해, 서버는 일반적으로 PII를 반환하지 않는 엔드포인트로 제한됩니다. 이를 통해 워크스페이스와 그 안의 사용자에 대한 위험을 줄입니다.

### API 키를 재사용할 수 있나요? {#can-i-reuse-my-api-keys}

아니요. MCP 클라이언트를 위해 새로운 API 키를 생성해야 합니다. AI 도구에는 자신이 편안하게 느끼는 수준의 접근 권한만 부여하고, 과도한 권한은 피하세요.

### Braze MCP 서버는 로컬에 호스팅되나요, 아니면 원격에 호스팅되나요? {#is-the-braze-mcp-server-hosted-locally-or-remotely}

Braze MCP 서버는 로컬에 호스팅됩니다.

### Cursor가 함수만 나열하는 이유는 무엇인가요? {#why-is-cursor-only-listing-functions}

ask 모드인지 agent 모드인지 확인하세요. MCP 서버를 사용하려면 agent 모드에 있어야 합니다.

### 에이전트가 잘못된 것처럼 보이는 답변을 반환할 때는 어떻게 해야 하나요? {#what-do-i-do-when-the-agent-returns-an-answer-that-looks-incorrect}

Cursor와 같은 도구를 사용할 때는 사용 중인 모델을 변경해 보세요. 예를 들어, 자동으로 설정되어 있다면 특정 모델로 변경하고 어떤 모델이 사용 사례에 가장 적합한지 실험해 보세요. 새로운 채팅을 시작하고 프롬프트를 다시 시도해 볼 수도 있습니다.

문제가 지속되면 [mcp-product@braze.com](mailto:mcp-product@braze.com)으로 이메일을 보내 알려주세요. 가능하다면 비디오를 포함하고 호출 함수를 확장하여 에이전트가 시도한 호출을 볼 수 있도록 해주세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}