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

As campanhas da API são normalmente usadas para envio de mensagens transacionais. Ao criar campanhas da API (não [campanhas disparadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)), o dashboard da Braze é usado apenas para gerar um `campaign_id`, que permite rastrear a análise de dados para relatórios de campanha. Também é possível gerar um ID de variação de mensagem, que é diferente para cada variante da sua campanha.

Em seguida, você enviará essas informações à sua equipe de desenvolvimento para serem usadas na solicitação da API, juntamente com:
- Cópia da campanha
- Participação do público
- Ativos

Após o início da campanha, você pode visualizar os resultados no dashboard. As campanhas da API usam as [APIs de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) da Braze, que têm as mesmas opções detalhadas de relatórios e redirecionamento que as campanhas criadas completamente por meio do dashboard.

{% alert warning %}
Como as campanhas da API são normalmente transacionais, todos os usuários são elegíveis para campanhas da API, mesmo os do seu grupo de controle global. Um cabeçalho de [cancelamento de inscrição na lista com um clique]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe) não é adicionado a esses envios. Se quiser adicionar um cabeçalho de cancelamento de inscrição com um clique a todas as campanhas da API, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Criar uma nova campanha {#create-a-new-campaign}

Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**, depois selecione **API Campaigns**. Agora, você pode prosseguir com a configuração da sua campanha de API.

Uma [campanha disparada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) é diferente de uma campanha de API.

## Configure sua campanha {#configure-your-campaign}

Para configurar sua campanha, siga as etapas a seguir:

1. Adicione um título descritivo para que você possa encontrar os resultados na página de Campaigns depois de enviar suas mensagens.
2. Selecione **Add Message** e adicione os tipos de mensagem incluídos na sua campanha de API. Isso permite gerar um `campaign_id` e um ID de variante de mensagem, que é diferente para cada canal incluído.
3. Opcionalmente, você pode adicionar um evento de conversão para rastrear conversões de usuários em uma ação ou meta de campanha específica.
4. Selecione **Save Campaign** e pronto para começar sua campanha de API!

## Chamadas de API {#api-calls}

Depois de salvar sua Campaign de API, inclua o seguinte na sua solicitação de API:
- Os campos `campaign_id` gerados com sua solicitação de API, conforme indicado nos [Endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).
- Um [objeto de mensagem]({{site.baseurl}}/api/objects_filters#messaging-objects) para cada plataforma incluída na Campaign. No objeto de mensagem, forneça o ID da variante da mensagem. Isso especifica que as estatísticas devem ser coletadas e exibidas sob essa variante. Os seguintes objetos de mensagem são compatíveis: Android, Content Cards, e-mail, iOS, Kindle, SMS/MMS, web push e webhook.

### Adicionando anexos de e-mail {#adding-email-attachments}

Para adicionar anexos a e-mails de Campaigns de API, inclua um array `attachments` no [objeto de e-mail]({{site.baseurl}}/api/objects_filters/messaging/email_object). Você pode referenciar um modelo de e-mail criado no editor de arrastar e soltar ou no editor de HTML fornecendo o `email_template_id` no objeto de e-mail e, em seguida, adicionar anexos por meio da chamada de API.

Para detalhes sobre anexos, limites de tamanho e práticas recomendadas, consulte [Exemplo de objeto de e-mail com anexo]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).