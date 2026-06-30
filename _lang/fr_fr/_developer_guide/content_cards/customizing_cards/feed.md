---
nav_title: Flux par défaut
article_title: Personnaliser le flux pour les Content Cards
page_order: 3
description: "Cet article traite des options de personnalisation du flux de Content Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personnaliser le flux pour les Content Cards {#customize-the-feed-for-content-cards}

> Un flux de Content Cards correspond à la séquence de Content Cards dans vos applications mobiles ou Web. Cet article traite de la configuration du moment où le flux est actualisé, de l'ordre des cartes, de la gestion de plusieurs flux et des messages d'erreur « flux vide ». Pour obtenir la liste complète des types de cartes de contenu, consultez [À propos des Content Cards]({{site.baseurl}}/developer_guide/content_cards).

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Actualiser le flux {#refreshing-the-feed}

### Actualisation automatique {#automatic-refresh}

Par défaut, le flux de Content Cards s'actualise automatiquement lorsque :

- Une nouvelle session est lancée
- Le flux par défaut de Content Cards est fermé puis rouvert après plus de 60 secondes depuis la dernière actualisation.

{% alert tip %}
Pour afficher dynamiquement des Content Cards à jour sans les actualiser manuellement, sélectionnez **À la première impression** lors de la création de la carte. Ces cartes seront actualisées dès qu'elles seront disponibles.
{% endalert %}

### Actualisation manuelle {#manual-refresh}

Pour actualiser manuellement le flux à un moment précis :

{% tabs %}
{% tab web %}

Demandez à tout moment une actualisation manuelle des Content Cards Braze à partir du SDK Web en appelant [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh).

Vous pouvez également appeler [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) pour obtenir toutes les cartes actuellement disponibles depuis la dernière actualisation des Content Cards.

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();
}
```

Pour ouvrir les liens des Content Cards dans un nouvel onglet du navigateur au lieu du même onglet, définissez `openCardsInNewTab: true` dans les options d'initialisation de votre SDK Web. Pour plus d'informations sur les options d'initialisation, consultez le [guide du dépôt du SDK Web]({{site.baseurl}}/developer_guide/sdk_repository_guides/web).

{% endtab %}
{% tab android %}

Demandez à tout moment une actualisation manuelle des Content Cards Braze à partir du SDK Android en appelant [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html).

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Demandez à tout moment une actualisation manuelle des Content Cards Braze à partir du SDK Swift en appelant la méthode [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) de la classe [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class) :

{% subtabs local %}
{% subtab Swift %}

Dans Swift, les Content Cards peuvent être actualisées soit avec un gestionnaire d'achèvement facultatif, soit avec un retour asynchrone en utilisant les API de concurrence natives de Swift.

#### Gestionnaire d'achèvement {#completion-handler}

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

#### Async/Await

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Synchronisation complète vs synchronisation partielle {#full-sync-vs-partial-sync}

Le SDK Braze utilise deux types de synchronisation lors de la récupération des Content Cards depuis le serveur :

- **Synchronisation complète :** récupère toutes les Content Cards auxquelles un utilisateur est éligible. Les synchronisations complètes se produisent automatiquement tous les 7 jours ou chaque fois que `changeUser()` est appelé.
- **Synchronisation partielle :** récupère uniquement les nouvelles Content Cards depuis la dernière requête. Si l'utilisateur n'est éligible à aucune nouvelle carte, la réponse renvoie zéro carte. Les synchronisations partielles se produisent chaque fois que `requestContentCardsRefresh()` est appelé (sauf si 7 jours se sont écoulés depuis la dernière synchronisation complète, auquel cas une synchronisation complète est déclenchée à la place).

Les synchronisations partielles réduisent la charge serveur et la consommation de batterie de l'appareil. Les Content Cards déjà reçues sont stockées localement dans le SDK, de sorte que les utilisateurs continueront à voir leurs cartes disponibles même lorsqu'une synchronisation partielle ne renvoie aucune nouvelle carte.

### Limite de débit {#rate-limit}

Braze utilise un algorithme de compartiment à jetons pour appliquer les limites de débit suivantes :
- Jusqu'à 5 appels d'actualisation par appareil, partagés entre les utilisateurs et les appels à `openSession()`
- Une fois la limite atteinte, un nouvel appel devient disponible toutes les 180 secondes (3 minutes)
- Le système conserve jusqu'à cinq appels que vous pouvez utiliser à tout moment
- `subscribeToContentCards()` renverra toujours les cartes mises en cache, même lorsque la limite de débit est atteinte

{% alert important %}
Le SDK Braze applique également des limites de débit pour garantir les performances et la fiabilité. Gardez cela à l'esprit lorsque vous effectuez des tests automatisés ou des tests d'assurance qualité manuels. Consultez les [limites de débit du SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/rate_limits) pour plus d'informations.
{% endalert %}

## Personnaliser l'ordre d'affichage des cartes {#customizing-displayed-card-order}

Vous pouvez modifier l'ordre d'affichage de vos Content Cards. Cela vous permet d'affiner l'expérience utilisateur en donnant la priorité à certains types de contenu, comme les promotions urgentes.

{% tabs %}
{% tab web %}

Personnalisez l'ordre d'affichage des Content Cards dans votre flux en utilisant le paramètre [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) de `showContentCards():`. Par exemple :

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view controller %}
Le [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) s'appuie sur un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) pour gérer tout tri ou modification des Content Cards avant leur affichage dans le flux. Un gestionnaire de mise à jour personnalisé peut être défini via [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) sur votre `ContentCardsFragment`.

Voici le `IContentCardsUpdateHandler` par défaut, qui peut servir de point de départ pour la personnalisation :

{% details Afficher l'exemple Java %}
```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```
{% enddetails %}

{% details Afficher l'exemple Kotlin %}
```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```
{% enddetails %}

{% alert tip %}
Le code source de `ContentCardsFragment` est disponible sur [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt).
{% endalert %}
{% endsubtab %}
{% subtab Jetpack Compose %}
Pour filtrer et trier les Content Cards dans Jetpack Compose, définissez le paramètre `cardUpdateHandler`. Par exemple :

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Personnalisez l'ordre du flux de cartes en modifiant directement la variable statique [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personnalisation via `BrazeContentCardUI.ViewController.Attributes` n'est pas disponible en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Personnaliser le message « flux vide » {#customizing-empty-feed-message}

Lorsqu'un utilisateur n'est éligible à aucune Content Card, le SDK affiche un message d'erreur « flux vide » indiquant : « Nous n'avons pas de mises à jour. Veuillez vérifier à nouveau plus tard. » Vous pouvez personnaliser ce message d'erreur de la manière suivante :

![Un message d'erreur de flux vide indiquant « Ceci est un message d'état vide personnalisé. »]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab web %}

Le SDK Web ne permet pas de remplacer le texte du « flux vide » par programmation. Vous pouvez choisir de le remplacer à chaque affichage du flux, mais cela n'est pas recommandé car le flux peut mettre un certain temps à s'actualiser et le texte du flux vide ne s'affichera pas immédiatement.

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

Si le [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) détermine que l'utilisateur n'est éligible à aucune Content Card, il affiche le message d'erreur du flux vide.

Un adaptateur spécial, le [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt), remplace l'adaptateur standard [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt) pour afficher ce message d'erreur. Pour définir le message personnalisé, remplacez la ressource de chaîne de caractères `com_braze_feed_empty`.

Le style utilisé pour afficher ce message est accessible via [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530) et est reproduit dans l'extrait de code suivant :

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

Pour plus d'informations sur la personnalisation des éléments de style des Content Cards, consultez [Personnaliser le style]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style).
{% endsubtab %}
{% subtab Jetpack Compose %}
Pour personnaliser le message d'erreur « flux vide » avec Jetpack Compose, vous pouvez passer une `emptyString` à [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). Vous pouvez également transmettre [`emptyTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html#1193499348%2FProperties%2F-1725759721) à `ContentCardListStyling` pour personnaliser davantage ce message.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Si vous souhaitez afficher un Composable à la place, vous pouvez passer `emptyComposable` à [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). Si `emptyComposable` est spécifié, `emptyString` ne sera pas utilisé.

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}
{% subtabs local %}
{% subtab Swift %}

Personnalisez l'état vide du contrôleur de vue en définissant les [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) associés.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Modifiez le texte qui s'affiche automatiquement dans les flux de Content Cards vides en redéfinissant les chaînes de caractères localisables des Content Cards dans le fichier [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) de votre application.

{% alert note %}
Si vous souhaitez mettre à jour ce message dans différentes langues, recherchez la langue correspondante dans la [structure du dossier Resources](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) avec la chaîne de caractères `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Implémenter plusieurs flux {#implementing-multiple-feeds}

Les Content Cards peuvent être filtrées dans votre application afin que seules certaines cartes soient affichées, ce qui vous permet de disposer de plusieurs flux de Content Cards pour différents cas d'utilisation. Par exemple, vous pouvez gérer à la fois un flux transactionnel et un flux marketing. Pour ce faire, créez différentes catégories de Content Cards en définissant des paires clé-valeur dans le tableau de bord de Braze. Ensuite, créez des flux dans votre application ou votre site qui traitent ces types de Content Cards différemment, en filtrant certains types et en affichant les autres.

### Étape 1 : Définir des paires clé-valeur sur les cartes {#step-1-set-key-value-pairs-on-cards}

Lors de la création d'une campagne de Content Cards, définissez des [données de paires clé-valeur]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) sur chaque carte. Vous utiliserez cette paire clé-valeur pour catégoriser les cartes. Les paires clé-valeur sont stockées dans la propriété `extras` du modèle de données de la carte.

Pour cet exemple, nous allons définir une paire clé-valeur avec la clé `feed_type` qui désignera dans quel flux de Content Cards la carte doit s'afficher. La valeur correspondra à vos flux personnalisés, par exemple `home_screen` ou `marketing`.

### Étape 2 : Filtrer les Content Cards {#step-2-filter-content-cards}

Une fois les paires clé-valeur attribuées, créez un flux avec une logique qui affichera les cartes souhaitées et filtrera les cartes d'autres types. Dans cet exemple, nous n'afficherons que les cartes dont la paire clé-valeur correspond à `feed_type: "Transactional"`.

{% tabs %}
{% tab web %}

L'exemple suivant affiche le flux de Content Cards pour les cartes de type `Transactional` :

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

Ensuite, vous pouvez configurer un bouton de basculement pour votre flux personnalisé :

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional");
};
```

Pour plus d'informations, consultez la [documentation des méthodes du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

Par défaut, le flux de Content Cards s'affiche dans un [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) et [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) renvoie une liste de cartes à afficher après avoir reçu un [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) du SDK Braze. Cependant, il ne fait que trier les cartes et ne gère pas directement le filtrage.

#### Étape 2.1 : Créer un gestionnaire personnalisé {#step-21-create-a-custom-handler}

Vous pouvez filtrer les Content Cards en implémentant un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) personnalisé en utilisant les paires clé-valeur définies par [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) dans le tableau de bord, puis en le modifiant pour supprimer de la liste toutes les cartes qui ne correspondent pas à la valeur de `feed_type` que vous avez définie précédemment.

{% details Afficher l'exemple Java %}
```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```
{% enddetails %}

{% details Afficher l'exemple Kotlin %}
```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```
{% enddetails %}

#### Étape 2.2 : L'ajouter à un fragment {#step-22-add-it-to-a-fragment}

Après avoir créé un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html), créez un [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) qui l'utilise. Ce flux personnalisé peut être utilisé comme n'importe quel autre `ContentCardsFragment`. Dans les différentes parties de votre application, affichez différents flux de Content Cards en fonction de la clé fournie dans le tableau de bord. Chaque flux `ContentCardsFragment` affichera un ensemble unique de cartes grâce au `IContentCardsUpdateHandler` personnalisé sur chaque fragment.

{% details Afficher l'exemple Java %}
```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% enddetails %}

{% details Afficher l'exemple Kotlin %}
```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% enddetails %}
{% endsubtab %}

{% subtab Jetpack Compose %}
Pour filtrer les Content Cards affichées dans ce flux, utilisez `cardUpdateHandler`. Par exemple :

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

The following example will show the Content Cards feed for `Transactional` type cards:

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

Pour aller plus loin, les cartes présentées dans le contrôleur de vue peuvent être filtrées en définissant la propriété `transform` sur votre structure `Attributes` afin de n'afficher que les cartes filtrées selon vos critères.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}