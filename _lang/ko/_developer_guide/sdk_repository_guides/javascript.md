---
nav_title: JavaScript SDK
article_title: JavaScript SDK 리포지토리 가이드
page_order: 4
description: "GitHub에서 미러링된 Braze JavaScript SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
# JavaScript SDK 리포지토리 가이드 {#javascript-sdk-repository-guide}

## Braze JavaScript SDK 소개 {#about-the-braze-javascript-sdk}

Braze JavaScript SDK는 Braze 메시징, 분석, 사용자 인게이지먼트 기능을 애플리케이션에 통합할 수 있도록 도와줍니다.

시작하려면 다음 리소스를 참조하세요:

- [Braze 사용자 가이드](https://www.braze.com/docs/user_guide/introduction/)
- [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=javascript)

### 아키텍처 개요 {#architecture-overview}

Braze JavaScript SDK는 순수 JavaScript 환경에서 작동하도록 설계된 **플랫폼 독립적** 라이브러리입니다. 브라우저 또는 Node.js 전용 API를 포함하지 않으므로 다양한 JavaScript 런타임에서 사용할 수 있습니다.

**주요 설계 원칙:**
- **의존성 주입**: SDK는 플랫폼별 API를 사용하는 대신 스토리지, 네트워킹, 기기 정보에 대한 구현을 요구합니다
- **비동기 우선**: 대부분의 API 메서드는 비동기이며 Promise를 반환합니다. 일부 유틸리티 메서드(예: `destroy`, `subscribeToInAppMessage`, `toggleLogging`, `setLogger`)는 동기식입니다. 정확한 시그니처는 TypeScript 정의를 참조하세요.
- **싱글톤 세션**: 모듈 수준 API(`initialize`/`destroy`)는 한 번에 하나의 활성 SDK 세션을 관리합니다.
- **내부 의존성 관리**: 제공된 구현으로부터 내부 의존성(UserManager, SessionManager, DataFlushController 등)을 생성하고 관리합니다

<!--
Effective marketing automation is an essential part of successfully scaling and managing your business. Braze empowers you to build better customer relationships through a seamless, multi-channel approach that addresses all aspects of the user life cycle. Braze helps you engage your users on an ongoing basis. We'll have you up and running in no time!

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction)
- [Initial Web SDK Setup](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)
- [Braze Web SDK Documentation](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html) -->

## 빠른 시작 {#quickstart}

npm으로 SDK를 설치합니다:

``` bash
npm install @braze/javascript-sdk
```

또는 yarn으로 설치합니다:

``` bash
yarn add @braze/javascript-sdk
```

모듈 수준 API 사용:
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

## 필수 조건 {#prerequisites}

Braze JavaScript SDK를 통합하기 전에 다음이 필요합니다:

- **Braze 계정**: API 접근 권한이 있는 Braze 계정
- **API 키**: Braze 대시보드에서 확인할 수 있는 앱의 API 키
- **SDK 엔드포인트**: Braze SDK 엔드포인트 URL(예: `sdk.iad-01.braze.com`)

### 자격 증명 확인하기 {#getting-your-credentials}

1. **API 키**: Braze 대시보드에서 **설정** > **API 키**에서 확인할 수 있습니다
2. **SDK 엔드포인트**: **설정** > **SDK 인증** > **엔드포인트**에서 확인할 수 있습니다

## 통합 {#integration}

### API 호출하기 {#calling-the-api}

모듈 수준 API를 사용합니다: `initialize()`를 한 번 호출한 다음 내보낸 함수를 호출합니다. 구성을 전환하려면 먼저 `destroy()`를 호출한 다음 `initialize()`를 다시 호출합니다.

``` typescript
import { initialize, logPurchase, changeUser } from '@braze/javascript-sdk';

await initialize({ apiKey, baseUrl, options, ... });
await changeUser('user-123');
await logPurchase('sku-1', 9.99, 'USD', 1);
```

### 핵심 개념 {#core-concepts}

#### 필수 구현 {#required-implementations}

initialize 구성 오브젝트에는 `storageManager`가 필수입니다. `networkManager`와 `pushManager`는 선택 사항입니다.

**1. StorageManager** - 비동기 키-값 스토리지 인터페이스
``` typescript
interface StorageManager {
  store(key: string, value: string, isId?: boolean): Promise<void>;
  remove(key: string, isId?: boolean): Promise<void>;
  retrieve(key: string, isId?: boolean): Promise<string | null>;
  clearData(storageKeys: string[]): Promise<void>;
}
```
- `isId` 매개변수는 **영구 ID 스토리지**를 나타냅니다: `true`인 경우 SDK는 영구 식별자(기기 ID, 사용자 ID) 또는 옵트아웃 플래그를 저장합니다. 구현 시 앱 재시작 후에도 이러한 값을 유지하여 SDK가 동일한 기기/사용자를 인식할 수 있도록 해야 합니다. `false`인 경우 값은 세션/캐시 데이터(이벤트, 속성 등)이며 메모리에만 저장될 수 있습니다. 웹 환경에서는 `isId: true`로 저장되는 키에 쿠키를 사용하여 세션 간 지속성을 보장하는 것을 고려하세요.
- 모든 스토리지 작업에 대해 비동기 작업을 처리해야 합니다

**2. NetworkManager** (선택 사항) - HTTP POST 요청 인터페이스
``` typescript
interface NetworkManager {
  postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: globalThis.Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>>;
}
```
- 기본 구현은 `fetch` API를 사용합니다(전역 `fetch` 및 `URL` 필요)
- `fetch`가 선호하는 API가 아닌 경우 덮어쓸 수 있습니다
- 참고: SDK에는 재시도 및 사용량 제한 로직이 이미 내장되어 있습니다

**3. PushManager** (선택 사항) - 푸시 알림 인터페이스
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
- 푸시 알림을 구현하는 경우에만 필요합니다

#### 데이터 플러시 {#data-flushing}

SDK는 캐시된 데이터를 10초마다(`flushIntervalInSeconds`로 구성 가능) Braze 서버로 자동 플러시합니다. 즉시 동기화를 강제하려면 `requestImmediateDataFlush()`를 사용하세요.

### 통합 패턴 {#integration-patterns}

메서드 시그니처, 매개변수 및 반환 타입, 전체 API 세부 정보는 패키지의 TypeScript 정의를 참조하세요.

#### 기본 통합 {#basic-integration}

오류 처리가 포함된 완전한 작동 예제:

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

#### 커스텀 스토리지 구현 {#custom-storage-implementation}

영구 ID를 위한 IndexedDB를 사용한 완전한 StorageManager 구현:

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

#### 커스텀 네트워크 구현 {#custom-network-implementation}

모든 발신 요청을 로깅하는 NetworkManager(SDK가 이미 오류 및 재시도를 처리합니다):

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

#### 오류 처리 {#error-handling}

완전한 오류 처리 패턴:

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

#### 구독 관리 {#subscription-management}

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

**구성 전환:** 한 번에 하나의 활성 세션만 존재합니다. 구성을 전환하려면 `destroy()`를 호출한 다음 `initialize()`를 호출합니다:

``` typescript
import { destroy, initialize } from '@braze/javascript-sdk';

destroy();
await initialize({ /* new config */ });
```

### 일반적인 사용 사례 {#common-use-cases}

#### 사용자 식별 및 속성 추적 {#user-identification-and-attribute-tracking}

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

#### 이벤트 로깅 및 분석 {#event-logging-and-analytics}

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

#### 인앱 메시지 처리 {#in-app-message-handling}

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

### 오류 처리 및 엣지 케이스 {#error-handling-edge-cases}

#### 일반적인 오류 조건 {#common-error-conditions}

**SDK가 초기화되지 않은 경우:**
- 대부분의 메서드는 SDK가 초기화되지 않은 경우 throw하지 않고 `undefined`를 반환합니다
- `initialize()`는 이미 초기화되었거나 유효성 검사에 실패한 경우 `false`를 반환합니다
- `changeUser()`는 SDK가 초기화되지 않은 경우 아무 작업도 수행하지 않으며 Promise가 resolve됩니다
- 반환 값을 사용하기 전에 항상 `undefined`를 확인하세요

**유효성 검사 실패:**
- 잘못된 API 키 또는 기본 URL: `initialize()`가 `false`를 반환하고 오류를 로깅합니다
- 잘못된 이벤트 이름/키: 최대 255자, `$`로 시작할 수 없으며, 영숫자 + 구두점만 허용됩니다
- 잘못된 속성 값: 문자열 최대 255자, 줄바꿈/탭/큰따옴표 불가, `$`로 시작할 수 없습니다
- 잘못된 통화 코드: 지원되지 않는 코드는 경고가 발생하며 아무 작업도 수행되지 않습니다
- 잘못된 구매 수량: 1-100이어야 하며, 그렇지 않으면 무시됩니다

**네트워크 오류:**
- NetworkManager `postRequest()`는 오류를 처리하고 Promise를 적절히 reject해야 합니다
- 데이터 플러시 컨트롤러는 실패한 요청을 자동으로 재시도합니다
- `requestImmediateDataFlush()` 콜백을 사용하여 플러시 실패를 감지합니다

**스토리지 오류:**
- StorageManager 메서드는 오류를 적절히 처리해야 합니다
- 스토리지가 실패하면 SDK가 올바르게 작동하지 않을 수 있습니다
- `isId` 플래그가 지속성을 결정합니다: ID는 세션 간에 유지되고, 오브젝트는 세션 범위입니다

**사용자 식별 엣지 케이스:**
- 식별 후 익명 사용자로 되돌릴 수 없습니다
- 사용자 전환 시 현재 세션이 종료되고 새 세션이 시작됩니다
- 처음 식별할 때 익명 사용자 기록이 보존됩니다
- 다른 기기에 사용자가 존재하는 경우 기록이 병합됩니다

**세션 관리:**
- 세션은 30분간 비활성 상태 후 타임아웃됩니다(구성 가능)
- `openSession()`은 새 세션인 경우 `true`를, 재개된 경우 `false`를 반환합니다
- `changeUser()` 또는 `setIdentifierToken()` 이후에 `openSession()`을 호출해야 합니다

**구독 관리:**
- 구독 콜백은 이벤트 발생 시 동기적으로 호출됩니다
- 메모리 누수를 방지하기 위해 구독을 제거하세요
- `removeAllSubscriptions()`는 모든 구독을 한 번에 제거합니다

**데이터 플러시:**
- 10초마다 자동 플러시(구성 가능, 최소: 3초)
- 플러시가 조용히 실패할 수 있습니다 - `requestImmediateDataFlush()` 콜백을 사용하세요
- 네트워크를 사용할 수 없는 경우 데이터가 대기열에 추가되고, 네트워크가 복원되면 플러시됩니다

### 중요한 구현 참고 사항 {#important-implementation-notes}

1. **대부분의 메서드는 비동기입니다**: 비동기 SDK 메서드는 Promise를 반환합니다(`await` 또는 `.then()`을 사용하세요). 일부 구성 및 유틸리티 메서드(예: `destroy`, `toggleLogging`, `setLogger`)는 동기식입니다. 자세한 내용은 TypeScript 정의 또는 빠른 참조 표를 참조하세요.

2. **메서드가 `undefined`를 반환할 수 있습니다**: SDK가 초기화되지 않은 경우 대부분의 메서드는 throw하지 않고 `undefined`를 반환합니다. 반환 값을 사용하기 전에 `undefined`를 확인하세요.

3. **메서드가 `null`을 반환할 수 있습니다**: 일부 메서드는 "찾을 수 없음"을 나타내기 위해 `null`을 반환합니다(예: `getUserId()`는 사용자가 익명인 경우 `null`을 반환합니다). 이는 `undefined`(SDK가 초기화되지 않음)와 다릅니다.

4. **스토리지 키는 `isId` 플래그를 사용합니다**: StorageManager 메서드의 `isId` 매개변수는 다음을 구분합니다:
   - ID 스토리지: 세션 간에 유지되어야 하는 영구 식별자(기기 ID, 사용자 ID)
   - 오브젝트 스토리지: 삭제할 수 있는 세션 범위 데이터

5. **SDK 메타데이터 태그**: `sdkMetadata` 배열은 SDK를 사용하는 플랫폼/래퍼를 식별합니다(예: `['npm']` 또는 `[BrazeSdkMetadata.NPM]`). 유효한 태그는 `BrazeSdkMetadata` 열거형(예: `npm`, `cdn`, `manu`, `shp`, `gg`, `kep`)으로 정의되며, SDK는 JavaScript SDK를 나타내기 위해 자동으로 `'wjs'`를 추가합니다.

6. **기본 NetworkManager**: `networkManager`가 제공되지 않으면 SDK는 전역 `fetch` 및 `URL` API가 필요한 기본 구현을 사용합니다. 이러한 API를 사용할 수 없는 경우 커스텀 구현을 제공하세요.

7. **PushManager는 선택 사항입니다**: 푸시 알림 기능이 필요한 경우에만 `PushManager`를 구현하세요. 그렇지 않으면 생략할 수 있습니다.

8. **정리 및 해제**: SDK를 해제해야 할 때 `destroy()`를 호출하세요. 한 번에 하나의 활성 세션만 존재할 수 있으므로 `initialize()`를 다시 호출하기 전에 `destroy()`를 호출해야 합니다. 이렇게 하면 타이머가 중지되고, 데이터가 플러시되며, 리소스가 해제됩니다.

9. **데이터 플러시**: 데이터는 10초마다 자동으로 플러시됩니다(구성 가능). 즉시 동기화하려면 `requestImmediateDataFlush()`를 사용하세요.

10. **세션 관리**: 중복 익명 사용자 생성을 방지하려면 `changeUser()` 또는 `setIdentifierToken()` 이후에 항상 `openSession()`을 호출하세요.

11. **타입 안전성**: SDK는 완전한 타입 정의와 함께 TypeScript로 작성되었습니다. 최상의 경험과 타입 검사를 위해 TypeScript를 사용하세요.

12. **유효성 검사 규칙**: 이벤트 이름, 속성 키, 속성정보 키에는 엄격한 유효성 검사가 적용됩니다(최대 255자, `$`로 시작할 수 없음, 영숫자 + 구두점만 허용). 잘못된 값은 무시되거나 오류를 발생시킬 수 있습니다.

## 디버깅 / 문제 해결 {#debugging-troubleshooting}

초기화 옵션에 `enableLogging: true` 옵션을 전달하세요. 이는 개발 시 유용하지만, 페이지를 프로덕션에 배포하기 전에 이 옵션을 제거하거나 [대체 로거를 제공](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html#setlogger)해야 합니다.

## 문의 {#contact}

질문이 있으시면 [support@braze.com](mailto:support@braze.com)으로 연락해 주세요.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-javascript-sdk](https://github.com/braze-inc/braze-javascript-sdk)를 참조하세요.