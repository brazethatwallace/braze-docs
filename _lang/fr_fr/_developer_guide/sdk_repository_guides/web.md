---
nav_title: SDK Web
article_title: Guide du dépôt du SDK Web
page_order: 1
description: "Référence du README du SDK Web de Braze, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guide du dépôt du SDK Web {#web-sdk-repository-guide}

## À propos du SDK Web de Braze {#about-the-braze-web-sdk}

Le SDK Web de Braze vous permet d'intégrer la plateforme d'engagement client de Braze directement dans vos applications Web. Conçu avec TypeScript et pensé pour le développement Web moderne, ce SDK fournit des outils complets pour la gestion des utilisateurs, l'envoi de messages, l'analytique et les feature flags.

### Ce que vous pouvez faire {#what-you-can-do}

- **Gestion des utilisateurs** : suivez et gérez les identités, les attributs et le comportement des utilisateurs dans votre application Web
- **In-App Messages** : affichez des messages et notifications ciblés aux utilisateurs pendant qu'ils utilisent activement votre site
- **Content Cards** : affichez des flux de contenu personnalisés et des cartes promotionnelles qui se mettent à jour en temps réel
- **Bannières** : affichez des messages sous forme de bannières dans des emplacements spécifiques de votre site
- **Notifications push** : envoyez des notifications push Web pour engager les utilisateurs même lorsqu'ils ne sont pas sur votre site
- **Feature flags** : contrôlez le déploiement des fonctionnalités et les tests A/B grâce à la gestion des feature flags côté serveur
- **Analytique** : suivez les événements personnalisés, les interactions utilisateur et les indicateurs de conversion
- **Gestion des sessions** : surveillez les sessions utilisateur et les schémas d'engagement

Que vous développiez une application monopage, un site e-commerce ou une plateforme de contenu, le SDK Web de Braze fournit les outils nécessaires pour créer des expériences utilisateur personnalisées et engageantes qui favorisent la croissance et la fidélisation.

## Conditions préalables {#prerequisites}

Avant d'intégrer le SDK Web de Braze, vous aurez besoin de :

{% multi_lang_include developer_guide/sdk_api_prerequisites.md %}

### Obtenir vos identifiants {#getting-your-credentials}

1. **Clé API** : disponible dans votre tableau de bord de Braze sous **Paramètres** > **Clés API**
2. **Endpoint du SDK** : disponible dans **Paramètres** > **Authentification SDK** > **Endpoints**
3. **Service worker** : requis pour les notifications push (voir la section Notifications push)

## Installation {#installation}

``` bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

## Démarrage rapide {#quick-start}

L'extrait suivant montre la configuration minimale requise pour initialiser le SDK Web de Braze.

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});

braze.changeUser('Jane Doe');
```

## Référence de configuration {#configuration-reference}

### Options d'initialisation {#initialization-options}

La fonction `initialize` accepte un objet d'options avec les propriétés suivantes :

| Option | Type | Par défaut | Description |
|--------|------|------------|-------------|
| `baseUrl` | `string` | **Requis** | Cette option est requise pour configurer le SDK Web de Braze afin d'utiliser l'endpoint approprié pour votre intégration — par exemple : `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | Définissez sur true pour activer la journalisation par défaut. Notez que cela amènera Braze à écrire dans la console JavaScript, visible par tous les utilisateurs ! Vous devriez probablement supprimer cette option ou fournir un logger alternatif avec setLogger avant de mettre votre page en production. |
| `allowUserSuppliedJavascript` | `boolean` | `false` | Par défaut, le SDK Web de Braze n'autorise pas les actions de clic JavaScript fournies par l'utilisateur, ni les messages in-app HTML et les bannières, car ils permettent aux utilisateurs du tableau de bord de Braze d'exécuter du JavaScript sur votre site. Pour indiquer que vous faites confiance aux utilisateurs du tableau de bord de Braze pour écrire des actions de clic JavaScript non malveillantes, définissez cette propriété sur true. |
| `doNotLoadFontAwesome` | `boolean` | `false` | Braze utilise Font Awesome pour les icônes des messages in-app. Par défaut, Braze charge automatiquement FontAwesome 4.7.0 depuis le CDN FontAwesome. Pour désactiver ce comportement (par exemple, parce que votre site utilise une version personnalisée de FontAwesome), définissez cette option sur `true`. Notez que si vous faites cela, vous êtes responsable de vous assurer que FontAwesome est chargé sur votre site — sinon les messages in-app pourraient ne pas s'afficher correctement. |
| `inAppMessageZIndex` | `number` | `999999` | Par défaut, le SDK Braze affiche les In-App Messages avec un z-index de 999999. Fournissez une valeur pour cette option afin de remplacer cette valeur par défaut. |
| `sessionTimeoutInSeconds` | `number` | `30` | Par défaut, une session expire après 30 secondes d'inactivité. Fournissez une valeur pour cette option afin de remplacer cette valeur par défaut. |
| `deviceId` | `string` | Généré automatiquement | Par défaut, Braze attribue un GUID aléatoire comme identifiant d'appareil. Fournissez une valeur pour cette option de configuration afin de remplacer cette valeur par défaut par une valeur de votre choix. |
| `appVersion` | `string` | `undefined` | Si vous fournissez une valeur pour cette option, les événements utilisateur envoyés à Braze seront associés à la version donnée, qui peut être utilisée pour la segmentation des utilisateurs. |
| `appVersionNumber` | `string` | `undefined` | Une valeur numérique de version d'application qui peut être utilisée pour la segmentation des utilisateurs. Cette valeur doit être envoyée avec quatre champs, tels que « 1.2.3.4 », sinon elle sera ignorée. Remarque : `appVersion` doit également être défini, soit avec la même valeur, soit avec un nom unique pour cette version. |
| `contentSecurityNonce` | `string` | `undefined` | Si vous fournissez une valeur pour cette option, le SDK Braze ajoutera le nonce à tous les éléments `<script>` et `<style>` créés par le SDK. Cela peut être utilisé pour permettre au SDK Braze de fonctionner avec la politique de sécurité du contenu de votre site Web. Notez qu'en plus de définir ce nonce, vous devrez peut-être également autoriser le chargement de FontAwesome, ce que vous pouvez faire en ajoutant `use.fontawesome.com` à la liste d'autorisation de votre politique de sécurité du contenu ou en utilisant l'option `doNotLoadFontAwesome` et en le chargeant manuellement. |
| `noCookies` | `boolean` | `false` | Par défaut, le SDK Web de Braze utilise des cookies. Pour désactiver l'utilisation des cookies, définissez cette option sur true. Notez que la désactivation des cookies peut affecter la capacité du SDK à mémoriser les identités des utilisateurs entre les sessions. |
| `allowCrawlerActivity` | `boolean` | `false` | Par défaut, le SDK Web de Braze ignore l'activité des robots d'indexation ou des crawlers Web connus, tels que Google, en se basant sur la chaîne user agent. Cela économise des points de donnée, rend l'analytique plus précise et peut améliorer le classement de la page. Cependant, si vous souhaitez que Braze enregistre l'activité de ces crawlers, vous pouvez définir cette option sur true. |
| `disablePushTokenMaintenance` | `boolean` | `false` | Par défaut, les utilisateurs qui ont déjà accordé l'autorisation de notification push Web (par exemple via requestPushPermission ou depuis un fournisseur de push précédent) synchroniseront automatiquement leur jeton de notification push avec le backend de Braze lors d'une nouvelle session pour garantir la livrabilité. Pour désactiver ce comportement, définissez cette option sur true. |
| `enableSdkAuthentication` | `boolean` | `false` | Définissez sur true pour activer la fonctionnalité d'authentification SDK. Pour plus d'informations sur l'authentification SDK, consultez notre documentation produit. |
| `manageServiceWorkerExternally` | `boolean` | `false` | Par défaut, le SDK Web de Braze gère son propre service worker pour les notifications push. Si vous gérez déjà un service worker dans votre application et souhaitez y intégrer la fonctionnalité du service worker de Braze, définissez cette option sur true et incluez le code du service worker de Braze dans votre fichier de service worker. |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | Par défaut, les actions de déclenchement (par exemple, l'affichage d'un message in-app) peuvent être déclenchées au maximum une fois toutes les 30 secondes par utilisateur. Fournissez une valeur pour cette option afin de remplacer cette valeur par défaut. |
| `serviceWorkerLocation` | `string` | `undefined` | Par défaut, le SDK Web de Braze recherche son fichier de service worker à la racine de votre domaine. Fournissez une valeur pour cette option afin de remplacer cette valeur par défaut et spécifier un emplacement personnalisé pour le fichier de service worker. |
| `safariWebsitePushId` | `string` | `undefined` | Requis pour les notifications push Safari. Cette valeur se trouve dans votre compte Apple Developer. Pour plus d'informations sur la configuration des notifications push Safari, consultez notre documentation produit. |
| `localization` | `string` | `undefined` | Si vous fournissez une valeur pour cette option, le SDK Braze tentera d'afficher les messages in-app et les Content Cards dans cette langue. |
| `openInAppMessagesInNewTab` | `boolean` | `false` | Par défaut, les liens dans les messages in-app s'ouvrent dans le même onglet. Définissez cette option sur true pour les ouvrir dans un nouvel onglet. |
| `openCardsInNewTab` | `boolean` | `false` | Par défaut, les liens dans les Content Cards s'ouvrent dans le même onglet. Définissez cette option sur true pour les ouvrir dans un nouvel onglet. |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | Par défaut, les messages in-app peuvent être fermés en cliquant en dehors d'eux ou en appuyant sur la touche Échap. Définissez cette option sur true pour exiger que les utilisateurs cliquent explicitement sur un bouton de fermeture ou un bouton d'action pour fermer le message. |
| `devicePropertyAllowlist` | `string[]` | `undefined` | Par défaut, le SDK Braze détecte et collecte automatiquement toutes les propriétés d'appareil dans DeviceProperties. Pour remplacer ce comportement, fournissez un tableau de DeviceProperties. Pour désactiver l'envoi de toutes les propriétés aux serveurs de Braze, fournissez un tableau vide. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, sans le fuseau horaire, la distribution selon le fuseau horaire local ne fonctionnera pas. |
| `serviceWorkerScope` | `string` | `undefined` | Par défaut, le SDK Web de Braze enregistre son service worker avec la portée par défaut (le répertoire du service worker). Fournissez une valeur pour cette option afin de remplacer cette valeur par défaut et spécifier une portée personnalisée pour le service worker. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Options d'initialisation" }

---

## Fonctionnalités principales {#core-features}

### Initialisation et configuration {#initialization-setup}

#### Initialisation de base {#basic-initialization}

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: 'YOUR-SDK-ENDPOINT-HERE',
    enableLogging: true // Remove in production
});

// Start a session
braze.openSession();
```

#### Options d'initialisation avancées {#advanced-initialization-options}

``` typescript
import * as braze from "@braze/web-sdk";

braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: 'YOUR-SDK-ENDPOINT-HERE',
    enableLogging: true,
    allowUserSuppliedJavascript: true,
    doNotLoadFontAwesome: false,
    inAppMessageZIndex: 999999,
    sessionTimeoutInSeconds: 30,
    deviceId: 'custom-device-id',
    appVersion: '1.0.0',
    contentSecurityNonce: 'your-nonce-here'
});
```

### Gestion des utilisateurs {#user-management}

#### Changer d'utilisateur {#change-user}

``` typescript
import { changeUser } from "@braze/web-sdk";

// Change to a new user
changeUser('user-123');
```

#### Définir les attributs utilisateur {#set-user-attributes}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    user.setEmail('user@example.com');
    user.setFirstName('John');
    user.setLastName('Doe');
    user.setCustomUserAttribute('subscription_tier', 'premium');
    user.setCustomUserAttribute('last_login', new Date());
}
```

#### Définir la localisation de l'utilisateur {#set-user-location}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    user.setCountry('US');
    user.setHomeCity('San Francisco');
    user.setLanguage('en');
    user.setCustomLocationAttribute('latitude', 37.7749);
    user.setCustomLocationAttribute('longitude', -122.4194);
}
```

#### Alias utilisateur et groupes d'abonnement {#user-aliases-and-subscription-groups}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    // Add alias
    user.addAlias('external_id', '12345');

    // Add to subscription group
    user.addToSubscriptionGroup('newsletter_subscribers');

    // Remove from subscription group
    user.removeFromSubscriptionGroup('old_subscribers');
}
```

#### Déconnexion de l'utilisateur {#user-logout}

``` typescript
import { wipeData } from "@braze/web-sdk";

// There is no explicit method to logout. To "forget" the current users entirely, use wipeData().
// This is a complete data wipe (use with caution, this wipes things such as device ID)
wipeData();
```

### In-App Messages

#### Affichage automatique {#automatic-display}

``` typescript
import { automaticallyShowInAppMessages } from "@braze/web-sdk";

// Automatically show in-app messages
automaticallyShowInAppMessages();
```

#### Affichage manuel {#manual-display}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

// Subscribe to in-app messages
subscribeToInAppMessage((inAppMessage) => {
    // Show the message
    showInAppMessage(inAppMessage);
});
```

#### Gestion personnalisée des messages in-app {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### Enregistrer les interactions avec les messages in-app {#log-in-app-message-interactions}

``` typescript
import {
    logInAppMessageClick,
    logInAppMessageImpression,
    logInAppMessageButtonClick
} from "@braze/web-sdk";

// Log when user sees the message
logInAppMessageImpression(inAppMessage);

// Log when user clicks the message
logInAppMessageClick(inAppMessage);

// Log when user clicks a button in the message
logInAppMessageButtonClick(inAppMessage, button);
```

#### Messages in-app HTML personnalisés {#custom-html-in-app-messages}

``` typescript
import { subscribeToInAppMessage, logInAppMessageImpression, logInAppMessageClick } from "@braze/web-sdk";

// Don't call automaticallyShowInAppMessages() when using custom rendering
// braze.automaticallyShowInAppMessages(); // Comment this out

subscribeToInAppMessage((inAppMessage) => {
    // Extract message data
    const messageData = {
        title: inAppMessage.getMessage(),
        body: inAppMessage.getBody(),
        imageUrl: inAppMessage.getImageUrl(),
        buttons: inAppMessage.getButtons(),
        deepLink: inAppMessage.getExtras()['deep_link_url']
    };

    // Define your own HTML structure, using messageData
    const customHTML = ` <!-- Add your custom styling and structure -->`;

    /* Render the In-App Message here */

    // Here we naively log an impression once the message is rendered.
    // Be precise about exactly when you want to log an impression (ie. only the first time it enters the view port).
    logInAppMessageImpression(inAppMessage);
});

// Handle button clicks and deep linking
const handleButtonClick = (button, inAppMessage) => {
    logInAppMessageClick(inAppMessage);
    // Handle additional click actions (ie. deep linking)
};
```

### Content Cards

#### Afficher les Content Cards {#display-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show content cards in default location
showContentCards();

// Show in specific container
const container = document.getElementById('content-cards-container');
showContentCards(container);
```

#### S'abonner aux mises à jour des Content Cards {#subscribe-to-content-cards-updates}

``` typescript
import { subscribeToContentCardsUpdates } from "@braze/web-sdk";

subscribeToContentCardsUpdates((cards) => {
    console.log('Content cards updated:', cards);
    // Display cards or update UI
});
```

#### Enregistrer les interactions avec les Content Cards {#log-content-card-interactions}

``` typescript
import {
    logContentCardClick,
    logContentCardImpressions,
    logCardDismissal
} from "@braze/web-sdk";

// Log card impressions
logContentCardImpressions(cards);

// Log card clicks
logContentCardClick(card);

// Log card dismissals
logCardDismissal(card);
```

#### Filtrer les Content Cards {#filter-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show only pinned cards
// You can also provide a parent element instead of null
showContentCards(null, (cards) => {
    return cards.filter(card => card.getIsPinned());
});
```

#### Demander l'actualisation des Content Cards {#request-content-cards-refresh}

``` typescript
import { requestContentCardsRefresh } from "@braze/web-sdk";

requestContentCardsRefresh(
    () => console.log('Content cards refreshed'),
    () => console.log('Failed to refresh content cards')
);
```

#### Content Cards personnalisées {#custom-content-cards}

``` typescript
import { subscribeToContentCardsUpdates, logContentCardClick, logContentCardImpressions, requestContentCardsRefresh } from "@braze/web-sdk";

// State for impression de-duping
const loggedImpressions = new Set();
const idToCard = new Map();

subscribeToContentCardsUpdates((cards) => {
    // Build cards one by one
    cards.getCards().forEach(card => {
        // Skip control cards
        if (card.getIsControl()) return;

        // Extract card data
        const cardData = {
            id: card.getId(),
            title: card.getTitle(),
            description: card.getDescription(),
            imageUrl: card.getImageUrl(),
            url: card.getUrl(),
            extras: card.getExtras()
        };

        // Define your own HTML structure, using cardData
        const customHTML = ` <!-- Add your custom styling and structure -->`;

        /* Render each card here */

        // Basic observer for impression logging.
        // Be precise about exactly when you want to log an impression (ie. only the first time it enters the view port).
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    logContentCardImpressions([card]);
                }
            });
        });

        // Observe card element when rendered
        // observer.observe(cardElement);
    });
});

// Handle card clicks
const handleCardClick = (card) => {
    logContentCardClick(card);
    // Handle additional click actions (ie. navigation)
};

```

### Notifications push {#push-notifications}

#### Demander l'autorisation de notification push {#request-push-permission}

``` typescript
import { requestPushPermission } from "@braze/web-sdk";

requestPushPermission(
    () => console.log('Push permission granted'),
    () => console.log('Push permission denied')
);
```

#### Vérifier la prise en charge des notifications push {#check-push-support}

``` typescript
import { isPushSupported, isPushPermissionGranted } from "@braze/web-sdk";

if (isPushSupported()) {
    if (isPushPermissionGranted()) {
        console.log('Push notifications are enabled');
    } else {
        console.log('Push permission not granted');
    }
}
```

#### Désenregistrer les notifications push {#unregister-push}

``` typescript
import { unregisterPush } from "@braze/web-sdk";

unregisterPush(
    () => console.log('Successfully unregistered'),
    () => console.log('Failed to unregister')
);
```

### Feature flags {#feature-flags}

#### Obtenir un feature flag {#get-feature-flag}

``` typescript
import { getFeatureFlag } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_checkout_flow');
if (featureFlag) {
    const isEnabled = featureFlag.getBooleanProperty('enabled', false);
    const rolloutPercentage = featureFlag.getNumberProperty('rollout_percentage', 0);

    if (isEnabled) {
        // Enable new checkout flow
    }
}
```

#### S'abonner aux mises à jour des feature flags {#subscribe-to-feature-flag-updates}

``` typescript
import { subscribeToFeatureFlagsUpdates } from "@braze/web-sdk";

subscribeToFeatureFlagsUpdates((featureFlags) => {
    featureFlags.forEach(flag => {
        console.log(`Feature flag ${flag.getId()}: ${flag.getBooleanProperty('enabled')}`);
    });
});
```

#### Enregistrer les impressions des feature flags {#log-feature-flag-impressions}

``` typescript
import { logFeatureFlagImpression } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_feature');
if (featureFlag) {
    logFeatureFlagImpression(featureFlag);
}
```

#### Demander l'actualisation des feature flags {#request-feature-flags-refresh}

``` typescript
import { refreshFeatureFlags } from "@braze/web-sdk";

refreshFeatureFlags(
    () => console.log('Feature flags refreshed'),
    () => console.log('Failed to refresh feature flags')
);
```

### Bannières {#banners}

#### Obtenir et afficher des bannières {#get-and-display-banners}

``` typescript
import { getBanner, insertBanner } from "@braze/web-sdk";

const banner = getBanner('homepage_banner');
if (banner) {
    // Insert banner into specific element
    const container = document.getElementById('banner-container');
    insertBanner(banner, container);
}
```

#### S'abonner aux mises à jour des bannières {#subscribe-to-banner-updates}

``` typescript
import { insertBanner, subscribeToBannersUpdates } from "@braze/web-sdk";

subscribeToBannersUpdates((banners) => {
    Object.entries(banners).forEach(([placementId, banner]) => {
        if (banner) {
            console.log(`Banner for ${placementId}:`, banner);

            // Insert banner into specific element
            const container = document.getElementById(`banner-container-${placementId}`);
            insertBanner(banner, container);
        }
    });
});
```

#### Fermer des bannières dans une interface personnalisée {#dismiss-banners-in-a-custom-ui}

``` typescript
import { dismissBanner, getBanner, subscribeToBannersUpdates } from "@braze/web-sdk";

subscribeToBannersUpdates((banners) => {
    const banner = getBanner("homepage_banner");
    const container = document.getElementById("custom-banner-container");
    if (!container) {
        return;
    }

    if (!banner) {
        container.replaceChildren();
        return;
    }

    banner.subscribeToDismissedEvent(() => {
        console.log("Dismissed banner:", banner);
    });

    const closeButton = document.createElement("button");
    closeButton.textContent = "Close";
    closeButton.addEventListener("click", () => {
        dismissBanner(banner);
    });

    // Render your custom UI here and include the close button.
});
```

Lorsque vous appelez `dismissBanner(banner)`, le SDK gère l'état de fermeture de la bannière, la retire des mises à jour de bannières actives, notifie les abonnés à l'événement de fermeture de la bannière et synchronise la fermeture avec Braze. Les interfaces personnalisées doivent utiliser `subscribeToBannersUpdates` pour réagir au retrait de la bannière fermée, plutôt que de traiter `dismissBanner` comme un simple changement d'interface locale ou une simple méthode d'enregistrement analytique.

#### Demander l'actualisation des bannières {#request-banner-refresh}

``` typescript
import { requestBannersRefresh } from "@braze/web-sdk";

requestBannersRefresh(
    ["placement_1", "placement_2"],
    () => console.log('Banners refreshed'),
    () => console.log('Failed to refresh banners')
);
```

### Analytique et événements {#analytics-events}

#### Enregistrer des événements personnalisés {#log-custom-events}

``` typescript
import { logCustomEvent } from "@braze/web-sdk";

// Simple event
logCustomEvent('button_clicked');

// Event with properties
logCustomEvent('purchase', {
    product_id: '123',
    price: 29.99,
    currency: 'USD'
});
```

#### Enregistrer des achats {#log-purchases}

``` typescript
import { logPurchase } from "@braze/web-sdk";

logPurchase('product-123', 29.99, 'USD', 1, {
    category: 'electronics',
    brand: 'Apple'
});
```

#### Demander l'envoi immédiat des données {#request-data-flush}

``` typescript
import { requestImmediateDataFlush } from "@braze/web-sdk";

// Force immediate data send
requestImmediateDataFlush();
```

### Gestion des sessions {#session-management}

#### Ouvrir une session {#open-session}

``` typescript
import { openSession } from "@braze/web-sdk";

// Start a new session
openSession();
```

#### Vérifier l'état du SDK {#check-sdk-status}

``` typescript
import { isInitialized, isDisabled } from "@braze/web-sdk";

if (isInitialized()) {
    console.log('SDK is initialized');

    if (isDisabled()) {
        console.log('SDK is disabled');
    }
}
```

#### Activer/désactiver le SDK {#enabledisable-sdk}

``` typescript
import { enableSDK, disableSDK } from "@braze/web-sdk";

// Disable SDK
disableSDK();

// Re-enable SDK
enableSDK();
```

### Gestion des données {#data-management}

#### Effacer les données {#wipe-data}

``` typescript
import { wipeData } from "@braze/web-sdk";

// Remove all locally stored data
wipeData();
```

#### Détruire le SDK {#destroy-sdk}

``` typescript
import { destroy } from "@braze/web-sdk";

// Clean up SDK resources
destroy();
```

#### Obtenir l'identifiant d'appareil {#get-device-id}

``` typescript
import { getDeviceId } from "@braze/web-sdk";

const deviceId = getDeviceId();
console.log('Device ID:', deviceId);
```

#### Authentification SDK {#sdk-authentication}

``` typescript
import { setSdkAuthenticationSignature } from "@braze/web-sdk";

// Set authentication signature
setSdkAuthenticationSignature('your-signature-here');
```

#### S'abonner aux échecs d'authentification {#subscribe-to-authentication-failures}

``` typescript
import { subscribeToSdkAuthenticationFailures } from "@braze/web-sdk";

subscribeToSdkAuthenticationFailures((error) => {
    console.log('Authentication failed:', error);
    // Provide new signature
    setSdkAuthenticationSignature('new-signature');
});
```

---

## Modèles d'intégration {#integration-patterns}

### Frameworks SSR {#ssr-frameworks}

Si vous utilisez un framework de rendu côté serveur (SSR) tel que Next.js, vous pouvez rencontrer des erreurs car le SDK est conçu pour être exécuté dans un environnement de navigateur. Vous pouvez résoudre ces problèmes en important dynamiquement le SDK.

Vous pouvez conserver les avantages du tree-shaking en exportant les parties du SDK dont vous avez besoin dans un fichier séparé, puis en important dynamiquement ce fichier dans votre composant.

``` javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

Alternativement, si vous utilisez webpack pour empaqueter votre application, vous pouvez tirer parti de ses commentaires magiques pour importer dynamiquement uniquement les parties du SDK dont vous avez besoin.

``` javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

### Vite

Si vous utilisez Vite et voyez un avertissement concernant des dépendances circulaires ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, vous devrez peut-être exclure le SDK Braze de sa découverte de dépendances :

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Framework Jest {#jest-framework}

Lorsque vous utilisez Jest, vous pouvez voir une erreur similaire à `SyntaxError: Unexpected token 'export'`. Pour corriger cela, ajustez votre configuration dans `package.json` pour ignorer le SDK Braze :

``` json
{
  "jest": {
    "transformIgnorePatterns": [
      "/node_modules/(?!@braze)"
    ]
  }
}
```

### Asynchronous Module Definition (AMD) {#asynchronous-module-definition-amd}

#### Désactiver la prise en charge AMD {#disable-amd-support}

Si votre site utilise RequireJS ou un autre chargeur de modules AMD, mais que vous préférez charger le SDK Web de Braze via le CDN, vous pouvez charger une version de la bibliothèque qui n'inclut pas la prise en charge AMD. Cette version de la bibliothèque peut être chargée depuis l'emplacement CDN : `https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`

#### Chargeur de modules {#module-loader}

Si vous utilisez RequireJS ou d'autres chargeurs de modules AMD, nous recommandons d'héberger vous-même une copie de notre bibliothèque et de la référencer comme vous le feriez avec d'autres ressources :

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Pages mobiles accélérées (AMP) {#accelerated-mobile-pages-amp}

Pour l'intégration AMP, vous devrez :

1. **Inclure le script de notification push Web AMP** : ajoutez la balise script asynchrone dans votre en-tête
2. **Ajouter des widgets d'abonnement** : ajoutez des widgets pour permettre aux utilisateurs de s'abonner ou de se désabonner
3. **Ajouter des fichiers d'aide** : incluez `helper-iframe.html` et `permission-dialog.html`
4. **Créer un service worker** : ajoutez le fichier de service worker de Braze
5. **Configurer l'élément de notification push Web AMP** : ajoutez l'élément `amp-web-push` avec votre clé API et l'URL de base comme paramètres de requête

Pour des instructions détaillées sur l'intégration AMP, consultez le [guide développeur de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web#amp).

### Electron

Electron ne prend pas officiellement en charge les notifications push Web (voir : ce [ticket GitHub](https://github.com/electron/electron/issues/6697)). Il existe d'autres [solutions open source](https://github.com/MatthieuLemoine/electron-push-receiver) que vous pouvez essayer, mais qui n'ont pas été testées par Braze.

### Intégration CDN {#cdn-integration}

- **Chargement du script** : initialisez après le chargement de la balise script en plaçant le code d'initialisation après la balise script, ou utilisez le gestionnaire d'événement `onload` de la balise script
- **Accès global** : le SDK est disponible en tant que `window.braze` lorsqu'il est chargé via le CDN

### Service worker (notifications push) {#service-worker-push-notifications}

- **Requis** : le service worker de Braze doit être inclus pour que les notifications push fonctionnent
- **Enregistrement par défaut** : par défaut, le SDK Web de Braze enregistre et gère automatiquement votre service worker lorsque `requestPushPermission()` est appelé, ainsi qu'au début de chaque nouvelle session pour les utilisateurs ayant déjà accordé l'autorisation de notification push. Vous devez tout de même héberger un fichier de service worker à l'emplacement attendu contenant le code du service worker de Braze.
- **Gérer votre propre service worker** : si vous gérez déjà un service worker dans votre application, définissez l'option d'initialisation `manageServiceWorkerExternally` sur `true`, ajoutez le code du service worker de Braze dans votre fichier de service worker et enregistrez-le vous-même en utilisant `navigator.serviceWorker.register()`
- **Autorisations push** : appelez `braze.requestPushPermission()` en réponse aux interactions utilisateur (par exemple, les clics sur un bouton). Utilisez des invites push douces (interface personnalisée) avant de demander l'autorisation du navigateur

### Gestionnaires de balises {#tag-managers}

#### Tealium iQ

Tealium iQ offre une intégration Braze clé en main de base. Pour configurer l'intégration, recherchez Braze dans l'interface de gestion des balises Tealium, et fournissez la clé API du SDK Web depuis votre tableau de bord. Pour plus de détails ou une assistance approfondie sur la configuration Tealium, consultez notre [documentation d'intégration](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou contactez votre gestionnaire de compte Tealium.

#### Google Tag Manager

Le SDK Web peut être initialisé et appelé depuis une balise HTML personnalisée dans votre conteneur Google Tag Manager. Consultez notre [application d'exemple Google Tag Manager](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/google-tag-manager) pour un exemple d'envoi d'événements à Braze via GTM, ou consultez notre [documentation d'intégration](https://www.braze.com/docs/developer_guide/sdk_integration/google_tag_manager) pour plus de détails.

#### Autres gestionnaires de balises {#other-tag-managers}

Braze peut également être compatible avec d'autres solutions de gestion de balises en suivant nos instructions d'intégration dans une balise HTML personnalisée. Contactez un conseiller Braze si vous avez besoin d'aide pour évaluer ces solutions.

---

## Bibliothèques {#libraries}

Le tableau suivant décrit les distributions disponibles du SDK Web de Braze.

| Nom | Description | npm | URL CDN
| --- | ----------- | --- | -------
| Complète | SDK complet avec interface utilisateur. Lorsque vous utilisez la version npm, les bundlers JavaScript suppriment le code inutilisé, y compris le code d'interface utilisateur. | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.10/braze.min.js
| Core | Contient le SDK sans interface utilisateur. Implémentez votre propre interface utilisateur pour les In-App Messages et les Content Cards lorsque vous utilisez cette version du SDK. Utilisez la bibliothèque complète pour la plupart des intégrations, car elle fournit des éléments d'interface utilisateur personnalisables via CSS. | N/A | https://js.appboycdn.com/web-sdk/6.10/braze.core.min.js
| No-AMD | Contient le SDK complet sans prise en charge AMD. Cela est utile si votre site utilise RequireJS ou un autre chargeur de modules AMD, mais que vous préférez charger le SDK via le CDN. | N/A | https://js.appboycdn.com/web-sdk/6.10/braze.no-amd.min.js
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bibliothèques" }

## Navigateurs pris en charge {#supported-browsers}

- Navigateurs modernes basés sur Chromium (Chrome, Edge, Opera)
- Firefox
- Safari

## Débogage et résolution des problèmes {#debugging-troubleshooting}

Passez l'option `enableLogging: true` à la fonction d'initialisation (`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`) pour que Braze écrive dans la console JavaScript. Cela est utile pour le développement mais est visible par tous les utilisateurs, donc supprimez cette option ou [fournissez un logger alternatif](https://js.appboycdn.com/web-sdk/6.10/doc/modules/braze.html#setlogger) avant de mettre votre page en production.

## Font Awesome

Braze utilise [Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0 pour les icônes des messages in-app. Pour désactiver le chargement de Font Awesome, utilisez l'option d'initialisation `doNotLoadFontAwesome`. Consultez l'[aide-mémoire](http://fortawesome.github.io/Font-Awesome/cheatsheet/) pour parcourir les icônes disponibles.

## Ressources supplémentaires {#additional-resources}

- [Guide développeur de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web)
- [Documentation du SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [Exemples de builds](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## Contact {#contact}

Si vous avez des questions, contactez le support technique de Braze pour obtenir de l'aide.
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les projets d'exemple, consultez [https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk).