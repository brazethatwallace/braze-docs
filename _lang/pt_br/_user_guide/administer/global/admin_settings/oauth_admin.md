---
nav_title: Configurações OAuth
article_title: Gerenciar configurações OAuth
page_order: 4
page_type: reference
description: "Saiba como gerenciar o acesso OAuth MCP para o servidor MCP da Braze."
---

# Gerenciar configurações OAuth {#manage-oauth-settings}

> As configurações OAuth gerenciam o acesso de toda a empresa ao [servidor MCP da Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server).

As configurações OAuth se aplicam a toda a sua empresa. As permissões atribuídas a cada usuário determinam quais espaços de trabalho e recursos eles podem acessar por meio do servidor MCP.

## Requisitos {#requirements}

| Requisito | Descrição |
| --- | --- |
| Permissão "Admin" | Você precisa ter a permissão "Admin" no nível da empresa para visualizar as configurações OAuth ou ativar/desativar o acesso OAuth MCP. |
| Permissão "Use MCP Server" | Os usuários precisam ter essa permissão para cada espaço de trabalho que desejam acessar por meio do servidor MCP. Essa permissão é separada da permissão "Admin" usada para gerenciar as configurações OAuth. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos para gerenciar configurações OAuth" }

Para saber mais sobre atribuição de permissões, consulte [Permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Como o acesso OAuth funciona {#how-oauth-access-works}

As configurações OAuth e as permissões de usuário funcionam em conjunto:

- As configurações OAuth de toda a empresa determinam se os usuários podem conectar clientes MCP à Braze.
- A permissão "Use MCP Server" determina se um usuário individual pode usar o servidor MCP em um espaço de trabalho.
- As permissões existentes do usuário no dashboard determinam quais dados e recursos da Braze um cliente MCP pode acessar.
- Uma conexão OAuth pode acessar apenas os espaços de trabalho que o usuário está autorizado a acessar.

Ativar o acesso OAuth MCP não concede aos usuários novas permissões de espaço de trabalho. Da mesma forma, remover uma permissão do dashboard remove essa capacidade do cliente MCP conectado do usuário.

## Controles de empresa e espaço de trabalho {#company-and-workspace-controls}

A política OAuth é armazenada no nível da empresa. Administradores de espaço de trabalho não podem substituir o **acesso OAuth MCP** para um único espaço de trabalho.

| Controle | Onde configurar | Escopo |
| --- | --- | --- |
| **Acesso OAuth MCP** | **Configurações** > **Configurações de administrador** > **OAuth** | Toda a empresa. Quando desativado, o OAuth MCP é negado em todos os espaços de trabalho. |
| Permissão "Use MCP Server" | **Configurações** > **Gerenciamento de usuários** | Por espaço de trabalho. Os usuários precisam dessa permissão em cada espaço de trabalho que acessam por meio do servidor MCP. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Controles OAuth de empresa e espaço de trabalho" }

Apenas usuários com a permissão "Admin" podem alterar o **acesso OAuth MCP**. Para entender como as permissões de espaço de trabalho interagem com essa configuração da empresa, consulte [OAuth e acesso MCP]({{site.baseurl}}/user_guide/administer/global/workspace_settings/oauth_settings).

## Ativar ou desativar o acesso OAuth MCP {#turn-mcp-oauth-access-on-or-off}

Para atualizar o acesso OAuth MCP da sua empresa:

1. Acesse **Configurações** > **Configurações de administrador** > **OAuth**.
2. Em **Controles de acesso global**, ative ou desative o **acesso OAuth MCP**.

Quando o **acesso OAuth MCP** está ativado, os usuários com a permissão "Use MCP Server" podem autorizar clientes MCP aprovados.

Quando está desativado, o acesso OAuth ao servidor MCP é negado para todos os usuários e espaços de trabalho da sua empresa. As conexões MCP existentes param de funcionar na próxima vez que usarem ou atualizarem seu token de acesso OAuth.

Se a Braze desativou o servidor MCP remoto para o seu ambiente, o botão de alternância **acesso OAuth MCP** fica desabilitado e uma mensagem explica que a configuração da empresa não tem efeito até que o servidor MCP remoto seja ativado novamente.

## Auditar a atividade OAuth {#audit-oauth-activity}

A Braze registra as conexões OAuth ao servidor MCP no [relatório de eventos de segurança]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report). Use esse relatório para auditar quando os usuários se conectam por meio do OAuth.

Para revogar o acesso MCP de um usuário, remova a permissão "Use MCP Server" desse usuário. Para orientações sobre configuração e solução de problemas, consulte [Configurar o servidor MCP da Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server/setup).