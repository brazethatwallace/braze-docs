---
nav_title: Web SDK
article_title: Leitfaden zum Web SDK Repository
page_order: 1
description: "Braze Web SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Über das Braze Web SDK {#about-the-braze-web-sdk}

Das Braze Web SDK ermöglicht es Ihnen, die Customer-Engagement-Plattform von Braze direkt in Ihre Webanwendungen zu integrieren. Es wurde mit TypeScript entwickelt und für moderne Webentwicklung konzipiert. Dieses SDK bietet umfassende Tools für Nutzerverwaltung, Messaging, Analytics und Feature-Flags.

### Was Sie damit tun können {#what-you-can-do}

- **Nutzerverwaltung**: Verfolgen und verwalten Sie Nutzeridentitäten, Attribute und Verhalten in Ihrer gesamten Webanwendung
- **In-App Messages**: Zeigen Sie gezielte Nachrichten und Benachrichtigungen an, während Nutzer:innen Ihre Website aktiv nutzen
- **Content Cards**: Zeigen Sie personalisierte Inhalts-Feeds und Aktionskarten an, die sich in Realtime aktualisieren
- **Banner**: Zeigen Sie Banner-Nachrichten an bestimmten Platzierungen innerhalb Ihrer Website an
- **Push-Benachrichtigungen**: Senden Sie Web-Push-Benachrichtigungen, um Nutzer:innen auch dann anzusprechen, wenn sie nicht auf Ihrer Website sind
- **Feature-Flags**: Steuern Sie Feature-Rollouts und A/B-Tests mit serverseitigem Feature-Flag-Management
- **Analytics**: Verfolgen Sie angepasste Events, Nutzerinteraktionen und Conversion-Metriken
- **Sitzungsverwaltung**: Überwachen Sie Nutzersitzungen und Engagement-Muster

Ob Sie eine Single-Page-Anwendung, eine E-Commerce-Website oder eine Content-Plattform erstellen – das Braze Web SDK bietet Ihnen die Tools, die Sie benötigen, um personalisierte, ansprechende Nutzererlebnisse zu schaffen, die Wachstum und Bindung fördern.

## Voraussetzungen {#prerequisites}

Bevor Sie das Braze Web SDK integrieren, benötigen Sie:

- **Braze-Konto**: Ein Braze-Konto mit API-Zugang
- **API-Schlüssel**: Den API-Schlüssel Ihrer App aus dem Braze-Dashboard
- **SDK-Endpunkt**: Ihre Braze SDK-Endpunkt-URL (z. B. `sdk.iad-01.braze.com`)

### Ihre Zugangsdaten abrufen {#getting-your-credentials}

1. **API-Schlüssel**: Zu finden in Ihrem Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**
2. **SDK-Endpunkt**: Zu finden unter **Einstellungen** > **SDK-Authentifizierung** > **Endpunkte**
3. **Service Worker**: Erforderlich für Push-Benachrichtigungen (siehe Abschnitt Push-Benachrichtigungen)

## Installation {#installation}

``` bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

## Schnellstart {#quick-start}

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});

braze.changeUser('Jane Doe');
```

## Konfigurationsreferenz {#configuration-reference}

### Initialisierungsoptionen {#initialization-options}

Die Funktion `initialize` akzeptiert ein Options-Objekt mit den folgenden Eigenschaften:

| Option | Typ | Standard | Beschreibung |
|--------|-----|----------|--------------|
| `baseUrl` | `string` | **Erforderlich** | Diese Option ist erforderlich, um das Braze Web SDK so zu konfigurieren, dass es den passenden Endpunkt für Ihre Integration verwendet – zum Beispiel: `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | Auf true setzen, um Logging standardmäßig zu aktivieren. Beachten Sie, dass Braze dadurch in die JavaScript-Konsole loggt, die für alle Nutzer:innen sichtbar ist! Sie sollten diese Option entfernen oder mit setLogger einen alternativen Logger bereitstellen, bevor Sie Ihre Seite in Produktion bringen. |
| `allowUserSuppliedJavascript` | `boolean` | `false` | Standardmäßig erlaubt das Braze Web SDK keine benutzerdefinierten JavaScript-Klickaktionen und aktiviert keine HTML-In-App-Nachrichten und Banner, da diese es Braze-Dashboard-Nutzer:innen ermöglichen, JavaScript auf Ihrer Website auszuführen. Um anzugeben, dass Sie den Braze-Dashboard-Nutzer:innen vertrauen, nicht-schädliche JavaScript-Klickaktionen zu schreiben, setzen Sie diese Eigenschaft auf true. |
| `doNotLoadFontAwesome` | `boolean` | `false` | Braze verwendet Font Awesome für In-App-Nachricht-Icons. Standardmäßig lädt Braze automatisch FontAwesome 4.7.0 vom FontAwesome CDN. Um dieses Verhalten zu deaktivieren (z. B. weil Ihre Website eine angepasste Version von FontAwesome verwendet), setzen Sie diese Option auf `true`. Beachten Sie, dass Sie in diesem Fall dafür verantwortlich sind, sicherzustellen, dass FontAwesome auf Ihrer Website geladen wird – andernfalls werden In-App-Nachrichten möglicherweise nicht korrekt dargestellt. |
| `inAppMessageZIndex` | `number` | `999999` | Standardmäßig zeigt das Braze SDK In-App Messages mit einem z-index von 999999 an. Geben Sie einen Wert für diese Option an, um diesen Standard zu überschreiben. |
| `sessionTimeoutInSeconds` | `number` | `30` | Standardmäßig läuft eine Sitzung nach 30 Sekunden Inaktivität ab. Geben Sie einen Wert für diese Option an, um diesen Standard zu überschreiben. |
| `deviceId` | `string` | Automatisch generiert | Standardmäßig weist Braze eine zufällige GUID als Geräte-ID zu. Geben Sie einen Wert für diese Konfigurationsoption an, um diesen Standard mit einem eigenen Wert zu überschreiben. |
| `appVersion` | `string` | `undefined` | Wenn Sie einen Wert für diese Option angeben, werden an Braze gesendete Nutzer-Events mit der angegebenen Version verknüpft, die für die Nutzersegmentierung verwendet werden kann. |
| `appVersionNumber` | `string` | `undefined` | Ein numerischer App-Versionswert, der für die Nutzersegmentierung verwendet werden kann. Dieser Wert muss mit vier Feldern gesendet werden, z. B. „1.2.3.4“, andernfalls wird er ignoriert. Hinweis: `appVersion` muss ebenfalls gesetzt werden, entweder mit demselben Wert oder einem eindeutigen Namen für diese Version. |
| `contentSecurityNonce` | `string` | `undefined` | Wenn Sie einen Wert für diese Option angeben, fügt das Braze SDK die Nonce zu allen vom SDK erstellten `<script>`- und `<style>`-Elementen hinzu. Dies kann verwendet werden, um das Braze SDK mit der Content Security Policy Ihrer Website kompatibel zu machen. Beachten Sie, dass Sie zusätzlich zum Setzen dieser Nonce möglicherweise auch das Laden von FontAwesome erlauben müssen, indem Sie entweder `use.fontawesome.com` zu Ihrer Content Security Policy Allowlist hinzufügen oder die Option `doNotLoadFontAwesome` verwenden und es manuell laden. |
| `noCookies` | `boolean` | `false` | Standardmäßig verwendet das Braze Web SDK Cookies. Um die Cookie-Nutzung zu deaktivieren, setzen Sie diese Option auf true. Beachten Sie, dass das Deaktivieren von Cookies die Fähigkeit des SDK beeinträchtigen kann, Nutzeridentitäten zwischen Sitzungen zu speichern. |
| `allowCrawlerActivity` | `boolean` | `false` | Standardmäßig ignoriert das Braze Web SDK Aktivitäten von bekannten Spidern oder Web-Crawlern wie Google, basierend auf dem User-Agent-String. Dies spart Datenpunkte, macht Analytics genauer und kann das Seitenranking verbessern. Wenn Sie jedoch möchten, dass Braze Aktivitäten dieser Crawler protokolliert, können Sie diese Option auf true setzen. |
| `disablePushTokenMaintenance` | `boolean` | `false` | Standardmäßig synchronisieren Nutzer:innen, die bereits die Web-Push-Berechtigung erteilt haben (z. B. über requestPushPermission oder von einem früheren Push-Anbieter), ihren Push-Token automatisch bei neuen Sitzungen mit dem Braze-Backend, um die Zustellbarkeit sicherzustellen. Um dieses Verhalten zu deaktivieren, setzen Sie diese Option auf true. |
| `enableSdkAuthentication` | `boolean` | `false` | Auf true setzen, um das Feature SDK-Authentifizierung zu aktivieren. Weitere Informationen zur SDK-Authentifizierung finden Sie in unserer Produktdokumentation. |
| `manageServiceWorkerExternally` | `boolean` | `false` | Standardmäßig verwaltet das Braze Web SDK seinen eigenen Service Worker für Push-Benachrichtigungen. Wenn Sie bereits einen Service Worker in Ihrer Anwendung verwalten und die Braze-Service-Worker-Funktionalität darin integrieren möchten, setzen Sie diese Option auf true und fügen Sie den Braze-Service-Worker-Code in Ihre Service-Worker-Datei ein. |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | Standardmäßig können Trigger-Aktionen (z. B. das Anzeigen einer In-App-Nachricht) höchstens einmal alle 30 Sekunden pro Nutzer:in ausgelöst werden. Geben Sie einen Wert für diese Option an, um diesen Standard zu überschreiben. |
| `serviceWorkerLocation` | `string` | `undefined` | Standardmäßig sucht das Braze Web SDK nach seiner Service-Worker-Datei im Stammverzeichnis Ihrer Domain. Geben Sie einen Wert für diese Option an, um diesen Standard zu überschreiben und einen benutzerdefinierten Speicherort für die Service-Worker-Datei anzugeben. |
| `safariWebsitePushId` | `string` | `undefined` | Erforderlich für Safari-Push-Benachrichtigungen. Dieser Wert ist in Ihrem Apple Developer-Konto zu finden. Weitere Informationen zum Einrichten von Safari-Push-Benachrichtigungen finden Sie in unserer Produktdokumentation. |
| `localization` | `string` | `undefined` | Wenn Sie einen Wert für diese Option angeben, versucht das Braze SDK, In-App-Nachrichten und Content Cards in diesem Gebietsschema anzuzeigen. |
| `openInAppMessagesInNewTab` | `boolean` | `false` | Standardmäßig werden Links in In-App-Nachrichten im selben Tab geöffnet. Setzen Sie diese Option auf true, damit sie stattdessen in einem neuen Tab geöffnet werden. |
| `openCardsInNewTab` | `boolean` | `false` | Standardmäßig werden Links in Content Cards im selben Tab geöffnet. Setzen Sie diese Option auf true, damit sie stattdessen in einem neuen Tab geöffnet werden. |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | Standardmäßig können In-App-Nachrichten durch Klicken außerhalb der Nachricht oder Drücken der Escape-Taste geschlossen werden. Setzen Sie diese Option auf true, damit Nutzer:innen explizit auf einen Schließen-Button oder Aktions-Button klicken müssen, um die Nachricht zu schließen. |
| `devicePropertyAllowlist` | `string[]` | `undefined` | Standardmäßig erkennt und erfasst das Braze SDK automatisch alle Geräteeigenschaften in DeviceProperties. Um dieses Verhalten zu überschreiben, geben Sie ein Array von DeviceProperties an. Um das Senden aller Eigenschaften an Braze-Server zu deaktivieren, geben Sie ein leeres Array an. Beachten Sie, dass ohne einige Eigenschaften nicht alle Features ordnungsgemäß funktionieren. Ohne die Zeitzone funktioniert beispielsweise die Zustellung nach Ortszeit nicht. |
| `serviceWorkerScope` | `string` | `undefined` | Standardmäßig registriert das Braze Web SDK seinen Service Worker mit dem Standard-Scope (dem Verzeichnis des Service Workers). Geben Sie einen Wert für diese Option an, um diesen Standard zu überschreiben und einen benutzerdefinierten Scope für den Service Worker anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Initialisierungsoptionen" }

---

## Kernfunktionen {#core-features}

### Initialisierung und Einrichtung {#initialization-setup}

#### Grundlegende Initialisierung {#basic-initialization}

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

#### Erweiterte Initialisierungsoptionen {#advanced-initialization-options}

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

### Nutzerverwaltung {#user-management}

#### Nutzer:in wechseln {#change-user}

``` typescript
import { changeUser } from "@braze/web-sdk";

// Change to a new user
changeUser('user-123');
```

#### Nutzerattribute setzen {#set-user-attributes}

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

#### Nutzerstandort setzen {#set-user-location}

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

#### Nutzer-Aliase und Abo-Gruppen {#user-aliases-and-subscription-groups}

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

#### Nutzer-Abmeldung {#user-logout}

``` typescript
import { wipeData } from "@braze/web-sdk";

// There is no explicit method to logout. To "forget" the current users entirely, use wipeData().
// This is a complete data wipe (use with caution, this wipes things such as device ID)
wipeData();
```

### In-App Messages

#### Automatische Anzeige {#automatic-display}

``` typescript
import { automaticallyShowInAppMessages } from "@braze/web-sdk";

// Automatically show in-app messages
automaticallyShowInAppMessages();
```

#### Manuelle Anzeige {#manual-display}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

// Subscribe to in-app messages
subscribeToInAppMessage((inAppMessage) => {
    // Show the message
    showInAppMessage(inAppMessage);
});
```

#### Benutzerdefinierte In-App-Nachricht-Verarbeitung {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### In-App-Nachricht-Interaktionen protokollieren {#log-in-app-message-interactions}

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

#### Benutzerdefinierte HTML-In-App-Nachrichten {#custom-html-in-app-messages}

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

#### Content Cards anzeigen {#display-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show content cards in default location
showContentCards();

// Show in specific container
const container = document.getElementById('content-cards-container');
showContentCards(container);
```

#### Content-Card-Updates abonnieren {#subscribe-to-content-cards-updates}

``` typescript
import { subscribeToContentCardsUpdates } from "@braze/web-sdk";

subscribeToContentCardsUpdates((cards) => {
    console.log('Content cards updated:', cards);
    // Display cards or update UI
});
```

#### Content-Card-Interaktionen protokollieren {#log-content-card-interactions}

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

#### Content Cards filtern {#filter-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show only pinned cards
// You can also provide a parent element instead of null
showContentCards(null, (cards) => {
    return cards.filter(card => card.getIsPinned());
});
```

#### Content-Card-Aktualisierung anfordern {#request-content-cards-refresh}

``` typescript
import { requestContentCardsRefresh } from "@braze/web-sdk";

requestContentCardsRefresh(
    () => console.log('Content cards refreshed'),
    () => console.log('Failed to refresh content cards')
);
```

#### Benutzerdefinierte Content Cards {#custom-content-cards}

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

### Push-Benachrichtigungen {#push-notifications}

#### Push-Berechtigung anfordern {#request-push-permission}

``` typescript
import { requestPushPermission } from "@braze/web-sdk";

requestPushPermission(
    () => console.log('Push permission granted'),
    () => console.log('Push permission denied')
);
```

#### Push-Unterstützung prüfen {#check-push-support}

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

#### Push-Registrierung aufheben {#unregister-push}

``` typescript
import { unregisterPush } from "@braze/web-sdk";

unregisterPush(
    () => console.log('Successfully unregistered'),
    () => console.log('Failed to unregister')
);
```

### Feature-Flags {#feature-flags}

#### Feature-Flag abrufen {#get-feature-flag}

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

#### Feature-Flag-Updates abonnieren {#subscribe-to-feature-flag-updates}

``` typescript
import { subscribeToFeatureFlagsUpdates } from "@braze/web-sdk";

subscribeToFeatureFlagsUpdates((featureFlags) => {
    featureFlags.forEach(flag => {
        console.log(`Feature flag ${flag.getId()}: ${flag.getBooleanProperty('enabled')}`);
    });
});
```

#### Feature-Flag-Impressionen protokollieren {#log-feature-flag-impressions}

``` typescript
import { logFeatureFlagImpression } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_feature');
if (featureFlag) {
    logFeatureFlagImpression(featureFlag);
}
```

#### Feature-Flag-Aktualisierung anfordern {#request-feature-flags-refresh}

``` typescript
import { refreshFeatureFlags } from "@braze/web-sdk";

refreshFeatureFlags(
    () => console.log('Feature flags refreshed'),
    () => console.log('Failed to refresh feature flags')
);
```

### Banner {#banners}

#### Banner abrufen und anzeigen {#get-and-display-banners}

``` typescript
import { getBanner, insertBanner } from "@braze/web-sdk";

const banner = getBanner('homepage_banner');
if (banner) {
    // Insert banner into specific element
    const container = document.getElementById('banner-container');
    insertBanner(banner, container);
}
```

#### Banner-Updates abonnieren {#subscribe-to-banner-updates}

``` typescript
import { subscribeToBannersUpdates } from "@braze/web-sdk";

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

#### Banner-Aktualisierung anfordern {#request-banner-refresh}

``` typescript
import { requestBannersRefresh } from "@braze/web-sdk";

requestBannersRefresh(
    ["placement_1", "placement_2"],
    () => console.log('Banners refreshed'),
    () => console.log('Failed to refresh banners')
);
```

### Analytics und Events {#analytics-events}

#### Angepasste Events protokollieren {#log-custom-events}

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

#### Käufe protokollieren {#log-purchases}

``` typescript
import { logPurchase } from "@braze/web-sdk";

logPurchase('product-123', 29.99, 'USD', 1, {
    category: 'electronics',
    brand: 'Apple'
});
```

#### Daten-Flush anfordern {#request-data-flush}

``` typescript
import { requestImmediateDataFlush } from "@braze/web-sdk";

// Force immediate data send
requestImmediateDataFlush();
```

### Sitzungsverwaltung {#session-management}

#### Sitzung öffnen {#open-session}

``` typescript
import { openSession } from "@braze/web-sdk";

// Start a new session
openSession();
```

#### SDK-Status prüfen {#check-sdk-status}

``` typescript
import { isInitialized, isDisabled } from "@braze/web-sdk";

if (isInitialized()) {
    console.log('SDK is initialized');

    if (isDisabled()) {
        console.log('SDK is disabled');
    }
}
```

#### SDK aktivieren/deaktivieren {#enabledisable-sdk}

``` typescript
import { enableSDK, disableSDK } from "@braze/web-sdk";

// Disable SDK
disableSDK();

// Re-enable SDK
enableSDK();
```

### Datenverwaltung {#data-management}

#### Daten löschen {#wipe-data}

``` typescript
import { wipeData } from "@braze/web-sdk";

// Remove all locally stored data
wipeData();
```

#### SDK zerstören {#destroy-sdk}

``` typescript
import { destroy } from "@braze/web-sdk";

// Clean up SDK resources
destroy();
```

#### Geräte-ID abrufen {#get-device-id}

``` typescript
import { getDeviceId } from "@braze/web-sdk";

const deviceId = getDeviceId();
console.log('Device ID:', deviceId);
```

#### SDK-Authentifizierung {#sdk-authentication}

``` typescript
import { setSdkAuthenticationSignature } from "@braze/web-sdk";

// Set authentication signature
setSdkAuthenticationSignature('your-signature-here');
```

#### Authentifizierungsfehler abonnieren {#subscribe-to-authentication-failures}

``` typescript
import { subscribeToSdkAuthenticationFailures } from "@braze/web-sdk";

subscribeToSdkAuthenticationFailures((error) => {
    console.log('Authentication failed:', error);
    // Provide new signature
    setSdkAuthenticationSignature('new-signature');
});
```

---

## Integrationsmuster {#integration-patterns}

### SSR-Frameworks {#ssr-frameworks}

Wenn Sie ein Server-Side-Rendering-(SSR)-Framework wie Next.js verwenden, können Fehler auftreten, da das SDK für die Ausführung in einer Browserumgebung konzipiert ist. Sie können diese Probleme lösen, indem Sie das SDK dynamisch importieren.

Sie können die Vorteile des Tree-Shakings beibehalten, indem Sie die benötigten Teile des SDK in einer separaten Datei exportieren und diese Datei dann dynamisch in Ihre Komponente importieren.

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

Alternativ können Sie, wenn Sie webpack zum Bundling Ihrer App verwenden, dessen Magic Comments nutzen, um nur die benötigten Teile des SDK dynamisch zu importieren.

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

Wenn Sie Vite verwenden und eine Warnung zu zirkulären Abhängigkeiten oder `Uncaught TypeError: Class extends value undefined is not a constructor or null` sehen, müssen Sie möglicherweise das Braze SDK von der Dependency-Erkennung ausschließen:

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Jest-Framework {#jest-framework}

Bei der Verwendung von Jest kann ein Fehler ähnlich wie `SyntaxError: Unexpected token 'export'` auftreten. Um dies zu beheben, passen Sie Ihre Konfiguration in `package.json` an, um das Braze SDK zu ignorieren:

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

#### AMD-Unterstützung deaktivieren {#disable-amd-support}

Wenn Ihre Website RequireJS oder einen anderen AMD-Modul-Loader verwendet, Sie das Braze Web SDK aber lieber über das CDN laden möchten, können Sie eine Version der Bibliothek laden, die keine AMD-Unterstützung enthält. Diese Version der Bibliothek kann vom CDN-Standort geladen werden: `https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`

#### Modul-Loader {#module-loader}

Wenn Sie RequireJS oder andere AMD-Modul-Loader verwenden, empfehlen wir, eine Kopie unserer Bibliothek selbst zu hosten und sie wie andere Ressourcen zu referenzieren:

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Accelerated Mobile Pages (AMP) {#accelerated-mobile-pages-amp}

Für die AMP-Integration müssen Sie:

1. **AMP-Web-Push-Skript einbinden**: Fügen Sie das async-Script-Tag in Ihren Head ein
2. **Abo-Widgets hinzufügen**: Fügen Sie Widgets hinzu, damit Nutzer:innen sich an- und abmelden können
3. **Hilfsdateien hinzufügen**: Binden Sie `helper-iframe.html` und `permission-dialog.html` ein
4. **Service Worker erstellen**: Fügen Sie die Braze-Service-Worker-Datei hinzu
5. **AMP-Web-Push-Element konfigurieren**: Fügen Sie das `amp-web-push`-Element mit Ihrem API-Schlüssel und Ihrer Basis-URL als Abfrageparameter hinzu

Detaillierte Anweisungen zur AMP-Integration finden Sie im [Braze Developer Guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#amp).

### Electron

Electron unterstützt Web-Push-Benachrichtigungen nicht offiziell (siehe: dieses [GitHub-Issue](https://github.com/electron/electron/issues/6697)). Es gibt andere [Open-Source-Workarounds](https://github.com/MatthieuLemoine/electron-push-receiver), die Sie ausprobieren können, die jedoch nicht von Braze getestet wurden.

### CDN-Integration {#cdn-integration}

- **Skript-Laden**: Initialisieren Sie nach dem Laden des Script-Tags, indem Sie den Initialisierungscode nach dem Script-Tag platzieren, oder verwenden Sie den `onload`-Event-Handler des Script-Tags
- **Globaler Zugriff**: Das SDK ist als `window.braze` verfügbar, wenn es über CDN geladen wird

### Service Worker (Push-Benachrichtigungen) {#service-worker-push-notifications}

- **Erforderlich**: Der Braze-Service-Worker muss eingebunden werden, damit Push-Benachrichtigungen funktionieren
- **Registrierung**: Registrieren Sie den Service Worker in Ihrem Website-Code mit `navigator.serviceWorker.register()`
- **Push-Berechtigungen**: Rufen Sie `braze.requestPushPermission()` als Reaktion auf Nutzerinteraktionen auf (z. B. Button-Klicks). Verwenden Sie Soft-Push-Prompts (benutzerdefinierte UI), bevor Sie die Browser-Berechtigung anfordern

### Tag-Manager {#tag-managers}

#### Tealium iQ

Tealium iQ bietet eine grundlegende schlüsselfertige Braze-Integration. Um die Integration zu konfigurieren, suchen Sie in der Tealium Tag-Management-Oberfläche nach Braze und geben Sie den Web SDK API-Schlüssel aus Ihrem Dashboard an. Weitere Details oder ausführliche Unterstützung bei der Tealium-Konfiguration finden Sie in unserer [Integrationsdokumentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) oder wenden Sie sich an Ihren Tealium Account Manager.

#### Andere Tag-Manager {#other-tag-managers}

Braze kann auch mit anderen Tag-Management-Lösungen kompatibel sein, indem Sie unsere Integrationsanweisungen innerhalb eines benutzerdefinierten HTML-Tags befolgen. Wenden Sie sich an eine Braze-Vertretung, wenn Sie Hilfe bei der Bewertung dieser Lösungen benötigen.

---

## Bibliotheken {#libraries}

| Name | Beschreibung | npm | CDN-URL
| ---- | ------------ | --- | -------
| Full | Vollständiges SDK mit UI. Bei Verwendung der npm-Version entfernen JavaScript-Bundler ungenutzten Code einschließlich der UI. | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.8/braze.min.js
| Core | Enthält das SDK ohne UI. Sie müssen Ihre eigene UI für In-App Messages und Content Cards implementieren, wenn Sie diese Version des SDK verwenden. Unsere UI-Elemente sind vollständig über CSS anpassbar, daher empfehlen wir generell die Integration der vollständigen Bibliothek. | N/A | https://js.appboycdn.com/web-sdk/6.8/braze.core.min.js
| No-AMD | Enthält das vollständige SDK ohne AMD-Unterstützung. Dies ist nützlich, wenn Ihre Website RequireJS oder einen anderen AMD-Modul-Loader verwendet, Sie das SDK aber lieber über das CDN laden möchten. | N/A | https://js.appboycdn.com/web-sdk/6.8/braze.no-amd.min.js
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bibliotheken" }

## Unterstützte Browser {#supported-browsers}

- Moderne Chromium-basierte Browser (Chrome, Edge, Opera)
- Firefox
- Safari

## Debugging und Fehlerbehebung {#debugging-troubleshooting}

Übergeben Sie die Option `enableLogging: true` an die Initialisierungsfunktion (`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`), damit Braze in die JavaScript-Konsole loggt. Dies ist wertvoll für die Entwicklung, aber für alle Nutzer:innen sichtbar. Entfernen Sie diese Option daher oder [stellen Sie einen alternativen Logger bereit](https://js.appboycdn.com/web-sdk/6.8/doc/modules/braze.html#setlogger), bevor Sie Ihre Seite in Produktion bringen.

## Font Awesome

Braze verwendet [Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0 für In-App-Nachricht-Icons. Um das Laden von Font Awesome zu deaktivieren, verwenden Sie die Initialisierungsoption `doNotLoadFontAwesome`. Durchsuchen Sie den [Spickzettel](http://fortawesome.github.io/Font-Awesome/cheatsheet/), um verfügbare Icons zu finden.

## Zusätzliche Ressourcen {#additional-resources}

- [Braze Developer Guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)
- [SDK-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [Beispiel-Builds](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## Kontakt {#contact}

Wenn Sie Fragen haben, kontaktieren Sie bitte [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk).