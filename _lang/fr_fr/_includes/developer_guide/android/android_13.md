# Mise à jour vers Android 13 {#upgrading-to-android-13}

> Ce guide décrit les modifications pertinentes introduites dans Android 13 (2022) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

Reportez-vous à la [documentation destinée aux développeurs d'Android 13](https://developer.android.com/about/versions/13) pour obtenir un guide de migration complet.

## SDK Braze pour Android 13 {#android-13-braze-sdk}

Pour vous préparer à Android 13, mettez à jour votre SDK Braze vers la [dernière version (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Vous aurez ainsi accès à notre nouvelle [fonctionnalité d'amorçage de notifications push « sans code »]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Modifications dans Android 13 {#changes-in-android-13}

### Autorisation des notifications push {#push-permission}

Android 13 introduit un [changement majeur](https://developer.android.com/about/versions/13/changes/notification-permission) dans la manière dont les utilisateurs gèrent les applications qui envoient des notifications push. Dans Android 13, les applications doivent obtenir une autorisation avant que les notifications push ne puissent être affichées.

![Un message push Android demandant « Autoriser Kitchenerie à vous envoyer des notifications ? » avec deux boutons « Autoriser » et « Ne pas autoriser » en bas du message.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Cette nouvelle autorisation suit un schéma similaire à celui d'iOS et du push Web, où vous ne disposez que d'une seule tentative pour obtenir l'autorisation. Si un utilisateur choisit `Don't Allow` ou ignore l'invite, votre application ne pourra plus demander l'autorisation.

Notez que les applications bénéficient d'une [exemption](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) pour les utilisateurs qui avaient précédemment activé les notifications push avant la mise à jour vers Android 13. Ces utilisateurs [resteront éligibles](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps) pour recevoir des notifications push lorsqu'ils passeront à Android 13 sans avoir à demander l'autorisation.

#### Moment de l'invite d'autorisation {#push-permission-timing}

**Ciblage d'Android 13**

Les applications ciblant Android 13 peuvent contrôler quand demander l'autorisation et afficher l'invite de notification push native.

Si votre utilisateur passe d'Android 12 à 13, que votre application était déjà installée et que vous envoyiez déjà des notifications push, le système accorde automatiquement la nouvelle autorisation de notification à toutes les applications éligibles. En d'autres termes, ces applications peuvent continuer à envoyer des notifications aux utilisateurs, et les utilisateurs ne voient pas d'invite d'autorisation au moment de l'exécution.

Pour plus de détails, consultez la documentation développeur d'Android concernant les [effets sur les mises à jour d'applications existantes](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Ciblage d'Android 12 ou version antérieure**

Si votre application ne cible pas encore Android 13, lorsqu'un nouvel utilisateur sous Android 13 installe votre application, il verra automatiquement une invite d'autorisation de notification push lorsque votre application créera son premier canal de notification (via `notificationManager.createNotificationChannel`). Les utilisateurs qui ont déjà installé votre application et qui passent ensuite à Android 13 ne verront jamais d'invite et se verront automatiquement accorder l'autorisation de notification push.

{% alert note %}
Le SDK Braze v23.0.0 crée automatiquement un canal de notification par défaut s'il n'en existe pas déjà lorsqu'une notification push est reçue. Si vous ne ciblez pas Android 13, cela déclenchera l'affichage de l'invite d'autorisation de notification push, nécessaire pour afficher la notification.
{% endalert %}

## Préparation pour Android 13 {#next-steps}

Il est fortement recommandé de faire en sorte que votre application cible Android 13 afin de contrôler quand les utilisateurs recevront une demande d'autorisation de notification push.

Vous pourrez ainsi optimiser votre [taux d'abonnement aux notifications push](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) en invitant les utilisateurs à des moments plus appropriés, ce qui entraînera une meilleure expérience utilisateur en ce qui concerne la manière et le moment où votre application demande l'autorisation d'envoyer des notifications push.

Pour commencer à utiliser notre nouvelle [fonctionnalité d'amorçage des notifications push « sans code »]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), mettez à niveau votre SDK Android vers la [dernière version (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).