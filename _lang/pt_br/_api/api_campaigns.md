---
nav_title: Campanhas da API
article_title: Campanhas da API
page_order: 5
description: "Este artigo de referência aborda como gerar um campaign_id para incluir em suas chamadas de API e como configurar essa campanha."
page_type: reference
tool: Campaigns

---
# Campanhas da API {#api-campaigns}

> Este artigo de referência aborda como gerar um `campaign_id` para incluir em suas chamadas de API e como configurar essa campanha.

As campanhas da API são normalmente usadas para envio de mensagens transacionais. Ao criar campanhas da API (não [campanhas disparadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/)), o dashboard da Braze é usado apenas para gerar um `campaign_id`, que permite rastrear a análise de dados para relatórios de campanha. Também é possível gerar um ID de variação de mensagem, que é diferente para cada variante da sua campanha.

Em seguida, você enviará essas informações à sua equipe de desenvolvimento para serem usadas na solicitação da API, juntamente com:
- Cópia da campanha
- Participação do público
- Ativos

Após o início da campanha, você pode visualizar os resultados no dashboard. As campanhas da API usam as [APIs de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) da Braze, que têm as mesmas opções detalhadas de relatórios e redirecionamento que as campanhas criadas completamente por meio do dashboard.

{% alert warning %}
Como as campanhas da API são normalmente transacionais, todos os usuários são elegíveis para campanhas da API, mesmo os do seu Grupo de controle global. Um cabeçalho de [cancelamento de inscrição na lista com um clique]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe) não é adicionado a esses envios. Se quiser adicionar um cabeçalho de cancelamento de inscrição com um clique a todas as campanhas da API, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Criar uma nova campanha {#create-a-new-campaign}

Acesse **Messaging** > **Campaigns** e selecione **Create Campaign** e, em seguida, selecione **API Campaigns**. Agora, você pode prosseguir com a configuração da sua campanha da API.

Uma [campanha disparada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) é diferente de uma campanha da API.

## Configure sua campanha {#configure-your-campaign}

Para configurar sua campanha, execute as seguintes etapas:

1. Adicione um título descritivo para que possa encontrar os resultados na página de campanhas após o envio das mensagens.
2. Clique em **Add Message** e adicione os tipos de mensagens que serão incluídos na sua campanha da API. Isso permitirá que você gere um `campaign_id` e um ID de variação de mensagem, que é diferente para cada canal incluído.
3. Opcionalmente, você pode adicionar um evento de conversão para rastrear as conversões do usuário em uma ação ou meta de campanha específica.
4. Clique em **Save Campaign** e você estará pronto para iniciar sua campanha da API!

## Chamadas de API {#api-calls}

Depois de salvar sua campanha da API, inclua o seguinte na sua solicitação de API:
- Os campos `campaign_id` gerados na sua solicitação de API, conforme indicado nos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints).
- Um [objeto de mensagem]({{site.baseurl}}/api/objects_filters/#messaging-objects) para cada plataforma incluída na campanha. No objeto de mensagem, forneça o ID de variação da mensagem. Isso especificará que as estatísticas devem ser coletadas e exibidas nessa variante. Os seguintes objetos de mensagem são compatíveis: Android, Content Cards, e-mail, iOS, Kindle, SMS/MMS, push para a web e webhook.