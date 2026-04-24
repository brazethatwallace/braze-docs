---
nav_title: FAQ
article_title: FAQ sobre Agents
description: "Este artigo fornece respostas para perguntas frequentes sobre Agents da Braze."
page_order: 10
---

# Perguntas frequentes sobre Agents

## Geral

### Qual é a diferença entre agents de Canvas e agents de catálogo?

Ao criar um agent, você especifica se deseja criar um agent de Canvas ou de catálogo. Isso determina os tipos de instruções e opções que o agent pode suportar. Agents de Canvas processam usuários em tempo real dentro de jornadas, enquanto agents de catálogo enriquecem dados do catálogo adicionando ou atualizando colunas com informações processadas.

### Quais são os benefícios de usar o modelo Auto em vez do modelo próprio (BYO)?

Os benefícios de usar o modelo Auto da Braze incluem:

- Não exigir recuperação ou inserção de chaves de API nem configuração de integração
- Roteamento automático de cada invocação para o modelo mais eficaz para realizar a tarefa

### Onde posso encontrar meu uso atual de agents?

Acesse **Configurações** > **Faturamento** > **Uso de créditos** para ver os detalhes do uso de agents e custos de créditos.

### Posso usar instruções condicionais de Liquid nas instruções do agent?

Não. Tentar escrever blocos Liquid como instruções {% raw %}`{% if %}`{% endraw %} pode resultar em um erro de validação. Em vez disso, os agents podem lidar com diferentes cenários por meio de descrições em linguagem natural no prompt.

### Os agents podem acessar dados de usuários além dos atributos ou valores Liquid específicos que eu passo para eles?

Não. Os agents recebem apenas os pontos de dados de usuários específicos que são passados usando Liquid, bem como os [recursos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#add-resources) adicionados ao contexto do agent. Os agents não podem pesquisar perfis de usuários em busca de atributos que o profissional de marketing não os configurou para procurar.

## Solução de problemas

### Por que meu agent não seguiu minhas instruções ou regras?

Considere usar o [Operator]({{site.baseurl}}/user_guide/brazeai/operator) para investigar por que seu agent não está seguindo suas instruções. O Operator pode fornecer instruções passo a passo e explicações detalhadas.

### Meu agent está tendo dificuldades com uma tarefa complexa. Como posso melhorar sua performance? {#subagent-approach}

Se o agent estiver tendo dificuldades com as tarefas que você está pedindo, considere uma abordagem de sub-agents. Por exemplo, você poderia usar três agents para fazer o seguinte:

- Agent 1 padroniza e transforma dados de contexto de Canvas não estruturados recebidos.
- Agent 2 consulta um catálogo de detalhes de itens e identifica quais itens podem ser relevantes.
- Agent 3 consulta um catálogo diferente que contém diversas descrições possíveis para cada item e identifica a descrição do item mais relevante para o usuário, para incluir em um e-mail.

### O que pode fazer com que um agent personalizado frequentemente expire por tempo limite?

Um agent personalizado pode expirar por tempo limite se:

- As instruções do agent estiverem incompletas ou contraditórias
- As instruções do agent não cobrirem todos os cenários ou não incluírem uma condição de fallback (como "Se todas as entradas estiverem em branco, retorne 'Não foi possível personalizar'")
- As instruções do agent pedirem que ele produza um formato de saída diferente do especificado na guia **Saída** (por exemplo, se as instruções do agent pedem uma string, mas na guia **Saída** a saída está definida como um número)
- A tarefa do agent for complexa demais e se beneficiaria de uma [abordagem de sub-agents](#subagent-approach)

## Conformidade

### O Console do agente está em conformidade com GDPR/CCPA?

Sim. Quando um cliente usa o modelo Auto da Braze (alimentado pelo Gemini), o Google atua como subprocessador da Braze, sujeito aos termos do Adendo de Processamento de Dados (DPA) entre o cliente e a Braze.

### O Console do agente está em conformidade com HIPAA?

Sim. Ao usar o modelo Auto da Braze, temos um acordo HIPAA específico, o Business Associate Addendum (BAA), com o Google cobrindo o Gemini, que alimenta nosso modelo Auto.

Nosso BAA se aplica apenas a clientes que usam o modelo Auto da Braze. Se os clientes usarem sua própria chave de LLM, a Braze não envia Informações de Saúde Protegidas (PHI) sujeitas ao HIPAA para um LLM em nome deles; os clientes as enviam diretamente. Nesse caso, o BAA entre a Braze e o Google não se aplica. O processamento de dados por meio da chave de LLM própria é regido pelo contrato do cliente e por qualquer BAA que ele tenha diretamente com seu provedor de LLM.