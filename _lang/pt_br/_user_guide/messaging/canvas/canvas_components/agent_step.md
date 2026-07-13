---
nav_title: Agente
article_title: Etapa de agente
alias: /agent_step/
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como usar a etapa de agente no Canvas para gerar conteúdo ou tomar decisões inteligentes em tempo real."
tool: Canvas
toc_headers: h2
---

# Etapa de agente {#agent-step}

> A etapa de agente permite adicionar decisões baseadas em IA e geração de conteúdo diretamente no fluxo de trabalho do seu Canvas. Para informações mais gerais, consulte [Agentes da Braze]({{site.baseurl}}/user_guide/brazeai/agents).

![Uma etapa de agente na jornada de usuário de um Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Pré-requisitos {#prerequisites}

As etapas de agente usam [variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para ingerir contexto relevante e gerar uma variável que pode ser utilizada no Canvas.

## Como funciona {#how-it-works}

Quando um usuário chega a uma etapa de agente em um Canvas, a Braze envia os dados de entrada que você configurou (contexto completo ou campos selecionados) para o agente escolhido. O agente então processa a entrada usando seu modelo e instruções e retorna uma saída. Essa saída é armazenada na variável de saída que você definiu na etapa.

Você pode usar essa variável de três formas principais:

- **Tomada de decisão:** Direcione os usuários por diferentes jornadas do Canvas com base na resposta do agente. Por exemplo, um agente de pontuação de leads pode retornar uma categoria de lead como "Sales Ready", "Marketing Qualified" ou "Disqualified". Você pode usar essa atribuição para disparar um alerta no Slack ou uma mensagem automatizada para leads "Sales Ready", enquanto remove leads "Disqualified" da jornada.
- **Personalização:** Insira a resposta do agente diretamente em uma mensagem. Por exemplo, um agente pode analisar o feedback de um cliente e gerar um e-mail de acompanhamento empático que faz referência ao comentário do cliente e sugere uma resolução.
- **Processamento de dados de usuários:** Analise e padronize seus dados de usuários e, em seguida, armazene-os no perfil de usuário ou envie-os usando um webhook. Por exemplo, um agente pode retornar uma pontuação de sentimento ou uma atribuição de afinidade de produto. Você pode armazenar esses dados em um perfil de usuário para uso futuro.

## Criando uma etapa de agente {#creating-an-agent-step}

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Agent** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Agent**.

### Etapa 2: Escolher o agente {#step-2-choose-your-agent}

Selecione o agente que processará os dados nesta etapa. Para orientações de configuração, consulte [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

Na lista de agentes, cada agente é identificado com seu [limite diário de invocações]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details). Passe o cursor sobre o limite para ver o progresso atual em relação a esse limite, incluindo a porcentagem utilizada e o número de invocações usadas hoje em comparação com o limite.

![O painel Configurar etapa de agente mostrando o menu suspenso de agentes com dois agentes listados. Cada agente é identificado com seu limite diário de invocações. Uma dica de ferramenta no primeiro agente mostra a porcentagem utilizada e as invocações usadas hoje.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Etapa 3: Definir a saída do agente {#define-the-output-variable}

As saídas do agente são chamadas de "variáveis de saída" e são armazenadas em uma [variável de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-types) para fácil acesso. Para definir a variável de saída, dê um nome à variável.

O tipo de dado da variável de saída é definido no [Console do agente]({{site.baseurl}}/user_guide/brazeai/agents). As saídas do agente podem ser salvas como strings, números, booleanos ou objetos. Isso as torna flexíveis tanto para personalização de texto quanto para lógica condicional no seu Canvas. Veja alguns usos comuns para cada tipo:

| Tipo de dado | Usos comuns |
| --- | --- |
| String | Personalização de mensagens (linhas de assunto, textos, respostas) |
| Número | Pontuação, limites, roteamento em [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Booleano | Ramificação Sim/Não em [Divisões de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Objeto | Aproveite um ou mais dos tipos de dados anteriores nesta seção com uma única chamada de LLM em uma estrutura de dados previsível |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Definir a saída do agente" }

Você pode usar uma variável de saída em todo o Canvas usando a mesma sintaxe de modelo que usaria com uma variável de contexto. Use o filtro de Segment **Context Variable** ou insira as respostas do agente diretamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}`{% endraw %}.

Para usar uma propriedade específica de uma variável de saída do tipo objeto, use a notação de ponto para acessar essa propriedade usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Etapa de agente para Body HTML Writer com um tipo de dado de objeto como saída para a variável "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Etapa 4: Adicionar contexto adicional (opcional) {#step-4-add-any-additional-context-optional}

Você pode optar por incluir valores de contexto adicionais para a etapa de agente referenciar durante a execução. Você pode inserir qualquer valor com modelo Liquid que normalmente usaria em um Canvas.

{% alert note %}
O agente já recebe automaticamente o contexto configurado na seção **Instructions**. Variáveis Liquid que já foram configuradas lá não precisam ser inseridas novamente aqui.
{% endalert %}

![A opção de adicionar contexto adicional a uma etapa de agente usando Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Etapa 5: Testar o agente {#step-5-test-the-agent}

Após configurar sua etapa de agente, você pode testar e pré-visualizar a saída desta etapa.

![Pré-visualizar a saída do agente como um usuário aleatório.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Tratamento de erros {#error-handling}

Para saber como a Braze lida com falhas de agentes, erros de limite de frequência e controles de fluxo de invocação, consulte [Tratamento de erros e comportamento de fallback]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) em Implantar agentes e [Tratamento de erros]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) em Agentes da Braze.

- Se o modelo conectado retornar um [erro de limite de frequência]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) do provedor de LLM, a Braze tenta novamente a solicitação de forma contínua usando backoff exponencial até que a chamada seja bem-sucedida ou a Braze determine que ela não pode ser concluída; os usuários então avançam para a próxima etapa do Canvas.
- Para outras falhas (como erro de timeout ou chave de API inválida), ou quando um agente atinge seu limite diário de invocações, a variável de saída é definida como `null`, a menos que o agente tenha [valores de fallback configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) no Console do agente. Quando valores de fallback estão configurados, a Braze renderiza o fallback com Liquid por usuário e armazena o resultado na variável de saída, inclusive quando o limite diário bloqueia uma invocação.
- Se você não configurar valores de fallback, use [valores padrão de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) nas etapas de mensagem subsequentes para lidar com saídas nulas. Por exemplo, no modal **Add Personalization**, você pode inserir um valor padrão de Liquid como {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- As respostas são armazenadas em cache para entradas idênticas e podem ser reutilizadas para invocações idênticas repetidas dentro de alguns minutos.
    - Respostas que usam valores em cache ainda contam para o total e as invocações diárias.
- As etapas de agente podem levar tempo para processar um grande lote de usuários. A Braze enfileira as invocações de acordo com os [controles de fluxo de invocação]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), então os usuários podem permanecer pendentes durante envios de alto volume. Verifique seus registros para confirmar que as invocações estão acontecendo.

## Analytics {#analytics}

Consulte as métricas a seguir para acompanhar o desempenho das suas etapas de agente:

| Métrica | Descrição |
| --- | --- |
| _Entered_ | O número de vezes que os usuários entraram na etapa de agente. |
| _Proceeded to Next Step_ | O número de usuários que avançaram para a próxima etapa do fluxo após passar pela etapa de agente. |
| _Exited Canvas_ | O número de usuários que saíram do Canvas após passar pela etapa de agente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }

## Práticas recomendadas {#best-practices}

### Divida tarefas entre agentes para casos de uso complexos {#split-tasks-between-agents-for-complicated-use-cases}

Se você perceber que um agente está tendo dificuldades com a complexidade das tarefas que você está pedindo, divida o trabalho em mais de uma etapa de agente. Quando um único prompt mistura limpeza de dados, lógica de roteamento e redação completa de mensagens, esses objetivos competem entre si e a qualidade da saída pode variar.

O padrão a seguir usa três agentes para um exemplo de viagens: alguém pesquisou no seu app recentemente, mas não fez a reserva, e você quer um texto de redirecionamento que o incentive a concluir a compra.

- O agente 1 resume o contexto do Canvas. Ele lê campos como nível de fidelidade, última cidade pesquisada e comportamento de pesquisa de alta intenção, e retorna um resumo curto e estruturado como uma variável de saída que as etapas seguintes podem reutilizar.
- O agente 2 retorna um valor de roteamento que seu Canvas pode usar para ramificação. Use um número, booleano ou objeto estruturado para que a saída corresponda à forma como você faz a ramificação. Mapeie esse valor para uma etapa de [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split). Por exemplo, considere jornadas separadas para mensagens baseadas em fidelidade versus mensagens baseadas em ofertas.
- O agente 3 redige o texto da mensagem gerada apenas nas ramificações onde você deseja. Passe o resumo do agente 1 (e qualquer contexto específico da ramificação) para que este agente se concentre no tom e nos limites do canal, em vez de normalizar entradas e escolher estratégias no mesmo prompt.

### Use a etapa jornada experimental para testar jornadas com agentes em pequena escala {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Para testar o desempenho e o consumo de créditos do seu agente em comparação com suas jornadas existentes, adicione uma etapa de [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que apenas parte do seu público entre na ramificação que contém sua etapa de agente.

Por exemplo, você pode começar enviando alguns milhares de usuários por dia por uma jornada com o agente e enviar o restante para uma jornada de controle ou uma jornada sem o agente. Colete dados por 1 a 2 semanas e compare indicadores-chave de desempenho (KPIs), contra-métricas e consumo de créditos do agente entre as jornadas. Dessa forma, você pode ganhar confiança e comprovar o ROI antes de aumentar o tráfego para a ramificação habilitada com agente, limitando o consumo de invocações ao mesmo tempo.

## Perguntas frequentes {#frequently-asked-questions}

### Quando devo usar uma etapa de agente? {#when-should-i-use-an-agent-step}

De modo geral, recomendamos usar uma etapa de agente quando você deseja alimentar dados contextuais específicos em um LLM e fazer com que ele atribua de forma agêntica uma variável de contexto do Canvas de maneira inteligente, em uma escala impossível para humanos.

Digamos que você está enviando uma mensagem personalizada para recomendar um novo sabor de sorvete a um usuário que anteriormente pediu chocolate e morango. Veja a diferença entre usar uma etapa de agente e a recomendação de itens de IA:

- **Etapa de agente:** Usa LLMs para tomar uma decisão qualitativa sobre o que o usuário pode querer com base nas instruções e nos dados de contexto fornecidos ao agente. Neste exemplo, uma etapa de agente pode recomendar um novo sabor com base na possibilidade de o usuário querer experimentar sabores diferentes.
- **Recomendação de itens de IA:** Usa modelos de machine learning para prever os produtos que um usuário tem maior probabilidade de querer com base em eventos passados do usuário, como compras. Neste exemplo, a recomendação de itens de IA sugeriria um sabor (baunilha) com base nos dois pedidos anteriores do usuário (chocolate e morango) e em como esses se comparam aos comportamentos de outros usuários no seu espaço de trabalho.

### Como as etapas de agente usam os dados de entrada? {#how-do-agent-steps-use-input-data}

Uma etapa de agente analisa os dados de contexto que o agente está configurado para usar, bem como qualquer contexto adicional que é [fornecido ao agente](#step-4-add-any-additional-context-optional).

## Artigos relacionados {#related-articles}

- [Visão geral dos agentes da Braze]({{site.baseurl}}/user_guide/brazeai/agents)
- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)