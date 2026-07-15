---
nav_title: Tests unitaires (facultatif)
article_title: Tests unitaires de notification push pour iOS
platform: iOS
page_order: 29.5
description: "Cet article de référence décrit comment implémenter des tests unitaires facultatifs pour votre implémentation de notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Tests unitaires {#unit-tests}

Ce guide facultatif décrit comment mettre en œuvre quelques tests unitaires qui vérifieront si votre app delegate suit correctement les étapes décrites dans nos [instructions d'intégration push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration).

Si tous les tests sont réussis, cela signifie généralement que la partie basée sur le code de votre configuration push est fonctionnelle. Si un test échoue, cela peut signifier que vous n'avez pas suivi correctement une étape, ou cela peut résulter d'une personnalisation valide qui ne correspond pas précisément à nos instructions par défaut.

Dans tous les cas, cette approche peut être utile pour vérifier que vous avez suivi les étapes d'intégration et pour surveiller d'éventuelles régressions.

## Étape 1 : Créer une cible de tests unitaires {#step-1-creating-a-unit-tests-target}

Ignorez cette étape si votre projet d'application dans Xcode contient déjà un lot de tests unitaires.

Dans votre projet d'application, sélectionnez **File > New > Target** et ajoutez un nouveau « Unit Testing Bundle ». Ce lot peut utiliser Objective-C ou Swift et peut porter n'importe quel nom. Définissez la « Target to be Tested » vers la cible de votre application principale.

## Étape 2 : Ajouter le SDK Braze à vos tests unitaires {#step-2-add-the-braze-sdk-to-your-unit-tests}

En utilisant la même méthode que celle utilisée initialement pour [installer le SDK Braze]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview), assurez-vous que la même installation du SDK est également disponible pour votre cible de tests unitaires. Par exemple, en utilisant CocoaPods :

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Étape 3 : Ajouter OCMock à vos tests unitaires {#step-3-add-ocmock-to-your-unit-tests}

Ajoutez [OCMock](https://ocmock.org/) à votre cible de test via CocoaPods, Carthage ou sa bibliothèque statique. Par exemple, en utilisant CocoaPods :

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## Étape 4 : Terminer l'installation des bibliothèques ajoutées {#step-4-finish-installing-the-added-libraries}

Terminez l'installation du SDK Braze et d'OCMock. Par exemple, en utilisant CocoaPods, naviguez dans le répertoire de votre projet d'application Xcode dans votre terminal et exécutez la commande suivante :

```
pod install
```

À ce stade, vous devriez pouvoir ouvrir l'espace de travail du projet Xcode créé par CocoaPods.

## Étape 5 : Ajouter des tests push {#step-5-adding-push-tests}

Créez un nouveau fichier Objective-C dans votre cible de tests unitaires.

Si la cible des tests unitaires est en Swift, Xcode peut demander : « Would you like to configure an Objective-C bridging header? » L'en-tête de pontage étant facultatif, vous pouvez cliquer sur **Don't Create** et exécuter ces tests unitaires avec succès.

Ajoutez le contenu du fichier [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) de l'exemple d'application HelloSwift au nouveau fichier.

## Étape 6 : Exécuter la suite de tests {#step-6-run-test-suite}

Exécutez les tests unitaires de votre application. Il peut s'agir d'une étape de vérification unique, ou vous pouvez l'inclure indéfiniment dans votre suite de tests pour vous aider à détecter toute régression.