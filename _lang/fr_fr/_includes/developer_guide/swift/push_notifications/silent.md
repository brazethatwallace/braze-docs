{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Limites d'iOS {#ios-limitations}

Le système d'exploitation iOS peut bloquer les notifications pour certaines fonctionnalités. Notez que si vous rencontrez des difficultés avec ces fonctionnalités, le blocage des notifications silencieuses d'iOS peut en être la cause. Pour plus de détails, consultez la documentation d'Apple sur les [méthodes d'instance](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) et les [notifications non reçues](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

## Mise en place de notifications push silencieuses {#setting-up-silent-push-notifications}

Pour utiliser les notifications push silencieuses afin de déclencher des tâches en arrière-plan, vous devez configurer votre application de manière à recevoir des notifications même lorsqu'elle est en arrière-plan. Pour ce faire, ajoutez la capacité Background Modes à l'aide du volet **Signing & Capabilities** à la cible principale de l'application dans Xcode. Cochez la case **Remote notifications**.

![Xcode affichant la case à cocher du mode « remote notifications » dans « capabilities ».]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Même avec le mode arrière-plan des notifications à distance activé, le système ne lancera pas votre application en arrière-plan si l'utilisateur a quitté l'application de manière forcée. L'utilisateur doit explicitement lancer l'application ou redémarrer l'appareil avant que l'application ne puisse être automatiquement lancée en arrière-plan par le système.

Pour plus d'informations, consultez la documentation sur l'[envoi de mises à jour en arrière-plan](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) et la [documentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) de `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Envoi de notifications push silencieuses {#sending-silent-push-notifications}

Pour envoyer une notification push silencieuse, définissez l'indicateur `content-available` sur `1` dans le payload d'une notification push.

{% alert note %}
Ce qu'Apple appelle une notification à distance est simplement une notification push normale avec l'indicateur `content-available` activé.
{% endalert %}

L'indicateur `content-available` peut être défini dans le tableau de bord de Braze ainsi que dans notre [objet Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) via l'[API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/).

{% alert warning %}
Il n'est pas recommandé d'associer un titre et un corps avec `content-available=1`, car cela peut entraîner un comportement indéfini. Pour qu'une notification soit véritablement silencieuse, excluez à la fois le titre et le corps lorsque vous définissez l'indicateur `content-available` sur `1.` Pour plus de détails, consultez la [documentation officielle d'Apple sur les mises à jour en arrière-plan](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![Le tableau de bord de Braze affichant la case « content-available » dans l'onglet « paramètres » du compositeur de push.]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

Lors de l'envoi d'une notification push silencieuse, vous pouvez également inclure des données dans le payload de la notification, afin que votre application puisse référencer l'événement. Cela peut vous éviter quelques requêtes réseau et améliorer la réactivité de votre application.

## Ignorer les notifications push internes {#ignoring-internal-push-notifications}

Braze utilise des notifications push silencieuses pour gérer en interne certaines fonctionnalités avancées, telles que le suivi des désinstallations. Si votre application effectue des actions automatiques au lancement ou lors de pushs en arrière-plan, envisagez de conditionner cette activité afin qu'elle ne soit pas déclenchée par des notifications push internes.

Par exemple, si votre logique appelle vos serveurs pour obtenir du nouveau contenu à chaque push en arrière-plan ou lancement d'application, vous souhaiterez peut-être empêcher le déclenchement des pushs internes de Braze afin d'éviter un trafic réseau inutile. Étant donné que Braze envoie certains types de pushs internes à tous les utilisateurs à peu près au même moment, une charge serveur importante peut survenir si les appels réseau au lancement provenant de pushs internes ne sont pas contrôlés.

### Étape 1 : Vérifiez les actions automatiques de votre application {#step-1-check-your-app-for-automatic-actions}

Vérifiez que votre application ne contient pas d'actions automatiques aux endroits suivants et mettez à jour votre code pour ignorer les pushs internes de Braze :

1. **Récepteurs de push.** Les notifications push en arrière-plan appellent `application:didReceiveRemoteNotification:fetchCompletionHandler:` sur le `UIApplicationDelegate`.
2. **Délégué d'application.** Les pushs en arrière-plan peuvent lancer les applications [suspendues](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) en arrière-plan, déclenchant les méthodes `application:willFinishLaunchingWithOptions:` et `application:didFinishLaunchingWithOptions:` sur votre `UIApplicationDelegate`. Vérifiez les `launchOptions` de ces méthodes pour déterminer si l'application a été lancée à partir d'un push en arrière-plan.

### Étape 2 : Utilisez la méthode utilitaire de push interne {#step-2-use-the-internal-push-utility-method}

Vous pouvez utiliser la méthode utilitaire statique dans `Braze.Notifications` pour vérifier si votre application a reçu ou a été lancée par un push interne de Braze. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) renvoie `true` pour toutes les notifications push internes de Braze, ce qui inclut le suivi des désinstallations et les notifications de synchronisation des [indicateurs de fonctionnalité]({{site.baseurl}}/user_guide/messaging/feature_flags/).

Par exemple :

{% tabs %}
{% tab swift %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}