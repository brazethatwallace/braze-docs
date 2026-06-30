---
nav_title: Notificações por push silenciosas
article_title: Notificações por push silenciosas para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência aborda a implementação de notificações por push silenciosas em seu aplicativo iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Notificações por push silenciosas {#silent-push-notifications}

As notificações por push permitem que você notifique seu app quando ocorrerem eventos importantes. Você pode enviar uma notificação por push quando tiver novas mensagens instantâneas para entregar, alertas de notícias de última hora para enviar ou o último episódio do programa de TV favorito do usuário pronto para ser baixado para visualização off-line. As notificações por push também podem ser silenciosas, não contendo nenhuma mensagem de alerta ou som, sendo usadas apenas para atualizar a interface do app ou disparar o trabalho em segundo plano.

As notificações por push são ótimas para conteúdo esporádico mas imediatamente importante, em que a postergação entre as buscas em segundo plano pode não ser aceitável. As notificações por push também podem ser muito mais eficientes do que a busca em segundo plano, pois seu aplicativo só é iniciado quando necessário.

As notificações por push têm limite de frequência, portanto, não tenha medo de enviar quantas forem necessárias para o seu aplicativo. O iOS e os servidores APNs controlarão a frequência com que elas são entregues, e você não terá problemas por enviar muitas. Se suas notificações por push forem limitadas, elas poderão sofrer postergação até a próxima vez que o dispositivo enviar um pacote keep-alive ou receber outra notificação.

## Envio de notificações por push silenciosas {#sending-silent-push-notifications}

Para enviar uma notificação por push silenciosa, defina o sinalizador `content-available` como `1` em uma carga útil de notificação por push. Ao enviar uma notificação por push silenciosa, talvez você também queira incluir alguns dados na carga útil da notificação, para que seu aplicativo possa fazer referência ao evento. Isso pode economizar algumas solicitações de rede e aumentar a capacidade de resposta do seu app.

{% alert warning %}
Anexar tanto um título quanto um corpo de texto com `content-available=1` não é recomendado porque pode levar a um comportamento indefinido. Para garantir que uma notificação seja realmente silenciosa, exclua tanto o título quanto o corpo de texto ao definir o sinalizador `content-available` para `1.` Para mais detalhes, consulte a [documentação oficial da Apple sobre atualizações em segundo plano](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

O sinalizador `content-available` pode ser definido no dashboard da Braze, bem como em nosso [objeto Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object) na [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).

![O dashboard da Braze mostrando a caixa de seleção "content-available" encontrada na guia "settings" do criador do push.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

## Use notificações por push silenciosas para disparar o trabalho em segundo plano {#use-silent-push-notifications-to-trigger-background-work}

As notificações por push silenciosas podem despertar seu app de um estado "Suspenso" ou "Não em execução" para atualizar o conteúdo ou executar determinadas tarefas sem notificar os usuários.

Para usar notificações por push silenciosas para disparar o trabalho em segundo plano, configure o sinalizador `content-available` seguindo as instruções anteriores sem nenhuma mensagem ou som. Configure o modo de segundo plano do seu app para ativar `remote notifications` na guia **Capabilities** das configurações do projeto. Uma notificação remota é apenas uma notificação por push normal com o sinalizador `content-available` definido.

![Xcode mostrando a caixa de seleção do modo "remote notifications" em "capabilities".]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

A ativação do modo em segundo plano para notificações remotas é necessária para o [rastreamento de desinstalação]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift).

Mesmo com o modo de segundo plano para notificações remotas ativado, o sistema não iniciará seu app em segundo plano se o usuário tiver forçado o encerramento do aplicativo. O usuário deve iniciar explicitamente o aplicativo ou reiniciar o dispositivo antes que o app possa ser lançado automaticamente em segundo plano pelo sistema.

Para saber mais, consulte [pushing background updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc) e [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:).

## Limitações de notificações silenciosas do iOS {#ios-silent-notifications-limitations}

O sistema operacional iOS pode bloquear notificações para alguns recursos. Note que, se estiver tendo dificuldades com esses recursos, o bloqueio de notificações silenciosas do iOS pode ser a causa.

A Braze tem vários recursos que dependem de notificações por push silenciosas do iOS:

| Recurso | Experiência do usuário |
|---|---|
| Rastreamento de desinstalação | O usuário recebe um push silencioso e noturno de rastreamento de desinstalação. |
| Geofences | Sincronização silenciosa de geofences do servidor para o dispositivo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitações de notificações silenciosas do iOS" }

Consulte a documentação sobre o [método de instância](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) e as [notificações não recebidas](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) da Apple para obter mais detalhes.

[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23