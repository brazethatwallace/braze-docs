## À propos des notifications push pour Android TV {#about-push-notifications-for-android-tv}

![Illustration d'un appareil Android TV utilisée pour le guide des notifications push Android TV.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Bien qu'il ne s'agisse pas d'une fonctionnalité native, l'intégration des notifications push pour Android TV est rendue possible en exploitant le SDK Braze pour Android et Firebase Cloud Messaging pour enregistrer un jeton de notification push pour Android TV. Il est cependant nécessaire de créer une interface utilisateur pour afficher le payload de la notification après sa réception.

## Prérequis {#prerequisites}

Pour utiliser cette fonctionnalité, vous devez effectuer les opérations suivantes :

- [Intégrer le SDK Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurer les notifications push pour le SDK Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## Configurer les notifications push {#setting-up-push-notifications}

Pour configurer les notifications push pour Android TV :

1. Créez une vue personnalisée dans votre application pour afficher vos notifications.
2. Créez une [fabrique de notifications personnalisée]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). Cela remplace le comportement par défaut du SDK et vous permet d'afficher manuellement les notifications. En retournant `null`, cela empêche le SDK de traiter la notification et nécessite un code personnalisé pour l'afficher. Une fois ces étapes terminées, vous pouvez commencer à envoyer des notifications push vers Android TV !<br><br>
3. (Facultatif) Pour suivre efficacement les analyses de clics, configurez le suivi des clics. Cela peut être réalisé en créant un [rappel de notification push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) pour écouter les intentions de push ouvertes et reçues de Braze.

{% alert note %}
Ces notifications **ne persistent pas** et ne sont visibles pour l'utilisateur que lorsque l'appareil les affiche. Cela est dû au fait que le centre de notifications d'Android TV ne prend pas en charge l'historique des notifications.
{% endalert %}

## Tester les notifications push Android TV {#testing-android-tv-push-notifications}

Pour vérifier que votre déploiement de notifications push fonctionne correctement, envoyez une notification depuis le tableau de bord de Braze comme vous le feriez normalement pour un appareil Android.

- **Si l'application est fermée** : le message push affichera une notification toast à l'écran.
- **Si l'application est ouverte** : vous avez la possibilité d'afficher le message dans votre propre interface hébergée. Nous vous recommandons de suivre le style d'interface de nos messages in-app du SDK Android Mobile.

## Bonnes pratiques {#best-practices}

Pour les marketeurs utilisant Braze, lancer une Campaign vers Android TV sera identique à lancer une notification push vers les applications mobiles Android. Pour cibler exclusivement ces appareils, nous vous recommandons de sélectionner l'application Android TV dans la segmentation.

La réponse de livraison et de clic retournée par FCM suivra la même convention qu'un appareil mobile Android. Par conséquent, toute erreur sera visible dans le journal d'activité du message.