{% comment %}
  Documentação compartilhada de pesquisas da Braze.
  Parâmetros:
  - channel (obrigatório): "in_app_message" ou "landing_page"
{% endcomment %}

Para uma visão geral das pesquisas e dos recursos compartilhados entre canais, consulte [Pesquisas]({{site.baseurl}}/user_guide/messaging/surveys).

## Pré-requisitos {#prerequisites}

Antes de criar uma pesquisa, você deve:

{% if include.channel == 'in_app_message' %}
- Ter acesso a mensagens no app no seu espaço de trabalho da Braze
- Estar familiarizado com a [criação de mensagens no app no editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
{% elsif include.channel == 'landing_page' %}
- Ter acesso a landing pages no seu espaço de trabalho da Braze
- Estar familiarizado com a [criação de landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- Ter acesso a landing pages, mensagens no app ou ambos no seu espaço de trabalho da Braze
- Estar familiarizado com a [criação de landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages) e a [criação de mensagens no app no editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
{% endif %}

## Criar uma pesquisa {#create-a-survey}

As pesquisas são criadas dentro do fluxo de composição de mensagens existente.

{% if include.channel == 'in_app_message' %}
1. Crie uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) em uma Campaign ou Canvas.
2. Selecione **Survey** como o tipo de mensagem.
{% elsif include.channel == 'landing_page' %}
1. Acessar **Messaging** > **Landing Pages**.
2. Crie uma nova landing page.
3. Selecione **Survey** como o tipo de mensagem.
{% else %}
1. Acessar **Messaging** > **Landing Pages**, ou crie uma [mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) em uma Campaign ou Canvas.
2. Crie uma nova mensagem.
3. Selecione **Survey** como o tipo de mensagem.
{% endif %}

{% if include.channel == 'in_app_message' %}

## Compor uma pesquisa de mensagem no app {#compose-an-in-app-message-survey}

As pesquisas de mensagem no app contêm duas páginas por padrão:

- **Página 1**, onde os usuários respondem às perguntas
- **Página de confirmação**, onde a pesquisa é enviada

Por padrão, os botões estão vinculados a **Next page**. Para alterar esse comportamento, atualize cada botão no painel **Actions**.

![Fluxo de páginas e configurações de ação de uma pesquisa de mensagem no app.]({% image_buster /assets/img/surveys/iam-survey-nav.png %}){: style="max-width:40%;"}

{% endif %}

## Use blocos de formulário de pesquisa {#use-survey-form-blocks}

Para controles compartilhados de estilo e composição, consulte:

{% if include.channel == 'in_app_message' %}
- [Blocos do editor de arrastar e soltar de mensagens no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
{% elsif include.channel == 'landing_page' %}
- [Blocos de formulário de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% else %}
- [Blocos do editor de arrastar e soltar de mensagens no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Blocos de formulário de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)
{% endif %}

Você pode adicionar os seguintes blocos de formulário a pesquisas:

- Captura de telefone
- Captura de e-mail
- Grupo de botões de opção
- Captura de texto curto
- Captura de texto longo
- Menu suspenso
- Caixa de seleção única
- Grupo de caixas de seleção
- Escala de avaliação
- Net Promoter Score (NPS)

### Randomizar opções de resposta {#randomize-answer-choices}

Os blocos de grupo de botões de opção, grupo de caixas de seleção e menu suspenso aceitam opções de resposta aleatórias. Ative **Randomize choice order** para embaralhar as opções cada vez que a pesquisa for carregada. Para saber mais, consulte [Ordem aleatória de opções]({{site.baseurl}}/user_guide/messaging/surveys#randomized-choice-order).

### Captura de texto longo {#long-text-capture}

A captura de texto longo é útil para feedback qualitativo, com até 1.000 caracteres. Para saber mais, consulte [Captura de texto em formato longo]({{site.baseurl}}/user_guide/messaging/surveys#long-form-text-capture).

### Escala de avaliação {#rating-scale}

A escala de avaliação (também chamada de pergunta com escala numérica) é útil para capturar sentimento, satisfação ou probabilidade de recomendação como um único número. Para saber mais, consulte [Perguntas com escala numérica]({{site.baseurl}}/user_guide/messaging/surveys#number-scale-questions).

{% if include.channel == 'in_app_message' %}
![Escala de avaliação para classificar sua experiência na loja de 1 a 5.]({% image_buster /assets/img/surveys/iam_rating_scale_example.png %}){: style="max-width:40%;"}
{% elsif include.channel == 'landing_page' %}
![Escala de avaliação para indicar a probabilidade de recomendar o produto a um amigo de 1 a 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% else %}
![Escala de avaliação para indicar a probabilidade de recomendar o produto a um amigo de 1 a 10.]({% image_buster /assets/img/surveys/landing_page_rating_scale_example.png %}){: style="max-width:70%;"}
{% endif %}

## Configurar campos e atributos obrigatórios {#configure-required-fields-and-attributes}

Para cada bloco de formulário, insira um **Identificador para relatório** no painel de configurações do lado direito. Esse identificador aparece nos relatórios de pesquisa e nas exportações em CSV.

Tenha em mente:

- Você pode registrar a maioria das respostas de pesquisa em atributos personalizados do perfil de usuário.
- Respostas de texto longo não podem ser registradas como atributos personalizados.
- Se você optar por não registrar uma resposta como atributo de usuário, não será possível segmentar usuários por esse valor de resposta.

![Configurações de identificador para relatório e registro de atributos.]({% image_buster /assets/img/surveys/reporting-id-surveys.png %}){: style="max-width:40%;"}

## Ver relatórios e análise de dados {#view-reporting-and-analytics}

Após o lançamento, revise os resultados em:

{% if include.channel == 'in_app_message' %}
- A guia **Responses** para pesquisas de mensagem no app
{% elsif include.channel == 'landing_page' %}
- A visualização de análise de dados da landing page para pesquisas de landing page
{% else %}
- A guia **Responses** para pesquisas de mensagem no app
- A visualização de análise de dados da landing page para pesquisas de landing page
{% endif %}

Para definições da análise de dados de nível superior disponível para cada pesquisa (todas as respostas, concluídas, parcialmente concluídas e impressões únicas), consulte [Análise de dados]({{site.baseurl}}/user_guide/messaging/surveys#analytics).

{% if include.channel == 'landing_page' %}
{% alert note %}
Pesquisas de landing page rastreiam respostas parcialmente concluídas quando a pesquisa usa [formulários de múltiplas etapas]({{site.baseurl}}/user_guide/messaging/surveys#multi-step-landing-page-forms).
{% endalert %}
{% endif %}

Você também pode revisar os detalhamentos de respostas por pergunta, escolher entre três tipos de gráfico e exportar dados como CSV. Para saber mais, consulte [Tipos de gráfico]({{site.baseurl}}/user_guide/messaging/surveys#chart-types).

## Redirecionar e disparar {#retarget-and-trigger}

Você pode:

- Segmentar usuários por respostas de pesquisa que são registradas como atributos de usuário.
- Segmentar usuários por status de conclusão da pesquisa.

{% if include.channel == 'in_app_message' %}

![Configuração de disparo e filtros de segmentação para acompanhamento de pesquisa.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Disparar Campaigns e Canvas quando um usuário conclui uma pesquisa em uma Campaign de mensagem no app.

![Configuração de disparo e filtro de segmentação para acompanhamento de pesquisa de Campaign de mensagem no app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% elsif include.channel == 'landing_page' %}

![Configuração de disparo e filtro de segmentação para acompanhamento de pesquisa de landing page.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

- Disparar Campaigns e Canvas quando um usuário conclui uma pesquisa em uma landing page.

{% else %}

![Configuração de disparo e filtros de segmentação para acompanhamento de pesquisa.]({% image_buster /assets/img/surveys/submit-survey-segment.png %})

- Disparar Campaigns e Canvas quando um usuário conclui uma pesquisa em uma landing page ou em uma Campaign de mensagem no app.

![Configuração de disparo e filtro de segmentação para acompanhamento de pesquisa de landing page.]({% image_buster /assets/img/surveys/trigger_landing_page_survey.png %})

![Configuração de disparo e filtro de segmentação para acompanhamento de pesquisa de Campaign de mensagem no app.]({% image_buster /assets/img/surveys/interact-campaign-step.png %})

{% endif %}

### Limitações {#limitations}

Você tem as seguintes restrições:

- Não é possível segmentar usuários por respostas de texto longo.
- O disparo por pergunta e resposta que não depende de atributos de usuário registrados não está disponível.