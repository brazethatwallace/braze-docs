## À propos du SDK Unity Braze {#about-the-unity-braze-sdk}

Pour obtenir la liste complète des types, fonctions, variables et autres, consultez le [fichier de déclaration Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs). En outre, si vous avez déjà intégré Unity manuellement pour iOS, vous pouvez [passer à une intégration automatisée](#unity_automated-integration) à la place.

## Intégration du SDK Unity {#integrating-the-unity-sdk}

### Conditions préalables {#prerequisites}

Avant de commencer, vérifiez que votre environnement est pris en charge par la [dernière version du SDK Braze Unity](https://github.com/braze-inc/braze-unity-sdk/releases).

### Étape 1 : Choisissez votre package Braze Unity {#step-1-choose-your-braze-unity-package}

{% tabs %}
{% tab Android %}
Le [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) Braze regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu'une interface C#.

Plusieurs packages Braze Unity sont disponibles au téléchargement sur la [page des versions de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) :

- `Appboy.unitypackage`
    - Ce package regroupe les SDK Android et iOS de Braze ainsi que la dépendance [SDWebImage](https://github.com/SDWebImage/SDWebImage) pour le SDK iOS, nécessaire au bon fonctionnement des messages in-app et des fonctionnalités Content Cards de Braze sur iOS. Le framework SDWebImage est utilisé pour télécharger et afficher des images, y compris des GIF. Si vous souhaitez utiliser l'ensemble des fonctionnalités de Braze, téléchargez et importez ce package.
- `Appboy-nodeps.unitypackage`
    - Ce package est similaire à `Appboy.unitypackage`, à l'exception du framework [SDWebImage](https://github.com/SDWebImage/SDWebImage) qui n'est pas inclus. Ce package est utile si vous ne souhaitez pas que le framework SDWebImage soit présent dans votre application iOS.

{% alert note %}
À partir d'Unity 2.6.0, l'artefact groupé du SDK Android de Braze nécessite les dépendances [AndroidX](https://developer.android.com/jetpack/androidx). Si vous utilisiez auparavant un `jetified unitypackage`, vous pouvez effectuer la transition en toute sécurité vers le `unitypackage` correspondant.

Si les compilations Android échouent avec le message « This project uses AndroidX dependencies, but the 'android.useAndroidX' property is not enabled », activez [Custom Gradle Properties Template](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) dans vos paramètres de publication Unity. Ouvrez ensuite `Assets/Plugins/Android/gradleTemplate.properties` et définissez `android.useAndroidX=true`. Pour un modèle fonctionnel, consultez l'[application exemple Braze Unity](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples) et son fichier [`gradleTemplate.properties`](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/gradleTemplate.properties).
{% endalert %}
{% endtab %}

{% tab Swift %}
Le [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) Braze regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu'une interface C#.

Le package Braze Unity est disponible au téléchargement sur la [page des versions de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) avec deux options d'intégration :

1. `Appboy.unitypackage` uniquement
  - Ce package regroupe les SDK Android et iOS de Braze sans aucune dépendance supplémentaire. Avec cette méthode d'intégration, les messages in-app et les fonctionnalités Content Cards de Braze ne fonctionneront pas correctement sur iOS. Si vous souhaitez utiliser l'ensemble des fonctionnalités de Braze sans code personnalisé, utilisez plutôt l'option ci-dessous.
  - Pour utiliser cette option d'intégration, assurez-vous que la case à côté de `Import SDWebImage dependency` est *décochée* dans l'interface Unity sous « Braze Configuration ».
2. `Appboy.unitypackage` avec `SDWebImage`
  - Cette option d'intégration regroupe les SDK Android et iOS de Braze ainsi que la dépendance [SDWebImage](https://github.com/SDWebImage/SDWebImage) pour le SDK iOS, nécessaire au bon fonctionnement des messages in-app et des fonctionnalités Content Cards de Braze sur iOS. Le framework `SDWebImage` est utilisé pour télécharger et afficher des images, y compris des GIF. Si vous souhaitez utiliser l'ensemble des fonctionnalités de Braze, téléchargez et importez ce package.
  - Pour importer automatiquement `SDWebImage`, veillez à *cocher* la case à côté de `Import SDWebImage dependency` dans l'interface Unity sous « Braze Configuration ».

{% alert note %}
Pour savoir si vous avez besoin de la dépendance [SDWebImage](https://github.com/SDWebImage/SDWebImage) pour votre projet iOS, consultez la [documentation sur les messages in-app iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).
{% endalert %}
{% endtab %}
{% endtabs %}

### Étape 2 : Importer le package {#step-2-import-the-package}

{% tabs %}
{% tab Android %}
Dans l'éditeur Unity, importez le package dans votre projet Unity en accédant à **Assets > Import Package > Custom Package**. Cliquez ensuite sur **Import**.

Vous pouvez également suivre les instructions d'[importation de packages d'actifs Unity](https://docs.unity3d.com/Manual/AssetPackages.html) pour un guide plus détaillé sur l'importation de packages Unity personnalisés.

{% alert note %}
Si vous souhaitez importer uniquement le plug-in iOS ou Android, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l'importation du `.unitypackage` Braze.
{% endalert %}
{% endtab %}

{% tab Swift %}
Dans l'éditeur Unity, importez le package dans votre projet Unity en accédant à **Assets > Import Package > Custom Package**. Cliquez ensuite sur **Import**.

Vous pouvez également suivre les instructions d'[importation de packages d'actifs Unity](https://docs.unity3d.com/Manual/AssetPackages.html) pour un guide plus détaillé sur l'importation de packages Unity personnalisés.

{% alert note %}
Si vous souhaitez importer uniquement le plug-in iOS ou Android, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l'importation du `.unitypackage` Braze.
{% endalert %}
{% endtab %}
{% endtabs %}

### Étape 3 : Configurer le SDK {#step-3-configure-the-sdk}

{% tabs %}
{% tab Android %}
#### Étape 3.1 : Configurer `AndroidManifest.xml` {#step-31-configure-androidmanifestxml}

Configurez [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) pour que le SDK Braze puisse fonctionner. Si votre application ne dispose pas d'un `AndroidManifest.xml`, vous pouvez utiliser le modèle suivant. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que les sections manquantes suivantes sont ajoutées à votre `AndroidManifest.xml` existant.

1. Accédez au répertoire `Assets/Plugins/Android/` et ouvrez votre fichier `AndroidManifest.xml`. Il s'agit de l'[emplacement par défaut dans l'éditeur Unity](https://docs.unity3d.com/Manual/android-manifest.html).
2. Dans votre `AndroidManifest.xml`, ajoutez les permissions et activités requises à partir du modèle suivant.
3. Lorsque vous aurez terminé, votre `AndroidManifest.xml` ne devrait contenir qu'une seule Activity avec `"android.intent.category.LAUNCHER"`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:theme="@style/UnityThemeSelector"
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

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

{% alert important %}
Toutes les classes Activity enregistrées dans votre fichier `AndroidManifest.xml` doivent être pleinement intégrées au SDK Android de Braze, sinon vos données analytiques ne seront pas collectées. Si vous ajoutez votre propre classe Activity, veillez à [étendre le lecteur Braze Unity](#unity_extend-unity-player) pour éviter ce problème.
{% endalert %}

#### Étape 3.2 : Mettre à jour `AndroidManifest.xml` avec le nom de votre package {#step-32-update-androidmanifestxml-with-your-package-name}

Pour trouver le nom de votre package, cliquez sur **File > Build Settings > Player Settings > Android Tab**.

![Onglet Android des paramètres du lecteur Unity affichant le nom du package de l'application.]({% image_buster /assets/img_archive/UnityPackageName.png %})

Dans votre `AndroidManifest.xml`, toutes les instances de `REPLACE_WITH_YOUR_PACKAGE_NAME` doivent être remplacées par votre `Package Name` de l'étape précédente.

#### Étape 3.3 : Ajouter les dépendances Gradle {#step-33-add-gradle-dependencies}

Pour ajouter des dépendances Gradle à votre projet Unity, activez d'abord [« Custom Main Gradle Template »](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) dans vos paramètres de publication. Cela créera un fichier Gradle modèle que votre projet utilisera. Un fichier Gradle gère la configuration des dépendances et d'autres paramètres du projet au moment de la compilation. Pour plus d'informations, consultez le fichier [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle) de l'application exemple Braze Unity.

Les dépendances suivantes sont requises :

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

Vous pouvez également définir ces dépendances à l'aide de l'[External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver).

#### Étape 3.4 : Automatiser l'intégration Unity Android {#step-34-automate-the-unity-android-integration}

Braze fournit une solution Unity native pour automatiser l'intégration Unity Android.

1. Dans l'éditeur Unity, ouvrez les paramètres de configuration de Braze en accédant à **Braze > Braze Configuration**.
2. Cochez la case **Automate Unity Android Integration**.
3. Dans le champ **Braze API Key**, saisissez la clé API de votre application disponible dans **Gérer les paramètres** depuis le tableau de bord de Braze.

{% alert note %}
Cette intégration automatique ne doit pas être utilisée avec un fichier `braze.xml` créé manuellement, car les valeurs de configuration pourraient entrer en conflit lors de la compilation du projet. Si vous avez besoin d'un `braze.xml` manuel, désactivez l'intégration automatique.
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Étape 3.1 : Définir votre clé API {#step-31-set-your-api-key}

Braze fournit une solution Unity native pour automatiser l'intégration Unity iOS. Cette solution modifie le projet Xcode compilé à l'aide du [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) de Unity et crée une sous-classe de `UnityAppController` avec la macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. Dans l'éditeur Unity, ouvrez les paramètres de configuration de Braze en accédant à **Braze > Braze Configuration**.
2. Cochez la case **Automate Unity iOS Integration**.
3. Dans le champ **Braze API Key**, saisissez la clé API de votre application disponible dans **Gérer les paramètres**.

![Fenêtre de configuration Braze dans Unity avec les champs Automate Unity iOS Integration et Braze API Key.]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Si votre application utilise déjà une autre sous-classe de `UnityAppController`, vous devrez fusionner votre implémentation de sous-classe avec `AppboyAppDelegate.mm`.
{% endtab %}
{% endtabs %}

## Personnaliser le package Unity {#customizing-the-unity-package}

### Étape 1 : Cloner le dépôt {#step-1-clone-the-repository}

Dans votre terminal, clonez le [dépôt GitHub du SDK Braze Unity](https://github.com/braze-inc/braze-unity-sdk), puis naviguez jusqu'à ce dossier :

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### Étape 2 : Exporter le package depuis le dépôt {#step-2-export-package-from-repository}

Tout d'abord, lancez Unity et laissez-le tourner en arrière-plan. Ensuite, à la racine du dépôt, exécutez la commande suivante pour exporter le package vers `braze-unity-sdk/unity-package/`.

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous rencontrez des problèmes après avoir exécuté ces commandes, consultez [Unity : arguments de la ligne de commande](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html).
{% endalert %}

### Étape 3 : Importer le package dans Unity {#step-3-import-package-into-unity}

1. Dans Unity, importez le package souhaité dans votre projet Unity en accédant à **Assets** > **Import Package** > **Custom Package**.
2. S'il y a des fichiers que vous ne souhaitez pas importer, désélectionnez-les maintenant.
3. Personnalisez le package Unity exporté situé dans `Assets/Editor/Build.cs`.

## Passer à une intégration automatisée (Swift uniquement) {#automated-integration}

Pour profiter de l'intégration iOS automatisée proposée dans le SDK Braze Unity, suivez ces étapes pour passer d'une intégration manuelle à une intégration automatisée.

1. Supprimez tout le code lié à Braze de la sous-classe `UnityAppController` de votre projet Xcode.
2. Supprimez les bibliothèques iOS de Braze de votre projet Unity ou Xcode (telles que `Appboy_iOS_SDK.framework` et `SDWebImage.framework`).
3. Importez à nouveau le package Braze Unity dans votre projet. Pour une procédure complète, consultez [Étape 2 : Importer le package](#unity_step-2-import-the-package).
4. Définissez à nouveau votre clé API. Pour une procédure complète, consultez [Étape 3.1 : Définir votre clé API](#unity_step-31-set-your-api-key).

## Configurations optionnelles {#optional-configurations}

### Journalisation détaillée {#verbose-logging}

Pour activer la journalisation détaillée dans l'éditeur Unity, procédez comme suit :

1. Ouvrez les paramètres de configuration de Braze en accédant à **Braze** > **Braze Configuration**.
2. Cliquez sur le menu déroulant **Show Braze Android Settings**.
3. Dans le champ **SDK Log Level**, saisissez la valeur « 0 ».

### Compatibilité Prime 31 {#prime-31-compatibility}

Pour utiliser le plug-in Braze Unity avec les plug-ins Prime31, modifiez le fichier `AndroidManifest.xml` de votre projet pour utiliser les classes Activity compatibles Prime31. Remplacez toutes les références de
`com.braze.unity.BrazeUnityPlayerActivity` par `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

### Amazon Device Messaging (ADM)

Braze prend en charge l'intégration des [notifications push ADM](https://developer.amazon.com/public/apis/engage/device-messaging) dans les applications Unity. Si vous souhaitez intégrer les notifications push ADM, créez un fichier appelé `api_key.txt` contenant votre clé API ADM et placez-le dans le dossier `Plugins/Android/assets/`. Pour plus d'informations sur l'intégration d'ADM avec Braze, consultez nos [instructions d'intégration des notifications push ADM]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity).

### Extension du lecteur Braze Unity (Android uniquement) {#extend-unity-player}

L'exemple de fichier `AndroidManifest.xml` fourni contient une classe Activity enregistrée, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Cette classe est intégrée au SDK Braze et étend `UnityPlayerActivity` avec la gestion des sessions, l'enregistrement des messages in-app, la journalisation analytique des notifications push, et bien plus encore. Consultez [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) pour plus d'informations sur l'extension de la classe `UnityPlayerActivity`.

Si vous créez votre propre `UnityPlayerActivity` personnalisée dans un projet de bibliothèque ou de plug-in, vous devrez étendre notre `BrazeUnityPlayerActivity` pour intégrer votre fonctionnalité personnalisée avec Braze. Avant de commencer à étendre `BrazeUnityPlayerActivity`, suivez nos instructions pour intégrer Braze dans votre projet Unity.

1. Ajoutez le SDK Android de Braze en tant que dépendance à votre projet de bibliothèque ou de plug-in, comme décrit dans les [instructions d'intégration du SDK Android de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
2. Intégrez notre `.aar` Unity, qui contient nos fonctionnalités spécifiques à Unity, dans votre projet de bibliothèque Android que vous développez pour Unity. Le fichier `appboy-unity.aar` est disponible dans notre [dépôt public](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). Une fois notre bibliothèque Unity intégrée avec succès, modifiez votre `UnityPlayerActivity` pour étendre `BrazeUnityPlayerActivity`.
3. Exportez votre projet de bibliothèque ou de plug-in et déposez-le dans `/<your-project>/Assets/Plugins/Android` comme d'habitude. N'incluez pas de code source Braze dans votre bibliothèque ou votre plug-in, car il sera déjà présent dans `/<your-project>/Assets/Plugins/Android`.
4. Modifiez votre `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` pour spécifier votre sous-classe de `BrazeUnityPlayerActivity` comme activité principale.

Vous devriez maintenant pouvoir générer un `.apk` depuis l'IDE Unity qui est entièrement intégré à Braze et contient votre fonctionnalité `UnityPlayerActivity` personnalisée.

## Résolution des problèmes {#troubleshooting}

### Erreur : « File could not be read » {#error-file-could-not-be-read}

Les erreurs ressemblant à ce qui suit peuvent être ignorées en toute sécurité. Le logiciel Apple utilise une extension PNG propriétaire appelée CgBI, qu'Unity ne reconnaît pas. Ces erreurs n'affecteront ni votre compilation iOS ni l'affichage correct des images associées dans le bundle Braze.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
