---
nav_title: Criar agentes
article_title: Criar agentes personalizados
description: "Aprenda como criar agentes, o que preparar antes de começar e como colocá-los para trabalhar em envio de mensagens, tomada de decisões e gerenciamento de dados."
page_order: 1
alias: /creating-agents/
---

# Criar agentes personalizados {#create-custom-agents}

> Aprenda como criar agentes personalizados, o que preparar antes de começar e como colocá-los para trabalhar em envio de mensagens, tomada de decisões e gerenciamento de dados. Para mais informações gerais, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents).

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

- [Permissão]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) para acessar o **Agent Console** no seu espaço de trabalho. Verifique com os administradores da Braze se você não vir essa opção.
- Permissão para criar e editar agentes de IA personalizados.
- Uma ideia do que você quer que o agente realize. Os Braze Agents podem realizar as seguintes ações:
   - **Envio de mensagens personalizadas:** gerar linhas de assunto, títulos, textos no produto ou outros conteúdos.
   - **Roteamento de usuários:** direcionar usuários no Canvas com base em comportamento, preferências ou atributos personalizados.
   - **Gerenciamento de dados:** calcular valores, enriquecer entradas de catálogo ou atualizar campos de perfil.

## Como funciona {#how-it-works}

Quando você cria um agente, define seu propósito e estabelece diretrizes para como ele deve se comportar. Depois que está ativo, o agente pode ser implantado na Braze para gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo. Enquanto constrói seu agente, você pode salvá-lo como rascunho e pode pausar ou atualizar um agente a qualquer momento pelo dashboard. Cada salvamento cria uma nova versão que você pode revisar na guia [Histórico de versões]({{site.baseurl}}/user_guide/brazeai/agents/reference#version-history).

Os casos de uso a seguir mostram algumas formas de aproveitar agentes personalizados.

| Caso de uso | Descrição |
| --- | --- |
| Tratamento de feedback de clientes | Envie o feedback do usuário para um agente analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir benefícios. |
| Localizar conteúdo | Traduza textos de catálogo para outro idioma em campanhas globais, ou ajuste o tom e o tamanho para canais específicos de cada região. Por exemplo, traduza "Classic Clubmaster Sunglasses" para o espanhol como "Gafas de sol Classic Clubmaster" ou encurte descrições para campanhas de SMS. |
| Resumir avaliações ou feedback | Resuma sentimentos ou feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um breve resumo de texto como "A maioria dos clientes menciona ótimo caimento, mas nota envio lento." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como funciona" }

## Criar um agente {#create-an-agent}

### Etapa 1: Escolha um tipo de agente {#step-1-choose-an-agent-type}

Para criar um agente, primeiro escolha o tipo de agente:

1. Acesse o **Agent Console**.
2. Escolha **Canvas Step Agents** ou **Catalog Agents**.

### Etapa 2: Escolha como criar um agente {#step-2-choose-how-to-build-an-agent}

Selecione **Create agent** e escolha uma das seguintes opções:

- **Custom agent** para criar um agente do zero
- Uma opção em **Create an agent with Operator** para usar o [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) e aplicar um [modelo inicial](#agent-templates-built-with-operator)

Se você usar o Operator, revise e aprove as alterações no chat antes de continuar para a próxima etapa.

### Etapa 3: Configure os detalhes {#step-3-set-up-details}

Em seguida, configure os detalhes do seu agente:

1. Insira um nome e uma descrição para ajudar sua equipe a entender a finalidade do agente.
2. (opcional) Adicione tags para filtrar seu agente.
3. Escolha o [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) que seu agente usará.
4. Se você não estiver usando o modelo **Braze Auto**, selecione o [nível de raciocínio]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) do modelo. Você pode escolher entre mínimo, baixo, médio ou alto. Recomendamos começar com **Minimal** e testar as respostas do agente, ajustando conforme necessário.
5. Defina um limite diário de invocações. Por padrão, esse valor é definido como 250.000, mas pode ser aumentado para 1.000.000. Se você tiver interesse em aumentar o limite acima de 1.000.000, entre em contato com seu gerente de sucesso do cliente para saber mais. Defina o limite alto o suficiente para o tamanho do público planejado após os testes. Um limite muito baixo causa falhas de limite diário (que não consomem créditos, mas aplicam valores de fallback ou deixam a saída como `null`).

O campo **Daily action credit cost limit** especifica o número máximo de créditos que esse agente pode consumir por dia. A Braze calcula esse valor a partir da proporção de créditos por invocação do seu espaço de trabalho para o modelo selecionado (do seu contrato, exibido na página [Credit Ratios]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)) multiplicado pelo limite diário de invocações. A estimativa é atualizada quando você altera o modelo ou o limite de invocações.

Para gerenciar custos, reduza o limite diário de invocações. Para modelos [bring-your-own (BYO)]({{site.baseurl}}/user_guide/brazeai/agents/reference#option-2-bring-your-own-api-key), você também pode mudar para um modelo de menor custo ou reduzir o [nível de raciocínio]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels). O **Braze Auto** não permite ajustar o nível de raciocínio. Acompanhe o uso real em **Settings** > **Billing** > **Credits Usage** > **Agent Console**.

![Interface do Agent Console para criar um agente personalizado na Braze. A tela exibe campos para inserir o nome e a descrição do agente, selecionar um modelo e definir um limite diário de invocações.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Etapa 4: Escreva as instruções {#agent-instructions}

Forneça instruções ao agente. Se você usou um modelo do Operator, revise as instruções pré-preenchidas e edite conforme necessário.

Inclua instruções sobre o que o agente deve fazer em cenários inesperados ou ambíguos. Isso minimiza o risco de que a confusão do agente leve a erros. Por exemplo, em vez de pedir ao agente apenas valores de sentimento "positivo" ou "negativo", peça que ele retorne "incerto" se não conseguir decidir.

Consulte [Escrevendo instruções]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) para melhores práticas e [Exemplos]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples) para inspiração sobre como orientar seu agente.

#### Adicionar contexto {#add-resources}

{% alert important %}
Os agentes recebem apenas os dados que você passa explicitamente — eles não pesquisam perfis de usuário nem avisam quando dados obrigatórios estão ausentes. Use Liquid nas suas instruções, selecione **+ Agent context**, adicione [etapas de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) anteriores no Canvas ou passe contexto adicional na etapa do agente. Para uma lista completa de fontes de dados e orientações de design, consulte [Quais dados os agentes recebem]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).
{% endalert %}

Selecione **+ Agent context** para escolher o que seu agente pode referenciar. Isso inclui:

- [Campos de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields): Dê ao agente acesso aos dados do seu catálogo para respostas mais precisas.
- [Fontes de conhecimento]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources): Dê ao agente acesso a dados de catálogo por meio de uma fonte de conhecimento para uma recuperação mais precisa do que anexar um catálogo diretamente.
- [Pertencimento a Segments]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context): Permita que o agente personalize respostas com base nos Segments aos quais um usuário pertence. Você pode selecionar até cinco Segments.
- [Diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines): Referencie as diretrizes de voz e estilo da marca para o agente seguir. Por exemplo, se você quer que seu agente gere textos de SMS para incentivar usuários a se inscreverem em uma academia, pode usar esse campo para referenciar sua diretriz predefinida de tom ousado e motivacional.
- [Todo o contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables): Analise todos os dados de contexto do Canvas para um usuário quando esse agente for invocado, incluindo quaisquer variáveis que não estejam referenciadas na seção **Instructions**.
- [Dados de interação do usuário]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history): Forneça ao agente os dados recentes de aberturas, cliques e conversões de Campaigns e Canvas de cada usuário.

{% alert tip %}
Para agentes de Canvas, você pode usar Liquid nas instruções para referenciar atributos do usuário, como nome e sobrenome, ou atributos personalizados. Qualquer variável Liquid nas instruções do agente é automaticamente passada para a etapa do agente quando um usuário entra na etapa. Consulte [Quais dados os agentes recebem]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive) para saber como passar contexto do Canvas e dados de perfil de forma deliberada.
{% endalert %}

### Etapa 5: Selecione a saída {#select-output}

Na seção **Output**, você pode organizar e definir a [saída]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs) do agente por esquemas básicos ou esquemas avançados. Se você usou um modelo do Operator, revise o esquema de saída pré-preenchido e edite conforme necessário.

Para melhores resultados, certifique-se de que o que você especifica na seção **Output** corresponda às instruções do agente inseridas na [Etapa 4](#agent-instructions). Por exemplo, se você mencionou nas instruções do agente que deseja um objeto com duas strings, certifique-se de especificar um objeto com duas strings na seção **Output**. Se as instruções do agente não estiverem alinhadas com a saída especificada, o agente pode ficar confuso, expirar o tempo limite ou gerar saídas indesejadas.

{% alert tip %}
Quando você usa um [esquema de saída avançado]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas), adicione um campo de string chamado `explanation` se quiser que o agente retorne sua justificativa além das outras saídas. Diga ao agente nas suas [instruções](#agent-instructions) para preencher `explanation` quando isso ajudar você a revisar ou depurar respostas.
{% endalert %}

#### Configurar valores de fallback {#configure-fallback-values}

Os valores de fallback estão disponíveis apenas para Canvas Step Agents. Na seção **Output** de um Canvas Step Agent, você pode definir valores que a Braze usa quando uma invocação do agente falha — por exemplo, quando o LLM expira o tempo limite ou retorna um erro de chave de API inválida. Os valores de fallback funcionam como padrões de personalização. Você pode definir uma linha de assunto estática ou uma mensagem curta que ainda forneça uma saída útil aos usuários quando o agente não puder ser executado.

Catalog Agents não permitem configurar valores de fallback no Agent Console.

![Configuração de saída do Agent Console mostrando o campo de saída de fallback para um esquema numérico.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Para agentes de Canvas, os valores de fallback suportam templates [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para que você possa referenciar atributos do usuário ou variáveis de contexto no texto de fallback.

Os campos de fallback se adaptam ao formato de saída do seu Canvas Step Agent:

| Formato de saída | Configuração de fallback |
| --- | --- |
| String, número ou booleano | Insira um único valor de fallback (Liquid suportado). |
| Campos (esquema avançado) | Insira um valor de fallback para cada campo definido na saída do agente. |
| Esquema JSON (esquema avançado) | A Braze lê seu esquema JSON e gera um campo de entrada para cada propriedade, para que você possa definir um valor de fallback por chave. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurar valores de fallback" }

Quando um Canvas Step Agent com valores de fallback é executado em uma [etapa do agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step), a Braze renderiza o fallback por usuário e o armazena na variável de saída em vez de `null`. Se você não configurar valores de fallback, invocações com falha deixam a saída do Canvas indefinida (`null`).

Para o comportamento em tempo de execução, consulte [Tratamento de erros e comportamento de fallback]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

### Etapa 6: Teste o agente {#step-6-test-the-agent}

O painel **Preview** é uma instância do agente que aparece como um painel lado a lado dentro da experiência de configuração. Você pode usar essa seção para testar o agente enquanto o cria ou faz atualizações, experimentando-o de forma semelhante aos usuários finais. Essa etapa ajuda a confirmar que ele está se comportando como esperado e oferece a chance de fazer ajustes finos antes de colocá-lo em produção.

1. No campo **Test your agent**, insira dados de exemplo do cliente ou respostas do cliente — qualquer coisa que reflita cenários reais que seu agente irá lidar.
2. Visualize a resposta do agente para um usuário aleatório, um usuário existente ou um usuário personalizado.
3. Selecione **Simulate response**. O agente será executado com base na sua configuração e exibirá sua resposta.

{% alert note %}
As execuções de teste contam para o seu limite diário de invocações.
{% endalert %}

![Agent Console mostrando o painel de prévia para testar um agente personalizado. A interface exibe um campo de entradas de exemplo com dados do cliente, um botão de execução de teste e uma área de resposta onde a saída do agente aparece.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revise a saída com um olhar crítico. Considere as seguintes perguntas:

- O texto está alinhado com a marca?
- A lógica de decisão direciona os clientes conforme o esperado?
- Os valores calculados estão precisos?

Se algo parecer errado, atualize a configuração do agente e teste novamente. Execute algumas entradas diferentes para ver como o agente se adapta em diversos cenários, especialmente casos extremos como ausência de dados ou respostas inválidas.

{% alert tip %}
Evite dizer ao agente exatamente o que você não quer que ele faça. Os LLMs ainda podem gerar esse conteúdo se você mencioná-lo nas instruções.
{% endalert %}

### Etapa 7: Use seu agente {#step-7-use-your-agent}

Seu agente está pronto para uso! Para mais detalhes, consulte [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Modelos de agente criados com o Operator {#agent-templates-built-with-operator}

O Operator pode pré-configurar instruções, campos de saída e contexto para os seguintes modelos iniciais do Agent Console. Escolha um modelo no Operator ou peça ao Operator para aplicar um pelo nome.

### Modelos de agente de etapa do Canvas {#canvas-step-agent-templates}

| Modelo | Descrição | Exemplo de saída |
| --- | --- | --- |
| Redator personalizado | Gera textos de mensagem específicos para o canal a partir de atributos do usuário, contexto do Canvas e diretrizes da marca | Linha de assunto e pré-cabeçalho de e-mail; título e corpo de push |
| Analista de feedback | Analisa feedback aberto de pesquisas ou suporte em campos estruturados para ramificação no Canvas | Sentimento, tópico, próxima ação recomendada |
| Roteador de jornada | Direciona cada usuário para a jornada do Canvas mais relevante com base no perfil e no contexto da jornada | Nome da jornada ou booleano para etapas de divisão de decisão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modelos de agente de etapa do Canvas" }

### Modelos de agente de catálogo {#catalog-agent-templates}

| Modelo | Descrição | Exemplo de saída |
| --- | --- | --- |
| Redator de descrições | Escreve descrições curtas de marketing a partir de colunas existentes do catálogo | Descrição de produto ou destino |
| Categorizador de itens | Atribui categorias ou tags a partir dos dados da linha | Rótulos de categoria para filtragem e recomendações |
| Tradutor de localização | Traduz strings do catálogo para localidades-alvo dentro de limites de caracteres | Texto localizado por localidade |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Modelos de agente de catálogo" }

## Recursos relacionados {#related-resources}

- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/agents/faq)
- [Webinar da Braze sobre IA em ação: 3 novos casos de uso para personalização 1:1](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)