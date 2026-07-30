---
nav_title: Notifications push
article_title: "Notifications push pour le SDK de Braze"
page_order: 2.3
description: "Cette page regroupe tout ce qui concerne les notifications push."
---

# Notifications push {#push-notifications}

> Les [notifications push]({{site.baseurl}}/user_guide/channels/push) vous permettent d'envoyer des notifications depuis votre application lorsque des événements importants se produisent. Vous pouvez envoyer une notification push lorsque vous avez de nouveaux messages instantanés à livrer, des alertes d'actualité à diffuser ou le dernier épisode de l'émission télévisée préférée de votre utilisateur prêt à être téléchargé pour un visionnage hors ligne. Elles sont également plus efficaces que la récupération en arrière-plan, car votre application ne se lance que lorsque c'est nécessaire.

{% alert note %}
Si l'option **Redirect to web URL** avec **Open web URL inside app** n'est pas sélectionnée, mais que le lien s'ouvre tout de même dans l'application, il est possible que l'application gère l'URL (par exemple, avec les liens universels sur iOS ou les App Links sur Android). Pour ouvrir le lien dans le navigateur, vérifiez que votre application délègue l'URL au navigateur système lorsque l'utilisateur appuie sur la notification, ou ajustez la gestion des URL de votre application afin que l'action au clic corresponde au paramètre du tableau de bord de Braze. Consultez la documentation push de votre plateforme pour savoir comment les actions au clic et la gestion des URL sont configurées.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
## À propos des notifications push pour Android TV {#about-push-notifications-for-android-tv}

![Illustration d'un appareil Android TV utilisée pour le guide des notifications push Android TV.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Bien qu'il ne s'agisse pas d'une fonctionnalité native, l'intégration des notifications push sur Android TV est rendue possible en exploitant le SDK Android de Braze et Firebase Cloud Messaging pour enregistrer un jeton push pour Android TV. Cependant, vous devez créer une interface utilisateur pour afficher le payload de la notification une fois celui-ci reçu.

## Prérequis {#prerequisites}

Pour utiliser cette fonctionnalité, vous devez effectuer les étapes suivantes :

- [Intégrer le SDK Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Configurer les notifications push pour le SDK Android de Braze]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## Configurer les notifications push {#setting-up-push-notifications}

Pour configurer les notifications push pour Android TV :

1. Créez une vue personnalisée dans votre application pour afficher vos notifications.
2. Créez une [fabrique de notifications personnalisée]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). Cela remplace le comportement par défaut du SDK et vous permet d'afficher manuellement les notifications. En renvoyant `null`, cela empêche le SDK de traiter la notification et nécessite du code personnalisé pour l'afficher. Une fois ces étapes terminées, vous pouvez commencer à envoyer des notifications push vers Android TV.<br><br>
3. (Facultatif) Pour suivre efficacement les analyses de clics, configurez le suivi des analyses de clics. Pour ce faire, créez un [rappel push]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) pour écouter les intentions d'ouverture et de réception des notifications push de Braze.

{% alert note %}
Ces notifications ne sont pas persistantes et ne sont visibles par l'utilisateur que lorsque l'appareil les affiche. Cela est dû au fait que le centre de notifications d'Android TV ne prend pas en charge l'historique des notifications.
{% endalert %}

## Tester les notifications push Android TV {#testing-android-tv-push-notifications}

Pour vérifier que votre implémentation push fonctionne correctement, envoyez une notification depuis le tableau de bord de Braze comme vous le feriez normalement pour un appareil Android.

- **Si l'application est fermée** : le message push affiche une notification toast à l'écran.
- **Si l'application est ouverte** : vous avez la possibilité d'afficher le message dans votre propre interface hébergée. Suivez le style d'interface des messages in-app du SDK Android Mobile.

## Bonnes pratiques {#best-practices}

Pour les marketeurs utilisant Braze, le lancement d'une Campaign vers Android TV est identique au lancement d'une notification push vers les applications mobiles Android. Pour cibler exclusivement ces appareils, sélectionnez l'application Android TV dans la segmentation.

La réponse de livraison et de clic renvoyée par FCM suit la même convention qu'un appareil Android mobile ; par conséquent, toute erreur est visible dans le journal d'activité des messages.

{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}