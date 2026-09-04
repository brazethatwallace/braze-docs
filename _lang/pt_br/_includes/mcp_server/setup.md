# Configurando o servidor Braze MCP {#setting-up-the-braze-mcp-server}

> Aprenda como se conectar ao servidor remoto Braze MCP, autenticar com OAuth e começar a usar as ferramentas da Braze a partir do seu cliente MCP. Para saber mais, consulte [servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos {#prerequisites}

Antes de começar, verifique se você tem o seguinte:

| Pré-requisito | Descrição |
|--------------|-------------|
| Cliente MCP compatível | Qualquer cliente que suporte servidores MCP remotos com OAuth pode funcionar. A Braze verificou Claude, ChatGPT, Cursor, OpenAI Codex, Claude Code e Visual Studio Code. |
| Conta no dashboard da Braze | Você faz login com suas credenciais normais da Braze, incluindo SSO ou SAML se sua empresa utilizar. Não há um login separado para o MCP. |
| Seleção do endpoint do servidor | Escolha `https://mcp.braze.com/mcp` (EUA) ou `https://mcp.braze.eu/mcp` (UE). Qualquer um dos endpoints pode acessar qualquer cluster da Braze. |
| Sem lista de permissões de IP | Clientes que usam a [lista de permissões de IP](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) não podem usar o servidor Braze MCP no momento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert note %}
O acesso do seu agente reflete suas permissões no dashboard. Se o seu acesso ao dashboard estiver limitado a uma equipe em vez de um espaço de trabalho completo, algumas ferramentas podem não funcionar.
{% endalert %}

## Gerenciando o acesso (para administradores) {#managing-access-for-admins}

{% alert note %}
Antes que os usuários possam se conectar, um administrador da empresa deve ativar o **Acesso OAuth ao MCP** em **Configurações** > **Configurações de administrador** > **OAuth**. Para saber mais, consulte [Gerenciar configurações OAuth]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin).
{% endalert %}

### Conceder acesso {#grant-access}

Os administradores controlam o acesso ao servidor MCP por meio da permissão "Use MCP Server". Por padrão, os usuários não possuem essa permissão, e ela deve ser concedida explicitamente.

### Revogar acesso {#revoke-access}

Para revogar o acesso, remova a permissão "Use MCP Server" do usuário. Remover permissões do dashboard de um usuário também remove essas capacidades de qualquer agente conectado na próxima solicitação.

### Auditar uso {#audit-usage}

Quando um usuário se conecta com sucesso por meio do OAuth, um evento é registrado no [relatório de eventos de segurança](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#security-event-report).

## Conecte seu cliente {#connect-your-client}

### Etapa 1: Confirme as permissões e o acesso ao espaço de trabalho {#step-1-confirm-permissions-and-workspace-access}

1. Você ou o administrador da sua empresa precisam confirmar que você tem a permissão "Use MCP Server".
2. Se você precisa acessar vários espaços de trabalho, verifique se a permissão está ativada para todos os espaços de trabalho relevantes.

### Etapa 2: Adicione a Braze como um conector MCP remoto {#step-2-add-braze-as-a-remote-mcp-connector}

No seu cliente MCP, adicione um novo servidor remoto ou conector personalizado e insira a URL do MCP da Braze. Por exemplo, no Claude, você pode acessar **Settings** > **Connectors** > **Add custom connector** e colar a URL.

Não é necessário informar ID de cliente, segredo de cliente ou chave de API. Seu cliente se registra automaticamente na Braze.

Opções de endpoint do MCP da Braze:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

{% alert tip %}
Clientes da UE devem usar o endpoint da UE. Clientes fora da UE podem usar qualquer um dos endpoints.
{% endalert %}

Guias de configuração de clientes:

- [Claude](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code](https://code.claude.com/docs/en/mcp-quickstart)
- [ChatGPT](https://developers.openai.com/api/docs/guides/developer-mode)
- [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
- [OpenAI Codex](https://developers.openai.com/codex/mcp)
- [Visual Studio Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)

### Etapa 3: Faça login na Braze via OAuth {#step-3-sign-in-to-braze-through-oauth}

Na primeira vez que seu agente chamar uma ferramenta da Braze, seu cliente abrirá uma janela do navegador e direcionará você para a Braze para fazer login.

1. Faça login na Braze como faria normalmente, incluindo SSO, se necessário.
2. Se o seu login pode acessar mais de uma empresa no mesmo cluster, selecione a empresa que deseja usar.
3. Na tela de consentimento, revise o acesso que o aplicativo está solicitando.
4. Marque a caixa de confirmação para concordar com a Política de Privacidade da Braze e selecione **Continue** para retornar ao seu cliente MCP.

![Tela de consentimento da Braze mostrando que o Claude Desktop está solicitando acesso às informações da conta Braze e acesso amplo aos dados da Braze, com uma caixa de confirmação da Política de Privacidade e os botões Cancel e Continue.]({% image_buster /assets/img/mcp_server/oauth_consent_screen.png %}){: width="639" height="1024" style="max-width:65%;"}

Sua sessão utiliza tokens de acesso de curta duração que são atualizados automaticamente. Ocasionalmente, pode ser necessário fazer login novamente.

### Etapa 4: Informe ao seu agente qual espaço de trabalho usar {#step-4-tell-your-agent-which-workspace-to-use}

Se a sua conta pode acessar mais de um espaço de trabalho, especifique o espaço de trabalho no seu prompt. Por exemplo:

- `I'd like to look at campaign analytics for the past week in the Production workspace.`
- `Can you compare this week's analytics between my prod-1 workspace and my prod-2 workspace?`

Se você não especificar um espaço de trabalho, seu agente pode pedir que você esclareça.

### Etapa 5: Envie um prompt de teste {#step-5-send-a-test-prompt}

Após a configuração, envie um prompt rápido de validação, como:

- `List the Braze tools available in this workspace.`
- `Show my recent Canvases from the Production workspace.`

Para saber mais, consulte [Usando o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

## Exemplo: Conectar com o Claude {#example-connect-with-claude}

Conectar um cliente leva apenas algumas etapas. O passo a passo a seguir usa o Claude, mas o fluxo é semelhante para outros clientes compatíveis.

1. No Claude, acesse **Settings** > **Connectors** > **Add custom connector**.
2. Insira um nome, como `Braze`, e cole a URL do Braze MCP: `https://mcp.braze.com/mcp` para US ou `https://mcp.braze.eu/mcp` para EU. Você não precisa de um client ID, client secret ou chave de API.
3. Selecione **Add** para salvar o conector. O Claude se registra na Braze automaticamente.
4. Selecione **Connect** para iniciar a autenticação. O Claude abre uma janela do navegador e direciona você para a Braze para fazer login.
5. Faça login na Braze com suas credenciais habituais, incluindo SSO se a sua empresa utiliza. Se o seu login pode acessar mais de uma empresa no mesmo cluster, selecione a empresa que você deseja usar.
6. Na tela de consentimento, revise o acesso solicitado, marque a caixa de confirmação e selecione **Continue**. O Claude retorna ao seu chat, e seu agente agora pode usar as ferramentas da Braze.

Para confirmar a conexão, envie um prompt de teste como `Show my recent Canvases from the Production workspace`.

## Migrando do servidor beta local {#migrating-from-the-local-beta-server}

Você pode executar o servidor beta local e o servidor hospedado remotamente lado a lado durante a migração. Talvez seja necessário informar explicitamente ao seu agente qual deles usar.

O servidor hospedado remotamente inclui novas ferramentas que não existem no servidor beta local. Se você criou skills para o servidor local, talvez seja necessário atualizar essas skills para referenciar novos nomes e comportamentos de ferramentas.

Depois de confirmar que seus fluxos de trabalho e skills estão funcionando no servidor remoto, desative o servidor hospedado localmente.

## Solução de problemas {#troubleshooting}

### A autenticação falha em um cliente suportado {#authentication-fails-in-a-supported-client}

1. Confirme que o administrador da sua empresa ativou o **acesso OAuth ao MCP** nas [configurações de OAuth]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin).
2. Confirme que o seu usuário tem a permissão "Use MCP Server".
3. Tente novamente o login e a autorização.

### A autenticação está bloqueada em um cliente não verificado {#authentication-is-blocked-in-an-unverified-client}

A Braze mantém uma lista de domínios de clientes suportados para segurança. Se você se conectar a partir de um cliente que não está na lista, a autenticação pode ser bloqueada. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="support for your MCP client" %}

Clientes que são executados localmente na sua máquina sem um esquema personalizado, como Claude Code e OpenAI Codex, também devem funcionar.

### As ferramentas não aparecem no seu cliente {#tools-dont-appear-in-your-client}

Se o seu agente não conseguir listar as ferramentas da Braze, aguarde alguns minutos e tente novamente. Esses problemas geralmente são temporários e se resolvem sozinhos.

### O agente não consegue acessar as ferramentas esperadas {#agent-cannot-access-expected-tools}

1. Confirme que o seu usuário do dashboard possui as permissões necessárias. O seu agente só pode usar ferramentas que correspondam ao seu próprio acesso no dashboard.
2. Confirme que você selecionou o espaço de trabalho esperado no seu prompt.
3. Peça ao seu agente para chamar `get_workspaces` e verifique os IDs de espaço de trabalho disponíveis.

### O agente usa o espaço de trabalho errado {#agent-uses-the-wrong-workspace}

Se a sua conta pode acessar mais de um espaço de trabalho, nomeie o espaço de trabalho no seu prompt usando o nome exato mostrado no dashboard da Braze. Se você não especificar um espaço de trabalho, o seu agente pode pedir esclarecimentos ou usar um inesperado.

{% alert important %}
Antes de o seu agente começar a trabalhar, sempre confirme qual espaço de trabalho ele está usando. Em alguns casos, um agente pode selecionar um espaço de trabalho diferente daquele que você pretendia.
{% endalert %}

### Mudando para uma empresa diferente {#switching-to-a-different-company}

A sua empresa é definida quando você autoriza pela primeira vez. Para trabalhar em uma empresa diferente no mesmo cluster, desconecte o conector da Braze no seu cliente, autorize novamente e selecione a outra empresa durante o login.

{% multi_lang_include mcp_server/legal_disclaimer.md %}