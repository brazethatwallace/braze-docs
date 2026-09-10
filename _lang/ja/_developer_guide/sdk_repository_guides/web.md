---
nav_title: Web SDK
article_title: Web SDK リポジトリガイド
page_order: 1
description: "GitHubからミラーリングされたBraze Web SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
# Web SDK リポジトリガイド {#web-sdk-repository-guide}

## Braze Web SDKについて {#about-the-braze-web-sdk}

Braze Web SDKを使用すると、BrazeのカスタマーエンゲージメントプラットフォームをWebアプリケーションに直接統合できます。TypeScriptで構築され、モダンなWeb開発向けに設計されたこのSDKは、ユーザー管理、メッセージング、分析、フィーチャーフラグのための包括的なツールを提供します。

### できること {#what-you-can-do}

- **ユーザー管理**: Webアプリケーション全体でユーザーのID、属性、行動を追跡・管理します
- **アプリ内メッセージング**: ユーザーがサイトをアクティブに利用している間に、ターゲットを絞ったメッセージや通知を表示します
- **Content Cards**: パーソナライズされたコンテンツフィードやプロモーションカードをリアルタイムで更新しながら表示します
- **バナー**: サイト内の特定のプレースメントにバナーメッセージを表示します
- **プッシュ通知**: ユーザーがサイトにアクセスしていない時でも、Webプッシュ通知を送信してエンゲージメントを促進します
- **フィーチャーフラグ**: サーバーサイドのフィーチャーフラグ管理で、機能のロールアウトやABテストをコントロールします
- **分析**: カスタムイベント、ユーザーインタラクション、コンバージョン指標を追跡します
- **セッション管理**: ユーザーセッションやエンゲージメントパターンをモニタリングします

シングルページアプリケーション、eコマースサイト、コンテンツプラットフォームのいずれを構築する場合でも、Braze Web SDKは、成長とリテンションを促進するパーソナライズされた魅力的なユーザー体験を作成するために必要なツールを提供します。

## 前提条件 {#prerequisites}

Braze Web SDKを統合する前に、以下が必要です。

- **Brazeアカウント**: APIアクセスが可能なBrazeアカウント
- **APIキー**: Brazeダッシュボードからのアプリ用APIキー
- **SDKエンドポイント**: BrazeのSDKエンドポイントURL（例: `sdk.iad-01.braze.com`）

### 認証情報の取得 {#getting-your-credentials}

1. **APIキー**: Brazeダッシュボードの**設定** > **APIキー**で確認できます
2. **SDKエンドポイント**: **設定** > **SDK認証** > **エンドポイント**にあります
3. **サービスワーカー**: プッシュ通知に必要です（プッシュ通知のセクションを参照してください）

## インストール {#installation}

``` bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

## クイックスタート {#quick-start}

以下のスニペットは、Braze Web SDKを初期化するために必要な最小限の構成を示しています。

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

`initialize` 関数は、以下のプロパティを持つオプションオブジェクトを受け取ります。

| オプション | 型 | デフォルト | 説明 |
|--------|------|---------|-------------|
| `baseUrl` | `string` | **必須** | このオプションは、Braze Web SDKが適切なエンドポイントを使用するように設定するために必要です。例: `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | デフォルトでログを有効にするには true に設定します。これにより、Braze は JavaScript コンソールにログを出力するようになり、すべてのユーザーに表示されることに注意してください。本番環境にページをリリースする前に、これを削除するか、setLogger で別のロガーを提供してください。 |
| `allowUserSuppliedJavascript` | `boolean` | `false` | デフォルトでは、Braze Web SDKはユーザーが提供した JavaScript クリックアクションを許可せず、HTMLアプリ内メッセージやバナーも有効にしません。これらを有効にすると、Brazeダッシュボードのユーザーがサイト上で JavaScript を実行できるようになるためです。Brazeダッシュボードのユーザーが悪意のない JavaScript クリックアクションを作成することを信頼する場合は、このプロパティを true に設定してください。 |
| `doNotLoadFontAwesome` | `boolean` | `false` | Braze はアプリ内メッセージのアイコンに Font Awesome を使用します。デフォルトでは、Braze は FontAwesome CDN から FontAwesome 4.7.0 を自動的に読み込みます。この動作を無効にする場合（例：サイトでカスタマイズ版の FontAwesome を使用している場合）、このオプションを `true` に設定します。この場合、サイトに FontAwesome が読み込まれていることを確認する責任はお客様にあります。そうしないと、アプリ内メッセージが正しくレンダリングされない場合があります。 |
| `inAppMessageZIndex` | `number` | `999999` | デフォルトでは、Braze SDKは z-index 999999 でIn-App Messagesを表示します。このデフォルト値を上書きするには、このオプションに値を指定してください。 |
| `sessionTimeoutInSeconds` | `number` | `30` | デフォルトでは、セッションは30秒間操作がないとタイムアウトします。このデフォルト値を上書きするには、このオプションに値を指定してください。 |
| `deviceId` | `string` | 自動生成 | デフォルトでは、Braze はランダムな GUID をデバイス ID として割り当てます。このデフォルト値を上書きして独自の値を使用するには、この設定オプションに値を指定してください。 |
| `appVersion` | `string` | `undefined` | このオプションに値を指定すると、Braze に送信されるユーザーイベントが指定されたバージョンに関連付けられ、ユーザーセグメンテーションに使用できます。 |
| `appVersionNumber` | `string` | `undefined` | ユーザーセグメンテーションに使用できる数値のアプリバージョン値です。この値は「1.2.3.4」のように4つのフィールドで送信する必要があります。そうしないと無視されます。注意: `appVersion` も設定する必要があり、同じ値またはこのバージョンの一意の名前を使用してください。 |
| `contentSecurityNonce` | `string` | `undefined` | このオプションに値を指定すると、Braze SDKはSDKが作成するすべての `<script>` および `<style>` 要素にそのノンスを追加します。これにより、Webサイトのコンテンツセキュリティポリシーと連携してBraze SDKを動作させることができます。このノンスの設定に加えて、FontAwesome の読み込みを許可する必要がある場合もあります。コンテンツセキュリティポリシーの許可リストに `use.fontawesome.com` を追加するか、`doNotLoadFontAwesome` オプションを使用して手動で読み込むことで対応できます。 |
| `noCookies` | `boolean` | `false` | デフォルトでは、Braze Web SDKは Cookie を使用します。Cookie の使用を無効にするには、このオプションを true に設定します。Cookie を無効にすると、セッション間でユーザーの ID を記憶するSDKの機能に影響を与える場合があることに注意してください。 |
| `allowCrawlerActivity` | `boolean` | `false` | デフォルトでは、Braze Web SDKはユーザーエージェント文字列に基づいて、Google などの既知のスパイダーや Web クローラーからのアクティビティを無視します。これにより、データポイントが節約され、分析がより正確になり、ページランクが向上する場合があります。ただし、これらのクローラーからのアクティビティを Braze で記録する場合は、このオプションを true に設定してください。 |
| `disablePushTokenMaintenance` | `boolean` | `false` | デフォルトでは、すでに Web プッシュ権限を付与しているユーザー（例: requestPushPermission を通じて、または以前のプッシュプロバイダーから）は、配信到達性を確保するために新しいセッションで自動的にプッシュトークンを Braze バックエンドに同期します。この動作を無効にするには、このオプションを true に設定します。 |
| `enableSdkAuthentication` | `boolean` | `false` | SDK 認証機能を有効にするには true に設定します。SDK 認証の詳細については、製品ドキュメントを参照してください。 |
| `manageServiceWorkerExternally` | `boolean` | `false` | デフォルトでは、Braze Web SDKはプッシュ通知用に独自のサービスワーカーを管理します。アプリケーションですでにサービスワーカーを管理しており、Braze サービスワーカーの機能を組み込みたい場合は、このオプションを true に設定し、サービスワーカーファイルに Braze サービスワーカーコードを含めてください。 |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | デフォルトでは、トリガーアクション（例: アプリ内メッセージの表示）はユーザーごとに最大30秒に1回発火できます。このデフォルト値を上書きするには、このオプションに値を指定してください。 |
| `serviceWorkerLocation` | `string` | `undefined` | デフォルトでは、Braze Web SDKはドメインのルートでサービスワーカーファイルを検索します。このデフォルト値を上書きして、サービスワーカーファイルのカスタムパスを指定するには、このオプションに値を指定してください。 |
| `safariWebsitePushId` | `string` | `undefined` | Safari プッシュ通知に必要です。この値は Apple Developer アカウントで確認できます。Safari プッシュ通知の設定について詳しくは、製品ドキュメントを参照してください。 |
| `localization` | `string` | `undefined` | このオプションに値を指定すると、Braze SDKはアプリ内メッセージとContent Cardsをそのロケールで表示しようとします。 |
| `openInAppMessagesInNewTab` | `boolean` | `false` | デフォルトでは、アプリ内メッセージ内のリンクは同じタブで開きます。新しいタブで開くようにするには、このオプションを true に設定します。 |
| `openCardsInNewTab` | `boolean` | `false` | デフォルトでは、Content Cards内のリンクは同じタブで開きます。新しいタブで開くようにするには、このオプションを true に設定します。 |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | デフォルトでは、アプリ内メッセージはメッセージの外側をクリックするか、エスケープキーを押すことで閉じることができます。ユーザーがメッセージを閉じるために明示的に閉じるボタンまたはアクションボタンをクリックすることを要求するには、このオプションを true に設定します。 |
| `devicePropertyAllowlist` | `string[]` | `undefined` | デフォルトでは、Braze SDKは DeviceProperties 内のすべてのデバイスプロパティを自動的に検出して収集します。この動作を上書きするには、DeviceProperties の配列を指定してください。Braze サーバーへのすべてのプロパティ送信を無効にするには、空の配列を指定してください。一部のプロパティがないと、すべての機能が正常に動作するとは限りません。例えば、タイムゾーンがないと、ローカルタイムゾーン配信は機能しません。 |
| `serviceWorkerScope` | `string` | `undefined` | デフォルトでは、Braze Web SDKはデフォルトのスコープ（サービスワーカーのディレクトリ）でサービスワーカーを登録します。このデフォルト値を上書きして、サービスワーカーのカスタムスコープを指定するには、このオプションに値を指定してください。 |
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

#### ユーザーの位置情報の設定 {#set-user-location}

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

#### ユーザーエイリアスと購読グループ {#user-aliases-and-subscription-groups}

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

### アプリ内メッセージ {#in-app-messages}

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

#### アプリ内メッセージのカスタムハンドリング {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### アプリ内メッセージのインタラクションを記録する {#log-in-app-message-interactions}

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

#### Content Cardsを表示する {#display-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show content cards in default location
showContentCards();

// Show in specific container
const container = document.getElementById('content-cards-container');
showContentCards(container);
```

#### Content Cardsの更新を購読する {#subscribe-to-content-cards-updates}

``` typescript
import { subscribeToContentCardsUpdates } from "@braze/web-sdk";

subscribeToContentCardsUpdates((cards) => {
    console.log('Content cards updated:', cards);
    // Display cards or update UI
});
```

#### Content Cardsのインタラクションを記録する {#log-content-card-interactions}

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

#### Content Cardsをフィルターする {#filter-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show only pinned cards
// You can also provide a parent element instead of null
showContentCards(null, (cards) => {
    return cards.filter(card => card.getIsPinned());
});
```

#### Content Cardsの更新をリクエストする {#request-content-cards-refresh}

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

#### プッシュ許可をリクエストする {#request-push-permission}

``` typescript
import { requestPushPermission } from "@braze/web-sdk";

requestPushPermission(
    () => console.log('Push permission granted'),
    () => console.log('Push permission denied')
);
```

#### プッシュのサポート状況を確認する {#check-push-support}

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

#### プッシュの登録を解除する {#unregister-push}

``` typescript
import { unregisterPush } from "@braze/web-sdk";

unregisterPush(
    () => console.log('Successfully unregistered'),
    () => console.log('Failed to unregister')
);
```

### フィーチャーフラグ {#feature-flags}

#### フィーチャーフラグを取得する {#get-feature-flag}

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

#### フィーチャーフラグの更新を購読する {#subscribe-to-feature-flag-updates}

``` typescript
import { subscribeToFeatureFlagsUpdates } from "@braze/web-sdk";

subscribeToFeatureFlagsUpdates((featureFlags) => {
    featureFlags.forEach(flag => {
        console.log(`Feature flag ${flag.getId()}: ${flag.getBooleanProperty('enabled')}`);
    });
});
```

#### フィーチャーフラグのインプレッションを記録する {#log-feature-flag-impressions}

``` typescript
import { logFeatureFlagImpression } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_feature');
if (featureFlag) {
    logFeatureFlagImpression(featureFlag);
}
```

#### フィーチャーフラグの更新をリクエストする {#request-feature-flags-refresh}

``` typescript
import { refreshFeatureFlags } from "@braze/web-sdk";

refreshFeatureFlags(
    () => console.log('Feature flags refreshed'),
    () => console.log('Failed to refresh feature flags')
);
```

### バナー {#banners}

#### バナーを取得して表示する {#get-and-display-banners}

``` typescript
import { getBanner, insertBanner } from "@braze/web-sdk";

const banner = getBanner('homepage_banner');
if (banner) {
    // Insert banner into specific element
    const container = document.getElementById('banner-container');
    insertBanner(banner, container);
}
```

#### バナーの更新を購読する {#subscribe-to-banner-updates}

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

#### カスタムUIでバナーを閉じる {#dismiss-banners-in-a-custom-ui}

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

`dismissBanner(banner)` を呼び出すと、SDKはバナーの閉じた状態を処理し、アクティブなバナー更新からそのバナーを削除し、バナーの閉じたイベントの購読者に通知し、閉じた状態をBrazeに同期します。カスタムUIでは、`dismissBanner` をローカルのUI変更のみや分析ログ記録メソッドのみとして扱うのではなく、`subscribeToBannersUpdates` を使用して閉じたバナーの削除に対応する必要があります。

#### バナーの更新をリクエストする {#request-banner-refresh}

``` typescript
import { requestBannersRefresh } from "@braze/web-sdk";

requestBannersRefresh(
    ["placement_1", "placement_2"],
    () => console.log('Banners refreshed'),
    () => console.log('Failed to refresh banners')
);
```

### 分析とイベント {#analytics-events}

#### カスタムイベントを記録する {#log-custom-events}

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

#### 購入を記録する {#log-purchases}

``` typescript
import { logPurchase } from "@braze/web-sdk";

logPurchase('product-123', 29.99, 'USD', 1, {
    category: 'electronics',
    brand: 'Apple'
});
```

#### データフラッシュをリクエストする {#request-data-flush}

``` typescript
import { requestImmediateDataFlush } from "@braze/web-sdk";

// Force immediate data send
requestImmediateDataFlush();
```

### セッション管理 {#session-management}

#### セッションを開始する {#open-session}

``` typescript
import { openSession } from "@braze/web-sdk";

// Start a new session
openSession();
```

#### SDKのステータスを確認する {#check-sdk-status}

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

#### データを消去する {#wipe-data}

``` typescript
import { wipeData } from "@braze/web-sdk";

// Remove all locally stored data
wipeData();
```

#### SDKを破棄する {#destroy-sdk}

``` typescript
import { destroy } from "@braze/web-sdk";

// Clean up SDK resources
destroy();
```

#### デバイスIDを取得する {#get-device-id}

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

#### 認証エラーを購読する {#subscribe-to-authentication-failures}

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

### SSR フレームワーク {#ssr-frameworks}

Next.js などのサーバーサイドレンダリング (SSR) フレームワークを使用している場合、SDKはブラウザ環境で実行されることを前提としているため、エラーが発生することがあります。SDKをダイナミックインポートすることで、これらの問題を解決できます。

SDKの必要な部分を別ファイルにエクスポートし、そのファイルをコンポーネントにダイナミックインポートすることで、ツリーシェイキングのメリットを維持できます。

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

また、webpack を使用してアプリをバンドルしている場合は、マジックコメントを活用してSDKの必要な部分のみをダイナミックインポートできます。

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

Vite を使用していて、循環依存関係に関する警告や `Uncaught TypeError: Class extends value undefined is not a constructor or null` が表示される場合は、Braze SDKを依存関係の検出から除外する必要があるかもしれません。

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Jest フレームワーク {#jest-framework}

Jest を使用している場合、`SyntaxError: Unexpected token 'export'` のようなエラーが表示されることがあります。これを修正するには、`package.json` の設定を調整して Braze SDKを無視するようにします。

``` json
{
  "jest": {
    "transformIgnorePatterns": [
      "/node_modules/(?!@braze)"
    ]
  }
}
```

### 非同期モジュール定義 (AMD) {#asynchronous-module-definition-amd}

#### AMD サポートの無効化 {#disable-amd-support}

サイトで RequireJS やその他の AMD モジュールローダーを使用しているが、Braze Web SDKを CDN 経由で読み込むことを希望する場合は、AMD サポートを含まないバージョンのライブラリを読み込むことができます。このバージョンのライブラリは、CDN の次の場所から読み込めます：`https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`

#### モジュールローダー {#module-loader}

RequireJS やその他の AMD モジュールローダーを使用している場合は、ライブラリのコピーを自身でホスティングし、他のリソースと同様に参照することをお勧めします。

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Accelerated Mobile Pages (AMP) {#accelerated-mobile-pages-amp}

AMP 統合には、以下の手順が必要です。

1. **AMP Web プッシュスクリプトの追加**：head に非同期スクリプトタグを追加します
2. **購読ウィジェットの追加**：ユーザーが購読/購読解除できるウィジェットを追加します
3. **ヘルパーファイルの追加**：`helper-iframe.html` と `permission-dialog.html` を含めます
4. **サービスワーカーの作成**：Braze サービスワーカーファイルを追加します
5. **AMP Web プッシュ要素の設定**：APIキーとベース URL をクエリパラメーターとして `amp-web-push` 要素を追加します

AMP 統合の詳細な手順については、[Braze 開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web#amp)を参照してください。

### Electron

Electron はWebプッシュ通知を公式にはサポートしていません（参照：この [GitHub issue](https://github.com/electron/electron/issues/6697)）。Braze ではテストしていませんが、試すことができる[オープンソースの回避策](https://github.com/MatthieuLemoine/electron-push-receiver)があります。

### CDN 統合 {#cdn-integration}

- **スクリプトの読み込み**：スクリプトタグの後に初期化コードを配置するか、スクリプトタグの `onload` イベントハンドラーを使用して、スクリプトタグの読み込み後に初期化します
- **グローバルアクセス**：CDN 経由で読み込まれた場合、SDKは `window.braze` として利用可能です

### サービスワーカー（プッシュ通知） {#service-worker-push-notifications}

- **必須**：プッシュ通知を機能させるには、Braze サービスワーカーを含める必要があります
- **デフォルトの登録**：デフォルトでは、Braze Web SDKは `requestPushPermission()` が呼び出されたとき、およびプッシュ許可を既に付与しているユーザーの新しいセッション開始時に、サービスワーカーを自動的に登録・管理します。ただし、Braze サービスワーカーコードを含むサービスワーカーファイルを、想定される場所にホスティングする必要があります。
- **独自のサービスワーカーの管理**：アプリケーションで既にサービスワーカーを管理している場合は、初期化オプション `manageServiceWorkerExternally` を `true` に設定し、サービスワーカーファイルに Braze サービスワーカーコードを追加して、`navigator.serviceWorker.register()` を使用して自身で登録します
- **プッシュ許可**：ユーザーの操作（ボタンクリックなど）に応じて `braze.requestPushPermission()` を呼び出します。ブラウザの許可をリクエストする前に、ソフトプッシュプロンプト（カスタム UI）を使用してください

### タグマネージャー {#tag-managers}

#### Tealium iQ

Tealium iQ は、基本的なターンキー Braze 統合を提供しています。統合を設定するには、Tealium タグ管理インターフェイスで Braze を検索し、ダッシュボードから Web SDK APIキーを入力します。詳細や Tealium の詳しい設定サポートについては、[統合ドキュメント](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)を確認するか、Tealium のアカウントマネージャーにお問い合わせください。

#### Google Tag Manager

Web SDKは、Google Tag Manager コンテナのカスタム HTML タグから初期化および呼び出しができます。GTM 経由で Braze にイベントを送信する例については、[Google Tag Manager サンプルアプリ](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/google-tag-manager)を参照してください。詳細については、[統合ドキュメント](https://www.braze.com/docs/developer_guide/sdk_integration/google_tag_manager)をご覧ください。

#### その他のタグマネージャー {#other-tag-managers}

Braze は、カスタム HTML タグ内の統合手順に従うことで、他のタグ管理ソリューションとも互換性がある場合があります。これらのソリューションの評価についてサポートが必要な場合は、Braze の担当者にお問い合わせください。

---

## ライブラリ {#libraries}

以下の表は、利用可能なBraze Web SDKのディストリビューションについて説明しています。

| 名前 | 説明 | npm | CDN URL
| ---- | ----------- | --- | -------
| Full | UIを含む完全なSDKです。npm版を使用すると、JavaScriptバンドラーがUIコードを含む未使用のコードを自動的に除去します。 | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.12/braze.min.js
| Core | UIを含まないSDKです。このバージョンのSDKを使用する場合は、In-App MessagesおよびContent Cardsの独自のUIを実装してください。CSSを通じてカスタマイズ可能なUI要素が提供されるため、ほとんどの統合にはフルライブラリを使用してください。 | N/A | https://js.appboycdn.com/web-sdk/6.12/braze.core.min.js
| No-AMD | AMDサポートを含まない完全なSDKです。サイトでRequireJSや他のAMDモジュールローダーを使用しているが、CDN経由でSDKを読み込むことを好む場合に便利です。 | N/A | https://js.appboycdn.com/web-sdk/6.12/braze.no-amd.min.js
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ライブラリ" }

## サポートされているブラウザ {#supported-browsers}

- 最新のChromiumベースのブラウザ（Chrome、Edge、Opera）
- Firefox
- Safari

## デバッグとトラブルシューティング {#debugging-troubleshooting}

初期化関数にオプション `enableLogging: true` を渡すと（`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`）、BrazeがJavaScriptコンソールにログを出力するようになります。これは開発時に役立ちますが、すべてのユーザーに表示されるため、ページを本番環境にリリースする前に、このオプションを削除するか、[代替のロガーを提供](https://js.appboycdn.com/web-sdk/6.12/doc/modules/braze.html#setlogger)してください。

## Font Awesome

Brazeはアプリ内メッセージのアイコンに[Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0を使用しています。Font Awesomeの読み込みを無効にするには、`doNotLoadFontAwesome`初期化オプションを使用してください。利用可能なアイコンを確認するには、[チートシート](http://fortawesome.github.io/Font-Awesome/cheatsheet/)をご覧ください。

## その他のリソース {#additional-resources}

- [Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web)
- [SDKドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [サンプルビルド](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## お問い合わせ {#contact}

ご質問がある場合は、Brazeテクニカルサポートにお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk)を参照してください。