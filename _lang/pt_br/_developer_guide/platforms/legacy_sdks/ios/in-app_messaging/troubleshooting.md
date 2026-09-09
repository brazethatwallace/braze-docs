---
nav_title: Solução de problemas
article_title: Solução de problemas de envio de mensagens no app para iOS
platform: iOS
page_order: 7
description: "Este artigo de referência aborda os possíveis tópicos de solução de problemas de mensagens no app do iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Solução de problemas em mensagens no app {#troubleshoot-in-app-messages}

## Impressões {#impressions}

### A análise de dados de impressões ou cliques não está sendo registrada {#impression-or-click-analytics-arent-being-logged}

Se você configurou um delegate de mensagem no app para lidar manualmente com a exibição da mensagem ou ações de clique, será necessário registrar manualmente os cliques e as impressões na mensagem no app.

#### As impressões estão abaixo do esperado {#impressions-are-lower-than-expected}

Os disparadores levam tempo para sincronizar com o dispositivo no início da sessão, então pode haver uma condição de corrida se os usuários registrarem um evento ou compra logo após o início da sessão. Uma possível solução seria alterar a Campaign para disparar com base no início da sessão e, em seguida, segmentar pelo evento ou compra desejado. Note que isso entregaria a mensagem no app no próximo início de sessão após o evento ter ocorrido.

## A mensagem no app esperada não foi exibida {#expected-in-app-message-did-not-display}

A maioria dos problemas com mensagens no app pode ser dividida em duas categorias principais: entrega e exibição. Para solucionar por que uma mensagem no app esperada não foi exibida no seu dispositivo, primeiro confirme que a [mensagem no app foi entregue ao dispositivo](#troubleshooting-in-app-message-delivery) e, em seguida, [solucione problemas de exibição da mensagem](#troubleshooting-in-app-message-display).

### Entrega de mensagens no app {#troubleshooting-in-app-message-delivery}

O SDK solicita mensagens no app dos servidores da Braze no início da sessão. Para verificar se as mensagens no app estão sendo entregues ao seu dispositivo, confirme que elas estão sendo solicitadas pelo SDK e retornadas pelos servidores da Braze.

#### Verifique se as mensagens estão sendo solicitadas e retornadas {#check-if-messages-are-requested-and-returned}

1. Adicione-se como [usuário teste]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) no dashboard.
2. Configure uma Campaign de mensagem no app direcionada ao seu usuário.
3. Confirme que uma nova sessão ocorra no seu app.
4. Use o [registro de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se o seu dispositivo está solicitando mensagens no app no início da sessão. Encontre a solicitação do SDK associada ao evento de início de sessão do seu usuário teste.
  - Se o seu app deveria solicitar mensagens no app disparadas, você verá `trigger` no campo **Requested Responses** em **Response Data**.
  - Se o seu app deveria solicitar mensagens no app originais, você verá `in_app` no campo **Requested Responses** em **Response Data**.
5. Use o [registro de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se as mensagens no app corretas estão sendo retornadas nos dados de resposta.<br>![Entradas do registro de usuários de eventos para solicitações de mensagens no app.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Solução de problemas para mensagens não solicitadas {#troubleshoot-messages-not-being-requested}

Se suas mensagens no app não estão sendo solicitadas, seu app pode não estar rastreando sessões corretamente, pois as mensagens no app são atualizadas no início da sessão. Além disso, confirme que seu app está realmente iniciando uma sessão com base na semântica de timeout de sessão do app:

![A solicitação do SDK encontrada no registro de usuários de eventos exibindo um evento de início de sessão bem-sucedido.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Solução de problemas para mensagens não retornadas {#troubleshoot-messages-not-being-returned}

Se suas mensagens no app não estão sendo retornadas, provavelmente há um problema de direcionamento da Campaign:

- Seu Segment não contém o seu usuário.
  - Verifique a guia [**Engajamento**]({{ site.baseurl }}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) do seu usuário para confirmar se o Segment correto aparece em **Segments**.
- Seu usuário já recebeu a mensagem no app anteriormente e não era elegível para recebê-la novamente.
  - Verifique as [configurações de reelegibilidade da Campaign]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) na etapa **Entrega** do **criador de Campaign** e confirme se as configurações de reelegibilidade estão alinhadas com a sua configuração de teste.
- Seu usuário atingiu o limite de frequência da Campaign.
  - Verifique as [configurações de limite de frequência]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) da Campaign e confirme se estão alinhadas com a sua configuração de teste.
- Se havia um grupo de controle na Campaign, seu usuário pode ter caído no grupo de controle.
  - Você pode verificar se isso aconteceu criando um Segment com um filtro de variante de Campaign recebida, onde a variante de Campaign está definida como **Controle**, e verificando se o seu usuário caiu nesse Segment.
  - Ao criar Campaigns para fins de teste de integração, certifique-se de não adicionar um grupo de controle.

### Exibição de mensagens no app {#troubleshooting-in-app-message-display}

Se o seu app está solicitando e recebendo mensagens no app com sucesso, mas elas não estão sendo exibidas, alguma lógica no dispositivo pode estar impedindo a exibição:

- Mensagens no app disparadas são limitadas com base no [intervalo mínimo de tempo entre disparos]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/in-app_message_delivery#minimum-time-interval-between-triggers), que é de 30 segundos por padrão.
- Se você configurou um delegate para personalizar o tratamento de mensagens no app, verifique o delegate para confirmar que ele não está afetando a exibição das mensagens no app.
- Falhas no download de imagens impedirão a exibição de mensagens no app que contenham imagens. Os downloads de imagens sempre falharão se o framework `SDWebImage` não estiver integrado corretamente. Verifique os logs do dispositivo para confirmar que os downloads de imagens não estão falhando.
- Se a orientação do dispositivo não correspondeu à orientação especificada pela mensagem no app, a mensagem no app não será exibida. Confirme que o seu dispositivo está na orientação correta.