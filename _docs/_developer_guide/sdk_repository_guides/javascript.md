---
nav_title: JavaScript SDK
article_title: JavaScript SDK repository guide
page_order: 4
description: "Braze JavaScript SDK README reference mirrored from GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## About the Braze JavaScript SDK

The Braze JavaScript SDK helps you integrate Braze messaging, analytics, and user engagement capabilities into your application.

To get started, refer to the following resources:

- [Braze User Guide]({{site.baseurl}}/user_guide/introduction/)
- [Braze Developer Guide]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=javascript)

### Architecture Overview

The Braze JavaScript SDK is a **platform-agnostic** library designed to work in any pure JavaScript environment. It does not contain browser or Node.js-specific APIs, making it suitable for use in various JavaScript runtimes.

**Key Design Principles:**
- **Dependency Injection**: The SDK requires implementations for storage, networking, and device information rather than using platform-specific APIs
- **Async-First**: Most API methods are asynchronous and return Promises; some utility methods (e.g. `destroy`, `subscribeToInAppMessage`, `toggleLogging`, `setLogger`) are synchronous. Refer to the TypeScript definitions for exact signatures.
- **Singleton session**: Module-level API (`initialize`/`destroy`) manages one active SDK session at a time.
- **Internal Dependency Management**: Creates and manages internal dependencies (UserManager, SessionManager, DataFlushController, etc.) from provided implementations

<!--
Effective marketing automation is an essential part of successfully scaling and managing your business. Braze empowers you to build better customer relationships through a seamless, multi-channel approach that addresses all aspects of the user life cycle. Braze helps you engage your users on an ongoing basis. We'll have you up and running in no time!

- [Braze User Guide]({{site.baseurl}}/user_guide/introduction)
- [Initial Web SDK Setup]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)
- [Braze Web SDK Documentation](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html) -->

## Quickstart

Install the SDK with npm:

``` bash
npm install @braze/javascript-sdk
```

Or with yarn:

``` bash
yarn add @braze/javascript-sdk
```

With Module-Level API:
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

## Prerequisites

Before integrating the Braze JavaScript SDK, you'll need:

- **Braze Account**: A Braze account with API access
- **API Key**: Your app's API key from the Braze dashboard
- **SDK Endpoint**: Your Braze SDK endpoint URL (e.g., `sdk.iad-01.braze.com`)

### Getting Your Credentials

1. **API Key**: Found in your Braze dashboard under Settings → API Keys
2. **SDK Endpoint**: Located in Settings → SDK Authentication → Endpoints

## Integration

### Calling the API

Use the module-level API: call `initialize()` once, then call the exported functions. To switch configuration, call `destroy()` first, then `initialize()` again.

``` typescript
import { initialize, logPurchase, changeUser } from '@braze/javascript-sdk';

await initialize({ apiKey, baseUrl, options, ... });
await changeUser('user-123');
await logPurchase('sku-1', 9.99, 'USD', 1);
```

### Core Concepts

#### Required Implementations

The initialize configuration object requires `storageManager`. `networkManager` and `pushManager` are optional.

**1. StorageManager** - Async key-value storage interface
``` typescript
interface StorageManager {
  store(key: string, value: string, isId?: boolean): Promise<void>;
  remove(key: string, isId?: boolean): Promise<void>;
  retrieve(key: string, isId?: boolean): Promise<string | null>;
  clearData(storageKeys: string[]): Promise<void>;
}
```
- The `isId` parameter indicates **persistent ID storage**: when `true`, the SDK is storing a persistent identifier (device ID, user ID) or the opt-out flag. Implementations should persist these across app restarts so the SDK can recognize the same device/user. When `false`, the value is session/cache data (events, attributes, etc.) and may be in-memory only. For web environments, consider using cookies for keys stored with `isId: true` to ensure cross-session persistence.
- Must handle async operations for all storage operations

**2. NetworkManager** (optional) - HTTP POST request interface
``` typescript
interface NetworkManager {
  postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: globalThis.Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>>;
}
```
- Default implementation uses `fetch` API (requires global `fetch` and `URL`)
- Can be overwritten if `fetch` is not the preferred API
- Note: The SDK has retry and rate limiting logic already built in

**3. PushManager** (optional) - Push notification interface
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
- Only required if implementing push notifications

#### Data Flushing

The SDK automatically flushes cached data to Braze servers every 10 seconds (configurable via `flushIntervalInSeconds`). Use `requestImmediateDataFlush()` to force immediate synchronization.

### Integration Patterns

For method signatures, parameter and return types, and full API details, see the TypeScript definitions in the package.

#### Basic Integration

Complete working example with error handling:

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

#### Custom Storage Implementation

Complete StorageManager implementation with IndexedDB for persistent IDs:

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

#### Custom Network Implementation

NetworkManager that logs every outgoing request (SDK already handles errors and retries):

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

#### Error Handling

Complete error handling patterns:

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

#### Subscription Management

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

**Switching configuration:** Only one active session exists at a time. To switch configurations, call `destroy()` then `initialize()`:

``` typescript
import { destroy, initialize } from '@braze/javascript-sdk';

destroy();
await initialize({ /* new config */ });
```

### Common Use Cases

#### User Identification and Attribute Tracking

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

#### Event Logging and Analytics

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

#### In-App Message Handling

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

### Error Handling & Edge Cases

#### Common Error Conditions

**SDK Not Initialized:**
- Most methods return `undefined` (not throw) when SDK not initialized
- `initialize()` returns `false` if already initialized or validation fails
- `changeUser()` is a no-op and the promise resolves if SDK not initialized
- Always check for `undefined` return values before using them

**Validation Failures:**
- Invalid API key or base URL: `initialize()` returns `false`, logs error
- Invalid event names/keys: Must be max 255 chars, cannot start with `$`, alphanumeric + punctuation only
- Invalid attribute values: Strings max 255 chars, no newlines/tabs/double quotes, cannot start with `$`
- Invalid currency codes: Unsupported codes result in warning, no action taken
- Invalid purchase quantity: Must be 1-100, otherwise ignored

**Network Errors:**
- NetworkManager `postRequest()` should handle errors and reject promises appropriately
- Data flush controller retries failed requests automatically
- Use `requestImmediateDataFlush()` callback to detect flush failures

**Storage Errors:**
- StorageManager methods should handle errors gracefully
- If storage fails, SDK may not function correctly
- `isId` flag determines persistence: IDs persist across sessions, objects are session-scoped

**User Identification Edge Cases:**
- Cannot revert to anonymous user after identification
- User switch ends current session and starts new session
- Anonymous user history preserved when identifying for first time
- History merged if user exists on another device

**Session Management:**
- Sessions timeout after 30 minutes of inactivity (configurable)
- `openSession()` returns `true` for new session, `false` if resumed
- Must call `openSession()` after `changeUser()` or `setIdentifierToken()`

**Subscription Management:**
- Subscription callbacks are called synchronously when events occur
- Remove subscriptions to prevent memory leaks
- `removeAllSubscriptions()` clears all subscriptions at once

**Data Flushing:**
- Automatic flush every 10 seconds (configurable, minimum: 3 seconds)
- Flush may fail silently - use `requestImmediateDataFlush()` callback
- Data is queued if network unavailable, flushed when network restored

### Important Implementation Notes

1. **Most methods are async**: Async SDK methods return a Promise (use `await` or `.then()`). Some configuration and utility methods (for example, `destroy`, `toggleLogging`, `setLogger`) are synchronous; refer to the TypeScript definitions or quick reference table for details.

2. **Methods may return `undefined`**: If the SDK is not initialized, most methods return `undefined` instead of throwing. Check for `undefined` before using return values.

3. **Methods may return `null`**: Some methods return `null` to indicate "not found" (e.g., `getUserId()` returns `null` if the user is anonymous). This is different from `undefined` (SDK not initialized).

4. **Storage keys use `isId` flag**: The `isId` parameter in StorageManager methods distinguishes between:
   - ID storage: Persistent identifiers (device ID, user ID) that should persist across sessions
   - Object storage: Session-scoped data that can be cleared

5. **SDK metadata tags**: The `sdkMetadata` array identifies the platform/wrapper using the SDK (for example, `['npm']` or `[BrazeSdkMetadata.NPM]`). Valid tags are defined by the `BrazeSdkMetadata` enum (such as `npm`, `cdn`, `manu`, `shp`, `gg`, `kep`), and the SDK automatically adds `'wjs'` to indicate JavaScript SDK.

6. **Default NetworkManager**: If `networkManager` is not provided, the SDK uses a default implementation that requires global `fetch` and `URL` APIs. Provide a custom implementation if these are not available.

7. **PushManager is optional**: Only implement `PushManager` if you need push notification functionality. Can be omitted otherwise.

8. **Destroy and cleanup**: Call `destroy()` when you need to tear down the SDK. Only one active session can exist at a time; you must call `destroy()` before calling `initialize()` again. Doing so stops timers, flushes data, and releases resources.

9. **Data flushing**: Data is automatically flushed every 10 seconds (configurable). Use `requestImmediateDataFlush()` for immediate synchronization.

10. **Session management**: Always call `openSession()` after `changeUser()` or `setIdentifierToken()` to avoid creating duplicate anonymous users.

11. **Type safety**: The SDK is written in TypeScript with full type definitions. Use TypeScript for best experience and type checking.

12. **Validation rules**: Event names, attribute keys, and property keys have strict validation (max 255 chars, cannot start with `$`, alphanumeric + punctuation only). Invalid values may be ignored or cause errors.

## Debugging / Troubleshooting

Pass the option `enableLogging: true` to the initialization options. This is valuable for development but be sure to remove this option or [provide an alternate logger](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html#setlogger) before you release your page to production.

## Contact

If you have questions, please contact [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

For repository details and sample projects, see [https://github.com/braze-inc/braze-javascript-sdk](https://github.com/braze-inc/braze-javascript-sdk).
