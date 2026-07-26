---
nav_title: JavaScript SDK
article_title: JavaScript SDK – Repository-Leitfaden
page_order: 4
description: "Braze JavaScript SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# JavaScript SDK – Repository-Leitfaden {#javascript-sdk-repository-guide}

## Über das Braze JavaScript SDK {#about-the-braze-javascript-sdk}

Das Braze JavaScript SDK hilft Ihnen, Braze-Messaging-, Analytics- und Nutzer:innen-Engagement-Funktionen in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen folgende Ressourcen zur Verfügung:

- [Braze-Benutzerhandbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=javascript)

### Architekturübersicht {#architecture-overview}

Das Braze JavaScript SDK ist eine **plattformunabhängige** Bibliothek, die in jeder reinen JavaScript-Umgebung funktioniert. Es enthält keine browser- oder Node.js-spezifischen APIs und eignet sich daher für den Einsatz in verschiedenen JavaScript-Laufzeitumgebungen.

**Zentrale Designprinzipien:**
- **Dependency Injection**: Das SDK erfordert Implementierungen für Speicher, Netzwerk und Geräteinformationen, anstatt plattformspezifische APIs zu verwenden
- **Async-First**: Die meisten API-Methoden sind asynchron und geben Promises zurück; einige Hilfsmethoden (z. B. `destroy`, `subscribeToInAppMessage`, `toggleLogging`, `setLogger`) sind synchron. Die genauen Signaturen finden Sie in den TypeScript-Definitionen.
- **Singleton-Sitzung**: Die API auf Modulebene (`initialize`/`destroy`) verwaltet jeweils eine aktive SDK-Sitzung.
- **Internes Abhängigkeitsmanagement**: Erstellt und verwaltet interne Abhängigkeiten (UserManager, SessionManager, DataFlushController usw.) aus den bereitgestellten Implementierungen

<!--
Effective marketing automation is an essential part of successfully scaling and managing your business. Braze empowers you to build better geschäftskunden relationships through a seamless, multi-channel approach that addresses all aspects of the user life cycle. Braze helps you engage your users on an ongoing basis. We'll have you up and running in no time!

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction)
- [Initial Web SDK Setup](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)
- [Braze Web SDK Documentation](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html) -->

## Schnellstart {#quickstart}

Installieren Sie das SDK mit npm:

``` bash
npm install @braze/javascript-sdk
```

Oder mit yarn:

``` bash
yarn add @braze/javascript-sdk
```

Mit der API auf Modulebene:
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

## Voraussetzungen {#prerequisites}

Bevor Sie das Braze JavaScript SDK integrieren, benötigen Sie:

{% multi_lang_include developer_guide/sdk_api_prerequisites.md %}

### Zugangsdaten abrufen {#getting-your-credentials}

1. **API-Schlüssel**: Zu finden in Ihrem Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**
2. **SDK-Endpunkt**: Zu finden unter **Einstellungen** > **SDK-Authentifizierung** > **Endpunkte**

## Integration {#integration}

### API aufrufen {#calling-the-api}

Verwenden Sie die API auf Modulebene: Rufen Sie `initialize()` einmal auf und nutzen Sie dann die exportierten Funktionen. Um die Konfiguration zu wechseln, rufen Sie zuerst `destroy()` und dann erneut `initialize()` auf.

``` typescript
import { initialize, logPurchase, changeUser } from '@braze/javascript-sdk';

await initialize({ apiKey, baseUrl, options, ... });
await changeUser('user-123');
await logPurchase('sku-1', 9.99, 'USD', 1);
```

### Kernkonzepte {#core-concepts}

#### Erforderliche Implementierungen {#required-implementations}

Das Konfigurationsobjekt für die Initialisierung erfordert `storageManager`. `networkManager` und `pushManager` sind optional.

**1. StorageManager** – Asynchrone Key-Value-Speicherschnittstelle
``` typescript
interface StorageManager {
  store(key: string, value: string, isId?: boolean): Promise<void>;
  remove(key: string, isId?: boolean): Promise<void>;
  retrieve(key: string, isId?: boolean): Promise<string | null>;
  clearData(storageKeys: string[]): Promise<void>;
}
```
- Der Parameter `isId` kennzeichnet **persistente ID-Speicherung**: Wenn `true`, speichert das SDK einen persistenten Bezeichner (Geräte-ID, Nutzer:innen-ID) oder das Opt-out-Flag. Implementierungen sollten diese über App-Neustarts hinweg beibehalten, damit das SDK dasselbe Gerät bzw. dieselbe:n Nutzer:in wiedererkennen kann. Wenn `false`, handelt es sich um Sitzungs-/Cache-Daten (Ereignisse, Attribute usw.), die nur im Arbeitsspeicher gehalten werden können. Für Webumgebungen empfiehlt es sich, Cookies für Schlüssel zu verwenden, die mit `isId: true` gespeichert werden, um sitzungsübergreifende Persistenz sicherzustellen.
- Muss asynchrone Operationen für alle Speichervorgänge unterstützen

**2. NetworkManager** (optional) – HTTP-POST-Anfrageschnittstelle
``` typescript
interface NetworkManager {
  postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: globalThis.Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>>;
}
```
- Die Standardimplementierung verwendet die `fetch`-API (erfordert globales `fetch` und `URL`)
- Kann überschrieben werden, wenn `fetch` nicht die bevorzugte API ist
- Hinweis: Das SDK verfügt bereits über integrierte Retry- und Rate-Limiting-Logik

**3. PushManager** (optional) – Push-Benachrichtigungsschnittstelle
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
- Nur erforderlich, wenn Push-Benachrichtigungen implementiert werden

#### Daten-Flushing {#data-flushing}

Das SDK überträgt zwischengespeicherte Daten automatisch alle 10 Sekunden an die Braze-Server (konfigurierbar über `flushIntervalInSeconds`). Verwenden Sie `requestImmediateDataFlush()`, um eine sofortige Synchronisierung zu erzwingen.

### Integrationsmuster {#integration-patterns}

Für Methodensignaturen, Parameter- und Rückgabetypen sowie vollständige API-Details siehe die TypeScript-Definitionen im Paket.

#### Grundlegende Integration {#basic-integration}

Vollständiges Arbeitsbeispiel mit Fehlerbehandlung:

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

#### Angepasste Speicherimplementierung {#custom-storage-implementation}

Vollständige StorageManager-Implementierung mit IndexedDB für persistente IDs:

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

#### Angepasste Netzwerkimplementierung {#custom-network-implementation}

NetworkManager, der jede ausgehende Anfrage protokolliert (das SDK übernimmt bereits Fehlerbehandlung und Retries):

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

#### Fehlerbehandlung {#error-handling}

Vollständige Muster zur Fehlerbehandlung:

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

#### Abo-Management {#subscription-management}

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

**Konfiguration wechseln:** Es existiert jeweils nur eine aktive Sitzung. Um die Konfiguration zu wechseln, rufen Sie `destroy()` und dann `initialize()` auf:

``` typescript
import { destroy, initialize } from '@braze/javascript-sdk';

destroy();
await initialize({ /* new config */ });
```

### Häufige Anwendungsfälle {#common-use-cases}

#### Nutzer:innen-Identifikation und Attribut-Tracking {#user-identification-and-attribute-tracking}

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

#### Ereignisprotokollierung und Analytics {#event-logging-and-analytics}

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

#### In-App-Nachrichten-Behandlung {#in-app-message-handling}

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

### Fehlerbehandlung und Sonderfälle {#error-handling-edge-cases}

#### Häufige Fehlerbedingungen {#common-error-conditions}

**SDK nicht initialisiert:**
- Die meisten Methoden geben `undefined` zurück (statt zu werfen), wenn das SDK nicht initialisiert ist
- `initialize()` gibt `false` zurück, wenn bereits initialisiert oder die Validierung fehlschlägt
- `changeUser()` ist ein No-Op und das Promise wird aufgelöst, wenn das SDK nicht initialisiert ist
- Prüfen Sie Rückgabewerte immer auf `undefined`, bevor Sie sie verwenden

**Validierungsfehler:**
- Ungültiger API-Schlüssel oder Base-URL: `initialize()` gibt `false` zurück und protokolliert einen Fehler
- Ungültige Ereignisnamen/Schlüssel: Maximal 255 Zeichen, dürfen nicht mit `$` beginnen, nur alphanumerische Zeichen und Satzzeichen
- Ungültige Attributwerte: Strings maximal 255 Zeichen, keine Zeilenumbrüche/Tabs/doppelte Anführungszeichen, dürfen nicht mit `$` beginnen
- Ungültige Währungscodes: Nicht unterstützte Codes führen zu einer Warnung, es wird keine Aktion ausgeführt
- Ungültige Kaufmenge: Muss zwischen 1 und 100 liegen, wird andernfalls ignoriert

**Netzwerkfehler:**
- Die `postRequest()`-Methode des NetworkManagers sollte Fehler behandeln und Promises entsprechend ablehnen
- Der Data-Flush-Controller wiederholt fehlgeschlagene Anfragen automatisch
- Verwenden Sie den Callback von `requestImmediateDataFlush()`, um Flush-Fehler zu erkennen

**Speicherfehler:**
- StorageManager-Methoden sollten Fehler ordnungsgemäß behandeln
- Wenn der Speicher fehlschlägt, funktioniert das SDK möglicherweise nicht korrekt
- Das `isId`-Flag bestimmt die Persistenz: IDs bleiben sitzungsübergreifend erhalten, Objekte sind sitzungsbezogen

**Sonderfälle bei der Nutzer:innen-Identifikation:**
- Nach der Identifikation kann nicht zu einer:m anonymen Nutzer:in zurückgekehrt werden
- Ein Nutzer:innenwechsel beendet die aktuelle Sitzung und startet eine neue
- Der Verlauf anonymer Nutzer:innen bleibt bei der erstmaligen Identifikation erhalten
- Der Verlauf wird zusammengeführt, wenn die:der Nutzer:in auf einem anderen Gerät existiert

**Sitzungsverwaltung:**
- Sitzungen laufen nach 30 Minuten Inaktivität ab (konfigurierbar)
- `openSession()` gibt `true` für eine neue Sitzung zurück, `false` bei Wiederaufnahme
- `openSession()` muss nach `changeUser()` oder `setIdentifierToken()` aufgerufen werden

**Abo-Management:**
- Abo-Callbacks werden synchron aufgerufen, wenn Ereignisse eintreten
- Entfernen Sie Abos, um Speicherlecks zu vermeiden
- `removeAllSubscriptions()` löscht alle Abos auf einmal

**Daten-Flushing:**
- Automatischer Flush alle 10 Sekunden (konfigurierbar, Minimum: 3 Sekunden)
- Flush kann stillschweigend fehlschlagen – verwenden Sie den Callback von `requestImmediateDataFlush()`
- Daten werden in die Warteschlange gestellt, wenn das Netzwerk nicht verfügbar ist, und übertragen, sobald das Netzwerk wiederhergestellt ist

### Wichtige Hinweise zur Implementierung {#important-implementation-notes}

1. **Die meisten Methoden sind asynchron**: Asynchrone SDK-Methoden geben ein Promise zurück (verwenden Sie `await` oder `.then()`). Einige Konfigurations- und Hilfsmethoden (z. B. `destroy`, `toggleLogging`, `setLogger`) sind synchron; Details finden Sie in den TypeScript-Definitionen oder der Kurzreferenztabelle.

2. **Methoden können `undefined` zurückgeben**: Wenn das SDK nicht initialisiert ist, geben die meisten Methoden `undefined` zurück, anstatt zu werfen. Prüfen Sie auf `undefined`, bevor Sie Rückgabewerte verwenden.

3. **Methoden können `null` zurückgeben**: Einige Methoden geben `null` zurück, um „nicht gefunden“ anzuzeigen (z. B. gibt `getUserId()` `null` zurück, wenn die:der Nutzer:in anonym ist). Dies unterscheidet sich von `undefined` (SDK nicht initialisiert).

4. **Speicherschlüssel verwenden das `isId`-Flag**: Der Parameter `isId` in StorageManager-Methoden unterscheidet zwischen:
   - ID-Speicher: Persistente Bezeichner (Geräte-ID, Nutzer:innen-ID), die sitzungsübergreifend erhalten bleiben sollen
   - Objekt-Speicher: Sitzungsbezogene Daten, die gelöscht werden können

5. **SDK-Metadaten-Tags**: Das `sdkMetadata`-Array identifiziert die Plattform/den Wrapper, der das SDK verwendet (z. B. `['npm']` oder `[BrazeSdkMetadata.NPM]`). Gültige Tags werden durch das `BrazeSdkMetadata`-Enum definiert (z. B. `npm`, `cdn`, `manu`, `shp`, `gg`, `kep`), und das SDK fügt automatisch `'wjs'` hinzu, um das JavaScript SDK zu kennzeichnen.

6. **Standard-NetworkManager**: Wenn kein `networkManager` bereitgestellt wird, verwendet das SDK eine Standardimplementierung, die globale `fetch`- und `URL`-APIs erfordert. Stellen Sie eine angepasste Implementierung bereit, wenn diese nicht verfügbar sind.

7. **PushManager ist optional**: Implementieren Sie `PushManager` nur, wenn Sie Push-Benachrichtigungsfunktionalität benötigen. Andernfalls kann er weggelassen werden.

8. **Destroy und Bereinigung**: Rufen Sie `destroy()` auf, wenn Sie das SDK herunterfahren müssen. Es kann jeweils nur eine aktive Sitzung existieren; Sie müssen `destroy()` aufrufen, bevor Sie `initialize()` erneut aufrufen. Dadurch werden Timer gestoppt, Daten übertragen und Ressourcen freigegeben.

9. **Daten-Flushing**: Daten werden automatisch alle 10 Sekunden übertragen (konfigurierbar). Verwenden Sie `requestImmediateDataFlush()` für eine sofortige Synchronisierung.

10. **Sitzungsverwaltung**: Rufen Sie `openSession()` immer nach `changeUser()` oder `setIdentifierToken()` auf, um die Erstellung doppelter anonymer Nutzer:innen zu vermeiden.

11. **Typsicherheit**: Das SDK ist in TypeScript mit vollständigen Typdefinitionen geschrieben. Verwenden Sie TypeScript für die beste Erfahrung und Typprüfung.

12. **Validierungsregeln**: Ereignisnamen, Attributschlüssel und Eigenschaftsschlüssel unterliegen einer strikten Validierung (maximal 255 Zeichen, dürfen nicht mit `$` beginnen, nur alphanumerische Zeichen und Satzzeichen). Ungültige Werte können ignoriert werden oder Fehler verursachen.

## Debugging und Fehlerbehebung {#debugging-troubleshooting}

Übergeben Sie die Option `enableLogging: true` an die Initialisierungsoptionen. Dies ist für die Entwicklung wertvoll, aber stellen Sie sicher, dass Sie diese Option entfernen oder [einen alternativen Logger bereitstellen](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html#setlogger), bevor Sie Ihre Seite in die Produktion überführen.

## Kontakt {#contact}

Wenn Sie Fragen haben, kontaktieren Sie bitte [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-javascript-sdk](https://github.com/braze-inc/braze-javascript-sdk).