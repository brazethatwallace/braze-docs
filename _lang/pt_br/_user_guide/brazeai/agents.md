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

Os Braze Agents ajudam sua equipe a entregar experiências mais inteligentes e personalizadas, sem adicionar trabalho extra. Eles atuam como agentes autônomos que não apenas respondem a comandos, mas entendem o contexto, tomam decisões e agem em direção a um objetivo.

Na prática, os agentes podem criar automaticamente textos de mensagens — como linhas de assunto ou textos dentro do produto — para que cada cliente receba uma comunicação que pareça feita sob medida. Eles também podem se adaptar em tempo real, direcionando pessoas por diferentes jornadas do Canvas com base em preferências, comportamentos ou outros dados.

Além do envio de mensagens, os agentes podem enriquecer seus catálogos calculando ou gerando valores de campos de produtos e perfis, mantendo seus dados atualizados e dinâmicos. Ao assumir tarefas repetitivas ou complexas, eles liberam sua equipe para focar em estratégia e criatividade em vez de configurações manuais. Os Braze Agents funcionam mais como colaboradores do que como processos em segundo plano — ajudando você a resolver problemas e gerar impacto em escala.

### Quando usar os Braze Agents em vez de outros recursos do BrazeAI {#when-to-use-braze-agents-versus-other-brazeai-features}

Use agentes para personalizar conteúdo em tempo real usando o contexto específico de um usuário. Por exemplo, se um agente sabe que o sabor de sorvete favorito de um determinado usuário é chocolate e a cobertura favorita são ursinhos de goma, ele pode criar um texto de push específico para essa combinação enquanto o usuário passa pelo Canvas.

No entanto, o agente não aprende por tentativa e erro, e não tem noção de um objetivo de marketing final que esteja buscando medir e maximizar. Mesmo que você diga para ele escrever textos que gerem conversões de modo geral, ele não tem um mecanismo para "monitorar" o impacto de conversão da sua escrita autônoma e integrar esses dados em chamadas futuras. Você pode pensar nisso como uma tomada de decisão por "intuição", e não como uma tomada de decisão baseada em recompensa com IA.

Em contraste, outras ferramentas do BrazeAI são projetadas para maximizar as métricas que estão medindo. Por exemplo, os agentes são muito bons em avaliar qualitativamente como as características de um usuário influenciam a probabilidade ou propensão de realizar um determinado evento ou gostar de um determinado produto. No entanto, como o agente não aprende por tentativa e erro, ele não sabe como medir sua precisão na previsão de probabilidades e melhorar o sinal ao longo do tempo. Sendo assim, usar o Predictive Suite supera a etapa de agente quando avaliado pela precisão de suas previsões e melhorias ao longo do tempo.

## Recursos {#features}

Os recursos dos Braze Agents incluem:

- **Configuração flexível:** Use um LLM fornecido pela Braze ou conecte seus próprios [provedores de modelos de IA]({{site.baseurl}}/partners/ai_model_providers) (como OpenAI, Anthropic, Google Gemini ou Databricks Mosaic).
- **Integração simplificada:** Implante agentes diretamente em etapas do Canvas ou campos de catálogo.
- **Testes, logs e histórico de versões:** Visualize a saída do seu agente testando com entradas de exemplo antes de lançar. Consulte os logs de cada execução do agente, incluindo a entrada e a saída dessa execução. Use a guia **Version history** para revisar versões anteriores e comparações inline de alterações nas instruções.
- **Controles de uso:** Limites diários ajudam a gerenciar performance e custos.

## Sobre os Braze Agents {#about-braze-agents}

Os agentes são configurados com instruções (prompts de sistema) que definem como eles se comportam. Quando um agente é executado, ele usa suas instruções junto com quaisquer dados que você passe explicitamente para gerar uma resposta. Eles não podem acessar dados de usuários além do que você configurar — variáveis Liquid, seleções de contexto do agente, variáveis de contexto do Canvas e valores de etapa de contexto. Os agentes não pesquisam perfis nem alertam quando dados estão ausentes. Consulte [Quais dados os agentes recebem]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Conceitos-chave {#key-concepts}

| Termo | Definição |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | O "cérebro" do agente — neste caso, um modelo de linguagem grande (LLM). Ele interpreta entradas, gera respostas e realiza raciocínio. Um modelo mais robusto (treinado com dados mais relevantes) torna o agente mais capaz e versátil. |
| [Instruções]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | As regras ou diretrizes que você fornece ao agente (prompt de sistema). Elas definem como o agente deve se comportar cada vez que é executado. Instruções claras tornam o agente mais confiável e previsível. |
| Contexto | Dados passados ao agente em tempo de execução, onde quer que ele esteja implantado, como campos de perfil de usuário ou linhas de catálogo. Essa entrada fornece as informações que o agente usa para gerar saídas. |
| [Variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Dados temporários que você pode criar e usar dentro da jornada de um usuário em um Canvas específico. |
| [Variável de saída]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | A saída que o agente produz quando usado em etapas do Canvas. As variáveis de saída armazenam o resultado do agente para personalizar conteúdo ou orientar caminhos do fluxo de trabalho. As variáveis de saída podem ser do tipo string, número ou booleano. |
| [Invocação](#limitations) | Uma única execução do agente. Isso conta contra seus limites diários. |
| [Formato de saída]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | A estrutura de dados predefinida da resposta do agente. |
| [Fontes de conhecimento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Um tipo de contexto de agente usado para recuperar dados de um catálogo com mais precisão do que se o catálogo fosse referenciado diretamente nas instruções do agente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conceitos-chave" }

## Limitações {#limitations}

As seguintes limitações se aplicam:

- Cada agente tem um limite diário padrão de invocação de 250.000 execuções, que pode ser aumentado até um máximo de 1.000.000 de execuções por dia. Entre em contato com o gerente de sucesso do cliente se tiver interesse em aumentar esse limite.
- O Agent Console mostra um **Limite diário de custo de créditos de ação** para cada agente — o máximo estimado de créditos por dia com base na proporção de créditos por invocação do seu modelo e no limite diário de invocação. Consulte [Limites diários de invocação e créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Por padrão, cada execução deve ser concluída em 20 segundos. Após 20 segundos, o agente retorna uma resposta `null` onde é utilizado.
    - Se seus agentes atingirem o tempo limite de forma consistente, entre em contato com o gerente da sua conta na Braze para aumentar esse limite.
- Os dados de entrada são limitados a 25 KB por solicitação. Entradas mais longas são truncadas.

## Boas práticas {#best-practices}

Priorize casos de uso de alto valor, nos quais os agentes podem gerar o maior retorno sobre o investimento (ROI), e escolha públicos com maior probabilidade de resposta. Um público menor e com alta oportunidade frequentemente supera um público grande com baixa oportunidade — por exemplo, redirecionar usuários que pesquisaram recentemente mas não converteram, em vez de enviar textos gerados por agentes para toda a sua base de usuários.

Para validar o ROI antes de escalar, use uma etapa de [jornadas experimentais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para enviar apenas parte do seu público por uma etapa de agente. Quando um teste em pequena escala apresentar bons resultados, escale o agente para todo o seu público-alvo e aumente o [limite diário de invocações]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits) para que as invocações não sejam limitadas no meio do envio. Confirme que você está confortável com o consumo estimado de créditos antes de escalar para todo o seu público. Para mais orientações sobre implantação, consulte [Implantar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Tratamento de erros {#error-handling}

Se o modelo conectado retornar um [erro de limite de frequência]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) do provedor de LLM durante uma invocação de agente de etapa do Canvas ou agente de catálogo, a Braze tenta novamente a solicitação de forma contínua usando backoff exponencial.

Para outras falhas (como timeout ou chave de API inválida), a saída do agente de etapa do Canvas é definida como `null`, a menos que o agente tenha [valores de fallback configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) no Agent Console (apenas para agentes de etapa do Canvas). Agentes de catálogo não fazem novas tentativas para falhas que não sejam de limite de frequência. Se um agente atingir seu limite diário de invocações, a Braze aplica os valores de fallback configurados quando presentes; caso contrário, a saída é definida como `null`.

Erros de limite de frequência, indisponibilidade do modelo e falhas por limite diário de invocações não consomem créditos da Braze. Timeouts consomem créditos. Consulte [Quando os créditos são consumidos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

Quando muitos usuários entram em uma etapa de agente ao mesmo tempo, o processamento pode demorar mais por causa dos [controles de fluxo de invocação]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls). Configure valores de fallback no Agent Console para agentes de etapa do Canvas para que os usuários ainda recebam uma saída quando uma invocação falhar, ou use [valores padrão de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) nas etapas de mensagem subsequentes.

## Como meus dados são usados e enviados para LLMs fornecidos pela Braze? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Para gerar saídas de IA por meio de recursos de IA da Braze que a Braze identifica como utilizando LLMs fornecidos pela Braze ("Saída"), a Braze enviará seu prompt de sistema ou qualquer outra entrada, conforme aplicável ("Entrada"), para o LLM fornecido pela Braze. Os dados enviados ao LLM fornecido pela Braze aplicável não são usados para treinar ou melhorar o LLM fornecido pela Braze. Entre você e a Braze, a Saída é sua propriedade intelectual. A Braze não reivindicará direitos autorais sobre essa Saída. A Braze não oferece garantia de qualquer tipo em relação a conteúdo gerado por IA em geral, incluindo a Saída.

O LLM fornecido pela Braze para os Braze Agents, identificado como "Auto", utiliza modelos Google Gemini. O Google retém Entradas e Saídas enviadas por meio da Braze por 55 dias, após os quais os dados são excluídos.

## Próximos passos {#next-steps}

Agora que você conhece os Braze Agents, está pronto para os próximos passos:

- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Implantar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)