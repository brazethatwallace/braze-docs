{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Configuration des notifications push {#setting-up-push-notification}

### Étape 1 : Configurer la plateforme {#step-1-set-up-the-platform}

{% tabs %}
{% tab Android %}
#### Étape 1.1 : Activer Firebase {#step-11-enable-firebase}

Pour commencer, suivez la [documentation de configuration de Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
L'intégration du SDK Firebase Unity peut entraîner le remplacement de votre `AndroidManifest.xml`. Si cela se produit, assurez-vous de revenir à l'original.
{% endalert %}

#### Étape 1.2 : Définir vos identifiants Firebase {#step-12-set-your-firebase-credentials}

Vous devez saisir votre clé de serveur Firebase et votre ID d'expéditeur dans le tableau de bord de Braze. Pour ce faire, connectez-vous à la [Firebase Developers Console](https://console.firebase.google.com/) et sélectionnez votre projet Firebase. Ensuite, sélectionnez **Cloud Messaging** sous **Settings** et copiez la clé du serveur et l'ID de l'expéditeur :<br>![Paramètres Cloud Messaging de la console Firebase affichant la clé du serveur et l'ID de l'expéditeur.]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Dans Braze, sélectionnez votre application Android sur la page **App Settings**, sous **Manage Settings**. Saisissez ensuite votre clé de serveur Firebase dans le champ **Firebase Cloud Messaging Server Key** et l'ID d'expéditeur Firebase dans le champ **Firebase Cloud Messaging Sender ID**.

![Paramètres de l'application Android dans Braze avec les champs de clé de serveur et d'ID d'expéditeur Firebase Cloud Messaging.]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Étape 1.1 : Vérifier la méthode d'intégration {#step-11-verify-integration-method}

Braze fournit une solution Unity native pour automatiser les intégrations de notifications push iOS. Si vous préférez configurer et gérer votre intégration manuellement, consultez [Swift : Notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Sinon, passez à l'étape suivante.

{% alert note %}
Notre solution de notification push automatique tire parti de la fonctionnalité d'autorisation provisoire d'iOS 12 et n'est pas disponible avec la fenêtre contextuelle d'invite de notification push native.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Étape 1.1 : Activer ADM {#step-11-enable-adm}

1. Créez un compte sur le [portail des développeurs Amazon Apps & Games](https://developer.amazon.com/public) si vous ne l'avez pas encore fait.
2. Obtenez les [identifiants OAuth (ID client et secret client) et une clé API ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Activez **Automatic ADM Registration Enabled** dans la fenêtre de configuration de Braze Unity.
  - Vous pouvez également ajouter la ligne suivante à votre fichier `res/values/braze.xml` pour activer l'enregistrement ADM :

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Étape 2 : Configurer les notifications push {#step-2-configure-push-notifications}

{% tabs %}
{% tab Android %}
#### Étape 2.1 : Configurer les paramètres push {#unity_step-21-configure-push-settings}

Le SDK Braze peut gérer automatiquement l'enregistrement push auprès des serveurs Firebase Cloud Messaging pour que les appareils reçoivent des notifications push. Dans Unity, activez **Automate Unity Android Integration**, puis configurez les paramètres de **Push Notification** suivants.

| Paramètre | Description |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatic Firebase Cloud Messaging Registration Enabled | Indique au SDK Braze de récupérer et d'envoyer automatiquement un jeton de notification push FCM pour un appareil. |
| Firebase Cloud Messaging Sender ID | L'ID de l'expéditeur provenant de votre console Firebase. |
| Handle Push Deeplinks Automatically | Indique si le SDK doit gérer l'ouverture des liens profonds ou de l'application lorsque des notifications push sont cliquées. |
| Small Notification Icon Drawable | Référence de ressource drawable Android pour la petite icône affichée lorsqu'une notification push arrive. Saisissez la référence complète incluant le préfixe `@drawable/` (par exemple, `@drawable/hourglass_icon`). L'intégration automatique écrit cette valeur dans `braze.xml` telle que saisie. Si vous laissez ce champ vide, la notification utilise l'icône de l'application comme petite icône. |
| Large Notification Icon Drawable | Grande icône facultative pour les notifications. Utilisez le même format `@drawable/` que pour la petite icône (par exemple, `@drawable/my_large_icon`). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2.1: Configure push settings" }

{% alert note %}
**Small Notification Icon Drawable** et **Large Notification Icon Drawable** apparaissent sous **Push Configuration** dans **Braze > Braze Configuration**. Les deux valeurs sont écrites dans `braze.xml` telles que vous les saisissez. Incluez le préfixe `@drawable/` vous-même — l'intégration Braze Unity ne l'ajoute pas pour vous (par exemple, `<drawable name="com_braze_push_small_notification_icon">@drawable/hourglass_icon</drawable>`).
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Étape 2.1 : Télécharger votre jeton APNs {#step-21-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Étape 2.2 : Activer le push automatique {#step-22-enable-automatic-push}

Ouvrez les paramètres de configuration de Braze dans l'éditeur Unity en accédant à **Braze > Braze Configuration**.

Cochez **Integrate Push With Braze** pour inscrire automatiquement les utilisateurs aux notifications push, transmettre les jetons push à Braze, suivre l'analytique des ouvertures de push et tirer parti de notre gestion par défaut des notifications push.

#### Étape 2.3 : Activer le push en arrière-plan (facultatif) {#step-23-enable-background-push-optional}

Cochez **Enable Background Push** si vous souhaitez activer le `background mode` pour les notifications push. Cela permet au système de réveiller votre application depuis l'état `suspended` lorsqu'une notification push est reçue, permettant à votre application de télécharger du contenu en réponse aux notifications push. Cocher cette option est nécessaire pour notre fonctionnalité de suivi de la désinstallation.

![L'éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, les options « Automate Unity iOS integration », « Integrate push with Braze » et « Enable background push » sont activées.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Étape 2.4 : Désactiver l'enregistrement automatique (facultatif) {#step-24-disable-automatic-registration-optional}

Les utilisateurs qui n'ont pas encore accepté les notifications push seront automatiquement autorisés à recevoir des notifications push lors de l'ouverture de votre application. Pour désactiver cette fonctionnalité et enregistrer manuellement les utilisateurs pour le push, cochez **Disable Automatic Push Registration**.

- Si la case **Disable Provisional Authorization** n'est pas cochée sous iOS 12 ou une version ultérieure, l'utilisateur sera provisoirement (silencieusement) autorisé à recevoir des notifications push silencieuses. Si cette option est cochée, l'utilisateur verra l'invite de notification push native.
- Si vous devez configurer exactement quand l'invite est affichée lors de l'exécution, désactivez l'enregistrement automatique depuis l'éditeur de configuration Braze et utilisez `AppboyBinding.PromptUserForPushPermissions()` à la place.

![L'éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, les options « Automate Unity iOS integration », « Integrate push with Braze » et « Disable automatic push registration » sont activées.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Étape 2.1 : Mettre à jour `AndroidManifest.xml` {#unity_step-21-update-androidmanifestxml}

Si votre application n'a pas de `AndroidManifest.xml`, vous pouvez utiliser le modèle suivant. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que toutes les sections manquantes suivantes sont ajoutées à votre `AndroidManifest.xml` existant.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:label="@string/app_name"
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Étape 2.2 : Stocker votre clé API ADM {#step-22-store-your-adm-api-key}

Tout d'abord, [générez une clé API ADM pour votre application](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), puis enregistrez la clé dans un fichier nommé `api_key.txt` et ajoutez-le dans le répertoire [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) de votre projet.

{% alert important %}
Amazon ne reconnaîtra pas votre clé si `api_key.txt` contient des caractères d'espacement, comme un saut de ligne en fin de fichier.
{% endalert %}

Ensuite, dans votre fichier `mainTemplate.gradle`, ajoutez ce qui suit :

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Étape 2.3 : Ajouter le Jar ADM {#step-23-add-adm-jar}

Le fichier Jar ADM requis peut être placé n'importe où dans votre projet, conformément à la [documentation JAR d'Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

#### Étape 2.4 : Ajouter le secret client et l'ID client à votre tableau de bord de Braze {#step-24-add-client-secret-and-client-id-to-your-braze-dashboard}

Enfin, vous devez ajouter le secret client et l'ID client que vous avez obtenus à l'[étape 1](#unity_step-1-enable-adm) à la page **Manage Settings** du tableau de bord de Braze.

![Page des paramètres de l'application Fire OS dans Braze avec les champs ID client et secret client ADM.]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Étape 3 : Définir les écouteurs push {#step-3-set-push-listeners}

{% tabs %}
{% tab Android %}
#### Étape 3.1 : Activer l'écouteur de réception push {#step-31-enable-push-received-listener}

L'écouteur de réception push est déclenché lorsqu'un utilisateur reçoit une notification push. Pour envoyer le payload push à Unity, définissez le nom de votre objet de jeu et la méthode de rappel de l'écouteur de réception push sous **Set Push Received Listener**.

#### Étape 3.2 : Activer l'écouteur d'ouverture push {#step-32-enable-push-opened-listener}

L'écouteur d'ouverture push est déclenché lorsqu'un utilisateur lance l'application en cliquant sur une notification push. Pour envoyer le payload push à Unity, définissez le nom de votre objet de jeu et la méthode de rappel de l'écouteur d'ouverture push sous **Set Push Opened Listener**.

#### Étape 3.3 : Activer l'écouteur de suppression push {#step-33-enable-push-deleted-listener}

L'écouteur de suppression push est déclenché lorsqu'un utilisateur balaie ou rejette une notification push. Pour envoyer le payload push à Unity, définissez le nom de votre objet de jeu et la méthode de rappel de l'écouteur de suppression push sous **Set Push Deleted Listener**.

#### Exemple d'écouteur push {#push-listener-example}

L'exemple suivant implémente l'objet de jeu `BrazeCallback` en utilisant respectivement les noms de méthode de rappel `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` et `PushNotificationDeletedCallback`.

![Ce graphique d'exemple d'implémentation montre les options de configuration Braze mentionnées dans les sections précédentes et un extrait de code C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Swift %}
#### Étape 3.1 : Activer l'écouteur de réception push

L'écouteur de réception push est déclenché lorsqu'un utilisateur reçoit une notification push alors qu'il utilise activement l'application (par exemple, lorsque l'application est au premier plan). Définissez l'écouteur de réception push dans l'éditeur de configuration Braze. Si vous devez configurer votre écouteur d'objet de jeu lors de l'exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_RECEIVED`.

![L'éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l'option « Set Push Received Listener » est développée, et le « Game Object Name » (AppBoyCallback) et le « Callback Method Name » (PushNotificationReceivedCallback) sont fournis.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Étape 3.2 : Activer l'écouteur d'ouverture push

L'écouteur d'ouverture push est déclenché lorsqu'un utilisateur lance l'application en cliquant sur une notification push. Pour envoyer le payload push à Unity, définissez le nom de votre objet de jeu et la méthode de rappel de l'écouteur d'ouverture push sous l'option **Set Push Opened Listener** :

![L'éditeur Unity affiche les options de configuration Braze. Dans cet éditeur, l'option « Set Push Opened Listener » est développée, et le « Game Object Name » (AppBoyCallback) et le « Callback Method Name » (PushNotificationOpenedCallback) sont fournis.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Si vous devez configurer votre écouteur d'objet de jeu lors de l'exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.PUSH_OPENED`.

#### Exemple d'écouteur push

L'exemple suivant implémente l'objet de jeu `AppboyCallback` en utilisant respectivement les noms de méthode de rappel `PushNotificationReceivedCallback` et `PushNotificationOpenedCallback`.

![Ce graphique d'exemple d'implémentation montre les options de configuration Braze mentionnées dans les sections précédentes et un extrait de code C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Amazon Device Messaging %}
En mettant à jour votre `AndroidManifest.xml` à l'[étape précédente](#unity_step-21-update-androidmanifestxml), les écouteurs push ont été automatiquement configurés lorsque vous avez ajouté les lignes suivantes. Aucune configuration supplémentaire n'est donc nécessaire.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Pour en savoir plus sur les écouteurs push ADM, consultez [Amazon : Intégrer Amazon Device Messaging](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configurations facultatives {#optional-configurations}

{% tabs %}
{% tab Android %}
### Liens profonds vers des ressources in-app {#deep-linking-to-in-app-resources}

Bien que Braze puisse gérer les liens profonds standard par défaut (tels que les URL de sites web, les URI Android, etc.), la création de liens profonds personnalisés nécessite une configuration supplémentaire du Manifeste.

Pour obtenir des conseils sur la configuration, consultez [Deep Linking to In-App Resources](https://developer.android.com/training/app-links/deep-linking).

#### Ajout d'icônes de notification push Braze {#adding-braze-push-notification-icons}

{% alert important %}
N'ajoutez pas d'images d'icônes de notification sous `Assets/Plugins/Android/res`. Unity [a déprécié la fourniture de ressources Android dans ce chemin](https://support.unity.com/hc/en-us/articles/115005875443-Providing-Android-resources-in-Assets-Plugins-Android-res-is-deprecated), ce qui peut générer des avertissements de build ou des erreurs de validation. Empaquetez vos drawables d'icônes dans un [plug-in Android Archive (AAR)](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) ou un projet de bibliothèque Android afin qu'ils soient fusionnés dans les ressources de l'application compilée comme tout autre drawable.
{% endalert %}

Pour ajouter des icônes push à votre projet, créez un plug-in AAR ou une bibliothèque Android contenant les fichiers d'image des icônes sous `res/drawable*` (ou des dossiers spécifiques à la densité), puis référencez chaque icône dans **Braze > Braze Configuration** en utilisant le nom complet de la ressource `@drawable/` (voir [Étape 2.1 : Configurer les paramètres push](#unity_step-21-configure-push-settings)). Pour les étapes d'empaquetage et d'importation dans Unity, consultez [Android Library Projects and Android Archive plug-ins](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).

Pour les règles de conception des petites icônes (alpha uniquement, sans couleur), consultez [Notifications push Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android), étape 2 : conformer les petites icônes aux directives de conception.
{% endtab %}

{% tab Swift %}
#### Rappel de jeton push {#push-token-callback}

Pour recevoir une copie des jetons d'appareil Braze depuis le système d'exploitation, définissez un délégué à l'aide de `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
Il n'y a pas de configurations facultatives pour ADM à l'heure actuelle.
{% endtab %}
{% endtabs %}