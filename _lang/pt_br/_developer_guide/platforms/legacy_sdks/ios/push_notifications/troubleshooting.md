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

## Entendendo o fluxo de trabalho Braze/APNs {#understanding-the-brazeapns-workflow}

O serviço de Notificações por Push da Apple (APN) é a infraestrutura da Apple para o envio de notificações por push para aplicativos iOS e OS X. Aqui está a estrutura simplificada de como as notificações por push são ativadas para os dispositivos dos seus usuários e como a Braze pode enviar notificações por push para eles:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Etapa 1: Configurando o certificado push e o perfil de provisionamento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Ao desenvolver seu app, crie um certificado SSL para ativar as notificações por push. Esse certificado é incluído no perfil de provisionamento com o qual seu app é compilado e também deve ser enviado para o dashboard da Braze. O certificado permite que a Braze informe ao APN que estamos autorizados a enviar notificações por push em seu nome.

Existem dois tipos de [perfis de provisionamento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) e certificados: desenvolvimento e distribuição. Recomendamos usar apenas perfis e certificados de distribuição para evitar qualquer confusão. Se você optar por usar perfis e certificados diferentes para desenvolvimento e distribuição, certifique-se de que o certificado enviado ao dashboard corresponda ao perfil de provisionamento que você está usando atualmente.

{% alert warning %}
Não altere o ambiente do certificado push (desenvolvimento versus produção). Alterar o certificado push para o ambiente errado pode fazer com que os tokens por push dos seus usuários sejam removidos acidentalmente, tornando-os inacessíveis por push.
{% endalert %}

#### Etapa 2: Os dispositivos se registram no APN e fornecem tokens por push à Braze {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Quando os usuários abrem seu app, eles serão solicitados a aceitar notificações por push. Se aceitarem essa solicitação, o APN gerará um token por push para aquele dispositivo específico. O SDK para iOS enviará imediata e assincronamente o token por push para apps que usam a [política de envio automático]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) padrão. Depois que tivermos um token por push associado a um usuário, ele aparecerá como "Push Registered" no dashboard, em seu perfil de usuário na guia **Engajamento**, e será elegível para receber notificações por push de Campaigns da Braze.

{% alert note %}
A partir do Xcode 14, você pode testar notificações por push remotas em um simulador iOS.
{% endalert %}

#### Etapa 3: Lançando uma Campaign de push na Braze {#step-3-launching-a-braze-push-campaign}

Quando uma Campaign de push é lançada, a Braze fará solicitações ao APN para entregar sua mensagem. A Braze usará o certificado SSL de push enviado no dashboard para autenticar e verificar que estamos autorizados a enviar notificações por push para os tokens por push fornecidos. Se um dispositivo estiver online, a notificação deverá ser recebida logo após o envio da Campaign. A Braze define a [data de expiração](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) padrão do APN para notificações como 30 dias.

#### Etapa 4: Removendo tokens inválidos {#step-4-removing-invalid-tokens}

Se o [APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informar que algum dos tokens por push para os quais estávamos tentando enviar uma mensagem é inválido, removemos esses tokens dos perfis de usuário aos quais estavam associados.

## Utilizando os registros de erros de push {#utilizing-the-push-error-logs}

A Braze fornece um registro de erros de notificações por push no **Registro de atividade de mensagens**. Esse registro de erros oferece diversos alertas que podem ser muito úteis para identificar por que suas Campaigns não estão funcionando como esperado. Ao selecionar uma mensagem de erro, você é redirecionado para a documentação relevante que ajuda a solucionar um incidente específico.

![Registros de erros de push exibindo o horário em que o erro ocorreu, o nome do app, o canal, o tipo de erro e a mensagem de erro.]({% image_buster /assets/img_archive/message_activity_log.png %})

Erros comuns que você pode encontrar aqui incluem notificações específicas do usuário, como ["Received Unregistered Sending to Push Token"](#received-unregistered-sending).

Além disso, a Braze também fornece um changelog de push no perfil de usuário, na guia **Engajamento**. Esse changelog oferece insights sobre o comportamento de registro de push, como invalidação de token, erros de registro de push, tokens sendo transferidos para novos usuários, etc.

![Exemplo animado de cartão de conteúdo.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Problemas de registro de push {#push-registration-issues}

Para adicionar verificação à lógica de registro de push do seu aplicativo, implemente [testes unitários de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Nenhum prompt de registro de push {#no-push-registration-prompt}

Se o aplicativo não solicitar que você se registre para notificações por push, provavelmente há um problema com a integração do registro de push. Certifique-se de ter seguido nossa [documentação]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) e integrado corretamente nosso registro de push. Você também pode definir breakpoints no seu código para garantir que o código de registro de push está sendo executado.

#### Nenhum usuário "registrado para push" aparecendo no dashboard {#no-push-registered-users-showing-in-the-dashboard}

- Verifique se o seu app está solicitando que você permita notificações por push. Normalmente, esse prompt aparece na primeira abertura do app, mas pode ser programado para aparecer em outro lugar. Se ele não aparecer onde deveria, o problema provavelmente está na configuração básica das capacidades de push do seu app.
  - Verifique se as etapas para a [integração de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) foram concluídas com sucesso.
  - Verifique se o perfil de provisionamento com o qual seu app foi compilado inclui permissões para push. Certifique-se de que está baixando todos os perfis de provisionamento disponíveis da sua conta de desenvolvedor Apple. Para confirmar isso, siga as seguintes etapas:
    1. No Xcode, navegue até **Preferences > Accounts** (ou use o atalho de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecione o Apple ID que você usa para sua conta de desenvolvedor e clique em **View Details**.
    3. Na próxima página, clique em **<i class="fas fa-redo-alt"></i> Refresh** e confirme que está baixando todos os perfis de provisionamento disponíveis.
- Verifique se você [ativou corretamente a capacidade de push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities) no seu app.
- Verifique se o perfil de provisionamento de push corresponde ao ambiente em que você está testando. Certificados universais podem ser configurados no dashboard da Braze para enviar para o ambiente de APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
- Verifique se você está chamando nosso método `registerPushToken` definindo um breakpoint no seu código.
- Verifique se você está em um dispositivo (push não funciona em um simulador) e tem boa conectividade de rede.

## Dispositivos que não recebem notificações por push {#devices-not-receiving-push-notifications}

### Usuários não estão mais "registrados para push" após o envio de uma notificação por push {#users-no-longer-push-registered-after-sending-a-push-notification}

Isso provavelmente indica que o usuário tinha um token por push inválido. Isso pode acontecer por vários motivos:

#### Incompatibilidade entre o certificado do dashboard e o do app {#dashboard-and-app-certificate-mismatch}

Se o certificado de push que você enviou no dashboard não for o mesmo do perfil de provisionamento com o qual seu app foi compilado, o APN rejeitará o token. Verifique se você enviou o certificado correto e concluiu outra sessão no app antes de tentar outra notificação de teste.

##### Desinstalações {#uninstalls}

Se um usuário desinstalou seu aplicativo, o token por push dele será inválido e removido no próximo envio.

##### Regenerando seu perfil de provisionamento {#regenerating-your-provisioning-profile}

Como último recurso, começar do zero e criar um perfil de provisionamento totalmente novo pode resolver erros de configuração que surgem ao trabalhar com vários ambientes, perfis e apps ao mesmo tempo. Existem muitas "partes móveis" na configuração de notificações por push para apps iOS, então, às vezes, é melhor tentar novamente desde o início. Isso também ajudará a isolar o problema caso você precise continuar a solução de problemas.

#### Usuários ainda "registrados para push" após o envio de uma notificação por push {#users-still-push-registered-after-sending-a-push-notification}

##### O app está em primeiro plano {#app-is-foregrounded}

Em versões do iOS que não integram push por meio do framework `UserNotifications`, se o app estiver em primeiro plano quando a mensagem push for recebida, ela não será exibida. Você deve colocar o app em segundo plano nos seus dispositivos de teste antes de enviar mensagens de teste.

##### Notificação de teste agendada incorretamente {#test-notification-scheduled-incorrectly}

Verifique o cronograma que você definiu para sua mensagem de teste. Se estiver configurado para entrega no fuso local ou com [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), é possível que você simplesmente ainda não tenha recebido a mensagem (ou que o app estivesse em primeiro plano quando ela foi recebida).

#### Usuário não está "registrado para push" para o app sendo testado {#user-not-push-registered-for-the-app-being-tested}

Verifique o perfil do usuário para quem você está tentando enviar uma mensagem de teste. Na guia **Engajamento**, deve haver uma lista de "apps com push habilitado". Verifique se o app para o qual você está tentando enviar mensagens de teste está nessa lista. Os usuários aparecerão como "Push Registered" se tiverem um token por push para qualquer app no seu espaço de trabalho, então isso pode ser um falso positivo.

O seguinte indicaria um problema com o registro de push ou que o token do usuário foi retornado à Braze como inválido pelo APN após o envio:

![Um perfil de usuário exibindo as configurações de contato de um usuário. Aqui, é possível ver para quais apps o push está registrado.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Mensagens push não estão sendo enviadas {#push-messages-not-sending}

Para solucionar problemas com notificações por push que não estão sendo enviadas, consulte [Solução de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Erros do registro de atividade de mensagens {#message-activity-log-errors}

### Recebido envio não registrado para token por push {#received-unregistered-sending}

- Verifique se o token por push enviado à Braze pelo método `[[Appboy sharedInstance] registerPushToken:]` é válido. Você pode consultar o **Registro de atividade de mensagens** para ver o token por push. Ele deve se parecer com algo como `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, uma string longa contendo uma combinação de letras e números. Se o seu token por push parecer diferente, verifique o seu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) de envio dos tokens por push à Braze.
- Verifique se o perfil de provisionamento de push corresponde ao ambiente em que você está testando. Certificados universais podem ser configurados no dashboard da Braze para enviar ao ambiente de APN de desenvolvimento ou de produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
 - Verifique se o token por push que você enviou à Braze corresponde ao perfil de provisionamento usado para compilar o app do qual o token por push foi enviado.

#### Token de dispositivo não corresponde ao tópico {#device-token-not-for-topic}

Esse erro indica que o certificado de push do seu app e o bundle ID estão incompatíveis. Verifique se o certificado de push enviado à Braze corresponde ao perfil de provisionamento usado para compilar o app do qual o token por push foi enviado.

#### BadDeviceToken ao enviar para token por push {#baddevicetoken-sending-to-push-token}

O `BadDeviceToken` é um código de erro do APN e não é originado pela Braze. Pode haver diversas razões para essa resposta ser retornada, incluindo as seguintes:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Problemas após a entrega de push {#issues-after-push-delivery}

Para adicionar verificação ao tratamento de push do seu aplicativo, implemente [testes unitários de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Cliques em push não registrados {#push-clicks-not-logged}

- Se isso está ocorrendo apenas no iOS 10, verifique se você seguiu as etapas de integração de push para [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling).
- A Braze não trata notificações por push recebidas silenciosamente em primeiro plano (por exemplo, o comportamento padrão de push em primeiro plano antes do framework `UserNotifications`). Isso significa que os links não serão abertos e os cliques em push não serão registrados. Se o seu aplicativo ainda não integrou o framework `UserNotifications`, a Braze não tratará as notificações por push quando o estado do aplicativo for `UIApplicationStateActive`. Você deve garantir que seu app não atrase as chamadas aos nossos [métodos de tratamento de push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling); caso contrário, o SDK para iOS pode tratar as notificações por push como eventos silenciosos de push em primeiro plano e não processá-las.

#### Links da web a partir de cliques em push não abrem {#web-links-from-push-clicks-not-opening}

O iOS 9+ exige que os links estejam em conformidade com ATS para serem abertos em web views. Verifique se seus links da web usam HTTPS. Consulte nosso artigo sobre [conformidade com ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats) para saber mais.

#### Deep links a partir de cliques em push não abrem {#deep-links-from-push-clicks-not-opening}

A maior parte do código que trata deep links também trata aberturas de push. Primeiro, verifique se as aberturas de push estão sendo registradas. Se não estiverem, [corrija esse problema](#push-clicks-not-logged) (pois a correção geralmente também resolve o tratamento de links).

Se as aberturas estão sendo registradas, verifique se o problema é com o deep link em geral ou com o tratamento de deep linking no clique de push. Para isso, teste se um deep link a partir de um clique em uma mensagem no app funciona.

#### Poucas ou nenhuma Abertura Direta {#few-or-no-direct-opens}

Se pelo menos um usuário abre sua notificação por push no iOS, mas poucas ou nenhuma _Abertura Direta_ é registrada na Braze, pode haver um problema com sua [integração SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview). Lembre-se de que _Aberturas Diretas_ não são registradas para envios de teste ou notificações por push silenciosas.

- Verifique se as mensagens não estão sendo enviadas como [notificações por push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications). A mensagem deve ter texto no título ou no corpo para não ser considerada silenciosa.
- Verifique novamente as seguintes etapas do [guia de integração de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration):
   - [Registrar para push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns): Em cada inicialização do app, preferencialmente dentro de `application:didFinishLaunchingWithOptions:`, o código da etapa 3 precisa ser executado. A propriedade delegate de `UNUserNotificationCenter.current()` precisa ser atribuída a um objeto que implemente `UNUserNotificationCenterDelegate` e contenha o método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`.
   - [Ativar o tratamento de push]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling): Verifique se o método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` foi implementado.