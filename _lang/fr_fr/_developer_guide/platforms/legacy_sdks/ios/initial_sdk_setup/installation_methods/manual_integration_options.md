---
nav_title: Manuel
article_title: Options d'intégration manuelle pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre comment intégrer manuellement le SDK Braze pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration manuelle {#manual-integration}

{% alert tip %}
Nous vous recommandons vivement d'implémenter le SDK via un gestionnaire de paquets tel que le [gestionnaire de paquets Swift](../swift_package_manager/), [CocoaPods](../cocoapods/) ou [Carthage](../carthage_integration/). Cela vous fera gagner beaucoup de temps et automatisera une grande partie du processus. Cependant, si vous n'êtes pas en mesure de le faire, vous pouvez effectuer l'intégration manuellement en suivant les instructions ci-dessous.
{% endalert %}

## Étape 1 : Téléchargement du SDK Braze {#step-1-downloading-the-braze-sdk}

### Option 1 : XCFramework dynamique {#option-1-dynamic-xcframework}

1. Téléchargez `Appboy_iOS_SDK.xcframework.zip` depuis la [page de publication](https://github.com/appboy/appboy-ios-sdk/releases) et extrayez le fichier.
2. Dans Xcode, faites glisser et déposez ce `.xcframework` dans votre projet.
3. Sous l'onglet **General** du projet, sélectionnez **Embed & Sign** pour `Appboy_iOS_SDK.xcframework`.

### Option 2 : XCFramework statique pour l'intégration statique {#option-2-static-xcframework-for-static-integration}

1. Téléchargez `Appboy_iOS_SDK.zip` depuis la [page de publication](https://github.com/appboy/appboy-ios-sdk/releases).<br><br>
2. Dans Xcode, depuis le navigateur de projet, sélectionnez le projet ou le groupe de destination pour Braze.<br><br>
3. Naviguez vers **File > Add Files > Project_Name**.<br><br>
4. Ajoutez les dossiers `AppboyKit` et `AppboyUI` à votre projet en tant que groupe.
	- Assurez-vous que l'option **Copy items into destination group's folder** est sélectionnée si vous effectuez l'intégration pour la première fois. Développez **Options** dans le sélecteur de fichiers pour sélectionner **Copy items if needed** et **Create groups**.
	- Supprimez les répertoires `AppboyKit/include` et `AppboyUI/include`.<br><br>
5. (Facultatif) Si l'un des cas suivants s'applique à vous :
  - Vous souhaitez uniquement les fonctionnalités d'analyse de base du SDK et n'utilisez aucune fonctionnalité d'interface utilisateur (par exemple, les messages in-app ou les Content Cards).
  - Vous disposez d'une interface utilisateur personnalisée pour les fonctionnalités de l'interface Braze et gérez vous-même le téléchargement des images.<br><br>Vous pouvez utiliser la version principale du SDK en supprimant le fichier `ABKSDWebImageProxy.m` et `Appboy.bundle`. Cela supprimera la dépendance au framework `SDWebImage` ainsi que toutes les ressources liées à l'interface utilisateur (par exemple, les fichiers Nib, les images, les fichiers de localisation) du SDK.

{% alert warning %}
Si vous essayez d'utiliser la version principale du SDK sans les fonctionnalités d'interface de Braze, les messages in-app ne s'afficheront pas. Tenter d'afficher l'interface Content Cards de Braze avec la version principale entraînera un comportement imprévisible.
{% endalert %}

## Étape 2 : Ajout des bibliothèques iOS requises {#step-2-adding-required-ios-libraries}

1. Cliquez sur la cible de votre projet (en utilisant la navigation de gauche) et sélectionnez l'onglet **Build Phases**.<br><br>
2. Cliquez sur le bouton <i class="fas fa-plus"></i> sous **Link Binary With Libraries**.<br><br>
3. Dans le menu, sélectionnez `SystemConfiguration.framework`.<br><br>
4. Marquez cette bibliothèque comme requise à l'aide du menu déroulant à côté de `SystemConfiguration.framework`.<br><br>
5. Répétez l'opération pour ajouter chacun des frameworks requis suivants à votre projet, en les marquant comme « required ».
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. Ajoutez les frameworks suivants et marquez-les comme facultatifs :
	- `CoreTelephony.framework`<br><br>
7. Sélectionnez l'onglet **Build Settings**. Dans la section **Linking**, localisez le paramètre **Other Linker Flags** et ajoutez le drapeau `-ObjC`.<br><br>
8. Le framework `SDWebImage` est nécessaire pour que les Content Cards et les messages in-app fonctionnent correctement. `SDWebImage` est utilisé pour le téléchargement et l'affichage des images, y compris les GIF. Si vous avez l'intention d'utiliser les Content Cards ou les messages in-app, suivez les étapes d'intégration de SDWebImage.

### Intégration de SDWebImage {#sdwebimage-integration}

Pour installer `SDWebImage`, suivez leurs [instructions](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework), puis faites glisser et déposez le `XCFramework` résultant dans votre projet.

### Suivi facultatif de la localisation {#optional-location-tracking}

1. Ajoutez le `CoreLocation.framework` pour activer le suivi de la localisation.
2. Vous devez autoriser la localisation pour vos utilisateurs à l'aide de `CLLocationManager` dans votre application.

## Étape 3 : En-tête de pont Objective-C {#step-3-objective-c-bridging-header}

{% alert note %}
Si votre projet utilise uniquement Objective-C, ignorez cette étape.
{% endalert %}

Si votre projet utilise Swift, vous aurez besoin d'un fichier d'en-tête de pont.

Si vous n'avez pas de fichier d'en-tête de pont, créez-en un et nommez-le `your-product-module-name-Bridging-Header.h` en choisissant **File > New > File > (iOS ou OS X) > Source > Header File**. Ajoutez ensuite la ligne de code suivante en haut de votre fichier d'en-tête de pont :
```
#import "AppboyKit.h"
```

Dans les **Build Settings** de votre projet, ajoutez le chemin relatif de votre fichier d'en-tête au paramètre de compilation `Objective-C Bridging Header` sous `Swift Compiler - Code Generation`.

## Étapes suivantes {#next-steps}

Suivez les instructions pour [terminer l'intégration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).