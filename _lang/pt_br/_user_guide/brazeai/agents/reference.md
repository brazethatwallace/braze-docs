---
nav_title: Referência
article_title: Referência para agentes
description: "Detalhes de referência sobre os Agentes da Braze."
page_order: 3
---

# Referência para agentes {#reference-for-agents}

> Ao criar agentes personalizados, consulte este artigo para mais informações sobre configurações importantes, como instruções e esquemas de saída. Para a configuração passo a passo, veja [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/). Para uma introdução, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) e [Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/agents/faq/).

## Modelos {#models}

Quando você configura um agente, pode escolher o modelo que ele usa para gerar respostas. Você tem duas opções: usar um modelo fornecido pela Braze ou trazer sua própria chave de API.

{% alert important %}
O modelo **Auto** fornecido pela Braze é otimizado para modelos cujas capacidades de raciocínio são suficientes para realizar tarefas como busca em catálogo e associação a Segments. Ao usar outros modelos, recomendamos testar para confirmar se o modelo funciona bem para o seu caso de uso. Pode ser necessário ajustar suas [instruções](#writing-instructions) para fornecer diferentes níveis de detalhe ou raciocínio passo a passo para modelos com diferentes velocidades e capacidades.
{% endalert %}

### Opção 1: Use um modelo fornecido pela Braze {#option-1-use-a-braze-powered-model}

Esta é a opção mais simples, sem configuração extra necessária. A Braze fornece acesso a grandes modelos de linguagem (LLMs) diretamente. Para usar esta opção, selecione **Auto**, que utiliza modelos Gemini.

{% alert important %}
Se você não vê **Braze Auto** como opção no menu suspenso **Model** ao criar um agente, entre em contato com seu gerente de sucesso do cliente para saber como se tornar elegível para usar o modelo Braze Auto.
{% endalert %}

### Opção 2: Traga sua própria chave de API {#option-2-bring-your-own-api-key}

Com esta opção, você pode conectar sua conta da Braze com provedores como OpenAI, Anthropic ou Google Gemini. Se você trouxer sua própria chave de API de um provedor de LLM, os custos de token são cobrados diretamente pelo seu provedor, não pela Braze.

Recomendamos testar rotineiramente os modelos mais recentes, pois modelos legados podem ser descontinuados ou depreciados após alguns meses. Certifique-se de que você tem créditos suficientes com seu provedor para executar seus agentes em escala. Você também pode se inscrever para receber notificações do Console do agente em [Preferências de notificação]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences/) para ser alertado quando a Braze detectar que um modelo não está mais disponível ou encontrar problemas de cobrança com seu provedor de LLM.

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

A Braze usa os mesmos intervalos de IP para chamadas de LLM de saída que para Conteúdo conectado. Os intervalos estão listados na [lista de permissão de IP de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#connected-content-ip-allowlisting). Se seu provedor suporta lista de permissão de IP, você pode restringir a chave a esses intervalos para que apenas a Braze possa usá-la.

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

### Erros de limite de taxa {#rate-limit-errors}

Se o provedor de LLM retornar um erro de limite de taxa durante uma **etapa de agente no Canvas**, a Braze tenta novamente a solicitação continuamente usando backoff exponencial até que a chamada seja bem-sucedida ou a Braze determine que ela não pode ser concluída. **Agentes de catálogo** não tentam novamente invocações com limite de taxa.

Quando as tentativas do Canvas se esgotam, o painel de detalhes de **Logs** mostra **Error** e a mensagem do provedor (como `Rate limit exceeded`) em **Output**. As tentativas são visíveis nos logs, incluindo a primeira invocação, independentemente do seu eventual sucesso ou falha. Para um determinado usuário, se forem necessárias quatro novas tentativas para finalmente obter sucesso, você pode pesquisar o ID do usuário e ver todas as cinco (original mais quatro novas tentativas) nos **Logs**, e a original mais as três primeiras novas tentativas mostrarão **Error** com `Rate limit exceeded`.

![Detalhes do log do Console do agente mostrando um erro de limite de taxa excedido no campo Output.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Escrevendo instruções {#writing-instructions}

Instruções são as regras ou diretrizes que você dá ao agente (prompt do sistema). Elas definem como o agente deve se comportar cada vez que é executado. As instruções do sistema podem ter até 25 KB.

Se você criou seu agente com o [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) usando um [modelo inicial]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator), revise as instruções pré-preenchidas e edite conforme necessário.

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

Para configurações iniciais no Console do agente, veja [Modelos de agentes criados com o Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator). Para exemplos completos de instruções que você pode copiar ou adaptar, veja a [biblioteca de casos de uso para Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/use_cases/).

### Usando Liquid {#using-liquid}

Incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) nas instruções do seu agente pode adicionar uma camada extra de personalização na resposta. Você pode especificar a variável Liquid exata que o agente recebe e incluí-la no contexto do seu prompt. Por exemplo, em vez de escrever explicitamente "nome", você pode usar o trecho Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Na seção **Logs** do **Console do agente**, você pode revisar os detalhes da entrada e saída do agente para entender qual valor é renderizado a partir do Liquid.

![Detalhes de um agente que tem Liquid em suas instruções.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Para agentes de catálogo, use **Campos** na seção **Saída** em vez de esquema JSON; você ainda pode escrever instruções que peçam ao modelo uma saída em formato chave-valor correspondente aos nomes desses campos.

Para saber mais sobre as melhores práticas de prompting, consulte os guias dos seguintes provedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Saídas {#outputs}

Se você criou seu agente com o [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) usando um [modelo inicial]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator), revise o esquema de saída pré-preenchido e edite conforme necessário.

### Esquemas básicos {#basic-schemas}

Esquemas básicos são uma saída simples que um agente retorna. Pode ser uma string, um número, um booleano, um array de strings ou um array de números.

Por exemplo, se você quiser coletar pontuações de sentimento dos usuários a partir de uma pesquisa de feedback simples para determinar o nível de satisfação dos seus clientes após receberem um produto, você pode selecionar **Number** como esquema básico para estruturar o formato de saída.

{% alert important %}
Arrays estão disponíveis apenas para agentes de Canvas, não para agentes de catálogo.
{% endalert %}

![Console do agente com número selecionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Esquemas avançados {#advanced-schemas}

As opções de esquema avançado incluem estruturar campos manualmente ou usar JSON.

- **Campos:** Uma forma sem código de definir uma saída de agente que você pode usar de forma consistente.
- **JSON:** Uma abordagem com código para criar um formato de saída preciso, onde você pode aninhar variáveis e objetos dentro do esquema JSON. Disponível apenas para agentes de Canvas, não para agentes de catálogo.

Recomendamos usar esquemas avançados quando você quiser que o agente retorne uma estrutura de dados com múltiplos valores definidos de forma estruturada, em vez de uma saída de valor único. Isso permite que a saída seja melhor formatada como uma variável de contexto consistente.

### Saída de fallback {#fallback-output}

Valores de fallback estão disponíveis apenas para **agentes de etapa do Canvas**. Na seção **Saída** do Console do agente para um agente de Canvas, você pode definir valores que a Braze usa quando uma invocação falha.

Para esquemas **JSON**, a Braze lê o esquema e gera um campo de entrada para cada propriedade, para que você possa definir um valor de fallback por chave. Para esquemas de **Campos**, você insere um valor de fallback para cada campo. Para esquemas básicos, você insere um único valor de fallback. Agentes de Canvas suportam Liquid em valores de fallback.

Para as etapas de configuração, veja [Configurar valores de fallback]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#configure-fallback-values). Para o comportamento em tempo de execução no Canvas, veja [Tratamento de erros e comportamento de fallback]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#fallback-behavior).

Por exemplo, você pode usar um formato de saída dentro de um agente destinado a criar um itinerário de viagem de exemplo para um usuário com base em um formulário que ele enviou. O formato de saída permite que você defina que toda resposta do agente deve retornar com valores para `tripStartDate`, `tripEndDate` e `destination`. Cada um desses valores pode ser extraído de variáveis de contexto e inserido em uma etapa de Mensagem para personalização usando Liquid.

{% tabs %}
{% tab Campos %}

Se você quiser formatar respostas de uma pesquisa de feedback simples para determinar a probabilidade de os respondentes recomendarem o novo sabor de sorvete do seu restaurante, você pode configurar os seguintes campos para estruturar o formato de saída:

| Nome do campo | Valor |
| --- | --- |
| **likelihood_score** | Número |
| **explanation** | String |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquemas avançados" }

![Console do agente mostrando três campos de saída para pontuação de probabilidade, explicação e pontuação de confiança.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab Esquema JSON %}

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

Escolha catálogos específicos para um agente referenciar e forneça ao seu agente o contexto necessário para entender seus produtos e outros dados não relacionados ao usuário quando relevante. Os agentes usam ferramentas para encontrar apenas os itens relevantes e enviá-los ao LLM para minimizar o uso de tokens.

![O catálogo "restaurants" e a coluna "Loyalty_Program" selecionados para o agente pesquisar.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Quando você implanta um agente de catálogo em um campo de catálogo, ative o controle de entrada obrigatória e escolha quais colunas selecionadas são **obrigatórias para execução** antes que o agente seja invocado. O agente pula uma linha somente quando uma dessas colunas obrigatórias está em branco ou ausente — por exemplo, um campo `gender` que ainda não foi preenchido. As colunas selecionadas começam como obrigatórias por padrão, mas você pode remover colunas que podem estar vazias sem bloquear a execução. Isso evita desperdício de tokens com dados incompletos.

Agentes de catálogo também respeitam a ordem das colunas quando os campos de entrada dependem uns dos outros. Se a coluna D deve ser gerada a partir das colunas B e C, o agente não executa na coluna D até que B e C contenham valores para aquela linha.

Para cenários de implantação e exemplos, veja [Usar agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#use-catalog-agents) e [Melhores práticas para agentes de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#catalog-agent-best-practices).

## Contexto de associação a Segments {#segment-membership-context}

Você pode selecionar até cinco Segments para o agente verificar a associação de cada usuário quando o agente é usado em um Canvas. Digamos que seu agente tenha a associação a Segments selecionada para um Segment "Loyalty Users", e o agente é usado em um Canvas. Quando os usuários entram em uma etapa de agente, o agente pode verificar se cada usuário é membro de cada Segment que você especificou no Console do agente e usar a associação (ou não associação) de cada usuário como contexto para o LLM.

![O Segment "Loyalty Users" selecionado para acesso de associação do agente.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Diretrizes da marca {#brand-guidelines}

Você pode selecionar [diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) para o seu agente seguir em suas respostas. Por exemplo, se você quiser que seu agente gere textos de SMS para incentivar os usuários a se inscreverem em uma academia, você pode usar este campo para referenciar sua diretriz motivacional predefinida.

## Histórico de interação específico do usuário {#user-history}

Os dados de interação de um usuário incluem aberturas, cliques e dados de conversão recentes de Campaigns e Canvas. Por exemplo, você pode incluir esse contexto para um agente referenciar quando ele é avaliado em um Canvas. O histórico de interação específico do usuário também pode ajudar a influenciar um agente quando sua função é escrever textos de mensagens personalizadas.

## Duplicar agentes {#duplicate-agents}

Para testar melhorias ou iterações de um agente, você pode duplicar um agente e aplicar alterações para comparar com o original. Você também pode tratar a duplicação de agentes como controle de versão para rastrear variações nos detalhes do agente e quaisquer impactos no seu envio de mensagens. Para duplicar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Duplicar**.

## Arquivar agentes {#archive-agents}

À medida que você cria mais agentes personalizados, pode organizar a página **Gerenciamento de agentes** arquivando agentes que não estão sendo usados ativamente. Para arquivar um agente:

1. Passe o mouse sobre a linha do agente e selecione o menu <i class="fas fa-ellipsis-vertical"></i>.
2. Selecione **Arquivar**.