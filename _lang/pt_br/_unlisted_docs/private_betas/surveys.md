---
nav_title: Pesquisas
article_title: Pesquisas da Braze
description: "Saiba como criar pesquisas em mensagens no app e landing pages, revisar respostas e redirecionar usuários durante o beta fechado."
permalink: /braze_surveys/
hidden: true
---

# Pesquisas da Braze {#braze-surveys}

> As pesquisas da Braze coletam feedback em mensagens no app e landing pages que você pode analisar e usar em mensagens de acompanhamento.

{% alert important %}
As pesquisas da Braze estão em beta fechado. Envie seu feedback sobre o beta para [surveys-feedback@braze.com](mailto:surveys-feedback@braze.com).
{% endalert %}

## Pré-requisitos {#prerequisites}

Antes de criar uma pesquisa, você deve:

- Ter acesso a landing pages, mensagens no app, ou ambos no seu espaço de trabalho da Braze
- Estar familiarizado com a [criação de landing pages](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/)
- Estar familiarizado com a [criação de mensagens no app com arrastar e soltar](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)

## Criar uma pesquisa {#create-a-survey}

Durante o beta, as pesquisas são criadas dentro do seu fluxo de composição de mensagens existente.

1. Acesse **Messaging** > **Landing Pages**, ou crie uma [mensagem no app](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/) em uma Campaign ou Canvas.
2. Crie uma nova mensagem.
3. Selecione **Survey** como seu tipo de mensagem.

## Redigir uma pesquisa de mensagem no app {#compose-an-in-app-message-survey}

As pesquisas de mensagem no app contêm duas páginas por padrão:

- **Página 1**, onde os usuários respondem às perguntas
- **Página de confirmação**, onde a pesquisa é enviada

Por padrão, os botões estão vinculados a **Next page**. Para alterar esse comportamento, atualize cada botão no painel **Actions**.

![Fluxo de páginas da pesquisa de mensagem no app e configurações de ação.]({% image_buster /assets/unlisted_docs/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

## Usar blocos de formulário de pesquisa {#use-survey-form-blocks}

Para controles compartilhados de estilo e composição, consulte:

- [Blocos do editor de arrastar e soltar de mensagens no app](https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [Blocos de formulário de landing page](https://braze.com/docs/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

Você pode adicionar os seguintes blocos de formulário às pesquisas:

- Captura de telefone
- Captura de e-mail
- Grupo de botões de rádio
- Captura de texto curto
- Captura de texto longo
- Menu suspenso
- Caixa de seleção única
- Grupo de caixas de seleção

### Captura de texto longo {#long-text-capture}

A captura de texto longo é útil para feedback qualitativo.

Você pode configurar:

- Contagens mínima e máxima de caracteres (até 1.000)
- Se os limites de caracteres devem ser exibidos durante a composição
- Altura da área de texto (linhas)
- Texto de espaço reservado

Durante o beta, as respostas de texto longo estão disponíveis em relatórios e exportações, mas não podem ser registradas como atributos personalizados do perfil de usuário.

![Configurações do bloco de captura de texto longo.]({% image_buster /assets/unlisted_docs/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configurar campos obrigatórios e atributos {#configure-required-fields-and-attributes}

Para cada bloco de formulário, insira um **Identifier for Reporting** no painel de configurações do lado direito. Esse identificador aparece nos relatórios de pesquisa e nas exportações CSV.

Durante o beta:

- Você pode registrar a maioria das respostas de pesquisa como atributos personalizados do perfil de usuário.
- Respostas de texto longo não podem ser registradas como atributos personalizados.
- Se você optar por não registrar uma resposta como atributo de usuário, não será possível segmentar usuários por esse valor de resposta.

![Configurações de identificador para relatório e registro de atributos.]({% image_buster /assets/unlisted_docs/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Visualizar relatórios e análise de dados {#view-reporting-and-analytics}

Após o lançamento, revise os resultados em:

- A guia **Responses** para pesquisas de mensagem no app
- A visualização de análise de dados da landing page para pesquisas de landing page

![Guia de análise de dados da landing page.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-1.png %})

As análises de nível superior incluem:

- **All responses:** total de respostas completas e incompletas
- **Completed:** usuários que completaram todas as perguntas obrigatórias
- **Partially complete:** usuários que enviaram alguns dados, mas não completaram todas as perguntas obrigatórias
- **Unique impressions:** total de visualizações de página

{% alert note %}
As pesquisas de landing page não rastreiam respostas parcialmente completas durante o beta.
{% endalert %}

Você também pode revisar os detalhamentos de respostas por pergunta e exportar dados como CSV.

![Visão geral da análise de dados da pesquisa e detalhamento por pergunta.]({% image_buster /assets/unlisted_docs/img/surveys/survey-analytics-text.png %})

![Gráficos de barras do detalhamento por pergunta da pesquisa.]({% image_buster /assets/unlisted_docs/img/surveys/bar-charts-1.png %})

## Redirecionar e acionar {#retarget-and-trigger}

Durante o beta, você pode:

- Segmentar usuários por respostas de pesquisa que são registradas como atributos de usuário.
- Segmentar usuários por status de conclusão da pesquisa. <br><br>![Configuração de gatilho e filtros de segmentação para acompanhamento de pesquisa.]({% image_buster /assets/unlisted_docs/img/surveys/submit-survey-segment.png %})<br><br>
- Acionar Campaigns e Canvas quando um usuário conclui uma pesquisa em uma landing page ou em uma Campaign de mensagem no app. <br><br>![Configuração de gatilho e filtro de segmentação para acompanhamento de pesquisa de landing page.]({% image_buster /assets/unlisted_docs/img/surveys/trigger_landing_page_survey.png %}) <br><br>![Configuração de gatilho e filtro de segmentação para acompanhamento de pesquisa de Campaign de mensagem no app.]({% image_buster /assets/unlisted_docs/img/surveys/interact-campaign-step.png %})

### Limitações {#limitations}

Durante o beta, você está restrito pelo seguinte:

- Não é possível segmentar usuários por respostas de texto longo.
- O acionamento por pergunta e resposta que não depende de atributos de usuário registrados não está disponível.