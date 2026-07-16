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

### Qual é a diferença entre agentes de etapa do Canvas e agentes de catálogo? {#what-is-the-difference-between-canvas-step-agents-and-catalog-agents}

Ao criar um agente, você especifica se deseja criar um agente de etapa do Canvas ou um agente de catálogo. Isso determina os tipos de instruções e opções que o agente pode suportar. Os agentes de etapa do Canvas processam usuários em tempo real dentro de jornadas, enquanto os agentes de catálogo enriquecem dados do catálogo adicionando ou atualizando colunas com informações processadas.

### Quais são os benefícios de usar o modelo Auto em vez do modelo próprio (BYO)? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Os benefícios de usar o modelo Auto da Braze incluem:

- Não exigir recuperação ou inserção de chaves de API nem configuração de integração
- Roteamento automático de cada invocação para o modelo mais eficaz para realizar a tarefa

### Onde posso encontrar meu uso atual de agentes? {#where-can-i-find-my-current-agent-usage}

Acesse **Configurações** > **Faturamento** > **Uso de créditos** > **Console do agente** para ver o consumo de créditos, contagens de invocações e proporções de créditos por agente. Consulte [Limites diários de invocação e créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) para mais detalhes.

### Posso usar instruções condicionais de Liquid nas instruções do agente? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Não. Tentar escrever blocos Liquid como instruções {% raw %}`{% if %}`{% endraw %} pode resultar em um erro de validação. Em vez disso, os agentes podem lidar com diferentes cenários por meio de descrições em linguagem natural no prompt.

### Os agentes podem acessar dados de usuários além dos atributos Liquid específicos ou do contexto de Canvas que eu passo para eles? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

Não. Os agentes recebem apenas os pontos de dados de usuários específicos que são passados usando Liquid nas instruções, seleções de [+ Contexto do agente]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources), [etapas de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) anteriores no Canvas ou contexto adicional na etapa do agente. Os agentes não podem pesquisar perfis de usuários em busca de atributos que você não os configurou para receber.

Os agentes também não podem avisar quando dados obrigatórios estão ausentes — eles prosseguem com o que estiver no prompt. Trate a configuração do agente como um design deliberado de entrada para saída: passe todos os campos que o agente precisa e verifique as entradas em **Console do agente** > **Logs**. Para orientações, consulte [Quais dados os agentes recebem]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Solução de problemas {#troubleshooting}

### Por que meu agente não seguiu minhas instruções ou regras? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Considere usar o [Operator]({{site.baseurl}}/user_guide/brazeai/operator) para investigar por que seu agente não está seguindo suas instruções. O Operator pode fornecer instruções passo a passo e explicações detalhadas.

### Por que meu agente de catálogo pulou algumas linhas? {#why-did-my-catalog-agent-skip-some-rows}

Os agentes de catálogo pulam uma linha quando uma coluna marcada como **obrigatória para execução** está em branco ou ausente — por exemplo, um campo `gender` que não foi preenchido. Depois de selecionar as colunas de entrada, ative o controle de entrada obrigatória para o campo do catálogo e escolha quais colunas devem conter valores antes que o agente seja executado; as colunas selecionadas começam como obrigatórias por padrão, mas você pode remover colunas que podem ficar vazias sem bloquear a invocação. Isso evita o desperdício de tokens com dados incompletos.

O agente também respeita dependências entre colunas. Se uma coluna de saída depende de outras colunas (por exemplo, a coluna D requer valores nas colunas B e C), o agente não é executado até que essas colunas anteriores estejam preenchidas para aquela linha.

Para mais detalhes, consulte [Práticas recomendadas para agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### Meu agente está tendo dificuldades com uma tarefa complexa. Como posso melhorar o desempenho dele? {#subagent-approach}

Se o agente estiver tendo dificuldades com as tarefas que você está pedindo, considere uma abordagem com subagentes. Por exemplo, você poderia usar três agentes para fazer o seguinte:

- O agente 1 padroniza e transforma dados de contexto de Canvas não estruturados recebidos.
- O agente 2 consulta um catálogo de detalhes de itens e identifica quais itens podem ser relevantes.
- O agente 3 consulta um catálogo diferente que contém diversas descrições possíveis para cada item e identifica a descrição do item mais relevante para o usuário, para incluir em um e-mail.

### O que pode fazer com que um agente personalizado frequentemente expire por tempo limite? {#what-might-cause-a-custom-agent-to-frequently-time-out}

Um agente personalizado pode expirar por tempo limite se:

- As instruções do agente estiverem incompletas ou contraditórias
- As instruções do agente não cobrirem todos os cenários ou não incluírem uma condição de fallback (como "Se todas as entradas estiverem em branco, retorne 'Não foi possível personalizar'")
- As instruções do agente pedirem que ele produza um formato de saída diferente do especificado na guia **Output** (por exemplo, se as instruções pedem uma string, mas na guia **Output** a saída está definida como um número)
- A tarefa do agente for complexa demais e se beneficiaria de uma [abordagem com subagentes](#subagent-approach)

Para agentes de etapa do Canvas, configure [valores de fallback]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) no Console do agente para que os usuários ainda recebam uma saída quando uma invocação falhar.

### Por que meu agente funcionou bem nos testes, mas não está recebendo dados específicos do usuário quando eu o lanço em um Canvas? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

Se o seu agente funciona corretamente durante os testes, mas não recebe dados específicos do usuário em um Canvas ativo, tente estas etapas de solução de problemas:

- Verifique se os dados específicos do usuário que você deseja que o agente receba estão inseridos como variáveis Liquid nas instruções do agente.
- Se você tem dados importantes no contexto do Canvas, use a opção **Adicionar todo o contexto do Canvas** na configuração do agente para garantir que ele receba o contexto completo do Canvas.
- Verifique se qualquer contexto do Canvas que você deseja que o agente acesse está armazenado como contexto do Canvas. Use uma etapa de contexto antes da etapa do agente para armazenar esses dados.

## Conformidade {#compliance}

### O Console do agente está em conformidade com GDPR/CCPA? {#is-agent-console-gdprccpa-compliant}

Sim. Quando um cliente usa o modelo Auto da Braze (alimentado pelo Gemini), o Google atua como subprocessador da Braze, sujeito aos termos do Adendo de Processamento de Dados (DPA) entre o cliente e a Braze.

### O Console do agente está em conformidade com HIPAA? {#is-agent-console-hipaa-compliant}

Sim. Ao usar o modelo Auto da Braze, temos um acordo HIPAA específico, o Business Associate Addendum (BAA), com o Google cobrindo o Gemini, que alimenta nosso modelo Auto.

Nosso BAA se aplica apenas a clientes que usam o modelo Auto da Braze. Se os clientes usarem sua própria chave de LLM, a Braze não envia Informações de Saúde Protegidas (PHI) sujeitas ao HIPAA para um LLM em nome deles; os clientes as enviam diretamente. Nesse caso, o BAA entre a Braze e o Google não se aplica. O processamento de dados por meio da chave de LLM própria é regido pelo contrato do cliente e por qualquer BAA que ele tenha diretamente com seu provedor de LLM.