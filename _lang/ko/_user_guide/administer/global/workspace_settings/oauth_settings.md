---
nav_title: OAuth 및 MCP 액세스
article_title: 워크스페이스의 OAuth 및 MCP 액세스
page_order: 10
page_type: reference
description: "워크스페이스별로 제어할 수 있는 OAuth 및 MCP 액세스와 관리자 설정에서 회사 전체에 적용되는 항목에 대해 알아보세요."
---

# 워크스페이스의 OAuth 및 MCP 액세스 {#oauth-and-mcp-access-in-a-workspace}

> 회사 전체 OAuth 정책은 [관리자 설정]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)에서 구성합니다. 워크스페이스에서는 개별 사용자에게 MCP 서버 사용 권한을 부여할 수 있습니다.

특정 워크스페이스에 대해서만 MCP OAuth 액세스를 켜거나 끌 수는 없습니다.

## 회사 전체 설정과 워크스페이스별 설정 비교 {#whats-company-wide-versus-per-workspace}

| 제어 항목 | 회사 전체 | 워크스페이스별 |
| --- | --- | --- |
| **MCP OAuth 액세스** | 예. 이 토글은 **설정** > **관리자 설정** > **OAuth**의 **글로벌 액세스 제어** 아래에 있습니다. | 아니요. 워크스페이스 관리자가 회사 설정을 재정의할 수 없습니다. |
| "MCP 서버 사용" 권한 | 아니요. | 예. 사용자가 MCP 서버를 통해 액세스해야 하는 각 워크스페이스에 대해 이 권한을 부여합니다. |
| MCP에 미러링되는 대시보드 권한 | 아니요. | 예. MCP 클라이언트는 해당 워크스페이스에서 사용자가 이미 액세스할 수 있는 Braze 기능만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="회사 전체와 워크스페이스별 OAuth 제어 비교" }

## 회사에서 MCP OAuth 액세스가 꺼져 있는 경우 {#if-mcp-oauth-access-is-off-for-the-company}

**관리자 설정**에서 **MCP OAuth 액세스**가 꺼져 있으면, Braze는 모든 워크스페이스에 대해 MCP OAuth를 거부합니다. "MCP 서버 사용" 권한이 있는 사용자도 연결할 수 없으며, 워크스페이스 수준에서 MCP OAuth 액세스를 다시 켤 수 있는 설정은 없습니다.

연결을 시도하는 사용자에게는 회사에 대해 원격 MCP 액세스가 활성화되지 않았다는 메시지가 표시될 수 있습니다. 회사 관리자는 **설정** > **관리자 설정** > **OAuth**에서 **MCP OAuth 액세스**를 켤 수 있습니다.

회사 수준의 MCP OAuth 액세스 및 해당 설정을 변경할 수 있는 사용자에 대한 자세한 내용은 [OAuth 설정 관리]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)를 참조하세요.