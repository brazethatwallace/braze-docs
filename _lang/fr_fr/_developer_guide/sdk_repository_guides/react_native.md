---
nav_title: SDK React Native
article_title: Guide du dépôt du SDK React Native
page_order: 7
description: "Référence du README du SDK React Native de Braze, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## À propos du SDK React Native de Braze

Le SDK React Native de Braze connecte vos applications iOS et Android à Braze : profils utilisateur, surfaces d'envoi de messages, analyses et indicateurs de fonctionnalité. Il encapsule les SDK natifs [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) et [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) derrière une API JavaScript.

**L'initialisation est pilotée par JavaScript :** vous configurez la partie native (notifications push, journalisation, délégués) dans les ressources Android et le `AppDelegate` iOS, puis appelez `Braze.initialize(apiKey, endpoint)` depuis JavaScript pour démarrer le SDK. Cela vous donne un contrôle total sur le moment où le SDK s'initialise et avec quelles informations d'identification. Après l'initialisation, appelez les autres méthodes du SDK (par exemple `changeUser`, `logCustomEvent`) selon vos besoins.

### Ce que vous pouvez faire

- **Gestion des utilisateurs** : identifier les utilisateurs, définir les champs de profil, les attributs personnalisés, les alias et les groupes d'abonnement
- **Messages in-app** : interface utilisateur Braze par défaut ou gestion personnalisée via des abonnements et des API de journalisation
- **Content Cards** : flux par défaut, ou récupérer les cartes et créer votre propre interface
- **Bannières** : bannières HTML basées sur des emplacements, y compris `BrazeBannerView`
- **Notifications push** : invites d'autorisation, enregistrement de jetons, écouteurs de payloads (voir les notes par plateforme ci-dessous)
- **Indicateurs de fonctionnalité** : actualiser, lire les propriétés, enregistrer les impressions
- **Analyses** : événements personnalisés, achats, envoi immédiat des données
- **Contrôles du SDK** : activer/désactiver le SDK, effacer les données locales, signatures d'authentification SDK

## Conditions préalables

- **Compte Braze** avec une clé API d'application et un endpoint SDK
- Environnement de développement **React Native** ([configuration de l'environnement React Native](https://reactnative.dev/docs/set-up-your-environment))
- **iOS** : Xcode, CocoaPods (`cd ios && pod install`)
- **Android** : Android Studio / Gradle ; plugin Kotlin Gradle tel que requis par votre modèle React Native
- **Push** (si utilisé) : configuration FCM (Android) et APNs (iOS) selon la [documentation push](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)

Pour l'emplacement des informations d'identification dans le tableau de bord, suivez l'[aperçu de l'intégration](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Installation

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## Démarrage rapide

Cette section présente la configuration minimale requise pour initialiser le SDK React Native de Braze.

1. Installez le package npm (ci-dessus).
2. Effectuez la **configuration native** pour Android et iOS (configuration, autorisations, push si nécessaire).
3. Initialisez le SDK depuis JavaScript et commencez à l'utiliser :

``` typescript
import Braze from "@braze/react-native-sdk";

// Initialize the SDK — call early in your app lifecycle (e.g. in a useEffect).
// The API key and endpoint are passed from JavaScript; native configuration
// (push, logging, etc.) is applied automatically from your native setup.
Braze.initialize("<YOUR_API_KEY>", "<YOUR_SDK_ENDPOINT>");

Braze.changeUser("user-123");
Braze.logCustomEvent("button_clicked", { screen: "home" });
```

Les typages TypeScript sont inclus dans le package (`src/index.d.ts` sur GitHub).

Appeler `Braze.initialize` à nouveau avec des informations d'identification différentes détruit l'instance actuelle et la recrée, prenant en charge la réinitialisation en cours de session.

---

## Configuration native

> **Source de référence :** les écrans étape par étape, les modifications Gradle/CocoaPods et la liste complète des clés XML Android se trouvent dans le [guide développeur React Native de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). Les extraits ci-dessous sont des exemples minimaux.

### Android

- Ajoutez le **plugin Kotlin Gradle** dans votre `build.gradle` racine si votre modèle ne l'inclut pas déjà (les versions dépendent de votre version de React Native).
- Ajoutez un fichier de ressources `braze.xml` dans `res/values` avec votre configuration. Activez l'initialisation différée pour que le SDK attende l'appel de `Braze.initialize()` depuis JavaScript avant de démarrer. Les autres valeurs de configuration (push, délai d'expiration de session, etc.) sont toujours lues depuis ce fichier et appliquées au moment de l'initialisation.
- Assurez-vous que les autorisations de base telles que `INTERNET` et `ACCESS_NETWORK_STATE` sont présentes dans `AndroidManifest.xml`.
- Pour le push, effectuez l'intégration FCM et les indicateurs d'enregistrement / ID d'expéditeur spécifiques à Braze décrits dans la documentation.

``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- Enable delayed initialization so the SDK starts when
       Braze.initialize() is called from JavaScript. -->
  <bool name="com_braze_enable_delayed_initialization">true</bool>

  <!-- Additional native configuration (applied at initialization time) -->
  <bool name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">YOUR_SENDER_ID</string>
</resources>
```

{% alert note %}
** La clé API et l'endpoint ne sont plus définis dans `braze.xml` — ils sont passés depuis JavaScript via `Braze.initialize(apiKey, endpoint)`.
{% endalert %}
### iOS

``` bash
cd ios && pod install
```

Utilisez `BrazeReactInitializer.configure` dans votre `AppDelegate` pour enregistrer la configuration native. Les closures que vous fournissez sont stockées et appliquées ultérieurement lorsque `Braze.initialize(apiKey, endpoint)` est appelé depuis JavaScript.

``` swift
import BrazeKit
import braze_react_native_sdk

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Register native configuration for when JS calls Braze.initialize().
    BrazeReactInitializer.configure { config in
      config.logger.level = .info
      config.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup
    return true
  }
}
```

- **Closure `configure`** : reçoit un `Braze.Configuration` et vous permet de définir les propriétés de configuration native (journalisation, push, sessions, etc.). La clé API et l'endpoint sont fournis depuis JavaScript — vous ne les définissez pas ici.
- **Closure `postInitialization`** *(facultatif)* : reçoit l'instance `Braze` active après sa création, pour les configurations nécessitant l'instance (par ex. stocker une référence, définir des délégués).

{% alert note %}
** `BrazeReactInitializer.configure` est une API Swift-first qui remplace la méthode dépréciée `BrazeReactBridge.initBraze(_:)`. Elle résout également un problème de résolution de type Swift avec `Braze.Configuration` dans le bridge Objective-C.
{% endalert %}
---

## Référence de configuration

Dans React Native, **la configuration est native** : Android lit `res/values/braze.xml`, et iOS utilise les closures enregistrées via **`BrazeReactInitializer.configure`**. Les deux sont appliquées lorsque `Braze.initialize(apiKey, endpoint)` est appelé depuis JavaScript.

### Android (`braze.xml`)

Les valeurs par défaut sont définies en XML ; [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) peut les remplacer au démarrage. La liste officielle des clés et types se trouve dans le [guide d'intégration du SDK Android](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/) et dans [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) (chaque propriété Kotlin correspond à des ressources `com_braze_*` documentées).

Entrées couramment utilisées :

| Clé | Type de ressource | Description |
|-----|-------------------|-------------|
| `com_braze_enable_delayed_initialization` | `bool` | **Requis.** Définir sur `true` pour que le SDK attende l'appel de `Braze.initialize()` depuis JavaScript. |
| `com_braze_api_key` | `string` | Non nécessaire lors de l'utilisation de `Braze.initialize()` depuis JavaScript (les informations d'identification sont passées depuis JS). Requis uniquement pour l'initialisation native héritée. |
| `com_braze_custom_endpoint` | `string` | Non nécessaire lors de l'utilisation de `Braze.initialize()` depuis JavaScript. Requis uniquement pour l'initialisation native héritée. |
| `com_braze_server_target` | `string` | Sélecteur optionnel de cluster / environnement (par ex. certaines builds internes ou de staging). Préférez `com_braze_custom_endpoint` pour la production, sauf si votre intégration Braze spécifie le contraire. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | Lorsque `true`, Braze s'enregistre pour FCM (configuration push typique). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | ID d'expéditeur FCM lorsque l'enregistrement automatique est activé. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Laisser Braze ouvrir automatiquement les liens profonds des notifications push. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | Nombre minimum de secondes entre les actions de déclenchement de messages in-app. |
| **Autre** | *divers* | Clés supplémentaires non listées ici (délai d'expiration de session, géorepérages, localisation, valeurs par défaut des notifications, listes d'autorisation d'appareils, initialisation différée, authentification SDK, etc.). Voir [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) et le [guide d'intégration du SDK Android](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

Définissez les propriétés de configuration native dans la closure `configure` passée à `BrazeReactInitializer.configure`. La closure reçoit une instance `Braze.Configuration` — la clé API et l'endpoint sont définis automatiquement depuis l'appel JavaScript `Braze.initialize`. Détails complets : [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) et les types imbriqués **`api`**, **`push`**, **`logger`**, **`location`**.

| Domaine | Membres (représentatifs) | Notes |
|---------|--------------------------|-------|
| **Informations d'identification** | `api.key`, `api.endpoint` | Définis automatiquement depuis `Braze.initialize(apiKey, endpoint)` en JavaScript. Ne les définissez pas dans la closure `configure`. |
| **Journalisation** | `logger.level` | La journalisation détaillée est destinée au développement ; réduisez le bruit en production. |
| **Push** | `push.automation`, `push.appGroup`, … | L'automatisation simplifie l'enregistrement ; `appGroup` est nécessaire pour Push Stories / extensions lorsqu'elles sont utilisées. |
| **Messages in-app** | `triggerMinimumTimeInterval` | Par défaut **30** secondes entre les déclenchements. |
| **Sessions** | `sessionTimeout` | Inactivité avant une nouvelle session (voir la documentation des sessions Braze). |
| **Confidentialité / données** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | À aligner avec le [manifeste de confidentialité](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/) et les paramètres du produit d'authentification SDK. |
| **Réseau** | `api.requestPolicy`, `api.flushInterval` | Politique de réessai des requêtes et cadence d'envoi. |
| **Abonnement push** | `optInWhenPushAuthorized` | Lorsque `true`, l'abonnement peut passer à « opted-in » après que l'utilisateur a autorisé les notifications. |
| **IAM et changements d'utilisateur** | `preventInAppMessageDisplayForDifferentUser` | Réduit les messages in-app inadaptés si l'ID utilisateur change. |
| **Autre** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | Voir la documentation Swift pour le comportement complet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

Le bridge React Native définit les métadonnées **`api.sdkFlavor`** / SDK spécifiques à React lors de l'initialisation ; ne les remplacez pas sauf si la documentation Braze vous y invite.

---

## API JavaScript / TypeScript

L'export par défaut du package est la classe `Braze` avec des méthodes **statiques** (par exemple `Braze.changeUser`, `Braze.logPurchase`). Les constantes telles que `Braze.Events`, `Braze.Genders` et `Braze.NotificationSubscriptionTypes` sont rattachées au même export.

---

## Fonctionnalités principales

### Gestion des utilisateurs

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

**Authentification SDK** optionnelle : passez une signature comme second argument à `changeUser`, ou appelez `Braze.setSdkAuthenticationSignature(signature)` lorsque cette fonctionnalité est activée dans le tableau de bord.

### Messages in-app

- Avec l'**interface Braze par défaut**, suivez la [documentation des messages in-app](https://www.braze.com/docs/developer_guide/in_app_messages?sdktab=react%20native) ; vous n'avez généralement **pas** besoin d'appeler `subscribeToInAppMessage` uniquement pour afficher l'interface par défaut.
- Pour une gestion **personnalisée**, abonnez-vous avec `useBrazeUI: false`, puis enregistrez les impressions/clics selon vos besoins :

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getContentCards();
Braze.requestContentCardsRefresh();
Braze.launchContentCards(); // default Braze UI

Braze.logContentCardImpression(cardId);
Braze.logContentCardClicked(cardId);
```

Écoutez les mises à jour avec `Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, ...)`.

### Bannières

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.requestBannersRefresh(["homepage_banner"]);
const banner = await Braze.getBanner("homepage_banner");

// Or use the native Banner view:
// <Braze.BrazeBannerView placementID="homepage_banner" />
```

### Notifications push

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`** : à utiliser lorsque l'application s'ouvre depuis une notification pour éviter les conditions de concurrence avec `Linking` de RN ; nécessite des hooks natifs (`BrazeReactUtils` sur iOS, `BrazeReactUtils.populateInitialPushPayloadFromIntent` sur Android) comme décrit dans les commentaires de la documentation TypeScript et l'application exemple.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`** est **réservé à Android** selon les typages publics.

### Indicateurs de fonctionnalité

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### Analyses et achats

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

Remarque : `logPurchase` prend le **prix sous forme de chaîne de caractères** (voir les typages).

### Gestion des données et état du SDK

**`changeUser`** indique uniquement à Braze quel ID utilisateur attribuer à la **nouvelle** activité. Il **n'efface pas** les données SDK mises en cache sur l'appareil. Il n'existe pas d'API « déconnexion » distincte : si vous avez besoin d'une déconnexion traditionnelle (effacer l'état local de Braze pour que le profil, les messages et les jetons mis en cache de l'utilisateur précédent soient supprimés de cette installation), vous utilisez généralement **`wipeData()`**. Il s'agit d'une réinitialisation locale complète.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — Efface les données **locales** de Braze pour cette installation (état utilisateur/session/carte mis en cache, association de jeton push, etc.). À utiliser pour un comportement de type **déconnexion** lorsque vous ne devez pas laisser l'état Braze de l'utilisateur précédent sur l'appareil, ainsi que pour les demandes **« supprimer mes données sur cet appareil »**, les réinitialisations **QA** sans réinstallation, ou les flux de **confidentialité** stricts. **`changeUser`** seul n'effectue pas ce nettoyage — il définit uniquement quel ID utilisateur reçoit les **nouveaux** événements. Sur **iOS**, le comportement peut différer d'Android (par ex. interaction avec l'état SDK désactivé) ; consultez la documentation native de Braze si vous utilisez cela en production.

**`disableSDK()`** — Arrête le fonctionnement du SDK (aucune collecte/transmission telle que configurée). À utiliser pour les bascules d'**opt-out utilisateur**, les **modes restreints** (conformité, paramètres enfants), ou le **débogage** sans supprimer la dépendance.

**`enableSDK()`** — Réactive le SDK après **`disableSDK()`**. Sur **iOS**, la réactivation peut **ne pas s'appliquer** avant le **prochain lancement de l'application** ; vérifiez dans la documentation Braze Swift/iOS avant de compter sur une réactivation immédiate.

---

## Événements

Abonnez-vous avec `Braze.addListener(event, callback)`. L'appel retourne un objet d'abonnement ; appelez **`.remove()`** dessus pour arrêter l'écoute.

**Configurer un écouteur :**

``` typescript
import Braze from "@braze/react-native-sdk";

const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (update) => {
    console.log("Content cards:", update.cards);
  }
);
```

**Supprimer l'écouteur :**

``` typescript
subscription.remove();
```

Dans un composant React, stockez l'abonnement et appelez `.remove()` dans votre nettoyage (par ex. le retour d'un `useEffect`) :

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| Constante d'événement | Payload (résumé) |
|------------------------|------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | Dernières Content Cards |
| `Braze.Events.BANNER_CARDS_UPDATED` | Dernières bannières |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | Tableau d'indicateurs de fonctionnalité |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | Événement de message in-app |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | Détails de l'erreur d'authentification SDK |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | Payload push (**Android uniquement**) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements" }

---

## Notes d'intégration

- **Expo** : utilisez le [plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin) pour éviter le câblage natif manuel dans la mesure du possible.
- **Nouvelle architecture / Turbo Modules** : pris en charge sur les versions récentes du plugin ; suivez le guide développeur et les paramètres `AppDelegate` / Gradle de l'application exemple si vous migrez.
- **Confidentialité (iOS)** : des méthodes telles que `updateTrackingPropertyAllowList` prennent en charge la configuration liée au manifeste de confidentialité ; voir le [manifeste de confidentialité Swift](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/).
- **Jest** : simulez les modules natifs `react-native` ou le Turbo module Braze (voir `__tests__/jest.setup.js` dans ce dépôt pour des exemples).

## Compatibilité des versions

{% alert note %}
Ce SDK a été testé avec React Native version **0.85.3**.
{% endalert %}
Le tableau suivant répertorie les versions de React Native prises en charge par version du plugin Braze.

| Plugin Braze | React Native | Nouvelle architecture |
|--------------|--------------|----------------------|
| 9.0.0+       | ≥ 0.71       | Oui                  |
| 6.0.0+       | ≥ 0.68       | Oui (≥ 0.70.0)      |
| 2.0.0+       | ≥ 0.68       | Oui                  |
| ≤ 1.41.0     | ≤ 0.71       | Non                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Compatibilité des versions" }

Respectez également les exigences des SDK natifs :

- [Informations de version du SDK Android](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Informations de version du SDK Swift](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Plugin Braze Expo

Pour les workflows gérés par Expo, consultez le [dépôt du plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin).

---

## Application exemple

`BrazeProject` dans ce dépôt est un exemple complet (gestion des utilisateurs, Content Cards, indicateurs de fonctionnalité, bannières, etc.).

``` bash
cd BrazeProject/
yarn install
npx react-native start
```

**iOS** (depuis `BrazeProject`) :

``` bash
cd ios && pod install && cd ..
npx react-native run-ios
```

Utilisez `RCT_NEW_ARCH_ENABLED=0 pod install` si vous avez besoin de l'architecture héritée.

**Android** (depuis `BrazeProject`) :

``` bash
npx react-native run-android
```

---

## Débogage et résolution des problèmes

Activez la journalisation Braze dans la configuration **native** pendant le développement pour que le SDK écrive dans la console système (Xcode / Android Logcat). Cela permet de vérifier l'initialisation, les changements d'utilisateur et la distribution des événements.

- **iOS** — Dans la closure `configure` passée à `BrazeReactInitializer.configure`, définissez `config.logger.level = .debug` (ou `.info`). Réduisez ou désactivez en production pour que les journaux ne soient pas visibles par les utilisateurs.
- **Android** — Utilisez la ressource `com_braze_logger_initial_log_level` dans `braze.xml` ou définissez l'équivalent sur `BrazeConfig.Builder` (voir [BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)). Utilisez un niveau non détaillé ou supprimez le remplacement avant la mise en production.

Pour une résolution des problèmes plus approfondie (réseau, session ou comportement de campagne), consultez le [guide développeur React Native de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native) et la documentation des SDK natifs ([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)).

---

## Ressources supplémentaires

- [Guide développeur Braze — React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)
- [Notifications push — React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)
- [Dépôt GitHub](https://github.com/braze-inc/braze-react-native-sdk)
- [Package npm](https://www.npmjs.com/package/@braze/react-native-sdk)

## Contact

Si vous avez des questions, veuillez contacter [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les projets exemples, consultez [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk).