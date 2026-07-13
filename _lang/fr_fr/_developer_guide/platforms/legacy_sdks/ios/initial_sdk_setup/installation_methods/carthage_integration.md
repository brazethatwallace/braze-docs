---
nav_title: Carthage
article_title: Intégration de Carthage pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence montre comment intégrer le SDK Braze à l'aide de Carthage pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration de Carthage {#carthage-integration}

## Importer le SDK {#import-the-sdk}

À partir de la version `4.4.0`, le SDK Braze prend en charge les XCFrameworks lors de l'intégration via Carthage. Pour importer le SDK complet, incluez ces lignes dans votre `Cartfile` :
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Consultez le [guide de démarrage rapide de Carthage](https://github.com/Carthage/Carthage#quick-start) pour plus d'instructions sur l'importation du SDK.

Lors de la migration à partir d'une version antérieure à `4.4.0`, suivez le [guide de migration de Carthage pour les XCFrameworks](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks).

{% alert note %}
Pour plus de détails sur la syntaxe du `Cartfile` ou sur des fonctionnalités telles que le verrouillage de version, consultez la [documentation de Carthage](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile).
Pour l'utilisation de Carthage spécifique à une plateforme, consultez leur [guide de l'utilisateur](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
{% endalert %}

### Versions précédentes {#previous-versions}

Pour les versions `3.24.0` à `4.3.4`, incluez les éléments suivants dans votre `Cartfile` :
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

Pour importer des versions antérieures à `3.24.0`, incluez les éléments suivants dans votre `Cartfile` :
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Assurez-vous de remplacer `<BRAZE_IOS_SDK_VERSION>` par la [version appropriée](https://github.com/Appboy/appboy-ios-sdk/releases) du SDK iOS de Braze au format « x.y.z ».

## Étapes suivantes {#next-steps}

Suivez les instructions pour [finaliser l'intégration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).

## Intégration Core uniquement {#core-only-integration}

Si vous souhaitez utiliser le SDK Core sans composants d'interface utilisateur ni dépendances, installez la version Core du framework Carthage de Braze en incluant la ligne suivante dans votre `Cartfile` :

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

