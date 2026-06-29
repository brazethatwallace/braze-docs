---
nav_title: FAQ
article_title: Perguntas frequentes sobre agentes
description: "Este artigo fornece respostas para perguntas frequentes sobre os Braze Agents."
page_order: 10
---

# Perguntas frequentes sobre agentes {#agents-frequently-asked-questions}

> Este artigo responde a perguntas frequentes sobre os Braze Agents.

## Geral {#general}

### Qual é a diferença entre agentes de Canvas e agentes de catálogo? {#what-is-the-difference-between-canvas-agents-and-catalog-agents}

Ao criar um agente, você especifica se deseja criar um agente de Canvas ou de catálogo. Isso determina os tipos de instruções e opções que o agente pode suportar. Os agentes de Canvas processam usuários em tempo real dentro de jornadas, enquanto os agentes de catálogo enriquecem dados do catálogo adicionando ou atualizando colunas com informações processadas.

### Quais são os benefícios de usar o modelo Auto em vez do modelo próprio (BYO)? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Os benefícios de usar o modelo Auto da Braze incluem:

- Não exigir recuperação ou inserção de chaves de API nem configuração de integração
- Roteamento automático de cada invocação para o modelo mais eficaz para realizar a tarefa

### Onde posso encontrar meu uso atual de agentes? {#where-can-i-find-my-current-agent-usage}

Acesse **Configurações** > **Faturamento** > **Uso de créditos** para ver os detalhes do uso de agentes e custos de créditos.

### Posso usar instruções condicionais de Liquid nas instruções do agente? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Não. Tentar escrever blocos Liquid como instruções {% raw %}`{% if %}`{% endraw %} pode resultar em um erro de validação. Em vez disso, os agentes podem lidar com diferentes cenários por meio de descrições em linguagem natural no prompt.

### Os agentes podem acessar dados de usuários além dos atributos ou valores Liquid específicos que eu passo para eles? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-values-that-i-pass-to-them}

Não. Os agentes recebem apenas os pontos de dados de usuários específicos que são passados usando Liquid, bem como os [recursos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources) adicionados ao contexto do agente. Os agentes não podem pesquisar perfis de usuários em busca de atributos que o profissional de marketing não os configurou para procurar.

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

Para agentes de Canvas, configure [valores de fallback]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) no Console do agente para que os usuários ainda recebam uma saída quando uma invocação falhar.

## Conformidade {#compliance}

### O Console do agente está em conformidade com GDPR/CCPA? {#is-agent-console-gdprccpa-compliant}

Sim. Quando um cliente usa o modelo Auto da Braze (alimentado pelo Gemini), o Google atua como subprocessador da Braze, sujeito aos termos do Adendo de Processamento de Dados (DPA) entre o cliente e a Braze.

### O Console do agente está em conformidade com HIPAA? {#is-agent-console-hipaa-compliant}

Sim. Ao usar o modelo Auto da Braze, temos um acordo HIPAA específico, o Business Associate Addendum (BAA), com o Google cobrindo o Gemini, que alimenta nosso modelo Auto.

Nosso BAA se aplica apenas a clientes que usam o modelo Auto da Braze. Se os clientes usarem sua própria chave de LLM, a Braze não envia Informações de Saúde Protegidas (PHI) sujeitas ao HIPAA para um LLM em nome deles; os clientes as enviam diretamente. Nesse caso, o BAA entre a Braze e o Google não se aplica. O processamento de dados por meio da chave de LLM própria é regido pelo contrato do cliente e por qualquer BAA que ele tenha diretamente com seu provedor de LLM.