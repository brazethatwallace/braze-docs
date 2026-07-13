---
nav_title: Notifications push silencieuses
article_title: Notifications push silencieuses pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence couvre l'implémentation des notifications push silencieuses dans votre application iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Notifications push silencieuses {#silent-push-notifications}

Les notifications push vous permettent d'informer votre application lorsque des événements importants se produisent. Vous pouvez envoyer une notification push lorsque vous avez de nouveaux messages instantanés à livrer, des alertes d'actualité à envoyer ou le dernier épisode de l'émission télévisée préférée de votre utilisateur prêt à être téléchargé pour un visionnage hors ligne. Les notifications push peuvent également être silencieuses, ne contenir aucun message d'alerte ni son, et être utilisées uniquement pour mettre à jour l'interface de votre application ou déclencher des tâches en arrière-plan.

Les notifications push sont idéales pour le contenu sporadique mais immédiatement important, lorsque le délai entre les récupérations en arrière-plan peut ne pas être acceptable. Les notifications push peuvent également être beaucoup plus efficaces que la récupération en arrière-plan, car votre application ne démarre que si nécessaire.

Les notifications push sont limitées en débit, alors n'hésitez pas à en envoyer autant que votre application en a besoin. iOS et les serveurs APNs contrôleront la fréquence de livraison, et vous n'aurez pas de problèmes si vous en envoyez trop. Si vos notifications push sont limitées, elles peuvent être retardées jusqu'à la prochaine fois que l'appareil envoie un paquet keep-alive ou reçoit une autre notification.

## Envoi de notifications push silencieuses {#sending-silent-push-notifications}

Pour envoyer une notification push silencieuse, définissez l'indicateur `content-available` sur `1` dans le payload d'une notification push. Lors de l'envoi d'une notification push silencieuse, vous pouvez également inclure certaines données dans le payload de la notification, afin que votre application puisse référencer l'événement. Cela pourrait vous éviter quelques requêtes réseau et augmenter la réactivité de votre application.

{% alert warning %}
Il n'est pas recommandé d'attacher à la fois un titre et un corps avec `content-available=1`, car cela peut entraîner un comportement indéfini. Pour qu'une notification soit vraiment silencieuse, excluez à la fois le titre et le corps lorsque vous définissez l'indicateur `content-available` sur `1.` Pour plus de détails, reportez-vous à la [documentation officielle d'Apple sur les mises à jour en arrière-plan](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

L'indicateur `content-available` peut être défini dans le tableau de bord de Braze ainsi que dans notre [objet Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object) dans l'[API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

![Le tableau de bord de Braze affichant la case « content-available » dans l'onglet « Settings » du compositeur de notifications push.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

## Utiliser des notifications push silencieuses pour déclencher des tâches en arrière-plan {#use-silent-push-notifications-to-trigger-background-work}

Les notifications push silencieuses peuvent faire sortir votre application d'un état « Suspended » ou « Not Running » pour mettre le contenu à jour ou exécuter certaines tâches sans en avertir vos utilisateurs.

Pour utiliser des notifications push silencieuses afin de déclencher des tâches en arrière-plan, configurez l'indicateur `content-available` en suivant les instructions précédentes, sans message ni son. Configurez le mode d'arrière-plan de votre application pour activer `remote notifications` dans l'onglet **Capabilities** des paramètres de votre projet. Une notification à distance est simplement une notification push normale avec l'indicateur `content-available` activé.

![Xcode affichant la case à cocher du mode « remote notifications » dans « Capabilities ».]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

L'activation du mode arrière-plan pour les notifications à distance est nécessaire pour le [suivi des désinstallations]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift).

Même avec le mode arrière-plan des notifications à distance activé, le système ne lancera pas votre application en arrière-plan si l'utilisateur a quitté l'application de manière forcée. L'utilisateur doit explicitement lancer l'application ou redémarrer l'appareil avant que l'application ne puisse être automatiquement lancée en arrière-plan par le système.

Pour plus d'informations, reportez-vous à la documentation sur l'[envoi de mises à jour en arrière-plan](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app?language=objc) et à [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:).

## Limitations des notifications silencieuses iOS {#ios-silent-notifications-limitations}

Le système d'exploitation iOS peut bloquer les notifications pour certaines fonctionnalités. Notez que si vous rencontrez des difficultés avec ces fonctionnalités, le blocage des notifications silencieuses d'iOS peut en être la cause.

Braze possède plusieurs fonctionnalités qui reposent sur les notifications push silencieuses iOS :

| Fonctionnalité | Expérience utilisateur |
|---|---|
| Suivi des désinstallations | L'utilisateur reçoit une notification push silencieuse et nocturne de suivi de désinstallation. |
| Géorepérages | Synchronisation silencieuse des géorepérages du serveur vers l'appareil. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitations des notifications silencieuses iOS" }

Reportez-vous à la documentation d'Apple sur les [méthodes d'instance](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) et les [notifications non reçues](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) pour plus de détails.

[8]:https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23