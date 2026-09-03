---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Cette page couvre les étapes de configuration initiales du SDK Braze pour tvOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuration initiale du SDK {#initial-sdk-setup}

> Cet article de référence explique comment installer le SDK Braze pour tvOS. L'installation du SDK Braze vous fournira des fonctionnalités d'analyse de base.

{% alert note %}
Notre SDK tvOS prend actuellement en charge la fonctionnalité d'analyse. Pour ajouter une application tvOS dans votre tableau de bord, ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

Le SDK Braze pour tvOS doit être installé ou mis à jour à l'aide de [CocoaPods](http://cocoapods.org/), un gestionnaire de dépendances pour les projets Objective-C et Swift. CocoaPods offre une simplicité supplémentaire pour l'intégration et la mise à jour.

## Intégration du SDK tvOS avec CocoaPods

### Étape 1 : Installer CocoaPods

L'installation du SDK via [CocoaPods](http://cocoapods.org/) pour tvOS automatise la majeure partie du processus d'installation. Avant de commencer, assurez-vous d'utiliser [Ruby version 2.0.0](https://www.ruby-lang.org/en/installation/) ou ultérieure.

Exécutez la commande suivante pour démarrer :

```bash
$ sudo gem install cocoapods
```

- Si vous êtes invité à écraser l'exécutable `rake`, consultez la section [Getting started](http://guides.cocoapods.org/using/getting-started.html) sur CocoaPods.org pour plus de détails.
- Si vous rencontrez des problèmes avec CocoaPods, consultez le [guide de résolution des problèmes CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Étape 2 : Créer le Podfile

Maintenant que vous avez installé le Ruby Gem CocoaPods, vous devez créer un fichier nommé `Podfile` dans le répertoire de votre projet Xcode.

Ajoutez la ligne suivante à votre Podfile :

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Nous vous recommandons de versionner Braze afin que les mises à jour du pod récupèrent automatiquement tout ce qui est inférieur à une mise à jour de version mineure. Cela ressemble à `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Si vous souhaitez intégrer automatiquement la dernière version du SDK Braze, même avec des changements majeurs, vous pouvez utiliser `pod 'Appboy-tvOS-SDK'` dans votre Podfile.

### Étape 3 : Installer le SDK Braze

Pour installer le SDK Braze via CocoaPods, accédez au répertoire de votre projet d'application Xcode dans votre terminal et exécutez la commande suivante :
```
pod install
```

À ce stade, vous devriez pouvoir ouvrir le nouvel espace de travail Xcode créé par CocoaPods. Assurez-vous d'utiliser cet espace de travail Xcode plutôt que votre projet Xcode.

![À ce stade, vous devriez pouvoir ouvrir le nouvel espace de travail Xcode créé par CocoaPods. Assurez-vous d'utiliser cet espace de travail Xcode plutôt que votre projet Xcode.]({% image_buster /assets/img_archive/podsworkspace.png %})

### Étape 4 : Mettre à jour le délégué de votre application

{% tabs %}
{% tab OBJECTIVE-C %}

Ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

Dans votre fichier `AppDelegate.m`, ajoutez l'extrait de code suivant dans votre méthode `application:didFinishLaunchingWithOptions` :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Enfin, mettez à jour `YOUR-API-KEY` avec la valeur correcte depuis votre page **Gérer les paramètres**.

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec CocoaPods ou Carthage, ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` :

```swift
import AppboyTVOSKit
```

Pour plus d'informations sur l'utilisation de code Objective-C dans des projets Swift, consultez la [documentation Apple Developer](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Dans `AppDelegate.swift`, ajoutez l'extrait de code suivant à votre méthode `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Ensuite, mettez à jour `YOUR-API-KEY` avec la valeur correcte depuis votre page **Gérer les paramètres**.

Le singleton `sharedInstance` sera nil tant que `startWithApiKey:` n'aura pas été appelé, car il s'agit d'un prérequis pour utiliser toute fonctionnalité Braze.

{% endtab %}
{% endtabs %}

{% alert warning %}
Assurez-vous d'initialiser Braze dans le thread principal de votre application. L'initialisation asynchrone peut entraîner des dysfonctionnements.
{% endalert %}

### Étape 5 : Spécifier votre endpoint personnalisé ou cluster de données

{% alert note %}
Depuis décembre 2019, les endpoints personnalisés ne sont plus distribués. Si vous disposez d'un endpoint personnalisé préexistant, vous pouvez continuer à l'utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics#endpoints">liste des endpoints disponibles</a>.
{% endalert %}

Votre conseiller Braze devrait déjà vous avoir indiqué le [bon endpoint]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuration de l'endpoint à la compilation (recommandé)
Si vous disposez d'un endpoint personnalisé préexistant :
- À partir de la version 3.0.2 du SDK iOS de Braze, vous pouvez définir un endpoint personnalisé à l'aide du fichier `Info.plist`. Ajoutez le dictionnaire `Appboy` à votre fichier Info.plist. À l'intérieur du dictionnaire `Appboy`, ajoutez la sous-entrée de type chaîne de caractères `Endpoint` et définissez la valeur sur l'autorité de l'URL de votre endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, et non `https://sdk.iad-01.braze.com`).

#### Configuration de l'endpoint à l'exécution
Si vous disposez d'un endpoint personnalisé préexistant :
- À partir de la version 3.17.0+ du SDK iOS de Braze, vous pouvez remplacer votre endpoint via `ABKEndpointKey` dans le paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la valeur sur l'autorité de l'URL de votre endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, et non `https://sdk.iad-01.braze.com`).

{% alert note %}
La prise en charge de la configuration des endpoints à l'exécution via `ABKAppboyEndpointDelegate` a été supprimée dans la version 3.17.0 du SDK iOS de Braze. Si vous utilisez déjà `ABKAppboyEndpointDelegate`, notez que dans les versions 3.14.1 à 3.16.0 du SDK iOS de Braze, toute référence à `dev.appboy.com` dans votre méthode `getApiEndpoint()` doit être remplacée par une référence à `sdk.iad-01.braze.com`.
{% endalert %}

### Intégration SDK terminée

Braze devrait maintenant collecter des données depuis votre application, et votre intégration de base devrait être terminée. Notez que lors de la compilation de votre application tvOS et de toute autre bibliothèque tierce, le Bitcode doit être activé.

### Mettre à jour le SDK Braze via CocoaPods

Pour mettre à jour un CocoaPod, exécutez simplement les commandes suivantes dans le répertoire de votre projet :

```
pod update
```

## Personnaliser Braze au démarrage

Si vous souhaitez personnaliser Braze au démarrage, vous pouvez utiliser la méthode d'initialisation de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` et transmettre un `NSDictionary` facultatif de clés de démarrage Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

Dans votre fichier `AppDelegate.m`, au sein de votre méthode `application:didFinishLaunchingWithOptions`, ajoutez la méthode Braze suivante :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Dans `AppDelegate.swift`, au sein de votre méthode `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, ajoutez la méthode Braze suivante :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

où `appboyOptions` est un `Dictionary` de valeurs de configuration au démarrage.

{% endtab %}
{% endtabs %}

Cette méthode remplace la méthode d'initialisation `startWithApiKey:inApplication:withLaunchOptions:` et est appelée avec les paramètres suivants :

- `YOUR-API-KEY` : La clé API de votre application se trouve sous **Gérer les paramètres** dans le tableau de bord de Braze.
- `application` : L'application actuelle.
- `launchOptions` : Le `NSDictionary` d'options que vous obtenez depuis `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` : Un `NSDictionary` facultatif contenant les valeurs de configuration au démarrage pour Braze.

Consultez [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) pour obtenir la liste des clés de démarrage de Braze.

## Appboy.sharedInstance() et la nullabilité en Swift
Contrairement à la pratique courante, le singleton `Appboy.sharedInstance()` est optionnel. En effet, `sharedInstance` est `nil` avant l'appel de `startWithApiKey:`, et il existe certaines implémentations non standard, mais valides, dans lesquelles une initialisation différée peut être utilisée.

Si vous appelez `startWithApiKey:` dans votre délégué `didFinishLaunchingWithOptions:` avant tout accès au `sharedInstance` d'Appboy (l'implémentation standard), vous pouvez utiliser le chaînage optionnel, comme `Appboy.sharedInstance()?.changeUser("testUser")`, pour éviter des vérifications fastidieuses. Cela offrira une parité avec une implémentation en Objective-C qui supposait un `sharedInstance` non nul.

Vous pouvez également intégrer notre SDK tvOS manuellement : récupérez simplement le framework depuis notre [dépôt public](https://github.com/appboy/appboy-ios-sdk) et initialisez Braze comme décrit dans les sections précédentes.

## Identifier les utilisateurs et générer des rapports d'analyse
Consultez notre [documentation iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift) pour obtenir des informations sur la définition des ID utilisateur, l'enregistrement d'événements personnalisés et la définition des attributs utilisateur. Nous vous recommandons également de vous familiariser avec nos [conventions de dénomination des événements]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).