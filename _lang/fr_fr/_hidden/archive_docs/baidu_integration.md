---
nav_title: Intégration Baidu
article_title: Intégration de notifications push Baidu pour Android
platform: Android
permalink: /baidu_integration/
description: "Cet article montre comment configurer une intégration Baidu pour Android."
hidden: true
---
# Intégration Baidu {#baidu-integration}
{% alert warning %}
L'intégration Baidu Push de Braze est obsolète depuis le 24 mars 2022.

* **24 mars 2022 :** aucune nouvelle application Baidu ne peut être créée dans le tableau de bord de Braze.
* **15 septembre 2022 :** aucun nouveau message de notification push Baidu ne peut être créé. Les messages existants et la collecte de données ne sont pas affectés.
* **15 janvier 2023 :** Braze ne distribue plus de messages et ne collecte plus de données à partir des applications Baidu.
{% endalert %}

Braze peut envoyer des notifications push aux appareils Android à l'aide de [Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}). Notez que l'utilisation de Baidu Cloud Push ne nécessite pas la distribution de vos applications via la boutique d'applications Baidu.

## Étape 1 : Créer un compte Baidu {#step-1-create-a-baidu-account}

Pour créer un compte Baidu, rendez-vous sur le [portail Baidu](https://www.baidu.com/) et cliquez sur **登录** (Se connecter) pour faire apparaître une boîte de dialogue qui vous permettra de vous connecter ou de créer un nouveau compte.

![Portail Baidu]({% image_buster /assets/img_archive/baidu_portal.png %})

Pour créer un nouveau compte, en bas de la boîte de dialogue de connexion, cliquez sur **立即注册** (nouveau compte).

![Boîte de dialogue de connexion Baidu]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

Saisissez votre nom d'utilisateur, votre numéro de téléphone et votre mot de passe dans la page de création de compte. Ensuite, cliquez sur le bouton « Recevoir le code de vérification ». Vous recevrez alors un SMS de Baidu contenant un code de vérification. Enfin, acceptez l'accord de licence et cliquez sur **注册** (créer un compte) pour vous enregistrer. Si ces étapes de configuration échouent, essayez de vous enregistrer à l'aide de la connexion Cloud Baidu telle que décrite dans cet [article sur la connexion](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/).

![Page d'inscription Baidu]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## Étape 2 : S'enregistrer en tant que développeur Baidu {#step-2-register-as-a-baidu-developer}

Ensuite, vous devez vous inscrire en tant que développeur Baidu. Commencez par vous rendre sur le [portail des développeurs Baidu](http://developer.baidu.com/) et choisissez **注册** (créer un nouveau compte de développeur) pour commencer l'enregistrement.

![Portail des développeurs Baidu]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

Sur la page d'inscription, choisissez votre type de compte (个人 pour les particuliers, 公司 pour les entreprises) et le type de développeur (développeur est présélectionné et correct dans la plupart des cas). Saisissez votre nom, une biographie et un numéro de téléphone avec l'indicatif du pays entre parenthèses (par exemple, (1)xxxxxxxxxx). Cliquez sur **发送验证码** (envoyer le code de vérification) et entrez le code de vérification dans la ligne suivante. Les deux champs suivants, le site Internet du développeur et le logo du développeur, sont facultatifs. Acceptez l'accord de licence et cliquez sur **提交** (envoyer) pour valider. Vous disposez maintenant d'un compte de développeur Baidu.

![Page d'inscription développeur Baidu]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## Étape 3 : Enregistrer votre application auprès de Baidu {#step-3-register-your-application-with-baidu}

Pour enregistrer votre application auprès de Baidu, rendez-vous sur le [portail de projets Baidu](http://developer.baidu.com/console#app/project) et cliquez sur **创建工程** (créer un projet).

![Portail de projets Baidu]({% image_buster /assets/img_archive/baidu_project.png %})

Sur la page suivante, saisissez le nom de votre application. Les deux cases à cocher suivantes permettent d'activer des services Baidu supplémentaires. Dans la plupart des cas, elles doivent rester décochées.

![Nom de l'application Baidu]({% image_buster /assets/img_archive/baidu_app_name.png %})

Lors de la configuration de votre application, vous serez redirigé vers une console qui affiche des informations sur votre application, y compris la clé API. Ensuite, cliquez sur **云推送** (cloud push) dans la barre latérale. Sur la page suivante, cliquez sur **推送设置** (configurer les notifications push).

![Console de l'application Baidu]({% image_buster /assets/img_archive/baidu_app_console.png %})

![Page de continuation Baidu]({% image_buster /assets/img_archive/baidu_continue.png %})

Sur la page suivante, saisissez le nom du paquet de votre application (par exemple, `com.braze.sample`) et indiquez si les messages doivent être mis en cache et, le cas échéant, pendant combien de temps (en heures). Cela indique à Baidu pendant combien de temps continuer à essayer d'envoyer des messages aux utilisateurs hors ligne. Cliquez sur **保存设置** (enregistrer les paramètres) pour enregistrer.

![Configuration du cloud push Baidu]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## Étape 4 : Ajouter Baidu à votre application {#step-4-add-baidu-to-your-application}

Rendez-vous sur le [portail du SDK push Baidu](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk) et téléchargez la dernière version du SDK Android Baidu Cloud Push.

![SDK Baidu]({% image_buster /assets/img_archive/baidu_sdk.png %})

Dans le SDK, vous trouverez le fichier jar du service de notification push et les bibliothèques natives spécifiques à la plateforme. Intégrez-les à votre projet. Assurez-vous que votre application cible la version du SDK la plus élevée actuellement prise en charge par Baidu. Cette documentation est à jour pour la version `4.6.2.38` du SDK Android Baidu Cloud Push.

Ajoutez les autorisations Baidu requises suivantes au fichier `AndroidManifest.xml` de votre application.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

La bibliothèque de Baidu contient des récepteurs de diffusion qui traitent les messages de notification push entrants. Déclarez les récepteurs Baidu internes dans le fichier `AndroidManifest.xml` de votre application, à l'intérieur de l'élément `<application>`.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

Vous devrez également créer un récepteur de diffusion qui écoute les messages et les notifications push entrants. Déclarez votre récepteur dans le fichier `AndroidManifest.xml` de votre application, à l'intérieur de l'élément `<application>`. Ce récepteur devra étendre `com.baidu.android.pushservice.PushMessageReceiver` et implémenter des méthodes qui reçoivent des mises à jour d'événements depuis le service de notification push Baidu.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

Dans la méthode `onCreate()` de votre activité principale, ajoutez la ligne suivante qui enregistrera votre application auprès de Baidu et commencera à écouter les messages de notification push entrants. Assurez-vous de remplacer « Your-API-Key » par la clé API Baidu de votre projet.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Enfin, vous devrez enregistrer vos utilisateurs auprès de Braze. Dans la méthode `onBind()` du récepteur de diffusion Baidu que vous avez créé à cette étape, envoyez le `channelId` à Braze en utilisant `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Étape 5 : Enregistrer les ouvertures de notifications push {#step-5-registering-push-opens}

Baidu prend en charge l'envoi de paires clé-valeur supplémentaires avec les messages de notification push au format JSON. La méthode `public void onNotificationClicked(Context context, String title, String description, String customContentString)` de votre récepteur de diffusion sera appelée chaque fois qu'un utilisateur clique sur un message de notification push entrant. Le paramètre `customContentString` contient les données supplémentaires au format JSON. Tous les messages de Braze contiendront les deux paires clé-valeur suivantes :

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Chaque fois que `onNotificationClicked` est appelé par votre récepteur Baidu, ce dernier doit envoyer une [intention](http://developer.android.com/reference/android/content/Intent.html) à votre application contenant `customContentString`. Votre application enregistrera le clic auprès de Braze en utilisant le `customContentString`.

L'exemple de code suivant transmet `customContentString` à Braze et enregistre un clic :

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Étape 6 : Données supplémentaires {#step-6-extras}

En plus des clés réservées utilisées par Braze, le paramètre `customContentString` contiendra également toutes les paires clé-valeur personnalisées définies par l'utilisateur. Pour extraire vos paires clé-valeur, encapsulez `customContentString` dans un objet JSONObject et récupérez vos données supplémentaires :

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Étape 7 : Configurer les clés Baidu {#step-7-set-up-baidu-keys}

Vous devez saisir votre clé API Baidu et votre clé secrète Baidu dans le tableau de bord de Braze. Les deux clés sont disponibles depuis la console d'application Baidu.

Sur la page **Gérer les paramètres**, sélectionnez votre application Android China et entrez votre clé API Baidu et votre clé secrète Baidu dans la section des notifications push.

![Clé API]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## Ressources complémentaires {#additional-resources}

- [Portail Baidu](https://www.baidu.com/)
- [Portail des développeurs Baidu](http://developer.baidu.com/)
- [Portail de projets Baidu](http://developer.baidu.com/console#app/project)
- [Portail du SDK push Baidu](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Documentation sur l'intégration Baidu](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)