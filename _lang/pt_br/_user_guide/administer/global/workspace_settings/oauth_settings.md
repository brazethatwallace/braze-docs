---
nav_title: Acesso OAuth e MCP
article_title: Acesso OAuth e MCP em um espaço de trabalho
page_order: 10
page_type: reference
description: "Saiba quais controles de acesso OAuth e MCP podem ser gerenciados por espaço de trabalho e quais permanecem em nível de empresa nas configurações de administrador."
---

# Acesso OAuth e MCP em um espaço de trabalho {#oauth-and-mcp-access-in-a-workspace}

> A política OAuth em nível de empresa é configurada nas [Configurações de administrador]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin). Em um espaço de trabalho, você concede a usuários individuais a permissão para usar o servidor MCP.

Não é possível ativar ou desativar o acesso OAuth do MCP para um único espaço de trabalho.

## O que é em nível de empresa versus por espaço de trabalho {#whats-company-wide-versus-per-workspace}

| Controle | Em nível de empresa | Por espaço de trabalho |
| --- | --- | --- |
| **Acesso OAuth do MCP** | Sim. Essa opção está em **Configurações** > **Configurações de administrador** > **OAuth**, na seção **Controles de acesso global**. | Não. Administradores do espaço de trabalho não podem substituir a configuração da empresa. |
| Permissão "Use MCP Server" | Não. | Sim. Conceda essa permissão para cada espaço de trabalho ao qual o usuário deve ter acesso por meio do servidor MCP. |
| Permissões do dashboard espelhadas pelo MCP | Não. | Sim. O cliente MCP pode usar apenas os recursos da Braze que o usuário já pode acessar naquele espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Controles OAuth em nível de empresa versus por espaço de trabalho" }

## Se o acesso OAuth do MCP estiver desativado para a empresa {#if-mcp-oauth-access-is-off-for-the-company}

Quando o **Acesso OAuth do MCP** está desativado em **Configurações de administrador**, a Braze nega o OAuth do MCP para todos os espaços de trabalho. Usuários com a permissão "Use MCP Server" ainda não conseguem se conectar, e não há nenhuma configuração em nível de espaço de trabalho para reativar o acesso OAuth do MCP.

Usuários que tentarem se conectar podem ver uma mensagem informando que o acesso remoto ao MCP não foi ativado para a empresa. Um administrador da empresa pode ativar o **Acesso OAuth do MCP** em **Configurações** > **Configurações de administrador** > **OAuth**.

Para saber mais sobre o acesso OAuth do MCP em nível de empresa e quem pode alterar essa configuração, consulte [Gerenciar configurações OAuth]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin).