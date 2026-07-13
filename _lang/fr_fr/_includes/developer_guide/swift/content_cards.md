## Conditions préalables {#prerequisites}

Avant de pouvoir utiliser les Content Cards, vous devez intégrer le [SDK Swift de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) dans votre application. Cependant, aucune configuration supplémentaire n'est nécessaire.

## Contextes du contrôleur de vue {#view-controller-contexts}

L'interface utilisateur par défaut des Content Cards peut être intégrée à partir de la bibliothèque `BrazeUI` du SDK Braze. Créez le contrôleur de vue des Content Cards en utilisant l'instance `braze`. Si vous souhaitez intercepter le cycle de vie de l'interface utilisateur des Content Cards et y réagir, implémentez [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) en tant que délégué pour votre `BrazeContentCardUI.ViewController`.

{% alert note %}
Pour plus d'informations sur les options du contrôleur de vue iOS, reportez-vous à la [documentation du développeur Apple](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

La bibliothèque `BrazeUI` du SDK Swift propose deux contextes de contrôleur de vue par défaut : [navigation](#swift_navigation) ou [modale](#swift_modal). Cela signifie que vous pouvez intégrer les Content Cards dans ces contextes en ajoutant quelques lignes de code à votre application ou site. Les deux vues offrent des options de personnalisation et de style décrites dans le [guide de personnalisation]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). Vous pouvez également créer un contrôleur de vue de Content Cards personnalisé au lieu d'utiliser le contrôleur standard de Braze pour bénéficier d'encore plus d'options de personnalisation — reportez-vous au [tutoriel sur l'interface utilisateur des Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) pour voir un exemple.

{% alert important %}
Pour gérer la variante de contrôle des Content Cards dans votre interface utilisateur personnalisée, transmettez votre objet [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)), puis appelez la méthode `logImpression` comme vous le feriez avec n'importe quel autre type de Content Card. L'objet enregistrera implicitement une impression de contrôle pour informer notre analytique du moment où un utilisateur aurait vu la carte de contrôle.
{% endalert %}

### Navigation {#swift_navigation}

Un contrôleur de navigation est un contrôleur de vue qui gère un ou plusieurs contrôleurs de vue enfants dans une interface de navigation. Voici un exemple d'ajout d'une instance de `BrazeContentCardUI.ViewController` dans un contrôleur de navigation :

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

### Modale {#swift_modal}

Utilisez les présentations modales pour créer des interruptions temporaires dans le flux de travail de votre application, par exemple en demandant à l'utilisateur de fournir des informations importantes. Cette vue comporte une barre de navigation en haut et un bouton **Done** sur le côté de la barre. Voici un exemple d'insertion d'une instance de `BrazeContentCard.ViewController` dans un contrôleur modal :

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Pour un exemple d'utilisation des contrôleurs de vue `BrazeUI`, consultez les exemples d'interface utilisateur des Content Cards correspondants dans notre [application Exemples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Modèle de carte de base {#base-card-model}

Le modèle de données des Content Cards est disponible dans le module `BrazeKit` du SDK Swift de Braze. Ce module contient les types de Content Cards suivants, qui sont une implémentation du type `Braze.ContentCard`. Pour une liste complète des propriétés des Content Cards et de leur utilisation, voir la [classe `ContentCard`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

- Image uniquement
- Image avec légende
- Classique
- Image classique
- Contrôle

Pour accéder au modèle de données des Content Cards, appelez `contentCards.cards` sur votre instance `braze`. Voir [Enregistrer les analyses]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) pour plus d'informations sur l'abonnement aux données de cartes.

{% alert note %}
La lecture de `contentCards.cards`, `contentCards.unviewedCards` ou `contentCards.lastUpdate` bloque le thread appelant jusqu'à ce que le SDK ait terminé ses opérations post-initialisation. Pour les contextes sur le thread principal ou sensibles à la latence, utilisez plutôt les alternatives non bloquantes [`getCachedContentCards(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getcachedcontentcards(_:)), [`getUnviewedCards(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getunviewedcards(_:)) ou [`getLastUpdate(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getlastupdate(_:)).
{% endalert %}

{% alert note %}
N'oubliez pas que `BrazeKit` propose une classe alternative [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) pour la compatibilité avec Objective-C.
{% endalert %}

## Méthodes de carte {#card-methods}

Chaque carte est initialisée avec un objet `Context`, qui contient diverses méthodes pour gérer l'état de votre carte. Appelez ces méthodes lorsque vous souhaitez modifier la propriété d'état correspondante d'un objet de carte particulier.

| Méthode | Description |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()` | Enregistre l'événement d'impression de la Content Card. |
| `card.context?.logClick()` | Enregistre l'événement de clic sur la Content Card. |
| `card.context?.processClickAction()` | Traite une entrée [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) donnée. |
| `card.context?.logDismissed()` | Enregistre l'événement de rejet de la Content Card. |
| `card.context?.logError()` | Enregistre une erreur liée à la Content Card. |
| `card.context?.loadImage()` | Charge une image de Content Card à partir d'une URL. Cette méthode peut être nulle si la Content Card n'a pas d'image. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Méthodes de carte" }

Pour plus de détails, reportez-vous à la [documentation de la classe `Context`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)