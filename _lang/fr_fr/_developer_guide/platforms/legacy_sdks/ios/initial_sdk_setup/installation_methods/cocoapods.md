---
nav_title: CocoaPods
article_title: Intégration de CocoaPods pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence montre comment intégrer le SDK Braze à l'aide de CocoaPods pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration de CocoaPods {#cocoapods-integration}

## Étape 1 : Installer CocoaPods {#step-1-install-cocoapods}

L'installation du SDK iOS via [CocoaPods](http://cocoapods.org/) automatise la majeure partie du processus d'installation à votre place. Avant de lancer ce processus, assurez-vous d'utiliser [Ruby 2.0.0](https://www.ruby-lang.org/en/installation/) ou une version ultérieure. Ne vous inquiétez pas, il n'est pas nécessaire de connaître la syntaxe Ruby pour installer ce SDK.

Exécutez la commande suivante pour démarrer :

```bash
$ sudo gem install cocoapods
```

Si vous rencontrez des problèmes avec CocoaPods, consultez le [guide de résolution des problèmes](http://guides.cocoapods.org/using/troubleshooting.html) de CocoaPods.

{% alert note %}
Si vous êtes invité à écraser l'exécutable `rake`, consultez les instructions de [démarrage](http://guides.cocoapods.org/using/getting-started.html) sur CocoaPods.org pour plus de détails.
{% endalert %}

## Étape 2 : Construire le Podfile {#step-2-constructing-the-podfile}

Maintenant que vous avez installé le CocoaPods Ruby Gem, vous devez créer un fichier dans votre répertoire de projet Xcode nommé `Podfile`.

Ajoutez la ligne suivante à votre Podfile :

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

Nous vous suggérons de versionner Braze afin que les mises à jour du pod récupèrent automatiquement tout ce qui est inférieur à une mise à jour mineure de version. Cela ressemble à `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build`. Si vous souhaitez intégrer automatiquement la dernière version du SDK Braze, même avec des modifications majeures, vous pouvez utiliser `pod 'Appboy-iOS-SDK'` dans votre Podfile.

#### Sous-spécifications {#subspecs}

Nous recommandons aux intégrateurs d'importer notre SDK complet. Cependant, si vous êtes certain de n'intégrer qu'une fonctionnalité Braze spécifique, vous pouvez importer uniquement la sous-spécification d'interface utilisateur souhaitée plutôt que le SDK complet.

| Sous-spécification | Détails |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | La sous-spécification `InAppMessage` contient l'interface utilisateur des messages in-app de Braze et le SDK Core. |
| `pod 'Appboy-iOS-SDK/ContentCards'` | La sous-spécification `ContentCards` contient l'interface utilisateur des Content Cards de Braze et le SDK Core. |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | La sous-spécification `NewsFeed` contient le SDK Core de Braze. |
| `pod 'Appboy-iOS-SDK/Core'` | La sous-spécification `Core` prend en charge l'analytique, comme les événements personnalisés et les attributs. |
{: .ws-td-nw-1 aria-label="Subspecs" }

## Étape 3 : Installer le SDK Braze {#step-3-installing-the-braze-sdk}

Pour installer le SDK Braze via CocoaPods, accédez au répertoire de votre projet d'application Xcode dans votre terminal et exécutez la commande suivante :
```
pod install
```

À ce stade, vous devriez pouvoir ouvrir le nouvel espace de travail du projet Xcode créé par CocoaPods. Assurez-vous d'utiliser cet espace de travail Xcode au lieu de votre projet Xcode.

![Un dossier d'exemple Appboy déplié pour afficher le nouveau fichier AppbpyExample.workspace.]({% image_buster /assets/img_archive/podsworkspace.png %})

## Étapes suivantes {#next-steps}

Suivez les instructions pour [terminer l'intégration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).

## Mettre à jour le SDK Braze via CocoaPods {#updating-the-braze-sdk-via-cocoapods}

Pour mettre à jour un CocoaPod, il vous suffit d'exécuter la commande suivante dans votre répertoire de projet :

```
pod update
```

