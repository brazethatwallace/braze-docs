---
nav_title: Referência
article_title: Referência para agentes
description: "Detalhes de referência sobre os Agentes da Braze."
page_order: 3
---

# Referência para agentes {#reference-for-agents}

> Ao criar agentes personalizados, consulte este artigo para mais informações sobre configurações importantes, como instruções e esquemas de saída. Para a configuração passo a passo, veja [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Para uma introdução, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) e [Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Modelos {#models}

Quando você configura um agente, pode escolher o modelo que ele usa para gerar respostas. Você tem duas opções: usar um modelo fornecido pela Braze ou trazer sua própria chave de API.

{% alert important %}
O modelo **Auto** fornecido pela Braze é otimizado para modelos cujas capacidades de raciocínio são suficientes para realizar tarefas como busca em catálogo e associação a segmentos. Ao usar outros modelos, recomendamos testar para confirmar se o modelo funciona bem para o seu caso de uso. Pode ser necessário ajustar suas [instruções](#writing-instructions) para fornecer diferentes níveis de detalhe ou raciocínio passo a passo para modelos com diferentes velocidades e capacidades.
{% endalert %}

### Opção 1: Use um modelo fornecido pela Braze {#option-1-use-a-braze-powered-model}

Esta é a opção mais simples, sem configuração extra necessária. A Braze fornece acesso a grandes modelos de linguagem (LLMs) diretamente. Para usar esta opção, selecione **Auto**, que utiliza modelos Gemini.

{% alert important %}
Se você não vê **Braze Auto** como opção no menu suspenso **Model** ao criar um agente, entre em contato com seu gerente de sucesso do cliente para saber como se tornar elegível para usar o modelo Braze Auto.
{% endalert %}

### Opção 2: Traga sua própria chave de API {#option-2-bring-your-own-api-key}

Com esta opção, você pode conectar sua conta da Braze com provedores como OpenAI, Anthropic ou Google Gemini. Se você trouxer sua própria chave de API de um provedor de LLM, os custos de token são cobrados diretamente pelo seu provedor, não pela Braze.

Recomendamos testar rotineiramente os modelos mais recentes, pois modelos legados podem ser descontinuados ou depreciados após alguns meses. Certifique-se de que você tem créditos suficientes com seu provedor para executar seus agentes em escala. Você também pode se inscrever para receber notificações do Console do agente em [Preferências de notificação]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) para ser alertado quando a Braze detectar que um modelo não está mais disponível ou encontrar problemas de cobrança com seu provedor de LLM.

Para configurar isso:

1. Acesse **Integrações de parceiros** > **Parceiros de tecnologia** e encontre seu provedor.
2. Insira sua chave de API do provedor.
3. Selecione **Salvar**.

Em seguida, você pode voltar ao seu agente e selecionar o modelo.

Quando você usa um LLM fornecido pela Braze, os provedores desse modelo atuarão como Subprocessadores da Braze, sujeitos aos termos do Aditivo de Processamento de Dados (DPA) entre você e a Braze. Se você optar por trazer sua própria chave de API, o provedor da sua assinatura de LLM é considerado um Provedor Terceiro sob o contrato entre você e a Braze.

#### Níveis de raciocínio {#thinking-levels}

Alguns provedores de LLM podem permitir que você ajuste o nível de raciocínio de um modelo selecionado. Os níveis de raciocínio definem a amplitude de pensamento que o modelo usa antes de responder — desde respostas rápidas e diretas até cadeias mais longas de raciocínio. Isso afeta a qualidade da resposta, a latência e o uso de tokens.

| Nível | Quando usar |
|-------|-------------|
| **Mínimo** | Tarefas simples e bem definidas (como busca em catálogo, classificação direta). Respostas mais rápidas e menor custo. |
| **Baixo** | Tarefas que se beneficiam de um pouco mais de raciocínio, mas não precisam de análise profunda. |
| **Médio** | Tarefas com múltiplas etapas ou nuances (como analisar várias entradas para recomendar uma ação). |
| **Alto** | Raciocínio complexo, casos extremos ou quando você precisa que o modelo trabalhe as etapas antes de responder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Níveis de raciocínio" }

Recomendamos começar com **Mínimo** e testar as respostas do seu agente. Depois, você pode ajustar o nível de raciocínio para **Baixo** ou **Médio** se perceber que o agente está tendo dificuldade em fornecer respostas precisas. Em casos raros, um nível de raciocínio **Alto** pode ser necessário, embora usar esse nível possa resultar em altos custos de token e tempos de resposta mais longos ou maior risco de erros de timeout. Se seu agente está tendo dificuldade em equilibrar raciocínio com múltiplas etapas e tempos de resposta razoáveis, considere dividir seu caso de uso em mais de um agente que possam trabalhar juntos em um Canvas ou catálogo.

A Braze usa os mesmos intervalos de IP para chamadas de LLM de saída que para Connected Content. Os intervalos estão listados na [lista de permissão de IP de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting). Se seu provedor suporta lista de permissão de IP, você pode restringir a chave a esses intervalos para que apenas a Braze possa usá-la.

{% alert important %}
Quando você usa um LLM fornecido pela Braze, os provedores desse modelo atuarão como Subprocessadores da Braze, sujeitos aos termos do Aditivo de Processamento de Dados (DPA) entre você e a Braze. Se você optar por trazer sua própria chave de API, o provedor da sua assinatura de LLM é considerado um Provedor Terceiro sob o contrato entre você e a Braze.
{% endalert %}

#### Determinar qual modelo usar {#determine-which-model-to-use}

Cada provedor de LLM tem uma combinação ligeiramente diferente de capacidades de modelo, custos e níveis de raciocínio. Aqui estão algumas diretrizes gerais e melhores práticas:

- Para eficiência de custo, priorize testar modelos com menor custo de token antes dos modelos com custo mais alto. Ajuste para modelos de custo mais alto somente se os modelos de menor custo estiverem tendo dificuldade com o caso de uso ou gerando saídas inconsistentes ou imprecisas.
- Para eficiência de velocidade e desempenho, priorize testar níveis de raciocínio mais baixos antes dos mais altos. Ajuste para níveis de raciocínio mais altos somente se os níveis mais baixos estiverem tendo dificuldade com o caso de uso ou gerando saídas inconsistentes ou imprecisas.
- Se modelos de menor custo ou níveis de raciocínio mais baixos estiverem tendo dificuldade com o caso de uso ou gerando saídas inconsistentes ou imprecisas, considere ajustar para modelos de custo mais alto ou níveis de raciocínio mais altos.
- Durante os testes, certifique-se de equilibrar a confiabilidade e a precisão com o uso de tokens e a duração da invocação.
- Cada caso de uso pode ter um modelo e nível de raciocínio ideais diferentes. Recomendamos testar minuciosamente para verificar a qualidade consistente sem timeouts.

### Controles de fluxo de invocação {#invocation-flow-controls}

Os seguintes controles de fluxo de invocação se aplicam por espaço de trabalho:

- **Modelo fornecido pela Braze:** 5.000 invocações por minuto
- **Trazendo sua própria chave de API:** 5.000 invocações por minuto

Quando muitos usuários entram em uma etapa de agente ao mesmo tempo, a Braze enfileira as invocações de acordo com esses limites, então o processamento pode levar mais tempo durante envios de alto volume.

### Limites diários de invocação e créditos {#daily-invocation-and-credit-limits}

Cada agente tem um limite diário de invocações (padrão 250.000; máximo 1.000.000, a menos que seu contrato permita mais). Toda invocação — incluindo prévias do Console do agente e execuções de Canvas de teste que usam **Simulate response** — conta para esse limite.

No Console do agente, o **Limite diário de custo de créditos de ação** estima o máximo de créditos que um agente pode consumir por dia. A Braze multiplica a **taxa de crédito** por invocação do seu espaço de trabalho para o modelo selecionado pelo limite diário de invocações.

### Monitorar uso de créditos {#monitor-credit-usage}

Acesse **Configurações** > **Faturamento** > **Uso de créditos** > **Agent Console** para ver o consumo de créditos, contagens de invocações e taxas de crédito por agente.

As taxas de crédito vêm do seu contrato e aparecem no dashboard de [Uso de créditos]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) (guia **Credit Ratios** e guia **Agent Console**). A estimativa é atualizada quando você altera o modelo ou o limite de invocações.

Para gerenciar gastos, reduza o limite diário de invocações. Para modelos [BYO (traga o seu próprio)](#option-2-bring-your-own-api-key), você também pode escolher um modelo de menor custo ou reduzir o [nível de raciocínio](#thinking-levels) para diminuir os custos de token do provedor. O **Braze Auto** não suporta ajuste do nível de raciocínio.

### Erros de limite de frequência {#rate-limit-errors}

Se o provedor de LLM retornar um erro de limite de frequência durante uma invocação de agente de etapa do Canvas ou de agente de catálogo, a Braze tenta novamente a solicitação continuamente usando backoff exponencial até que a chamada seja bem-sucedida ou a Braze determine que ela não pode ser concluída.

Quando as tentativas do Canvas ou catálogo se esgotam, o painel de detalhes de **Logs** mostra **Error** e a mensagem do provedor (como `Rate limit exceeded`) em **Output**. As tentativas são visíveis nos logs, incluindo a primeira invocação, independentemente do seu eventual sucesso ou falha. Para um determinado usuário, se forem necessárias quatro novas tentativas para finalmente obter sucesso, você pode pesquisar o ID do usuário e ver todas as cinco (original mais quatro novas tentativas) nos **Logs**, e a original mais as três primeiras novas tentativas mostrarão **Error** com `Rate limit exceeded`.

![Detalhes do log do Console do agente mostrando um erro de limite de frequência excedido no campo Output.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Escrevendo instruções {#writing-instructions}

Instruções são as regras ou diretrizes que você dá ao agente (prompt do sistema). Elas definem como o agente deve se comportar cada vez que é executado. As instruções do sistema podem ter até 25 KB.

Se você criou seu agente com o [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) usando um [modelo inicial]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), revise as instruções pré-preenchidas e edite conforme necessário.

Aqui estão algumas melhores práticas gerais para você começar a criar prompts:

1. Comece com o fim em mente. Declare o objetivo primeiro.
2. Dê ao modelo um papel ou persona ("Você é um ...").
3. Defina contexto e restrições claros (público, comprimento, tom, formato).
4. Peça por estrutura ("Retorne JSON/lista com marcadores/tabela...").
5. Mostre, não conte. Inclua alguns exemplos de alta qualidade.
6. Divida tarefas complexas em etapas ordenadas ("Etapa 1... Etapa 2...").
7. Incentive o raciocínio ("Pense nas etapas internamente, depois forneça uma resposta final concisa," ou "explique brevemente sua decisão").
8. Pilote, inspecione e itere. Pequenos ajustes podem levar a grandes ganhos de qualidade.
9. Lide com os casos extremos, adicione barreiras de proteção e instruções de recusa.
10. Meça e documente o que funciona internamente para reutilização e escalabilidade.

### Exemplos {#examples}

Para configurações iniciais no Console do agente, veja [Modelos de agentes criados com o Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Para exemplos completos de instruções que você pode copiar ou adaptar, veja a [biblioteca de casos de uso para Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Exemplo | Categoria | Tipo de agente | O que faz |
| --- | --- | --- | --- |
| [Escrever mensagens personalizadas com base no contexto do usuário]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Geração de conteúdo | Agente de etapa do Canvas | Gera assunto/pré-cabeçalho de e-mail e título/corpo de push coordenados para usuários que pesquisaram, mas não reservaram. |
| [Analisar feedback do usuário para determinar próximos passos]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Padronização de dados | Agente de etapa do Canvas | Classifica o sentimento e o tópico de uma pesquisa pós-viagem e recomenda um próximo passo de CRM. |
| [Categorizar usuários em grupos de interesse a partir de atributos existentes]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Agente de afinidade | Agente de etapa do Canvas | Classifica usuários em grupos de interesse a partir de atributos e sinais de alta intenção, e recomenda a melhor próxima experiência ou item. |
| [Direcionar usuários para a jornada do Canvas mais relevante com base no comportamento recente]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Agente de afinidade | Agente de etapa do Canvas | Infere a motivação a partir do comportamento recente e retorna a melhor chave de rota para a próxima etapa do Canvas do usuário. |
| [Atribuir categorias de interesse aos usuários a partir de ações de alta intenção em tempo real]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Agente de afinidade | Agente de etapa do Canvas | Atribui categorias de interesse a partir de ações de alta intenção e recomenda a melhor próxima experiência ou item. |
| [Classificar mensagens recebidas quanto à intenção de cancelamento]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Classificação e roteamento | Agente de etapa do Canvas | Retorna um booleano estrito indicando se uma mensagem é uma solicitação de cancelamento. |
| [Padronizar mensagens recebidas em dados estruturados para automação]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Padronização de dados | Agente de etapa do Canvas | Normaliza SMS ou chat recebidos em intenção estruturada, entidades e sinalizadores de conformidade para automação downstream. |
| [Escrever descrições de alta conversão alinhadas com as diretrizes da marca]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Geração de conteúdo | Agente de catálogo | Gera descrições curtas e alinhadas à marca para cada linha do catálogo. |
| [Fornecer traduções com base no idioma usado por região]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Enriquecimento de catálogo | Agente de catálogo | Localiza strings de UI e marketing por localidade e limite de caracteres. |
| [Enriquecer itens do catálogo com descrições, categorias e tags]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Enriquecimento de catálogo | Agente de catálogo | Gera descrições aprimoradas, categorias e tags a partir dos dados existentes do item do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Resumo dos exemplos" }

### Usando Liquid {#using-liquid}

Incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) nas instruções do seu agente pode adicionar uma camada extra de personalização na resposta. Você pode especificar a variável Liquid exata que o agente recebe e incluí-la no contexto do seu prompt. Por exemplo, em vez de escrever explicitamente "nome", você pode usar o snippet Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Na seção **Logs** do **Agent Console**, você pode revisar os detalhes da entrada e saída do agente para entender qual valor é renderizado a partir do Liquid.

### Quais dados os agentes recebem {#what-data-agents-receive}

O contexto do agente não é uma memória conversacional aberta. Diferente de um assistente de chat, um agente só vê os dados que você passa explicitamente no momento da invocação — ele não navega por perfis de usuário, não infere campos ausentes e não avisa quando informações obrigatórias estão faltando.

Projete cada agente como um pipeline deliberado de entrada para saída. Conecte cada ponto de dados que o agente precisa usando um ou mais dos seguintes métodos:

1. **Liquid nas instruções:** Insira atributos de usuário ({% raw %}`{{${first_name}}}`{% endraw %}) e [variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) diretamente no prompt do agente.
2. **+ Contexto do agente:** Selecione catálogos, associação a segmentos, diretrizes da marca, **All Canvas Context** ou dados de interação do usuário no Console do agente.
3. [Etapas de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): Defina ou atualize variáveis `context.*` antes da execução de uma etapa de agente no Canvas.
4. **Contexto adicional na etapa de agente:** Passe quaisquer valores adicionais com template Liquid que não foram especificados pelos outros métodos para o agente no momento do envio a partir da configuração da etapa.

Certifique-se de inserir essas variáveis de contexto via template Liquid nas instruções do agente ou selecione **Add All Canvas Context**. Se um valor não for passado por um desses canais, o agente não o recebe. Liste as entradas obrigatórias nas suas instruções ou nos [pré-requisitos do caso de uso]({{site.baseurl}}/user_guide/brazeai/agents/use_cases), e verifique as entradas em **Agent Console** > **Logs** após os testes.

![Detalhes de um agente que tem Liquid em suas instruções.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Para agentes de catálogo, use **Fields** na seção **Output** em vez de esquema JSON; você ainda pode escrever instruções que peçam ao modelo uma saída em formato chave-valor correspondente aos nomes desses campos.

Para saber mais sobre as melhores práticas de prompting, consulte os guias dos seguintes provedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Saídas {#outputs}

Se você criou seu agente com o [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) usando um [modelo inicial]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator), revise o esquema de saída pré-preenchido e edite conforme necessário.

### Esquemas básicos {#basic-schemas}

Esquemas básicos são uma saída simples que um agente retorna. Pode ser uma string, um número, um booleano, um array de strings ou um array de números.

Por exemplo, se você quiser coletar pontuações de sentimento dos usuários a partir de uma pesquisa de feedback simples para determinar o nível de satisfação dos seus clientes após receberem um produto, você pode selecionar **Number** como esquema básico para estruturar o formato de saída.

{% alert important %}
Arrays estão disponíveis apenas para agentes de etapa do Canvas, não para agentes de catálogo.
{% endalert %}

![Console do agente com número selecionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Esquemas avançados {#advanced-schemas}

As opções de esquema avançado incluem estruturar campos manualmente ou usar JSON.

- **Fields:** Uma forma sem código de definir uma saída de agente que você pode usar de forma consistente.
- **JSON:** Uma abordagem com código para criar um formato de saída preciso, onde você pode aninhar variáveis e objetos dentro do esquema JSON. Disponível apenas para agentes de etapa do Canvas, não para agentes de catálogo.

Recomendamos usar esquemas avançados quando você quiser que o agente retorne uma estrutura de dados com múltiplos valores definidos de forma estruturada, em vez de uma saída de valor único. Isso permite que a saída seja melhor formatada como uma variável de contexto consistente.

### Saída de fallback {#fallback-output}

Valores de fallback estão disponíveis apenas para agentes de etapa do Canvas. Na seção **Output** do Console do agente para um agente de etapa do Canvas, você pode definir valores que a Braze usa quando uma invocação falha.

Para esquemas **JSON**, a Braze lê o esquema e gera um campo de entrada para cada propriedade, para que você possa definir um valor de fallback por chave. Para esquemas de **Fields**, você insere um valor de fallback para cada campo. Para esquemas básicos, você insere um único valor de fallback. Agentes de etapa do Canvas suportam Liquid em valores de fallback.

Para as etapas de configuração, veja [Configurar valores de fallback]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Para o comportamento em tempo de execução no Canvas, veja [Tratamento de erros e comportamento de fallback]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Por exemplo, você pode usar um formato de saída dentro de um agente destinado a criar um itinerário de viagem de exemplo para um usuário com base em um formulário que ele enviou. O formato de saída permite que você defina que toda resposta do agente deve retornar com valores para `tripStartDate`, `tripEndDate` e `destination`. Cada um desses valores pode ser extraído de variáveis de contexto e inserido em uma etapa de mensagem para personalização usando Liquid.

{% tabs %}
{% tab Fields %}

Se você quiser formatar respostas de uma pesquisa de feedback simples para determinar a probabilidade de os respondentes recomendarem o novo sabor de sorvete do seu restaurante, você pode configurar os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquemas avançados" }

![Console do agente mostrando três campos de saída para pontuação de probabilidade, explicação e pontuação de confiança.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON Schema %}

Se você quiser coletar feedback dos usuários sobre a experiência gastronômica mais recente na sua rede de restaurantes, você pode selecionar **JSON Schema** como formato de saída e inserir o seguinte JSON para retornar um objeto de dados que inclui uma variável de sentimento e uma variável de raciocínio.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## Catálogos e campos {#catalogs-and-fields}

Escolha catálogos específicos para um agente referenciar e forneça ao seu agente o contexto necessário para entender seus produtos e outros dados não relacionados ao usuário quando relevante. Os agentes usam ferramentas para encontrar apenas os itens relevantes e enviá-los ao LLM para minimizar o uso de tokens. Para uma melhor recuperação de catálogo, crie uma [fonte de conhecimento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) e adicione-a como contexto do agente em vez de anexar o catálogo diretamente.

![O catálogo "restaurants" e a coluna "Loyalty_Program" selecionados para o agente pesquisar.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Quando você implanta um agente de catálogo em um campo de catálogo, ative o controle de entrada obrigatória e escolha quais colunas selecionadas são obrigatórias para execução antes que o agente seja invocado. O agente pula uma linha somente quando uma dessas colunas obrigatórias está em branco ou ausente — por exemplo, um campo `gender` que ainda não foi preenchido. As colunas selecionadas começam como obrigatórias por padrão, mas você pode remover colunas que podem estar vazias sem bloquear a execução. Isso evita desperdício de tokens com dados incompletos.

Agentes de catálogo também respeitam a ordem das colunas quando os campos de entrada dependem uns dos outros. Se a coluna D deve ser gerada a partir das colunas B e C, o agente não executa na coluna D até que B e C contenham valores para aquela linha.

Para cenários de implantação e exemplos, veja [Usar agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) e [Melhores práticas para agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Contexto de associação a segmentos {#segment-membership-context}

Você pode selecionar até cinco segmentos para o agente verificar a associação de cada usuário quando o agente é usado em um Canvas. Digamos que seu agente tenha a associação a segmentos selecionada para um segmento "Loyalty Users", e o agente é usado em um Canvas. Quando os usuários entram em uma etapa de agente, o agente pode verificar se cada usuário é membro de cada segmento que você especificou no Console do agente e usar a associação (ou não associação) de cada usuário como contexto para o LLM.

![O segmento "Loyalty Users" selecionado para acesso de associação do agente.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Diretrizes da marca {#brand-guidelines}

Você pode selecionar [diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) para o seu agente seguir em suas respostas. Por exemplo, se você quiser que seu agente gere textos de SMS para incentivar os usuários a se inscreverem em uma academia, você pode usar este campo para referenciar sua diretriz motivacional predefinida.

## Histórico de interação específico do usuário {#user-history}

Os dados de interação de um usuário incluem aberturas, cliques e dados de conversão recentes de Campaigns e Canvas. Por exemplo, você pode incluir esse contexto para um agente referenciar quando ele é avaliado em um Canvas. O histórico de interação específico do usuário também pode ajudar a influenciar um agente quando sua função é escrever textos de mensagens personalizadas.

## Histórico de versões {#version-history}

O Console do agente registra uma nova versão cada vez que você salva alterações no agente. A guia **Histórico de versões** lista todas as versões salvas e as edições entre os salvamentos.

1. Abra o agente no Console do agente.
2. Selecione a guia **Histórico de versões**.
3. Selecione uma versão para revisar sua configuração.

Para inspecionar o que mudou em uma versão, selecione **View**. A Braze exibe um diff inline no estilo de código que destaca adições e exclusões. O conteúdo excluído aparece com estilo de tachado em vermelho.

Se você precisar recuperar instruções de uma versão anterior, abra **View** para essa versão, copie o texto da instrução e cole no campo **Instructions** atual.

{% alert tip %}
Na visualização de diff inline, pressione <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) ou <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows) para selecionar todas as instruções sem a marcação de exclusão em vermelho, para que você possa copiar e recuperar o texto limpo.
{% endalert %}

## Duplicar agentes {#duplicate-agents}

Duplique um agente para testar melhorias ou iterações lado a lado com o original. Use o [histórico de versões](#version-history) para revisar ou recuperar configurações anteriores. Para duplicar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Duplicar**.

## Arquivar agentes {#archive-agents}

À medida que você cria mais agentes personalizados, pode organizar a página **Gerenciamento de agentes** arquivando agentes que não estão sendo usados ativamente. Para arquivar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Arquivar**.