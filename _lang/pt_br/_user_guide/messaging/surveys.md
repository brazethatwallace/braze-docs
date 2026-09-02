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

As pesquisas estão disponíveis em dois canais. Cada página de canal aborda o fluxo de criação, a composição e a localização dos relatórios específicos do canal, enquanto esta página aborda os conceitos e recursos que se aplicam a ambos.

| Canal | Crie pesquisas em |
| --- | --- |
| Landing pages | [Pesquisas em landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| Mensagens no app | [Pesquisas em mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidade de pesquisas por canal" }

## Página de pesquisas {#surveys-page}

Acesse **Messaging** > **Surveys** para encontrar pesquisas de landing pages, Campaigns e Canvas em um só lugar. Use essa página como ponto de partida para revisar o desempenho das pesquisas entre canais.

{% alert note %}
Se você não vê **Surveys** em **Messaging**, entre em contato com o gerente da sua conta Braze.
{% endalert %}

## Análise de dados {#analytics}

Todo tipo de pergunta de pesquisa inclui relatórios aprimorados por padrão, permitindo que você revise os dados de respostas rapidamente, sem precisar criar um Segment or segmento or segmento ou exportar para uma ferramenta separada.

A análise de dados de nível superior inclui:

- **Todas as respostas:** total de respostas completas e incompletas
- **Concluídas:** usuários que responderam a todas as perguntas obrigatórias
- **Parcialmente concluídas:** usuários que enviaram alguns dados, mas não responderam a todas as perguntas obrigatórias
- **Impressões únicas:** total de visualizações de página

![Página de respostas de pesquisa mostrando análise de dados de NPS com porcentagens de promotores, passivos e detratores e um gráfico de barras horizontal da distribuição de pontuação.]({% image_buster /assets/img/surveys/survey_responses.png %})

### Tipos de gráfico {#chart-types}

Para blocos de formulário de botão de opção, dropdown e caixa de seleção, você pode escolher entre três tipos de gráfico na visualização de análise de dados da pesquisa. Isso oferece mais flexibilidade para interpretar e compartilhar insights sem exportar para uma ferramenta de terceiros.

| Tipo de gráfico | Ideal para |
| --- | --- |
| **Gráfico de barras** | A visualização horizontal padrão de contagens e porcentagens de respostas. |
| **Gráfico de colunas** | Uma visualização vertical de contagens e porcentagens de respostas. Use este gráfico para comparar respostas lado a lado, especialmente para perguntas de múltipla seleção ou perguntas com mais opções de resposta. |
| **Gráfico de pizza** | Uma divisão proporcional das respostas. Use este gráfico para perguntas de seleção única quando quiser ver como as respostas estão distribuídas entre as opções. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de gráfico de pesquisa" }

Cada gráfico exibe dados em tempo real conforme as respostas chegam. Você pode alternar entre tipos de gráfico a qualquer momento sem afetar os dados subjacentes.

![Detalhamento por pergunta de pesquisa usando um gráfico de barras.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Formulários de landing page com múltiplas etapas {#multi-step-landing-page-forms}

Crie uma pesquisa como uma única landing page com múltiplas etapas vinculadas automaticamente, em vez de criar várias landing pages independentes e vinculá-las manualmente. Por exemplo, você pode definir etapas separadas para cada pergunta da pesquisa, além de uma etapa de confirmação no final.

Esse recurso é específico do canal de landing pages. As pesquisas em mensagens no app também oferecem suporte a um gerenciador de páginas para navegar entre etapas; consulte [Criar uma pesquisa em mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey) para mais detalhes.

![Editor de landing page com uma prévia de formulário com múltiplas etapas e o painel de propriedades do formulário listando as etapas e uma etapa de confirmação bloqueada.]({% image_buster /assets/img/surveys/multi_step.png %})

## Blocos de perguntas e formulários {#question-and-form-blocks}

Landing pages e mensagens no app oferecem suporte a todos os blocos de formulário padrão também em pesquisas, incluindo grupo de botões de opção, caixa de seleção, grupo de caixas de seleção, dropdown, captura de telefone, captura de e-mail e captura de texto curto. Esta seção destaca os três blocos de formulário com relatórios criados especificamente para pesquisas: Net Promoter Score (NPS), escala numérica e texto longo.

{% tabs local %}
{% tab Net Promoter Score (NPS) %}
### Bloco Net Promoter Score (NPS) independente {#standalone-nps-block}

O bloco **Net Promoter Score (NPS)** é um bloco de formulário separado do bloco **Classificação** (escala numérica), não uma opção de configuração dentro dele. Adicione-o a uma pesquisa para fazer a pergunta padrão de Net Promoter Score (0–10) e obter relatórios criados especificamente para esse caso de uso.

O bloco **Net Promoter Score (NPS)** oferece relatórios mais completos no dashboard do que uma pergunta simples de classificação usada para o mesmo propósito. Em vez de uma contagem simples de respostas por número, a Braze agrupa automaticamente as respostas em promotores (9–10), passivos (7–8) e detratores (0–6) e exibe esses segmentos — e a pontuação Net Promoter Score (NPS) resultante — diretamente na visualização de análise de dados da pesquisa.

O Currents exporta a pontuação numérica (e, se adicionado, o campo de feedback em texto livre) no evento **Survey Response**. Os segmentos de promotores, passivos e detratores não são campos separados no Currents.

![Uma pesquisa NPS em dispositivo móvel ao lado do dashboard de respostas da pesquisa, que mostra uma pontuação NPS com detalhamento de promotores, passivos e detratores e um gráfico de distribuição de respostas.]({% image_buster /assets/img/surveys/survey_and_chart.png %})
{% endtab %}

{% tab Escala numérica %}
### Perguntas de escala numérica {#number-scale-questions}

Também chamada de escala de classificação nas páginas de canal; ambos os termos se referem ao mesmo bloco de formulário **Classificação**. Capture perguntas de escala numérica de 1–5, 1–10 ou 0–10 para atender a diferentes necessidades de pesquisa e relatórios, desde classificações simples de satisfação até pontuações de probabilidade de recomendação. Para capturas de tela de composição específicas por canal, consulte a seção de escala de classificação na página de [pesquisas em landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) ou [pesquisas em mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale).

Você pode coletar uma classificação como resposta de pesquisa, registrá-la como um atributo personalizado de número inteiro, ou ambos. Combine uma pergunta de escala numérica com um bloco de [captura de texto longo](#long-form-text-capture) para coletar uma pontuação numérica junto com feedback qualitativo na mesma pesquisa.

![Editor de pesquisa em landing page com uma pergunta de classificação de 1–5 selecionada e o painel de propriedades de classificação aberto à direita.]({% image_buster /assets/img/surveys/rating_block.png %})
{% endtab %}

{% tab Texto longo %}
### Captura de texto longo {#long-form-text-capture}

A captura de texto longo é útil para feedback qualitativo. Você pode configurar o número mínimo e máximo de caracteres (até 1.000 caracteres), se o limite de caracteres deve ser exibido durante a composição, a altura da área de texto e o texto de espaço reservado.

![Configurações do bloco de captura de texto longo.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

As respostas de texto longo estão disponíveis em relatórios e exportações, mas não podem ser registradas como atributos personalizados do perfil de usuário — portanto, não é possível segmentar usuários diretamente pelo valor de uma resposta de texto longo. Consulte [Limitações]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations) na página de cada canal para mais detalhes.

No Currents, as respostas de texto longo usam `answer_type = 'free_form_text'` com o texto em `answer_long_string`.
{% endtab %}
{% endtabs %}

## Ordem aleatória de opções {#randomized-choice-order}

Os blocos de grupo de botões de opção, grupo de caixas de seleção e dropdown oferecem suporte à aleatorização das opções de resposta. Ative **Randomize choice order** para embaralhar as opções a cada carregamento da pesquisa, reduzindo o viés de ordem quando a mesma primeira opção poderia distorcer as respostas.

A aleatorização altera apenas a ordem de exibição para cada respondente da pesquisa. Os rótulos e valores dos relatórios permanecem mapeados para as opções que você configurou, então a análise de dados, as exportações em CSV e a segmentação usam os mesmos dados de resposta independentemente da ordem que um determinado usuário viu.

## Modelos de pesquisa {#survey-templates}

Salve uma pesquisa como modelo a partir da biblioteca de modelos de landing pages ou mensagens no app para que os criadores possam começar a partir dele, em vez de recriar as mesmas perguntas e blocos de formulário a cada vez. Quando os modelos de pesquisa estiverem ativados para o seu espaço de trabalho, filtre a biblioteca por **Survey** para encontrar e reutilizar estruturas de pesquisa salvas em Campaigns, Canvas e landing pages.

## Eventos de resposta de pesquisa {#survey-response-events}

As respostas de pesquisa fluem para o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para que você possa exportar dados de pesquisa para o seu data warehouse ou uma ferramenta de BI de terceiros para análises avançadas, junções com outros dados de engajamento e relatórios personalizados que vão além da análise de dados integrada ao dashboard.

A Braze exporta respostas individuais de pesquisa para o Currents por meio do evento **Survey Response** (`users.messages.survey.Response`). Cada evento representa a resposta de um respondente a uma pergunta da pesquisa. Para a referência completa dos campos, consulte [Eventos de resposta de pesquisa]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) no glossário de eventos do Currents.

## Funil de engajamento de landing pages {#landing-page-engagement-funnel}

As pesquisas em landing pages também geram eventos **Landing Page Impression** e **Landing Page Click** para visualizações de página e cliques rastreados. Concluir uma pesquisa em landing page grava um evento **Survey Response**; ela não dispara também o evento genérico **Landing Page Form Submission**, que é destinado a formulários de landing page padrão (não de pesquisa). Para a referência completa dos campos desses eventos, consulte o [glossário de eventos do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Artigos relacionados {#related-articles}

- [Pesquisas em landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys): fluxo de criação, composição e relatórios para o canal de landing pages
- [Pesquisas em mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys): fluxo de criação, composição e relatórios para o canal de mensagens no app
- [Blocos do editor de arrastar e soltar]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks): referência completa dos blocos de formulário que você pode adicionar a uma pesquisa
- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents): configure a exportação de dados para o seu data warehouse ou ferramenta de BI