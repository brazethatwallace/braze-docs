# Braze MCP 서버 설정하기 {#setting-up-the-braze-mcp-server}

> Braze 원격 MCP 서버에 연결하고, OAuth로 인증하고, MCP 클라이언트에서 Braze 도구를 사용하는 방법을 알아보세요. 자세한 내용은 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건 {#prerequisites}

시작하기 전에 다음 사항을 확인하세요:

| 필수 조건 | 설명 |
|--------------|-------------|
| 지원되는 MCP 클라이언트 | OAuth를 사용하는 원격 MCP 서버를 지원하는 모든 클라이언트를 사용할 수 있습니다. Braze에서는 Claude, ChatGPT, Cursor, OpenAI Codex, Claude Code, Visual Studio Code에서 검증을 완료했습니다. |
| Braze 대시보드 계정 | 일반 Braze 자격 증명으로 로그인합니다. 회사에서 SSO 또는 SAML을 사용하는 경우에도 동일하게 적용됩니다. 별도의 MCP 로그인은 필요하지 않습니다. |
| 서버 엔드포인트 선택 | `https://mcp.braze.com/mcp`(US) 또는 `https://mcp.braze.eu/mcp`(EU) 중에서 선택하세요. 두 엔드포인트 모두 모든 Braze 클러스터에 접근할 수 있습니다. |
| IP 허용 목록 미지원 | [IP 허용 목록](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting)을 사용하는 고객은 현재 Braze MCP 서버를 사용할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

{% alert note %}
에이전트의 접근 권한은 대시보드 권한을 그대로 반영합니다. 대시보드 접근 권한이 전체 워크스페이스가 아닌 특정 팀으로 제한된 경우, 일부 도구가 작동하지 않을 수 있습니다.
{% endalert %}

## 접근 관리 (관리자용) {#managing-access-for-admins}

{% alert note %}
사용자가 연결하려면 먼저 회사 관리자가 **설정** > **관리자 설정** > **OAuth**에서 **MCP OAuth 접근**을 활성화해야 합니다. 자세한 내용은 [OAuth 설정 관리]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)를 참조하세요.
{% endalert %}

### 접근 권한 부여 {#grant-access}

관리자는 "Use MCP Server" 권한을 통해 MCP 서버에 대한 접근을 제어합니다. 기본적으로 사용자에게는 이 권한이 없으며, 명시적으로 부여해야 합니다.

### 접근 권한 해제 {#revoke-access}

접근 권한을 해제하려면 사용자에게서 "Use MCP Server" 권한을 제거하세요. 사용자의 대시보드 권한을 제거하면 다음 요청 시 연결된 모든 에이전트에서도 해당 기능이 제거됩니다.

### 사용 감사 {#audit-usage}

사용자가 OAuth를 통해 성공적으로 연결하면 [보안 이벤트 보고서](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report)에 이벤트가 기록됩니다.

## 클라이언트 연결하기 {#connect-your-client}

### 1단계: 권한 및 워크스페이스 접근 권한 확인하기 {#step-1-confirm-permissions-and-workspace-access}

1. 본인 또는 회사 관리자에게 "Use MCP Server" 권한이 있는지 확인해야 합니다.
2. 여러 워크스페이스에 접근해야 하는 경우, 관련된 모든 워크스페이스에서 해당 권한이 활성화되어 있는지 확인하세요.

### 2단계: Braze를 원격 MCP 커넥터로 추가하기 {#step-2-add-braze-as-a-remote-mcp-connector}

MCP 클라이언트에서 새 원격 서버 또는 커스텀 커넥터를 추가하고 Braze MCP URL을 입력합니다. 예를 들어, Claude에서는 **Settings** > **Connectors** > **Add custom connector**로 이동하여 URL을 붙여넣을 수 있습니다.

클라이언트 ID, 클라이언트 시크릿 또는 API 키는 필요하지 않습니다. 클라이언트가 Braze에 자동으로 등록됩니다.

Braze MCP 엔드포인트 옵션:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

{% alert tip %}
EU 고객은 EU 엔드포인트를 사용해야 합니다. EU 이외의 고객은 어느 엔드포인트든 사용할 수 있습니다.
{% endalert %}

클라이언트 설정 가이드:

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)
- [Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

### 3단계: OAuth를 통해 Braze에 로그인하기 {#step-3-sign-in-to-braze-through-oauth}

에이전트가 처음으로 Braze 도구를 호출하면 클라이언트가 브라우저 창을 열어 Braze 로그인 페이지로 이동합니다.

1. SSO가 필요한 경우를 포함하여 평소와 같이 Braze에 로그인합니다.
2. 동일한 클러스터에서 둘 이상의 회사에 접근할 수 있는 로그인인 경우, 사용할 회사를 선택합니다.
3. 동의 화면에서 애플리케이션이 요청하는 접근 권한을 검토합니다.
4. 동의 체크박스를 선택하여 Braze 개인정보 보호정책에 동의한 다음, **Continue**를 선택하여 MCP 클라이언트로 돌아갑니다.

![Claude Desktop이 Braze 계정 정보 및 Braze 데이터에 대한 광범위한 접근을 요청하고 있음을 보여주는 Braze 동의 화면. 개인정보 보호정책 동의 체크박스와 Cancel 및 Continue 버튼이 표시됩니다.]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: width="639" height="1024" style="max-width:65%;"}

세션은 자동으로 갱신되는 단기 접근 토큰을 사용합니다. 가끔 다시 로그인해야 할 수 있습니다.

### 4단계: 에이전트에 사용할 워크스페이스 지정하기 {#step-4-tell-your-agent-which-workspace-to-use}

계정이 둘 이상의 워크스페이스에 접근할 수 있는 경우, 프롬프트에서 워크스페이스를 지정하세요. 예를 들어:

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

워크스페이스를 지정하지 않으면, 에이전트가 확인을 요청할 수 있습니다.

### 5단계: 테스트 프롬프트 전송하기 {#step-5-send-a-test-prompt}

설정 후 다음과 같은 간단한 검증 프롬프트를 전송하세요:

- `List the Braze tools available in this workspace.`
- `Show my recent Canvases from the Production workspace.`

더 많은 예시는 [Braze MCP 서버 사용하기]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}를 참조하세요.

## 예시: Claude와 연결하기 {#example-connect-with-claude}

클라이언트를 연결하는 데는 몇 단계만 필요합니다. 다음 안내에서는 Claude를 사용하지만, 다른 지원 클라이언트에서도 흐름은 비슷합니다.

1. Claude에서 **Settings** > **Connectors** > **Add custom connector**로 이동합니다.
2. `Braze`와 같은 이름을 입력한 다음, Braze MCP URL을 붙여넣습니다: US의 경우 `https://mcp.braze.com/mcp`, EU의 경우 `https://mcp.braze.eu/mcp`를 입력합니다. 클라이언트 ID, 클라이언트 시크릿, 또는 API 키는 필요하지 않습니다.
3. **Add**를 선택하여 커넥터를 저장합니다. Claude가 자동으로 Braze에 등록됩니다.
4. **Connect**를 선택하여 인증을 시작합니다. Claude가 브라우저 창을 열고 Braze 로그인 페이지로 이동합니다.
5. SSO를 사용하는 경우를 포함하여, 일반적으로 사용하는 자격 증명으로 Braze에 로그인합니다. 동일한 클러스터에서 두 개 이상의 회사에 접근할 수 있는 로그인인 경우, 사용할 회사를 선택합니다.
6. 동의 화면에서 요청된 접근 권한을 검토하고, 확인 체크박스를 선택한 다음 **Continue**를 선택합니다. Claude가 채팅으로 돌아가며, 이제 에이전트에서 Braze 도구를 사용할 수 있습니다.

연결을 확인하려면 `Show my recent Canvases from the Production workspace`와 같은 테스트 프롬프트를 보내보세요.

## 로컬 베타 서버에서 마이그레이션하기 {#migrating-from-the-local-beta-server}

마이그레이션 중에는 로컬 베타 서버와 원격 호스팅 서버를 동시에 실행할 수 있습니다. 에이전트에 어느 서버를 사용할지 명시적으로 지정해야 할 수 있습니다.

원격 호스팅 서버에는 로컬 베타 서버에 없는 새로운 도구가 포함되어 있습니다. 로컬 서버용으로 스킬을 구축한 경우, 새로운 도구 이름과 동작을 참조하도록 해당 스킬을 업데이트해야 할 수 있습니다.

워크플로와 스킬이 원격 서버에서 정상적으로 작동하는 것을 확인한 후, 로컬 호스팅 서버를 비활성화하세요.

## 문제 해결 {#troubleshooting}

### 지원되는 클라이언트에서 인증이 실패하는 경우 {#authentication-fails-in-a-supported-client}

1. 회사 관리자가 [OAuth 설정]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)에서 **MCP OAuth access**를 활성화했는지 확인합니다.
2. 사용자에게 "Use MCP Server" 권한이 있는지 확인합니다.
3. 로그인 및 인증을 다시 시도합니다.

### 검증되지 않은 클라이언트에서 인증이 차단되는 경우 {#authentication-is-blocked-in-an-unverified-client}

Braze는 보안을 위해 지원되는 클라이언트 도메인의 허용 목록을 관리합니다. 허용 목록에 없는 클라이언트에서 연결하면 인증이 차단될 수 있습니다. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="support for your MCP client" %}

Claude Code 및 OpenAI Codex처럼 커스텀 스킴 없이 로컬 머신에서 실행되는 클라이언트도 정상적으로 작동합니다.

### 클라이언트에 도구가 표시되지 않는 경우 {#tools-dont-appear-in-your-client}

에이전트가 Braze 도구를 목록으로 불러올 수 없다면, 몇 분 정도 기다린 후 다시 시도하세요. 이러한 문제는 대부분 일시적이며 자동으로 해결됩니다.

### 에이전트가 예상 도구에 접근할 수 없는 경우 {#agent-cannot-access-expected-tools}

1. 대시보드 사용자에게 필요한 권한이 있는지 확인합니다. 에이전트는 사용자 본인의 대시보드 접근 권한에 맞는 도구만 사용할 수 있습니다.
2. 프롬프트에서 예상 워크스페이스를 선택했는지 확인합니다.
3. 에이전트에게 `get_workspaces`를 호출하도록 요청하고 사용 가능한 워크스페이스 ID를 확인합니다.

### 에이전트가 잘못된 워크스페이스를 사용하는 경우 {#agent-uses-the-wrong-workspace}

계정이 둘 이상의 워크스페이스에 접근할 수 있는 경우, Braze 대시보드에 표시되는 정확한 이름을 사용하여 프롬프트에 워크스페이스를 지정하세요. 워크스페이스를 지정하지 않으면, 에이전트가 확인을 요청하거나 예상과 다른 워크스페이스를 사용할 수 있습니다.

{% alert important %}
에이전트가 작업을 시작하기 전에, 항상 어떤 워크스페이스를 사용하고 있는지 확인하세요. 경우에 따라 에이전트가 의도한 것과 다른 워크스페이스를 선택할 수 있습니다.
{% endalert %}

### 다른 회사로 전환하기 {#switching-to-a-different-company}

회사는 처음 인증할 때 설정됩니다. 동일한 클러스터에서 다른 회사로 작업하려면, 클라이언트에서 Braze 커넥터를 연결 해제하고 다시 인증한 다음, 로그인 중에 다른 회사를 선택하세요.

{% multi_lang_include mcp_server/legal_disclaimer.md %}