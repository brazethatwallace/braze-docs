---
nav_title: SDK React Native
article_title: Guide du dépôt du SDK React Native
page_order: 7
description: "Référence du README du SDK React Native de Braze, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guide du dépôt du SDK React Native {#react-native-sdk-repository-guide}

## À propos du SDK Braze React Native

Le SDK Braze React Native connecte vos applications iOS et Android à Braze : profils utilisateur, surfaces de communication, analyses et feature flags. Il encapsule le [SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk) natif et le [SDK Braze Android](https://github.com/braze-inc/braze-android-sdk) natif derrière une API JavaScript.

**L'initialisation est pilotée par JavaScript :** vous configurez les éléments natifs (notifications push, journalisation, délégués) dans les ressources Android et le fichier `AppDelegate` iOS, puis vous appelez `Braze.initialize(apiKey, endpoint)` depuis JavaScript pour démarrer le SDK. Cela vous donne un contrôle total sur le moment où le SDK s'initialise et avec quels identifiants. Après l'initialisation, appelez les autres méthodes du SDK (par exemple `changeUser`, `logCustomEvent`) selon vos besoins.

### Ce que vous pouvez faire

- **Gestion des utilisateurs** : identifier les utilisateurs, définir les champs de profil, les attributs personnalisés, les alias et les groupes d'abonnement
- **Messages in-app** : interface utilisateur Braze par défaut ou gestion personnalisée via des abonnements et des API de journalisation
- **Content Cards** : flux par défaut, ou récupération des cartes pour créer votre propre interface
- **Bannières** : bannières HTML basées sur les emplacements, y compris `BrazeBannerView`
- **Notifications push** : demandes d'autorisation, enregistrement de jetons, écouteurs de payload (voir les notes spécifiques à chaque plateforme dans **Configuration native**)
- **Feature flags** : actualisation, lecture des propriétés, journalisation des impressions
- **Analyses** : événements personnalisés, achats, envoi immédiat
- **Contrôles du SDK** : activer/désactiver le SDK, effacer les données locales, signatures SDK Authentication

## Conditions préalables

- **Compte Braze** avec une clé API d'application et un endpoint SDK
- Environnement de développement **React Native** ([configuration de l'environnement React Native](https://reactnative.dev/docs/set-up-your-environment))
- **iOS** : Xcode, CocoaPods (`cd ios && pod install`)
- **Android** : Android Studio / Gradle ; plugin Kotlin Gradle tel que requis par votre modèle React Native
- **Notifications push** (si utilisées) : configuration FCM (Android) et APNs (iOS) conformément à la [documentation sur les notifications push](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)

Pour localiser les identifiants dans le tableau de bord, consultez l'[aperçu de l'intégration](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Installation

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## Démarrage rapide

Cette section présente la configuration minimale requise pour initialiser le SDK React Native de Braze.

1. Installez le package npm (dans **Installation**).
2. Effectuez la **configuration native** pour Android et iOS (configuration, autorisations, notifications push si nécessaire).
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

Appeler `Braze.initialize` une seconde fois avec des identifiants différents détruit l'instance en cours et en crée une nouvelle, permettant ainsi une réinitialisation en cours de session.

---

## Configuration native

> **Source de référence :** Les écrans étape par étape, les modifications Gradle/CocoaPods et la liste complète des clés XML Android se trouvent dans le [guide développeur React Native de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). Les extraits de cette section sont des exemples minimaux.

### Android

- Ajoutez le **plugin Kotlin Gradle** dans votre fichier racine `build.gradle` si votre modèle ne l'inclut pas déjà (les versions dépendent de votre version de React Native).
- Ajoutez un fichier de ressource `braze.xml` dans `res/values` avec votre configuration. Activez l'initialisation différée afin que le SDK attende l'appel de `Braze.initialize()` depuis JavaScript avant de démarrer. Les autres valeurs de configuration (notifications push, délai d'expiration de session, etc.) sont toujours lues depuis ce fichier et appliquées au moment de l'initialisation.
- Assurez-vous que les permissions de base telles que `INTERNET` et `ACCESS_NETWORK_STATE` sont présentes dans `AndroidManifest.xml`.
- Pour les notifications push, complétez l'intégration FCM ainsi que les indicateurs d'ID d'expéditeur / d'enregistrement spécifiques à Braze décrits dans la documentation.

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
** La clé API et l'endpoint ne sont plus définis dans `braze.xml` — ils sont transmis depuis JavaScript via `Braze.initialize(apiKey, endpoint)`.
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

- **Closure `configure`** : reçoit un objet `Braze.Configuration` et vous permet de définir les propriétés de configuration native (journalisation, notifications push, sessions, etc.). La clé API et l'endpoint sont fournis depuis JavaScript — vous ne les définissez pas ici.
- **Closure `postInitialization`** *(facultative)* : reçoit l'instance `Braze` active après sa création, pour les configurations nécessitant l'instance (par exemple, stocker une référence, définir des délégués).

{% alert note %}
** `BrazeReactInitializer.configure` est une API Swift-first qui remplace la méthode dépréciée `BrazeReactBridge.initBraze(_:)`. Elle résout également un problème de résolution de type Swift avec `Braze.Configuration` dans le bridge Objective-C.
{% endalert %}
---

## Référence de configuration

Dans React Native, **la configuration est native** : Android lit `res/values/braze.xml`, et iOS utilise des closures enregistrées via **`BrazeReactInitializer.configure`**. Les deux sont appliquées lorsque `Braze.initialize(apiKey, endpoint)` est appelé depuis JavaScript.

### Android (`braze.xml`)

Les valeurs par défaut sont définies en XML ; [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) peut les remplacer au démarrage. La liste officielle des clés et des types se trouve dans le [guide d'intégration du SDK Android](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/) et dans [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) (chaque propriété Kotlin correspond aux ressources documentées `com_braze_*`).

Entrées couramment utilisées :

| Clé | Type de ressource | Description |
|-----|-------------------|-------------|
| `com_braze_enable_delayed_initialization` | `bool` | **Obligatoire.** Définir sur `true` pour que le SDK attende `Braze.initialize()` depuis JavaScript. |
| `com_braze_api_key` | `string` | Non nécessaire lorsque vous utilisez `Braze.initialize()` depuis JavaScript (les identifiants sont transmis depuis JS). Requis uniquement pour l'initialisation native héritée. |
| `com_braze_custom_endpoint` | `string` | Non nécessaire lorsque vous utilisez `Braze.initialize()` depuis JavaScript. Requis uniquement pour l'initialisation native héritée. |
| `com_braze_server_target` | `string` | Sélecteur optionnel de cluster / environnement (par ex. certains builds internes ou de staging). Préférez `com_braze_custom_endpoint` en production, sauf indication contraire de votre intégration Braze. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | Lorsque défini sur `true`, Braze s'enregistre auprès de FCM (configuration push classique). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | ID d'expéditeur FCM lorsque l'enregistrement automatique est activé. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Permet à Braze d'ouvrir automatiquement les deep links de notification push. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | Nombre minimum de secondes entre les actions de déclenchement de messages in-app. |
| **Autres** | *divers* | Clés supplémentaires non répertoriées ici (délai d'expiration de session, géorepérages, emplacement, paramètres par défaut des notifications, listes d'autorisation d'appareils, initialisation différée, authentification SDK, etc.). Consultez [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) et le [guide d'intégration du SDK Android](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

Définissez les propriétés de configuration natives dans la closure `configure` transmise à `BrazeReactInitializer.configure`. La closure reçoit une instance de `Braze.Configuration` — la clé API et l'endpoint sont définis automatiquement à partir de l'appel JavaScript `Braze.initialize`. Détails complets : [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) et les types imbriqués **`api`**, **`push`**, **`logger`**, **`location`**.

| Domaine | Membres (représentatifs) | Notes |
|---------|--------------------------|-------|
| **Identifiants** | `api.key`, `api.endpoint` | Définis automatiquement à partir de `Braze.initialize(apiKey, endpoint)` en JavaScript. Ne les définissez pas dans la closure `configure`. |
| **Journalisation** | `logger.level` | La journalisation détaillée est destinée au développement ; réduisez le bruit en production. |
| **Push** | `push.automation`, `push.appGroup`, … | L'automatisation simplifie l'enregistrement ; `appGroup` est nécessaire pour les Push Stories / extensions lorsqu'ils sont utilisés. |
| **Messages in-app** | `triggerMinimumTimeInterval` | Par défaut, **30** secondes entre les déclenchements. |
| **Sessions** | `sessionTimeout` | Durée d'inactivité avant une nouvelle session (voir la documentation Braze sur les sessions). |
| **Confidentialité / données** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | À aligner avec le [manifeste de confidentialité](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/) et les paramètres du produit d'authentification SDK. |
| **Réseau** | `api.requestPolicy`, `api.flushInterval` | Politique de nouvelle tentative de requête et cadence d'envoi. |
| **Abonnement push** | `optInWhenPushAuthorized` | Lorsque défini sur `true`, l'abonnement peut passer à « opt-in » après que l'utilisateur a autorisé les notifications. |
| **Messages in-app et changements d'utilisateur** | `preventInAppMessageDisplayForDifferentUser` | Réduit les messages in-app non concordants si l'identifiant utilisateur change. |
| **Autres** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | Consultez la documentation Swift pour le comportement complet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

Le pont React Native définit les métadonnées **`api.sdkFlavor`** / SDK spécifiques à React lors de l'initialisation ; ne les remplacez pas, sauf si la documentation Braze vous y invite.

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

**Authentification SDK** optionnelle : passez une signature comme deuxième argument de `changeUser`, ou appelez `Braze.setSdkAuthenticationSignature(signature)` lorsque cette option est activée dans le tableau de bord.

### Messages in-app

- Avec l'**interface utilisateur Braze par défaut**, suivez la [documentation des messages in-app](https://www.braze.com/docs/developer_guide/in_app_messages?sdktab=react%20native) ; en général, vous n'avez **pas** besoin d'appeler `subscribeToInAppMessage` uniquement pour afficher l'interface par défaut.
- Pour un traitement **personnalisé**, abonnez-vous avec `useBrazeUI: false`, puis enregistrez les impressions/clics selon vos besoins :

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getCachedContentCards();
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
// <Braze.BrazeBannerView placementId="homepage_banner" />
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

- **`getInitialPushPayload`** : à utiliser lorsque l'application s'ouvre depuis une notification afin d'éviter les conditions de concurrence RN `Linking` ; nécessite des hooks natifs (`BrazeReactUtils` sur iOS, `BrazeReactUtils.populateInitialPushPayloadFromIntent` sur Android) comme décrit dans les commentaires de documentation TypeScript et l'application d'exemple.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`** est disponible **uniquement sur Android** d'après les typages publics.

### Feature flags

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### Analyse et achats

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

Remarque : `logPurchase` attend le **prix sous forme de chaîne de caractères** (voir les typages).

### Gestion des données et état du SDK

**`changeUser`** indique uniquement à Braze quel identifiant utilisateur doit recevoir la **nouvelle** activité. Cette méthode n'efface **pas** les données SDK en cache sur l'appareil. Il n'existe pas d'API distincte de « déconnexion » : si vous avez besoin d'une déconnexion classique (effacer l'état local Braze afin que le profil, les messages et les jetons en cache de l'utilisateur précédent ne soient plus présents sur cette installation), vous utilisez généralement **`wipeData()`**. Il s'agit d'une réinitialisation locale complète.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — Efface les données **locales** de Braze pour cette installation (état de l'utilisateur/session/cartes en cache, association du jeton push, etc.). À utiliser pour un comportement de type **déconnexion** lorsque vous ne devez pas laisser l'état Braze de l'utilisateur précédent sur l'appareil, ainsi que pour les scénarios **« supprimer mes données sur cet appareil »**, les réinitialisations **QA** sans réinstallation ou les flux de **confidentialité** stricts. **`changeUser`** seul n'effectue pas ce nettoyage — il définit uniquement quel identifiant utilisateur reçoit les **nouveaux** événements. Sur **iOS**, le comportement peut différer d'Android (par exemple, l'interaction avec l'état du SDK désactivé) ; consultez la documentation native de Braze si vous utilisez cette fonctionnalité en production.

**`disableSDK()`** — Arrête le fonctionnement du SDK (aucune collecte/transmission selon la configuration). À utiliser pour les bascules de **refus de l'utilisateur**, les **modes restreints** (conformité, paramètres enfants) ou le **débogage** sans supprimer la dépendance.

**`enableSDK()`** — Réactive le SDK après un appel à **`disableSDK()`**. Sur **iOS**, la réactivation peut **ne pas s'appliquer** avant le **prochain lancement de l'application** ; vérifiez dans la documentation Braze Swift/iOS avant de compter sur une réactivation immédiate.

---

## Événements

Abonnez-vous avec `Braze.addListener(event, callback)`. L'appel renvoie un objet d'abonnement ; appelez **`.remove()`** sur celui-ci pour arrêter l'écoute.

**Mise en place d'un écouteur :**

``` typescript
import Braze from "@braze/react-native-sdk";

const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (update) => {
    console.log("Content cards:", update.cards);
  }
);
```

**Suppression de l'écouteur :**

``` typescript
subscription.remove();
```

Dans un composant React, stockez l'abonnement et appelez `.remove()` dans votre nettoyage (par exemple, le retour d'un `useEffect`) :

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| Constante d'événement | Payload (résumé) |
|----------------|-------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | Dernières Content Cards |
| `Braze.Events.BANNER_CARDS_UPDATED` | Dernières bannières |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | Tableau de feature flags |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | Événement de message in-app |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | Détails de l'erreur d'authentification SDK |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | Payload de notification push (**Android uniquement**) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Événements" }

---

## Notes d'intégration

- **Expo** : utilisez le [plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin) pour éviter autant que possible le câblage natif manuel.
- **Nouvelle architecture / Turbo Modules** : pris en charge dans les versions récentes du plugin ; suivez le guide développeur et les exemples de configuration `AppDelegate` / Gradle si vous effectuez la migration.
- **Confidentialité (iOS)** : des méthodes telles que `updateTrackingPropertyAllowList` prennent en charge la configuration liée au manifeste de confidentialité ; consultez le [manifeste de confidentialité Swift](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/).

- **Jest** : simulez les modules natifs `react-native` ou le module Braze Turbo (consultez `__tests__/jest.setup.js` dans ce dépôt pour des exemples de configuration).

## Prise en charge des versions

{% alert note %}
Ce SDK a été testé avec la version **0.85.3** de React Native.
{% endalert %}
Le tableau suivant répertorie les versions de React Native prises en charge par version du plugin Braze.

| Plugin Braze | React Native | Nouvelle architecture |
|--------------|--------------|------------------|
| 9.0.0+       | ≥ 0.71       | Oui              |
| 6.0.0+       | ≥ 0.68       | Oui (≥ 0.70.0)   |
| 2.0.0+       | ≥ 0.68       | Oui              |
| ≤ 1.41.0     | ≤ 0.71       | Non               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prise en charge des versions" }

Respectez également les exigences des SDK natifs :

- [Informations sur les versions du SDK Android](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Informations sur les versions du SDK Swift](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Plugin Braze Expo

Pour les workflows gérés par Expo, consultez le [dépôt du plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin).

---

## Application d'exemple

`BrazeProject` dans ce dépôt est un exemple complet (gestion des utilisateurs, Content Cards, feature flags, bannières, etc.).

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

Activez la journalisation Braze dans la configuration **native** pendant le développement afin que le SDK écrive dans la console système (Xcode / Android Logcat). Cela permet de vérifier l'initialisation, les changements d'utilisateur et la distribution des événements.

- **iOS** — Dans la closure `configure` passée à `BrazeReactInitializer.configure`, définissez `config.logger.level = .debug` (ou `.info`). Réduisez ou désactivez ce niveau en production pour que les journaux ne soient pas visibles par les utilisateurs.
- **Android** — Utilisez la ressource `com_braze_logger_initial_log_level` dans `braze.xml` ou définissez l'équivalent sur `BrazeConfig.Builder` (voir [BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)). Utilisez un niveau non verbeux ou supprimez la surcharge avant la mise en production.

Pour une résolution des problèmes plus approfondie (réseau, session ou comportement des Campaigns), consultez le [guide du développeur Braze React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native) et la documentation des SDK natifs ([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)).

---

## Ressources supplémentaires

- [Guide développeur Braze — React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)
- [Notifications push — React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)
- [Dépôt GitHub](https://github.com/braze-inc/braze-react-native-sdk)
- [Package npm](https://www.npmjs.com/package/@braze/react-native-sdk)

## Contact

Pour toute question, contactez le support technique de Braze pour obtenir de l'aide.
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les exemples de projets, consultez [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk).