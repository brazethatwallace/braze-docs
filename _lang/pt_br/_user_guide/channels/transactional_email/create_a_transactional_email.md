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
O e-mail de transação da Braze está disponível apenas como parte de pacotes selecionados da Braze. Entre em contato com o seu gerente de sucesso do cliente da Braze ou abra um [ticket de suporte]({{site.baseurl}}/braze_support) para mais detalhes.
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

## Etapa 1: Criar uma nova campanha {#step-1-create-a-new-campaign}

Para criar uma nova campanha de e-mail de transação, crie uma campanha e selecione **Transactional Email** como seu canal de envio de mensagens.

![Menu suspenso Criar campanha com a opção de e-mail de transação destacada.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Agora, você pode prosseguir para configurar sua campanha de e-mail de transação.

## Etapa 2: Configurar sua campanha {#step-2-configure-your-campaign}

O fluxo de criação de campanha para campanhas de e-mail de transação é simplificado em comparação com o de uma [campanha de e-mail padrão]({{site.baseurl}}/user_guide/channels/email/html_editor) para garantir que seu e-mail de transação crítico para o negócio possa alcançar todos os usuários.

Como resultado, você notará que várias configurações com as quais pode estar familiarizado de outros tipos de campanha da Braze não são necessárias ao configurar este tipo de campanha:

- A etapa **Entrega** foi simplificada para remover opções de agendamento. Os e-mails de transação sempre serão disparados pela REST API da Braze usando o ID da campanha exibido na página **Entrega**. Configurações adicionais, como controles de reelegibilidade e configurações de limite de frequência, também foram removidas para confirmar que todos os usuários estejam acessíveis para esses alertas transacionais críticos quando seu serviço dispara uma solicitação de envio.
- A etapa **Público-alvo** foi removida. Como os e-mails de transação inscrevem toda a sua base de usuários como elegível (incluindo usuários que cancelaram a inscrição), não há necessidade de especificar filtros ou segmentos. Portanto, se você tiver alguma lógica para aplicar sobre quem deve receber esta mensagem, recomendamos aplicar essa lógica antes de decidir se deve fazer a solicitação de API para a Braze para disparar a mensagem para um usuário específico.
- A etapa **Conversões** foi removida. Os e-mails de transação não suportam rastreamento de eventos de conversão no momento.

![Fluxo de trabalho Redigir, Entrega e Confirmar para criar uma campanha de e-mail de transação.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Para configurar sua campanha de e-mail de transação, siga estas etapas:

1. Adicione um nome descritivo para que você possa encontrar os resultados na sua página **Campaigns** depois de enviar suas mensagens.
2. Redija seu e-mail ou selecione a partir de um modelo.
3. Anote seu `campaign_id`. Depois de salvar sua campanha de API, você deve incluir os campos `campaign_id` gerados na sua solicitação de API, conforme indicado no artigo do [endpoint de e-mail de transação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Clique em **Save Campaign** e pronto para iniciar sua campanha de API!

{% alert note %}
A configuração de cancelamento de inscrição com um clique para campanhas de e-mail de transação tem como padrão **Use workspace default**, semelhante a outras campanhas de e-mail. Como isso é destinado a envio de mensagens transacionais, a Braze não adiciona o cancelamento de inscrição com um clique. Para adicionar o cancelamento de inscrição com um clique a este tipo de campanha, [edite esta configuração]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#message-level-one-click-list-unsubscribe) em **Sending Info**.
{% endalert %}

### Tags não permitidas em e-mails de transação {#disallowed-tags-in-transactional-emails}

As Liquid tags `Connected Content` e `Promotion Code` não estão disponíveis em campanhas de e-mail de transação.

Usar a tag `Connected Content` exige que a Braze faça uma solicitação de API externa durante nosso processo de envio, o que pode desacelerar o processo de envio de mensagens se o serviço externo que solicitamos estiver com latência. Da mesma forma, a tag `Promotion Code` exige que a Braze realize processamento adicional para avaliar a disponibilidade de uma promoção antes do envio, o que pode desacelerar o processo de envio caso uma não esteja disponível.

Como resultado, não suportamos a inclusão de tags `Connected Content` ou `Promotion Code` em nenhum campo da sua campanha de e-mail de transação.