# Braze MCP 서버 {#the-braze-mcp-server}

> Braze MCP 서버에 대해 알아보세요. 이는 Claude 및 Cursor와 같은 AI 도구가 비PII Braze 데이터에 접근하여 질문에 답하고, 트렌드를 분석하며, 인사이트를 제공하고, 콘텐츠를 생성할 수 있는 안전한 원격 연결입니다.

{% alert important %}
원격 MCP 서버는 얼리 액세스 단계입니다. 액세스를 요청하려면 계정 매니저에게 문의하세요.
{% endalert %}

## MCP(Model Context Protocol)란 무엇인가요? {#what-is-model-context-protocol-mcp}

​​Model Context Protocol(MCP)은 AI 에이전트가 다른 플랫폼의 데이터에 연결하고 작업할 수 있도록 하는 표준입니다. MCP는 두 가지 주요 구성 요소로 이루어져 있습니다:

- **MCP 클라이언트:** Cursor나 Claude와 같이 AI 에이전트가 실행되는 애플리케이션입니다.
- **MCP 서버:** Braze와 같은 다른 플랫폼에서 제공하는 서비스로, AI가 사용할 수 있는 도구와 접근할 수 있는 데이터를 정의합니다.

## Braze MCP 서버 소개 {#about-the-braze-mcp-server}

[Braze MCP 서버를 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}한 후, 에이전트, 어시스턴트, 챗봇과 같은 AI 도구를 Braze에 직접 연결하여 Canvas 및 Campaign 분석, 커스텀 속성, Segments 등의 집계 데이터를 읽을 수 있습니다. Braze MCP 서버는 다음과 같은 용도에 적합합니다:

- Braze 컨텍스트가 필요한 AI 기반 도구 구축.
- 다단계 에이전트 워크플로를 생성하는 CRM 엔지니어.
- 자연어 쿼리를 실험하는 기술 마케터.

Braze MCP 서버에는 읽기 및 쓰기 도구가 모두 포함되어 있습니다. 이러한 도구는 Braze 고객 프로필의 데이터를 반환하지 않습니다. 에이전트는 Braze 대시보드 사용자 권한을 상속합니다. 사용 가능한 도구의 전체 목록은 [사용 가능한 API 함수]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}를 참조하세요.

{% alert warning %}
사용자 수준의 PII를 노출하는 도구는 사용할 수 없습니다.
{% endalert %}

MCP 서버를 사용하여 Campaign 및 Canvas 성능에 대해 질문하고, Segments 및 커스텀 속성을 탐색하고, 보고서를 생성하고, 자연어를 통해 이메일 템플릿, Content Blocks, 미디어 라이브러리 에셋과 같은 콘텐츠를 생성할 수 있습니다.

## 베타 MCP 서버는 더 이상 지원되지 않나요? {#is-the-beta-mcp-server-deprecated}

네. 2025년 8월에 출시된 로컬 호스팅 MCP 서버는 더 이상 지원되지 않으며 추가 업데이트가 제공되지 않습니다. 계속 사용할 수는 있지만, Braze에서는 원격 호스팅 버전으로 마이그레이션할 것을 권장합니다.

### 원격 서버는 어떻게 다른가요? {#how-is-the-remote-server-different}

이전 Braze MCP 서버는 로컬 머신에서 실행되었습니다. 패키지를 설치하고, 구성 파일을 관리하며, 적절한 권한이 있는 Braze API 키를 생성해야 했습니다. 원격 MCP 서버는 이러한 로컬 설정을 제거합니다.

지원되는 MCP 클라이언트에서 1분 이내에 연결할 수 있습니다. 인증은 OAuth를 사용합니다. 접근 권한은 공유 API 키가 아닌 Braze 대시보드 사용자 계정에 연결되므로, 에이전트가 보고 수행할 수 있는 작업이 대시보드 권한과 동일하게 반영됩니다. 대시보드 사용자가 Braze에서 접근 권한을 잃으면 클라이언트도 접근 권한을 잃게 됩니다.

주요 차이점은 다음과 같습니다:

- **설정:** 패키지를 설치하고 구성 파일을 편집하는 대신 Braze URL을 붙여넣기만 하면 됩니다.
- **인증:** API 키를 생성하는 대신 Braze 계정으로 로그인합니다.
- **권한:** API 키 권한이 아닌 대시보드 사용자 계정을 기반으로 접근 권한이 부여됩니다.
- **워크스페이스 타겟팅:** 로컬 구성에 고정되는 대신 요청별로 워크스페이스 컨텍스트가 전달됩니다.

## 자주 묻는 질문(FAQ) {#faq}

### 어떤 MCP 클라이언트가 지원되나요? {#which-mcp-clients-are-supported}

OAuth를 지원하는 원격 MCP 서버와 호환되는 모든 MCP 클라이언트를 사용할 수 있습니다. Braze가 검증한 클라이언트는 다음과 같습니다:

- 커스텀 커넥터를 통한 Claude
- 커스텀 커넥터를 통한 ChatGPT
- Cursor
- OpenAI Codex
- Claude Code
- Visual Studio Code

### 내 MCP 클라이언트가 어떤 Braze 데이터에 접근할 수 있나요? {#what-braze-data-can-my-mcp-client-access}

MCP 클라이언트는 사용자 수준 PII를 반환하지 않는 도구에 접근할 수 있습니다.

### 내 MCP 클라이언트가 Braze 데이터를 변경할 수 있나요? {#can-my-mcp-client-change-braze-data}

네, 대시보드 사용자에게 해당 권한이 있는 경우 가능합니다.

### Braze API 키가 여전히 필요한가요? {#do-i-still-need-a-braze-api-key}

MCP에는 필요하지 않습니다. API 키는 REST API에서 계속 작동하며 더 이상 사용되지 않는 것은 아닙니다.

### 어떤 리전이 지원되나요? {#which-regions-are-supported}

두 Braze 클러스터 모두 지원됩니다. 현재 두 개의 엔드포인트를 사용할 수 있습니다:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

어느 엔드포인트든 모든 Braze 클러스터에 접근할 수 있습니다.

### 검증된 목록 외의 도구에서 Braze 원격 MCP 서버를 사용할 수 있나요? {#can-i-use-the-braze-remote-mcp-server-with-tools-other-than-the-verified-list}

시도할 수 있지만 인증이 차단될 수 있습니다. Braze는 현재 보안을 위해 지원되는 도메인의 허용 목록을 유지하고 있습니다. 도구가 목록에 없고 인증 문제가 발생하면 [mcp-product@braze.com](mailto:mcp-product@braze.com)으로 문의하세요.

### 원격 서버가 여러 워크스페이스를 지원하나요? {#does-the-remote-server-support-multiple-workspaces}

네. 대화별 또는 요청별로 워크스페이스를 지정할 수 있습니다. 하나의 연결로 접근 권한이 있는 모든 워크스페이스를 사용할 수 있습니다.

### 에이전트가 사용자 수준 PII에 접근할 수 있나요? {#can-my-agent-access-user-level-pii}

아니요. 현재 PII를 노출하는 도구는 사용할 수 없습니다.

### 권한이 변경되면 어떻게 되나요? {#what-happens-when-my-permissions-change}

에이전트 접근 권한은 대시보드 사용자에 따라 변경됩니다. 권한 변경은 다음 요청 시 적용됩니다. 비활성화된 대시보드 사용자는 MCP 접근 권한을 잃습니다.

### 클라이언트 디렉토리에서 Braze 커넥터가 보이지 않는 이유는 무엇인가요? {#why-do-i-not-see-the-braze-connector-in-my-clients-directory}

디렉토리 목록은 얼리 액세스가 시작된 후 순차적으로 제공됩니다. Braze MCP URL을 사용하여 언제든지 수동으로 연결할 수 있습니다.

### 우리 회사에서 IP 허용 목록을 사용합니다. 원격 MCP 서버를 사용할 수 있나요? {#my-company-uses-ip-allowlisting-can-we-use-the-remote-mcp-server}

현재는 불가능합니다. [IP 허용 목록](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting)을 사용하는 고객은 얼리 액세스 프로그램에 참여할 수 없습니다.

{% multi_lang_include mcp_server/legal_disclaimer.md %}