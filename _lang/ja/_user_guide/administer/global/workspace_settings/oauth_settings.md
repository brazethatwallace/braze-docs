---
nav_title: OAuthとMCPアクセス
article_title: ワークスペースでのOAuthとMCPアクセス
page_order: 10
page_type: reference
description: "ワークスペースごとに制御できるOAuthとMCPアクセスの範囲、および管理者設定で会社全体に適用される項目について説明します。"
---

# ワークスペースでのOAuthとMCPアクセス {#oauth-and-mcp-access-in-a-workspace}

> 会社全体のOAuthポリシーは[管理者設定]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)で構成します。ワークスペースでは、個々のユーザーにMCPサーバーを使用する権限を付与します。

1つのワークスペースに対してMCP OAuthアクセスをオンまたはオフにすることはできません。

## 会社全体とワークスペース単位の違い {#whats-company-wide-versus-per-workspace}

| コントロール | 会社全体 | ワークスペース単位 |
| --- | --- | --- |
| **MCP OAuthアクセス** | はい。このトグルは**設定** > **管理者設定** > **OAuth**の**グローバルアクセスコントロール**にあります。 | いいえ。ワークスペース管理者は会社の設定をオーバーライドできません。 |
| 「Use MCP Server」権限 | いいえ。 | はい。MCPサーバーを通じてアクセスする必要がある各ワークスペースに対して、この権限を付与します。 |
| MCPに反映されるダッシュボード権限 | いいえ。 | はい。MCPクライアントは、そのワークスペースでユーザーがすでにアクセスできるBraze機能のみを使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="会社全体とワークスペース単位のOAuthコントロール" }

## 会社全体でMCP OAuthアクセスがオフの場合 {#if-mcp-oauth-access-is-off-for-the-company}

**管理者設定**で**MCP OAuthアクセス**がオフの場合、Brazeはすべてのワークスペースに対してMCP OAuthを拒否します。「Use MCP Server」権限を持つユーザーであっても接続できず、MCP OAuthアクセスを再度オンにするワークスペースレベルの設定もありません。

接続しようとしたユーザーには、会社でリモートMCPアクセスがオンになっていないというメッセージが表示される場合があります。会社管理者は、**設定** > **管理者設定** > **OAuth**で**MCP OAuthアクセス**をオンにできます。

会社レベルのMCP OAuthアクセスとその設定を変更できるユーザーについては、[OAuth設定の管理]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin)を参照してください。