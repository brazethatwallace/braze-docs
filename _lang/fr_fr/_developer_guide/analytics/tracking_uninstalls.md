---
nav_title: Suivre les désinstallations
article_title: Suivre les désinstallations via le SDK Braze
page_order: 3.5
description: "Découvrez comment suivre les désinstallations grâce au SDK de Braze."

---

# Suivre les désinstallations {#track-uninstalls}

> Découvrez comment configurer le suivi des désinstallations via le SDK de Braze. Pour des informations générales, consultez le [Guide de l'utilisateur : Suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

{% sdktabs %}
{% sdktab android %}
## Mise en place d'un suivi des désinstallations {#setting-up-uninstall-tracking}

### Étape 1 : Mise en place du FCM {#step-1-set-up-fcm}

Le SDK Android Braze utilise Firebase Cloud Messaging (FCM) pour envoyer des notifications push silencieuses, qui sont utilisées pour collecter des analyses/analytiques de suivi de désinstallation. Si ce n'est pas déjà fait, [configurez]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#android_setting-up-push-notifications) ou [migrez vers l']({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)API Firebase Cloud Messaging pour les notifications push.

### Étape 2 : Détecter manuellement le suivi des désinstallations (facultatif) {#step-2-manually-detect-uninstall-tracking-optional}

Par défaut, le SDK Android Braze détecte et ignore automatiquement les notifications push silencieuses liées au suivi de la désinstallation. Cependant, vous pouvez choisir de détecter manuellement le suivi de la désinstallation à l'aide de la méthode [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html).

{% alert important %}
Étant donné que les notifications silencieuses pour le suivi de la désinstallation ne sont transmises à aucun rappel push de Braze, vous ne pouvez utiliser cette méthode qu'avant de transmettre une notification push à Braze.
{% endalert %}

### Étape 3 : Suppression des pings automatiques du serveur {#step-3-remove-automatic-server-pings}

Une notification push silencieuse réveille votre application et instancie le composant `Application` si l'application n'est pas déjà en cours d'exécution. Par conséquent, si vous disposez d'une sous-classe [`Application`](https://developer.android.com/reference/android/app/Application) personnalisée, supprimez toute logique qui envoie automatiquement des pings à vos serveurs pendant la méthode de cycle de vie [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()).

### Étape 4 : Activer le suivi des désinstallations {#step-4-enable-uninstall-tracking}

Enfin, activez le suivi des désinstallations dans Braze. Pour une procédure complète, consultez [Activer le suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
Le suivi des désinstallations peut être imprécis. Les indicateurs que vous voyez sur Braze peuvent être retardés ou inexacts.
{% endalert %}

{% endsdktab %}

{% sdktab swift %}
## Mise en place d'un suivi des désinstallations

### Étape 1 : Activer les notifications push d'arrière-plan {#step-1-enable-background-push}

Dans votre projet Xcode, allez dans **Capacités** et assurez-vous que les **Modes d'arrière-plan** sont activés. Pour plus d'informations, consultez la [notification push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Étape 2 : Ignorer les notifications push internes {#step-2-ignore-internal-push-notifications}

Le SDK Swift de Braze utilise des notifications push en arrière-plan pour collecter des analyses/analytiques de suivi de désinstallation. Assurez-vous que votre application [ignore les notifications push internes]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) afin qu'elle n'effectue pas d'actions non désirées lorsque celles-ci sont envoyées.

### Étape 3 : Envoyer une notification push de test (facultatif) {#step-3-send-a-test-push-optional}

Ensuite, envoyez-vous une notification push de test à partir du tableau de bord de Braze (ne vous inquiétez pas&#8212;elle ne mettra pas à jour votre profil utilisateur).

1. Allez dans **Envoi de messages** > **Campaigns** et créez une campagne de notification push à l'aide de la plateforme correspondante.
2. Allez dans **Paramètres** > **Paramètres de l'application** et ajoutez la clé `appboy_uninstall_tracking` avec la valeur `true` correspondante, puis cochez **Add Content-Available Flag**.
3. Utilisez la page **Aperçu** pour vous envoyer une notification push de test de suivi de désinstallation.
4. Vérifiez que votre application n'effectue aucune action automatique non désirée lorsqu'elle reçoit une notification push.

{% alert note %}
Un numéro de badge est envoyé avec la notification push de test&#8212;cependant, une véritable notification push de suivi de désinstallation n'envoie aucun numéro de badge.
{% endalert %}

### Étape 4 : Activer le suivi des désinstallations

Enfin, activez le suivi des désinstallations dans Braze. Pour une procédure complète, consultez [Activer le suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
Le suivi des désinstallations peut être imprécis. Les indicateurs que vous voyez sur Braze peuvent être retardés ou inexacts.
{% endalert %}

{% endsdktab %}
{% endsdktabs %}