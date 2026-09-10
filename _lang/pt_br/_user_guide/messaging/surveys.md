---
nav_title: Pesquisas
article_title: Pesquisas
page_order: 9
page_type: reference
channel:
  - landing pages
  - in-app messages
description: "Saiba como as pesquisas da Braze permitem coletar feedback primário em landing pages e mensagens no app, incluindo análise de dados, blocos de formulário e exportação via Currents."
---

# Pesquisas {#surveys}

> As pesquisas da Braze permitem coletar feedback primário diretamente dos seus usuários e utilizá-lo em envios de mensagens de acompanhamento, sem sair do dashboard da Braze. Use pesquisas para entender o sentimento dos usuários, capturar preferências e criar segmentos e disparadores a partir das respostas coletadas.

## Disponibilidade por canal {#channel-availability}

As pesquisas estão disponíveis em dois canais. Cada página de canal cobre o fluxo de criação, composição e local de relatórios específicos do canal, enquanto esta página cobre os conceitos e recursos que se aplicam a ambos.

| Canal | Crie pesquisas em |
| --- | --- |
| Landing pages | [Pesquisas em landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| In-App Messages | [Pesquisas em mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidade de pesquisas por canal" }

## Página de pesquisas {#surveys-page}

Acesse **Messaging** > **Surveys** para encontrar pesquisas em landing pages, Campaigns e Canvas em um só lugar. Use como seu ponto de entrada para revisar o desempenho de pesquisas em todos os canais.

{% alert note %}
Se você não encontrar **Surveys** em **Messaging**, entre em contato com o gerente de conta da Braze.
{% endalert %}

## Análise de dados {#analytics}

Cada tipo de pergunta de pesquisa inclui relatórios aprimorados por padrão, para que você possa revisar os dados de resposta rapidamente, sem precisar criar um Segment ou exportar para uma ferramenta separada.

As análises de nível superior incluem:

- **Todas as respostas:** Total de respostas completas e incompletas
- **Concluídas:** Usuários que completaram todas as perguntas obrigatórias
- **Parcialmente concluídas:** Usuários que enviaram alguns dados, mas não completaram todas as perguntas obrigatórias
- **Impressões únicas:** Total de visualizações de página

![Página de respostas da pesquisa mostrando análise de pontuação NPS com porcentagens de promotores, passivos e detratores e um gráfico de barras horizontais com a distribuição de pontuações.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Tipos de gráfico {#chart-types}

Para blocos de formulário com botão de opção, menu suspenso e caixa de seleção, você pode escolher entre três tipos de gráfico na visualização de análise da pesquisa. Isso oferece mais flexibilidade para interpretar e compartilhar insights sem precisar exportar para uma ferramenta de terceiros.

| Tipo de gráfico | Melhor para |
| --- | --- |
| **Gráfico de barras** | A visualização horizontal padrão de contagens e porcentagens de respostas. |
| **Gráfico de colunas** | Uma visualização vertical de contagens e porcentagens de respostas. Use este gráfico para comparar respostas lado a lado, especialmente para perguntas de múltipla seleção ou perguntas com mais opções de resposta. |
| **Gráfico de pizza** | Uma divisão proporcional das respostas. Use este gráfico para perguntas de seleção única, quando você quiser ver como as respostas estão distribuídas entre as opções. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de gráfico de pesquisa" }

Cada gráfico mostra dados em tempo real à medida que as respostas chegam. Você pode alternar entre os tipos de gráfico a qualquer momento sem afetar os dados subjacentes.

![Detalhamento por pergunta da pesquisa usando um gráfico de barras.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Formulários de landing page com várias etapas {#multi-step-landing-page-forms}

Crie uma pesquisa como uma única landing page com várias etapas que são vinculadas automaticamente, em vez de criar várias landing pages independentes e vinculá-las manualmente. Por exemplo, você pode definir etapas separadas para cada pergunta da pesquisa, além de uma etapa de confirmação no final.

Esse recurso é específico do canal de landing pages. As pesquisas em mensagens no app também oferecem suporte a um gerenciador de páginas para navegar entre etapas; consulte [Compor uma pesquisa em mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey) para mais detalhes.

![Editor de landing page com uma prévia de formulário de várias etapas e o painel de propriedades do formulário listando as etapas e uma etapa de confirmação bloqueada.]({% image_buster /assets/img/surveys/multi_step.png %})

## Blocos de perguntas e formulários {#question-and-form-blocks}

Landing pages e mensagens no app oferecem suporte a todos os blocos de formulário padrão em pesquisas, incluindo grupo de botões de opção, caixa de seleção, grupo de caixas de seleção, menu suspenso, captura de telefone, captura de e-mail e captura de texto curto. Esta seção destaca os três blocos de formulário com relatórios criados especificamente para pesquisas: NPS, escala numérica e texto longo.

{% tabs local %}
{% tab NPS %}
### Bloco NPS independente {#standalone-nps-block}

O bloco **NPS** é um bloco de formulário separado do bloco **Avaliação** (escala numérica), não uma opção de configuração dentro dele. Adicione-o a uma pesquisa para fazer a pergunta padrão de Net Promoter Score (NPS) (0–10) e obter relatórios criados especificamente para esse caso de uso.

O bloco **NPS** oferece relatórios melhores no dashboard do que uma simples pergunta de avaliação usada com o mesmo propósito. Em vez de uma contagem simples de respostas por número, a Braze agrupa automaticamente as respostas em promotores (9–10), passivos (7–8) e detratores (0–6) e exibe esses segmentos — e a pontuação NPS resultante — diretamente na visualização de análise de dados da pesquisa.

O Currents exporta a pontuação numérica (e, se adicionado, o campo de feedback em texto livre) no evento **Survey Response**. Os segmentos de promotores, passivos e detratores não são campos separados no Currents.

![Uma pesquisa NPS em dispositivo móvel ao lado do dashboard de respostas da pesquisa, que mostra uma pontuação NPS com detalhamentos de promotores, passivos e detratores e um gráfico de distribuição de respostas.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Escala numérica %}
### Perguntas de escala numérica {#number-scale-questions}

Também chamada de escala de avaliação nas páginas dos canais; ambos os termos se referem ao mesmo bloco de formulário **Avaliação**. Capture perguntas de escala numérica de 1–5, 1–10 ou 0–10 para atender a diferentes necessidades de pesquisa e relatório, desde avaliações simples de satisfação até pontuações de probabilidade de recomendação. Para capturas de tela de composição específicas de cada canal, consulte a seção Escala de avaliação na página de [pesquisas em landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) ou [pesquisas em mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale).

Você pode coletar uma avaliação como resposta de pesquisa, registrá-la como um atributo personalizado de número inteiro, ou ambos. Combine uma pergunta de escala numérica com um bloco de [captura de texto longo](#long-form-text-capture) para coletar uma pontuação numérica junto com feedback qualitativo na mesma pesquisa.

![Editor de pesquisa em landing page com uma pergunta de avaliação de 1–5 selecionada e o painel de propriedades de Avaliação aberto à direita.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Texto longo %}
### Captura de texto longo {#long-form-text-capture}

A captura de texto longo é útil para feedback qualitativo. Você pode configurar a contagem mínima e máxima de caracteres (até 1.000 caracteres), se o limite de caracteres deve ser exibido durante a composição, a altura da área de texto e o texto de espaço reservado.

![Configurações do bloco de captura de texto longo.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

{% alert important %}
Os campos de texto longo em pesquisas de mensagens no app no iOS estão temporariamente limitados a 250 caracteres. Essa limitação será resolvida em uma atualização futura do SDK para iOS. Por enquanto, considere manter a contagem máxima de caracteres em 250 ou menos para pesquisas exibidas a usuários do iOS.
{% endalert %}

As respostas de texto longo estão disponíveis em relatórios e exportações, mas não podem ser registradas como atributos personalizados do perfil de usuário — portanto, não é possível segmentar usuários diretamente pelo valor de uma resposta de texto longo. Consulte [Limitações]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) na página de cada canal para mais detalhes.

No Currents, as respostas de texto longo usam `answer_type = 'free_form_text'` com o texto em `answer_long_string`.
{% endtab %}
{% endtabs %}

## Ordem aleatória de escolhas {#randomized-choice-order}

Os blocos de grupo de botões de rádio, grupo de caixas de seleção e menu suspenso oferecem suporte à aleatorização das opções de resposta. Ative **Randomize choice order** para embaralhar as opções cada vez que a pesquisa for carregada, o que reduz o viés de ordem quando a mesma primeira opção poderia distorcer as respostas.

A aleatorização altera apenas a ordem de exibição para cada respondente da pesquisa. Os rótulos e valores dos relatórios permanecem mapeados para as opções que você configurou, então a análise de dados, as exportações CSV e a segmentação usam os mesmos dados de resposta, independentemente da ordem que um determinado usuário visualizou.

## Modelos de pesquisa {#survey-templates}

Salve uma pesquisa como modelo a partir da landing page ou da biblioteca de modelos de mensagens no app para que os criadores possam começar a partir dele em vez de recriar as mesmas perguntas e blocos de formulário toda vez. Quando os modelos de pesquisa estiverem ativados para o seu espaço de trabalho, filtre a biblioteca por **Survey** para encontrar e reutilizar estruturas de pesquisa salvas em Campaigns, Canvas e landing pages.

## Eventos de resposta de pesquisa {#survey-response-events}

As respostas de pesquisa fluem para o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), permitindo que você exporte dados de pesquisa para seu data warehouse ou uma ferramenta de BI de terceiros para análise downstream, junções com outros dados de engajamento e relatórios personalizados que vão além da análise de dados integrada do dashboard.

A Braze exporta respostas individuais de pesquisa para o Currents por meio do evento **Survey Response** (`users.messages.survey.Response`). Cada evento representa a resposta de um respondente a uma pergunta da pesquisa. Para a referência completa dos campos, consulte [Eventos de resposta de pesquisa]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) no glossário de eventos do Currents.

## Funil de engajamento de landing page {#landing-page-engagement-funnel}

As pesquisas em landing pages também geram eventos de **Landing Page Impression** e **Landing Page Click** para visualizações de página e cliques rastreados. Concluir uma pesquisa em landing page registra um evento de **Survey Response**; isso não dispara também o evento genérico **Landing Page Form Submission**, que é destinado a formulários de landing page padrão (não pesquisas). Para a referência completa dos campos desses eventos, consulte o [glossário de eventos do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Artigos relacionados {#related-articles}

- [Pesquisas em landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): Fluxo de criação, composição e relatórios para o canal de landing pages
- [Pesquisas em mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): Fluxo de criação, composição e relatórios para o canal de mensagens no app
- [Blocos do editor de arrastar e soltar]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): Referência completa dos blocos de formulário que você pode adicionar a uma pesquisa
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): Configure a exportação de dados para o seu data warehouse ou ferramenta de BI