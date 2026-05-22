# Envio de mensagens de teste {#sending-test-messages}

> Antes de enviar uma campanha de mensagens para seus usuários, você pode querer testá-la para garantir que ela esteja correta e funcione da maneira esperada. Você pode usar o dashboard para criar e enviar mensagens de teste com notificações por push, mensagens no app (IAM) ou e-mail.

## Envio de uma mensagem de teste {#sending-a-test-message}

### Etapa 1: Crie um segmento de teste designado <a class="margin-fix" name="test-segment"></a> {#step-1-create-a-designated-test-segment}

Depois de configurar um segmento de teste, você poderá usá-lo para testar qualquer um dos seus canais de envio de mensagens da Braze. Quando configurado corretamente, isso só precisa ser feito uma única vez.

Para configurar um segmento de teste, acesse **Segments** e crie um novo segmento. Selecione **Add Filter** e escolha um dos filtros de teste.

![Uma campanha de teste da Braze exibindo os filtros disponíveis na etapa de direcionamento.]({% image_buster /assets/img_archive/testmessages1.png %})

Com os filtros de teste, é possível garantir que apenas os usuários com um endereço de e-mail específico ou [ID de usuário externo]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) recebam a mensagem de teste.

![Um menu suspenso exibindo vários filtros listados sob um título que diz Testing]({% image_buster /assets/img_archive/testmessages2.png %})

Os filtros de endereço de e-mail e de ID de usuário externo oferecem as seguintes opções:

| Operador          | Descrição |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | Isso procurará uma correspondência exata do e-mail ou da ID de usuário que você fornecer. Use essa opção se quiser enviar as campanhas de teste apenas para dispositivos associados a um único e-mail ou ID de usuário. |
| `does not equal` | Use essa opção se quiser excluir um e-mail ou ID de usuário específico das campanhas de teste. |
| `matches`     | Isso encontrará usuários que tenham endereços de e-mail ou IDs de usuário que correspondam a parte do termo de pesquisa fornecido. Isso pode ser usado para encontrar apenas os usuários que têm um endereço `@yourcompany.com`, permitindo o envio de mensagens a todos da sua equipe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create a designated test segment a class="margin-fix" name="test-segment"/a" }

Você pode selecionar vários e-mails específicos usando a opção "`matches`" e separando os endereços de e-mail com um caractere &#124;. Por exemplo: "`matches`" "`email1@braze.com` &#124; `email2@braze.com`". Você também pode combinar vários operadores. Por exemplo, o segmento de teste pode incluir um filtro de endereço de e-mail que "`matches`" "`@braze.com`" e outro filtro que "`does not equal`" "`sales@braze.com`".

Depois de adicionar os filtros de teste ao seu segmento de teste, é possível verificar se ele está funcionando selecionando **Preview** ou **Settings** > **CSV Export All User Data** para exportar os dados de usuários desse segmento para um arquivo CSV.

![Uma seção de uma campanha da Braze intitulada Segment Details]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
Exportar os dados de usuários do segmento para um arquivo CSV é o método de verificação mais preciso, pois a pré-visualização mostrará apenas uma amostra dos seus usuários e poderá não incluir todos os usuários.
{% endalert %}

### Etapa 2: Envie a mensagem {#step-2-send-the-message}

Você pode enviar uma mensagem usando o dashboard da Braze ou a linha de comando.

{% tabs local %}
{% tab Using the dashboard %}
{% subtabs %}
{% subtab push or in-app message %}
Para enviar notificações por push de teste ou mensagens no app, você precisa direcionar o segmento de teste criado anteriormente. Comece criando sua Campaign e seguindo os passos habituais. Quando chegar à etapa **Target Audiences**, selecione seu segmento de teste no menu suspenso.

![Uma campanha de teste da Braze exibindo os segmentos disponíveis na etapa de direcionamento.]({% image_buster /assets/img_archive/test_segment.png %})

Confirme sua Campaign e lance-a para testar a notificação por push e as mensagens no app.

{% alert note %}
Certifique-se de selecionar **Allow users to become re-eligible to receive campaign** na parte **Schedule** do criador de campanhas se você pretende usar uma única Campaign para enviar uma mensagem de teste para si mesmo mais de uma vez.
{% endalert %}
{% endsubtab %}

{% subtab email message %}
Se você estiver apenas testando mensagens de e-mail, não é necessário configurar um segmento de teste. Na primeira etapa do criador de campanhas, onde você compõe a mensagem de e-mail da sua Campaign, clique em **Send Test** e insira o endereço de e-mail para o qual você deseja enviar um e-mail de teste.

![Uma campanha da Braze com a guia Send Test selecionada]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Você também pode ativar ou desativar [TEST (ou SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) sendo anexado às suas mensagens de teste.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Using the command line %}
Como alternativa, você pode enviar uma única notificação usando cURL e a [API de envio de mensagens da Braze]({{site.baseurl}}/api/endpoints/messaging/). Note que esses exemplos fazem uma solicitação usando a instância `US-01`. Para descobrir a sua, consulte [Endpoints de API]({{site.baseurl}}/api/basics/#endpoints).

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": {
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

Substitua o seguinte:

| Espaço reservado         | Descrição                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | Sua chave de API da Braze usada para autenticação. Na Braze, acesse **Settings** > **API Keys** para localizar sua chave. |
| `EXTERNAL_USER_ID` | O ID de usuário externo usado para enviar sua mensagem a um usuário específico. Na Braze, acesse **Audience** > **Search Users** e pesquise um usuário. |
| `CUSTOM_KEY`         | (Opcional) Uma chave personalizada para dados adicionais.              |
| `CUSTOM_VALUE`       | (Opcional) Um valor personalizado atribuído à sua chave personalizada.    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Send the message" }
{% endtab %}
{% endtabs %}

## Limitações do teste {#test-limitations}

Existem algumas situações em que as mensagens de teste não têm paridade completa de recursos com o lançamento de uma Campaign ou Canvas para um conjunto real de usuários. Nesses casos, para validar esse comportamento, você deve lançar a Campaign ou Canvas para um conjunto limitado de usuários de teste.

- A visualização da [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) da Braze a partir das **Mensagens de Teste** fará com que o botão de envio fique acinzentado.
- O cabeçalho list-unsubscribe não está incluído nos e-mails enviados pela funcionalidade de mensagem de teste.
- Para mensagens no app e Content Cards, o usuário de destino deve ter um token por push para o dispositivo de destino.