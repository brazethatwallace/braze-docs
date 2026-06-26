---
nav_title: SDK Android
article_title: Guide du dépôt du SDK Android
page_order: 2
description: "Référence du README du SDK Android de Braze, reproduite depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## À propos du SDK Android de Braze {#about-the-braze-android-sdk}

Le SDK Android de Braze vous aide à intégrer les fonctionnalités d'envoi de messages, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide utilisateur de Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guide développeur de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)

## Démarrage rapide {#quickstart}

Les extraits de code suivants montrent la configuration minimale requise pour ajouter le SDK Android de Braze à votre application.

``` groovy
// build.gradle

// ...
repositories {
  mavenCentral()
}
// ...
dependencies {
  `implementation 'com.braze:android-sdk-ui:42.3.+'`
  `implementation 'com.braze:android-sdk-location:42.3.+'`
}
// ...
```

``` xml
<!-- res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` kotlin
Braze.getInstance(context).changeUser("Jane Doe");
```

Pour plus d'informations sur les options d'intégration avancées, consultez le [Guide développeur de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

## Prise en charge des versions {#version-support}

{% alert important %}
Le SDK Android de Braze déclare un `minSdkVersion` de API 21+, ce qui permet au SDK de se compiler dans des applications prenant en charge dès l'API 21. Bien que le SDK se compile pour ces versions, Braze ne fournit pas de support officiel pour les versions d'API inférieures à 25, et le SDK peut ne pas fonctionner comme prévu sur les appareils exécutant ces versions.

Si votre application prend en charge ces versions, procédez comme suit :

- Vérifiez que votre intégration du SDK fonctionne comme prévu sur des appareils physiques (pas uniquement des émulateurs) pour ces versions d'API.
- Si vous ne pouvez pas valider le comportement attendu, vous devez soit appeler [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html), soit ne pas initialiser le SDK sur ces versions. Sinon, vous risquez de provoquer des effets secondaires indésirables ou une dégradation des performances sur les appareils de vos utilisateurs.
{% endalert %}
Le tableau suivant répertorie les versions minimales prises en charge pour les outils utilisés par le SDK Android de Braze.

Outil | Version minimale prise en charge
:----|:----
minSdk|5.0+ / API 21+ (Lollipop et versions ultérieures)
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|24.1.2
Font Awesome|4.3.0

## Modules {#modules}

Le tableau suivant décrit chaque module du SDK Android de Braze.

Module | Description
:----|:----
`android-sdk-base`|La bibliothèque d'analyse de base du SDK Braze.
`android-sdk-ui`|La bibliothèque d'interface utilisateur du SDK Braze pour les messages in-app, les notifications push, les Content Cards et les bannières.
`android-sdk-location`|La bibliothèque de localisation du SDK Braze pour la localisation et le géorepérage.
`android-sdk-jetpack-compose`|La bibliothèque du SDK Braze pour la prise en charge de Jetpack Compose.
`droidboy`|Un exemple d'application qui montre comment utiliser Braze en profondeur.
`android-sdk-unity`|Une bibliothèque qui permet les intégrations du SDK Braze sur Unity.
`samples`|Un dossier contenant des exemples d'applications pour diverses options d'intégration.

## Contact {#contact}

Pour toute question, contactez l'assistance technique de Braze.
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les exemples de projets, consultez [https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk).