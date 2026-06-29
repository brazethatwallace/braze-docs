---
nav_title: Web SDK
article_title: Web SDK 리포지토리 가이드
page_order: 1
description: "GitHub에서 미러링된 Braze Web SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Web SDK 소개 {#about-the-braze-web-sdk}

Braze Web SDK를 사용하면 Braze의 고객 참여 플랫폼을 웹 애플리케이션에 직접 통합할 수 있습니다. TypeScript로 구축되고 최신 웹 개발을 위해 설계된 이 SDK는 사용자 관리, 메시징, 분석 및 기능 플래그를 위한 포괄적인 도구를 제공합니다.

### 주요 기능 {#what-you-can-do}

- **사용자 관리**: 웹 애플리케이션 전반에서 사용자 ID, 속성 및 동작을 추적하고 관리합니다
- **인앱 메시지**: 사용자가 사이트를 활발히 사용하는 동안 타겟팅된 메시지와 알림을 표시합니다
- **Content Cards**: 실시간으로 업데이트되는 개인화된 콘텐츠 피드와 프로모션 카드를 표시합니다
- **배너**: 사이트 내 특정 위치에 배너 메시지를 표시합니다
- **푸시 알림**: 사용자가 사이트에 없을 때도 웹 푸시 알림을 전송하여 참여를 유도합니다
- **기능 플래그**: 서버 측 기능 플래그 관리를 통해 기능 출시 및 A/B 테스트를 제어합니다
- **분석**: 커스텀 이벤트, 사용자 상호작용 및 전환 측정기준을 추적합니다
- **세션 관리**: 사용자 세션 및 참여 패턴을 모니터링합니다

싱글 페이지 애플리케이션, 이커머스 사이트 또는 콘텐츠 플랫폼을 구축하든, Braze Web SDK는 성장과 리텐션을 촉진하는 개인화되고 매력적인 사용자 경험을 만드는 데 필요한 도구를 제공합니다.

## 필수 조건 {#prerequisites}

Braze Web SDK를 통합하기 전에 다음이 필요합니다:

- **Braze 계정**: API 접근 권한이 있는 Braze 계정
- **API 키**: Braze 대시보드에서 확인할 수 있는 앱의 API 키
- **SDK 엔드포인트**: Braze SDK 엔드포인트 URL (예: `sdk.iad-01.braze.com`)

### 자격 증명 확인하기 {#getting-your-credentials}

1. **API 키**: Braze 대시보드에서 **설정** > **API 키**에서 확인할 수 있습니다
2. **SDK 엔드포인트**: **설정** > **SDK 인증** > **엔드포인트**에서 확인할 수 있습니다
3. **서비스 워커**: 푸시 알림에 필요합니다 (푸시 알림 섹션 참조)

## 설치 {#installation}

``` bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

## 빠른 시작 {#quick-start}

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});

braze.changeUser('Jane Doe');
```

## 구성 참조 {#configuration-reference}

### 초기화 옵션 {#initialization-options}

`initialize` 함수는 다음 속성을 가진 옵션 오브젝트를 받습니다:

| 옵션 | 유형 | 기본값 | 설명 |
|--------|------|---------|-------------|
| `baseUrl` | `string` | **필수** | 이 옵션은 통합에 적합한 엔드포인트를 사용하도록 Braze Web SDK를 구성하는 데 필수입니다. 예: `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | 기본적으로 로깅을 활성화하려면 true로 설정합니다. 이렇게 하면 Braze가 모든 사용자에게 표시되는 JavaScript 콘솔에 로그를 기록합니다! 프로덕션에 페이지를 릴리스하기 전에 이 옵션을 제거하거나 setLogger를 사용하여 대체 로거를 제공해야 합니다. |
| `allowUserSuppliedJavascript` | `boolean` | `false` | 기본적으로 Braze Web SDK는 사용자 제공 JavaScript 클릭 동작을 허용하지 않으며, HTML 인앱 메시지 및 배너를 활성화하지 않습니다. 이는 Braze 대시보드 사용자가 사이트에서 JavaScript를 실행할 수 있기 때문입니다. Braze 대시보드 사용자가 악의적이지 않은 JavaScript 클릭 동작을 작성한다고 신뢰하는 경우 이 속성을 true로 설정합니다. |
| `doNotLoadFontAwesome` | `boolean` | `false` | Braze는 인앱 메시지 아이콘에 Font Awesome을 사용합니다. 기본적으로 Braze는 FontAwesome CDN에서 FontAwesome 4.7.0을 자동으로 로드합니다. 이 동작을 비활성화하려면(예: 사이트에서 사용자 정의 버전의 FontAwesome을 사용하는 경우) 이 옵션을 `true`로 설정합니다. 이 경우 사이트에 FontAwesome이 로드되어 있는지 확인해야 합니다. 그렇지 않으면 인앱 메시지가 올바르게 렌더링되지 않을 수 있습니다. |
| `inAppMessageZIndex` | `number` | `999999` | 기본적으로 Braze SDK는 z-index 999999로 In-App Messages를 표시합니다. 이 기본값을 재정의하려면 이 옵션에 값을 제공합니다. |
| `sessionTimeoutInSeconds` | `number` | `30` | 기본적으로 세션은 30초 동안 비활성 상태이면 타임아웃됩니다. 이 기본값을 재정의하려면 이 옵션에 값을 제공합니다. |
| `deviceId` | `string` | 자동 생성 | 기본적으로 Braze는 기기 ID로 임의의 GUID를 할당합니다. 사용자 정의 값으로 이 기본값을 재정의하려면 이 구성 옵션에 값을 제공합니다. |
| `appVersion` | `string` | `undefined` | 이 옵션에 값을 제공하면 Braze로 전송되는 사용자 이벤트가 지정된 버전과 연결되며, 이를 사용자 세분화에 사용할 수 있습니다. |
| `appVersionNumber` | `string` | `undefined` | 사용자 세분화에 사용할 수 있는 숫자 앱 버전 값입니다. 이 값은 "1.2.3.4"와 같이 네 개의 필드로 전송해야 하며, 그렇지 않으면 무시됩니다. 참고: `appVersion`도 동일한 값 또는 이 버전의 고유한 이름으로 설정해야 합니다. |
| `contentSecurityNonce` | `string` | `undefined` | 이 옵션에 값을 제공하면 Braze SDK가 SDK에서 생성하는 모든 `<script>` 및 `<style>` 요소에 nonce를 추가합니다. 이를 통해 Braze SDK가 웹사이트의 콘텐츠 보안 정책과 함께 작동하도록 할 수 있습니다. 이 nonce를 설정하는 것 외에도 FontAwesome 로드를 허용해야 할 수 있으며, 이는 콘텐츠 보안 정책 허용 목록에 `use.fontawesome.com`을 추가하거나 `doNotLoadFontAwesome` 옵션을 사용하고 수동으로 로드하여 수행할 수 있습니다. |
| `noCookies` | `boolean` | `false` | 기본적으로 Braze Web SDK는 쿠키를 사용합니다. 쿠키 사용을 비활성화하려면 이 옵션을 true로 설정합니다. 쿠키를 비활성화하면 세션 간에 사용자 ID를 기억하는 SDK의 기능에 영향을 줄 수 있습니다. |
| `allowCrawlerActivity` | `boolean` | `false` | 기본적으로 Braze Web SDK는 사용자 에이전트 문자열을 기반으로 Google과 같은 알려진 스파이더 또는 웹 크롤러의 활동을 무시합니다. 이를 통해 데이터 포인트를 절약하고, 분석을 더 정확하게 하며, 페이지 순위를 향상시킬 수 있습니다. 그러나 이러한 크롤러의 활동을 Braze에 기록하려면 이 옵션을 true로 설정할 수 있습니다. |
| `disablePushTokenMaintenance` | `boolean` | `false` | 기본적으로 이미 웹 푸시 권한을 부여한 사용자(예: requestPushPermission을 통해 또는 이전 푸시 제공자로부터)는 전달 가능성을 보장하기 위해 새 세션에서 자동으로 Braze 백엔드와 푸시 토큰을 동기화합니다. 이 동작을 비활성화하려면 이 옵션을 true로 설정합니다. |
| `enableSdkAuthentication` | `boolean` | `false` | SDK 인증 기능을 활성화하려면 true로 설정합니다. SDK 인증에 대한 자세한 내용은 제품 설명서를 참조하세요. |
| `manageServiceWorkerExternally` | `boolean` | `false` | 기본적으로 Braze Web SDK는 푸시 알림을 위해 자체 서비스 워커를 관리합니다. 애플리케이션에서 이미 서비스 워커를 관리하고 있으며 Braze 서비스 워커 기능을 통합하려는 경우 이 옵션을 true로 설정하고 서비스 워커 파일에 Braze 서비스 워커 코드를 포함합니다. |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | 기본적으로 트리거 동작(예: 인앱 메시지 표시)은 사용자당 최소 30초마다 한 번만 실행될 수 있습니다. 이 기본값을 재정의하려면 이 옵션에 값을 제공합니다. |
| `serviceWorkerLocation` | `string` | `undefined` | 기본적으로 Braze Web SDK는 도메인의 루트에서 서비스 워커 파일을 찾습니다. 이 기본값을 재정의하고 서비스 워커 파일의 사용자 정의 위치를 지정하려면 이 옵션에 값을 제공합니다. |
| `safariWebsitePushId` | `string` | `undefined` | Safari 푸시 알림에 필요합니다. 이 값은 Apple Developer 계정에서 확인할 수 있습니다. Safari 푸시 알림 설정에 대한 자세한 내용은 제품 설명서를 참조하세요. |
| `localization` | `string` | `undefined` | 이 옵션에 값을 제공하면 Braze SDK가 해당 로케일로 인앱 메시지와 Content Cards를 표시하려고 시도합니다. |
| `openInAppMessagesInNewTab` | `boolean` | `false` | 기본적으로 인앱 메시지의 링크는 같은 탭에서 열립니다. 새 탭에서 열리도록 하려면 이 옵션을 true로 설정합니다. |
| `openCardsInNewTab` | `boolean` | `false` | 기본적으로 Content Cards의 링크는 같은 탭에서 열립니다. 새 탭에서 열리도록 하려면 이 옵션을 true로 설정합니다. |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | 기본적으로 인앱 메시지는 외부를 클릭하거나 Escape 키를 눌러 닫을 수 있습니다. 사용자가 명시적으로 닫기 버튼이나 동작 버튼을 클릭하여 메시지를 닫도록 하려면 이 옵션을 true로 설정합니다. |
| `devicePropertyAllowlist` | `string[]` | `undefined` | 기본적으로 Braze SDK는 DeviceProperties의 모든 기기 속성을 자동으로 감지하고 수집합니다. 이 동작을 재정의하려면 DeviceProperties 배열을 제공합니다. Braze 서버로 전송되는 모든 속성을 비활성화하려면 빈 배열을 제공합니다. 일부 속성이 없으면 모든 기능이 제대로 작동하지 않을 수 있습니다. 예를 들어 시간대가 없으면 로컬 시간대 전달이 작동하지 않습니다. |
| `serviceWorkerScope` | `string` | `undefined` | 기본적으로 Braze Web SDK는 기본 범위(서비스 워커의 디렉토리)로 서비스 워커를 등록합니다. 이 기본값을 재정의하고 서비스 워커의 사용자 정의 범위를 지정하려면 이 옵션에 값을 제공합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Initialization Options" }

---

## 핵심 기능 {#core-features}

### 초기화 및 설정 {#initialization-setup}

#### 기본 초기화 {#basic-initialization}

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

#### 고급 초기화 옵션 {#advanced-initialization-options}

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

### 사용자 관리 {#user-management}

#### 사용자 변경 {#change-user}

``` typescript
import { changeUser } from "@braze/web-sdk";

// Change to a new user
changeUser('user-123');
```

#### 사용자 속성 설정 {#set-user-attributes}

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

#### 사용자 위치 설정 {#set-user-location}

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

#### 사용자 별칭 및 구독 그룹 {#user-aliases-and-subscription-groups}

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

#### 사용자 로그아웃 {#user-logout}

``` typescript
import { wipeData } from "@braze/web-sdk";

// There is no explicit method to logout. To "forget" the current users entirely, use wipeData().
// This is a complete data wipe (use with caution, this wipes things such as device ID)
wipeData();
```

### In-App Messages

#### 자동 표시 {#automatic-display}

``` typescript
import { automaticallyShowInAppMessages } from "@braze/web-sdk";

// Automatically show in-app messages
automaticallyShowInAppMessages();
```

#### 수동 표시 {#manual-display}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

// Subscribe to in-app messages
subscribeToInAppMessage((inAppMessage) => {
    // Show the message
    showInAppMessage(inAppMessage);
});
```

#### 커스텀 인앱 메시지 처리 {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### 인앱 메시지 상호작용 기록 {#log-in-app-message-interactions}

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

#### 커스텀 HTML 인앱 메시지 {#custom-html-in-app-messages}

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

#### Content Cards 표시 {#display-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show content cards in default location
showContentCards();

// Show in specific container
const container = document.getElementById('content-cards-container');
showContentCards(container);
```

#### Content Cards 업데이트 구독 {#subscribe-to-content-cards-updates}

``` typescript
import { subscribeToContentCardsUpdates } from "@braze/web-sdk";

subscribeToContentCardsUpdates((cards) => {
    console.log('Content cards updated:', cards);
    // Display cards or update UI
});
```

#### Content Cards 상호작용 기록 {#log-content-card-interactions}

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

#### Content Cards 필터링 {#filter-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show only pinned cards
// You can also provide a parent element instead of null
showContentCards(null, (cards) => {
    return cards.filter(card => card.getIsPinned());
});
```

#### Content Cards 새로고침 요청 {#request-content-cards-refresh}

``` typescript
import { requestContentCardsRefresh } from "@braze/web-sdk";

requestContentCardsRefresh(
    () => console.log('Content cards refreshed'),
    () => console.log('Failed to refresh content cards')
);
```

#### 커스텀 Content Cards {#custom-content-cards}

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

### 푸시 알림 {#push-notifications}

#### 푸시 권한 요청 {#request-push-permission}

``` typescript
import { requestPushPermission } from "@braze/web-sdk";

requestPushPermission(
    () => console.log('Push permission granted'),
    () => console.log('Push permission denied')
);
```

#### 푸시 지원 확인 {#check-push-support}

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

#### 푸시 등록 해제 {#unregister-push}

``` typescript
import { unregisterPush } from "@braze/web-sdk";

unregisterPush(
    () => console.log('Successfully unregistered'),
    () => console.log('Failed to unregister')
);
```

### 기능 플래그 {#feature-flags}

#### 기능 플래그 가져오기 {#get-feature-flag}

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

#### 기능 플래그 업데이트 구독 {#subscribe-to-feature-flag-updates}

``` typescript
import { subscribeToFeatureFlagsUpdates } from "@braze/web-sdk";

subscribeToFeatureFlagsUpdates((featureFlags) => {
    featureFlags.forEach(flag => {
        console.log(`Feature flag ${flag.getId()}: ${flag.getBooleanProperty('enabled')}`);
    });
});
```

#### 기능 플래그 노출 기록 {#log-feature-flag-impressions}

``` typescript
import { logFeatureFlagImpression } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_feature');
if (featureFlag) {
    logFeatureFlagImpression(featureFlag);
}
```

#### 기능 플래그 새로고침 요청 {#request-feature-flags-refresh}

``` typescript
import { refreshFeatureFlags } from "@braze/web-sdk";

refreshFeatureFlags(
    () => console.log('Feature flags refreshed'),
    () => console.log('Failed to refresh feature flags')
);
```

### 배너 {#banners}

#### 배너 가져오기 및 표시 {#get-and-display-banners}

``` typescript
import { getBanner, insertBanner } from "@braze/web-sdk";

const banner = getBanner('homepage_banner');
if (banner) {
    // Insert banner into specific element
    const container = document.getElementById('banner-container');
    insertBanner(banner, container);
}
```

#### 배너 업데이트 구독 {#subscribe-to-banner-updates}

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

#### 배너 새로고침 요청 {#request-banner-refresh}

``` typescript
import { requestBannersRefresh } from "@braze/web-sdk";

requestBannersRefresh(
    ["placement_1", "placement_2"],
    () => console.log('Banners refreshed'),
    () => console.log('Failed to refresh banners')
);
```

### 분석 및 이벤트 {#analytics-events}

#### 커스텀 이벤트 기록 {#log-custom-events}

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

#### 구매 기록 {#log-purchases}

``` typescript
import { logPurchase } from "@braze/web-sdk";

logPurchase('product-123', 29.99, 'USD', 1, {
    category: 'electronics',
    brand: 'Apple'
});
```

#### 데이터 플러시 요청 {#request-data-flush}

``` typescript
import { requestImmediateDataFlush } from "@braze/web-sdk";

// Force immediate data send
requestImmediateDataFlush();
```

### 세션 관리 {#session-management}

#### 세션 열기 {#open-session}

``` typescript
import { openSession } from "@braze/web-sdk";

// Start a new session
openSession();
```

#### SDK 상태 확인 {#check-sdk-status}

``` typescript
import { isInitialized, isDisabled } from "@braze/web-sdk";

if (isInitialized()) {
    console.log('SDK is initialized');

    if (isDisabled()) {
        console.log('SDK is disabled');
    }
}
```

#### SDK 활성화/비활성화 {#enabledisable-sdk}

``` typescript
import { enableSDK, disableSDK } from "@braze/web-sdk";

// Disable SDK
disableSDK();

// Re-enable SDK
enableSDK();
```

### 데이터 관리 {#data-management}

#### 데이터 삭제 {#wipe-data}

``` typescript
import { wipeData } from "@braze/web-sdk";

// Remove all locally stored data
wipeData();
```

#### SDK 제거 {#destroy-sdk}

``` typescript
import { destroy } from "@braze/web-sdk";

// Clean up SDK resources
destroy();
```

#### 기기 ID 가져오기 {#get-device-id}

``` typescript
import { getDeviceId } from "@braze/web-sdk";

const deviceId = getDeviceId();
console.log('Device ID:', deviceId);
```

#### SDK 인증 {#sdk-authentication}

``` typescript
import { setSdkAuthenticationSignature } from "@braze/web-sdk";

// Set authentication signature
setSdkAuthenticationSignature('your-signature-here');
```

#### 인증 실패 구독 {#subscribe-to-authentication-failures}

``` typescript
import { subscribeToSdkAuthenticationFailures } from "@braze/web-sdk";

subscribeToSdkAuthenticationFailures((error) => {
    console.log('Authentication failed:', error);
    // Provide new signature
    setSdkAuthenticationSignature('new-signature');
});
```

---

## 통합 패턴 {#integration-patterns}

### SSR 프레임워크 {#ssr-frameworks}

Next.js와 같은 서버 사이드 렌더링(SSR) 프레임워크를 사용하는 경우, SDK가 브라우저 환경에서 실행되도록 설계되어 있기 때문에 오류가 발생할 수 있습니다. SDK를 동적으로 가져오면 이러한 문제를 해결할 수 있습니다.

필요한 SDK 부분을 별도의 파일로 내보낸 다음 해당 파일을 컴포넌트에 동적으로 가져오면 트리 셰이킹의 이점을 유지할 수 있습니다.

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

또는 webpack을 사용하여 앱을 번들링하는 경우, 매직 코멘트를 활용하여 필요한 SDK 부분만 동적으로 가져올 수 있습니다.

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

Vite를 사용하면서 순환 종속성에 대한 경고나 `Uncaught TypeError: Class extends value undefined is not a constructor or null` 오류가 표시되는 경우, Braze SDK를 종속성 검색에서 제외해야 할 수 있습니다:

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Jest 프레임워크 {#jest-framework}

Jest를 사용할 때 `SyntaxError: Unexpected token 'export'`와 유사한 오류가 표시될 수 있습니다. 이를 해결하려면 `package.json`에서 Braze SDK를 무시하도록 구성을 조정합니다:

``` json
{
  "jest": {
    "transformIgnorePatterns": [
      "/node_modules/(?!@braze)"
    ]
  }
}
```

### 비동기 모듈 정의(AMD) {#asynchronous-module-definition-amd}

#### AMD 지원 비활성화 {#disable-amd-support}

사이트에서 RequireJS 또는 다른 AMD 모듈 로더를 사용하지만 CDN을 통해 Braze Web SDK를 로드하려는 경우, AMD 지원이 포함되지 않은 라이브러리 버전을 로드할 수 있습니다. 이 버전의 라이브러리는 CDN 위치 `https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`에서 로드할 수 있습니다.

#### 모듈 로더 {#module-loader}

RequireJS 또는 다른 AMD 모듈 로더를 사용하는 경우, 라이브러리의 사본을 자체 호스팅하고 다른 리소스와 마찬가지로 참조하는 것을 권장합니다:

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### 가속 모바일 페이지(AMP) {#accelerated-mobile-pages-amp}

AMP 통합을 위해 다음이 필요합니다:

1. **AMP 웹 푸시 스크립트 포함**: head에 비동기 스크립트 태그를 추가합니다
2. **구독 위젯 추가**: 사용자가 구독/구독 취소할 수 있는 위젯을 추가합니다
3. **헬퍼 파일 추가**: `helper-iframe.html` 및 `permission-dialog.html`을 포함합니다
4. **서비스 워커 생성**: Braze 서비스 워커 파일을 추가합니다
5. **AMP 웹 푸시 요소 구성**: API 키와 기본 URL을 쿼리 파라미터로 포함하여 `amp-web-push` 요소를 추가합니다

자세한 AMP 통합 지침은 [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#amp)를 참조하세요.

### Electron

Electron은 공식적으로 웹 푸시 알림을 지원하지 않습니다 (참조: 이 [GitHub 이슈](https://github.com/electron/electron/issues/6697)). Braze에서 테스트하지 않은 다른 [오픈 소스 해결 방법](https://github.com/MatthieuLemoine/electron-push-receiver)을 시도해 볼 수 있습니다.

### CDN 통합 {#cdn-integration}

- **스크립트 로딩**: 스크립트 태그 뒤에 초기화 코드를 배치하거나 스크립트 태그의 `onload` 이벤트 핸들러를 사용하여 스크립트 태그가 로드된 후 초기화합니다
- **전역 접근**: CDN을 통해 로드하면 SDK를 `window.braze`로 사용할 수 있습니다

### 서비스 워커(푸시 알림) {#service-worker-push-notifications}

- **필수**: 푸시 알림이 작동하려면 Braze 서비스 워커를 포함해야 합니다
- **등록**: `navigator.serviceWorker.register()`를 사용하여 웹사이트 코드에서 서비스 워커를 등록합니다
- **푸시 권한**: 사용자 상호작용(예: 버튼 클릭)에 대한 응답으로 `braze.requestPushPermission()`을 호출합니다. 브라우저 권한을 요청하기 전에 소프트 푸시 프롬프트(커스텀 UI)를 사용합니다

### 태그 관리자 {#tag-managers}

#### Tealium iQ

Tealium iQ는 기본적인 턴키 Braze 통합을 제공합니다. 통합을 구성하려면 Tealium 태그 관리 인터페이스에서 Braze를 검색하고 대시보드에서 Web SDK API 키를 제공합니다. 자세한 내용이나 심층적인 Tealium 구성 지원은 [통합 설명서]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium)를 확인하거나 Tealium 계정 매니저에게 문의하세요.

#### 기타 태그 관리자 {#other-tag-managers}

Braze는 커스텀 HTML 태그 내에서 통합 지침을 따르면 다른 태그 관리 솔루션과도 호환될 수 있습니다. 이러한 솔루션을 평가하는 데 도움이 필요하면 Braze 담당자에게 문의하세요.

---

## 라이브러리 {#libraries}

| 이름 | 설명 | npm | CDN URL
| ---- | ----------- | --- | -------
| Full | UI가 포함된 전체 SDK입니다. npm 버전을 사용할 때 JavaScript 번들러는 UI를 포함하여 사용하지 않는 코드를 제거합니다. | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.8/braze.min.js
| Core | UI가 없는 SDK입니다. 이 버전의 SDK를 사용할 때는 In-App Messages 및 Content Cards에 대한 자체 UI를 구현해야 합니다. UI 요소는 CSS를 통해 완전히 사용자 정의할 수 있으므로 일반적으로 전체 라이브러리 통합을 권장합니다. | N/A | https://js.appboycdn.com/web-sdk/6.8/braze.core.min.js
| No-AMD | AMD 지원이 없는 전체 SDK입니다. 사이트에서 RequireJS 또는 다른 AMD 모듈 로더를 사용하지만 CDN을 통해 SDK를 로드하려는 경우에 유용합니다. | N/A | https://js.appboycdn.com/web-sdk/6.8/braze.no-amd.min.js
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Libraries" }

## 지원 브라우저 {#supported-browsers}

- 최신 Chromium 기반 브라우저 (Chrome, Edge, Opera)
- Firefox
- Safari

## 디버깅 및 문제 해결 {#debugging-troubleshooting}

initialize 함수에 `enableLogging: true` 옵션을 전달하면(`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`) Braze가 JavaScript 콘솔에 로그를 기록합니다. 이는 개발에 유용하지만 모든 사용자에게 표시되므로, 프로덕션에 페이지를 릴리스하기 전에 이 옵션을 제거하거나 [대체 로거를 제공](https://js.appboycdn.com/web-sdk/6.8/doc/modules/braze.html#setlogger)해야 합니다.

## Font Awesome

Braze는 인앱 메시지 아이콘에 [Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0을 사용합니다. Font Awesome 로딩을 비활성화하려면 `doNotLoadFontAwesome` 초기화 옵션을 사용합니다. 사용 가능한 아이콘을 찾아보려면 [치트 시트](http://fortawesome.github.io/Font-Awesome/cheatsheet/)를 확인하세요.

## 추가 리소스 {#additional-resources}

- [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)
- [SDK 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [샘플 빌드](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## 문의 {#contact}

질문이 있으시면 [support@braze.com](mailto:support@braze.com)으로 연락해 주세요.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk)를 참조하세요.