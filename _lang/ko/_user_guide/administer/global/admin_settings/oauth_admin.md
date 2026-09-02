---
nav_title: OAuth 설정
article_title: OAuth 설정 관리
page_order: 4
page_type: reference
description: "Braze MCP 서버에 대한 MCP OAuth 액세스를 관리하는 방법을 알아보세요."
---

# OAuth 설정 관리 {#manage-oauth-settings}

> OAuth 설정은 [Braze MCP 서버]({{site.baseurl}}/user_guide/brazeai/mcp_server)에 대한 회사 전체 액세스를 관리합니다.

OAuth 설정은 전체 회사에 적용됩니다. 각 사용자에게 할당된 권한에 따라 MCP 서버를 통해 액세스할 수 있는 워크스페이스와 기능이 결정됩니다.

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| --- | --- |
| "Admin" 권한 | OAuth 설정을 보거나 MCP OAuth 액세스를 켜거나 끄려면 회사 수준의 "Admin" 권한이 있어야 합니다. |
| "Use MCP Server" 권한 | 사용자는 MCP 서버를 통해 액세스하려는 각 워크스페이스에 대해 이 권한이 있어야 합니다. 이 권한은 OAuth 설정을 관리하는 데 사용되는 "Admin" 권한과 별개입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="OAuth 설정 관리를 위한 요구 사항" }

권한 할당에 대한 자세한 내용은 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 참조하세요.

## OAuth 액세스 작동 방식 {#how-oauth-access-works}

OAuth 설정과 사용자 권한은 함께 작동합니다.

- 회사 전체 OAuth 설정은 사용자가 MCP 클라이언트를 Braze에 연결할 수 있는지 여부를 결정합니다.
- "Use MCP Server" 권한은 개별 사용자가 워크스페이스에서 MCP 서버를 사용할 수 있는지 여부를 결정합니다.
- 사용자의 기존 대시보드 권한에 따라 MCP 클라이언트가 액세스할 수 있는 Braze 데이터와 기능이 결정됩니다.
- 하나의 OAuth 연결은 사용자가 액세스 권한을 가진 워크스페이스에만 액세스할 수 있습니다.

MCP OAuth 액세스를 켜도 사용자에게 새로운 워크스페이스 권한이 부여되지 않습니다. 마찬가지로, 대시보드 권한을 제거하면 해당 사용자의 연결된 MCP 클라이언트에서도 해당 기능이 제거됩니다.

## 회사 및 워크스페이스 제어 {#company-and-workspace-controls}

OAuth 정책은 회사 수준에서 저장됩니다. 워크스페이스 관리자는 단일 워크스페이스에 대해 **MCP OAuth 액세스**를 재정의할 수 없습니다.

| 제어 | 설정 위치 | 범위 |
| --- | --- | --- |
| **MCP OAuth 액세스** | **설정** > **관리자 설정** > **OAuth** | 전체 회사. 이 옵션이 꺼져 있으면 모든 워크스페이스에서 MCP OAuth가 거부됩니다. |
| "Use MCP Server" 권한 | **설정** > **사용자 관리** | 워크스페이스별. 사용자는 MCP 서버를 통해 액세스하는 각 워크스페이스에서 이 권한이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="회사 및 워크스페이스 OAuth 제어" }

"Admin" 권한이 있는 사용자만 **MCP OAuth 액세스**를 변경할 수 있습니다. 워크스페이스 권한이 이 회사 설정과 상호작용하는 방식에 대해서는 [OAuth 및 MCP 액세스]({{site.baseurl}}/user_guide/administer/global/workspace_settings/oauth_settings)를 참조하세요.

## MCP OAuth 액세스 켜기 또는 끄기 {#turn-mcp-oauth-access-on-or-off}

회사의 MCP OAuth 액세스를 업데이트하려면 다음과 같이 진행하세요.

1. **설정** > **관리자 설정** > **OAuth**로 이동합니다.
2. **글로벌 액세스 제어**에서 **MCP OAuth 액세스**를 켜거나 끕니다.

**MCP OAuth 액세스**가 켜져 있으면 "Use MCP Server" 권한이 있는 사용자가 승인된 MCP 클라이언트를 인증할 수 있습니다.

꺼져 있으면 회사의 모든 사용자와 워크스페이스에 대해 MCP 서버에 대한 OAuth 액세스가 거부됩니다. 기존 MCP 연결은 다음에 OAuth 액세스 토큰을 사용하거나 갱신할 때 작동이 중지됩니다.

Braze가 해당 환경에서 원격 MCP 서버를 꺼놓은 경우, **MCP OAuth 액세스** 토글이 비활성화되고 원격 MCP 서버가 다시 켜질 때까지 회사 설정이 효과가 없다는 메시지가 표시됩니다.

## OAuth 활동 감사 {#audit-oauth-activity}

Braze는 MCP 서버에 대한 OAuth 연결을 [보안 이벤트 보고서]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report)에 기록합니다. 이 보고서를 사용하여 사용자가 OAuth를 통해 연결한 시기를 감사할 수 있습니다.

특정 사용자의 MCP 액세스를 취소하려면 해당 사용자에게서 "Use MCP Server" 권한을 제거하세요. 설정 및 문제 해결 안내는 [Braze MCP 서버 설정]({{site.baseurl}}/user_guide/brazeai/mcp_server/setup)을 참조하세요.