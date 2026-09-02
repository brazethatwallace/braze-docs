## Entendendo o fluxo de trabalho Braze/APNs {#understanding-the-brazeapns-workflow}

O serviço de Notificações por Push da Apple (APN) é a infraestrutura para enviar notificações por push a aplicativos executados nas plataformas da Apple. Aqui está a estrutura simplificada de como as notificações por push são ativadas para os dispositivos dos seus usuários e como a Braze pode enviar notificações por push para eles:

1. Você configura o certificado de push e o perfil de provisionamento
2. Os dispositivos se registram no APN e fornecem à Braze os tokens por push
3. Você lança uma Campaign de push na Braze
4. A Braze remove tokens inválidos

### Etapa 1: Configurando o certificado de push e o perfil de provisionamento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Ao desenvolver seu app, você precisará criar um certificado SSL para ativar as notificações por push. Esse certificado será incluído no perfil de provisionamento com o qual seu app é compilado e também precisará ser enviado ao dashboard da Braze. O certificado permite que a Braze informe ao APN que estamos autorizados a enviar notificações por push em seu nome.

Existem dois tipos de [perfis de provisionamento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) e certificados: desenvolvimento e distribuição. Recomendamos usar apenas perfis e certificados de distribuição para evitar qualquer confusão. Se você optar por usar perfis e certificados diferentes para desenvolvimento e distribuição, verifique se o certificado enviado ao dashboard corresponde ao perfil de provisionamento que você está usando no momento.

{% alert warning %}
Não altere o ambiente do certificado de push (desenvolvimento versus produção). Alterar o certificado de push para o ambiente errado pode fazer com que os tokens por push dos seus usuários sejam removidos acidentalmente, tornando-os inalcançáveis por push.
{% endalert %}

### Etapa 2: Os dispositivos se registram no APN e fornecem à Braze os tokens por push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Quando os usuários abrem seu app, eles recebem uma solicitação para aceitar notificações por push. Se aceitarem, o APN gerará um token por push para aquele dispositivo específico. O SDK or kit de desenvolvimento de software Swift enviará imediata e assincronamente o token por push para apps que usam a [política de envio automático]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) padrão. Depois que tivermos um token por push associado a um usuário, ele aparecerá como "Push Registered" no dashboard, no perfil do usuário, na guia **Engagement**, e será elegível para receber notificações por push de Campaigns da Braze.

{% alert note %}
A partir do macOS 13, em determinados dispositivos, você pode testar notificações por push em um simulador iOS 16 executado no Xcode 14. Para saber mais, consulte as [Notas de versão do Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considerações sobre a geração de tokens por push {#considerations-for-push-token-generation}

- Se os usuários instalarem seu app em outro dispositivo, outro token será criado e capturado da mesma forma.
- Se os usuários reinstalarem seu app, um novo token será gerado e transmitido à Braze. No entanto, o token original ainda pode ser registrado como válido pelo APN e pela Braze.
- Se os usuários desinstalarem seu app, a Braze não é notificada imediatamente e o token ainda aparecerá como válido até ser descontinuado pelo APN.
- Em algum momento, o APN descontinuará tokens antigos. A Braze não tem controle nem visibilidade sobre isso.

### Etapa 3: Lançando uma Campaign de push na Braze {#step-3-launching-a-braze-push-campaign}

Quando uma Campaign de push é lançada, a Braze faz solicitações ao APN para entregar sua mensagem. Especificamente, as solicitações são enviadas ao APN para cada token por push válido atual, a menos que **Send to a user's most recent device** esteja selecionado. Depois que a Braze recebe uma resposta bem-sucedida do APN, registramos uma entrega bem-sucedida no perfil do usuário, embora o usuário possa não ter recebido a mensagem real por motivos que incluem:
- O dispositivo está desligado.
- O dispositivo não está conectado à internet (Wi-Fi ou celular).
- O app foi desinstalado recentemente.

A Braze usará o certificado SSL de push enviado ao dashboard para autenticar e verificar que estamos autorizados a enviar notificações por push aos tokens por push fornecidos. Se o dispositivo estiver online, a notificação deverá ser recebida pouco depois do envio da Campaign. A Braze define a [data de expiração](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) padrão do APN para notificações como 30 dias.

### Etapa 4: Removendo tokens inválidos {#step-4-removing-invalid-tokens}

Se o [APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informar que algum dos tokens por push para os quais estávamos tentando enviar uma mensagem é inválido, removemos esses tokens dos perfis de usuário aos quais estavam associados.

{% alert note %}
É normal que o APN inicialmente retorne um status de sucesso mesmo quando um token se torna não registrado, pois o APN não reporta imediatamente eventos de invalidação de tokens. O APN atrasa intencionalmente o retorno de um status `410` para tokens inválidos em um cronograma aleatório, projetado para proteger a privacidade do usuário e impedir o rastreamento de desinstalações de apps. Você pode continuar enviando notificações para um token não registrado com segurança até que o APN retorne um status `410`.
{% endalert %}

## Usando os logs de erro de push {#using-the-push-error-logs}

O [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) oferece a oportunidade de ver todas as mensagens (especialmente mensagens de erro) associadas às suas campanhas e envios, incluindo erros de notificações por push. Esse log de erros fornece diversos alertas que podem ser muito úteis para identificar por que suas campanhas não estão funcionando como esperado. Clicar em uma mensagem de erro redirecionará você para a documentação relevante para ajudar na solução de problemas de um incidente específico.

![Logs de erro de push exibindo o horário em que o erro ocorreu, o nome do app, o canal, o tipo de erro e a mensagem de erro.]({% image_buster /assets/img_archive/message_activity_log.png %})

Erros comuns que você pode ver aqui incluem notificações específicas do usuário, como ["Received Unregistered Sending to token por push"](#swift_received-unregistered-sending).

Além disso, a Braze também fornece um changelog de push no perfil de usuário na guia **Engajamento**. Esse changelog oferece insights sobre o comportamento de registro de push, como invalidação de token, erros de registro de push, tokens sendo transferidos para novos usuários, etc.

![Guia Engajamento do perfil de usuário da Braze mostrando o changelog de registro de push.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erros do registro de atividade de mensagens {#message-activity-log-errors}

#### Received unregistered sending to token por push {#received-unregistered-sending}

- Certifique-se de que o token por push enviado para a Braze pelo método `AppDelegate.braze?.notifications.register(deviceToken:)` seja válido. Você pode consultar o **Registro de atividade de mensagens** para ver o token por push. Ele deve se parecer com algo como `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, uma string longa contendo uma combinação de letras e números. Se o seu token por push parecer diferente, verifique seu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze) para o envio dos tokens por push para a Braze.
- Verifique se o perfil de provisionamento de push corresponde ao ambiente em que você está testando. Certificados universais podem ser configurados no dashboard da Braze para enviar ao ambiente de APNs de desenvolvimento ou de produção. Usar um certificado de desenvolvimento para um app de produção, ou um certificado de produção para um app de desenvolvimento, não funcionará.
 - Verifique se o token por push que você enviou para a Braze corresponde ao perfil de provisionamento usado para compilar o app de onde o token por push foi enviado.

#### Device token not for topic

O APNs retorna `DeviceTokenNotForTopic` (status HTTP 400) quando o token por push não corresponde ao tópico (bundle ID) configurado para suas credenciais. A Braze pode exibir isso no **Registro de atividade de mensagens** ou nos logs de entrega de push como `DeviceTokenNotForTopic`.

Para resolver a divergência:

1. Confirme se o **bundle ID** do app corresponde ao **App Bundle ID** na Braze (**Configurações** > **Configurações do app** > **Configurações de notificação por push**).
2. Verifique se o perfil de provisionamento usado para compilar o app inclui a capacidade de push para esse bundle ID.
3. Confirme se a credencial de push enviada para a Braze corresponde ao ambiente do app (desenvolvimento versus produção).
4. Para chaves `.p8`, verifique se o **Team ID** e o **Key ID** na Braze correspondem à sua conta do Apple Developer.
5. Reenvie uma chave `.p8` válida ou um certificado `.p12` se as credenciais foram rotacionadas ou revogadas.

Prefira chaves de autenticação `.p8` quando possível. Para tipos de credenciais e indicadores de status do dashboard, consulte [Migrar para uma chave de autenticação .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken sending to token por push

O `BadDeviceToken` é um código de erro do APNs e não tem origem na Braze. Pode haver vários motivos para essa resposta ser retornada, incluindo os seguintes:

- O app recebeu um token por push que era inválido para as credenciais enviadas ao dashboard.
- O push foi desativado para este espaço de trabalho.
- O usuário optou por não receber push.
- O app foi desinstalado.
- A Apple atualizou o token por push, invalidando o token antigo.
- O app foi compilado para um ambiente de produção, mas as credenciais de push enviadas para a Braze estão configuradas para um ambiente de desenvolvimento (ou vice-versa).

## Problemas no registro de push {#push-registration-issues}

### Nenhum prompt de registro de push {#no-push-registration-prompt}

Se o aplicativo não solicitar o registro para notificações por push, provavelmente há um problema com a integração do registro de push. Certifique-se de que você seguiu nossa [documentação]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) e integrou corretamente nosso registro de push. Você também pode definir breakpoints no seu código para garantir que o código de registro de push esteja sendo executado.

### Nenhum usuário com "push registrado" aparecendo no dashboard (antes do envio de mensagens) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Certifique-se de que o app está configurado corretamente para permitir notificações por push. Pontos de falha comuns a serem verificados incluem:

- Verifique se o app está solicitando que você permita notificações por push. Normalmente, esse prompt aparece na primeira abertura do app, mas pode ser programado para aparecer em outro lugar. Se ele não aparecer onde deveria, o problema provavelmente está na configuração básica dos recursos de push do app.
  - Verifique se as etapas da [integração de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) foram concluídas com sucesso.
  - Verifique se o perfil de provisionamento com o qual o app foi compilado inclui permissões para push. Certifique-se de que você está baixando todos os perfis de provisionamento disponíveis da sua conta de desenvolvedor Apple. Para confirmar isso, siga as etapas a seguir:
    1. No Xcode, navegue até **Preferences > Accounts** (ou use o atalho de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecione o Apple ID que você usa para sua conta de desenvolvedor e clique em **View Details**.
    3. Na próxima página, clique em **<i class="fas fa-redo-alt"></i> Refresh** e confirme que está baixando todos os perfis de provisionamento disponíveis.
- Verifique se você [ativou corretamente o recurso de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-2-enable-push-capabilities) no app.
- Verifique se o perfil de provisionamento de push corresponde ao ambiente em que você está testando. Certificados universais podem ser configurados no dashboard da Braze para enviar ao ambiente de APN de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
- Verifique se você está chamando nosso método `registerPushToken` definindo um breakpoint no seu código.
- Certifique-se de que está testando em um dispositivo (push não funciona em um simulador) e que tem boa conectividade de rede.

## Notificações por push enviadas, mas não exibidas nos dispositivos dos usuários {#push-notifications-sent-but-not-displayed-on-users-devices}

### Usuários "registrados para push" deixam de estar ativados após o envio de mensagens {#push-registered-users-no-longer-enabled-after-sending-messages}

Isso provavelmente indica que o usuário tinha um token de push inválido. Isso pode acontecer por vários motivos:

#### Incompatibilidade entre o certificado do dashboard e o do app {#dashboard-and-app-certificate-mismatch}

Se o certificado de push que você enviou no dashboard não for o mesmo que está no perfil de provisionamento com o qual seu app foi compilado, o APN rejeitará o token. Verifique se você enviou o certificado correto e concluiu outra sessão no app antes de tentar outra notificação de teste.

#### O app foi desinstalado {#application-was-uninstalled}

Se um usuário desinstalou seu app, o token de push dele será inválido e removido no próximo envio.

#### Regenerando seu perfil de provisionamento {#regenerating-your-provisioning-profile}

Como último recurso, começar do zero e criar um perfil de provisionamento totalmente novo pode resolver erros de configuração que surgem ao trabalhar com vários ambientes, perfis e apps ao mesmo tempo. Existem muitas "partes móveis" na configuração de notificações por push, então, às vezes, é melhor recomeçar do início. Isso também ajudará a isolar o problema caso você precise continuar a solução de problemas.

### Mensagens não entregues a usuários "registrados para push" {#messages-not-delivered-to-push-registered-users}

#### O app está em primeiro plano {#app-is-foregrounded}

Nas versões do iOS que não integram push por meio do framework `UserNotifications`, se o app estiver em primeiro plano quando a mensagem de push for recebida, ela não será exibida. Você deve colocar o app em segundo plano nos seus dispositivos de teste antes de enviar mensagens de teste.

#### Notificação de teste agendada incorretamente {#test-notification-scheduled-incorrectly}

Verifique o cronograma que você definiu para sua mensagem de teste. Se estiver configurado para entrega no fuso local ou com [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), pode ser que você ainda não tenha recebido a mensagem (ou o app estava em primeiro plano quando ela foi recebida).

### O usuário não está "registrado para push" no app que está sendo testado {#user-not-push-registered-for-the-app-being-tested}

Verifique o perfil do usuário para quem você está tentando enviar uma mensagem de teste. Na guia **Engajamento**, deve haver uma lista de "apps com push habilitado". Verifique se o app para o qual você está tentando enviar mensagens de teste está nessa lista. Os usuários aparecerão como "Push Registered" se tiverem um token de push para qualquer app no seu espaço de trabalho, então isso pode ser um falso positivo.

O seguinte indicaria um problema com o registro de push ou que o token do usuário foi retornado à Braze como inválido pelo APN após o envio:

![Um perfil de usuário exibindo as configurações de contato de um usuário. Em Push, "No Apps" é exibido.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Cliques de push não registrados {#push-clicks-not-logged}

- Certifique-se de ter seguido as [etapas de integração de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling).
- A Braze não gerencia notificações por push recebidas silenciosamente em primeiro plano (comportamento padrão de push em primeiro plano antes do framework `UserNotifications`). Isso significa que os links não serão abertos e os cliques no push não serão registrados. Se seu app ainda não estiver integrado com o framework `UserNotifications`, a Braze não gerenciará as notificações por push quando o estado do app for `UIApplicationStateActive`. Certifique-se de que seu app não atrase as chamadas para os [métodos de tratamento de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling); caso contrário, o Swift SDK or kit de desenvolvimento de software poderá tratar as notificações por push como eventos push silenciosos em primeiro plano e não processá-las.

## Deep links não funcionam {#deep-links-not-working}

Para uma solução de problemas abrangente em todos os canais — incluindo links universais, esquemas personalizados, e-mail e provedores terceirizados como Branch or ramificação — consulte [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Links da web a partir de cliques em push não abrem {#web-links-from-push-clicks-not-opening}

Os links em notificações por push precisam estar em conformidade com o ATS para serem abertos em visualizações web. Certifique-se de que seus links da web usem HTTPS. Para saber mais, consulte [Conformidade com ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking#app-transport-security-ats).

### Deep links a partir de cliques em push não abrem {#deep-links-from-push-clicks-not-opening}

A maior parte do código que lida com deep links também gerencia aberturas de push. Primeiro, verifique se as aberturas de push estão sendo registradas. Caso não estejam, corrija esse problema (pois a correção geralmente também resolve o tratamento de links).

Se as aberturas estiverem sendo registradas, verifique se o problema é com o deep link em geral ou com o tratamento do clique em push via deep linking. Para isso, teste se um deep link a partir de um clique em uma mensagem no app funciona.