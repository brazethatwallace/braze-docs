---
nav_title: "Criar um e-mail de transação"
article_title: "Criar um e-mail de transação"
page_order: 1

description: "Este artigo de referência aborda como criar e configurar uma nova campanha de e-mail de transação da Braze."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Criar um e-mail de transação {#create-a-transactional-email}

> Os e-mails de transação da Braze são enviados para facilitar uma transação acordada entre um remetente e o destinatário. Este artigo de referência aborda como criar uma campanha de e-mail de transação no dashboard da Braze e gerar um `campaign_id` para incluir nas suas chamadas de API para o nosso [endpoint `/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

{% alert important %}
O e-mail de transação da Braze está disponível apenas como parte de pacotes selecionados da Braze. Entre em contato com o seu CSM da Braze ou abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) para mais detalhes.
{% endalert %}

O tipo de campanha de e-mail de transação foi criado especificamente para enviar mensagens de e-mail automatizadas e não promocionais, facilitando uma transação acordada entre você e seus clientes. Isso inclui informações como:

- Confirmações de pedido
- Redefinições de senha
- Alertas de cobrança
- Alertas de envio

Em resumo, você pode usar e-mails de transação para enviar notificações críticas para o negócio originadas do seu serviço para um único usuário, onde a velocidade é de extrema importância.

{% alert important %}
Os e-mails de transação são diferentes das campanhas transacionais, que podem ser usadas para direcionar seus usuários sem custos adicionais. Campanhas transacionais, por exemplo, podem incluir mensagens enviadas depois que um usuário adiciona um item ao carrinho. Confira as [opções de direcionamento de público]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) para mais informações.
{% endalert %}

{% alert note %}
Os envios de e-mail de transação via API suportam o arquivamento de mensagem. Se o arquivamento de mensagem estiver ativado para e-mail no seu espaço de trabalho, a Braze salva uma cópia renderizada de cada envio de e-mail de transação. Para saber mais, consulte [Arquivamento de mensagem]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving).
{% endalert %}

## Etapa 1: Criar uma nova campaign {#step-1-create-a-new-campaign}

Para criar uma nova campaign de e-mail de transação, crie uma campaign e selecione **Transactional Email** como seu canal de envio de mensagens.

![Menu suspenso Criar Campaign com a opção de e-mail de transação destacada.]({% image_buster /assets/img/transactional_email_campaign.png %}){: width="534" height="800" style="float:right;max-width:35%;margin-left:15px;height:auto;"}

Agora, você pode prosseguir para configurar sua campaign de e-mail de transação.

## Etapa 2: Configure sua campanha {#step-2-configure-your-campaign}

O fluxo de criação de campanhas de e-mail de transação é simplificado em comparação com o de uma [campanha de e-mail padrão]({{site.baseurl}}/user_guide/channels/email/html_editor) para garantir que seu e-mail de transação crítico para o negócio possa alcançar todos os usuários.

Como resultado, você notará que várias configurações com as quais pode estar familiarizado em outros tipos de campanha da Braze não são necessárias ao configurar esse tipo de campanha:

- A etapa **Delivery** foi simplificada para remover opções de agendamento. E-mails de transação sempre serão disparados pela REST API da Braze usando o ID da campanha exibido na página **Delivery**. Configurações adicionais, como controles de reelegibilidade e configurações de limite de frequência, também foram removidas para garantir que todos os usuários sejam alcançáveis para esses alertas transacionais críticos quando seu serviço dispara uma solicitação de envio.
- A etapa **Target Audiences** foi removida. Como os e-mails de transação incluem toda a sua base de usuários como elegível (incluindo usuários que cancelaram inscrição), não é necessário especificar filtros ou Segments. Portanto, se você tiver alguma lógica para aplicar a quem deve receber essa mensagem, recomendamos aplicar essa lógica antes de determinar se deve fazer a solicitação de API à Braze para disparar a mensagem a um usuário específico.
- A etapa **Conversions** foi removida. E-mails de transação não oferecem suporte ao rastreamento de eventos de conversão no momento.

![Fluxo de trabalho de composição, entrega e confirmação para criar uma campanha de e-mail de transação.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: width="1586" height="1112" style="max-width:80%;height:auto;"}

Para configurar sua campanha de e-mail de transação, siga estas etapas:

1. Adicione um nome descritivo para que você possa encontrar os resultados na página **Campaigns** depois de enviar suas mensagens.
2. Componha seu e-mail ou selecione a partir de um modelo.
3. Anote seu `campaign_id`. Depois de salvar sua campanha de API, você deve incluir os campos `campaign_id` gerados na sua solicitação de API, conforme indicado no artigo [Endpoint de e-mail de transação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Clique em **Save Campaign** e pronto para iniciar sua campanha de API!

{% alert note %}
A configuração de cancelamento de inscrição com um clique para campanhas de e-mail de transação é definida como **Use workspace default** por padrão, assim como outras campanhas de e-mail. Como isso é destinado ao envio de mensagens transacionais, a Braze não adiciona o cancelamento de inscrição com um clique. Para adicionar o cancelamento de inscrição com um clique a esse tipo de campanha, [edite essa configuração]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#message-level-one-click-list-unsubscribe) em **Sending Info**.
{% endalert %}

### Tags não permitidas em e-mails de transação {#disallowed-tags-in-transactional-emails}

As Liquid tags `Connected Content` e `Promotion Code` não estão disponíveis em campanhas de e-mail de transação.

Usar a tag `Connected Content` requer que a Braze faça uma solicitação de API externa durante nosso processo de envio, o que pode desacelerar o processo de envio de mensagens se o serviço externo solicitado estiver com latência. Da mesma forma, a tag `Promotion Code` requer que a Braze realize processamento adicional para avaliar a disponibilidade de um código de promoção antes do envio, o que pode desacelerar o processo caso não haja nenhum disponível.

Por isso, não oferecemos suporte à inclusão de tags `Connected Content` ou `Promotion Code` em nenhum campo da sua campanha de e-mail de transação.