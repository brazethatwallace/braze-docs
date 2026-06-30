---
nav_title: Web SDK
article_title: Web SDK リポジトリガイド
page_order: 1
description: "GitHubからミラーリングされたBraze Web SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Web SDKについて {#about-the-braze-web-sdk}

Braze Web SDKを使用すると、BrazeのカスタマーエンゲージメントプラットフォームをWebアプリケーションに直接統合できます。TypeScriptで構築され、モダンなWeb開発向けに設計されたこのSDKは、ユーザー管理、メッセージング、分析、フィーチャーフラグのための包括的なツールを提供します。

### できること {#what-you-can-do}

- **ユーザー管理**: Webアプリケーション全体でユーザーのアイデンティティ、属性、動作を追跡・管理します
- **アプリ内メッセージング**: ユーザーがサイトをアクティブに使用している間に、ターゲットを絞ったメッセージや通知を表示します
- **Content Cards**: リアルタイムで更新されるパーソナライズされたコンテンツフィードやプロモーションカードを表示します
- **バナー**: サイト内の特定のプレースメントにバナーメッセージを表示します
- **プッシュ通知**: ユーザーがサイトにいないときでもWebプッシュ通知を送信してエンゲージメントを促進します
- **フィーチャーフラグ**: サーバーサイドのフィーチャーフラグ管理で機能のロールアウトやABテストを制御します
- **分析**: カスタムイベント、ユーザーインタラクション、コンバージョン指標を追跡します
- **セッション管理**: ユーザーセッションとエンゲージメントパターンを監視します

シングルページアプリケーション、ECサイト、コンテンツプラットフォームのいずれを構築する場合でも、Braze Web SDKは成長とリテンションを促進するパーソナライズされた魅力的なユーザー体験を作成するために必要なツールを提供します。

## 前提条件 {#prerequisites}

Braze Web SDKを統合する前に、以下が必要です。

- **Brazeアカウント**: APIアクセスが可能なBrazeアカウント
- **APIキー**: BrazeダッシュボードからのアプリのAPIキー
- **SDKエンドポイント**: BrazeのSDKエンドポイントURL（例: `sdk.iad-01.braze.com`）

### 認証情報の取得 {#getting-your-credentials}

1. **APIキー**: Brazeダッシュボードの**設定** > **APIキー**にあります
2. **SDKエンドポイント**: **設定** > **SDK認証** > **エンドポイント**にあります
3. **Service Worker**: プッシュ通知に必要です（プッシュ通知セクションを参照）

## インストール {#installation}

``` bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

## クイックスタート {#quick-start}

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});

braze.changeUser('Jane Doe');
```

## 設定リファレンス {#configuration-reference}

### 初期化オプション {#initialization-options}

`initialize`関数は、以下のプロパティを持つオプションオブジェクトを受け取ります。

| オプション | 型 | デフォルト | 説明 |
|--------|------|---------|-------------|
| `baseUrl` | `string` | **必須** | このオプションは、統合に適切なエンドポイントを使用するようBraze Web SDKを設定するために必須です。例: `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | デフォルトでログを有効にするにはtrueに設定します。これによりBrazeがJavaScriptコンソールにログを出力するようになり、すべてのユーザーに表示されます。本番環境にリリースする前に、このオプションを削除するか、setLoggerで代替ロガーを提供してください。 |
| `allowUserSuppliedJavascript` | `boolean` | `false` | デフォルトでは、Braze Web SDKはユーザー提供のJavaScriptクリックアクションを許可せず、HTMLアプリ内メッセージやバナーも有効にしません。これらはBrazeダッシュボードのユーザーがサイト上でJavaScriptを実行できるようにするためです。Brazeダッシュボードのユーザーが悪意のないJavaScriptクリックアクションを記述することを信頼する場合は、このプロパティをtrueに設定してください。 |
| `doNotLoadFontAwesome` | `boolean` | `false` | Brazeはアプリ内メッセージのアイコンにFont Awesomeを使用しています。デフォルトでは、BrazeはFontAwesome CDNからFontAwesome 4.7.0を自動的に読み込みます。この動作を無効にするには（例えば、サイトでカスタマイズされたバージョンのFontAwesomeを使用している場合）、このオプションを`true`に設定してください。この場合、サイトでFontAwesomeが読み込まれていることを確認する責任はお客様にあります。そうしないと、アプリ内メッセージが正しくレンダリングされない場合があります。 |
| `inAppMessageZIndex` | `number` | `999999` | デフォルトでは、Braze SDKはアプリ内メッセージをz-index 999999で表示します。このオプションに値を指定すると、そのデフォルトを上書きできます。 |
| `sessionTimeoutInSeconds` | `number` | `30` | デフォルトでは、セッションは30秒間操作がないとタイムアウトします。このオプションに値を指定すると、そのデフォルトを上書きできます。 |
| `deviceId` | `string` | 自動生成 | デフォルトでは、BrazeはデバイスIDとしてランダムなGUIDを割り当てます。この設定オプションに値を指定すると、そのデフォルトを独自の値で上書きできます。 |
| `appVersion` | `string` | `undefined` | このオプションに値を指定すると、Brazeに送信されるユーザーイベントが指定されたバージョンに関連付けられ、ユーザーセグメンテーションに使用できます。 |
| `appVersionNumber` | `string` | `undefined` | ユーザーセグメンテーションに使用できる数値のアプリバージョン値です。この値は「1.2.3.4」のように4つのフィールドで送信する必要があり、そうでない場合は無視されます。注: `appVersion`も設定する必要があり、同じ値またはこのバージョンの一意の名前を使用してください。 |
| `contentSecurityNonce` | `string` | `undefined` | このオプションに値を指定すると、Braze SDKはSDKが作成するすべての`<script>`および`<style>`要素にnonceを追加します。これにより、WebサイトのContent Security PolicyでBraze SDKを動作させることができます。このnonceの設定に加えて、FontAwesomeの読み込みを許可する必要がある場合があります。Content Security Policyの許可リストに`use.fontawesome.com`を追加するか、`doNotLoadFontAwesome`オプションを使用して手動で読み込んでください。 |
| `noCookies` | `boolean` | `false` | デフォルトでは、Braze Web SDKはCookieを使用します。Cookieの使用を無効にするには、このオプションをtrueに設定してください。Cookieを無効にすると、セッション間でユーザーのアイデンティティを記憶するSDKの機能に影響を与える可能性があります。 |
| `allowCrawlerActivity` | `boolean` | `false` | デフォルトでは、Braze Web SDKはユーザーエージェント文字列に基づいて、Googleなどの既知のスパイダーやWebクローラーからのアクティビティを無視します。これによりデータポイントが節約され、分析がより正確になり、ページランクが向上する可能性があります。ただし、Brazeにこれらのクローラーからのアクティビティを記録させたい場合は、このオプションをtrueに設定できます。 |
| `disablePushTokenMaintenance` | `boolean` | `false` | デフォルトでは、すでにWebプッシュ許可を付与しているユーザー（例: requestPushPermissionまたは以前のプッシュプロバイダーを通じて）は、配信性を確保するために新しいセッションでBrazeバックエンドとプッシュトークンを自動的に同期します。この動作を無効にするには、このオプションをtrueに設定してください。 |
| `enableSdkAuthentication` | `boolean` | `false` | SDK認証機能を有効にするにはtrueに設定します。SDK認証の詳細については、製品ドキュメントを参照してください。 |
| `manageServiceWorkerExternally` | `boolean` | `false` | デフォルトでは、Braze Web SDKはプッシュ通知用に独自のService Workerを管理します。アプリケーションですでにService Workerを管理しており、BrazeのService Worker機能を組み込みたい場合は、このオプションをtrueに設定し、Service WorkerファイルにBrazeのService Workerコードを含めてください。 |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | デフォルトでは、トリガーアクション（例: アプリ内メッセージの表示）はユーザーごとに30秒に1回のみ実行できます。このオプションに値を指定すると、そのデフォルトを上書きできます。 |
| `serviceWorkerLocation` | `string` | `undefined` | デフォルトでは、Braze Web SDKはドメインのルートでService Workerファイルを探します。このオプションに値を指定すると、そのデフォルトを上書きし、Service Workerファイルのカスタムロケーションを指定できます。 |
| `safariWebsitePushId` | `string` | `undefined` | Safariプッシュ通知に必須です。この値はApple Developerアカウントで確認できます。Safariプッシュ通知の設定の詳細については、製品ドキュメントを参照してください。 |
| `localization` | `string` | `undefined` | このオプションに値を指定すると、Braze SDKはそのロケールでアプリ内メッセージやContent Cardsを表示しようとします。 |
| `openInAppMessagesInNewTab` | `boolean` | `false` | デフォルトでは、アプリ内メッセージのリンクは同じタブで開きます。新しいタブで開くようにするには、このオプションをtrueに設定してください。 |
| `openCardsInNewTab` | `boolean` | `false` | デフォルトでは、Content Cardsのリンクは同じタブで開きます。新しいタブで開くようにするには、このオプションをtrueに設定してください。 |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | デフォルトでは、アプリ内メッセージはメッセージの外側をクリックするかEscapeキーを押すことで閉じることができます。ユーザーが明示的に閉じるボタンまたはアクションボタンをクリックしてメッセージを閉じることを要求するには、このオプションをtrueに設定してください。 |
| `devicePropertyAllowlist` | `string[]` | `undefined` | デフォルトでは、Braze SDKはDevicePropertiesのすべてのデバイスプロパティを自動的に検出して収集します。この動作を上書きするには、DevicePropertiesの配列を指定してください。すべてのプロパティのBrazeサーバーへの送信を無効にするには、空の配列を指定してください。一部のプロパティがないと、すべての機能が正しく動作しない場合があります。例えば、タイムゾーンがないと、ローカルタイムゾーン配信が機能しません。 |
| `serviceWorkerScope` | `string` | `undefined` | デフォルトでは、Braze Web SDKはデフォルトのスコープ（Service Workerのディレクトリ）でService Workerを登録します。このオプションに値を指定すると、そのデフォルトを上書きし、Service Workerのカスタムスコープを指定できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="初期化オプション" }

---

## コア機能 {#core-features}

### 初期化とセットアップ {#initialization-setup}

#### 基本的な初期化 {#basic-initialization}

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

#### 高度な初期化オプション {#advanced-initialization-options}

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

### ユーザー管理 {#user-management}

#### ユーザーの変更 {#change-user}

``` typescript
import { changeUser } from "@braze/web-sdk";

// Change to a new user
changeUser('user-123');
```

#### ユーザー属性の設定 {#set-user-attributes}

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

#### ユーザーロケーションの設定 {#set-user-location}

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

#### ユーザーエイリアスとサブスクリプショングループ {#user-aliases-and-subscription-groups}

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

#### ユーザーのログアウト {#user-logout}

``` typescript
import { wipeData } from "@braze/web-sdk";

// There is no explicit method to logout. To "forget" the current users entirely, use wipeData().
// This is a complete data wipe (use with caution, this wipes things such as device ID)
wipeData();
```

### In-App Messages

#### 自動表示 {#automatic-display}

``` typescript
import { automaticallyShowInAppMessages } from "@braze/web-sdk";

// Automatically show in-app messages
automaticallyShowInAppMessages();
```

#### 手動表示 {#manual-display}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

// Subscribe to in-app messages
subscribeToInAppMessage((inAppMessage) => {
    // Show the message
    showInAppMessage(inAppMessage);
});
```

#### カスタムアプリ内メッセージ処理 {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### アプリ内メッセージインタラクションの記録 {#log-in-app-message-interactions}

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

#### カスタムHTMLアプリ内メッセージ {#custom-html-in-app-messages}

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

#### Content Cardsの表示 {#display-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show content cards in default location
showContentCards();

// Show in specific container
const container = document.getElementById('content-cards-container');
showContentCards(container);
```

#### Content Cards更新のサブスクライブ {#subscribe-to-content-cards-updates}

``` typescript
import { subscribeToContentCardsUpdates } from "@braze/web-sdk";

subscribeToContentCardsUpdates((cards) => {
    console.log('Content cards updated:', cards);
    // Display cards or update UI
});
```

#### Content Cardsインタラクションの記録 {#log-content-card-interactions}

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

#### Content Cardsのフィルタリング {#filter-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show only pinned cards
// You can also provide a parent element instead of null
showContentCards(null, (cards) => {
    return cards.filter(card => card.getIsPinned());
});
```

#### Content Cardsの更新リクエスト {#request-content-cards-refresh}

``` typescript
import { requestContentCardsRefresh } from "@braze/web-sdk";

requestContentCardsRefresh(
    () => console.log('Content cards refreshed'),
    () => console.log('Failed to refresh content cards')
);
```

#### カスタムContent Cards {#custom-content-cards}

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

### プッシュ通知 {#push-notifications}

#### プッシュ許可のリクエスト {#request-push-permission}

``` typescript
import { requestPushPermission } from "@braze/web-sdk";

requestPushPermission(
    () => console.log('Push permission granted'),
    () => console.log('Push permission denied')
);
```

#### プッシュサポートの確認 {#check-push-support}

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

#### プッシュの登録解除 {#unregister-push}

``` typescript
import { unregisterPush } from "@braze/web-sdk";

unregisterPush(
    () => console.log('Successfully unregistered'),
    () => console.log('Failed to unregister')
);
```

### フィーチャーフラグ {#feature-flags}

#### フィーチャーフラグの取得 {#get-feature-flag}

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

#### フィーチャーフラグ更新のサブスクライブ {#subscribe-to-feature-flag-updates}

``` typescript
import { subscribeToFeatureFlagsUpdates } from "@braze/web-sdk";

subscribeToFeatureFlagsUpdates((featureFlags) => {
    featureFlags.forEach(flag => {
        console.log(`Feature flag ${flag.getId()}: ${flag.getBooleanProperty('enabled')}`);
    });
});
```

#### フィーチャーフラグインプレッションの記録 {#log-feature-flag-impressions}

``` typescript
import { logFeatureFlagImpression } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_feature');
if (featureFlag) {
    logFeatureFlagImpression(featureFlag);
}
```

#### フィーチャーフラグの更新リクエスト {#request-feature-flags-refresh}

``` typescript
import { refreshFeatureFlags } from "@braze/web-sdk";

refreshFeatureFlags(
    () => console.log('Feature flags refreshed'),
    () => console.log('Failed to refresh feature flags')
);
```

### バナー {#banners}

#### バナーの取得と表示 {#get-and-display-banners}

``` typescript
import { getBanner, insertBanner } from "@braze/web-sdk";

const banner = getBanner('homepage_banner');
if (banner) {
    // Insert banner into specific element
    const container = document.getElementById('banner-container');
    insertBanner(banner, container);
}
```

#### バナー更新のサブスクライブ {#subscribe-to-banner-updates}

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

#### バナーの更新リクエスト {#request-banner-refresh}

``` typescript
import { requestBannersRefresh } from "@braze/web-sdk";

requestBannersRefresh(
    ["placement_1", "placement_2"],
    () => console.log('Banners refreshed'),
    () => console.log('Failed to refresh banners')
);
```

### 分析とイベント {#analytics-events}

#### カスタムイベントの記録 {#log-custom-events}

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

#### 購入の記録 {#log-purchases}

``` typescript
import { logPurchase } from "@braze/web-sdk";

logPurchase('product-123', 29.99, 'USD', 1, {
    category: 'electronics',
    brand: 'Apple'
});
```

#### データフラッシュのリクエスト {#request-data-flush}

``` typescript
import { requestImmediateDataFlush } from "@braze/web-sdk";

// Force immediate data send
requestImmediateDataFlush();
```

### セッション管理 {#session-management}

#### セッションの開始 {#open-session}

``` typescript
import { openSession } from "@braze/web-sdk";

// Start a new session
openSession();
```

#### SDKステータスの確認 {#check-sdk-status}

``` typescript
import { isInitialized, isDisabled } from "@braze/web-sdk";

if (isInitialized()) {
    console.log('SDK is initialized');

    if (isDisabled()) {
        console.log('SDK is disabled');
    }
}
```

#### SDKの有効化/無効化 {#enabledisable-sdk}

``` typescript
import { enableSDK, disableSDK } from "@braze/web-sdk";

// Disable SDK
disableSDK();

// Re-enable SDK
enableSDK();
```

### データ管理 {#data-management}

#### データの消去 {#wipe-data}

``` typescript
import { wipeData } from "@braze/web-sdk";

// Remove all locally stored data
wipeData();
```

#### SDKの破棄 {#destroy-sdk}

``` typescript
import { destroy } from "@braze/web-sdk";

// Clean up SDK resources
destroy();
```

#### デバイスIDの取得 {#get-device-id}

``` typescript
import { getDeviceId } from "@braze/web-sdk";

const deviceId = getDeviceId();
console.log('Device ID:', deviceId);
```

#### SDK認証 {#sdk-authentication}

``` typescript
import { setSdkAuthenticationSignature } from "@braze/web-sdk";

// Set authentication signature
setSdkAuthenticationSignature('your-signature-here');
```

#### 認証失敗のサブスクライブ {#subscribe-to-authentication-failures}

``` typescript
import { subscribeToSdkAuthenticationFailures } from "@braze/web-sdk";

subscribeToSdkAuthenticationFailures((error) => {
    console.log('Authentication failed:', error);
    // Provide new signature
    setSdkAuthenticationSignature('new-signature');
});
```

---

## 統合パターン {#integration-patterns}

### SSRフレームワーク {#ssr-frameworks}

Next.jsなどのサーバーサイドレンダリング（SSR）フレームワークを使用している場合、SDKはブラウザ環境で実行されることを前提としているため、エラーが発生する可能性があります。SDKを動的にインポートすることで、これらの問題を解決できます。

必要なSDKの部分を別のファイルにエクスポートし、そのファイルをコンポーネントに動的にインポートすることで、ツリーシェイキングの利点を維持できます。

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

また、webpackを使用してアプリをバンドルしている場合は、マジックコメントを利用して必要なSDKの部分のみを動的にインポートできます。

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

Viteを使用していて、循環依存関係に関する警告や`Uncaught TypeError: Class extends value undefined is not a constructor or null`が表示される場合は、Braze SDKを依存関係の検出から除外する必要がある場合があります。

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Jestフレームワーク {#jest-framework}

Jestを使用している場合、`SyntaxError: Unexpected token 'export'`のようなエラーが表示されることがあります。これを修正するには、`package.json`の設定を調整してBraze SDKを無視するようにしてください。

``` json
{
  "jest": {
    "transformIgnorePatterns": [
      "/node_modules/(?!@braze)"
    ]
  }
}
```

### 非同期モジュール定義（AMD） {#asynchronous-module-definition-amd}

#### AMDサポートの無効化 {#disable-amd-support}

サイトでRequireJSまたは別のAMDモジュールローダーを使用しているが、CDNを通じてBraze Web SDKを読み込みたい場合は、AMDサポートを含まないバージョンのライブラリを読み込むことができます。このバージョンのライブラリは、CDNロケーション`https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`から読み込めます。

#### モジュールローダー {#module-loader}

RequireJSまたは他のAMDモジュールローダーを使用している場合は、ライブラリのコピーをセルフホスティングし、他のリソースと同様に参照することをお勧めします。

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Accelerated Mobile Pages（AMP） {#accelerated-mobile-pages-amp}

AMP統合には、以下が必要です。

1. **AMP Webプッシュスクリプトの追加**: headに非同期スクリプトタグを追加します
2. **サブスクリプションウィジェットの追加**: ユーザーがサブスクライブ/アンサブスクライブできるウィジェットを追加します
3. **ヘルパーファイルの追加**: `helper-iframe.html`と`permission-dialog.html`を含めます
4. **Service Workerの作成**: BrazeのService Workerファイルを追加します
5. **AMP Webプッシュ要素の設定**: APIキーとベースURLをクエリパラメーターとして`amp-web-push`要素を追加します

AMP統合の詳細な手順については、[Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web#amp)を参照してください。

### Electron

Electronは公式にはWebプッシュ通知をサポートしていません（この[GitHubイシュー](https://github.com/electron/electron/issues/6697)を参照）。Brazeではテストされていませんが、試すことができる他の[オープンソースの回避策](https://github.com/MatthieuLemoine/electron-push-receiver)があります。

### CDN統合 {#cdn-integration}

- **スクリプトの読み込み**: スクリプトタグの後に初期化コードを配置するか、スクリプトタグの`onload`イベントハンドラーを使用して、スクリプトタグの読み込み後に初期化します
- **グローバルアクセス**: CDN経由で読み込んだ場合、SDKは`window.braze`として利用できます

### Service Worker（プッシュ通知） {#service-worker-push-notifications}

- **必須**: プッシュ通知を機能させるには、BrazeのService Workerを含める必要があります
- **登録**: `navigator.serviceWorker.register()`を使用して、WebサイトのコードでService Workerを登録します
- **プッシュ許可**: ユーザーインタラクション（例: ボタンクリック）に応じて`braze.requestPushPermission()`を呼び出します。ブラウザの許可をリクエストする前に、ソフトプッシュプロンプト（カスタムUI）を使用してください

### タグマネージャー {#tag-managers}

#### Tealium iQ

Tealium iQは、基本的なターンキーBraze統合を提供します。統合を設定するには、Tealiumタグ管理インターフェイスでBrazeを検索し、ダッシュボードからWeb SDK APIキーを入力してください。詳細やTealiumの設定サポートについては、[統合ドキュメント](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)を確認するか、Tealiumのアカウントマネージャーにお問い合わせください。

#### その他のタグマネージャー {#other-tag-managers}

Brazeは、カスタムHTMLタグ内の統合手順に従うことで、他のタグ管理ソリューションとも互換性がある場合があります。これらのソリューションの評価についてサポートが必要な場合は、Brazeの担当者にお問い合わせください。

---

## ライブラリ {#libraries}

| 名前 | 説明 | npm | CDN URL
| ---- | ----------- | --- | -------
| Full | UIを含む完全なSDKです。npmバージョンを使用する場合、JavaScriptバンドラーはUIを含む未使用のコードを削除します。 | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.8/braze.min.js
| Core | UIなしのSDKです。このバージョンのSDKを使用する場合、In-App MessagesとContent Cards用に独自のUIを実装する必要があります。UI要素はCSSで完全にカスタマイズ可能なため、一般的にはフルライブラリの統合をお勧めします。 | N/A | https://js.appboycdn.com/web-sdk/6.8/braze.core.min.js
| No-AMD | AMDサポートなしの完全なSDKです。サイトでRequireJSまたは別のAMDモジュールローダーを使用しているが、CDNを通じてSDKを読み込みたい場合に便利です。 | N/A | https://js.appboycdn.com/web-sdk/6.8/braze.no-amd.min.js
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ライブラリ" }

## サポートされているブラウザ {#supported-browsers}

- モダンなChromiumベースのブラウザ（Chrome、Edge、Opera）
- Firefox
- Safari

## デバッグとトラブルシューティング {#debugging-troubleshooting}

initialize関数にオプション`enableLogging: true`を渡すと（`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`）、BrazeがJavaScriptコンソールにログを出力するようになります。これは開発時に有用ですが、すべてのユーザーに表示されるため、本番環境にリリースする前にこのオプションを削除するか、[代替ロガーを提供](https://js.appboycdn.com/web-sdk/6.8/doc/modules/braze.html#setlogger)してください。

## Font Awesome

Brazeはアプリ内メッセージのアイコンに[Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0を使用しています。Font Awesomeの読み込みを無効にするには、`doNotLoadFontAwesome`初期化オプションを使用してください。利用可能なアイコンを確認するには、[チートシート](http://fortawesome.github.io/Font-Awesome/cheatsheet/)をご覧ください。

## その他のリソース {#additional-resources}

- [Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web)
- [SDKドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [サンプルビルド](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## お問い合わせ {#contact}

ご質問がある場合は、[support@braze.com](mailto:support@braze.com)までお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk)を参照してください。