---
nav_title: FAQ
article_title: Perguntas frequentes sobre agentes
description: "Este artigo fornece respostas para perguntas frequentes sobre os Braze Agents."
page_order: 10
toc_headers: h2
---

# Perguntas frequentes sobre agentes {#agents-frequently-asked-questions}

> Este artigo responde a perguntas frequentes sobre os Braze Agents.

## Geral {#general}

### Qual é a diferença entre Agentes de Etapa do Canvas e Agentes de Catálogo? {#what-is-the-difference-between-canvas-step-agents-and-catalog-agents}

Ao criar um agente, você especifica se deseja criar um Agente de Etapa do Canvas ou um Agente de Catálogo. Isso determina os tipos de instruções e opções que o agente pode suportar. Agentes de Etapa do Canvas processam usuários em tempo real dentro de jornadas, enquanto Agentes de Catálogo enriquecem dados de catálogo adicionando ou atualizando colunas com informações processadas.

### Quais são os benefícios de usar o modelo Auto em comparação com o modelo próprio (BYO)? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Os benefícios de usar o modelo Auto da Braze incluem:

- Não exigir recuperação ou inserção de chaves de API nem configuração de integração
- Roteamento automático de cada invocação para o modelo mais eficaz para realizar a tarefa

### Onde posso encontrar meu uso atual de agentes? {#where-can-i-find-my-current-agent-usage}

Acesse **Configurações** > **Faturamento** > **Uso de créditos** > **Agent Console** para ver o consumo de créditos, contagens de invocações e proporções de créditos por agente. Consulte [Limites diários de invocação e créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) para mais detalhes.

### Posso usar instruções condicionais em Liquid nas instruções do agente? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Não. Tentar escrever blocos Liquid como instruções {% raw %}`{% if %}{% endraw %}` pode resultar em um erro de validação. Em vez disso, os agentes podem lidar com diferentes cenários por meio de descrições em linguagem natural no prompt.

### Os agentes podem acessar dados de usuários além dos atributos Liquid específicos ou do contexto do Canvas que eu passo para eles? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

Não. Os agentes recebem apenas os pontos de dados específicos do usuário que são passados usando Liquid nas instruções, seleções de [+ Contexto do agente]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources), [etapas de Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) anteriores no Canvas ou contexto adicional na etapa do agente. Os agentes não podem pesquisar perfis de usuários em busca de atributos que você não os configurou para receber.

Os agentes também não podem avisar quando dados obrigatórios estão ausentes — eles prosseguem com o que estiver no prompt. Trate a configuração do agente como um design deliberado de entrada-para-saída: passe todos os campos que o agente precisa e verifique as entradas em **Agent Console** > **Logs**. Para orientações, consulte [Quais dados os agentes recebem]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Solução de problemas {#troubleshooting}

### Por que meu agente não seguiu minhas instruções ou regras? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Considere usar o [Operator]({{site.baseurl}}/user_guide/brazeai/operator) para investigar por que seu agente não está seguindo suas instruções. O Operator pode fornecer instruções passo a passo e explicações detalhadas.

### Por que meu agente de catálogo pulou algumas linhas? {#why-did-my-catalog-agent-skip-some-rows}

Agentes de catálogo pulam uma linha quando uma coluna que você marcou como **obrigatória para execução** está em branco ou ausente — por exemplo, um campo `gender` que não foi preenchido. Depois de selecionar as colunas de entrada, ative o controle de entrada obrigatória para o campo do catálogo e escolha quais colunas devem conter valores antes que o agente seja executado; as colunas selecionadas começam como obrigatórias por padrão, mas você pode remover colunas que podem ficar vazias sem bloquear a invocação. Isso evita o desperdício de tokens com dados incompletos.

O agente também respeita dependências entre colunas. Se uma coluna de saída depende de outras colunas (por exemplo, a coluna D requer valores nas colunas B e C), o agente não é executado até que essas colunas anteriores estejam preenchidas para aquela linha.

Para mais detalhes, consulte [Práticas recomendadas para agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### Invocações de agente com falha consomem créditos? {#do-failed-agent-invocations-consume-credits}

Depende do tipo de falha:

| Falha | Consome créditos? |
| --- | --- |
| Erro de limite de frequência | Não |
| Modelo indisponível | Não |
| Limite diário de invocações atingido | Não |
| Timeout | Sim |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Invocações de agente com falha consomem créditos?" }

Consulte [Quando os créditos são consumidos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed) para mais detalhes.

### Meu agente está tendo dificuldades com uma tarefa complexa. Como posso melhorar o desempenho dele? {#subagent-approach}

Se você perceber que o agente está tendo dificuldades com as tarefas que você está pedindo, considere uma abordagem de subagentes. Por exemplo, você poderia usar três agentes para fazer o seguinte:

- O agente 1 padroniza e transforma dados não estruturados de contexto do Canvas recebidos.
- O agente 2 consulta um catálogo de detalhes de itens e identifica quais itens podem ser relevantes.
- O agente 3 consulta um catálogo diferente que contém diversas descrições possíveis para cada item e identifica a descrição do item mais relevante para o usuário, para incluir em um e-mail.

### O que pode fazer um agente personalizado atingir timeout com frequência? {#what-might-cause-a-custom-agent-to-frequently-time-out}

Um agente personalizado pode atingir timeout se:

- As instruções do agente estiverem incompletas ou contraditórias
- As instruções do agente não cobrirem todos os cenários ou não incluírem uma condição de fallback (como "Se todas as entradas estiverem em branco, retorne 'Não foi possível personalizar'")
- As instruções do agente pedirem um formato de saída diferente do especificado na guia **Output** (por exemplo, se as instruções pedirem uma string, mas na guia **Output** a saída estiver definida como número)
- A tarefa do agente for complexa demais e se beneficiaria de uma [abordagem de subagentes](#subagent-approach)

#### Como reduzir timeouts {#how-to-reduce-timeouts}

Se o seu agente atinge timeout com frequência, tente o seguinte antes de entrar em contato com seu gerente de conta sobre um limite de timeout mais alto:

- **Escolha um modelo mais simples ou de menor custo:** Modelos mais rápidos geralmente concluem dentro da janela de timeout padrão. Consulte [Determinar qual modelo usar]({{site.baseurl}}/user_guide/brazeai/agents/reference#determine-which-model-to-use).
- **Reduza o nível de raciocínio (somente modelos BYO):** Comece em **Minimal** e aumente apenas se a qualidade da saída for prejudicada. Consulte [Níveis de raciocínio]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels).
- **Simplifique o prompt:** Remova instruções redundantes, encurte exemplos e restrinja o esquema de saída. Use o [Operator]({{site.baseurl}}/user_guide/brazeai/operator) para revisar e refinar suas instruções.
- **Divida fluxos de trabalho complexos em vários agentes:** Se o caso de uso tiver várias subetapas (por exemplo, classificar a intenção e depois gerar o texto), use agentes separados em sequência no Canvas ou catálogo em vez de um único agente que faz tudo. Consulte a [abordagem de subagentes](#subagent-approach).

{% alert note %}
Timeouts consomem créditos da Braze mesmo quando o agente não retorna nenhuma saída utilizável. Consulte [Quando os créditos são consumidos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).
{% endalert %}

Para agentes de etapa do Canvas, configure [valores de fallback]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) no Agent Console para que os usuários ainda recebam uma saída quando uma invocação falhar.

### Por que meu agente funcionou bem nos testes, mas não está recebendo dados específicos do usuário quando eu o lanço em um Canvas? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

Se o seu agente funciona corretamente durante os testes, mas não recebe dados específicos do usuário em um Canvas ativo, tente estas etapas de solução de problemas:

- Certifique-se de que os dados específicos do usuário que você deseja que o agente receba estejam inseridos como variáveis Liquid nas instruções do agente.
- Se você tiver dados importantes no contexto do Canvas, use a opção **Add all Canvas context** na configuração do agente para garantir que o agente receba todo o contexto do Canvas.
- Certifique-se de que qualquer contexto do Canvas que você deseja que o agente acesse esteja armazenado como contexto do Canvas. Use uma etapa de contexto antes da etapa do agente para armazenar esses dados.

## Conformidade {#compliance}

### O Agent Console está em conformidade com o GDPR/CCPA? {#is-agent-console-gdprccpa-compliant}

Sim. Quando um cliente usa o modelo Braze Auto (desenvolvido com o Gemini), o Google atua como subprocessador da Braze, sujeito aos termos do Adendo de Processamento de Dados (DPA) entre o cliente e a Braze.

### O Agent Console está em conformidade com o HIPAA? {#is-agent-console-hipaa-compliant}

Sim. Ao usar o modelo Braze Auto, temos um acordo específico de HIPAA, o Adendo de Associado Comercial (BAA), com o Google cobrindo o Gemini, que alimenta nosso modelo Auto.

Nosso BAA se aplica apenas a clientes que usam o modelo Braze Auto. Se os clientes usarem sua própria chave de LLM, a Braze não envia Informações de Saúde Protegidas (PHI) sujeitas ao HIPAA para um LLM em nome deles; os clientes as enviam diretamente. Nesse caso, o BAA entre a Braze e o Google não se aplica. O processamento de dados por meio da chave de LLM do próprio cliente é regido pelo contrato do cliente e por qualquer BAA que ele tenha diretamente com seu provedor de LLM.