---
nav_title: Implantar agentes
article_title: Implantar agentes personalizados
description: "Aprenda como utilizar agentes personalizados na Braze após criá-los."
alias: /deploying-agents/
page_order: 2
---

# Implantar agentes personalizados {#deploy-custom-agents}

> Aprenda como utilizar agentes personalizados em etapas do Canvas ou campos do catálogo após criá-los. Para uma introdução, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

## Agentes no Canvas {#agents-in-canvas}

Você pode usar agentes como etapas em uma jornada para personalizar mensagens ou guiar decisões em tempo real. Para etapas de configuração detalhadas, consulte [Etapa de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/).

### Casos de uso {#use-cases}

| Caso de uso | Descrição |
| --- | --- |
| Pontuação e qualificação de leads | Use uma etapa de agente para avaliar leads recebidos em uma escala (por exemplo, 1-10). Direcione usuários com pontuação acima de um limite para jornadas de nutrição e desqualifique leads com baixo potencial. |
| Personalização dinâmica de mensagens | Faça um agente gerar linhas de assunto, recomendações de produtos ou textos de mensagens com base em atributos do usuário ou comportamentos recentes. A resposta pode ser inserida diretamente em uma etapa de Mensagem. |
| Tratamento de feedback do cliente | Passe comentários dos clientes para um agente analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir benefícios. |
| Roteamento inteligente | Use saídas do agente (booleanas ou numéricas) para dividir usuários em diferentes jornadas do Canvas. Por exemplo, classifique usuários como "em risco" ou "saudáveis" e ajuste a cadência das mensagens de acordo. |
| Interpretação de pesquisas ou respostas | Permita que um agente analise respostas abertas de pesquisas ou campos de texto livre, retornando valores estruturados (por exemplo, categorizando intenção ou necessidade) que direcionam jornadas subsequentes. |
| Raciocínio em múltiplas etapas | Configure um agente para combinar campos de contexto e tomar decisões complexas, como recomendar a próxima melhor ação (e-mail, SMS ou contato humano) com base em múltiplos atributos do usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

## Agentes em catálogos {#agents-in-catalogs}

Você pode aplicar um agente a campos de catálogo para que ele gere ou calcule automaticamente valores para cada linha. O agente também será executado em novas linhas que forem adicionadas ao catálogo no futuro.

### Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Gerar descrições de produtos | Crie automaticamente textos curtos de marketing para novas entradas do catálogo — por exemplo, gerando uma descrição atraente a partir de dados estruturados do produto, como nome, categoria e características. |
| Enriquecer atributos de produtos | Preencha valores ausentes, como família de cores, estilo ou estação, com base no nome e nos detalhes do produto. Por exemplo, se o nome do produto for "Laguna Polarized Sunglasses", o agente poderia atribuir o estilo como "esportivo" e a família de cores como "azul". |
| Calcular campos derivados | Use campos existentes para gerar novos dados, como um "índice de adequação" com base em atributos ou uma "tag de popularidade" a partir de contagens de vendas e avaliações. |
| Categorizar ou etiquetar itens | Atribua tags para lógica de recomendação, para que modelos de personalização possam segmentar produtos de forma mais eficaz. Por exemplo, etiquete produtos como "ao ar livre", "pronto para festivais" ou "premium". |
| Localizar conteúdo | Traduza o texto do catálogo para outro idioma em campanhas globais, ou ajuste o tom e o tamanho para canais específicos de cada região. Por exemplo, traduza "Classic Clubmaster Sunglasses" para o espanhol como "Gafas de sol Classic Clubmaster", ou encurte descrições para campanhas de SMS. |
| Resumir avaliações ou feedback | Resuma sentimentos ou feedback em um novo campo, como atribuir pontuações de sentimento (Positivo, Neutro ou Negativo) ou criar um resumo curto como "A maioria dos clientes elogia o ajuste, mas menciona o envio lento." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso" }

### Etapas {#steps}

![Uma etapa de agente em um campo de catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para adicionar um agente ao seu campo de catálogo:

1. No seu catálogo, adicione um novo campo.
2. Selecione **Apply AI agent**.
3. Atribua um agente a este campo.
4. Selecione quais colunas devem ser passadas como entrada. Se nenhuma for selecionada, o agente terá acesso a todas as colunas do catálogo.
5. Decida se o agente deve recalcular os campos quando as linhas do catálogo forem atualizadas. Se você não selecionar esta opção, o agente será executado apenas uma vez por linha.
6. Selecione **Add fields** para implantar o agente e revisar as estimativas de custo. O modal **Cost estimation** mostra quantas vezes o agente será executado neste catálogo, aproximadamente igual ao número total de linhas. Para continuar, selecione **Confirm**.

### Como os agentes de catálogo funcionam {#how-catalog-agents-run}

Após o lançamento, o agente executa e avalia cada linha, usando as colunas selecionadas como contexto para produzir uma saída. Os agentes são executados em todas as novas linhas adicionadas após a implantação. Se você selecionou **Recalculate when catalog rows update**, todos os valores desse campo serão atualizados quando os campos de origem existentes mudarem.

Você pode atualizar e editar os campos do catálogo que usam agentes. Para remover um agente de uma coluna, desmarque **Apply AI agent**. Isso reverte a coluna para uma coluna não agente, e os campos mantêm os últimos valores que o agente aplicou na última execução no catálogo.

Referências circulares em catálogos não são suportadas. Portanto, o seguinte cenário não pode ocorrer:

- A Coluna Agente 1 usa a Coluna Agente 2 como entrada
- A Coluna Agente 2 usa a Coluna Agente 1 como entrada

![A opção de selecionar "Apply AI agent" para um campo de catálogo.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Agentes de catálogo estão limitados a processar valores de entrada de até 25 KB por linha.
{% endalert %}

#### Definir campos de resposta {#define-response-fields}

Se o seu agente usar [campos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas) como formato de saída, você pode selecionar, no campo **Response Field**, o campo correspondente do agente para usar no campo do catálogo.

Digamos que você tenha um agente que adiciona descrições de produtos a um catálogo com os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **description** | Texto |
| **confidence_score_out_of_ten** | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definir campos de resposta" }

Você pode adicionar um campo chamado **product_description** a um catálogo e selecionar **description** como o **Response Field** para preencher a coluna com as descrições do agente.

![Um campo "product_description" com o agente "Descriptor" aplicado. A saída "description" é selecionada como o campo de resposta.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Você também pode substituir manualmente a célula gerada pelo agente selecionando **Edit Item** e atualizando a descrição gerada pelo agente com suas edições. Para reverter à descrição gerada pelo agente, selecione o símbolo de atualizar na célula.

### Tratamento de erros em catálogos {#error-handling-in-catalogs}

- Invocações de catálogo com falha não são tentadas novamente, incluindo [erros de limite de taxa]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors) do provedor de LLM.
- Se a chamada de API para o provedor do modelo fundamental retornar qualquer outro erro, como um erro de chave de API inválida, o valor do campo não é atualizado.
- Você pode revisar os registros do agente para ver detalhes sobre execuções com falha.

## Monitore seu agente {#monitor-your-agent}

Na seção **Uso** do seu agente, você pode consultar e navegar até onde o agente está sendo usado ativamente em catálogos e Canvas.

![Seção de uso do agente que mostra dois agentes ativos e um agente inativo para Canvas.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Na seção **Registros** do seu agente, você pode monitorar chamadas reais do agente que ocorrem nos seus Canvas e catálogos. Você pode filtrar por informações como intervalo de datas, resultado (sucesso ou falha) ou local de chamada. Também pode selecionar **Exportar CSV** para exportar os registros mostrados apenas na página atual.

{% alert tip %}
Você também pode monitorar erros de limite de invocação diária no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/).
{% endalert %}

![Registros para um agente de pontuação de sentimento de IA.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Selecione **Visualizar** em uma chamada de agente específica para ver a entrada, a saída e o ID do usuário.

![O painel de detalhes para um agente de atribuição aleatória de esportes que mostra o prompt de entrada, a resposta de saída e um ID de usuário associado.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Use o Currents {#use-currents}

Você também pode usar esses eventos do Currents para acessar os esquemas de registro do Kafka:

- Eventos de execução de agente
- Eventos de invocação de ferramenta

Consulte o [glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) para mais detalhes.

## Artigos relacionados {#related-articles}

- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/agents/faq/)