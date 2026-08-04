---
nav_title: "Migration depuis les Content Cards"
article_title: "Migration des Content Cards vers les bannières"
description: "Découvrez comment effectuer la migration des Content Cards vers les bannières, avec des exemples de code pour tous les SDK pris en charge, les limitations et les avantages."
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Migration des Content Cards vers les bannières {#migrate-from-content-cards-to-banners}

> Ce guide vous accompagne dans la migration des Content Cards vers les bannières pour les cas d'usage de messages de type bannière. Les bannières sont idéales pour les messages in-app et web persistants, intégrés directement dans votre application à des emplacements spécifiques.

## Pourquoi migrer vers les Banners ? {#why-migrate-to-banners}

- Si votre équipe d'ingénierie développe ou maintient des Content Cards personnalisées, migrer vers les Banners peut réduire cet investissement continu. Les Banners permettent aux marketeurs de contrôler l'interface utilisateur directement, libérant les développeurs pour d'autres tâches.
- Si vous lancez de nouveaux messages sur la page d'accueil, des flux d'onboarding ou des annonces persistantes, commencez par les Banners plutôt que de développer sur les Content Cards. Vous pouvez bénéficier de la personnalisation en temps réel, de l'absence d'expiration à 30 jours, de l'absence de limite de taille et de la priorisation native dès le premier jour.
- Si vous contournez la limite d'expiration de 30 jours, gérez une logique de rééligibilité complexe ou êtes frustré par une personnalisation obsolète, les Banners résolvent ces problèmes nativement.

Les Banners offrent plusieurs avantages par rapport aux Content Cards pour les communications de type bannière :

### Production accélérée {#accelerated-production}

- **Moins de support technique continu requis** : les marketeurs peuvent créer des messages personnalisés à l'aide d'un éditeur glisser-déposer et de HTML personnalisé sans nécessiter l'assistance d'un développeur pour la personnalisation.
- **Options de personnalisation flexibles** : concevez directement dans l'éditeur, utilisez du HTML ou tirez parti des modèles de données existants avec des propriétés personnalisées.

### Meilleure expérience utilisateur {#better-ux}

- **Mises à jour dynamiques du contenu** : les Banners actualisent la logique Liquid et l'éligibilité à chaque rafraîchissement, garantissant que les utilisateurs voient toujours le contenu le plus pertinent.
- **Prise en charge native des emplacements** : les messages apparaissent dans des contextes spécifiques plutôt que dans un flux, offrant une meilleure pertinence contextuelle.
- **Priorisation native** : contrôle de l'ordre d'affichage sans logique personnalisée, facilitant la gestion de la hiérarchie des messages.

### Persistance {#persistence}

- **Aucune limite d'expiration** : les Campaigns de type Banner n'ont pas de limite d'expiration de 30 jours comme les Content Cards, permettant une véritable persistance des messages.

## Quand migrer {#when-to-migrate}

Envisagez de migrer vers les Banners si vous utilisez les Content Cards pour :

- Des héros de page d'accueil, des promotions de pages produits, des offres au moment du paiement
- Des annonces de navigation persistantes ou des messages dans la barre latérale
- Des messages permanents diffusés pendant plus de 30 jours
- Des messages pour lesquels vous souhaitez une personnalisation et une éligibilité en temps réel

## Quand conserver les Content Cards {#when-to-keep-content-cards}

Continuez à utiliser les Content Cards si vous avez besoin de :

- **Expériences de flux :** Tout cas d'usage impliquant plusieurs messages défilants ou une « boîte de réception » basée sur des cartes.
- **Fonctionnalités spécifiques :** Messages nécessitant des codes promotionnels, car les bannières ne les prennent pas en charge nativement. Les bannières prennent en charge le [contenu connecté]({{site.baseurl}}/developer_guide/banners#connected-content) en accès anticipé.
- **Livraison déclenchée :** Cas d'usage nécessitant strictement une livraison déclenchée par API ou par événement. Bien que les bannières ne prennent pas en charge la livraison déclenchée par API ou par événement, l'évaluation de l'éligibilité en temps réel signifie que les utilisateurs se qualifient ou se disqualifient instantanément en fonction de leur appartenance à un Segment à chaque actualisation.

## Guide de migration {#migration-guide}

### Prérequis {#prerequisites}

Avant de migrer, assurez-vous que votre SDK Braze respecte les versions minimales requises :

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

Les fermetures et la rééligibilité nécessitent les versions minimales de SDK suivantes :

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### S'abonner aux mises à jour {#subscribe-to-updates}

#### Approche Content Cards {#content-cards-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### Approche Banners {#banners-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("sample_placement_id").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### Afficher le contenu {#display-content}

{% alert note %}
Les Content Cards peuvent être rendues manuellement avec une logique d'interface personnalisée, tandis que les Banners ne peuvent être rendues qu'avec les méthodes prêtes à l'emploi du SDK.
{% endalert %}

#### Approche Content Cards

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getCachedContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### Approche Banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### Enregistrer les analyses (implémentations personnalisées) {#log-analytics-custom-implementations}

{% alert note %}
Les Content Cards et les Banners suivent automatiquement les analyses lorsque vous utilisez leurs composants d'interface par défaut. Les exemples suivants concernent les implémentations personnalisées où vous créez votre propre interface.
{% endalert %}

#### Approche Content Cards

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
  card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
  card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
  braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### Approche Banners

{% tabs %}
{% tab Web %}

{% alert important %}
Les analyses sont automatiquement suivies lors de l'utilisation d'`insertBanner()`. L'enregistrement manuel ne doit pas être utilisé avec `insertBanner()`.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
Les analyses sont automatiquement suivies lors de l'utilisation de BannerView. L'enregistrement manuel ne doit pas être utilisé avec BannerView.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
Les analyses sont automatiquement suivies lors de l'utilisation de BannerUIView. L'enregistrement manuel ne doit pas être utilisé avec BannerUIView par défaut.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
Les analyses sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucun enregistrement manuel n'est nécessaire.
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
Les analyses sont automatiquement suivies lors de l'utilisation de BrazeBannerView. Aucun enregistrement manuel n'est nécessaire.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Obtenir les propriétés {#getting-properties}

#### Approche Content Cards

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### Approche Banners

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### Gérer les groupes de contrôle {#handling-control-groups}

#### Approche Content Cards

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### Approche Banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## Limitations {#limitations}

Lors de la migration de Content Cards vers les bannières, tenez compte des limitations suivantes :

### Migration des messages déclenchés {#migrating-triggered-messages}

Les bannières ne prennent en charge que les Campaigns à livraison planifiée. Pour migrer un message qui était précédemment déclenché par API ou par événement, convertissez-le en ciblage basé sur les segments :

- **Exemple :** Au lieu de déclencher une carte « Compléter le profil » avec l'API, créez un Segment pour les utilisateurs qui se sont inscrits au cours des 7 derniers jours mais n'ont pas complété leur profil.
- **Éligibilité en temps réel :** Les utilisateurs deviennent éligibles ou inéligibles pour la bannière instantanément à chaque actualisation en fonction de leur appartenance au Segment.

### Différences de fonctionnalités {#feature-differences}

| Fonctionnalité | Content Cards | Bannières |
|---------|--------------|---------|
| **Structure du contenu** |
| Plusieurs cartes dans le flux | ✅ Pris en charge | ✅ Possibilité de créer plusieurs emplacements pour obtenir une implémentation de type carrousel. Une seule bannière est renvoyée par emplacement. |
| Emplacements multiples | N/A | ✅ Emplacements multiples pris en charge |
| Types de cartes (Classique, Avec légende, Image uniquement) | ✅ Plusieurs types prédéfinis | ✅ Bannière unique basée sur HTML (plus flexible) |
| **Gestion du contenu** |
| Éditeur par glisser-déposer | ❌ Nécessite un développeur pour la personnalisation | ✅ Les marketeurs peuvent créer/mettre à jour sans ingénierie |
| HTML/CSS personnalisé | ❌ Limité à la structure de la carte | ✅ Prise en charge complète HTML/CSS |
| Paires clé-valeur pour la personnalisation | ✅ Requis pour la personnalisation avancée | ✅ Paires clé-valeur fortement typées appelées « propriétés » pour la personnalisation avancée |
| Extras de message | ✅ Pris en charge | ❌ Non pris en charge actuellement |
| **Persistance et expiration** |
| Expiration de la carte | ✅ Pris en charge (limite de 30 jours) | ✅ Pris en charge (pas de limite d'expiration) |
| Persistance réelle | ❌ Maximum de 30 jours | ✅ Persistance illimitée |
| **Affichage et ciblage** |
| Interface du flux | ✅ Flux par défaut disponible | ❌ Basé sur les emplacements uniquement |
| Emplacement contextuel | ❌ Basé sur le flux | ✅ Prise en charge native des emplacements |
| Priorisation | ❌ Nécessite une logique personnalisée | ✅ Priorisation native |
| **Interaction utilisateur** |
| Fermeture manuelle | ✅ Pris en charge | ✅ Pris en charge |
| Rééligibilité après fermeture | ❌ Nécessite des filtres personnalisés ou une logique de Campaign | ✅ Période d'attente par défaut |
| Cartes épinglées | ✅ Pris en charge | N/A |
| **Analyse** |
| Analyse automatique (interface par défaut) | ✅ Pris en charge | ✅ Pris en charge |
| Tri par priorité | ❌ Non pris en charge | ✅ Pris en charge |
| **Mises à jour du contenu** |
| Actualisation du templating Liquid | ❌ Une seule fois par carte à l'envoi/lancement | ✅ Actualisation à chaque rafraîchissement |
| Actualisation de l'éligibilité | ❌ Une seule fois par carte à l'envoi/lancement | ✅ Actualisation à chaque session |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Différences de fonctionnalités" }

### Limitations du produit {#product-limitations}

- Jusqu'à 25 messages actifs par emplacement.
- Jusqu'à 10 ID d'emplacement par requête d'actualisation ; les requêtes au-delà de cette limite sont tronquées.

### Limitations du SDK {#sdk-limitations}

- Les bannières ne sont actuellement pas prises en charge sur .NET MAUI (Xamarin), Cordova, Unity, Vega ou les plateformes TV.
- Assurez-vous d'utiliser les versions minimales du SDK indiquées dans les prérequis.

## Articles connexes {#related-articles}

- [Emplacements de bannières]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutoriel : Afficher une bannière par ID d'emplacement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Analyse des bannières]({{site.baseurl}}/developer_guide/banners/analytics)
- [FAQ sur les bannières]({{site.baseurl}}/developer_guide/banners/faq)