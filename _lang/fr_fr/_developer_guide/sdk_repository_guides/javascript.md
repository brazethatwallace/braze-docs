---
nav_title: SDK JavaScript
article_title: Guide du dépôt du SDK JavaScript
page_order: 4
description: "Référence du README du SDK JavaScript de Braze, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guide du dépôt du SDK JavaScript {#javascript-sdk-repository-guide}

## À propos du SDK JavaScript de Braze {#about-the-braze-javascript-sdk}

Le SDK JavaScript de Braze vous aide à intégrer les fonctionnalités de communication, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide utilisateur de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guide développeur de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=javascript)

### Aperçu de l'architecture {#architecture-overview}

Le SDK JavaScript de Braze est une bibliothèque **indépendante de la plateforme**, conçue pour fonctionner dans tout environnement JavaScript pur. Il ne contient pas d'API spécifiques au navigateur ou à Node.js, ce qui le rend adapté à une utilisation dans divers environnements d'exécution JavaScript.

**Principes de conception clés :**
- **Injection de dépendances** : le SDK nécessite des implémentations pour le stockage, la mise en réseau et les informations sur l'appareil, plutôt que d'utiliser des API spécifiques à une plateforme.
- **Asynchrone par défaut** : la plupart des méthodes de l'API sont asynchrones et renvoient des Promises ; certaines méthodes utilitaires (par exemple `destroy`, `subscribeToInAppMessage`, `toggleLogging`, `setLogger`) sont synchrones. Consultez les définitions TypeScript pour les signatures exactes.
- **Session singleton** : l'API au niveau du module (`initialize`/`destroy`) gère une seule session SDK active à la fois.
- **Gestion interne des dépendances** : crée et gère les dépendances internes (UserManager, SessionManager, DataFlushController, etc.) à partir des implémentations fournies.

<!--
Effective marketing automation is an essential part of successfully scaling and managing your business. Braze empowers you to build better customer relationships through a seamless, multi-channel approach that addresses all aspects of the user life cycle. Braze helps you engage your users on an ongoing basis. We'll have you up and running in no time!

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction)
- [Initial Web SDK Setup](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)
- [Braze Web SDK Documentation](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html) -->

## Démarrage rapide {#quickstart}

Installez le SDK avec npm :

``` bash
npm install @braze/javascript-sdk
```

Ou avec yarn :

``` bash
yarn add @braze/javascript-sdk
```

Avec l'API au niveau du module :
``` typescript
import { initialize, openSession, changeUser } from '@braze/javascript-sdk';

await initialize({
  apiKey,
  baseUrl,
  options,
  sdkMetadata,
  deviceInfo,
  storageManager,
  networkManager,
});

await changeUser(userId);

await openSession();
```

## Prérequis {#prerequisites}

Avant d'intégrer le SDK JavaScript de Braze, vous aurez besoin des éléments suivants :

- **Compte Braze** : un compte Braze avec accès à l'API
- **Clé API** : la clé API de votre application, disponible dans le tableau de bord de Braze
- **Endpoint du SDK** : l'URL de votre endpoint du SDK Braze (par exemple, `sdk.iad-01.braze.com`)

### Obtenir vos identifiants {#getting-your-credentials}

1. **Clé API** : disponible dans votre tableau de bord de Braze sous **Paramètres** > **Clés API**
2. **Endpoint du SDK** : accessible dans **Paramètres** > **Authentification du SDK** > **Endpoints**

## Intégration {#integration}

### Appeler l'API {#calling-the-api}

Utilisez l'API au niveau du module : appelez `initialize()` une seule fois, puis appelez les fonctions exportées. Pour changer de configuration, appelez d'abord `destroy()`, puis `initialize()` à nouveau.

``` typescript
import { initialize, logPurchase, changeUser } from '@braze/javascript-sdk';

await initialize({ apiKey, baseUrl, options, ... });
await changeUser('user-123');
await logPurchase('sku-1', 9.99, 'USD', 1);
```

### Concepts fondamentaux {#core-concepts}

#### Implémentations requises {#required-implementations}

L'objet de configuration d'initialisation nécessite `storageManager`. `networkManager` et `pushManager` sont optionnels.

**1. StorageManager** - Interface de stockage clé-valeur asynchrone
``` typescript
interface StorageManager {
  store(key: string, value: string, isId?: boolean): Promise<void>;
  remove(key: string, isId?: boolean): Promise<void>;
  retrieve(key: string, isId?: boolean): Promise<string | null>;
  clearData(storageKeys: string[]): Promise<void>;
}
```
- Le paramètre `isId` indique un **stockage d'identifiant persistant** : lorsqu'il vaut `true`, le SDK stocke un identifiant persistant (ID d'appareil, ID utilisateur) ou le drapeau de désinscription. Les implémentations doivent conserver ces données entre les redémarrages de l'application afin que le SDK puisse reconnaître le même appareil/utilisateur. Lorsqu'il vaut `false`, la valeur correspond à des données de session/cache (événements, attributs, etc.) et peut rester uniquement en mémoire. Pour les environnements web, envisagez d'utiliser des cookies pour les clés stockées avec `isId: true` afin de garantir la persistance entre les sessions.
- Doit gérer les opérations asynchrones pour toutes les opérations de stockage

**2. NetworkManager** (optionnel) - Interface de requêtes HTTP POST
``` typescript
interface NetworkManager {
  postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: globalThis.Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>>;
}
```
- L'implémentation par défaut utilise l'API `fetch` (nécessite `fetch` et `URL` globaux)
- Peut être remplacée si `fetch` n'est pas l'API souhaitée
- Remarque : le SDK intègre déjà une logique de réessai et de limitation du débit

**3. PushManager** (optionnel) - Interface de notifications push
``` typescript
interface PushManager {
  isPushBlocked(): boolean | undefined;
  isPushPermissionGranted(): boolean | undefined;
  isPushSupported(): boolean | undefined;
  registerPush(
    successCallback?: (endpoint: string, publicKey: string, userAuth: string) => void,
    deniedCallback?: (temporaryDenial: boolean) => void,
  ): void;
  unregisterPush(successCallback?: () => void, errorCallback?: () => void): void;
}
```
- Requis uniquement si vous implémentez les notifications push

#### Vidage des données {#data-flushing}

Le SDK vide automatiquement les données en cache vers les serveurs Braze toutes les 10 secondes (configurable via `flushIntervalInSeconds`). Utilisez `requestImmediateDataFlush()` pour forcer une synchronisation immédiate.

### Modèles d'intégration {#integration-patterns}

Pour les signatures de méthodes, les types de paramètres et de retour, ainsi que les détails complets de l'API, consultez les définitions TypeScript dans le package.

#### Intégration de base {#basic-integration}

Exemple fonctionnel complet avec gestion des erreurs :

``` typescript
import {
  initialize,
  openSession,
  changeUser,
  logCustomEvent,
  type StorageManager,
  type DeviceInfo
} from '@braze/javascript-sdk';

// Implement required StorageManager interface (in-memory only; does not persist data).
// This example treats all keys equally and ignores the isId parameter
// See "Complete StorageManager implementation with IndexedDB" below for an
// example where we properly handle isId
class InMemoryStorageManager implements StorageManager {
  private storage = new Map<string, string>();

  async store(key: string, value: string, isId?: boolean): Promise<void> {
    this.storage.set(key, value);
  }

  async retrieve(key: string, isId?: boolean): Promise<string | null> {
    return this.storage.get(key) ?? null;
  }

  async remove(key: string, isId?: boolean): Promise<void> {
    this.storage.delete(key);
  }

  async clearData(storageKeys: string[]): Promise<void> {
    for (const key of storageKeys) {
      this.storage.delete(key);
    }
  }
}

const storageManager: StorageManager = new InMemoryStorageManager();

// Provide device information (use your platform's APIs for non-browser)
const deviceInfo: DeviceInfo = {
  os: 'my-runtime-os',
  language: 'en',
  timezone: 'UTC',
  browser: 'Chrome', // Optional
  browserVersion: '120', // Optional
  userAgent: "some-user-agent" // Optional
};

// Browser-only example (uncomment and adapt if you are running in a web browser)
// const deviceInfo: DeviceInfo = {
//   os: navigator.platform || 'Unknown',
//   language: navigator.language || 'en',
//   timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
//   browser: 'Chrome', // Optional
//   browserVersion: '120', // Optional
//   userAgent: navigator.userAgent // Optional
// };

// Initialize SDK
try {
  const initialized = await initialize({
    apiKey: 'YOUR-API-KEY-HERE',
    baseUrl: 'sdk.iad-01.braze.com', // Your Braze SDK endpoint
    options: {
      sdkVersion: '1.0.0',
      enableLogging: true, // Remove in production
      sessionTimeoutInSeconds: 1800, // 30 minutes
      flushIntervalInSeconds: 10
    },
    sdkMetadata: ['npm'], // Identify your platform
    deviceInfo,
    storageManager
  });

  if (!initialized) {
    console.error('Failed to initialize Braze SDK');
    return;
  }

  // Identify user (wait for promise to resolve)
  await changeUser('user-123');

  // Open session (must be after changeUser)
  const isNewSession = await openSession();
  console.log('Session opened:', isNewSession ? 'new' : 'resumed');

  // Log events
  await logCustomEvent('app_opened', {
    source: 'homepage',
    timestamp: new Date().toISOString()
  });

} catch (error) {
  console.error('Braze SDK error:', error);
}
```

#### Implémentation de stockage personnalisée {#custom-storage-implementation}

Implémentation complète de StorageManager avec IndexedDB pour les identifiants persistants :

``` typescript
import type { StorageManager } from '@braze/javascript-sdk';

class IndexedDBStorageManager implements StorageManager {
  private dbName = 'braze-storage';
  private storeName = 'braze-ids';
  private memoryCache = new Map<string, string>();
  private db: IDBDatabase | null = null;
  private dbInitPromise: Promise<void> | null = null;

  private async initDB(): Promise<void> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, 1);
      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve();
      };
      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;
        if (!db.objectStoreNames.contains(this.storeName)) {
          db.createObjectStore(this.storeName);
        }
      };
    });
  }

  private async ensureDB(): Promise<void> {
    if (this.dbInitPromise !== null) {
      return this.dbInitPromise;
    }
    this.dbInitPromise = this.initDB();
    return this.dbInitPromise;
  }

  async store(key: string, value: string, isId?: boolean): Promise<void> {
    await this.ensureDB();
    this.memoryCache.set(key, value);

    if (isId && this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readwrite');
        const store = transaction.objectStore(this.storeName);
        await new Promise<void>((resolve, reject) => {
          const request = store.put(value, key);
          request.onsuccess = () => resolve();
          request.onerror = () => reject(request.error);
        });
      } catch (error) {
        console.error('Failed to store ID in IndexedDB:', error);
      }
    }
  }

  async retrieve(key: string, isId?: boolean): Promise<string | null> {
    await this.ensureDB();
    if (this.memoryCache.has(key)) {
      return this.memoryCache.get(key) || null;
    }

    if (isId && this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readonly');
        const store = transaction.objectStore(this.storeName);
        return new Promise<string | null>((resolve, reject) => {
          const request = store.get(key);
          request.onsuccess = () => {
            const value = request.result;
            if (value) {
              this.memoryCache.set(key, value);
            }
            resolve(value || null);
          };
          request.onerror = () => reject(request.error);
        });
      } catch (error) {
        console.error('Failed to retrieve ID from IndexedDB:', error);
        return null;
      }
    }

    return null;
  }

  async remove(key: string, isId?: boolean): Promise<void> {
    await this.ensureDB();
    this.memoryCache.delete(key);

    if (isId && this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readwrite');
        const store = transaction.objectStore(this.storeName);
        await new Promise<void>((resolve, reject) => {
          const request = store.delete(key);
          request.onsuccess = () => resolve();
          request.onerror = () => reject(request.error);
        });
      } catch (error) {
        console.error('Failed to remove ID from IndexedDB:', error);
      }
    }
  }

  async clearData(storageKeys: string[]): Promise<void> {
    await this.ensureDB();
    for (const key of storageKeys) {
      this.memoryCache.delete(key);
    }

    if (this.db) {
      try {
        const transaction = this.db.transaction([this.storeName], 'readwrite');
        const store = transaction.objectStore(this.storeName);
        await Promise.all(
          storageKeys.map(
            (key) =>
              new Promise<void>((resolve, reject) => {
                const request = store.delete(key);
                request.onsuccess = () => resolve();
                request.onerror = () => reject(request.error);
              })
          )
        );
      } catch (error) {
        console.error('Failed to clear data from IndexedDB:', error);
      }
    }
  }
}

const storageManager = new IndexedDBStorageManager();
```

#### Implémentation réseau personnalisée {#custom-network-implementation}

NetworkManager qui journalise chaque requête sortante (le SDK gère déjà les erreurs et les réessais) :

``` typescript
import type { NetworkManager } from '@braze/javascript-sdk';

function logRequest(url: string, data: Partial<Record<string, unknown>>): void {
  // Send to your analytics, monitoring, or logging backend
  console.log('Braze SDK request', { url, data });
}

class LoggingNetworkManager implements NetworkManager {
  async postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>> {
    logRequest(url, data);

    const requestHeaders = new Headers(headers);
    requestHeaders.set('Content-Type', 'application/json');

    const response = await fetch(url, {
      method: 'POST',
      headers: requestHeaders,
      body: JSON.stringify(data),
    });

    const result = await response.json();
    return result as Partial<Record<string, unknown>>;
  }
}

const networkManager = new LoggingNetworkManager();
```

#### Gestion des erreurs {#error-handling}

Modèles complets de gestion des erreurs :

``` typescript
import {
  getUserId,
  logCustomEvent,
  initialize,
} from '@braze/javascript-sdk';

// Pattern 1: Check for undefined (SDK not initialized)
async function getDevice() {
  const deviceId = await getDeviceId();
  if (deviceId === undefined) {
    console.warn('SDK not initialized');
    return null;
  }
  return deviceId;
}

// Pattern 2: Try-catch for methods that may throw
async function logEventSafely() {
  try {
    const success = await logCustomEvent('button_clicked', { button: 'submit' });
    if (success === undefined) {
      console.warn('SDK not initialized, event not logged');
    } else if (success) {
      console.log('Event logged successfully');
    } else {
      console.warn('Event failed to enqueue');
    }
  } catch (error) {
    console.error('Error logging event:', error);
    // Handle error (e.g., retry, queue for later)
  }
}

// Pattern 3: Handle null vs undefined distinction
async function checkUser() {
  const userId = await getUserId();

  if (userId === undefined) {
    // SDK not initialized
    console.warn('SDK not initialized');
  } else if (userId === null) {
    // Current user is anonymous
    console.log('Current user is anonymous');
  } else {
    // User is identified
    console.log(`User ID is ${userId}`);
  }
}

// Pattern 4: Handle initialization errors
async function initializeSafely() {
  try {
    const initialized = await initialize({
      apiKey: 'YOUR-API-KEY',
      baseUrl: 'sdk.iad-01.braze.com',
      options: { sdkVersion: '1.0.0' },
      sdkMetadata: ['npm'],
      deviceInfo: { os: 'iOS', language: 'en', timezone: 'UTC' },
      storageManager: myStorageManager
    });

    if (!initialized) {
      console.error('Failed to initialize SDK');
      // Check if already initialized, disabled, or validation failed
      return false;
    }

    return true;
  } catch (error) {
    console.error('Initialization error:', error);
    return false;
  }
}
```

#### Gestion des abonnements {#subscription-management}

``` typescript
import {
  ControlMessage,
  logInAppMessageImpression,
  removeSubscription,
  subscribeToInAppMessage,
} from '@braze/javascript-sdk';

const displayMessage = (inAppMessage) => {
  // Add custom code to display in-app messages
}

// Subscribe to in-app messages
const subscriptionId = subscribeToInAppMessage((inAppMessage) => {
  if (inAppMessage instanceof ControlMessage) {
    return; // Skip control messages
  }

  displayMessage(inAppMessage);

  logInAppMessageImpression(inAppMessage);
});

// Later, remove subscription if it was successfully created
if (subscriptionId) {
  removeSubscription(subscriptionId);
}
```

**Changement de configuration :** une seule session active existe à la fois. Pour changer de configuration, appelez `destroy()` puis `initialize()` :

``` typescript
import { destroy, initialize } from '@braze/javascript-sdk';

destroy();
await initialize({ /* new config */ });
```

### Cas d'usage courants {#common-use-cases}

#### Identification des utilisateurs et suivi des attributs {#user-identification-and-attribute-tracking}

``` typescript
import {
  changeUser,
  setCustomUserAttribute,
  setUserEmail,
  setUserFirstName,
  setUserLastName,
} from '@braze/javascript-sdk';

// Identify user
await changeUser('user-123');

// Set standard attributes
await setUserEmail('user@example.com');
await setUserFirstName('John');
await setUserLastName('Doe');

// Set custom attributes
await setCustomUserAttribute('subscription_tier', 'premium');
await setCustomUserAttribute('last_login', new Date());
await setCustomUserAttribute('tags', ['vip', 'early-adopter']);
```

#### Journalisation des événements et analyse {#event-logging-and-analytics}

``` typescript
import {
  logCustomEvent,
  logPurchase,
  requestImmediateDataFlush,
} from '@braze/javascript-sdk';

await logCustomEvent('product_viewed', {
  product_id: '123',
  category: 'electronics',
  price: 99.99
});

await logPurchase('product-123', 99.99, 'USD', 1, {
  category: 'electronics'
});

// Flushing these events to the server will happen periodically,
// however you can manually trigger a flush if necessary
requestImmediateDataFlush((success) => {
  console.log('Data flushed:', success);
});
```

#### Gestion des messages in-app {#in-app-message-handling}

``` typescript
import {
  ControlMessage,
  logInAppMessageImpression,
  subscribeToInAppMessage,
} from '@braze/javascript-sdk';

const displayInAppMessage = async (inAppMessage) => {
  // Add custom code to display in-app messages
}

subscribeToInAppMessage(async (inAppMessage) => {
  if (inAppMessage instanceof ControlMessage) {
    return;
  }

  await displayInAppMessage(inAppMessage);

  await logInAppMessageImpression(inAppMessage);
});
```

### Gestion des erreurs et cas limites {#error-handling-edge-cases}

#### Conditions d'erreur courantes {#common-error-conditions}

**SDK non initialisé :**
- La plupart des méthodes retournent `undefined` (sans lever d'exception) lorsque le SDK n'est pas initialisé
- `initialize()` retourne `false` s'il est déjà initialisé ou si la validation échoue
- `changeUser()` est un no-op et la promesse se résout si le SDK n'est pas initialisé
- Vérifiez toujours les valeurs de retour `undefined` avant de les utiliser

**Échecs de validation :**
- Clé API ou URL de base invalide : `initialize()` retourne `false`, journalise l'erreur
- Noms d'événements/clés invalides : 255 caractères maximum, ne peuvent pas commencer par `$`, caractères alphanumériques et ponctuation uniquement
- Valeurs d'attributs invalides : chaînes de 255 caractères maximum, pas de sauts de ligne/tabulations/guillemets doubles, ne peuvent pas commencer par `$`
- Codes de devise invalides : les codes non pris en charge génèrent un avertissement, aucune action effectuée
- Quantité d'achat invalide : doit être comprise entre 1 et 100, sinon ignorée

**Erreurs réseau :**
- La méthode `postRequest()` du NetworkManager doit gérer les erreurs et rejeter les promesses de manière appropriée
- Le contrôleur de vidage des données réessaie automatiquement les requêtes échouées
- Utilisez le rappel de `requestImmediateDataFlush()` pour détecter les échecs de vidage

**Erreurs de stockage :**
- Les méthodes du StorageManager doivent gérer les erreurs de manière élégante
- Si le stockage échoue, le SDK peut ne pas fonctionner correctement
- Le drapeau `isId` détermine la persistance : les identifiants persistent entre les sessions, les objets sont limités à la session

**Cas limites d'identification des utilisateurs :**
- Impossible de revenir à un utilisateur anonyme après identification
- Le changement d'utilisateur met fin à la session en cours et en démarre une nouvelle
- L'historique de l'utilisateur anonyme est conservé lors de la première identification
- L'historique est fusionné si l'utilisateur existe sur un autre appareil

**Gestion des sessions :**
- Les sessions expirent après 30 minutes d'inactivité (configurable)
- `openSession()` retourne `true` pour une nouvelle session, `false` si elle est reprise
- Vous devez appeler `openSession()` après `changeUser()` ou `setIdentifierToken()`

**Gestion des abonnements :**
- Les rappels d'abonnement sont appelés de manière synchrone lorsque des événements se produisent
- Supprimez les abonnements pour éviter les fuites de mémoire
- `removeAllSubscriptions()` supprime tous les abonnements en une seule fois

**Vidage des données :**
- Vidage automatique toutes les 10 secondes (configurable, minimum : 3 secondes)
- Le vidage peut échouer silencieusement — utilisez le rappel de `requestImmediateDataFlush()`
- Les données sont mises en file d'attente si le réseau est indisponible, puis vidées lorsque le réseau est rétabli

### Notes importantes sur l'implémentation {#important-implementation-notes}

1. **La plupart des méthodes sont asynchrones** : les méthodes asynchrones du SDK retournent une Promise (utilisez `await` ou `.then()`). Certaines méthodes de configuration et utilitaires (par exemple, `destroy`, `toggleLogging`, `setLogger`) sont synchrones ; consultez les définitions TypeScript ou le tableau de référence rapide pour plus de détails.

2. **Les méthodes peuvent retourner `undefined`** : si le SDK n'est pas initialisé, la plupart des méthodes retournent `undefined` au lieu de lever une exception. Vérifiez la présence de `undefined` avant d'utiliser les valeurs de retour.

3. **Les méthodes peuvent retourner `null`** : certaines méthodes retournent `null` pour indiquer « non trouvé » (par exemple, `getUserId()` retourne `null` si l'utilisateur est anonyme). Cela diffère de `undefined` (SDK non initialisé).

4. **Les clés de stockage utilisent le drapeau `isId`** : le paramètre `isId` dans les méthodes du StorageManager distingue entre :
   - Le stockage d'identifiants : identifiants persistants (ID d'appareil, ID utilisateur) qui doivent persister entre les sessions
   - Le stockage d'objets : données limitées à la session qui peuvent être effacées

5. **Tags de métadonnées du SDK** : le tableau `sdkMetadata` identifie la plateforme/le wrapper utilisant le SDK (par exemple, `['npm']` ou `[BrazeSdkMetadata.NPM]`). Les tags valides sont définis par l'enum `BrazeSdkMetadata` (tels que `npm`, `cdn`, `manu`, `shp`, `gg`, `kep`), et le SDK ajoute automatiquement `'wjs'` pour indiquer le SDK JavaScript.

6. **NetworkManager par défaut** : si `networkManager` n'est pas fourni, le SDK utilise une implémentation par défaut qui nécessite les API globales `fetch` et `URL`. Fournissez une implémentation personnalisée si celles-ci ne sont pas disponibles.

7. **PushManager est optionnel** : implémentez `PushManager` uniquement si vous avez besoin de la fonctionnalité de notifications push. Il peut être omis dans le cas contraire.

8. **Destruction et nettoyage** : appelez `destroy()` lorsque vous devez démonter le SDK. Une seule session active peut exister à la fois ; vous devez appeler `destroy()` avant d'appeler `initialize()` à nouveau. Cela arrête les minuteurs, vide les données et libère les ressources.

9. **Vidage des données** : les données sont automatiquement vidées toutes les 10 secondes (configurable). Utilisez `requestImmediateDataFlush()` pour une synchronisation immédiate.

10. **Gestion des sessions** : appelez toujours `openSession()` après `changeUser()` ou `setIdentifierToken()` pour éviter de créer des utilisateurs anonymes en double.

11. **Sécurité des types** : le SDK est écrit en TypeScript avec des définitions de types complètes. Utilisez TypeScript pour une meilleure expérience et une vérification des types.

12. **Règles de validation** : les noms d'événements, les clés d'attributs et les clés de propriétés ont une validation stricte (255 caractères maximum, ne peuvent pas commencer par `$`, caractères alphanumériques et ponctuation uniquement). Les valeurs invalides peuvent être ignorées ou provoquer des erreurs.

## Débogage / Résolution des problèmes {#debugging-troubleshooting}

Passez l'option `enableLogging: true` aux options d'initialisation. Cela est utile pour le développement, mais veillez à supprimer cette option ou à [fournir un logger alternatif](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html#setlogger) avant de mettre votre page en production.

## Contact

Si vous avez des questions, veuillez contacter [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les exemples de projets, consultez [https://github.com/braze-inc/braze-javascript-sdk](https://github.com/braze-inc/braze-javascript-sdk).