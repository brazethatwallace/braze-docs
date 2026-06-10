## Noções básicas sobre o fluxo de trabalho Braze/APNs {#understanding-the-brazeapns-workflow}

O serviço de Notificações por Push da Apple (APNs) é a infraestrutura para o envio de notificações por push para aplicativos executados nas plataformas da Apple. Esta é a estrutura simplificada de como as notificações por push são ativadas para os dispositivos de seus usuários e como a Braze pode enviar notificações por push para eles:

1. Você configura o certificado de push e o perfil de provisionamento
2. Os dispositivos se registram no APNs e fornecem à Braze os tokens de push
3. Você lança uma Campaign de push da Braze
4. A Braze remove tokens inválidos

### Etapa 1: Configuração do certificado de push e do perfil de provisionamento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Ao desenvolver seu app, você precisará criar um certificado SSL para ativar notificações por push. Esse certificado será incluído no perfil de provisionamento com o qual seu app é construído e também precisará ser enviado para o dashboard da Braze. O certificado permite que a Braze informe ao APNs que estamos autorizados a enviar notificações por push em seu nome.

Há dois tipos de [perfis de provisionamento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) e certificados: desenvolvimento e distribuição. Recomendamos usar apenas perfis e certificados de distribuição para evitar qualquer confusão. Se você optar por usar perfis e certificados diferentes para desenvolvimento e distribuição, certifique-se de que o certificado enviado para o dashboard corresponda ao perfil de provisionamento que você está usando no momento.

{% alert warning %}
Não altere o ambiente do certificado de push (desenvolvimento versus produção). Alterar o certificado de push para o ambiente errado pode levar à remoção acidental do token por push dos seus usuários, tornando-os inalcançáveis por push.
{% endalert %}

### Etapa 2: Os dispositivos se registram no APNs e fornecem à Braze os tokens de push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Quando os usuários abrirem seu app, eles serão solicitados a aceitar notificações por push. Se aceitarem esse prompt, o APNs gerará um token por push para aquele dispositivo específico. O Swift SDK enviará imediatamente e de forma assíncrona o token por push para os apps que usam a [política de descarga automática]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control/#automatic-request-processing) padrão. Depois que tivermos um token por push associado a um usuário, ele aparecerá como "Push Registered" no dashboard em seu perfil de usuário na guia **Engajamento** e será elegível para receber notificações por push de Campaigns da Braze.

{% alert note %}
A partir do macOS 13, em determinados dispositivos, você pode testar as notificações por push em um simulador iOS 16 executado no Xcode 14. Para saber mais, consulte as [Notas de versão do Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considerações para a geração de token por push {#considerations-for-push-token-generation}

- Se os usuários instalarem seu app em outro dispositivo, um novo token será criado e capturado da mesma forma.
- Se os usuários reinstalarem seu app, um novo token será gerado e enviado para a Braze. No entanto, o token original pode ainda ser registrado como válido pelo APNs e pela Braze.
- Se os usuários desinstalarem seu app, a Braze não é notificada imediatamente e o token ainda aparecerá como válido até que seja retirado pelo APNs.
- Em algum momento, o APNs retirará tokens antigos. A Braze não tem controle ou visibilidade sobre isso.

### Etapa 3: Lançamento de uma Campaign de push da Braze {#step-3-launching-a-braze-push-campaign}

Quando uma Campaign de push for lançada, a Braze fará solicitações ao APNs para entregar sua mensagem. Especificamente, as solicitações são enviadas ao APNs para cada token de push válido atual, a menos que **Enviar para o dispositivo mais recente de um usuário** seja selecionado. Depois que a Braze recebe uma resposta bem-sucedida do APNs, registraremos uma entrega bem-sucedida no perfil do usuário, embora o usuário possa não ter recebido a mensagem real por razões que incluem:
- O dispositivo está desligado.
- O dispositivo não está conectado à internet (Wi-Fi ou celular).
- O usuário desinstalou o app recentemente.

A Braze usará o certificado push SSL carregado no dashboard para autenticar e verificar que temos permissão para enviar notificações por push para os tokens de push fornecidos. Se um dispositivo estiver online, a notificação deve ser recebida logo após o envio da Campaign. Note que a Braze define a [data de expiração](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) padrão do APNs para notificações como 30 dias.

### Etapa 4: Remoção de tokens inválidos {#step-4-removing-invalid-tokens}

Se o [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informar que qualquer um dos tokens por push para os quais estávamos tentando enviar uma mensagem é inválido, removeremos esses tokens dos perfis de usuário aos quais eles estavam associados.

{% alert note %}
É normal que o APNs retorne inicialmente um status de sucesso, mesmo que um token se torne não registrado, pois o APNs não relata imediatamente eventos de invalidação de token. O APNs intencionalmente atrasa o retorno de um status `410` para tokens inválidos em uma programação aleatória, projetada para proteger a privacidade do usuário e evitar o rastreamento de desinstalações de apps. Você pode continuar enviando notificações para um token não registrado até que o APNs retorne um status `410`.
{% endalert %}

## Usando os registros de erros do push {#using-the-push-error-logs}

O [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) oferece a oportunidade de ver todas as mensagens (especialmente mensagens de erro) associadas às suas Campaigns e envios, incluindo erros de notificação por push. Esse registro de erros fornece uma variedade de avisos que podem ser muito úteis para identificar por que suas Campaigns não estão funcionando como esperado. Clicar em uma mensagem de erro irá redirecioná-lo para a documentação relevante para ajudá-lo a solucionar um incidente específico.

![Logs de erro de push exibindo a hora em que o erro ocorreu, o nome do app, o canal, o tipo de erro e a mensagem de erro.]({% image_buster /assets/img_archive/message_activity_log.png %})

Os erros comuns que podem ser vistos aqui incluem notificações específicas do usuário, como ["Received Unregistered Sending to Push Token"](#swift_received-unregistered-sending).

Além disso, a Braze também apresenta um changelog de push no perfil do usuário na guia **Engajamento**. Esse changelog contém insights sobre o comportamento de registro de push, como invalidação de token, erros de registro de push, tokens transferidos para novos usuários, etc.

![]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erros no Registro de atividades de envio de mensagem {#message-activity-log-errors}

#### Recebido envio não registrado para token por push {#received-unregistered-sending}

- Certifique-se de que o token por push enviado para a Braze a partir do método `AppDelegate.braze?.notifications.register(deviceToken:)` seja válido. Consulte o **Registro de atividades de envio de mensagem** para ver o token por push. Deve parecer algo como `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, uma longa string contendo uma mistura de letras e números. Se seu token por push parecer diferente, verifique seu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze) para enviar os tokens por push à Braze.
- Verifique se o seu perfil de provisionamento de push corresponde ao ambiente que está testando. Os certificados universais podem ser configurados no dashboard da Braze para enviar para o ambiente APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
 - Verifique se o token por push que você enviou para a Braze corresponde ao perfil de provisionamento que você usou para desenvolver o app de onde você enviou o token por push.

#### Token de dispositivo não para tópico {#device-token-not-for-topic}

O APNs retorna `DeviceTokenNotForTopic` (status HTTP 400) quando o token por push não corresponde ao tópico (bundle ID) configurado para suas credenciais. A Braze pode exibir isso no **Registro de atividades de envio de mensagem** ou nos logs de entrega de push como `DeviceTokenNotForTopic`.

Para resolver a incompatibilidade:

1. Confirme se o **bundle ID** do app corresponde ao **App Bundle ID** na Braze (**Configurações** > **Configurações do app** > **Configurações das notificações por push**).
2. Verifique se o perfil de provisionamento usado para compilar o app inclui a capacidade de push para esse bundle ID.
3. Confirme se a credencial de push enviada para a Braze corresponde ao ambiente do app (desenvolvimento versus produção).
4. Para chaves `.p8`, verifique se o **Team ID** e o **Key ID** na Braze correspondem à sua conta de desenvolvedor Apple.
5. Faça upload novamente de uma chave `.p8` válida ou de um certificado `.p12` se as credenciais foram rotacionadas ou revogadas.

Prefira chaves de autenticação `.p8` quando possível. Para tipos de credenciais e indicadores de status no dashboard, consulte [Migrar para uma chave de autenticação .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting/#migrate-to-a-p8-authentication-key).

#### Envio de BadDeviceToken para token por push {#baddevicetoken-sending-to-push-token}

O `BadDeviceToken` é um código de erro do APNs e não se origina da Braze. Pode haver várias razões para essa resposta ser retornada, incluindo as seguintes:

- O app recebeu um token por push que era inválido para as credenciais enviadas para o dashboard.
- Push foi desativado para este espaço de trabalho.
- O usuário optou por não receber push.
- O app foi desinstalado.
- A Apple atualizou o token por push, o que invalidou o token antigo.
- O app foi criado para um ambiente de produção, mas as credenciais de push enviadas para a Braze estão definidas para um ambiente de desenvolvimento (ou o contrário).

## Problemas de registro de push {#push-registration-issues}

### Nenhum prompt de registro de push {#no-push-registration-prompt}

Se o aplicativo não solicitar que você se registre para notificações por push, provavelmente há um problema com a integração do seu registro de push. Certifique-se de ter seguido nossa [documentação]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) e integrado corretamente nosso registro de push. Você também pode definir pontos de interrupção em seu código para garantir que o código de registro de push esteja em execução.

### Nenhum usuário "push registered" é exibido no dashboard (antes do envio de mensagens) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Certifique-se de que seu app esteja configurado corretamente para permitir notificações por push. Os pontos de falha comuns a serem verificados incluem:

- Verifique se o seu app está solicitando a permissão para notificações por push. Normalmente, esse prompt aparecerá na primeira vez que você abrir o app, mas pode ser programado para aparecer em outro momento. Se não aparecer onde deveria, o problema provavelmente está na configuração básica das capacidades de push do seu app.
  - Verifique se as etapas da [integração de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) foram concluídas com êxito.
  - Verifique se o perfil de provisionamento com o qual seu app foi criado inclui permissões para push. Certifique-se de que está baixando todos os perfis de provisionamento disponíveis da sua conta de desenvolvedor Apple. Para confirmar isso, execute as etapas a seguir:
    1. No Xcode, acesse **Preferences > Accounts** (ou use o atalho de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecione o Apple ID que você usa para sua conta de desenvolvedor e clique em **View Details**.
    3. Na próxima página, clique em **<i class="fas fa-redo-alt"></i> Refresh** e confirme que você está baixando todos os perfis de provisionamento disponíveis.
- Verifique se você [ativou corretamente a capacidade de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-2-enable-push-capabilities) em seu app.
- Verifique se o seu perfil de provisionamento de push corresponde ao ambiente em que você está testando. Os certificados universais podem ser configurados no dashboard da Braze para enviar para o ambiente APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funcionará.
- Verifique se você está chamando nosso método `registerPushToken` definindo um ponto de interrupção no código.
- Certifique-se de que esteja testando usando um dispositivo (o push não funcionará em um simulador) e que tenha boa conectividade de rede.

## Notificações por push enviadas, mas não exibidas nos dispositivos dos usuários {#push-notifications-sent-but-not-displayed-on-users-devices}

### Os usuários "push registered" não são mais ativados após o envio de mensagens {#push-registered-users-no-longer-enabled-after-sending-messages}

Provavelmente isso indica que o usuário tinha um token por push inválido. Isso pode acontecer por várias razões:

#### Incompatibilidade entre o certificado do dashboard e do app {#dashboard-and-app-certificate-mismatch}

Se o certificado de push que você carregou no dashboard não for o mesmo no perfil de provisionamento com o qual seu app foi desenvolvido, o APNs rejeitará o token. Verifique se fez upload do certificado correto e se concluiu outra sessão no app antes de tentar outra notificação de teste.

#### O aplicativo foi desinstalado {#application-was-uninstalled}

Se um usuário tiver desinstalado seu aplicativo, o token por push dele será inválido e removido no próximo envio.

#### Regenerando seu perfil de provisionamento {#regenerating-your-provisioning-profile}

Como último recurso, começar do zero e criar um perfil de provisionamento totalmente novo pode eliminar erros de configuração decorrentes do trabalho com vários ambientes, perfis e apps ao mesmo tempo. Existem muitos fatores na configuração de notificações por push, então, às vezes, é melhor tentar novamente desde o início. Isso também ajudará a isolar o problema se você precisar continuar com a solução de problemas.

### Mensagens não entregues a usuários "push registered" {#messages-not-delivered-to-push-registered-users}

#### O app está em primeiro plano {#app-is-foregrounded}

Nas versões do iOS que não integram push via o framework `UserNotifications`, se o app estiver em primeiro plano quando a mensagem push for recebida, ela não será exibida. Você deve colocar o app em segundo plano nos seus dispositivos de teste antes de enviar mensagens de teste.

#### Notificação de teste agendada incorretamente {#test-notification-scheduled-incorrectly}

Verifique a programação que você definiu para sua mensagem de teste. Se estiver definida para entrega no fuso horário local ou [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), você pode simplesmente não ter recebido a mensagem ainda (ou ter o app em primeiro plano quando foi recebida).

### Usuário não "push registered" para o app que está sendo testado {#user-not-push-registered-for-the-app-being-tested}

Verifique o perfil do usuário para o qual você está tentando enviar uma mensagem de teste. Na guia **Engajamento**, deve haver uma lista de "apps que podem receber push". Verifique se o app para o qual você está tentando enviar mensagens de teste está nessa lista. Os usuários aparecerão como "Push Registered" se tiverem um token por push para qualquer app no seu espaço de trabalho, então isso pode ser algo como um falso positivo.

O seguinte indicaria um problema com o registro de push ou que o token do usuário foi retornado à Braze como inválido pelo APNs após o envio:

![Um perfil de usuário exibindo as configurações de contato de um usuário. Em Push, é exibido "No Apps".]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Cliques de push não registrados {#push-clicks-not-logged}

- Certifique-se de ter seguido as [etapas de integração de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling).
- A Braze não gerencia notificações por push recebidas silenciosamente em primeiro plano (comportamento padrão de push em primeiro plano antes do framework `UserNotifications`). Isso significa que os links não serão abertos e os cliques no push não serão registrados. Se seu app ainda não estiver integrado com o framework `UserNotifications`, a Braze não gerenciará as notificações por push quando o estado do app for `UIApplicationStateActive`. Certifique-se de que seu app não atrase as chamadas para os [métodos de tratamento de push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling); caso contrário, o Swift SDK poderá tratar as notificações por push como eventos push silenciosos em primeiro plano e não processá-las.

## Deep links não estão funcionando {#deep-links-not-working}

Para solução de problemas abrangente em todos os canais — incluindo links universais, esquemas personalizados, e-mail e provedores de terceiros como Branch — veja [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/).

### Links da web não abrem com cliques em push {#web-links-from-push-clicks-not-opening}

Os links nas notificações por push precisam ser compatíveis com ATS para serem abertos em visualizações na web. Certifique-se de que seus links da web usem HTTPS. Para saber mais, consulte [conformidade com ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#app-transport-security-ats).

### Deep links de cliques em push não abrem {#deep-links-from-push-clicks-not-opening}

A maior parte do código que lida com deep links também lida com aberturas de push. Primeiro, confira se as aberturas do push estão sendo registradas. Se não, resolva esse problema (pois a correção geralmente corrige o manuseio de links).

Se as aberturas estiverem sendo registradas, verifique se é um problema com o deep link em geral ou com o manuseio do clique de push com deep linking. Para fazer isso, teste para ver se um deep link de um clique de mensagem no app funciona.