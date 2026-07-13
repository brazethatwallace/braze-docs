---
nav_title: Pontuação de leads
article_title: Criar um fluxo de trabalho de pontuação de leads
page_order: 1
page_type: reference
description: "Saiba como usar a Braze para fazer pontuação simples de leads, pontuação externa de leads e transferências de leads."
---

# Criar um fluxo de trabalho de pontuação de leads {#create-a-lead-scoring-workflow}

> Este caso de uso demonstra como você pode usar a Braze para atualizar as pontuações de leads dos usuários em tempo real e entregar automaticamente os leads às suas equipes de vendas.

Há duas etapas principais para criar um fluxo de trabalho de pontuação de leads na Braze:

1. Crie um Canvas de pontuação de leads na Braze ou integre uma ferramenta externa de pontuação de leads:
- [Pontuação simples de leads](#simple-lead-scoring)
- [Pontuação externa de leads](#external-lead-scoring)

2. Crie uma campanha de webhook para enviar leads qualificados para sua equipe de vendas:
- [Transferência de leads: Lead qualificado de marketing (MQL) para vendas](#lead-handoff)

## Pontuação simples de leads {#simple-lead-scoring}

### Etapa 1: Criar um Canvas {#step-1-create-a-canvas}

1. Acesse **Envio de mensagens** > **Canvas** e selecione **Criar Canvas** e, em seguida, preencha os dados básicos do Canvas.

2. Dê ao seu Canvas um nome relevante, como "Lead Scoring Canvas" e, para facilitar a localização, adicione uma tag como "Lead Management".<br><br>![Etapa 1 da criação de um Canvas com o nome "Lead Scoring Canvas" e a tag "Lead Management".]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Etapa 2: Configure seus critérios de entrada {#step-2-set-up-your-entry-criteria}

1. Prossiga para a etapa **Cronograma de entrada** e selecione um cronograma de entrada **Baseado em ação**. Isso inserirá os usuários no Canvas quando eles realizarem ações específicas.

2. Em **Opções baseadas em ação**, adicione essas duas ações:
    - **Alterar valor de atributo personalizado** com o nome do seu atributo de pontuação de leads (como `lead score`). Se você ainda não criou um atributo de pontuação de leads, siga as etapas em [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes). Isso inserirá os usuários no Canvas sempre que a pontuação de leads deles for alterada.
    - **Adicionar um endereço de e-mail**

![Etapa 2 da criação de um Canvas com o cronograma de entrada "Baseado em ação" e opções baseadas em ação para alterar um atributo personalizado "lead score" e adicionar um endereço de e-mail.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Etapa 3: Identifique seu público-alvo {#step-3-identify-your-target-audience}

#### Etapa 3a: Selecione os segmentos {#step-3a-select-segments}

Todos os usuários são elegíveis para a pontuação de leads, então você pode adicionar regras específicas da empresa sobre quem pontuar, selecionando quais [segmentos]({{site.baseurl}}/user_guide/audience/segments) de usuários direcionar e aplicando [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) adicionais. Por exemplo, é possível excluir colaboradores, usuários que já são clientes e similares.

![Etapa 3 da criação de um Canvas com opções para selecionar segmentos e filtros para restringir o público de entrada.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Etapa 3b: Definir reelegibilidade do Canvas {#step-3b-set-canvas-re-eligibility}

Um usuário passará por esse Canvas muitas vezes ao longo do ciclo de vida dele com você, então certifique-se de que ele possa entrar novamente tão rapidamente quanto saiu da vez anterior. Isso pode ser feito por meio das configurações de reelegibilidade.

Em **Controles de entrada**, faça o seguinte:
- Selecione **Permitir que os usuários entrem novamente neste Canvas**.
- Selecione **Período especificado**.
- Defina a reelegibilidade como "0" **segundos**.

![Seção "Controles de entrada" com seleções para "Permitir que os usuários entrem novamente neste Canvas" em um "Período especificado" de 0 segundos.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Etapa 3c: Atualizar configurações de envio {#step-3c-update-send-settings}

Dada a natureza operacional desse Canvas e o fato de que nenhuma mensagem será enviada a esses usuários, não é necessário aderir aos status de inscrição.

Em **Configurações de inscrição**, para **Enviar para esses usuários:** selecione **todos os usuários, inclusive os que cancelaram inscrição**.

![Etapa 4 da criação de um Canvas para definir as opções de envio de mensagens.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Etapa 4: Crie seu Canvas {#step-4-build-your-canvas}

#### Etapa 4a: Adicionar uma jornada de ação {#step-4a-add-an-action-path}

Na sua variante, selecione <i class="fas fa-plus" aria-label="Adicionar"></i> **Adicionar** e, em seguida, selecione **Jornadas de ação**.

![Canvas com "Jornadas de ação" exibidas no menu aberto pelo ícone de adição.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Etapa 4b: Criar grupos de ação {#step-4b-create-action-groups}

Cada grupo de ação representará todas as ações que levam ao mesmo incremento ou decremento de pontos. Você pode definir até oito grupos de ação. Neste cenário, vamos configurar quatro grupos.

Adicione os seguintes grupos à sua jornada de ação:

- **Grupo 1:** Todos os eventos que contam para um incremento de 1 ponto.
- **Grupo 2:** Todos os eventos que contam para um incremento de 5 pontos.
- **Grupo 3:** Todos os eventos que contam para um decremento de 1 ponto.
- **Restante do público:** As jornadas de ação permitem definir um período de espera para ver se um usuário executa uma ação, antes de colocá-lo em um grupo "restante do público". Para a pontuação de leads, essa é uma oportunidade de diminuir a pontuação por "inatividade".

![Jornada de ação contendo grupos de ação para adicionar um ponto, cinco pontos e dez pontos; subtrair um ponto e dez pontos; e "Restante do público".]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Etapa 4c: Configure cada grupo para incluir os eventos relevantes {#step-4c-configure-each-group-to-include-the-relevant-events}

Em cada grupo de ação, selecione **Selecionar gatilho** e escolha o evento que adicionará o número de pontos para esse grupo de ação específico. Adicione mais gatilhos para incluir todos os eventos que aumentarão a pontuação do lead em um ponto. Por exemplo, um usuário pode aumentar sua pontuação em um ponto quando iniciar uma sessão em qualquer app ou realizar um evento personalizado (como registrar-se ou participar de um webinar).

![Grupo de ação para adicionar um ponto com os gatilhos de "Iniciar sessão em qualquer app" e "Realizar evento personalizado".]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Etapa 4d: Adicionar etapas de atualização de usuário {#step-4d-add-user-update-steps}

Adicione uma etapa de atualização de usuário a cada jornada do Canvas criada na sua jornada de ação.

![Canvas exibindo a jornada de ação com jornadas ramificadas de atualização de usuário para cada grupo de ação.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start="2"}
Na guia **Redigir** de cada etapa de atualização de usuário, faça o seguinte para os respectivos campos:

| Campo | Ação |
| --- | --- |
| **Nome do atributo** | Selecione o atributo de pontuação de leads que você selecionou na etapa 2 (`lead score`). |
| **Ação** | Altere a ação para **Incrementar por** se a jornada aumentar a pontuação ou **Decrementar por** se a jornada diminuir a pontuação. |
| **Incrementar por** ou **Decrementar por** | Insira o número de pontos que serão aumentados ou diminuídos da pontuação de leads. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4d: Add User Update steps" }

### Etapa 5: Lance seu Canvas {#step-5-launch-your-canvas}

É isso! Seu Canvas de pontuação de leads está pronto para ser lançado.

## Pontuação externa de leads {#external-lead-scoring}

Seja usando um dos nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home), seu próprio modelo interno de pontuação de leads, machine learning ou outra ferramenta de pontuação de leads, temos várias opções para você.

### Parceiros externos {#external-partners}

Confira [Parceiros de tecnologia]({{site.baseurl}}/partners/home) para saber mais sobre nossos parceiros B2B que oferecem recursos de pontuação de leads. Não está vendo sua ferramenta lá? Você pode fazer a integração chamando o endpoint [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) da nossa API.

### Modelos internos de dados de pontuação de leads {#internal-lead-scoring-data-models}

Você pode integrar a Braze com seus modelos de dados internos, incluindo modelos de pontuação de leads, de várias maneiras. Veja abaixo alguns exemplos comuns de como nossos clientes se integraram à Braze.

#### Data warehouse integrado na nuvem {#integrated-cloud-data-warehouse}

{% tabs %}
{% tab Braze como fonte de dados %}

Como sua ferramenta de marketing, a Braze contém dados extremamente relevantes que podem complementar o modelo interno de pontuação de leads da sua equipe.

Por exemplo, os dados de engajamento com mensagens (como aberturas e cliques de e-mail, engajamento da landing page e outros) podem determinar o nível de engajamento de um lead. Você pode enviar esses dados de volta para seu data warehouse na nuvem e disponibilizá-los como entrada para seus modelos de pontuação de leads usando as soluções de exportação de dados da Braze:

- [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)
- [Compartilhamento seguro de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

{% endtab %}
{% tab Braze como destino %}

Depois que suas equipes internas criarem e executarem seu modelo de pontuação de leads, você pode puxar esses dados de volta para a Braze para segmentar e direcionar melhor os leads para o envio de mensagens relevantes. Você pode fazer isso com a [Ingestão de dados na nuvem da Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Com a ingestão de dados na nuvem, suas equipes internas criarão uma nova tabela ou visualização com os identificadores de usuários, as pontuações de leads mais recentes e os timestamps de quando as pontuações foram atualizadas. A Braze pegará a tabela ou visualização e adicionará as pontuações de leads aos perfis de usuário.

{% endtab %}
{% endtabs %}

## Transferência de leads: Lead qualificado de marketing (MQL) para vendas {#lead-handoff}

Nossa abordagem recomendada para as transferências de leads é ter um lead ou contato correspondente vinculado a cada usuário na Braze. Esses leads entrariam na fila das suas equipes de vendas quando seus status de lead mudassem para um estágio de MQL, momento em que o Salesforce daria início a um fluxo de trabalho de encaminhamento ou atribuição de leads.

Para atualizar o registro do lead no Salesforce com o status do lead da Braze, recomendamos o uso de um modelo de webhook disparado.

### Etapa 1: Criar uma campanha de webhook {#step-1-create-a-webhook-campaign}

### Etapa 2: Configure seu webhook {#step-2-configure-your-webhook}

#### Etapa 2a: Redigir webhook {#step-2a-compose-webhook}

1. Dê um nome à sua campanha de webhook, como "Salesforce > Update lead to MQL".

2. Digite a URL do webhook no formato {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. O ID de usuário da Braze {% raw %}`{{${user_id}}}`{% endraw %} deve corresponder ao seu ID de contato do Salesforce. Caso contrário, use um alias em vez de {% raw %}`{{${user_id}}}`{% endraw %}.

3. Atualize o **Método HTTP** para **PATCH**.

4. Configure sua carga útil para atualizar o registro do lead no Salesforce somente se a pontuação do lead ultrapassar o limite predefinido. Veja o exemplo de corpo de solicitação abaixo para uma pontuação de lead superior a 100.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. Inclua os seguintes cabeçalhos:

| Cabeçalho | Conteúdo |
| --- | --- |
| Authorization | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Para recuperar um token, [configure um app conectado](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) para o fluxo de credenciais do cliente OAuth 2.0 e, em seguida, use o Conteúdo conectado para recuperar o bearer do Salesforce: <br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content-Type | application/json |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2a: Compose webhook" }

![Webhook sendo criado com uma URL de webhook do Salesforce, método HTTP PATCH, corpo de solicitação em texto bruto e cabeçalhos de solicitação.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Etapa 2b: Agendar envios de webhook {#step-2b-schedule-webhook-sends}

A campanha deve ser disparada sempre que a pontuação de leads do usuário for alterada. Essa campanha será disparada para qualquer usuário cuja pontuação mude, mas afetará apenas os usuários que não são atualmente um MQL e que ultrapassaram o limite definido na etapa anterior.

Na etapa **Programar entrega**, selecione o seguinte:
- Um tipo de entrega **Baseada em ação**
- Uma ação-gatilho de **Alterar valor de atributo personalizado** com o nome do seu atributo de pontuação de leads e uma ação de **qualquer novo valor**

#### Etapa 2c: Identificar o público-alvo {#step-2c-identify-target-audience}

Na etapa **Público-alvo**, inclua um filtro que exclua usuários cujos status de lead já estejam em MQL ou além, como "`lead_status` `is none of` `MQL`".

![Opções de direcionamento do webhook com o filtro de "lead_status" não é nenhum dos "MQL".]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Etapa 3: Lance a campanha {#step-3-launch-campaign}

Selecione **Lançar** e veja o status do seu lead mudar no Salesforce à medida que seus clientes ultrapassam o limite de pontuação de lead MQL.