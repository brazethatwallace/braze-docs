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

As etapas de agente usam [variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para ingerir contexto relevante e gerar uma variável que pode ser aproveitada no Canvas.

## Como funciona {#how-it-works}

Quando um usuário chega a uma etapa de Agente em um Canvas, a Braze envia os dados de entrada que você configurou (contexto completo ou campos selecionados) para o agente escolhido. O agente então processa a entrada usando seu modelo e instruções e retorna uma saída. Essa saída é armazenada na variável de saída que você definiu na etapa.

Você pode usar essa variável de três formas principais:

- **Tomada de decisão:** Direcione os usuários por diferentes jornadas do Canvas com base na resposta do agente. Por exemplo, um agente de pontuação de leads pode retornar uma categoria de lead como "Pronto para vendas", "Qualificado para marketing" ou "Desqualificado". Você pode usar essa atribuição para disparar um alerta no Slack ou uma mensagem automatizada para leads "Prontos para vendas", enquanto remove leads "Desqualificados" da jornada.
- **Personalização:** Insira a resposta do agente diretamente em uma mensagem. Por exemplo, um agente pode analisar o feedback de um cliente e gerar um e-mail de acompanhamento empático que faz referência ao comentário do cliente e sugere uma resolução.
- **Processamento de dados de usuários:** Analise e padronize seus dados de usuários, depois armazene-os no perfil de usuário ou envie-os usando um webhook. Por exemplo, um agente pode retornar uma pontuação de sentimento ou uma atribuição de afinidade de produto. Você pode armazenar esses dados em um perfil de usuário para uso futuro.

## Criando uma etapa de Agente {#creating-an-agent-step}

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Agente** da barra lateral, ou selecione o botão de mais <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Agente**.

### Etapa 2: Escolher seu agente {#step-2-choose-your-agent}

Selecione o agente que processará os dados nesta etapa. Para orientações de configuração, consulte [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

Na lista de agentes, cada agente é identificado com seu [limite diário de invocações]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details). Passe o cursor sobre o limite para ver o progresso atual em relação a esse limite, incluindo a porcentagem utilizada e o número de invocações realizadas hoje em comparação com o limite.

![O painel Configurar Etapa de Agente mostrando o menu suspenso de agentes com dois agentes listados. Cada agente é identificado com seu limite diário de invocações. Uma dica de ferramenta no primeiro agente mostra a porcentagem utilizada e as invocações realizadas hoje.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Etapa 3: Definir a saída do seu agente {#define-the-output-variable}

As saídas do agente são chamadas de "variáveis de saída" e são armazenadas em uma [variável de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-filters) para fácil acesso. Para definir a variável de saída, dê um nome à variável.

Observe que o tipo de dados da variável de saída é definido no [Console de Agentes]({{site.baseurl}}/user_guide/brazeai/agents). As saídas do agente podem ser salvas como strings, números, booleanos ou objetos. Isso as torna flexíveis tanto para personalização de texto quanto para lógica condicional no seu Canvas. Aqui estão alguns usos comuns para cada tipo:

| Tipo de dados | Usos comuns |
| --- | --- |
| String | Personalização de mensagens (linhas de assunto, texto, respostas) |
| Número | Pontuação, limites, roteamento em [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Booleano | Ramificação Sim/Não em [divisões de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Objeto | Aproveite um ou mais dos tipos de dados anteriores nesta seção com uma única chamada LLM em uma estrutura de dados previsível |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Definir a saída do seu agente #define-the-output-variable" }

Você pode usar uma variável de saída em todo o Canvas utilizando a mesma sintaxe de modelo que usaria com uma variável de contexto. Use o filtro de Segment or segmento or segmento **Context Variable** ou insira as respostas do agente diretamente usando Liquid: {% raw %}`{{context.${response_variable_name}}}`{% endraw %}.

Para usar uma propriedade específica de uma variável de saída do tipo objeto, use notação de ponto para acessar essa propriedade usando Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Etapa de agente para Body HTML Writer com um tipo de dados objeto como saída para a variável "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Etapa 4: Adicionar instruções opcionais à etapa {#step-4-add-optional-step-instructions}

Você pode incluir instruções opcionais à etapa para qualquer informação que seu agente precise saber e que seja específica a esta etapa e ainda não esteja coberta nas instruções principais do agente. Você pode inserir qualquer valor de modelo Liquid que normalmente usaria em um Canvas.

### Etapa 5: Testar o agente {#step-5-test-the-agent}

Você pode testar uma etapa de Agente de duas formas:

**Prévia na etapa (construtor de Canvas):** Após configurar a etapa, use a prévia da etapa para ver a saída do agente para um usuário aleatório, um usuário existente ou um usuário personalizado. Isso testa a etapa isoladamente, sem percorrer o caminho completo do Canvas.

**Testar Canvas (jornada completa):** Selecione **Test Canvas** no rodapé do Canvas para visualizar o caminho do usuário de ponta a ponta. Quando o teste chegar à sua etapa de Agente, a Braze perguntará **Deseja executar o agente "{agentName}"?**

- Selecione **Sim** para opcionalmente adicionar contexto, depois selecione **Simular resposta** para invocar o agente para o usuário de prévia. Você pode descrever entradas de exemplo em linguagem natural (por exemplo, conteúdo do carrinho ou texto da mensagem) para complementar o perfil do usuário de teste e qualquer contexto de Canvas já definido anteriormente.
- Selecione **Não** para pular a invocação ao vivo e usar a **saída de fallback** configurada do agente no Console de Agentes.

As invocações de **Simular resposta** contam para o limite diário de invocações do agente e aparecem em **Console de Agentes** > **Logs**. Para o comportamento completo de Testar Canvas, consulte [Visualizar jornadas de usuários]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps).

![Prévia da saída do agente como um usuário aleatório.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Tratamento de erros {#error-handling}

Para saber como a Braze lida com falhas de agentes, erros de limite de frequência e controles de fluxo de invocação, consulte [Tratamento de erros e comportamento de fallback]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) em Implantar agentes e [Tratamento de erros]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) em Agentes da Braze.

- Se o modelo conectado retornar um [erro de limite de frequência]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) do provedor de LLM, a Braze tenta novamente a solicitação de forma contínua usando backoff exponencial até que a chamada seja bem-sucedida ou a Braze determine que ela não pode ser concluída; os usuários então avançam para a próxima etapa do Canvas.
- Para outras falhas (como erro de timeout ou chave de API or interface de programação do aplicativo (API) inválida), ou quando um agente atinge seu limite diário de invocações, a variável de saída é definida como `null`, a menos que o agente tenha [valores de fallback configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) no Console do agente. Quando valores de fallback estão configurados, a Braze renderiza o fallback com Liquid por usuário e armazena o resultado na variável de saída, inclusive quando o limite diário bloqueia uma invocação.
- Se você não configurar valores de fallback, use [valores padrão de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) nas etapas de mensagem subsequentes para lidar com saídas nulas. Por exemplo, no modal **Add Personalization**, você pode inserir um valor padrão de Liquid como {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} ou {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- As respostas são armazenadas em cache para entradas idênticas e podem ser reutilizadas para invocações idênticas repetidas dentro de alguns minutos.
    - Respostas que usam valores em cache ainda contam para o total e as invocações diárias.
- As etapas de agente podem levar tempo para processar um grande lote de usuários. A Braze enfileira as invocações de acordo com os [controles de fluxo de invocação]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), então os usuários podem permanecer pendentes durante envios de alto volume. Verifique seus registros para confirmar que as invocações estão acontecendo.

## Análise de dados {#analytics}

Consulte as métricas a seguir para acompanhar o desempenho das suas etapas do Agent:

| Métrica | Descrição |
| --- | --- |
| _Entered_ | O número de vezes que os usuários entraram na etapa do Agent. |
| _Proceeded to Next Step_ | O número de usuários que avançaram para a próxima etapa do fluxo após passar pela etapa do Agent. |
| _Exited Canvas_ | O número de usuários que saíram do Canvas após passar pela etapa do Agent. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Análise de dados" }

## Práticas recomendadas {#best-practices}

### Divida tarefas entre agentes para casos de uso complexos {#split-tasks-between-agents-for-complicated-use-cases}

Se você perceber que um agente está com dificuldades diante da complexidade das tarefas que você está pedindo, divida o trabalho em mais de uma etapa de agente. Quando um único prompt mistura limpeza de dados, lógica de roteamento e redação completa de mensagens, esses objetivos competem entre si e a qualidade do resultado pode variar.

O padrão a seguir usa três agentes para um exemplo de viagens: alguém pesquisou recentemente no seu app, mas não fez a reserva, e você quer um texto de redirecionamento que incentive essa pessoa a concluir a compra.

- O Agente 1 resume o contexto do Canvas. Ele lê campos como nível de fidelidade, última cidade pesquisada e comportamento de busca de alta intenção, e retorna um resumo estruturado curto como variável de saída que etapas posteriores podem reutilizar.
- O Agente 2 retorna um valor de roteamento no qual seu Canvas pode ramificar. Use um número, booleano ou objeto estruturado para que a saída corresponda à forma como você faz a Branch or ramificação or ramificação. Mapeie esse valor para uma etapa de [jornada do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split). Por exemplo, considere jornadas separadas para mensagens baseadas em fidelidade versus mensagens baseadas em ofertas.
- O Agente 3 redige o texto gerado da mensagem apenas nas ramificações onde você deseja isso. Passe o resumo do Agente 1 (e qualquer contexto específico da Branch or ramificação or ramificação) para que esse agente foque no tom e nos limites do canal, em vez de normalizar entradas e escolher estratégia no mesmo prompt.

### Use a etapa da jornada experimental para testar jornadas com agentes em pequena escala {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Para testar o desempenho e o consumo de créditos do seu agente em comparação com suas jornadas existentes, adicione uma etapa de [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que apenas parte do seu público entre na Branch or ramificação or ramificação que contém a etapa do agente.

Por exemplo, você pode começar enviando alguns milhares de usuários por dia para uma jornada com o agente e enviar o restante para uma jornada de controle ou uma jornada sem o agente. Colete dados por 1 a 2 semanas e compare indicadores chave de desempenho (KPIs), contra-métricas e consumo de créditos do agente entre as jornadas. Dessa forma, você ganha confiança e comprova o ROI or retorno sobre o investimento (ROI) antes de aumentar o tráfego para a Branch or ramificação or ramificação com o agente habilitado, limitando o consumo de invocações ao mesmo tempo.

## Perguntas frequentes {#frequently-asked-questions}

### Quando devo usar uma etapa de Agente? {#when-should-i-use-an-agent-step}

De modo geral, recomendamos usar uma etapa de Agente quando você deseja fornecer dados contextuais específicos a um LLM e fazer com que ele atribua de forma agêntica uma variável de contexto do Canvas de maneira inteligente, em uma escala impossível para humanos.

Digamos que você esteja enviando uma mensagem personalizada para recomendar um novo sabor de sorvete a um usuário que anteriormente pediu chocolate e morango. Veja a diferença entre usar uma etapa de Agente e recomendações de itens com IA:

- **Etapa de Agente:** Usa LLMs para tomar uma decisão qualitativa sobre o que o usuário pode querer, com base nas instruções e nos pontos de dados contextuais fornecidos ao agente. Neste exemplo, uma etapa de Agente pode recomendar um novo sabor com base na possibilidade de o usuário querer experimentar sabores diferentes.
- **Recomendação de itens com IA:** Usa modelos de machine learning para prever os produtos que um usuário tem maior probabilidade de querer, com base em eventos passados do usuário, como compras. Neste exemplo, a recomendação de itens com IA sugeriria um sabor (baunilha) com base nos dois pedidos anteriores do usuário (chocolate e morango) e em como esses pedidos se comparam aos comportamentos de outros usuários no seu espaço de trabalho.

### Como as etapas de Agente usam dados de entrada? {#how-do-agent-steps-use-input-data}

Uma etapa de Agente analisa os dados de contexto que o agente está configurado para usar, bem como quaisquer [instruções opcionais da etapa](#step-4-add-optional-step-instructions) que você adicionar à etapa.

## Artigos relacionados {#related-articles}

- [Visão geral do Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents)
- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)