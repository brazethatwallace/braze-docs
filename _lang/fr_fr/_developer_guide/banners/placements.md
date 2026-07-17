---
nav_title: Gérer les placements
article_title: Gérer les emplacements de bannières pour le SDK Braze
description: "Découvrez comment créer et gérer les emplacements de bannières dans le SDK Braze, notamment comment accéder à leurs propriétés uniques et enregistrer les impressions."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Gérer les emplacements de bannières {#manage-banner-placements}

> Découvrez comment créer et gérer les emplacements de bannières dans le SDK Braze, notamment comment accéder à leurs propriétés uniques et enregistrer les impressions. Pour plus d'informations générales, consultez [À propos des bannières]({{site.baseurl}}/developer_guide/banners).

## À propos des demandes de placement {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Créer un placement {#create-a-placement}

### Conditions préalables {#prerequisites}

Voici les versions minimales du SDK requises pour créer des emplacements de bannières :

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Étape 2 : Actualiser les placements dans votre application {#requestBannersRefresh}

Pour actualiser les placements, appelez la méthode d'actualisation de votre SDK (`requestBannersRefresh()` sur Web et Android, ou `requestRefresh()` sur Swift).

Le comportement d'actualisation des bannières suit deux chemins :

1. **Actualisation explicite :** Vous pouvez appeler la méthode d'actualisation à tout moment pendant une session active.
2. **Actualisation automatique lors d'une nouvelle session :** Après avoir effectué au moins une demande d'actualisation explicite, le SDK peut redemander les ID de placement les plus récemment demandés lorsqu'une nouvelle session Braze démarre (par exemple, après `changeUser()` ou après un délai d'expiration de session).

Le rôle de `subscribeToBannersUpdates()` diffère selon la plateforme :

- **iOS et Android :** `subscribeToBannersUpdates()` (ou `subscribeToUpdates()` sur Swift) enregistre un rappel de mise à jour. L'actualisation automatique au démarrage de session ne dépend pas de l'activation de l'abonnement.
- **Web :** L'actualisation automatique au démarrage de session est liée à l'enregistrement de `subscribeToBannersUpdates()`. Sans abonnement actif, le SDK ne répète pas automatiquement l'actualisation lors d'une nouvelle session.

Dans tous les cas, vous devez effectuer au moins une demande d'actualisation explicite par cycle de vie de l'application afin que le SDK sache quels ID de placement maintenir à jour. Les bannières ne sont pas récupérées automatiquement au premier lancement sans cet appel initial, et les ID de placement suivis sont réinitialisés après le redémarrage de l'application.

Les actualisations automatiques au démarrage de session ne consomment pas de jeton de limitation du débit.

{% alert tip %}
Actualisez les placements dès que possible afin d'éviter tout retard dans le téléchargement ou l'affichage des bannières.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Étape 3 : Écouter les mises à jour {#subscribeToBannersUpdates}

{% alert tip %}
Si vous insérez des bannières à l'aide des méthodes SDK décrites dans ce guide, tous les événements analytiques (tels que les impressions et les clics) sont gérés automatiquement, et les impressions ne sont enregistrées que lorsque la bannière est visible.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Si vous utilisez du JavaScript vanilla avec le SDK Braze pour le Web, utilisez [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) pour écouter les mises à jour de placement, puis appelez [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) pour les récupérer.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Si vous utilisez React avec le SDK Braze pour le Web, configurez [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) à l'intérieur d'un hook `useEffect` et appelez [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) après avoir enregistré votre écouteur.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

{% alert note %}
Votre écouteur de mise à jour de bannière reflète l'état en mémoire des bannières du SDK. Une seule mise à jour peut inclure des placements déjà mis en cache (par exemple, à partir d'une actualisation précédente, d'un autre écran ou d'un travail automatique du SDK), et pas uniquement les ID de placement de votre appel `requestRefresh` le plus récent. Si vous ne vous intéressez qu'à certains placements, vérifiez l'ID de placement de chaque bannière dans votre écouteur et ignorez les autres. Après avoir enregistré votre écouteur, appelez `requestRefresh` pour les placements que vous souhaitez synchroniser depuis Braze.
{% endalert %}

```swift
let placementIds = ["global_banner", "navigation_square_banner"]
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
// Always refresh after your subscriber is registered
brazeClient.braze()?.banners.requestRefresh(placementIds: placementIds)
```

{% endtab %}
{% tab Android %}

{% alert note %}
Votre écouteur de mise à jour de bannière reflète l'état en mémoire des bannières du SDK. Une seule mise à jour peut inclure des placements déjà mis en cache (par exemple, à partir d'une actualisation précédente, d'un autre écran ou d'un travail automatique du SDK), et pas uniquement les ID de placement de votre appel `requestBannersRefresh` le plus récent. Si vous ne vous intéressez qu'à certains placements, vérifiez l'ID de placement de chaque bannière dans votre écouteur et ignorez les autres. Après avoir enregistré votre écouteur, appelez `requestBannersRefresh` pour les placements que vous souhaitez synchroniser depuis Braze.
{% endalert %}

{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> placementIds = new ArrayList<>();
placementIds.add("global_banner");
placementIds.add("navigation_square_banner");
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val placementIds = listOf("global_banner", "navigation_square_banner")
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Étape 4 : Insérer à l'aide de l'ID de placement {#insertBanner}

{% alert tip %}
Pour un tutoriel complet étape par étape, consultez [Afficher une bannière par ID de placement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Créez un élément conteneur pour la bannière. Veillez à définir sa largeur et sa hauteur.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Si vous utilisez du JavaScript vanilla avec le SDK Braze pour le Web, appelez la méthode [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) pour remplacer le HTML interne de l'élément conteneur.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
  baseUrl: "sdk-base-url",
  allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
  // get this placement's banner. If it's `null` the user did not qualify for one.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  // choose where in the DOM you want to insert the banner HTML
  const container = document.getElementById("global-banner-container");

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Si vous utilisez React avec le SDK Braze pour le Web, appelez la méthode [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) avec un `ref` pour remplacer le HTML interne de l'élément conteneur.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Pour suivre les impressions, veillez à appeler `insertBanner` pour `isControl`. Vous pouvez ensuite masquer ou réduire votre conteneur.
{% endalert %}

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// UIKit implementation:
// If you simply want the Banner view, initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// SwiftUI implementation:
// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Pour obtenir la bannière en code Java, utilisez :

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Vous pouvez créer des bannières dans la disposition de vos vues Android en incluant ce XML :

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Si vous utilisez Android Views, utilisez ce XML :

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Pour utiliser Jetpack Compose, ajoutez l'artefact `com.braze:android-sdk-jetpack-compose` au module de votre application. Utilisez la même version que vos autres dépendances du SDK Braze pour Android. Ce module est distinct de `android-sdk-ui` et fournit le composable [`Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html) sous `com.braze.jetpackcompose.banners`.

{% alert note %}
Certaines bibliothèques d'interface Compose définissent leur propre composable `Banner`. Importez `com.braze.jetpackcompose.banners.Banner` explicitement pour appeler l'API de Braze.
{% endalert %}

```kotlin
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
    Banner(placementId = "global_banner")
}
```

Vous pouvez éventuellement passer `heightCallback` pour recevoir la hauteur rendue en dp lorsque la taille de la bannière change. Pour référence, consultez la [KDoc pour `Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html).

Si vous n'ajoutez pas le module Jetpack Compose, encapsulez [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html) dans [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView) :

```kotlin
import android.view.ViewGroup
import androidx.compose.runtime.Composable
import androidx.compose.ui.viewinterop.AndroidView
import com.braze.ui.banners.BannerView

@Composable
fun myBannerSlot() {
    AndroidView(
        factory = { context ->
            BannerView(context, "global_banner").apply {
                layoutParams = ViewGroup.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
                )
            }
        },
        update = { it.placementId = "global_banner" }
    )
}
```

Pour obtenir la bannière en Kotlin, utilisez :
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

Si vous utilisez la [nouvelle architecture de React Native](https://reactnative.dev/architecture/landing-page), vous devez enregistrer `BrazeBannerView` en tant que composant Fabric dans votre `AppDelegate.mm`.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```
Pour l'intégration la plus simple, ajoutez l'extrait de code JavaScript XML (JSX) suivant dans votre hiérarchie de vues, en fournissant uniquement l'ID de placement.

```javascript
<Braze.BrazeBannerView
  placementId='global_banner'
/>
```

Pour obtenir le modèle de données de la bannière dans React Native, ou pour vérifier la présence de ce placement dans le cache de votre utilisateur, utilisez :

```javascript
const banner = await Braze.getBanner("global_banner");
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}
Pour l'intégration la plus simple, ajoutez le widget suivant dans votre hiérarchie de vues, en fournissant uniquement l'ID de placement.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Vous pouvez utiliser la méthode `getBanner` pour vérifier la présence de ce placement dans le cache de votre utilisateur.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Étape 5 : Envoyer une bannière de test (facultatif) {#handling-test-cards}

Avant de lancer une campagne de bannières, vous pouvez [envoyer une bannière de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=banners) pour vérifier votre intégration. Les bannières de test sont stockées dans un cache en mémoire distinct et ne persistent pas lors des redémarrages de l'application. Bien qu'aucune configuration supplémentaire ne soit nécessaire, votre appareil de test doit être capable de recevoir des notifications push au premier plan pour pouvoir afficher le test.

{% alert note %}
Les bannières de test fonctionnent comme toutes les autres bannières, sauf qu'elles sont supprimées lors de la session d'application suivante.
{% endalert %}

## Enregistrer les impressions {#log-impressions}

Braze enregistre automatiquement les impressions pour les bannières visibles lorsque vous utilisez les méthodes SDK pour insérer une bannière&#8212;il n'est donc pas nécessaire de suivre les impressions manuellement.

## Enregistrer les clics {#logging-clicks}

La méthode utilisée pour enregistrer les clics sur les bannières dépend de la manière dont votre bannière est affichée et de l'emplacement de votre gestionnaire de clics.

### Contenu standard de la bannière (automatique) {#standard-banner-content-automatic}

Si vous utilisez les méthodes SDK par défaut et prêtes à l'emploi pour insérer des bannières, et que votre bannière utilise des composants d'éditeur standard (images, boutons, texte), les clics sont suivis automatiquement. Le SDK associe des écouteurs de clics à ces éléments, et aucun code supplémentaire n'est nécessaire.

### Blocs de code personnalisés {#custom-code-blocks}

Si votre bannière utilise le bloc éditeur **Code personnalisé** dans le tableau de bord de Braze, vous devez utiliser `brazeBridge.logClick()` pour enregistrer les clics depuis ce HTML personnalisé. Cela s'applique même lorsque vous utilisez les méthodes SDK pour afficher la bannière, car le SDK ne peut pas associer automatiquement des écouteurs aux éléments de votre code personnalisé.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Pour la référence complète, consultez [Code personnalisé et pont JavaScript pour les bannières]({{site.baseurl}}/user_guide/channels/banners/custom_code). Le `brazeBridge` fournit une couche de communication entre le HTML interne de la bannière et le SDK Braze parent.

### Implémentations d'interface utilisateur personnalisées (headless) {#custom-ui-implementations-headless}

Si vous créez une interface utilisateur entièrement personnalisée à l'aide des [propriétés personnalisées](#custom-properties) de la bannière plutôt que d'afficher le HTML de la bannière, vous devez enregistrer manuellement les clics et les impressions depuis le code de votre application. Étant donné que le SDK n'effectue pas le rendu de la bannière, il n'a aucun moyen de suivre automatiquement les interactions avec vos éléments d'interface utilisateur personnalisés.

Pour les signatures de méthodes et tous les détails, consultez la [documentation de référence du SDK Braze]({{site.baseurl}}/developer_guide/references).

#### Enregistrer les impressions {#logging-impressions}

Appelez la méthode d'impression de bannière de la plateforme lorsque votre interface utilisateur personnalisée considère la bannière comme « vue ». Construisez une logique robuste pour déterminer ce qui constitue une impression afin d'éviter les événements en double — par exemple, enregistrez uniquement lorsque la bannière entre dans la zone visible (ou équivalent), et ne réenregistrez pas lorsque la même bannière revient dans la zone visible ou lorsque votre composant se re-rend sans un nouvel événement de vue.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
const banner = braze.getBanner("placement_id_homepage_top");
if (banner) {
  braze.logBannerImpressions([banner]);
}
```
[Référence du SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top")
```
{% endsubtab %}
{% subtab Java %}
```java
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top");
```
{% endsubtab %}
{% endsubtabs %}
[Référence du SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-impression.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logImpression()
}
```
[Référence du SDK Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logimpression())
{% endtab %}
{% tab React Native %}
```javascript
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");
```
Consultez le [dépôt du SDK React Native](https://github.com/braze-inc/braze-react-native-sdk) pour les dernières signatures de méthodes.
{% endtab %}
{% tab Flutter %}
```dart
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");
```
[Référence du SDK Flutter](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerImpression.html)
{% endtab %}
{% endtabs %}

#### Enregistrer les clics

Appelez la méthode de clic de bannière de la plateforme lorsque l'utilisateur appuie sur votre bannière personnalisée (ou sur un bouton spécifique). Passez le paramètre facultatif `buttonId` lorsque le clic concerne un bouton spécifique afin que les analyses puissent attribuer le clic correctement.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
[Référence du SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId)  // buttonID parameter can be null
```
{% endsubtab %}
{% subtab Java %}
```java
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
{% endsubtab %}
{% endsubtabs %}
[Référence du SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-click.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logClick(buttonId: buttonId)  // buttonID is optional
}
```
[Référence du SDK Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logclick(buttonid:))
{% endtab %}
{% tab React Native %}
```javascript
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
Consultez le [dépôt du SDK React Native](https://github.com/braze-inc/braze-react-native-sdk) pour les dernières signatures de méthodes.
{% endtab %}
{% tab Flutter %}
```dart
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
[Référence du SDK Flutter](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerClicked.html)
{% endtab %}
{% endtabs %}

## Enregistrer les fermetures {#log-dismissals}

Les fermetures de bannières suppriment programmatiquement une bannière d'un placement lorsqu'un utilisateur la ferme activement. Une fois fermée, la bannière est masquée pour cet utilisateur. La prochaine fois que la liste des placements est actualisée, une nouvelle bannière est renvoyée si l'utilisateur est éligible.

### Conditions préalables

Voici les versions minimales du SDK requises pour enregistrer les fermetures de bannières :

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### Intégrations {#integrations}

#### Intégrations de bannières standard (éditeur par glisser-déposer) {#standard-banner-integrations-drag-and-drop-editor}

Si votre bannière utilise l'éditeur par glisser-déposer et inclut un composant de bouton de fermeture, aucun code supplémentaire n'est nécessaire. Lorsqu'un utilisateur clique sur le bouton de fermeture, le message est masqué, déclenche une fermeture, puis enregistre un événement de fermeture pour les analyses.

#### Blocs de code personnalisés

Si votre bannière utilise le bloc éditeur **Code personnalisé**, vous pouvez déclencher une fermeture directement depuis le HTML de la bannière en utilisant `brazeBridge.closeMessage()`.

```html
<button onclick="brazeBridge.closeMessage()">
  Dismiss
</button>
```

#### Fermer une bannière par programmation {#dismiss-a-banner-programmatically}

Si vous utilisez le `BrazeBannerView` standard avec le bouton de fermeture créé dans l'éditeur par glisser-déposer, aucun code supplémentaire n'est nécessaire ; la fermeture est gérée automatiquement.

Pour les intégrations d'interface utilisateur personnalisées, vous pouvez appeler la méthode de fermeture directement sur votre instance Braze pour fermer programmatiquement une bannière et enregistrer un événement de fermeture. La méthode de fermeture peut être appelée plusieurs fois en toute sécurité — le SDK ignore les appels en double pour la même bannière.

Voici les versions minimales du SDK requises pour fermer une bannière par programmation :

{% sdk_min_versions swift:15.1.0 android:42.3.0 web:6.9.0 reactnative:22.0.0 flutter:20.0.0 %}

{% tabs %}
{% tab Web %}
Passez l'objet `Banner` à `braze.dismissBanner()`. Vous pouvez obtenir l'objet `Banner` depuis `braze.getAllBanners()` ou depuis un rappel `subscribeToBannersUpdates`.

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% subtab React %}
```typescript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
Braze.getInstance(context).dismissBanner("your-placement-id");
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
Braze.getInstance(context).dismissBanner("your-placement-id")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}

Utilisez `dismiss()` sur le contexte de la bannière lorsqu'il est disponible. Cette méthode est idempotente et déclenche automatiquement le rappel `onDismiss`. Si le contexte n'est pas disponible, appelez `dismiss(using:)` directement sur la bannière. Les deux méthodes doivent être appelées depuis le thread principal.

```swift
// Preferred: dismiss via context.
banner.context?.dismiss()

// Fallback: if context is unavailable.
banner.dismiss(using: braze)
```

En Objective-C, ces méthodes sont disponibles sous la forme `[banner.context dismiss]` et `[banner dismissUsing:braze]`.

{% endtab %}

{% tab React Native %}
```javascript
Braze.dismissBanner("your-placement-id");
```
{% endtab %}

{% tab Flutter %}
```dart
braze.dismissBanner("your-placement-id");
```
{% endtab %}
{% endtabs %}

### Enregistrer des analyses personnalisées lors de la fermeture d'une bannière {#log-custom-analytics-on-banner-dismissal}

Pour exécuter une logique personnalisée lorsqu'une bannière est fermée — comme l'enregistrement d'analyses — utilisez le rappel de fermeture de votre SDK. Le rappel reçoit un objet événement contenant le `placementId`, le `stableKey` et le `trackingId` de la bannière.

{% tabs %}
{% tab Web %}
Utilisez [`Banner.subscribeToDismissedEvent()`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html#subscribetodismissedevent) pour exécuter une logique personnalisée lorsqu'une bannière spécifique est fermée. Abonnez-vous à l'événement avant d'afficher la bannière.

{% alert note %}
`Banner.subscribeToDismissedEvent()` nécessite le SDK Web 6.9.0 ou ultérieur. Sur les versions antérieures, utilisez `braze.subscribeToBannersUpdates()` et détectez la fermeture en vérifiant si la bannière n'est plus présente dans la carte des bannières mise à jour.
{% endalert %}

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  const banner = banners["global_banner"];

  if (banner) {
    banner.subscribeToDismissedEvent(() => {
      // Run any custom logic here, such as logging custom analytics
      console.log("Banner was dismissed");
    });
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endsubtab %}
{% subtab React %}
```typescript
import { useEffect } from "react";
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    const banner = banners["global_banner"];

    if (banner) {
      banner.subscribeToDismissedEvent(() => {
        // Run any custom logic here, such as logging custom analytics
        console.log("Banner was dismissed");
      });
    }
  });

  braze.requestBannersRefresh(["global_banner"]);

  return () => {
    braze.removeSubscription(subscriptionId);
  };
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
Définissez la propriété facultative [`onDismissCallback`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/on-dismiss-callback.html) sur [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html).

{% subtabs %}
{% subtab Java %}

```java
import android.util.Log;
import com.braze.ui.banners.BannerView;
import kotlin.Unit;

// After obtaining your BannerView instance (for example from XML via findViewById, or `new BannerView(context, "global_banner")`)

bannerView.setOnDismissCallback((snapshot) -> {
  Log.d(TAG, "placementId: " + snapshot.getPlacementId()
    + ", stableKey: " + snapshot.getStableKey()
    + ", trackingId: " + snapshot.getTrackingId());

  // Run any custom logic here, such as logging custom analytics
  return Unit.INSTANCE;
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
import android.util.Log
import com.braze.ui.banners.BannerView

// After obtaining your BannerView instance (for example via findViewById or `BannerView(context, "global_banner")`)

bannerView.onDismissCallback = { snapshot ->
  Log.d(TAG, "placementId: ${snapshot.placementId}, stableKey: ${snapshot.stableKey}, trackingId: ${snapshot.trackingId}")

  // Run any custom logic here, such as logging custom analytics
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}
```swift
// After initializing your banner view instance using UIKit or SwiftUI

bannerView.onDismiss = { event in
  print("Banner dismissed — placementId: \(event.placementId ?? "unknown")")
  print("  stableKey: \(event.stableKey ?? "unknown")")
  print("  trackingId: \(event.trackingId ?? "unknown")")

  // Run any custom logic here, such as logging custom analytics
}
```
{% endtab %}

{% tab React Native %}
Définissez la propriété `onDismiss` sur `Braze.BrazeBannerView` pour exécuter une logique personnalisée lorsqu'une bannière est fermée.

```javascript
import Braze from "@braze/react-native-sdk";

<Braze.BrazeBannerView
  placementId="global_banner"
  onDismiss={(event) => {
    console.log("placementId:", event.placementId, "stableKey:", event.stableKey, "trackingId:", event.trackingId);
    // Run any custom logic here, such as logging custom analytics
  }}
/>
```
{% endtab %}

{% tab Flutter %}
Définissez le paramètre `onDismiss` sur `BrazeBannerView` pour exécuter une logique personnalisée lorsqu'une bannière est fermée.

```dart
BrazeBannerView(
  placementId: 'global_banner',
  onDismiss: (BrazeBannerDismissEvent event) {
    print('placementId: ${event.placementId}, stableKey: ${event.stableKey}, trackingId: ${event.trackingId}');
    // Run any custom logic here, such as logging custom analytics
  },
)
```
{% endtab %}
{% endtabs %}

### Limite de stockage des fermetures en attente {#pending-dismissal-storage-cap}

Les événements de fermeture sont stockés localement en tant qu'entrées en attente jusqu'à ce qu'ils puissent être synchronisés avec le serveur Braze lors du prochain appel `requestBannersRefresh`.

{% alert warning %}
Dans de rares cas où un grand nombre de fermetures s'accumulent sans synchronisation réussie, les fermetures en attente les plus anciennes peuvent être supprimées. Si cela se produit, les bannières précédemment fermées peuvent réapparaître jusqu'à ce que la prochaine synchronisation réussie soit terminée. Pour minimiser ce risque, appelez `requestBannersRefresh` chaque fois que votre application retrouve une connectivité réseau.
{% endalert %}

## Dimensions et taille {#dimensions-and-sizing}

Voici ce que vous devez savoir sur les dimensions et la taille des bannières :

- Bien que le compositeur vous permette de prévisualiser les bannières dans différentes dimensions, cette information n'est pas enregistrée ni envoyée au SDK.
- Le HTML occupera toute la largeur du conteneur dans lequel il est affiché.
- Nous vous recommandons de créer un élément de dimension fixe et de tester ces dimensions dans le compositeur.

## Propriétés personnalisées {#custom-properties}

Vous pouvez utiliser les propriétés personnalisées de votre campagne de bannières pour récupérer des données clé-valeur via le SDK et modifier le comportement ou l'apparence de votre application. Par exemple, vous pourriez :

- Envoyer des métadonnées pour vos analyses ou intégrations tierces.
- Utiliser des métadonnées telles qu'un `timestamp` ou un objet JSON pour déclencher une logique conditionnelle.
- Contrôler le comportement d'une bannière en fonction des métadonnées incluses comme `ratio` ou `format`.

### Conditions préalables

Vous devez [ajouter des propriétés personnalisées]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#custom-properties) à votre campagne de bannières. De plus, voici les versions minimales du SDK requises pour accéder aux propriétés personnalisées :

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Accéder aux propriétés personnalisées {#access-custom-properties}

Pour accéder aux propriétés personnalisées d'une bannière, utilisez l'une des méthodes suivantes en fonction du type de propriété défini dans le tableau de bord. Si la clé ne correspond pas à une propriété de ce type ou n'existe pas, la méthode renvoie `null`.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');

  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');

  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');

  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');

  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');

  // Get the JSON object property
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');

  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}