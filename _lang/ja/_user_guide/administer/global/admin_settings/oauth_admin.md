---
nav_title: OAuth設定
article_title: OAuth設定の管理
page_order: 4
page_type: reference
description: "Braze MCPサーバーのMCP OAuthアクセスを管理する方法を説明します。"
---

# OAuth設定の管理 {#manage-oauth-settings}

> OAuth設定は、[Braze MCPサーバー]({{site.baseurl}}/user_guide/brazeai/mcp_server)への会社全体のアクセスを管理します。

OAuth設定は会社全体に適用されます。各ユーザーに割り当てられた権限により、MCPサーバーを通じてアクセスできるワークスペースと機能が決まります。

## 要件 {#requirements}

| 要件 | 説明 |
| --- | --- |
| 「Admin」権限 | OAuth設定を表示したり、MCP OAuthアクセスのオン・オフを切り替えるには、会社レベルの「Admin」権限が必要です。 |
| 「Use MCP Server」権限 | ユーザーがMCPサーバーを通じてアクセスしたい各ワークスペースについて、この権限が必要です。この権限は、OAuth設定の管理に使用される「Admin」権限とは別のものです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="OAuth設定の管理に関する要件" }

権限の割り当てについて詳しくは、[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。

## OAuthアクセスの仕組み {#how-oauth-access-works}

OAuth設定とユーザー権限は連携して動作します。

- 会社全体のOAuth設定は、ユーザーがMCPクライアントをBrazeに接続できるかどうかを決定します。
- 「Use MCP Server」権限は、個々のユーザーがワークスペースでMCPサーバーを使用できるかどうかを決定します。
- ユーザーの既存のダッシュボード権限は、MCPクライアントがアクセスできるBrazeのデータと機能を決定します。
- 1つのOAuth接続は、ユーザーがアクセスを許可されているワークスペースにのみアクセスできます。

MCP OAuthアクセスをオンにしても、ユーザーに新しいワークスペース権限は付与されません。同様に、ダッシュボード権限を削除すると、そのユーザーの接続済みMCPクライアントからもその機能が削除されます。

## 会社とワークスペースのコントロール {#company-and-workspace-controls}

OAuthポリシーは会社レベルで保存されます。ワークスペース管理者は、単一のワークスペースに対して**MCP OAuthアクセス**を上書きすることはできません。

| コントロール | 設定場所 | スコープ |
| --- | --- | --- |
| **MCP OAuthアクセス** | **設定** > **管理者設定** > **OAuth** | 会社全体。これがオフの場合、すべてのワークスペースでMCP OAuthが拒否されます。 |
| 「Use MCP Server」権限 | **設定** > **ユーザー管理** | ワークスペースごと。ユーザーはMCPサーバーを通じてアクセスする各ワークスペースでこの権限が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="会社とワークスペースのOAuthコントロール" }

「Admin」権限を持つユーザーのみが**MCP OAuthアクセス**を変更できます。ワークスペース権限がこの会社設定とどのように連携するかについては、[OAuthとMCPアクセス]({{site.baseurl}}/user_guide/administer/global/workspace_settings/oauth_settings)を参照してください。

## MCP OAuthアクセスのオン・オフの切り替え {#turn-mcp-oauth-access-on-or-off}

会社のMCP OAuthアクセスを更新するには、次の手順に従います。

1. **設定** > **管理者設定** > **OAuth**に移動します。
2. **グローバルアクセスコントロール**で、**MCP OAuthアクセス**をオンまたはオフにします。

**MCP OAuthアクセス**がオンの場合、「Use MCP Server」権限を持つユーザーは、承認済みのMCPクライアントを認可できます。

オフの場合、会社内のすべてのユーザーとワークスペースに対して、MCPサーバーへのOAuthアクセスが拒否されます。既存のMCP接続は、次回OAuthアクセストークンを使用またはリフレッシュする際に動作を停止します。

Brazeがお客様の環境でリモートMCPサーバーをオフにしている場合、**MCP OAuthアクセス**のトグルは無効になり、リモートMCPサーバーが再度オンになるまで会社設定は効果がないことを説明するメッセージが表示されます。

## OAuthアクティビティの監査 {#audit-oauth-activity}

Brazeは、MCPサーバーへのOAuth接続を[セキュリティイベントレポート]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report)に記録します。このレポートを使用して、ユーザーがOAuthを通じて接続した日時を監査できます。

特定のユーザーのMCPアクセスを取り消すには、そのユーザーから「Use MCP Server」権限を削除します。設定とトラブルシューティングのガイダンスについては、[Braze MCPサーバーの設定]({{site.baseurl}}/user_guide/brazeai/mcp_server/setup)を参照してください。