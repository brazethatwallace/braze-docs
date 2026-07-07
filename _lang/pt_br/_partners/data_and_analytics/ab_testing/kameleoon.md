---
nav_title: Kameleoon
article_title: Kameleoon
description: "Saiba como integrar o Kameleoon à Braze"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[O Kameleoon](https://www.kameleoon.com) é uma solução de otimização com experimentos, personalização com IA e recursos de gerenciamento de funcionalidades em uma única plataforma unificada.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Requisito | Descrição |
| --- | --- |
| Conta Kameleoon | É necessário ter uma conta Kameleoon para aproveitar essa parceria. |
| Conta Braze | Uma conta Braze ativa com o [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado em sua página da web. Você também precisará ativar a segmentação de propriedades de eventos. Para solicitá-la, consulte [Considerações](#considerations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

O Kameleoon envia eventos personalizados à Braze para identificar os usuários que participam de campanhas de experimentação e personalização, possibilitando um direcionamento mais preciso e o envio de mensagens personalizadas.

## Integração do Kameleoon {#integrating-kameleoon}

Essa integração é executada como um rastreador JavaScript por meio do engine.js do Kameleoon. Ela pode ser rapidamente ativada na plataforma do Kameleoon.

### Etapa 1: Acessar a página de integrações do Kameleoon {#step-1-go-to-the-kameleoon-integrations-page}

No seu app Kameleoon, selecione **Admin** e, em seguida, **Integrations** na barra lateral.

![O painel de administração na plataforma Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Etapa 2: Instalar a ferramenta Braze {#step-2-install-the-braze-tool}

Por padrão, a ferramenta Braze não está instalada. Procure o ícone da Braze e selecione **Install the tool**. ![Um quadrado cinza com uma seta apontando para baixo.]({% image_buster /assets/img/kameleoon/img_2.png %})

Selecione os projetos para os quais você deseja ativar a ferramenta Braze, para que os dados do Kameleoon sejam reportados corretamente à Braze.

![O ícone da ferramenta Braze no Kameleoon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Depois de configurar a ferramenta, selecione **Validate**, que fechará o painel de configuração. Em seguida, você verá um botão **ON** ao lado do ícone da ferramenta Braze, incluindo o número de projetos nos quais a ferramenta está configurada.

![A ferramenta Braze ativada no Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}
Esse recurso está em versão beta. Participe do [Kameleoon Beta Program](https://help.kameleoon.com/account-and-team-management/join-beta-program/) para começar a usar essa integração.
{% endalert %}

### Etapa 3: Associar a Braze às campanhas do Kameleoon {#step-3-associate-braze-with-kameleoon-campaigns}

#### No editor gráfico/código {#in-the-graphiccode-editor}

Para finalizar seu experimento, selecione a etapa **Integrations** para configurar a Braze como uma ferramenta de rastreamento e, em seguida, selecione **Braze**.

![O dashboard de integrações no Kameleoon mostrando todas as integrações disponíveis, incluindo a integração ativa Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

A Braze será mencionada no resumo antes de entrar em operação. O Kameleoon transmitirá automaticamente os dados para a Braze, e você poderá usá-los para análise de dados e segmentação diretamente na Braze.

##### Criação de personalização {#personalization-creation}

Na página **Personalization Creation**, você pode selecionar a Braze entre as ferramentas de relatório para personalizar seus relatórios.

![Seção Reporting Tools mostrando integrações como Heap, Mixpanel, Clarity, com Braze selecionado.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Criação de Feature Flag {#feature-flag-creation}

Configure a integração no ambiente de Feature Flag na seção **Integrations**. Ative-a para os ambientes em que você deseja que ela esteja ativa.

![A página de Feature Flag no Kameleoon com as integrações disponíveis. Há dois switches para cada parceiro, "Delivery rules" e "Feature experiments".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Página de resultados {#results-page}

Depois que a Braze for definida como uma ferramenta de relatório para um experimento, você poderá selecioná-la (ou desmarcá-la) na página de resultados do Kameleoon no menu **Experiment configuration**.

{% alert note %}
Essa integração requer uma [implementação híbrida](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) e só é compatível com SDKs da web.
{% endalert %}

![O painel lateral da página de resultados no Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

As ferramentas de relatório associadas ao experimento serão exibidas. Selecione **Edit** para editar essa seleção.

### Etapa 4: Analise e aproveite seus dados do Kameleoon na Braze {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

Depois que a integração for configurada, o Kameleoon enviará eventos personalizados chamados `kameleoon_exposure` com propriedades como **Experiment name**, **Experiment ID**, **Variation name** e **Variation ID** para a Braze.

![O registro de usuários de eventos personalizados na Braze, mostrando um exemplo de carga útil do evento recebido pela Braze do Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

Em seguida, você pode visualizar esses dados nos eventos personalizados, criar relatórios de eventos personalizados para identificar a exposição às campanhas do Kameleoon e ativar a segmentação com base nas propriedades do evento. Você pode usar eventos personalizados ao criar Campaigns e Canvas subsequentes ou vinculados por meio de [Jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [disparos baseados em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) ou criação de [segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).

Além disso, esses eventos poderão ser acessados por meio de [objetos de eventos personalizados do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) para permitir relatórios e análises abrangentes.

## Considerações {#considerations}

### Solicitar segmentação de propriedades de eventos {#request-event-property-segmentation}

Antes de poder usar a segmentação de propriedades de eventos, você precisará ativá-la na Braze. Use o modelo a seguir para entrar em contato com o CSM da Braze ou com a equipe de suporte para obter acesso.

   <table aria-label="Solicitar segmentação de propriedades de eventos">
     <caption>Solicitar segmentação de propriedades de eventos</caption>
   <thead>
      <tr>
         <th>Campo</th>
         <th>Informações</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Assunto</strong></td>
         <td>Request to Enable Event Property Segmentation for Kameleoon Integration</td>
      </tr>
      <tr>
         <td><strong>Corpo</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our Kameleoon&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> Kameleoon<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Solicitar segmentação de propriedades de eventos" }

### Pontos de dados da Braze {#braze-data-points}

O evento personalizado enviado do Kameleoon para a Braze&#8212;incluindo quaisquer propriedades de evento ativadas para segmentação&#8212;registrará pontos de dados na sua instância da Braze.