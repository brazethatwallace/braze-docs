---
nav_title: SDK Cordova
article_title: Guide du dépôt du SDK Cordova
page_order: 5
description: "Référence du README du SDK Braze Cordova, reproduite depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## À propos du SDK Braze Cordova {#about-the-braze-cordova-sdk}

Le SDK Braze Cordova vous aide à intégrer les fonctionnalités d'envoi de messages, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide de l'utilisateur Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guide du développeur Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Versions minimales requises {#minimum-version-requirements}

| Plugin Braze | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Versions minimales requises" }

Ce SDK hérite également des exigences de ses SDK natifs Braze sous-jacents. Veillez à respecter les listes ci-dessous :
* [Exigences du SDK Android](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [Exigences du SDK Swift](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## Installation du SDK {#installing-the-sdk}
{% alert warning %}
Ajoutez le SDK Braze Cordova uniquement en utilisant les méthodes ci-dessous. N'essayez pas de l'installer par d'autres moyens, car cela pourrait entraîner une faille de sécurité.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## Exécution de l'application exemple {#running-the-sample-application}
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les projets exemples, consultez [https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk).