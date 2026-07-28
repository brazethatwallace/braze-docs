# O servidor MCP da Braze {#the-braze-mcp-server}

> Saiba mais sobre o servidor MCP da Braze, uma conexão remota segura que permite que ferramentas de IA como Claude e Cursor acessem dados da Braze que não são IPI para responder perguntas, analisar tendências, fornecer insights e criar conteúdo.

{% alert important %}
O servidor MCP remoto está em acesso antecipado. Entre em contato com seu gerente de conta para solicitar acesso.
{% endalert %}

## O que é o Model Context Protocol (MCP)? {#what-is-model-context-protocol-mcp}

​​O Model Context Protocol, ou MCP, é um padrão que permite que agentes de IA se conectem e trabalhem com dados de outra plataforma. Ele tem duas partes principais:

- **Cliente MCP:** O aplicativo onde o agente de IA é executado, como Cursor ou Claude.
- **Servidor MCP:** Um serviço fornecido por outra plataforma, como a Braze, que define quais ferramentas a IA pode usar e quais dados ela pode acessar.

## Sobre o servidor MCP da Braze {#about-the-braze-mcp-server}

Após [configurar o servidor MCP da Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, você pode conectar ferramentas de IA como agentes, assistentes e chatbots diretamente à Braze, permitindo que eles leiam dados agregados, como análises de Canvas e Campaign, atributos personalizados, segmentos e mais. O servidor MCP da Braze é ótimo para:

- Construir ferramentas impulsionadas por IA que precisam de contexto da Braze.
- Engenheiros de CRM criando fluxos de trabalho de agentes em várias etapas.
- Profissionais de marketing técnico experimentando consultas em linguagem natural.

O servidor MCP da Braze inclui ferramentas de leitura e escrita. Essas ferramentas não retornam dados dos perfis de usuários da Braze. Seus agentes herdam as permissões do seu usuário no dashboard da Braze. Para a lista completa de ferramentas disponíveis, veja [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Ferramentas que expõem IPI em nível de usuário não estão disponíveis.
{% endalert %}

Use o servidor MCP para fazer perguntas sobre o desempenho de Campaigns e Canvas, explorar seus Segments e atributos personalizados, gerar relatórios e criar conteúdo como modelos de e-mail, Content Blocks e ativos da biblioteca de mídia por meio de linguagem natural.

## O servidor MCP beta foi descontinuado? {#is-the-beta-mcp-server-deprecated}

Sim. O servidor MCP hospedado localmente, lançado em agosto de 2025, foi descontinuado e não receberá atualizações adicionais. Você pode continuar usando-o, mas a Braze recomenda migrar para a versão hospedada remotamente.

### Como o servidor remoto é diferente? {#how-is-the-remote-server-different}

O servidor MCP anterior da Braze era executado localmente na sua máquina. Você precisava instalar um pacote, gerenciar um arquivo de configuração e criar uma chave de API da Braze com as permissões corretas. O servidor MCP remoto elimina essa configuração local.

Conecte-se a partir de um cliente MCP compatível em menos de um minuto. A autenticação usa OAuth. O acesso está vinculado à sua conta de usuário no dashboard da Braze, não a uma chave de API compartilhada, então o que um agente pode ver e fazer reflete suas permissões no dashboard. Se um usuário do dashboard perder o acesso na Braze, o cliente também perde o acesso.

As principais diferenças são:

- **Configuração:** Cole uma URL da Braze em vez de instalar um pacote e editar arquivos de configuração.
- **Autenticação:** Faça login com sua conta da Braze em vez de criar uma chave de API.
- **Permissões:** O acesso é baseado na sua conta de usuário do dashboard em vez de permissões de chave de API.
- **Direcionamento de espaço de trabalho:** O contexto do espaço de trabalho é passado por requisição em vez de ser fixado na configuração local.

## Perguntas frequentes (FAQ) {#faq}

### Quais clientes MCP são suportados? {#which-mcp-clients-are-supported}

Qualquer cliente MCP que suporte servidores MCP remotos com OAuth pode funcionar. A Braze verificou:

- Claude por meio de conectores personalizados
- ChatGPT por meio de conectores personalizados
- Cursor
- OpenAI Codex
- Claude Code

### Quais dados da Braze meu cliente MCP pode acessar? {#what-braze-data-can-my-mcp-client-access}

Os clientes MCP podem acessar ferramentas que não retornam IPI em nível de usuário.

### Meu cliente MCP pode alterar dados da Braze? {#can-my-mcp-client-change-braze-data}

Sim, se o seu usuário do dashboard tiver essas permissões.

### Ainda preciso de uma chave de API da Braze? {#do-i-still-need-a-braze-api-key}

Não para o MCP. As chaves de API ainda funcionam para a REST API e não estão sendo descontinuadas.

### Quais regiões são suportadas? {#which-regions-are-supported}

Ambos os clusters da Braze são suportados. Dois endpoints estão disponíveis hoje:

- `https://mcp.braze.com/mcp` (EUA)
- `https://mcp.braze.eu/mcp` (UE)

Qualquer um dos endpoints pode alcançar qualquer cluster da Braze.

### Posso usar o servidor MCP remoto da Braze com ferramentas além da lista verificada? {#can-i-use-the-braze-remote-mcp-server-with-tools-other-than-the-verified-list}

Você pode tentar, mas a autenticação pode ser bloqueada. A Braze atualmente mantém uma lista de domínios permitidos por segurança. Se sua ferramenta não estiver na lista e você encontrar problemas de autenticação, entre em contato com [mcp-product@braze.com](mailto:mcp-product@braze.com).

### O servidor remoto suporta múltiplos espaços de trabalho? {#does-the-remote-server-support-multiple-workspaces}

Sim. Especifique o espaço de trabalho por conversa ou por requisição. Uma conexão cobre todos os espaços de trabalho aos quais você tem acesso autorizado.

### Meu agente pode acessar IPI em nível de usuário? {#can-my-agent-access-user-level-pii}

Não. Atualmente, ferramentas que expõem IPI não estão disponíveis.

### O que acontece quando minhas permissões mudam? {#what-happens-when-my-permissions-change}

O acesso do agente muda junto com o usuário do dashboard. Alterações de permissão são aplicadas na próxima requisição. Usuários do dashboard desativados perdem o acesso ao MCP.

### Por que não vejo o conector da Braze no diretório do meu cliente? {#why-do-i-not-see-the-braze-connector-in-my-clients-directory}

As listagens de diretório são disponibilizadas após o início do acesso antecipado. Você sempre pode se conectar manualmente usando a URL do MCP da Braze.

### Minha empresa usa lista de IPs permitidos. Podemos usar o servidor MCP remoto? {#my-company-uses-ip-allowlisting-can-we-use-the-remote-mcp-server}

Não no momento. Clientes que usam [lista de IPs permitidos](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#dashboard-ip-allowlisting) não podem participar do programa de acesso antecipado.

{% multi_lang_include mcp_server/legal_disclaimer.md %}