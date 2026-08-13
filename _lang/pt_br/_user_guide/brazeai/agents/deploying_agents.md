---
nav_title: Implantar agentes
article_title: Implantar agentes personalizados
description: "Aprenda como utilizar agentes personalizados na Braze após criá-los."
alias: /deploying-agents/
page_order: 2
---

# Implantar agentes personalizados {#deploy-custom-agents}

> Depois de [criar um agente]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents), use esta página para saber onde e como implantá-lo na Braze. O tipo de agente que você escolhe no momento da criação — agente de Canvas ou agente de catálogo — determina onde o agente pode ser executado. Para uma introdução, consulte [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents).

## Tipos de agentes personalizados {#types-of-custom-agents}

Os agentes personalizados são implantados em diferentes partes da Braze, dependendo do tipo. Use a tabela a seguir para encontrar o caminho de implantação correto para o seu agente.

| Tipo de agente | Implantado em | Executa quando | Seção |
| --- | --- | --- | --- |
| Agente de etapa do Canvas | [Etapa de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) no Canvas | Um usuário entra na etapa | [Usar agentes de etapa do Canvas](#use-canvas-step-agents) |
| Agente de catálogo | Campo de catálogo | Uma linha do catálogo é criada ou atualizada | [Usar agentes de catálogo](#use-catalog-agents) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tipos de agentes personalizados" }

Você seleciona o tipo de agente no **Agent Console** ao criar o agente. Para as etapas de configuração, consulte [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-1-choose-an-agent-type).

## Práticas recomendadas {#best-practices}

Priorize casos de uso de alto valor em que os agentes possam gerar o maior retorno sobre o investimento (ROI) e escolha públicos com maior probabilidade de resposta. Um público menor e com alta oportunidade frequentemente supera um público grande com baixa oportunidade.

Para agentes de etapa do Canvas, comece com usuários que apresentam sinais fortes — como buscas recentes, alto engajamento ou dados de perfil ricos — antes de expandir para Segments mais amplos. Para agentes de catálogo, priorize linhas em que as colunas de entrada necessárias já estejam preenchidas, para que cada invocação tenha contexto suficiente para produzir resultados úteis.

Para testar o ROI em pequena escala antes de lançar um agente de forma ampla, use uma etapa de [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) para que apenas parte do seu público entre na ramificação que contém a etapa do agente.

### Escale após um teste bem-sucedido {#scale-after-a-successful-test}

Depois que um teste em pequena escala (por exemplo, uma ramificação de [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)) apresentar qualidade e ROI aceitáveis, planeje lançar o agente para todo o seu público-alvo (não apenas o grupo de teste) para que todos os usuários elegíveis se beneficiem.

Antes de escalar, considere o seguinte:

- Aumente o limite diário de invocações do agente no Agent Console para que ele possa lidar com o volume total do seu público. O padrão é 250.000; você pode aumentá-lo para até 1.000.000 (ou mais, com o seu gerente de sucesso do cliente). Consulte [Limites diários de invocação e créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Revise a estimativa de **Daily action credit cost limit** e confirme que o seu espaço de trabalho tem créditos suficientes para envios em escala total.
- Remova ou reconfigure o experimento para que todo o público-alvo entre na etapa do agente (ou promova a variante vencedora para a jornada principal).

Escalar para o público completo aumenta o consumo de créditos proporcionalmente. Monitore o uso em **Settings** > **Billing** > **Credits Usage** > **Agent Console** após o lançamento.

## Usar agentes de etapa do Canvas {#use-canvas-step-agents}

Depois de criar um agente de etapa do Canvas, adicione-o a um Canvas como uma etapa de agente para personalizar mensagens ou orientar a tomada de decisões em tempo real.

### Como funciona {#how-it-works}

Quando um usuário chega a uma etapa de agente em um Canvas, a Braze envia os dados de entrada que você configurou para o seu agente. O agente processa a entrada usando seu modelo e instruções e, em seguida, retorna uma saída armazenada na variável de saída que você definiu na etapa. Você pode usar essa saída para tomada de decisões, personalização ou processamento posterior.

As etapas de agente usam [variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) para ingerir contexto relevante e gerar uma variável que pode ser usada no Canvas. Para pré-requisitos e uma referência completa, consulte [Etapa de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Adicionar uma etapa de agente {#add-an-agent-step}

Para adicionar um agente ao seu Canvas:

1. Arraste e solte o componente **Agente** da barra lateral, ou selecione o botão <i class="fas fa-plus-circle" aria-label="Adicionar etapa"></i> de adição na parte inferior de uma etapa e selecione **Agente**.
2. Selecione o agente que processará os dados nesta etapa.
3. Defina o nome da variável de saída. O tipo de dado de saída é definido no [Console de Agentes]({{site.baseurl}}/user_guide/brazeai/agents).
4. (Opcional) Adicione valores de contexto adicionais para o agente referenciar durante a execução. Isso pode incluir variáveis Liquid extras ou contexto do Canvas que você ainda não vinculou na configuração do agente — por exemplo, valores que você deseja passar apenas no momento do envio a partir desta etapa.
5. Teste o agente usando a prévia na etapa ou [Testar Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps) para percorrer a jornada completa do usuário.

Para tipos de dados de saída, templates Liquid e capturas de tela, consulte [Etapa de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Casos de uso {#use-cases}

| Caso de uso | Descrição |
| --- | --- |
| Pontuação e qualificação de leads | Use uma etapa de agente para avaliar leads recebidos em uma escala (por exemplo, 1-10). Direcione usuários com pontuação acima de um limite para jornadas de nutrição, enquanto desqualifica leads com baixo ajuste. |
| Personalização dinâmica de mensagens | Faça com que um agente gere linhas de assunto, recomendações de produtos ou textos de mensagens com base em atributos do usuário ou comportamentos recentes. A resposta pode ser inserida diretamente em uma etapa de mensagem. |
| Tratamento de feedback de clientes | Passe comentários de clientes para um agente analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir benefícios. |
| Roteamento inteligente | Use saídas do agente (booleanas ou numéricas) para dividir usuários em diferentes jornadas do Canvas. Por exemplo, classifique usuários como "em risco" ou "saudáveis" e ajuste a cadência de envio de mensagens de acordo. |
| Interpretação de pesquisas ou respostas | Permita que um agente analise respostas abertas de pesquisas ou campos de texto livre, retornando valores estruturados (por exemplo, categorizando intenção ou necessidade) que direcionam jornadas posteriores. |
| Raciocínio em múltiplas etapas | Configure um agente para combinar campos de contexto e tomar decisões complexas, como recomendar a próxima melhor ação (e-mail, SMS ou contato humano) com base em múltiplos atributos do usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

### Usar a saída do agente {#use-the-agent-output}

Depois que o agente é executado, use a variável de saída no seu Canvas:

- **Roteamento de jornada:** Direcione usuários por diferentes jornadas do Canvas com base na resposta do agente. Use [jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [divisões de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) com saídas numéricas, booleanas ou estruturadas.
- **Personalização:** Insira a resposta do agente diretamente em uma etapa de mensagem usando Liquid.
- **Processamento de dados de usuários:** Analise e padronize dados de usuários e, em seguida, armazene-os no perfil de usuário (por exemplo, com uma etapa de [atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)) ou envie-os usando um webhook.

Para exemplos, consulte [Como funciona]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#how-it-works) em Etapa de agente.

### Tratamento de erros e comportamento de fallback {#fallback-behavior}

O seguinte se aplica a agentes de etapa do Canvas em uma [etapa de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

- Se o modelo conectado retornar um [erro de limite de frequência]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) do provedor de LLM, a Braze tenta novamente a solicitação continuamente usando backoff exponencial até que a chamada seja bem-sucedida ou a Braze determine que não pode ser concluída; os usuários então prosseguem para a próxima etapa do Canvas.
- Para outras falhas (como timeout ou chave de API inválida), a variável de saída é definida como `null`, a menos que o agente tenha [valores de fallback configurados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) no Console de Agentes.
- Se um agente atingir seu limite diário de invocações, a Braze também aplica os valores de fallback configurados quando presentes; caso contrário, a variável de saída é definida como `null`.

Quando valores de fallback são configurados, a Braze os aplica para erros não passíveis de nova tentativa e para falhas de limite diário. A Braze renderiza o fallback com Liquid por usuário e armazena o resultado na variável de saída da etapa de agente. Sem valores de fallback, essas falhas definem a variável de saída como `null`. Se você preferir configurar valores padrão específicos da etapa em etapas de mensagem em vez de fallbacks no Console de Agentes, ainda pode usar [valores padrão de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) posteriormente. Para isso, deixe os fallbacks em branco na seção **Saída** da configuração do agente para que os valores padrão de Liquid possam ser aplicados quando o agente retornar null.

Erros de limite de frequência, indisponibilidade do modelo e falhas de limite diário de invocações não consomem créditos da Braze. Timeouts consomem créditos. Consulte [Quando os créditos são consumidos]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

- As respostas são armazenadas em cache para entradas idênticas e podem ser reutilizadas para invocações idênticas repetidas dentro de alguns minutos. Respostas em cache ainda contam para o total e as invocações diárias.
- As etapas de agente podem levar tempo para processar um grande lote de usuários. A Braze enfileira as invocações de acordo com os [controles de fluxo de invocação]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls), então os usuários podem permanecer pendentes durante envios de alto volume.

Para detalhes de configuração e execução da etapa de agente, consulte [Tratamento de erros]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#error-handling) em Etapa de agente. Para mais detalhes, consulte [Tratamento de erros]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) em Braze Agents.

## Usar Catalog Agents {#use-catalog-agents}

Depois de criar um Catalog Agent, aplique-o a um campo do catálogo para gerar ou calcular valores automaticamente para cada linha. O agente também é executado em novas linhas adicionadas ao catálogo no futuro.

### Como funciona

Após o lançamento, o agente é executado e avalia cada linha, considerando as colunas selecionadas em seu contexto para produzir uma saída. Os agentes são executados em todas as novas linhas adicionadas após a implantação do agente. Se você selecionou **Recalculate when catalog rows update**, todos os valores desse campo serão atualizados se os campos de origem existentes forem alterados.

Ao configurar as colunas de entrada para um Catalog Agent, ative o controle no produto que marca quais colunas selecionadas são obrigatórias antes que o agente seja invocado (os rótulos podem variar ligeiramente por espaço de trabalho). Com esse controle ativado, escolha o subconjunto de colunas que devem conter valores — as colunas selecionadas começam como obrigatórias por padrão, mas você pode remover colunas que podem ficar vazias sem bloquear o agente. O agente pula uma linha apenas quando uma coluna que você deixou como obrigatória está em branco ou ausente — por exemplo, um campo `gender` que não foi preenchido. Executar sem o contexto obrigatório desperdiça tokens e pode produzir saídas de baixa qualidade.

Os Catalog Agents também respeitam dependências entre colunas. Se a coluna D é gerada a partir das colunas B e C, o agente não é executado na coluna D para uma linha até que B e C contenham valores para essa linha.

Você pode atualizar e editar os campos do seu catálogo que usam agentes. Para remover um agente de uma coluna, desmarque **Apply AI agent**. Isso reverte a coluna para uma coluna não agêntica, e os campos mantêm os últimos valores que o agente aplicou na última vez que foi executado no catálogo.

Referências circulares em catálogos não são suportadas, o que significa que o seguinte cenário não pode ocorrer:

- A Coluna Agêntica 1 usa a Coluna Agêntica 2 como entrada
- A Coluna Agêntica 2 usa a Coluna Agêntica 1 como entrada

### Adicionar um agente a um campo do catálogo {#add-an-agent-to-a-catalog-field}

![Uma etapa de agente em um campo do catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Para adicionar um agente ao campo do seu catálogo:

1. No seu catálogo, adicione um novo campo.
2. Selecione **Apply AI agent**.
3. Atribua um agente a esse campo.
4. Selecione quais colunas devem ser passadas como entrada. Se nenhuma for selecionada, o agente terá acesso a todas as colunas do catálogo.
5. (Opcional) Ative **Only run when required columns have values** para pular linhas em que uma ou mais colunas de entrada selecionadas estejam em branco. Quando essa opção estiver ativada, selecione quais das colunas de entrada devem estar preenchidas para que o agente seja executado — todas as colunas selecionadas começam como obrigatórias por padrão, mas você pode remover qualquer uma que possa ficar vazia sem bloquear a execução.
6. Decida se o agente deve recalcular os campos quando as linhas do catálogo forem atualizadas. Se você não selecionar essa opção, o agente será executado apenas uma vez por linha.
7. Selecione **Add fields** para implantar o agente e revisar as estimativas de custo. O modal **Cost estimation** mostra quantas vezes o agente será executado nesse catálogo, aproximadamente igual ao número total de linhas. Para continuar, selecione **Confirm**.

### Práticas recomendadas para Catalog Agents {#catalog-agent-best-practices}

Planeje quais colunas o agente precisa antes de aplicá-lo a um campo do catálogo. Depois de ativar os controles de entrada obrigatória para o campo, selecione as colunas que contêm os dados que seu agente deve ler e, em seguida, desmarque qualquer coluna que possa ficar vazia sem bloquear a execução. O agente pula uma linha apenas quando uma coluna que você deixou marcada como obrigatória está em branco.

Não deixe uma coluna marcada como obrigatória se você espera que ela fique vazia em algumas linhas e ainda deseja que o agente seja executado — remova-a do conjunto obrigatório. Pular linhas incompletas evita o uso incorreto de tokens e mantém a qualidade da saída alta.

| Cenário | O que acontece |
| --- | --- |
| Linhas pré-preenchidas com placeholders | Se você adicionar linhas ao catálogo com apenas um ID e um nome de fundo, e preencher outras colunas depois, o agente pula essas linhas até que as colunas de entrada obrigatórias tenham valores. |
| Agente aplicado após as linhas existirem | Quando você aplica um agente a um campo em um catálogo que já possui linhas, o agente avalia cada linha, mas é executado apenas onde as colunas de entrada obrigatórias estão preenchidas. |
| Catálogo parcialmente completo | Por exemplo, um catálogo com 100 linhas em que `leader` está preenchido para as entradas de 2026, mas outras linhas contêm apenas um ID e nome do fundo com campos em branco. O agente é executado nas linhas com um valor de `leader` e pula as linhas sem ele quando `leader` permanece obrigatório. |
| Colunas dependentes | Se a coluna 3 depende das colunas 1 e 2, o agente não grava na coluna 3 até que as colunas 1 e 2 tenham valores para essa linha. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Práticas recomendadas para Catalog Agents" }

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Gerar descrições de produtos | Crie automaticamente textos curtos de marketing para novas entradas do catálogo, por exemplo, gerando uma descrição atraente a partir de dados estruturados do produto, como nome, categoria e recursos. |
| Enriquecer atributos de produtos | Preencha valores ausentes, como família de cores, estilo ou temporada, com base no nome e nos detalhes do produto. Por exemplo, se o nome do produto for "Laguna Polarized Sunglasses", o agente poderia atribuir o estilo como "sport" e a família de cores como "blue". |
| Calcular campos derivados | Use campos existentes para gerar novos dados, como uma "pontuação de adequação" com base em atributos ou uma "tag de popularidade" a partir de vendas e contagens de avaliações. |
| Categorizar ou etiquetar itens | Atribua tags para lógica de recomendação, para que os modelos de personalização possam segmentar produtos de forma mais eficaz. Por exemplo, etiquetar produtos como "outdoor", "festival-ready" ou "premium". |
| Localizar conteúdo | Traduza o texto do catálogo para outro idioma para campanhas globais, ou ajuste o tom e o comprimento para canais específicos de cada região. Por exemplo, traduzir "Classic Clubmaster Sunglasses" para espanhol como "Gafas de sol Classic Clubmaster", ou encurtar descrições para campanhas de SMS. |
| Resumir avaliações ou feedback | Resuma sentimentos ou feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um breve resumo de texto como "A maioria dos clientes menciona ótimo caimento, mas observa envio lento." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

### Definir campos de resposta {#define-response-fields}

Se o seu agente usa [campos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents?tab=fields#advanced-schemas) como formato de saída, você pode selecionar o campo correspondente do agente em **Response Field** para usar no campo do catálogo.

Digamos que você tenha um agente que adiciona descrições de produtos a um catálogo com os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **description** | Texto |
| **confidence_score_out_of_ten** | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definir campos de resposta" }

Você pode adicionar um campo chamado **product_description** a um catálogo e selecionar **description** como o **Response Field** para preencher a coluna com as descrições do agente.

![Um campo "product_description" com o agente "Descriptor" aplicado. A saída "description" está selecionada como o campo de resposta.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Você também pode substituir manualmente a célula gerada pelo agente selecionando **Edit Item** e atualizando a descrição gerada pelo agente com suas edições. Para reverter para a descrição gerada pelo agente, selecione o símbolo de atualização na célula.

### Tratamento de erros {#error-handling}

- Se o provedor de LLM retornar um [erro de limite de frequência]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors), a Braze tenta novamente a solicitação continuamente usando backoff exponencial até que a chamada seja bem-sucedida ou a Braze determine que não pode ser concluída.
- Para outras falhas (como timeout ou chave de API inválida), o valor do campo do catálogo não é atualizado. Os Catalog Agents não suportam a configuração de valores de fallback no Agent Console.
- Você pode revisar os logs do agente para obter detalhes sobre execuções com falha.
- Os Catalog Agents são limitados ao processamento de valores de entrada de até 25 KB por linha.

## Monitore seu agente {#monitor-your-agent}

O monitoramento funciona da mesma forma, independentemente de o agente ser executado em Canvas ou em catálogos.

Na seção **Uso** do seu agente, você pode consultar e navegar até onde o agente está sendo usado ativamente em catálogos e Canvas.

![Seção de uso do agente mostrando dois agentes ativos e um agente inativo para Canvas.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Na seção **Logs** do seu agente, você pode monitorar as chamadas reais do agente que ocorrem nos seus Canvas e catálogos. Você pode filtrar por informações como intervalo de datas, resultado (sucesso ou falha) ou local de chamada. Também é possível selecionar **Exportar CSV** para exportar os logs exibidos apenas na página atual.

{% alert tip %}
Você também pode monitorar erros de limite de invocação diária no [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).
{% endalert %}

![Logs de um agente AI Sentiment Score.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Selecione **Visualizar** para uma chamada específica do agente para ver a entrada, a saída e o ID do usuário.

![Painel de detalhes de um agente Random Sports Assignment mostrando o prompt de entrada, a resposta de saída e um ID de usuário associado.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

Para agentes de etapa do Canvas, os logs incluem uma seção **Fallback Output** que mostra qualquer saída de fallback usada quando a invocação apresentou erro.

### Use o Currents {#use-currents}

Você também pode usar esses eventos do Currents para acessar os esquemas de registro do Kafka:

- Eventos de execução do agente
- Eventos de invocação de ferramenta

Consulte o [Glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para mais detalhes.

## Artigos relacionados {#related-articles}

- [Etapa de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)
- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/agents/faq)