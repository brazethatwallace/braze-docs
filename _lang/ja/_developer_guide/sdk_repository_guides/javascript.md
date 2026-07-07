---
nav_title: JavaScript SDK
article_title: JavaScript SDK リポジトリガイド
page_order: 4
description: "GitHubからミラーリングされたBraze JavaScript SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
# JavaScript SDK リポジトリガイド {#javascript-sdk-repository-guide}

## Braze JavaScript SDKについて {#about-the-braze-javascript-sdk}

Braze JavaScript SDKは、Brazeのメッセージング、分析、ユーザーエンゲージメント機能をアプリケーションに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド](https://www.braze.com/docs/user_guide/introduction/)
- [Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=javascript)

### アーキテクチャの概要 {#architecture-overview}

Braze JavaScript SDKは、純粋なJavaScript環境で動作するように設計された**プラットフォーム非依存**のライブラリです。ブラウザやNode.js固有のAPIを含まないため、さまざまなJavaScriptランタイムでの使用に適しています。

**主要な設計原則：**
- **依存性注入**: SDKはプラットフォーム固有のAPIを使用する代わりに、ストレージ、ネットワーキング、デバイス情報の実装を必要とします
- **非同期ファースト**: ほとんどのAPIメソッドは非同期でPromiseを返します。一部のユーティリティメソッド（例：`destroy`、`subscribeToInAppMessage`、`toggleLogging`、`setLogger`）は同期的です。正確なシグネチャについてはTypeScript定義を参照してください。
- **シングルトンセッション**: モジュールレベルAPI（`initialize`/`destroy`）は、一度に1つのアクティブなSDKセッションを管理します。
- **内部依存関係管理**: 提供された実装から内部依存関係（UserManager、SessionManager、DataFlushControllerなど）を作成・管理します

<!--
Effective marketing automation is an essential part of successfully scaling and managing your business. Braze empowers you to build better customer relationships through a seamless, multi-channel approach that addresses all aspects of the user life cycle. Braze helps you engage your users on an ongoing basis. We'll have you up and running in no time!

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction)
- [Initial Web SDK Setup](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)
- [Braze Web SDK Documentation](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html) -->

## クイックスタート {#quickstart}

npmでSDKをインストールします：

``` bash
npm install @braze/javascript-sdk
```

またはyarnで：

``` bash
yarn add @braze/javascript-sdk
```

モジュールレベルAPIを使用する場合：
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

## 前提条件 {#prerequisites}

Braze JavaScript SDKを統合する前に、以下が必要です：

- **Brazeアカウント**: APIアクセスが可能なBrazeアカウント
- **APIキー**: BrazeダッシュボードからのアプリのAPIキー
- **SDKエンドポイント**: BrazeのSDKエンドポイントURL（例：`sdk.iad-01.braze.com`）

### 認証情報の取得 {#getting-your-credentials}

1. **APIキー**: Brazeダッシュボードの**設定** > **APIキー**にあります
2. **SDKエンドポイント**: **設定** > **SDK認証** > **エンドポイント**にあります

## 統合 {#integration}

### APIの呼び出し {#calling-the-api}

モジュールレベルAPIを使用します。`initialize()`を一度呼び出してから、エクスポートされた関数を呼び出します。設定を切り替えるには、まず`destroy()`を呼び出してから、再度`initialize()`を呼び出します。

``` typescript
import { initialize, logPurchase, changeUser } from '@braze/javascript-sdk';

await initialize({ apiKey, baseUrl, options, ... });
await changeUser('user-123');
await logPurchase('sku-1', 9.99, 'USD', 1);
```

### コアコンセプト {#core-concepts}

#### 必須の実装 {#required-implementations}

初期化設定オブジェクトには`storageManager`が必須です。`networkManager`と`pushManager`はオプションです。

**1. StorageManager** - 非同期キーバリューストレージインターフェイス
``` typescript
interface StorageManager {
  store(key: string, value: string, isId?: boolean): Promise<void>;
  remove(key: string, isId?: boolean): Promise<void>;
  retrieve(key: string, isId?: boolean): Promise<string | null>;
  clearData(storageKeys: string[]): Promise<void>;
}
```
- `isId`パラメーターは**永続的なIDストレージ**を示します。`true`の場合、SDKは永続的な識別子（デバイスID、ユーザーID）またはオプトアウトフラグを保存しています。実装では、SDKが同じデバイス/ユーザーを認識できるように、アプリの再起動後もこれらを永続化する必要があります。`false`の場合、値はセッション/キャッシュデータ（イベント、属性など）であり、メモリ内のみでも構いません。Web環境では、クロスセッションの永続性を確保するために、`isId: true`で保存されるキーにはCookieの使用を検討してください。
- すべてのストレージ操作で非同期操作を処理する必要があります

**2. NetworkManager**（オプション）- HTTP POSTリクエストインターフェイス
``` typescript
interface NetworkManager {
  postRequest(
    url: string,
    data: Partial<Record<string, unknown>>,
    headers?: globalThis.Headers | [string, string][]
  ): Promise<Partial<Record<string, unknown>>>;
}
```
- デフォルトの実装は`fetch` APIを使用します（グローバルな`fetch`と`URL`が必要）
- `fetch`が推奨APIでない場合は上書きできます
- 注：SDKにはリトライとレート制限のロジックがすでに組み込まれています

**3. PushManager**（オプション）- プッシュ通知インターフェイス
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
- プッシュ通知を実装する場合にのみ必要です

#### データフラッシュ {#data-flushing}

SDKは、キャッシュされたデータを10秒ごとに自動的にBrazeサーバーにフラッシュします（`flushIntervalInSeconds`で設定可能）。即時同期を強制するには`requestImmediateDataFlush()`を使用します。

### 統合パターン {#integration-patterns}

メソッドシグネチャ、パラメーターと戻り値の型、および完全なAPIの詳細については、パッケージ内のTypeScript定義を参照してください。

#### 基本的な統合 {#basic-integration}

エラーハンドリングを含む完全な動作例：

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

#### カスタムストレージ実装 {#custom-storage-implementation}

永続的なIDのためのIndexedDBを使用した完全なStorageManager実装：

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

#### カスタムネットワーク実装 {#custom-network-implementation}

すべての送信リクエストをログに記録するNetworkManager（SDKはエラーとリトライをすでに処理しています）：

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

#### エラーハンドリング {#error-handling}

完全なエラーハンドリングパターン：

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

#### 購読管理 {#subscription-management}

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

**設定の切り替え：** 一度にアクティブなセッションは1つだけ存在します。設定を切り替えるには、`destroy()`を呼び出してから`initialize()`を呼び出します：

``` typescript
import { destroy, initialize } from '@braze/javascript-sdk';

destroy();
await initialize({ /* new config */ });
```

### 一般的なユースケース {#common-use-cases}

#### ユーザー識別と属性トラッキング {#user-identification-and-attribute-tracking}

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

#### イベントログと分析 {#event-logging-and-analytics}

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

#### アプリ内メッセージの処理 {#in-app-message-handling}

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

### エラーハンドリングとエッジケース {#error-handling-edge-cases}

#### 一般的なエラー条件 {#common-error-conditions}

**SDKが初期化されていない場合：**
- ほとんどのメソッドは、SDKが初期化されていない場合にスローするのではなく`undefined`を返します
- `initialize()`は、すでに初期化されているかバリデーションに失敗した場合に`false`を返します
- `changeUser()`は、SDKが初期化されていない場合はno-opとなり、Promiseが解決されます
- 戻り値を使用する前に、常に`undefined`をチェックしてください

**バリデーション失敗：**
- 無効なAPIキーまたはベースURL：`initialize()`が`false`を返し、エラーをログに記録します
- 無効なイベント名/キー：最大255文字、`$`で始めることはできず、英数字と句読点のみ使用可能です
- 無効な属性値：文字列は最大255文字、改行/タブ/ダブルクォートは使用不可、`$`で始めることはできません
- 無効な通貨コード：サポートされていないコードは警告が表示され、アクションは実行されません
- 無効な購入数量：1〜100の範囲でなければならず、それ以外は無視されます

**ネットワークエラー：**
- NetworkManagerの`postRequest()`はエラーを適切に処理し、Promiseをリジェクトする必要があります
- データフラッシュコントローラーは失敗したリクエストを自動的にリトライします
- フラッシュの失敗を検出するには`requestImmediateDataFlush()`コールバックを使用します

**ストレージエラー：**
- StorageManagerのメソッドはエラーを適切に処理する必要があります
- ストレージが失敗した場合、SDKが正しく機能しない可能性があります
- `isId`フラグが永続性を決定します：IDはセッション間で永続化され、オブジェクトはセッションスコープです

**ユーザー識別のエッジケース：**
- 識別後に匿名ユーザーに戻すことはできません
- ユーザーの切り替えにより、現在のセッションが終了し、新しいセッションが開始されます
- 初回識別時に匿名ユーザーの履歴が保持されます
- 別のデバイスにユーザーが存在する場合、履歴がマージされます

**セッション管理：**
- セッションは30分間の非アクティブ後にタイムアウトします（設定可能）
- `openSession()`は新しいセッションの場合`true`を、再開の場合`false`を返します
- `changeUser()`または`setIdentifierToken()`の後に`openSession()`を呼び出す必要があります

**購読管理：**
- 購読コールバックは、イベント発生時に同期的に呼び出されます
- メモリリークを防ぐために購読を削除してください
- `removeAllSubscriptions()`はすべての購読を一度にクリアします

**データフラッシュ：**
- 10秒ごとに自動フラッシュ（設定可能、最小：3秒）
- フラッシュはサイレントに失敗する場合があります - `requestImmediateDataFlush()`コールバックを使用してください
- ネットワークが利用できない場合、データはキューに入れられ、ネットワーク復旧時にフラッシュされます

### 重要な実装上の注意事項 {#important-implementation-notes}

1. **ほとんどのメソッドは非同期です**: 非同期SDKメソッドはPromiseを返します（`await`または`.then()`を使用してください）。一部の設定およびユーティリティメソッド（例：`destroy`、`toggleLogging`、`setLogger`）は同期的です。詳細についてはTypeScript定義またはクイックリファレンステーブルを参照してください。

2. **メソッドが`undefined`を返す場合があります**: SDKが初期化されていない場合、ほとんどのメソッドはスローする代わりに`undefined`を返します。戻り値を使用する前に`undefined`をチェックしてください。

3. **メソッドが`null`を返す場合があります**: 一部のメソッドは「見つからない」ことを示すために`null`を返します（例：`getUserId()`はユーザーが匿名の場合`null`を返します）。これは`undefined`（SDKが初期化されていない）とは異なります。

4. **ストレージキーは`isId`フラグを使用します**: StorageManagerメソッドの`isId`パラメーターは以下を区別します：
   - IDストレージ：セッション間で永続化する必要がある永続的な識別子（デバイスID、ユーザーID）
   - オブジェクトストレージ：クリア可能なセッションスコープのデータ

5. **SDKメタデータタグ**: `sdkMetadata`配列は、SDKを使用しているプラットフォーム/ラッパーを識別します（例：`['npm']`または`[BrazeSdkMetadata.NPM]`）。有効なタグは`BrazeSdkMetadata`列挙型（`npm`、`cdn`、`manu`、`shp`、`gg`、`kep`など）で定義されており、SDKはJavaScript SDKを示す`'wjs'`を自動的に追加します。

6. **デフォルトのNetworkManager**: `networkManager`が提供されない場合、SDKはグローバルな`fetch`と`URL` APIを必要とするデフォルトの実装を使用します。これらが利用できない場合は、カスタム実装を提供してください。

7. **PushManagerはオプションです**: プッシュ通知機能が必要な場合にのみ`PushManager`を実装してください。それ以外の場合は省略できます。

8. **破棄とクリーンアップ**: SDKを破棄する必要がある場合は`destroy()`を呼び出します。一度にアクティブなセッションは1つだけ存在できます。再度`initialize()`を呼び出す前に`destroy()`を呼び出す必要があります。これにより、タイマーが停止し、データがフラッシュされ、リソースが解放されます。

9. **データフラッシュ**: データは10秒ごとに自動的にフラッシュされます（設定可能）。即時同期には`requestImmediateDataFlush()`を使用してください。

10. **セッション管理**: 重複する匿名ユーザーの作成を避けるため、`changeUser()`または`setIdentifierToken()`の後に必ず`openSession()`を呼び出してください。

11. **型安全性**: SDKはTypeScriptで記述されており、完全な型定義が含まれています。最良のエクスペリエンスと型チェックのためにTypeScriptを使用してください。

12. **バリデーションルール**: イベント名、属性キー、プロパティキーには厳格なバリデーションがあります（最大255文字、`$`で始めることはできず、英数字と句読点のみ使用可能）。無効な値は無視されるか、エラーが発生する場合があります。

## デバッグ / トラブルシューティング {#debugging-troubleshooting}

初期化オプションに`enableLogging: true`を渡します。これは開発時に有用ですが、本番環境にページをリリースする前に、このオプションを削除するか、[代替のロガーを提供](https://js.appboycdn.com/web-sdk/{{VERSION}}/doc/modules/braze.html#setlogger)してください。

## お問い合わせ {#contact}

ご質問がある場合は、[support@braze.com](mailto:support@braze.com)までお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-javascript-sdk](https://github.com/braze-inc/braze-javascript-sdk)を参照してください。