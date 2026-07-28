{% multi_lang_include developer_guide/prerequisites/android.md %}

## Configuration des notifications push {#setting-up-push-notifications}

Les téléphones récents fabriqués par [Huawei](https://huaweimobileservices.com/) sont équipés des services mobiles Huawei (HMS), un service utilisé pour envoyer des notifications push au lieu de recourir à Firebase Cloud Messaging (FCM) de Google.

### Étape 1 : Enregistrer un compte de développeur Huawei {#step-1-register-for-a-huawei-developer-account}

Avant de commencer, vous devrez vous enregistrer et configurer un [compte de développeur Huawei](https://developer.huawei.com/consumer/en/console). Dans votre compte Huawei, allez dans **My Projects > Project Settings > App Information**, et notez les valeurs `App ID` et `App secret`.

![Page d'informations de l'application dans la console développeur Huawei affichant l'App ID et l'App secret.]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### Étape 2 : Créer une nouvelle application Huawei dans le tableau de bord de Braze {#step-2-create-a-new-huawei-app-in-the-braze-dashboard}

Dans le tableau de bord de Braze, allez dans **Paramètres de l'application**, accessible sous la navigation **Paramètres**.

Cliquez sur **+ Add App**, fournissez un nom (comme Mon application Huawei) et sélectionnez `Android` comme plateforme.

![Boîte de dialogue d'ajout d'application Braze pour créer une application Android Huawei.]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Une fois votre nouvelle application Braze créée, localisez les paramètres de notification push et sélectionnez `Huawei` comme fournisseur de notification push. Ensuite, renseignez votre `Huawei Client Secret` et votre `Huawei App ID`.

![Paramètres du fournisseur de notifications push Huawei dans Braze avec les champs Huawei App ID et Client Secret.]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### Étape 3 : Intégrer le SDK de messagerie Huawei à votre application {#step-3-integrate-the-huawei-messaging-sdk-into-your-app}

Huawei a fourni un [codelab d'intégration Android](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) détaillant l'intégration du Huawei Messaging Service dans votre application. Suivez ces étapes pour commencer.

Après avoir terminé le codelab, vous devrez créer un [service de messages Huawei](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) personnalisé pour obtenir des jetons push et transmettre les messages au SDK de Braze.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

Après avoir ajouté votre service de notification push personnalisé, ajoutez les éléments suivants à votre `AndroidManifest.xml` :

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Étape 4 : Gérer les notifications en premier plan {#step-4-handle-foreground-notifications}

Par défaut, lorsqu'une notification push arrive alors que votre application est au premier plan, Huawei l'affiche automatiquement. Pour que Braze traite le payload de la notification push (à des fins de suivi analytique, de gestion des deep links et de traitement personnalisé), acheminez les données push entrantes vers Braze à l'intérieur de votre méthode `HmsMessageService.onMessageReceived`.

Lorsque vous appelez `BrazeHuaweiPushHandler.handleHmsRemoteMessageData`, Braze détermine si le payload correspond à une notification push Braze et, si tel est le cas, crée et affiche la notification. Pour plus d'informations, consultez la section [Gestion des notifications en premier plan]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) dans la documentation relative aux notifications push Android.

Pour un exemple complet, consultez la [référence du gestionnaire Huawei](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-huawei-push-handler/index.html) dans la documentation du SDK Android de Braze.

### Étape 5 : Tester vos notifications push (facultatif) {#step-5-test-your-push-notifications-optional}

À ce stade, vous avez créé une nouvelle application Android Huawei dans le tableau de bord de Braze, l'avez configurée avec vos identifiants de développeur Huawei et avez intégré les SDK Braze et Huawei dans votre application.

Vous pouvez maintenant tester l'intégration en lançant une nouvelle campagne de notifications push dans Braze.

#### Étape 5.1 : Créer une nouvelle campagne de notifications push {#step-51-create-a-new-push-notification-campaign}

Dans la page **Campaigns**, créez une nouvelle campagne et choisissez **Push Notification** comme type de message.

Après avoir nommé votre campagne, choisissez **Android Push** comme plateforme de notification push.

![L'éditeur de création de campagne affichant les plateformes push disponibles.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

Ensuite, composez votre campagne de notification push avec un titre et un message.

#### Étape 5.2 : Envoyer un test de notification push {#step-52-send-a-test-push}

Dans l'onglet **Test**, entrez votre ID utilisateur, que vous avez défini dans votre application à l'aide de la [méthode `changeUser(USER_ID_STRING)`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#assigning-a-user-id), et cliquez sur **Send Test** pour envoyer une notification push de test.

![L'onglet « Test » dans l'éditeur de création de campagne vous permet d'envoyer un message test à vous-même en fournissant votre ID utilisateur et en le saisissant dans le champ « Add Individual Users ».]({% image_buster /assets/img/huawei/huawei-test-send.png %})

À ce stade, vous devriez recevoir une notification push de test sur votre appareil Huawei (HMS) de la part de Braze.

#### Étape 5.3 : Configurer la segmentation Huawei (facultatif) {#step-53-set-up-huawei-segmentation-optional}

Étant donné que votre application Huawei dans le tableau de bord de Braze repose sur la plateforme de notification push Android, vous avez la possibilité d'envoyer des notifications push à tous les utilisateurs Android (Firebase Cloud Messaging et Huawei Mobile Services), ou de segmenter l'audience de votre campagne pour cibler des applications spécifiques.

Pour envoyer des notifications push uniquement aux applications Huawei, [créez un nouveau Segment]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) et sélectionnez votre application Huawei dans la section **Apps**.

![Filtre d'application de Segment dans Braze sélectionnant l'application Huawei pour le ciblage push.]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Bien entendu, si vous souhaitez envoyer la même notification push à tous les fournisseurs de push Android, vous pouvez choisir de ne pas spécifier l'application, ce qui enverra la notification à toutes les applications Android configurées dans l'espace de travail actuel.