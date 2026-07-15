# O servidor MCP da Braze {#the-braze-mcp-server}

> Saiba mais sobre o servidor MCP da Braze, uma conexão segura que permite que ferramentas de IA como Claude e Cursor acessem dados da Braze que não são IPI para responder perguntas, analisar tendências e fornecer insights.

{% alert important %}
Neste verão, a Braze está lançando um servidor MCP remoto, hospedado pela Braze, em acesso antecipado. Ele substitui o servidor beta hospedado localmente (`braze-mcp-server` no [PyPI](https://pypi.org/project/braze-mcp-server/) e no diretório de extensões do Claude Desktop).<br><br>

**O que isso significa para você:**<br><br>

- O servidor hospedado localmente continuará funcionando, mas não é mais suportado. Não adicionaremos novos endpoints nem corrigiremos problemas no beta.
- Quando o servidor remoto estiver disponível em acesso antecipado, você precisará migrar para ele. O servidor remoto não requer instalação local, usa OAuth em vez de chaves de API estáticas e funciona com clientes MCP como Claude, Copilot, Gemini CLI, Codex e Cursor.
- Acompanhe esta página para saber sobre a disponibilidade do acesso antecipado ou entre em contato com a equipe da sua conta na Braze para manifestar interesse.
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

O servidor MCP da Braze inclui endpoints somente leitura e de escrita. Eles não retornam dados dos perfis de usuários da Braze. Você escolhe quais endpoints atribuir à sua chave de API da Braze, e essa escolha controla o que um agente pode ler, criar ou atualizar. Para a lista completa de endpoints disponíveis e suas permissões necessárias, veja [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

{% alert warning %}
Atribua apenas as permissões de chave de API que você deseja que seu agente tenha. Se você não quiser que seu agente faça alterações na Braze, deixe as permissões de escrita desativadas ao criar sua chave de API. Agentes podem tentar gravar dados por meio de qualquer permissão de escrita que você conceder.
{% endalert %}

## Exemplo de uso {#usage-example}

Você pode interagir com a Braze por meio de linguagem natural usando ferramentas como Claude ou Cursor. Para outros exemplos e melhores práticas, veja [Usando o servidor MCP da Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
**Exemplo de prompt:** `What are my available Braze functions?`
**Exemplo de resposta:** Usou `list_functions` e retornou as categorias de funções MCP disponíveis da Braze.
{% endtab %}

{% tab Cursor %}
**Exemplo de prompt:** `What are my available Braze functions?`
**Exemplo de resposta:** Consultou `list_functions` e listou funções como `get_canvas_list`.
{% endtab %}
{% endtabs %}

## Perguntas frequentes (FAQ) {#faq}

### Quais clientes MCP são suportados? {#which-mcp-clients-are-supported}

Apenas [Claude](https://claude.ai/) e [Cursor](https://cursor.com/) são oficialmente suportados. Você deve ter uma conta em um desses clientes para usar o servidor MCP da Braze.

### Quais dados da Braze meu cliente MCP pode acessar? {#what-braze-data-can-my-mcp-client-access}

Os clientes MCP podem acessar endpoints que não retornam IPI. Você controla quais endpoints um agente pode usar por meio das permissões que atribui à sua chave de API.

### Meu cliente MCP pode alterar dados da Braze? {#can-my-mcp-client-change-braze-data}

Sim. O servidor expõe um conjunto focado de endpoints de escrita que permitem que agentes criem ou atualizem conteúdo no seu espaço de trabalho, como ativos da Biblioteca de mídia, modelos de e-mail e blocos de conteúdo. Cada endpoint de escrita requer sua própria permissão de chave de API. Se você não quiser que seu agente faça uma determinada alteração na Braze, deixe essa permissão desativada ao criar sua chave de API. Para a lista completa de funções de escrita e suas permissões necessárias, veja [Funções de API disponíveis]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/available_api_functions/){% endif %}.

### Posso usar um servidor MCP de terceiros para a Braze? {#can-i-use-a-third-party-mcp-server-for-braze}

Usar um servidor MCP de terceiros para dados da Braze não é recomendado. Use apenas o servidor MCP oficial da Braze hospedado no [PyPi](https://pypi.org/project/braze-mcp-server/).

### Por que o servidor MCP da Braze não oferece acesso a IPI? {#why-doesnt-the-braze-mcp-server-offer-pii-access}

Para proteger os dados dos usuários e ao mesmo tempo apoiar casos de uso valiosos, o servidor é limitado a endpoints que normalmente não retornam IPI. Isso reduz o risco para o seu espaço de trabalho e para as pessoas nele.

### Posso reutilizar minhas chaves de API? {#can-i-reuse-my-api-keys}

Não. Você precisará criar uma nova chave de API para seu cliente MCP. Lembre-se de dar acesso às suas ferramentas de IA apenas ao que você se sente confortável e evite permissões elevadas.

### O servidor MCP da Braze está hospedado localmente ou remotamente? {#is-the-braze-mcp-server-hosted-locally-or-remotely}

O servidor MCP da Braze atualmente disponível está hospedado localmente. Um servidor MCP remoto, hospedado pela Braze, está chegando em acesso antecipado neste verão e substituirá o servidor beta hospedado localmente.

### Por que o Cursor está listando apenas funções? {#why-is-cursor-only-listing-functions}

Verifique se você está no modo de pergunta ou no modo de agente. Para usar o servidor MCP, você precisa estar no modo de agente.

### O que eu faço quando o agente retorna uma resposta que parece incorreta? {#what-do-i-do-when-the-agent-returns-an-answer-that-looks-incorrect}

Ao trabalhar com ferramentas como o Cursor, você pode tentar mudar o modelo utilizado. Por exemplo, se estiver configurado como automático, tente mudar para um modelo específico e experimente para descobrir qual funciona melhor para o seu caso de uso. Você também pode iniciar um novo chat e repetir o prompt.

Se os problemas persistirem, envie um e-mail para [mcp-product@braze.com](mailto:mcp-product@braze.com) para nos informar. Se possível, inclua um vídeo e expanda as funções de chamada para que possamos ver quais chamadas o agente tentou.

{% multi_lang_include mcp_server/legal_disclaimer.md %}