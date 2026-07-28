---
nav_title: Comportement
article_title: Personnaliser le comportement des Content Cards
page_order: 2
description: "Ce guide de mise en œuvre aborde la modification du comportement des Content Cards, l'ajout d'éléments supplémentaires tels que des paires clé-valeur à votre payload, ainsi que des recettes pour des personnalisations courantes."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personnaliser le comportement des Content Cards {#customize-the-behavior-of-content-cards}

> Ce guide de mise en œuvre aborde la modification du comportement des Content Cards, l'ajout d'éléments supplémentaires tels que des paires clé-valeur à votre payload, ainsi que des recettes pour des personnalisations courantes. Pour obtenir la liste complète des types de Content Cards, consultez [À propos des Content Cards]({{site.baseurl}}/developer_guide/content_cards).

## Paires clé-valeur {#key-value-pairs}

Braze vous permet d'envoyer des payloads de données supplémentaires via les Content Cards aux appareils des utilisateurs à l'aide de paires clé-valeur. Celles-ci peuvent vous aider à suivre les indicateurs internes, à mettre à jour le contenu de l'application et à personnaliser les propriétés. [Ajoutez des paires clé-valeur à l'aide du tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional).

{% alert note %}
Nous vous déconseillons d'envoyer des valeurs JSON imbriquées sous forme de paires clé-valeur. Aplanissez plutôt le JSON avant de l'envoyer.
{% endalert %}

{% tabs %}
{% tab web %}

Les paires clé-valeur sont stockées sur des objets <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> sous la forme `extras`. Elles peuvent être utilisées pour envoyer des données avec une carte en vue d'un traitement ultérieur par l'application. Appelez `card.extras` pour accéder à ces valeurs.

{% endtab %}
{% tab android %}

Les paires clé-valeur sont stockées sur des objets <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> sous la forme `extras`. Elles peuvent être utilisées pour envoyer des données avec une carte en vue d'un traitement ultérieur par l'application. Appelez <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> pour accéder à ces valeurs.

{% endtab %}
{% tab swift %}

Les paires clé-valeur sont stockées sur des objets <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> sous la forme `extras`. Elles peuvent être utilisées pour envoyer des données avec une carte en vue d'un traitement ultérieur par l'application. Appelez <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> pour accéder à ces valeurs.

{% endtab %}
{% endtabs %}

{% alert tip %}
Il est important que vos équipes marketing et de développement se coordonnent sur les paires clé-valeur qui seront utilisées (par exemple, `feed_type = brand_homepage`), car toutes les paires clé-valeur saisies par les marketeurs dans le tableau de bord de Braze doivent correspondre exactement aux paires clé-valeur que les développeurs intègrent dans la logique de l'application.
{% endalert %}

## Content Cards en tant que contenu supplémentaire {#content-cards-as-supplemental-content}

![Flux avec une liste hybride combinant des données locales et des Content Cards de Braze.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Vous pouvez intégrer de façon fluide les Content Cards dans un flux existant, ce qui permet de charger simultanément les données de plusieurs flux. Cela crée une expérience cohésive et harmonieuse avec les Content Cards de Braze et le contenu du flux existant.

L'exemple ci-contre montre un flux avec une liste hybride d'éléments alimentés par des données locales et des Content Cards propulsées par Braze. Avec cette approche, les Content Cards peuvent être indifférenciables du contenu existant.

### Paires clé-valeur déclenchées par l'API {#api-triggered-key-value-pairs}

Les [Campaigns déclenchées par l'API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) sont une bonne stratégie à employer lorsque les valeurs d'une carte dépendent de facteurs externes pour déterminer le contenu à afficher à l'utilisateur. Par exemple, pour afficher du contenu supplémentaire, définissez des paires clé-valeur à l'aide de Liquid. Notez que `class_type` doit être connu au moment de la configuration.

![Les paires clé-valeur pour le cas d'usage des Content Cards supplémentaires. Dans cet exemple, différents aspects de la carte, tels que « tile_id », « tile_deeplink » et « tile_title », sont définis à l'aide de Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards en tant que contenu interactif {#content-cards-as-interactive-content}
![Une Content Card interactive affichant une promotion de 50 % apparaît dans le coin inférieur gauche de l'écran. Après un clic, la promotion est appliquée au panier.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Les Content Cards peuvent être exploitées pour créer des expériences dynamiques et interactives pour vos utilisateurs. Dans l'exemple ci-contre, une fenêtre contextuelle de Content Card apparaît au moment du paiement, proposant aux utilisateurs des promotions de dernière minute. Des cartes bien placées comme celle-ci constituent un excellent moyen d'inciter les utilisateurs à effectuer des actions spécifiques.

Les paires clé-valeur pour ce cas d'usage comprennent `discount_percentage` défini comme le montant de remise souhaité et `class_type` défini comme `coupon_code`. Ces paires clé-valeur vous permettent de filtrer et d'afficher des Content Cards spécifiques à un type sur l'écran de paiement. Pour plus d'informations sur l'utilisation de paires clé-valeur pour gérer plusieurs flux, consultez [Personnaliser le flux par défaut des Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds).
<br>
<br>

![Content Card interactive affichant une promotion au moment du paiement.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Badges de Content Cards {#content-card-badges}

![Écran d'accueil d'un iPhone montrant un exemple d'application Braze nommé Swifty avec un badge rouge affichant le chiffre 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Les badges sont de petites icônes idéales pour attirer l'attention d'un utilisateur. L'utilisation de badges pour alerter l'utilisateur sur le nouveau contenu des Content Cards peut inciter les utilisateurs à revenir sur votre application et augmenter le nombre de sessions.

### Affichage du nombre de Content Cards non lues sous forme de badge {#displaying-the-number-of-unread-content-cards-as-a-badge}

Vous pouvez afficher le nombre de Content Cards non lues de votre utilisateur sous forme de badge sur l'icône de votre application.

{% tabs %}
{% tab web %}

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Vous pouvez ensuite utiliser ces informations pour afficher un badge indiquant le nombre de Content Cards non lues. Consultez la <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">documentation de référence du SDK</a> pour plus d'informations.

{% endtab %}
{% tab android %}

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

Vous pouvez ensuite utiliser ces informations pour afficher un badge indiquant le nombre de Content Cards non lues. Consultez la <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">documentation de référence du SDK</a> pour plus d'informations.


{% endtab %}
{% tab swift %}

L'exemple suivant utilise `braze.contentCards` pour demander et afficher le nombre de Content Cards non lues. Après la fermeture de l'application et la fin de la session de l'utilisateur, ce code demande un décompte des cartes, en filtrant le nombre de cartes en fonction de la propriété `viewed`.

Les applications ayant adopté le [cycle de vie `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) (requis pour les applications compilées avec [Xcode 27 et versions ultérieures](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)) doivent implémenter cela dans `sceneDidEnterBackground(_:)` de `SceneDelegate.swift` plutôt que dans `applicationDidEnterBackground(_:)` de `AppDelegate.swift`.

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

Dans cette méthode, implémentez le code suivant, qui actualise activement le nombre de badges pendant que l'utilisateur consulte les cartes au cours d'une session donnée :

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

Dans cette méthode, implémentez le code suivant, qui actualise activement le nombre de badges pendant que l'utilisateur consulte les cartes au cours d'une session donnée :

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}