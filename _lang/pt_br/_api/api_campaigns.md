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

Envie essas informações à sua equipe de desenvolvimento para serem usadas na solicitação da API, juntamente com:
- Cópia da campanha
- Participação do público
- Ativos

Após o início da campanha, você pode visualizar os resultados no dashboard. As campanhas da API usam as [APIs de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) da Braze, que têm as mesmas opções detalhadas de relatórios e redirecionamento que as campanhas criadas completamente por meio do dashboard.

Como as campanhas da API sempre incluem um `campaign_id`, seus envios são refletidos nas estatísticas do dashboard. Se você chamar [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) sem um `campaign_id`, a Braze não incrementa essas métricas — os envios ainda aparecem no [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), mas não nas métricas de desempenho de e-mail no dashboard.

{% alert warning %}
Como as campanhas da API são normalmente transacionais, todos os usuários são elegíveis para campanhas da API, mesmo os do seu grupo de controle global. Um cabeçalho de [cancelamento de inscrição na lista com um clique]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) não é adicionado a esses envios por padrão. Para adicionar um cabeçalho de cancelamento de inscrição com um clique a uma campanha da API, consulte [Adicionar cancelamento de inscrição com um clique a campanhas da API](#add-one-click-list-unsubscribe-to-api-campaigns). Para adicionar um cabeçalho de cancelamento de inscrição com um clique a todas as campanhas da API, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Criar uma nova campanha {#create-a-new-campaign}

Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**, depois selecione **API Campaigns**. Agora, você pode prosseguir com a configuração da sua campanha de API.

Uma [campanha disparada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) é diferente de uma campanha de API.

## Configure sua campanha {#configure-your-campaign}

Para configurar sua campanha, siga as etapas a seguir:

1. Adicione um título descritivo para que você possa encontrar os resultados na página de Campaigns após enviar suas mensagens.
2. Selecione **Add Message** e adicione os tipos de mensagem incluídos na sua campanha de API. Isso permite gerar um `campaign_id` e um ID de variação de mensagem, que é diferente para cada canal incluído.
3. Opcionalmente, você pode adicionar um evento de conversão para rastrear conversões de usuários em uma ação ou meta de campanha específica.
4. Selecione **Save Campaign** para iniciar sua campanha de API.

## Chamadas de API {#api-calls}

Após salvar sua Campaign de API, inclua o seguinte na sua solicitação de API:

- Os campos `campaign_id` gerados na sua solicitação de API, conforme indicado nos [Endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).
- Um [objeto de mensagem]({{site.baseurl}}/api/objects_filters#messaging-objects) para cada plataforma incluída na Campaign. No objeto de mensagem, forneça o ID da variante da mensagem. Isso especifica que as estatísticas devem ser coletadas e exibidas nessa variante. Os seguintes objetos de mensagem são compatíveis: Android, Content Cards, e-mail, iOS, Kindle, SMS/MMS, web push e webhook.

## Adicionar cancelamento de inscrição em um clique via lista a Campaigns de API {#add-one-click-list-unsubscribe-to-api-campaigns}

{% raw %}
Por padrão, a Braze não adiciona o cabeçalho de cancelamento de inscrição em um clique via lista a Campaigns de API. Você pode adicionar esse cabeçalho a envios individuais de Campaigns de API incluindo a Liquid tag `{{${set_user_to_one_click_list_unsubscribe}}}` no campo de cabeçalhos de e-mail da sua solicitação de API.
{% endraw %}

Para estar em conformidade com a [RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058) para cancelamento de inscrição em um clique via lista, inclua os cabeçalhos `List-Unsubscribe` e `List-Unsubscribe-Post` na sua solicitação de API:

{% raw %}
```json
{
  "external_user_ids": ["user_id"],
  "messages": {
    "email": {
      "app_id": "your_app_id",
      "subject": "Your Subject",
      "from": "Sender Name <sender@example.com>",
      "body": "<p>Email body content</p>",
      "headers": {
        "List-Unsubscribe": "<{{${set_user_to_one_click_list_unsubscribe}}}>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
      }
    }
  }
}
```
{% endraw %}

{% alert note %}
A inclusão desses cabeçalhos não garante que o cliente de e-mail exiba um botão de cancelamento de inscrição. Os clientes de e-mail decidem se mostram a opção de cancelamento de inscrição com base em fatores como reputação do remetente e conteúdo da mensagem.
{% endalert %}

### Adicionar anexos de e-mail {#add-email-attachments}

Para adicionar anexos a e-mails de Campaigns de API, inclua um array `attachments` no [objeto de e-mail]({{site.baseurl}}/api/objects_filters/messaging/email_object). Você pode fazer referência a um modelo de e-mail criado no editor de arrastar e soltar ou no editor de HTML fornecendo o `email_template_id` no objeto de e-mail e, em seguida, adicionar anexos por meio da chamada de API.

Para detalhes sobre anexos, limites de tamanho e práticas recomendadas, consulte [Exemplo de objeto de e-mail com anexo]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).