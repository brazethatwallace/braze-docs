---
nav_title: Solução de problemas
article_title: Solução de problemas de notificação por push para iOS
platform: iOS
page_order: 30
description: "Este artigo de referência aborda possíveis tópicos de solução de problemas para sua implementação do push para iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Solução de problemas {#push-troubleshooting}

## Noções básicas sobre o fluxo de trabalho Braze/APNs {#understanding-the-brazeapns-workflow}

O serviço de Notificações por Push da Apple (APNs) é a infraestrutura da Apple para o envio de notificações por push para aplicativos iOS e OS X. Aqui está a estrutura simplificada de como as notificações por push são ativadas para os dispositivos dos seus usuários e como a Braze pode enviar notificações por push para eles:

1. Você configura o certificado de push e o perfil de provisionamento
2. Os dispositivos se registram no APNs e fornecem à Braze os tokens de push
3. Você lança uma Campaign de push da Braze
4. A Braze remove tokens inválidos

### Etapa 1: Configuração do certificado de push e do perfil de provisionamento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Ao desenvolver seu app, você precisará criar um certificado SSL para ativar notificações por push. Este certificado será incluído no perfil de provisionamento com o qual seu app é construído e também precisará ser enviado para o dashboard da Braze. O certificado permite que a Braze informe ao APNs que estamos autorizados a enviar notificações por push em seu nome.

Há dois tipos de [perfis de provisionamento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) e certificados: desenvolvimento e distribuição. Recomendamos usar apenas perfis e certificados de distribuição para evitar qualquer confusão. Se você optar por usar perfis e certificados diferentes para desenvolvimento e distribuição, certifique-se de que o certificado enviado para o dashboard corresponda ao perfil de provisionamento que você está usando no momento.

{% alert warning %}
Não altere o ambiente do certificado de push (desenvolvimento versus produção). Alterar o certificado de push para o ambiente errado pode levar a que os seus usuários tenham o token por push removido acidentalmente, tornando-os inalcançáveis por push.
{% endalert %}

#### Etapa 2: Os dispositivos se registram no APNs e fornecem à Braze os tokens de push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Quando os usuários abrirem seu app, eles serão solicitados a aceitar notificações por push. Se aceitarem este prompt, o APNs gerará um token por push para aquele dispositivo específico. O SDK do iOS enviará imediatamente e de forma assíncrona o token por push para os apps que usam a [política de descarga automática]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) padrão. Depois que tivermos um token por push associado a um usuário, ele aparecerá como "Push Registrado" no dashboard em seu perfil de usuário na guia **Engajamento** e será elegível para receber notificações por push das Campaigns da Braze.

{% alert note %}
A partir do Xcode 14, você pode testar notificações por push remotas em um simulador de iOS.
{% endalert %}

#### Etapa 3: Lançamento de uma Campaign de push da Braze {#step-3-launching-a-braze-push-campaign}

Quando uma Campaign de push for lançada, a Braze fará solicitações ao APNs para entregar sua mensagem. A Braze usará o certificado push SSL carregado no dashboard para autenticar e verificar que temos permissão para enviar notificações por push para os tokens de push fornecidos. Se um dispositivo estiver online, a notificação deve ser recebida logo após o envio da Campaign. Note que a Braze define a [data de expiração](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) padrão do APNs para notificações como 30 dias.

#### Etapa 4: Remoção de tokens inválidos {#step-4-removing-invalid-tokens}

Se o [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informar que qualquer um dos tokens por push para os quais estávamos tentando enviar uma mensagem é inválido, removeremos esses tokens dos perfis de usuário aos quais eles estavam associados.

## Utilização dos registros de erros do push {#utilizing-the-push-error-logs}

A Braze fornece um registro de erros de notificação por push dentro do **Registro de atividades de envio de mensagem**. Este registro de erros fornece uma variedade de avisos que podem ser muito úteis para identificar por que suas Campaigns não estão funcionando como esperado. Clicar em uma mensagem de erro irá redirecioná-lo para a documentação relevante para ajudá-lo a solucionar um incidente específico.

![Logs de erro de push exibindo a hora em que o erro ocorreu, o nome do app, o canal, o tipo de erro e a mensagem de erro.]({% image_buster /assets/img_archive/message_activity_log.png %})

Os erros comuns que podem ser vistos aqui incluem notificações específicas do usuário, como ["Received Unregistered Sending to Push Token"](#received-unregistered-sending).

Além disso, a Braze também apresenta um changelog de push no perfil do usuário na guia **Engajamento**. Esse changelog contém insights sobre o comportamento de registro de push, como invalidação de token, erros de registro de push, tokens transferidos para novos usuários, etc.

![Exemplo animado de cartão de conteúdo.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Problemas de registro de push {#push-registration-issues}

Para adicionar verificação à lógica de registro de push do seu aplicativo, implemente [testes unitários de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Nenhum prompt de registro de push {#no-push-registration-prompt}

Se o aplicativo não solicitar que você se registre para notificações por push, provavelmente há um problema com a integração do seu registro de push. Certifique-se de ter seguido nossa [documentação]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) e integrado corretamente nosso registro de push. Você também pode definir pontos de interrupção em seu código para garantir que o código de registro de push esteja em execução.

#### Nenhum usuário "push registrado" exibido no dashboard {#no-push-registered-users-showing-in-the-dashboard}

- Verifique se o seu app está solicitando permissão para notificações por push. Normalmente, este prompt aparecerá na primeira vez que você abrir o app, mas pode ser programado para aparecer em outro momento. Se não aparecer onde deveria, o problema provavelmente está na configuração básica das capacidades de push do seu app.
  - Verifique se as etapas da [integração push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) foram concluídas com êxito.
  - Verifique se o perfil de provisionamento com o qual seu app foi criado inclui permissões para push. Certifique-se de que está baixando todos os perfis de provisionamento disponíveis da sua conta de desenvolvedor Apple. Para confirmar isso, faça o seguinte:
    1. No Xcode, acesse **Preferences > Accounts** (ou use o atalho de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecione o ID Apple que você usa para sua conta de desenvolvedor e clique em **View Details**.
    3. Na próxima página, clique em **<i class="fas fa-redo-alt"></i> Refresh** e confirme que você está baixando todos os perfis de provisionamento disponíveis.
- Verifique se você [ativou corretamente a capacidade de push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities) em seu app.
- Verifique se o seu perfil de provisionamento de push corresponde ao ambiente em que você está testando. Os certificados universais podem ser configurados no dashboard da Braze para enviar para o ambiente APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
- Verifique se você está chamando nosso método `registerPushToken` definindo um ponto de interrupção no código.
- Verifique se você está em um dispositivo (push não funcionará em um simulador) e se tem uma boa conectividade de rede.

## Dispositivos não estão recebendo notificações por push {#devices-not-receiving-push-notifications}

### Usuários não estão mais "registrados para push" após o envio de uma notificação por push {#users-no-longer-push-registered-after-sending-a-push-notification}

Provavelmente indica que o usuário tinha um token por push inválido. Isso pode acontecer por várias razões:

#### Incompatibilidade entre o certificado do dashboard e do app {#dashboard-and-app-certificate-mismatch}

Se o certificado de push que você carregou no dashboard não for o mesmo no perfil de provisionamento com o qual seu app foi desenvolvido, o APNs rejeitará o token. Verifique se você carregou o certificado correto e completou outra sessão no app antes de tentar outra notificação de teste.

##### Desinstalações {#uninstalls}

Se um usuário desinstalou seu aplicativo, seu token por push será inválido e removido no próximo envio.

##### Regenerando seu perfil de provisionamento {#regenerating-your-provisioning-profile}

Como último recurso, começar do zero e criar um novo perfil de provisionamento pode resolver erros de configuração que surgem ao trabalhar com vários ambientes, perfis e aplicativos ao mesmo tempo. Existem muitos fatores na configuração de notificações por push para apps iOS, então, às vezes, é melhor tentar novamente desde o início. Isso também ajudará a isolar o problema se você precisar continuar solucionando problemas.

#### Usuários ainda estão "registrados para push" após o envio de uma notificação por push {#users-still-push-registered-after-sending-a-push-notification}

##### App está em primeiro plano {#app-is-foregrounded}

Nas versões do iOS que não integram push via o framework `UserNotifications`, se o app estiver em primeiro plano quando a mensagem push for recebida, ela não será exibida. Você deve colocar o app em segundo plano nos seus dispositivos de teste antes de enviar mensagens de teste.

##### Notificação de teste agendada incorretamente {#test-notification-scheduled-incorrectly}

Verifique a programação que você definiu para sua mensagem de teste. Se estiver definida para entrega no fuso horário local ou [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), você pode simplesmente não ter recebido a mensagem ainda (ou ter o app em primeiro plano quando foi recebida).

#### Usuário não "registrado para push" para o app que está sendo testado {#user-not-push-registered-for-the-app-being-tested}

Verifique o perfil do usuário para o qual você está tentando enviar uma mensagem de teste. Na guia **Engajamento**, deve haver uma lista de "apps que aceitam push". Verifique se o app para o qual você está tentando enviar mensagens de teste está nesta lista. Os usuários aparecerão como "Push Registrado" se tiverem um token por push para qualquer app no seu espaço de trabalho, então isso pode ser algo como um falso positivo.

O seguinte indicaria um problema com o registro de push ou que o token do usuário foi retornado à Braze como inválido pelo APNs após o envio:

![Um perfil de usuário exibindo as configurações de contato de um usuário. Aqui, você pode ver para quais apps o push está registrado.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## As mensagens push não estão sendo enviadas {#push-messages-not-sending}

Para solucionar problemas de notificações por push que não estão sendo enviadas, consulte [Solução de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Erros do registro de atividade de mensagens {#message-activity-log-errors}

### Recebido envio não registrado para token por push {#received-unregistered-sending}

- Certifique-se de que o token por push enviado para a Braze a partir do método `[[Appboy sharedInstance] registerPushToken:]` seja válido. Consulte o **Registro de atividades de envio de mensagem** para ver o token por push. Deve parecer algo como `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, uma longa string contendo uma mistura de letras e números. Se seu token por push parecer diferente, verifique seu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) para enviar os tokens por push à Braze.
- Verifique se o seu perfil de provisionamento de push corresponde ao ambiente que está testando. Os certificados universais podem ser configurados no dashboard da Braze para enviar para o ambiente APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
 - Verifique se o token por push que você enviou para a Braze corresponde ao perfil de provisionamento que você usou para desenvolver o app de onde você enviou o token por push.

#### Token de dispositivo não para tópico {#device-token-not-for-topic}

Este erro indica que o certificado de push do seu app e o ID do pacote não correspondem. Verifique se o certificado de push que você enviou para a Braze corresponde ao perfil de provisionamento usado para construir o app do qual o token por push foi enviado.

#### Envio de BadDeviceToken para token por push {#baddevicetoken-sending-to-push-token}

O `BadDeviceToken` é um código de erro do APNs e não se origina da Braze. Pode haver várias razões para essa resposta ser retornada, incluindo as seguintes:

- O app recebeu um token por push que era inválido para as credenciais enviadas para o dashboard.
- Push foi desativado para este espaço de trabalho.
- O usuário optou por não receber push.
- O app foi desinstalado.
- A Apple atualizou o token por push, o que invalidou o token antigo.
- O app foi construído para um ambiente de produção, mas as credenciais de push carregadas na Braze estão configuradas para um ambiente de desenvolvimento (ou vice-versa).

## Problemas após a entrega do push {#issues-after-push-delivery}

Para adicionar verificação ao tratamento de push do seu aplicativo, implemente [testes unitários de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Cliques de push não registrados {#push-clicks-not-logged}

- Se isso estiver ocorrendo apenas no iOS 10, certifique-se de ter seguido as etapas de integração push para o [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling).
- A Braze não gerencia notificações por push recebidas silenciosamente em primeiro plano (por exemplo, comportamento padrão de push em primeiro plano antes do framework `UserNotifications`). Isso significa que os links não serão abertos e os cliques de push não serão registrados. Se seu app ainda não estiver integrado com o framework `UserNotifications`, a Braze não gerenciará as notificações por push quando o estado do app for `UIApplicationStateActive`. Certifique-se de que o seu app não atrase as chamadas para os nossos [métodos de tratamento de push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling); caso contrário, o SDK do iOS poderá tratar as notificações por push como eventos push silenciosos em primeiro plano e não as processará.

#### Links da web não abrem com cliques em push {#web-links-from-push-clicks-not-opening}

O iOS 9 e posteriores exigem que os links estejam em conformidade com o ATS para serem abertos em visualizações da web. Certifique-se de que seus links da web usem HTTPS. Consulte nosso artigo sobre [conformidade com ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats) para saber mais.

#### Deep links de cliques push não abrem {#deep-links-from-push-clicks-not-opening}

A maior parte do código que lida com deep links também lida com aberturas de push. Primeiro, confira se as aberturas do push estão sendo registradas. Caso contrário, [corrija esse problema](#push-clicks-not-logged) (já que a correção geralmente corrige o tratamento de links).

Se as aberturas estiverem sendo registradas, verifique se é um problema com o deep link em geral ou com o tratamento do clique de push com deep linking. Para fazer isso, teste para ver se um deep link de um clique de mensagem no app funciona.

#### Poucas ou nenhuma abertura direta {#few-or-no-direct-opens}

Se pelo menos um usuário abrir a notificação por push do iOS, mas poucas ou nenhuma *abertura direta* for registrada na Braze, pode haver um problema com a [integração do SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview). Lembre-se de que *as aberturas diretas* não são registradas para envios de teste ou notificações por push silenciosas.

- Certifique-se de que as mensagens não estejam sendo enviadas como [notificações por push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications). A mensagem deve ter texto no título ou no corpo para não ser considerada silenciosa.
- Verifique novamente as seguintes etapas do [guia de integração push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration):
   - [Registre-se para push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns): Em cada lançamento de app, de preferência em `application:didFinishLaunchingWithOptions:`, o código da etapa 3 precisa ocorrer. A propriedade delegate de `UNUserNotificationCenter.current()` precisa ser atribuída a um objeto que implemente `UNUserNotificationCenterDelegate` e contenha o método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`.
   - [Ativar o tratamento de push]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling): Verifique se o método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` foi implementado.