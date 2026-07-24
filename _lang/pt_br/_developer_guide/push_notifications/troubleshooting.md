---
page_order: 10.9
nav_title: Solução de problemas
article_title: Solução de problemas de notificações por push para o SDK da Braze
channel:
  - push notifications
---

# Solução de problemas de notificações por push {#troubleshoot-push-notifications}

> Aprenda como solucionar problemas de notificações por push para o SDK da Braze.

{% sdktabs %}
{% sdktab web %}

## Solução de problemas {#troubleshooting}

Se você estiver enfrentando problemas após configurar as notificações por push, considere o seguinte:

- As notificações web push exigem que seu site use HTTPS.
- Nem todos os navegadores podem receber mensagens push. Verifique se `braze.isPushSupported()` retorna `true` no navegador.
- Alguns navegadores, como o Firefox, não exibem imagens nas notificações por push. Para detalhes sobre o suporte dos navegadores, consulte a [documentação do MDN sobre imagens de Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- Se um usuário negou o acesso push de um site, ele não será solicitado a conceder permissão novamente, a menos que remova o status de negação nas preferências do navegador.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}

## Entendendo o fluxo de trabalho Braze/APNs {#understanding-the-brazeapns-workflow}

O serviço de Notificações por Push da Apple (APN) é a infraestrutura para enviar notificações por push a aplicativos executados nas plataformas da Apple. Aqui está a estrutura simplificada de como as notificações por push são ativadas para os dispositivos dos seus usuários e como a Braze pode enviar notificações por push para eles:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Etapa 1: Configurando o certificado de push e o perfil de provisionamento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Para desenvolver seu app, crie um certificado SSL para ativar as notificações por push. Esse certificado é incluído no perfil de provisionamento com o qual seu app é compilado e também deve ser enviado ao dashboard da Braze. O certificado permite que a Braze informe ao APN que está autorizada a enviar notificações por push em seu nome.

Existem dois tipos de [perfis de provisionamento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) e certificados: desenvolvimento e distribuição. Recomendamos usar apenas perfis e certificados de distribuição para evitar qualquer confusão. Se você optar por usar perfis e certificados diferentes para desenvolvimento e distribuição, certifique-se de que o certificado enviado ao dashboard corresponda ao perfil de provisionamento que você está usando no momento.

{% alert warning %}
Não altere o ambiente do certificado de push (desenvolvimento versus produção). Alterar o certificado de push para o ambiente errado pode fazer com que os tokens por push dos seus usuários sejam removidos acidentalmente, tornando-os inacessíveis por push.
{% endalert %}

### Etapa 2: Os dispositivos se registram no APN e fornecem tokens por push à Braze {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Quando os usuários abrem seu app, eles são solicitados a aceitar notificações por push. Se aceitarem essa solicitação, o APN gera um token por push para aquele dispositivo específico. O SDK Swift envia imediata e assincronamente o token por push para apps que usam a [política de envio automático]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) padrão. Depois que temos um token por push associado a um usuário, ele aparece como "Push Registered" no dashboard, no perfil de usuário, na guia **Engajamento**, e se torna elegível para receber notificações por push de Campaigns da Braze.

{% alert note %}
A partir do macOS 13, em determinados dispositivos, você pode testar notificações por push em um simulador iOS 16 executado no Xcode 14. Para saber mais, consulte as [Notas de versão do Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considerações sobre a geração de tokens por push {#considerations-for-push-token-generation}

- Se os usuários instalarem seu app em outro dispositivo, a Braze cria e captura outro token da mesma forma.
- Se os usuários reinstalarem seu app, o SDK gera um novo token e o envia à Braze. No entanto, o APN e a Braze ainda podem registrar o token original como válido.
- Se os usuários desinstalarem seu app, a Braze não recebe uma notificação imediatamente, e o token ainda aparece como válido até que o APN o retire.
- Em algum momento, o APN retira tokens antigos. A Braze não controla nem tem visibilidade sobre esse processo.

### Etapa 3: Lançando uma Campaign de push da Braze {#step-3-launching-a-braze-push-campaign}

Quando uma Campaign de push é lançada, a Braze faz solicitações ao APN para entregar sua mensagem. Especificamente, as solicitações são enviadas ao APN para cada token por push válido atual, a menos que **Enviar para o dispositivo mais recente do usuário** esteja selecionado. Depois que a Braze recebe uma resposta de sucesso do APN, ela registra uma entrega bem-sucedida no perfil de usuário, embora o usuário possa não ter recebido a mensagem real por motivos como:
- O dispositivo está desligado.
- O dispositivo não está conectado à internet (Wi-Fi ou celular).
- O usuário desinstalou o app recentemente.

A Braze usa o certificado SSL de push enviado no dashboard para autenticar e verificar que está autorizada a enviar notificações por push para os tokens por push fornecidos. Se um dispositivo estiver online, a notificação deve ser recebida logo após o envio da Campaign. A Braze define a [data de expiração](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) padrão do APN para notificações como 30 dias.

### Etapa 4: Removendo tokens inválidos {#step-4-removing-invalid-tokens}

Se o [APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informar que algum dos tokens por push para os quais estávamos tentando enviar uma mensagem é inválido, removemos esses tokens dos perfis de usuário aos quais estavam associados.

{% alert note %}
É normal que o APN inicialmente retorne um status de sucesso mesmo que um token se torne não registrado, pois o APN não reporta imediatamente eventos de invalidação de token. O APN atrasa intencionalmente o retorno de um status `410` para tokens inválidos em um cronograma aleatório, projetado para proteger a privacidade do usuário e evitar o rastreamento de desinstalações de apps. Você pode continuar enviando notificações com segurança para um token não registrado até que o APN retorne um status `410`.
{% endalert %}

## Usando os logs de erros de push {#using-the-push-error-logs}

O [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) permite que você veja todas as mensagens (especialmente mensagens de erro) associadas às suas Campaigns e envios, incluindo erros de notificações por push. Esse log de erros fornece diversos alertas que podem ser muito úteis para identificar por que suas Campaigns não estão funcionando como esperado. Selecionar uma mensagem de erro redireciona você para a documentação relevante para ajudar a solucionar um incidente específico.

![Logs de erros de push exibindo o horário em que o erro ocorreu, o nome do app, o canal, o tipo de erro e a mensagem de erro.]({% image_buster /assets/img_archive/message_activity_log.png %})

Erros comuns que você pode ver aqui incluem notificações específicas do usuário, como ["Received Unregistered Sending to Push Token"](#swift_received-unregistered-sending).

Além disso, a Braze também fornece um changelog de push no perfil de usuário, na guia **Engajamento**. Esse changelog oferece insights sobre o comportamento de registro de push, como invalidação de token, erros de registro de push, tokens sendo movidos para novos usuários, etc.

![Guia Engajamento do perfil de usuário da Braze mostrando o changelog de registro de push.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erros do Registro de atividade de mensagens {#message-activity-log-errors}

#### Received unregistered sending to push token {#received-unregistered-sending}

- Certifique-se de que o token por push enviado para a Braze pelo método `AppDelegate.braze?.notifications.register(deviceToken:)` é válido. Você pode verificar no **Registro de atividade de mensagens** para ver o token por push. Ele deve se parecer com algo como `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, uma string longa contendo uma combinação de letras e números. Se o seu token por push parecer diferente, verifique o seu [código]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze) para enviar os tokens por push para a Braze.
- Certifique-se de que o perfil de provisionamento de push corresponde ao ambiente que você está testando. Certificados universais podem ser configurados no dashboard da Braze para enviar para o ambiente de APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funciona.
 - Verifique se o token por push que você enviou para a Braze corresponde ao perfil de provisionamento usado para compilar o app de onde o token por push foi enviado.

#### Device token not for topic {#device-token-not-for-topic}

O APNs retorna `DeviceTokenNotForTopic` (status HTTP 400) quando o token por push não corresponde ao tópico (bundle ID) configurado para suas credenciais. A Braze pode exibir isso no **Registro de atividade de mensagens** ou nos logs de entrega de push como `DeviceTokenNotForTopic`.

Para resolver a incompatibilidade:

1. Confirme se o **bundle ID** do app corresponde ao **App Bundle ID** na Braze (**Configurações** > **Configurações do app** > **Configurações de notificações por push**).
2. Verifique se o perfil de provisionamento usado para compilar o app inclui a capacidade de push para esse bundle ID.
3. Confirme se a credencial de push enviada para a Braze corresponde ao ambiente do app (desenvolvimento versus produção).
4. Para chaves `.p8`, verifique se o **Team ID** e o **Key ID** na Braze correspondem à sua conta do Apple Developer.
5. Reenvie uma chave `.p8` válida ou um certificado `.p12` se as credenciais foram rotacionadas ou revogadas.

Prefira chaves de autenticação `.p8` quando possível. Para tipos de credenciais e indicadores de status no dashboard, consulte [Migrar para uma chave de autenticação .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken sending to push token {#baddevicetoken-sending-to-push-token}

O `BadDeviceToken` é um código de erro do APNs e não é originado pela Braze. Pode haver diversas razões para essa resposta ser retornada, incluindo as seguintes:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Problemas de registro de push {#push-registration-issues}

### Nenhum prompt de registro de push {#no-push-registration-prompt}

Se o aplicativo não solicitar que você se registre para notificações por push, provavelmente há um problema com a integração do registro de push. Certifique-se de ter seguido nossa [documentação]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) e integrado corretamente nosso registro de push. Você também pode definir breakpoints no seu código para garantir que o código de registro de push esteja sendo executado.

### Nenhum usuário "registrado para push" aparecendo no dashboard (antes do envio de mensagens) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Certifique-se de que seu app está configurado corretamente para permitir notificações por push. Pontos comuns de falha a verificar incluem:

- Verifique se o app está solicitando que você permita notificações por push. Normalmente, esse prompt aparece na primeira abertura do app, mas pode ser programado para aparecer em outro lugar. Se ele não aparecer onde deveria, o problema provavelmente está na configuração básica dos recursos de push do seu app.
  - Verifique se as etapas da [integração de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) foram concluídas com sucesso.
  - Verifique se o perfil de provisionamento com o qual seu app foi compilado inclui permissões para push. Certifique-se de que está baixando todos os perfis de provisionamento disponíveis da sua conta de desenvolvedor Apple. Para confirmar, siga estas etapas:
    1. No Xcode, navegue até **Preferences > Accounts** (ou use o atalho de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecione o Apple ID que você usa para sua conta de desenvolvedor e clique em **View Details**.
    3. Na próxima página, clique em **<i class="fas fa-redo-alt"></i> Refresh** e confirme que está baixando todos os perfis de provisionamento disponíveis.
- Verifique se você [ativou corretamente o recurso de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities) no seu app.
- Verifique se o perfil de provisionamento de push corresponde ao ambiente em que você está testando. Certificados universais podem ser configurados no dashboard da Braze para enviar para o ambiente de APNs de desenvolvimento ou produção. Usar um certificado de desenvolvimento para um app de produção ou um certificado de produção para um app de desenvolvimento não funciona.
- Verifique se você está chamando nosso método `registerPushToken` definindo um breakpoint no seu código.
- Certifique-se de que está testando usando um dispositivo (push não funciona em um simulador) e que tem boa conectividade de rede.

## Notificações por push enviadas, mas não exibidas nos dispositivos dos usuários {#push-notifications-sent-but-not-displayed-on-users-devices}

### Usuários "registrados para push" deixam de estar ativados após o envio de mensagens {#push-registered-users-no-longer-enabled-after-sending-messages}

Isso provavelmente indica que o usuário tinha um token por push inválido. Isso pode acontecer por vários motivos:

#### Incompatibilidade entre o certificado do dashboard e o do app {#dashboard-and-app-certificate-mismatch}

Se o certificado de push que você enviou no dashboard não for o mesmo do perfil de provisionamento com o qual seu app foi compilado, o APN rejeitará o token. Verifique se você enviou o certificado correto e concluiu outra sessão no app antes de tentar outra notificação de teste.

#### O app foi desinstalado {#application-was-uninstalled}

Se um usuário desinstalou seu app, o token por push dele será inválido e removido no próximo envio.

#### Regenerando seu perfil de provisionamento {#regenerating-your-provisioning-profile}

Como último recurso, começar do zero e criar um perfil de provisionamento totalmente novo pode resolver erros de configuração que surgem ao trabalhar com vários ambientes, perfis e apps ao mesmo tempo. Existem muitas "partes móveis" na configuração de notificações por push, então, às vezes, é melhor tentar novamente desde o início. Isso também ajudará a isolar o problema caso você precise continuar a solução de problemas.

### Mensagens não entregues a usuários "registrados para push" {#messages-not-delivered-to-push-registered-users}

#### O app está em primeiro plano {#app-is-foregrounded}

Em versões do iOS que não integram push por meio do framework `UserNotifications`, se o app estiver em primeiro plano quando a mensagem push for recebida, ela não será exibida. Você deve colocar o app em segundo plano nos seus dispositivos de teste antes de enviar mensagens de teste.

#### Notificação de teste agendada incorretamente {#test-notification-scheduled-incorrectly}

Verifique o cronograma que você definiu para sua mensagem de teste. Se estiver configurado para entrega no fuso local ou com [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing), é possível que você simplesmente ainda não tenha recebido a mensagem (ou que o app estivesse em primeiro plano quando ela foi recebida).

### Usuário não "registrado para push" no app sendo testado {#user-not-push-registered-for-the-app-being-tested}

Verifique o perfil do usuário para quem você está tentando enviar uma mensagem de teste. Na guia **Engajamento**, deve haver uma lista de "apps com push habilitado". Verifique se o app para o qual você está tentando enviar mensagens de teste está nessa lista. Os usuários aparecerão como "Push Registered" se tiverem um token por push para qualquer app no seu espaço de trabalho, então isso pode ser um falso positivo.

O seguinte indicaria um problema com o registro de push ou que o token do usuário foi retornado à Braze como inválido pelo APN após o envio:

![Um perfil de usuário exibindo as configurações de contato de um usuário. Em Push, "No Apps" é exibido.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Cliques em push não registrados {#push-clicks-not-logged}

- Certifique-se de ter seguido as [etapas de integração de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling).
- A Braze não processa notificações por push recebidas silenciosamente em primeiro plano (comportamento padrão de push em primeiro plano antes do framework `UserNotifications`). Isso significa que os links não serão abertos e os cliques em push não serão registrados. Se seu aplicativo ainda não integrou o framework `UserNotifications`, a Braze não processará notificações por push quando o estado do aplicativo for `UIApplicationStateActive`. Certifique-se de que seu app não atrasa chamadas aos [métodos de processamento de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling); caso contrário, o SDK Swift pode tratar as notificações por push como eventos silenciosos de push em primeiro plano e não processá-las.

## Deep links não funcionam {#deep-links-not-working}

Para uma solução de problemas abrangente em todos os canais — incluindo links universais, esquemas personalizados, e-mail e provedores terceiros como Branch — consulte [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Links da web a partir de cliques em push não abrem {#web-links-from-push-clicks-not-opening}

Os links em notificações por push precisam estar em conformidade com o ATS para serem abertos em visualizações web. Certifique-se de que seus links da web usem HTTPS. Para saber mais, consulte [Conformidade com ATS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats).

### Deep links a partir de cliques em push não abrem {#deep-links-from-push-clicks-not-opening}

A maior parte do código que lida com deep links também lida com aberturas de push. Primeiro, verifique se as aberturas de push estão sendo registradas. Caso contrário, corrija esse problema (pois a correção geralmente também resolve o tratamento de links).

Se as aberturas estão sendo registradas, verifique se o problema é com o deep link em geral ou com o tratamento de deep linking no clique do push. Para isso, teste se um deep link a partir de um clique em uma mensagem no app funciona.

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}

## Solução de problemas

### Push não aparece após o app ser fechado pelo alternador de tarefas {#push-doesnt-appear-after-app-is-closed-from-task-switcher}

Se você perceber que as notificações por push não aparecem mais após o app ser fechado pelo alternador de tarefas, seu app provavelmente está no modo Debug. O .NET MAUI adiciona scaffolding no modo Debug que impede os apps de receberem push após o processo ser encerrado. Se você executar seu app no modo Release, deverá ver as notificações por push mesmo após o app ser fechado pelo alternador de tarefas.

### Fábrica de notificações personalizada não configurada corretamente {#custom-notification-factory-not-being-set-correctly}

As fábricas de notificações personalizadas (e todos os delegates) devem estender [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) para funcionar corretamente na comunicação entre C# e Java. Consulte [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) sobre a implementação de interfaces Java para saber mais.

{% endsdktab %}
{% endsdktabs %}

## Quebras de linha em notificações por push {#push-linebreaks}

Ao redigir notificações por push com Liquid tags, as quebras de linha adjacentes às Liquid tags são automaticamente removidas antes do envio da mensagem. No [criador de notificações por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message), essas quebras de linha são adicionadas novamente para que sua mensagem permaneça legível durante a edição. Se você notar quebras de linha ao redor das Liquid tags ao salvar sua mensagem, esse é o comportamento esperado.