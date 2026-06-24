---
nav_title: Criar agentes
article_title: Criar agentes personalizados
description: "Aprenda como criar agentes, o que preparar antes de começar e como colocá-los para trabalhar em envio de mensagens, tomada de decisões e gerenciamento de dados."
page_order: 1
alias: /creating-agents/
---

# Criar agentes personalizados {#create-custom-agents}

> Aprenda como criar agentes personalizados, o que preparar antes de começar e como colocá-los para trabalhar em envio de mensagens, tomada de decisões e gerenciamento de dados. Para mais informações gerais, veja [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

- [Permissão]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) para acessar o **Console do agente** no seu espaço de trabalho. Verifique com seus administradores da Braze se você não vê essa opção.
- Permissão para criar e editar agentes de IA personalizados.
- Uma ideia do que você quer que o agente realize. Os Braze Agents podem suportar as seguintes ações:
   - **Envio de mensagens personalizado:** Gerar linhas de assunto, manchetes, textos dentro do produto ou outros conteúdos.
   - **Direcionamento de usuários:** Direcionar usuários no Canvas com base em comportamento, preferências ou atributos personalizados.
   - **Gerenciamento de dados:** Calcular valores, enriquecer entradas de catálogo ou atualizar campos de perfil.

## Como funciona {#how-it-works}

Quando você cria um agente, define seu propósito e estabelece diretrizes sobre como ele deve se comportar. Depois que estiver ativo, o agente pode ser implantado na Braze para gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo. Enquanto constrói seu agente, você pode salvá-lo como rascunho, e pode pausar ou atualizar um agente a qualquer momento pelo dashboard.

Os seguintes casos de uso mostram algumas maneiras de aproveitar agentes personalizados.

| Caso de uso | Descrição |
| --- | --- |
| Tratamento de feedback do cliente | Passe o feedback do usuário para um agente analisar o sentimento e gerar mensagens de acompanhamento empáticas. Para usuários de alto valor, o agente pode escalar a resposta ou incluir benefícios. |
| Localizar conteúdo | Traduza o texto do catálogo para outro idioma para campanhas globais, ou ajuste o tom e o comprimento para canais específicos da região. Por exemplo, traduza "Classic Clubmaster Sunglasses" para o espanhol como "Gafas de sol Classic Clubmaster", ou encurte descrições para campanhas de SMS. |
| Resumir avaliações ou feedback | Resuma o sentimento ou feedback em um novo campo, como atribuir pontuações de sentimento como Positivo, Neutro ou Negativo, ou criar um resumo de texto curto como "A maioria dos clientes menciona um ótimo caimento, mas nota o envio lento." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como funciona" }

## Criar um agente {#create-an-agent}

### Etapa 1: Escolher um tipo de agente {#step-1-choose-an-agent-type}

Para criar um agente, primeiro escolha o tipo de agente:

1. Acesse **Console do agente**.
2. Escolha **Agentes de etapa do Canvas** ou **Agentes de catálogo**.

### Etapa 2: Escolher como construir um agente {#step-2-choose-how-to-build-an-agent}

Selecione **Criar agente** e escolha uma das seguintes opções:

- **Agente personalizado** para construir um agente do zero
- Uma opção em **Criar um agente com Operator** para usar o [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) e aplicar um [modelo inicial](#agent-templates-built-with-operator)

Se você usar o Operator, revise e aprove as alterações no chat antes de continuar para a próxima etapa.

### Etapa 3: Configurar informações {#step-3-set-up-details}

Em seguida, configure as informações do seu agente:

1. Digite um nome e uma descrição para ajudar sua equipe a entender seu propósito.
2. (opcional) Adicione tags para filtrar seu agente.
3. Escolha o [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) que seu agente deve usar.
4. Se você não estiver usando o modelo **Braze Auto**, selecione o [nível de pensamento]({{site.baseurl}}/user_guide/brazeai/agents/reference/#thinking-levels) do modelo. Você pode escolher entre mínimo, baixo, médio ou alto. Recomendamos começar com **Mínimo** e testar as respostas do seu agente, ajustando conforme necessário.
5. Defina um limite diário de invocação. Por padrão, esse valor é definido como 250.000, mas pode ser aumentado para 1.000.000. Se você tiver interesse em aumentar o limite acima de 1.000.000, entre em contato com seu gerente de sucesso do cliente para saber mais.

![Interface do Console do agente para criar um agente personalizado na Braze. A tela exibe campos para inserir o nome e a descrição do agente, selecionar um modelo e definir um limite diário de invocação.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Etapa 4: Escreva as instruções {#agent-instructions}

Dê instruções ao agente. Se você usou um modelo do Operator, revise as instruções pré-preenchidas e edite conforme necessário.

Inclua instruções sobre o que o agente deve fazer em cenários inesperados ou ambíguos. Isso minimiza o risco de que a confusão do agente leve a erros. Por exemplo, em vez de pedir ao agente apenas valores de sentimento "positivo" ou "negativo", peça para retornar "incerto" se ele não conseguir decidir.

Consulte [Escrevendo instruções]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) para melhores práticas e [Exemplos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) para inspiração sobre como orientar seu agente.

{% alert tip %}
Para agentes Canvas, você pode usar Liquid nas suas instruções para referenciar atributos do usuário, como primeiro e último nome, ou atributos personalizados. Qualquer variável Liquid nas instruções do agente é automaticamente passada para a etapa do agente quando um usuário entra na etapa.
{% endalert %}

#### Adicionar contexto {#add-resources}

Selecione **+ Contexto do agente** para escolher o que seu agente pode referenciar. Isso inclui:

- [Campos de catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Dê ao agente acesso aos dados do seu catálogo para respostas mais precisas.
- [Associação a segmentos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Permita que o agente personalize respostas com base nos segmentos aos quais um usuário pertence. Você pode selecionar até cinco segmentos.
- [Diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/): Referencie a voz da marca e as diretrizes de estilo para o agente seguir. Por exemplo, se você quiser que seu agente gere textos de SMS para incentivar os usuários a se inscreverem em uma academia, você pode usar este campo para referenciar sua diretriz da marca motivacional e em negrito predefinida.
- [Todo o contexto do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/): Analise todos os dados de contexto do Canvas para um usuário quando este agente for invocado, incluindo quaisquer variáveis que não estejam referenciadas na seção **Instruções**.
- [Dados de interação do usuário]({{site.baseurl}}/user_guide/brazeai/agents/reference/#user-history): Forneça ao agente os dados recentes de aberturas, cliques e conversões de Campaigns e Canvas de cada usuário.

### Etapa 5: Selecione a saída {#select-output}

Na seção **Saída**, você pode organizar e definir a [saída]({{site.baseurl}}/user_guide/brazeai/agents/reference/#outputs) do agente por esquemas básicos ou esquemas avançados. Se você usou um modelo do Operator, revise o esquema de saída pré-preenchido e edite conforme necessário.

Para melhores resultados, certifique-se de que o que você especifica na seção **Saída** corresponda às instruções do agente que você inseriu na [Etapa 4](#agent-instructions). Por exemplo, se você mencionou nas instruções do agente que deseja um objeto com duas strings, certifique-se de especificar um objeto com duas strings na seção **Saída**. Se as instruções do seu agente não estiverem alinhadas com a saída especificada, o agente pode ficar confuso, expirar ou gerar saídas indesejadas.

{% alert tip %}
Quando você usar um [esquema de saída avançado]({{site.baseurl}}/user_guide/brazeai/agents/reference/#advanced-schemas), adicione um campo de string chamado `explanation` se quiser que o agente retorne sua justificativa além das outras saídas. Diga ao agente nas suas [instruções](#agent-instructions) para preencher `explanation` quando isso ajudar você a revisar ou depurar respostas.
{% endalert %}

#### Configurar valores de fallback {#configure-fallback-values}

Os valores de fallback estão disponíveis apenas para **agentes de etapa do Canvas**. Na seção **Saída** de um agente Canvas, você pode definir valores que a Braze usa quando uma invocação do agente falha — por exemplo, quando o LLM expira ou retorna um erro de chave de API inválida. Os valores de fallback funcionam como padrões de personalização. Você pode definir uma linha de assunto estática ou uma mensagem curta que ainda forneça uma saída útil aos usuários quando o agente não puder ser executado.

**Agentes de catálogo** não suportam a configuração de valores de fallback no Console do agente.

![Configuração de saída do Console do agente mostrando o campo de saída de fallback para um esquema de número.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Para agentes Canvas, os valores de fallback suportam templates [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) para que você possa referenciar atributos do usuário ou variáveis de contexto no texto de fallback.

Os campos de fallback se adaptam ao formato de saída do seu agente Canvas:

| Formato de saída | Configuração de fallback |
| --- | --- |
| String, número ou booleano | Insira um único valor de fallback (Liquid suportado). |
| Campos (esquema avançado) | Insira um valor de fallback para cada campo definido na saída do agente. |
| Esquema JSON (esquema avançado) | A Braze lê seu esquema JSON e gera um campo de entrada para cada propriedade, para que você possa definir um valor de fallback por chave. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurar valores de fallback" }

Quando um agente Canvas com valores de fallback é executado em uma [etapa do agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/), a Braze renderiza o fallback por usuário e o armazena na variável de saída em vez de `null`. Se você não configurar valores de fallback, invocações com falha deixam a saída do Canvas indefinida (`null`).

Para o comportamento em tempo de execução, veja [Tratamento de erros e comportamento de fallback]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#fallback-behavior).

### Etapa 6: Teste o agente {#step-6-test-the-agent}

O painel de **Pré-visualização** é uma instância do agente que aparece como um painel lado a lado dentro da experiência de configuração. Você pode usar essa seção para testar o agente enquanto está criando ou fazendo atualizações, vivenciando-o de maneira semelhante aos usuários finais. Essa etapa ajuda você a confirmar que ele está se comportando da maneira esperada e dá a chance de fazer ajustes antes de colocá-lo no ar.

1. No campo **Teste seu agente**, insira dados de cliente de exemplo ou respostas de clientes — qualquer coisa que reflita cenários reais que seu agente vai lidar.
2. Visualize a resposta do agente para um usuário aleatório, usuário existente ou usuário personalizado.
3. Selecione **Simular resposta**. O agente executará com base na sua configuração e exibirá sua resposta.

{% alert note %}
Os testes contam para o seu limite diário de invocação.
{% endalert %}

![Console do agente mostrando o painel de Pré-visualização para testar um agente personalizado. A interface exibe um campo de entradas de exemplo com dados de cliente, um botão Executar teste e uma área de resposta onde a saída do agente aparece.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revise a saída com um olhar crítico. Considere as seguintes perguntas:

- O texto parece estar alinhado com a marca?
- A lógica de decisão direciona os clientes conforme o esperado?
- Os valores calculados estão precisos?

Se algo parecer errado, atualize a configuração do agente e teste novamente. Execute algumas entradas diferentes para ver como o agente se adapta a diferentes cenários, especialmente casos extremos como ausência de dados ou respostas inválidas.

{% alert tip %}
Evite dizer ao agente exatamente o que você não quer que ele faça. Os LLMs ainda podem gerar esse conteúdo se você mencioná-lo nas instruções.
{% endalert %}

### Etapa 7: Use seu agente {#step-7-use-your-agent}

Seu agente está pronto para uso! Para mais detalhes, consulte [Implantar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Modelos de agente criados com o Operator {#agent-templates-built-with-operator}

O Operator pode pré-configurar instruções, campos de saída e contexto para os seguintes modelos iniciais do Console do agente. Escolha um modelo no Operator ou peça ao Operator para aplicar um pelo nome.

### Modelos de agente de etapa do Canvas {#canvas-step-agent-templates}

| Modelo | Descrição | Exemplo de saída |
| --- | --- | --- |
| Redator personalizado | Gera textos de mensagem específicos para o canal a partir de atributos do usuário, contexto do Canvas e diretrizes da marca | Assunto e pré-cabeçalho de e-mail; título e corpo de push |
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

- [Referência para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/agents/faq/)
- [Webinar da Braze sobre IA em ação: 3 novos casos de uso para personalização 1:1](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)