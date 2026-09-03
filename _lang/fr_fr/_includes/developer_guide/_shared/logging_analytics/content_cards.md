> Lors de la création d'une interface utilisateur personnalisée pour les Content Cards, vous devez enregistrer manuellement les données analytiques telles que les impressions, les clics et les rejets, car cela n'est géré automatiquement que pour les modèles de cartes par défaut. L'enregistrement de ces événements fait partie intégrante de l'intégration des Content Cards et est essentiel pour garantir l'exactitude des rapports et de la facturation des Campaigns. Pour ce faire, alimentez votre interface utilisateur personnalisée avec les données provenant des modèles de données Braze, puis enregistrez manuellement les événements. Une fois que vous avez compris comment enregistrer les analyses, vous pouvez découvrir les façons courantes dont les clients de Braze [créent des Content Cards personnalisées]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Enregistrement des données analytiques {#logging-analytics}

Lors du déploiement de vos Content Cards personnalisées, vous pouvez analyser les objets Content Card et extraire les données de leur payload, telles que `title`, `cardDescription` et `imageUrl`. Vous pouvez ensuite utiliser les données du modèle obtenu pour alimenter votre interface utilisateur personnalisée.

Pour obtenir les modèles de données des Content Cards, abonnez-vous aux mises à jour des Content Cards. Deux propriétés méritent une attention particulière :

* **`id`** : Représente la chaîne d'identifiant de la Content Card. Il s'agit de l'identifiant unique utilisé pour enregistrer les données analytiques des Content Cards personnalisées.
* **`extras`** : Englobe toutes les paires clé-valeur du tableau de bord de Braze.

Toutes les propriétés en dehors de `id` et `extras` sont facultatives à analyser pour les Content Cards personnalisées. Pour plus d'informations sur le modèle de données, consultez l'article d'intégration de chaque plateforme : [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab web %}

Enregistrez une fonction de rappel pour vous abonner aux mises à jour lorsque les cartes sont actualisées.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Les Content Cards ne s'actualisent au démarrage de la session que si une demande d'abonnement est appelée avant `openSession()`. Vous pouvez également choisir d'[actualiser manuellement le flux]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) à tout moment.
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### Étape 1 : Créer une variable d'abonnement privée {#step-1-create-a-private-subscriber-variable}

Pour vous abonner aux mises à jour des cartes, déclarez d'abord une variable privée dans votre classe personnalisée pour contenir votre abonné :

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Étape 2 : S'abonner aux mises à jour {#step-2-subscribe-to-updates}

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour des Content Cards depuis Braze, généralement dans la méthode `Activity.onCreate()` de votre activité Content Cards personnalisée :

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

### Étape 3 : Se désabonner {#step-3-unsubscribe}

Nous recommandons également de vous désabonner lorsque votre activité personnalisée n'est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Étape 1 : Créer une variable d'abonnement privée

Pour vous abonner aux mises à jour des cartes, déclarez d'abord une variable privée dans votre classe personnalisée pour contenir votre abonné :

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Étape 2 : S'abonner aux mises à jour

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour des Content Cards depuis Braze, généralement dans la méthode `Activity.onCreate()` de votre activité Content Cards personnalisée :

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Étape 3 : Se désabonner

Nous recommandons également de vous désabonner lorsque votre activité personnalisée n'est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Pour accéder au modèle de données des Content Cards, appelez [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) sur votre instance `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

{% alert note %}
La lecture de `contentCards.cards`, `contentCards.unviewedCards` ou `contentCards.lastUpdate` bloque le thread appelant jusqu'à ce que le SDK ait terminé ses opérations post-initialisation. Utilisez les accesseurs non bloquants dans [Accesseurs de snapshot non bloquants](#non-blocking-snapshot-accessors) pour les contextes sur le thread principal ou sensibles à la latence.
{% endalert %}

De plus, vous pouvez également maintenir un abonnement pour observer les changements dans vos Content Cards. Vous pouvez le faire de deux manières :
1. En maintenant un cancellable ; ou
2. En maintenant un `AsyncStream`.

### Cancellable

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

### Accesseurs de snapshot non bloquants {#non-blocking-snapshot-accessors}

Utilisez ces méthodes pour lire l'état mis en cache actuel sans bloquer le thread appelant. Chaque gestionnaire de complétion est toujours livré sur le thread principal.

```swift
// All cached cards.
AppDelegate.braze?.contentCards.getCachedContentCards { cards in
  // Use `cards` here.
}

// Unviewed cards only (excludes control cards).
AppDelegate.braze?.contentCards.getUnviewedCards { cards in
  // Use `cards` here.
}

// Date of the last server sync for the current user (nil until the first sync completes).
AppDelegate.braze?.contentCards.getLastUpdate { date in
  // Use `date` here.
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

De plus, si vous souhaitez maintenir un abonnement à vos Content Cards, vous pouvez appeler [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) :

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

Pour lire l'état mis en cache actuel sans bloquer le thread appelant, utilisez les méthodes suivantes. Chaque gestionnaire de complétion est livré sur le thread principal.

```objc
// All cached cards.
[AppDelegate.braze.contentCards getCachedContentCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Unviewed cards only (excludes control cards).
[AppDelegate.braze.contentCards getUnviewedCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Date of the last server sync for the current user (nil until the first sync completes).
[AppDelegate.braze.contentCards getLastUpdateWithCompletion:^(NSDate * _Nullable date) {
  // Use `date` here.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}

Pour écouter les mises à jour, abonnez-vous aux événements de mise à jour des Content Cards :

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

Pour obtenir les données de Content Cards les plus récemment mises en cache :

```javascript
import Braze from "@braze/react-native-sdk";

const cachedCards = await Braze.getCachedContentCards();
```

Pour demander une actualisation manuelle des Content Cards depuis les serveurs Braze :

```javascript
Braze.requestContentCardsRefresh();
```

{% endtab %}
{% endtabs %}

## Enregistrement des événements {#logging-events}

L'enregistrement d'indicateurs importants tels que les impressions, les clics et les fermetures est rapide et simple. Définissez un écouteur de clic personnalisé pour gérer manuellement ces données analytiques.

{% tabs %}
{% tab web %}

Enregistrez les événements d'impression lorsque les cartes sont consultées par les utilisateurs à l'aide de [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions) :

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Enregistrez les événements de clic sur les cartes lorsque les utilisateurs interagissent avec une carte à l'aide de [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick) :

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

Le [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut référencer les dépendances du SDK Braze telles que la liste de tableaux d'objets Content Card pour obtenir l'objet [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) et appeler les méthodes d'enregistrement de Braze. Utilisez la classe de base `ContentCardable` pour référencer et fournir facilement des données au `BrazeManager`.

Pour enregistrer une impression ou un clic sur une carte, appelez respectivement [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) ou [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html).

Vous pouvez enregistrer manuellement ou marquer une Content Card comme « fermée » dans Braze pour une carte particulière avec [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). Si une carte est déjà marquée comme fermée, elle ne peut pas être marquée comme fermée à nouveau.

Pour créer un écouteur de clic personnalisé, créez une classe qui implémente [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) et enregistrez-la auprès de [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implémentez la méthode [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html), qui sera appelée lorsque l'utilisateur clique sur une Content Card. Ensuite, indiquez à Braze d'utiliser votre écouteur de clic pour les Content Cards.

{% subtabs local %}
{% subtab Java %}

Par exemple :

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

Par exemple :

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Pour gérer les Content Cards de variante de contrôle dans votre interface utilisateur personnalisée, transmettez votre objet [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), puis appelez la méthode `logImpression` comme vous le feriez avec tout autre type de Content Card. L'objet enregistrera implicitement une impression de contrôle pour informer nos analyses du moment où un utilisateur aurait vu la carte de contrôle.
{% endalert %}

{% endtab %}

{% tab swift %}

Implémentez le protocole [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) et définissez votre objet délégué comme propriété `delegate` de votre `BrazeContentCardUI.ViewController`. Ce délégué se chargera de transmettre les données de votre objet personnalisé à Braze pour enregistrement. Pour un exemple, consultez le [tutoriel sur l'interface utilisateur des Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Pour gérer les Content Cards de variante de contrôle dans votre interface utilisateur personnalisée, transmettez votre objet [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)), puis appelez la méthode `logImpression` comme vous le feriez avec tout autre type de Content Card. L'objet enregistrera implicitement une impression de contrôle pour informer nos analyses du moment où un utilisateur aurait vu la carte de contrôle.
{% endalert %}
{% endtab %}

{% tab react native %}

Enregistrez les événements d'impression lorsque les cartes sont consultées par les utilisateurs :

```javascript
Braze.logContentCardImpression(card.id);
```

Enregistrez les événements de clic sur les cartes lorsque les utilisateurs interagissent avec une carte :

```javascript
Braze.logContentCardClicked(card.id);
```

Enregistrez les événements de fermeture lorsqu'un utilisateur ferme une carte :

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## Gestion du comportement au clic {#handling-on-click-behavior}

{% tabs %}
{% tab web %}

Lorsqu'un utilisateur clique sur une Content Card dans un flux personnalisé, le comportement au clic (comme la navigation vers une URL, le deep linking ou l'enregistrement d'un événement personnalisé) n'est pas géré automatiquement. Utilisez [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction) pour traiter l'URL de la carte et exécuter l'action au clic configurée, y compris les actions Braze (URLs `brazeActions://`).

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| Paramètre | Description |
|---|---|
| `url` | Une URL valide, ou une URL d'action Braze valide avec le schéma `brazeActions://`. |
| `openLinkInNewTab` | (Facultatif) Indique si l'URL doit s'ouvrir dans un nouvel onglet. La valeur par défaut est `false`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestion du comportement au clic" }

{% alert important %}
Si vous n'appelez pas `handleBrazeAction()`, les comportements au clic configurés dans le tableau de bord de Braze (tels que « Enregistrer un événement personnalisé » ou « Naviguer vers une URL ») ne s'exécuteront pas pour les cartes affichées dans un flux personnalisé.
{% endalert %}

{% endtab %}
{% tab android %}

Le comportement au clic est géré automatiquement par l'interface utilisateur par défaut des Content Cards. Pour les implémentations personnalisées, utilisez l'interface [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) décrite dans **Enregistrement de l'analytique**.

{% endtab %}
{% tab swift %}

Le comportement au clic est géré automatiquement par l'interface utilisateur par défaut des Content Cards. Pour les implémentations personnalisées, utilisez le protocole [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) décrit dans **Enregistrement de l'analytique**.

{% endtab %}
{% tab React Native %}

Lorsqu'un utilisateur clique sur une Content Card dans un flux personnalisé, le comportement au clic n'est pas géré automatiquement. Après avoir enregistré le clic avec `Braze.logContentCardClicked(cardId)`, appelez `Braze.processContentCardClickAction(cardId)` pour traiter les deep links, les URLs et les actions `brazeActions://`. Pour la référence des méthodes, consultez [Content Cards React Native]({{site.baseurl}}/developer_guide/content_cards/?sdktab=react%20native).

```javascript
import Braze from "@braze/react-native-sdk";

function onCardPress(card) {
  Braze.logContentCardClicked(card.id);

  if (card.url) {
    Braze.processContentCardClickAction(card.id);
  }
}
```

{% alert important %}
Si vous n'appelez pas `processContentCardClickAction()`, les comportements au clic configurés dans le tableau de bord de Braze ne s'exécuteront pas pour les cartes dans un flux personnalisé.
{% endalert %}

{% endtab %}
{% endtabs %}