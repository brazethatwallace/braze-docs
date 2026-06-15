---
nav_title: Console do agente
article_title: Braze Agents
page_order: 1
description: "Os Braze Agents podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes."
---

# Braze Agents no Console do agente {#braze-agents-in-agent-console}

> Os Braze Agents são assistentes alimentados por IA que você pode criar dentro da Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes.

{% alert important %}
São necessários créditos de mensagem ou créditos de ação para acessar e usar os Braze Agents. Se você não tem créditos de ação no momento e deseja usar os Braze Agents, entre em contato com seu gerente de conta para saber as próximas etapas.
{% endalert %}

Assista a este vídeo para ter uma visão geral dos Braze Agents no Console do agente.

{% multi_lang_include video.html id="afd0hp0vrh" source="wistia" title="Visão geral dos Braze Agents no Console do agente" %}

## Por que usar os Braze Agents? {#why-use-braze-agents}

Os Braze Agents ajudam sua equipe a oferecer experiências mais inteligentes e personalizadas, sem adicionar trabalho extra. Eles agem como agentes autônomos que não apenas respondem a comandos, mas compreendem o contexto, tomam decisões e agem em direção a um objetivo.

Na prática, os agentes podem criar automaticamente textos de mensagens — como linhas de assunto ou texto no produto — para que cada cliente receba uma comunicação que pareça feita sob medida. Eles também podem se adaptar em tempo real, direcionando as pessoas por diferentes jornadas do Canvas com base em preferências, comportamentos ou outros dados.

Além do envio de mensagens, os agentes podem enriquecer seus catálogos calculando ou gerando valores de campos de produtos e perfis, mantendo seus dados atualizados e dinâmicos. Ao assumir tarefas repetitivas ou complexas, eles liberam sua equipe para se concentrar em estratégia e criatividade, em vez de configurações manuais. Os Braze Agents atuam mais como colaboradores do que como processos em segundo plano — ajudando você a resolver problemas e causar impacto em grande escala.

### Quando usar os Braze Agents em comparação com outros recursos do BrazeAI {#when-to-use-braze-agents-versus-other-brazeai-features}

Use agentes para personalizar o conteúdo em tempo real, utilizando o contexto específico do usuário. Por exemplo, se um agente sabe que o sabor de sorvete favorito de um determinado usuário é chocolate e sua cobertura favorita são ursinhos de goma, ele pode criar um texto de push específico para essa combinação para esse usuário quando ele passar pelo Canvas.

No entanto, o agente não aprende por tentativa e erro e não tem noção de um objetivo final de marketing que deseja medir e maximizar. Mesmo que você peça para ele escrever textos que gerem conversões, ele não possui um mecanismo para "monitorar" o impacto de conversão de suas redações e integrar esses dados em futuras chamadas. Você pode pensar nisso como uma decisão baseada na "vibração", e não como tomada de decisões por IA baseada em recompensas.

Em contrapartida, outras ferramentas do BrazeAI são projetadas para maximizar as métricas que estão medindo. Por exemplo, os agentes são muito bons em avaliar qualitativamente como as características de um usuário influenciam sua probabilidade ou propensão a realizar uma determinada ação ou gostar de um determinado produto. No entanto, como o agente não aprende por tentativa e erro, ele não sabe como medir sua precisão na previsão de probabilidades e melhorar o sinal ao longo do tempo. Portanto, o uso do Predictive Suite supera a etapa do agente quando avaliado pela precisão de suas previsões e melhorias ao longo do tempo.

## Recursos {#features}

Os recursos dos Braze Agents incluem:

- **Configuração flexível:** Use um LLM fornecido pela Braze ou conecte seus próprios [provedores de modelos de IA]({{site.baseurl}}/partners/ai_model_providers/) (como OpenAI, Anthropic, Google Gemini ou Databricks Mosaic).
- **Integração perfeita:** Implemente agentes diretamente nas etapas do Canvas ou nos campos do catálogo.
- **Ferramentas de teste e registro:** Pré-visualize o resultado do seu agente testando com entradas de amostra antes de lançar. Visualize os registros de cada execução do agente, incluindo a entrada e a saída dessa execução.
- **Controles de uso:** Os limites diários ajudam a gerenciar o desempenho e os custos.

## Sobre os Braze Agents {#about-braze-agents}

Os agentes são configurados com instruções (prompts de sistema) que definem como eles se comportam. Quando um agente é executado, ele usa suas instruções juntamente com quaisquer dados que você passar para gerar uma resposta. Eles não podem acessar dados de usuários além do que é fornecido pelo contexto e pelas instruções selecionados.

### Conceitos-chave {#key-concepts}

| Termo | Definição |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) | O "cérebro" do agente, neste caso, um grande modelo de linguagem (LLM). Ele interpreta entradas, gera respostas e realiza raciocínios. Um modelo mais robusto (treinado com dados mais relevantes) torna o agente mais capaz e versátil. |
| [Instruções]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) | As regras ou diretrizes que você fornece ao agente (prompt de sistema). Elas definem como o agente deve se comportar cada vez que é executado. Instruções claras tornam o agente mais confiável e previsível. |
| Contexto | Dados passados para o agente em tempo de execução, onde quer que ele esteja implantado, como campos de perfil do usuário ou linhas de catálogo. Essa entrada fornece as informações que o agente usa para gerar saídas. |
| [Variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#how-context-variables-work) | Dados temporários que você pode criar e usar dentro da jornada de um usuário em um Canvas específico. |
| [Variável de saída]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/#define-the-output-variable) | A saída que o agente produz quando usado nas etapas do Canvas. As variáveis de saída armazenam o resultado do agente para personalizar o conteúdo ou orientar as jornadas do fluxo de trabalho. As variáveis de saída podem ser uma string, um número ou um tipo de dados booleano. |
| [Invocação](#limitations) | Uma única execução do agente. Isso conta para os seus limites diários. |
| [Formato de saída]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#select-output) | A estrutura de dados predefinida da resposta do agente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceitos-chave" }

## Limitações {#limitations}

As seguintes limitações se aplicam:

- Cada agente tem um limite diário padrão de 250.000 execuções, que pode ser aumentado até um máximo de 1.000.000 de execuções por dia. Entre em contato com seu gerente de sucesso do cliente se estiver interessado em aumentar esse limite.
- Por padrão, cada execução deve ser concluída em 20 segundos. Após 20 segundos, o agente retorna uma resposta `null` onde é usado.
    - Se seus agentes estiverem constantemente excedendo o tempo limite, entre em contato com o gerente da sua conta na Braze para aumentar esse limite.
- Os dados de entrada estão limitados a 25 KB por solicitação. Entradas mais longas são truncadas.

## Tratamento de erros {#error-handling}

Se o modelo conectado retornar um [erro de limite de taxa]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors) do provedor de LLM durante uma etapa de agente do Canvas, a Braze tenta novamente a solicitação até cinco vezes usando backoff exponencial. Para outras falhas (como tempo limite ou chave de API inválida), a saída do agente é definida como `null`. Se um agente atingir seu limite diário de invocações, a saída também é definida como `null`.

Quando muitos usuários entram em uma etapa de agente ao mesmo tempo, o processamento pode demorar mais por causa dos [controles de fluxo de invocação]({{site.baseurl}}/user_guide/brazeai/agents/reference/#invocation-flow-controls). Use [valores padrão de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) para se proteger contra saídas nulas nas suas mensagens.

## Como meus dados são usados e enviados para os LLMs fornecidos pela Braze? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Para gerar resultados de IA por meio dos recursos de IA da Braze que a Braze identifica como utilizando LLMs fornecidos pela Braze ("Resultado"), a Braze enviará o prompt do seu sistema ou qualquer outra entrada, conforme aplicável ("Entrada"), para o LLM fornecido pela Braze. Os dados enviados para o LLM fornecido pela Braze não são utilizados para treinar ou melhorar o LLM fornecido pela Braze. Entre você e a Braze, o Resultado é sua propriedade intelectual. A Braze não reivindicará quaisquer direitos de propriedade autoral sobre tais Resultados. A Braze não oferece qualquer tipo de garantia em relação a qualquer conteúdo gerado por IA em geral, incluindo o Resultado.

O LLM fornecido pela Braze para os Braze Agents, identificado como "Auto", utiliza modelos Google Gemini. O Google retém as Entradas e os Resultados enviados por meio da Braze por 55 dias, após os quais os dados são excluídos.

## Próximas etapas {#next-steps}

Agora que você já conhece os Braze Agents, está pronto para as próximas etapas:

- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Implantar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)