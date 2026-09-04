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

Braze vous permet d'envoyer des payloads de données supplémentaires via les Content Cards vers les appareils des utilisateurs à l'aide de paires clé-valeur. Celles-ci peuvent vous aider à suivre des indicateurs internes, mettre à jour le contenu de l'application et personnaliser des propriétés. [Ajoutez des paires clé-valeur à l'aide du tableau de bord]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#step-4-configure-additional-settings-optional).

{% alert note %}
Nous vous déconseillons d'envoyer des valeurs JSON imbriquées en tant que paires clé-valeur. Aplatissez plutôt le JSON avant de l'envoyer.
{% endalert %}

{% tabs %}
{% tab web %}

Les paires clé-valeur sont stockées sur les objets <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> en tant que `extras`. Elles peuvent être utilisées pour envoyer des données accompagnant une carte en vue d'un traitement ultérieur par l'application. Appelez `card.extras` pour accéder à ces valeurs.

{% endtab %}
{% tab android %}

Les paires clé-valeur sont stockées sur les objets <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> en tant que `extras`. Elles peuvent être utilisées pour envoyer des données accompagnant une carte en vue d'un traitement ultérieur par l'application. Appelez <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> pour accéder à ces valeurs.

{% endtab %}
{% tab swift %}

Les paires clé-valeur sont stockées sur les objets <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> en tant que `extras`. Elles peuvent être utilisées pour envoyer des données accompagnant une carte en vue d'un traitement ultérieur par l'application. Appelez <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> pour accéder à ces valeurs.

{% endtab %}
{% endtabs %}

{% alert tip %}
Il est important que vos équipes marketing et de développement se coordonnent sur les paires clé-valeur qui seront utilisées (par exemple, `feed_type = brand_homepage`), car toute paire clé-valeur saisie par les marketeurs dans le tableau de bord de Braze doit correspondre exactement aux paires clé-valeur intégrées par les développeurs dans la logique de l'application.
{% endalert %}

## Les Content Cards comme contenu complémentaire {#content-cards-as-supplemental-content}

![Flux avec une liste hybride combinant des données locales et des Content Cards de Braze.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Vous pouvez intégrer de façon fluide les Content Cards dans un flux existant, permettant ainsi de charger simultanément les données de plusieurs flux. Cela crée une expérience cohérente et harmonieuse entre les Content Cards de Braze et le contenu de flux existant.

L'exemple ci-contre montre un flux avec une liste hybride d'éléments alimentés par des données locales et des Content Cards propulsées par Braze. Ainsi, les Content Cards peuvent se fondre parfaitement dans le contenu existant.

### Paires clé-valeur déclenchées par l'API {#api-triggered-key-value-pairs}

Les [Campaigns déclenchées par l'API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) constituent une bonne stratégie lorsque les valeurs d'une carte dépendent de facteurs externes pour déterminer le contenu à afficher à l'utilisateur. Par exemple, pour afficher du contenu complémentaire, définissez des paires clé-valeur à l'aide de Liquid. Notez que `class_type` doit être connu au moment de la configuration.

![Les paires clé-valeur pour le cas d'usage de Content Cards complémentaires. Dans cet exemple, différents aspects de la carte tels que « tile_id », « tile_deeplink » et « tile_title » sont définis à l'aide de Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Les Content Cards en tant que contenu interactif {#content-cards-as-interactive-content}
![Une Content Card interactive affichant une promotion de 50 pour cent apparaît dans le coin inférieur gauche de l'écran. Lorsqu'on clique dessus, la promotion est appliquée au panier.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Les Content Cards peuvent être exploitées pour créer des expériences dynamiques et interactives pour vos utilisateurs. Dans l'exemple ci-contre, une Content Card apparaît sous forme de pop-up lors du paiement pour proposer aux utilisateurs des promotions de dernière minute. Des cartes bien placées comme celle-ci constituent un excellent moyen d'inciter les utilisateurs à effectuer des actions spécifiques.

Les paires clé-valeur pour ce cas d'usage incluent un `discount_percentage` défini comme le montant de remise souhaité et un `class_type` défini comme `coupon_code`. Ces paires clé-valeur vous permettent de filtrer et d'afficher des Content Cards spécifiques à un type sur l'écran de paiement. Pour en savoir plus sur l'utilisation des paires clé-valeur pour gérer plusieurs flux, consultez la section [Personnaliser le flux de Content Cards par défaut]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds).
<br>
<br>

![Content Card interactive affichant une promotion lors du paiement.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Badges de Content Cards {#content-card-badges}

![Un écran d'accueil iPhone affichant un exemple d'application Braze nommée Swifty avec un badge rouge indiquant le chiffre 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Les badges sont de petites icônes idéales pour attirer l'attention d'un utilisateur. Utiliser des badges pour signaler du nouveau contenu de Content Cards peut inciter les utilisateurs à revenir dans votre application et augmenter les sessions.

### Afficher le nombre de Content Cards non lues sous forme de badge {#displaying-the-number-of-unread-content-cards-as-a-badge}

Vous pouvez afficher le nombre de Content Cards non lues de votre utilisateur sous forme de badge sur l'icône de votre application.

{% tabs %}
{% tab web %}

Vous pouvez demander le nombre de cartes non lues à tout moment en appelant :

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Vous pouvez ensuite utiliser cette information pour afficher un badge indiquant le nombre de Content Cards non lues. Consultez la <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">documentation de référence du SDK</a> pour plus d'informations.

{% endtab %}
{% tab android %}

Vous pouvez demander le nombre de cartes non lues à tout moment en appelant :

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

Vous pouvez ensuite utiliser cette information pour afficher un badge indiquant le nombre de Content Cards non lues. Consultez la <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">documentation de référence du SDK</a> pour plus d'informations.


{% endtab %}
{% tab swift %}

L'exemple suivant utilise `braze.contentCards` pour demander et afficher le nombre de Content Cards non lues. Après la fermeture de l'application et la fin de la session de l'utilisateur, ce code demande un décompte des cartes, en filtrant le nombre de cartes en fonction de la propriété `viewed`.

Les applications ayant adopté le [cycle de vie `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) (requis pour les applications compilées avec [Xcode 27 et versions ultérieures](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)) doivent implémenter ceci dans `sceneDidEnterBackground(_:)` de `SceneDelegate.swift` plutôt que dans `applicationDidEnterBackground(_:)` de `AppDelegate.swift`.

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

Dans cette méthode, implémentez le code suivant, qui met activement à jour le compteur du badge pendant que l'utilisateur consulte les cartes au cours d'une session donnée :

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

Dans cette méthode, implémentez le code suivant, qui met activement à jour le compteur du badge pendant que l'utilisateur consulte les cartes au cours d'une session donnée :

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