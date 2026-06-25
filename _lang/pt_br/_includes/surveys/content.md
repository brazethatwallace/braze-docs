{% comment %}
  Documentação compartilhada de pesquisas da Braze.
  Parâmetros:
  - channel (obrigatório): "in_app_message" ou "landing_page"
{% endcomment %}

{% multi_lang_include early_access_beta_alert.md feature='Braze surveys' %}

## Pré-requisitos {#prerequisites}

Antes de criar uma pesquisa, você deve:

{% if include.channel == 'in_app_message' %}
- Ter acesso a mensagens no app no seu espaço de trabalho da Braze
- Estar familiarizado com a [criação de mensagens no app no editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
{% elsif include.channel == 'landing_page' %}
- Ter acesso a landing pages no seu espaço de trabalho da Braze
- Estar familiarizado com a [criação de landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/)
{% else %}
- Ter acesso a landing pages, mensagens no app ou ambos no seu espaço de trabalho da Braze
- Estar familiarizado com a [criação de landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/) e a [criação de mensagens no app no editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
{% endif %}

## Criar uma pesquisa {#create-a-survey}

Durante o acesso antecipado, as pesquisas são criadas dentro do fluxo de composição de mensagens existente.

{% if include.channel == 'in_app_message' %}
1. Crie uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) em uma Campaign ou Canvas.
2. Selecione **Survey** como tipo de mensagem.
{% elsif include.channel == 'landing_page' %}
1. Acesse **Messaging** > **Landing Pages**.
2. Crie uma nova landing page.
3. Selecione **Survey** como tipo de mensagem.
{% else %}
1. Acesse **Messaging** > **Landing Pages** ou crie uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) em uma Campaign ou Canvas.
2. Crie uma nova mensagem.
3. Selecione **Survey** como tipo de mensagem.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Redigir uma pesquisa de mensagem no app {#compose-an-in-app-message-survey}

As pesquisas de mensagem no app contêm duas páginas por padrão:

- **Página 1**, onde os usuários respondem às perguntas
- **Página de confirmação**, onde a pesquisa é enviada

Por padrão, os botões estão vinculados a **Next page**. Para alterar esse comportamento, atualize cada botão no painel **Actions**.

![Fluxo de páginas da pesquisa de mensagem no app e configurações de ação.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Usar blocos de formulário de pesquisa {#use-survey-form-blocks}

Para controles compartilhados de estilo e composição, consulte:

{% if include.channel == 'in_app_message' %}
- [Blocos do editor de arrastar e soltar de mensagens no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Blocos de formulário de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% else %}
- [Blocos do editor de arrastar e soltar de mensagens no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Blocos de formulário de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)
{% endif %}

Você pode adicionar os seguintes blocos de formulário às pesquisas:

- Captura de telefone
- Captura de e-mail
- Grupo de botões de opção
- Captura de texto curto
- Captura de texto longo
- Menu suspenso
- Caixa de seleção individual
- Grupo de caixas de seleção

### Randomizar opções de resposta {#randomize-answer-choices}

Os blocos de grupo de botões de opção, grupo de caixas de seleção e menu suspenso suportam opções de resposta randomizadas. Ative **Randomize choice order** para embaralhar as opções cada vez que a pesquisa for carregada. Use essa configuração para reduzir o viés de ordem quando a mesma primeira opção pode distorcer as respostas.

A randomização altera apenas a ordem de exibição para cada respondente da pesquisa. Os rótulos e valores dos relatórios permanecem mapeados para as opções que você configurou, então a análise de dados, as exportações CSV e a segmentação usam os mesmos dados de resposta.

### Captura de texto longo {#long-text-capture}

A captura de texto longo é útil para feedback qualitativo.

Você pode configurar:

- Contagens mínima e máxima de caracteres (até 1.000)
- Se os limites de caracteres devem ser exibidos durante a composição
- Altura da área de texto (linhas)
- Texto de espaço reservado

Durante o acesso antecipado, as respostas de texto longo estão disponíveis em relatórios e exportações, mas não podem ser registradas como atributos personalizados do perfil de usuário.

![Configurações do bloco de captura de texto longo.]({% image_buster /assets/img/surveys/long-form-surveys.png %}){: style="max-width:40%;"}

## Configurar campos obrigatórios e atributos {#configure-required-fields-and-attributes}

Para cada bloco de formulário, insira um **Identifier for Reporting** no painel de configurações do lado direito. Esse identificador aparece nos relatórios de pesquisa e nas exportações CSV.

Durante o acesso antecipado:

- Você pode registrar a maioria das respostas de pesquisa como atributos personalizados do perfil de usuário.
- Respostas de texto longo não podem ser registradas como atributos personalizados.
- Se você optar por não registrar uma resposta como atributo de usuário, não será possível segmentar usuários por esse valor de resposta.

![Configurações de identificador para relatório e registro de atributos.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Visualizar relatórios e análise de dados {#view-reporting-and-analytics}

Após o lançamento, revise os resultados em:

{% if include.channel == 'in_app_message' %}
- A guia **Responses** para pesquisas de mensagem no app
{% elsif include.channel == 'landing_page' %}
- A visualização de análise de dados da landing page para pesquisas de landing page
{% else %}
- A guia **Responses** para pesquisas de mensagem no app
- A visualização de análise de dados da landing page para pesquisas de landing page
{% endif %}

![Guia de análise de dados da landing page.]({% image_buster /assets/img/surveys/survey-analytics-1.png %})

As análises de nível superior incluem:

- **All responses:** total de respostas completas e incompletas
- **Completed:** usuários que responderam a todas as perguntas obrigatórias
- **Partially complete:** usuários que enviaram alguns dados, mas não responderam a todas as perguntas obrigatórias
- **Unique impressions:** total de visualizações de página

{% if include.channel == 'landing_page' %}
{% alert note %}
As pesquisas de landing page não rastreiam respostas parcialmente completas durante o acesso antecipado.
{% endalert %}
{% endif %}

Você também pode revisar os detalhamentos de respostas por pergunta e exportar os dados como CSV.

### Escolher um tipo de gráfico {#choose-a-chart-type}

Para blocos de formulário de botão de opção, menu suspenso e caixa de seleção, você pode escolher entre três tipos de gráfico na visualização de análise de dados da pesquisa. Isso oferece mais flexibilidade para interpretar e compartilhar insights sem precisar exportar para uma ferramenta de terceiros.

| Tipo de gráfico | Melhor para |
| --- | --- |
| Gráfico de barras | A visualização horizontal padrão de contagens e porcentagens de respostas. |
| Gráfico de colunas | Uma visualização vertical de contagens e porcentagens de respostas. Use este gráfico para comparar respostas lado a lado, especialmente para perguntas de múltipla seleção ou perguntas com mais opções de resposta. |
| Gráfico de pizza | Um detalhamento proporcional das respostas. Use este gráfico para perguntas de seleção única quando quiser ver como as respostas estão distribuídas entre as opções. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de gráfico de pesquisa" }

Cada gráfico é atualizado em tempo real conforme as respostas chegam. Você pode alternar entre os tipos de gráfico a qualquer momento sem afetar os dados subjacentes.

![Detalhamento por pergunta da pesquisa usando um gráfico de barras.]({% image_buster /assets/img/surveys/bar-charts-1.png %})

## Redirecionar e acionar {#retarget-and-trigger}

Durante o acesso antecipado, você pode:

- Segmentar usuários por respostas de pesquisa registradas como atributos de usuário.
- Segmentar usuários por status de conclusão da pesquisa.

{% if include.channel == 'in_app_message' %}

![Configuração de gatilho e filtros de segmentação para acompanhamento de pesquisa.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Acionar Campaigns e Canvas quando um usuário conclui uma pesquisa em uma Campaign de mensagem no app.

![Configuração de gatilho e filtro de segmentação para acompanhamento de pesquisa de Campaign de mensagem no app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuração de gatilho e filtro de segmentação para acompanhamento de pesquisa de landing page.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Acionar Campaigns e Canvas quando um usuário conclui uma pesquisa em uma landing page.

{% else %}

![Configuração de gatilho e filtros de segmentação para acompanhamento de pesquisa.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Acionar Campaigns e Canvas quando um usuário conclui uma pesquisa em uma landing page ou em uma Campaign de mensagem no app.

![Configuração de gatilho e filtro de segmentação para acompanhamento de pesquisa de landing page.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuração de gatilho e filtro de segmentação para acompanhamento de pesquisa de Campaign de mensagem no app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitações {#limitations}

Durante o acesso antecipado, você está restrito pelo seguinte:

- Não é possível segmentar usuários por respostas de texto longo.
- O acionamento por pergunta e resposta que não depende de atributos de usuário registrados não está disponível.