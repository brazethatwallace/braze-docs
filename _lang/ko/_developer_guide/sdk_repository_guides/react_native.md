---
nav_title: React Native SDK
article_title: React Native SDK 리포지토리 가이드
page_order: 7
description: "GitHub에서 미러링된 Braze React Native SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze React Native SDK 소개 {#about-the-braze-react-native-sdk}

Braze React Native SDK는 iOS 및 Android 앱을 Braze에 연결합니다: 고객 프로필, 메시징 표면, 분석, 피처 플래그를 지원합니다. 네이티브 [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) 및 [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk)를 JavaScript API로 래핑합니다.

**초기화는 JavaScript 기반입니다:** Android 리소스와 iOS `AppDelegate`에서 네이티브 구성(푸시, 로깅, 델리게이트)을 설정한 다음, JavaScript에서 `Braze.initialize(apiKey, endpoint)`를 호출하여 SDK를 시작합니다. 이를 통해 SDK가 초기화되는 시점과 사용할 자격 증명을 완전히 제어할 수 있습니다. 초기화 후 필요에 따라 다른 SDK 메서드(예: `changeUser`, `logCustomEvent`)를 호출합니다.

### 주요 기능 {#what-you-can-do}

- **사용자 관리**: 사용자 식별, 프로필 필드 설정, 커스텀 속성, 별칭, 구독 그룹
- **인앱 메시지**: 기본 Braze UI 또는 구독 및 로깅 API를 통한 커스텀 처리
- **Content Cards**: 기본 피드 UI 또는 카드를 가져와 자체 UI 구축
- **배너**: `BrazeBannerView`를 포함한 배치 기반 HTML 배너
- **푸시 알림**: 권한 프롬프트, 토큰 등록, 페이로드 리스너(아래 플랫폼 참고 사항 참조)
- **피처 플래그**: 새로고침, 속성 읽기, 노출 기록
- **분석**: 커스텀 이벤트, 구매, 즉시 플러시
- **SDK 제어**: SDK 활성화/비활성화, 로컬 데이터 삭제, SDK 인증 서명

## 필수 조건 {#prerequisites}

- **Braze 계정** (앱 API 키 및 SDK 엔드포인트 포함)
- **React Native** 개발 환경 ([React Native 환경 설정](https://reactnative.dev/docs/set-up-your-environment))
- **iOS**: Xcode, CocoaPods (`cd ios && pod install`)
- **Android**: Android Studio / Gradle; React Native 템플릿에서 요구하는 Kotlin Gradle 플러그인
- **푸시** (사용 시): FCM (Android) 및 APNs (iOS) 설정 ([푸시 설명서]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications) 참조)

대시보드에서 자격 증명 위치를 확인하려면 [통합 개요]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native)를 참조하세요.

## 설치 {#installation}

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## 빠른 시작 {#quick-start}

이 섹션에서는 Braze React Native SDK를 초기화하는 데 필요한 최소 설정을 보여줍니다.

1. npm 패키지를 설치합니다(위 참조).
2. Android 및 iOS에 대한 **네이티브 설정**을 완료합니다(구성, 권한, 필요 시 푸시).
3. JavaScript에서 SDK를 초기화하고 사용을 시작합니다:

``` typescript
import Braze from "@braze/react-native-sdk";

// Initialize the SDK — call early in your app lifecycle (e.g. in a useEffect).
// The API key and endpoint are passed from JavaScript; native configuration
// (push, logging, etc.) is applied automatically from your native setup.
Braze.initialize("<YOUR_API_KEY>", "<YOUR_SDK_ENDPOINT>");

Braze.changeUser("user-123");
Braze.logCustomEvent("button_clicked", { screen: "home" });
```

TypeScript 타이핑은 패키지와 함께 제공됩니다(GitHub의 `src/index.d.ts`).

다른 자격 증명으로 `Braze.initialize`를 다시 호출하면 현재 인스턴스를 해제하고 다시 생성하여 세션 중 재초기화를 지원합니다.

---

## 네이티브 설정 {#native-setup}

> **정보 출처:** 단계별 화면, Gradle/CocoaPods 변경 사항, Android XML 키의 전체 목록은 [Braze React Native 개발자 가이드]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native)에 있습니다. 아래 스니펫은 최소한의 예시입니다.

### Android

- 템플릿에 아직 포함되어 있지 않은 경우 루트 `build.gradle`에 **Kotlin Gradle 플러그인**을 추가합니다(버전은 React Native 버전에 따라 다름).
- `res/values`에 구성이 포함된 `braze.xml` 리소스 파일을 추가합니다. JavaScript에서 `Braze.initialize()`를 호출할 때까지 SDK가 대기하도록 지연 초기화를 활성화합니다. 다른 구성 값(푸시, 세션 타임아웃 등)은 여전히 이 파일에서 읽혀 초기화 시 적용됩니다.
- `AndroidManifest.xml`에 `INTERNET` 및 `ACCESS_NETWORK_STATE`와 같은 기본 권한을 확인합니다.
- 푸시의 경우 FCM 통합 및 문서에 설명된 Braze 관련 발신자 ID / 등록 플래그를 완료합니다.

``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- Enable delayed initialization so the SDK starts when
       Braze.initialize() is called from JavaScript. -->
  <bool name="com_braze_enable_delayed_initialization">true</bool>

  <!-- Additional native configuration (applied at initialization time) -->
  <bool name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">YOUR_SENDER_ID</string>
</resources>
```

{% alert note %}
** API 키와 엔드포인트는 더 이상 `braze.xml`에서 설정하지 않습니다. JavaScript에서 `Braze.initialize(apiKey, endpoint)`를 통해 전달됩니다.
{% endalert %}
### iOS

``` bash
cd ios && pod install
```

`AppDelegate`에서 `BrazeReactInitializer.configure`를 사용하여 네이티브 구성을 등록합니다. 제공하는 클로저는 저장되었다가 나중에 JavaScript에서 `Braze.initialize(apiKey, endpoint)`가 호출될 때 적용됩니다.

``` swift
import BrazeKit
import braze_react_native_sdk

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Register native configuration for when JS calls Braze.initialize().
    BrazeReactInitializer.configure { config in
      config.logger.level = .info
      config.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup
    return true
  }
}
```

- **`configure` 클로저**: `Braze.Configuration`을 수신하며 네이티브 구성 속성(로깅, 푸시, 세션 등)을 설정할 수 있습니다. API 키와 엔드포인트는 JavaScript에서 제공되므로 여기서 설정하지 않습니다.
- **`postInitialization` 클로저** *(선택 사항)*: 생성 후 라이브 `Braze` 인스턴스를 수신하며, 인스턴스가 필요한 설정(예: 참조 저장, 델리게이트 설정)에 사용합니다.

{% alert note %}
** `BrazeReactInitializer.configure`는 더 이상 사용되지 않는 `BrazeReactBridge.initBraze(_:)`를 대체하는 Swift 우선 API입니다. 또한 Objective-C 브리지에서 `Braze.Configuration`의 Swift 타입 해석 문제를 해결합니다.
{% endalert %}
---

## 구성 참조 {#configuration-reference}

React Native에서 **구성은 네이티브**입니다: Android는 `res/values/braze.xml`을 읽고, iOS는 **`BrazeReactInitializer.configure`**를 통해 등록된 클로저를 사용합니다. 둘 다 JavaScript에서 `Braze.initialize(apiKey, endpoint)`가 호출될 때 적용됩니다.

### Android (`braze.xml`)

기본값은 XML에 있으며, [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)로 시작 시 재정의할 수 있습니다. 키와 타입의 공식 목록은 [Android SDK 통합 가이드]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration) 및 [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html)에 있습니다(각 Kotlin 속성은 문서화된 `com_braze_*` 리소스에 해당합니다).

자주 사용되는 항목:

| 키 | 리소스 타입 | 설명 |
|-----|---------------|-------------|
| `com_braze_enable_delayed_initialization` | `bool` | **필수.** JavaScript에서 `Braze.initialize()`를 호출할 때까지 SDK가 대기하도록 `true`로 설정합니다. |
| `com_braze_api_key` | `string` | JavaScript에서 `Braze.initialize()`를 사용할 때는 필요하지 않습니다(자격 증명은 JS에서 전달됨). 레거시 네이티브 우선 초기화에만 필요합니다. |
| `com_braze_custom_endpoint` | `string` | JavaScript에서 `Braze.initialize()`를 사용할 때는 필요하지 않습니다. 레거시 네이티브 우선 초기화에만 필요합니다. |
| `com_braze_server_target` | `string` | 선택적 클러스터 / 환경 선택기(예: 일부 내부 또는 스테이징 빌드). Braze 통합에서 별도로 지정하지 않는 한 프로덕션에서는 `com_braze_custom_endpoint`를 사용하세요. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | `true`이면 Braze가 FCM에 등록합니다(일반적인 푸시 설정). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | 자동 등록이 활성화된 경우의 FCM 발신자 ID입니다. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Braze가 푸시 딥링크를 자동으로 열도록 합니다. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | 인앱 메시지 트리거 동작 사이의 최소 시간(초)입니다. |
| **기타** | *다양함* | 여기에 표시되지 않은 추가 키(세션 타임아웃, 지오펜스, 위치, 알림 기본값, 기기 허용 목록, 지연 초기화, SDK 인증 등). [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) 및 [Android SDK 통합 가이드]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

`BrazeReactInitializer.configure`에 전달되는 `configure` 클로저에서 네이티브 구성 속성을 설정합니다. 클로저는 `Braze.Configuration` 인스턴스를 수신하며, API 키와 엔드포인트는 JavaScript `Braze.initialize` 호출에서 자동으로 설정됩니다. 전체 세부 정보: [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) 및 중첩 타입 **`api`**, **`push`**, **`logger`**, **`location`**.

| 영역 | 멤버 (대표적) | 참고 |
|------|--------------------------|--------|
| **자격 증명** | `api.key`, `api.endpoint` | JavaScript의 `Braze.initialize(apiKey, endpoint)`에서 자동으로 설정됩니다. `configure` 클로저에서 설정하지 마세요. |
| **로깅** | `logger.level` | 상세 로깅은 개발용입니다. 프로덕션에서는 노이즈를 줄이세요. |
| **푸시** | `push.automation`, `push.appGroup`, … | 자동화는 등록을 간소화합니다. Push Stories / 확장 프로그램 사용 시 `appGroup`이 필요합니다. |
| **인앱 메시지** | `triggerMinimumTimeInterval` | 트리거 사이 기본 **30**초입니다. |
| **세션** | `sessionTimeout` | 새 세션 시작 전 비활성 시간(Braze 세션 문서 참조). |
| **개인정보 / 데이터** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | [개인정보 매니페스트]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest) 및 SDK 인증 제품 설정에 맞춰 조정합니다. |
| **네트워킹** | `api.requestPolicy`, `api.flushInterval` | 요청 재시도 정책 및 플러시 주기입니다. |
| **푸시 구독** | `optInWhenPushAuthorized` | `true`이면 사용자가 알림을 승인한 후 구독이 옵트인으로 전환될 수 있습니다. |
| **IAM + 사용자 변경** | `preventInAppMessageDisplayForDifferentUser` | 사용자 ID가 변경될 때 불일치하는 IAM을 줄입니다. |
| **기타** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | 전체 동작은 Swift 설명서를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

React Native 브리지는 초기화 시 React 전용 **`api.sdkFlavor`** / SDK 메타데이터를 설정합니다. Braze 설명서에서 지시하지 않는 한 이를 재정의하지 마세요.

---

## JavaScript / TypeScript API

패키지 기본 내보내기는 **정적** 메서드가 있는 `Braze` 클래스입니다(예: `Braze.changeUser`, `Braze.logPurchase`). `Braze.Events`, `Braze.Genders`, `Braze.NotificationSubscriptionTypes`와 같은 상수도 동일한 내보내기에 연결되어 있습니다.

---

## 핵심 기능 {#core-features}

### 사용자 관리 {#user-management}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

선택적 **SDK 인증**: `changeUser`의 두 번째 인수로 서명을 전달하거나, 대시보드에서 활성화된 경우 `Braze.setSdkAuthenticationSignature(signature)`를 호출합니다.

### 인앱 메시지 {#in-app-messages}

- **기본 Braze UI**를 사용하는 경우 [인앱 메시지 설명서]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=react%20native)를 따르세요. 기본 UI만 표시하려면 일반적으로 `subscribeToInAppMessage`를 호출할 **필요가 없습니다**.
- **커스텀** 처리의 경우 `useBrazeUI: false`로 구독한 다음 필요에 따라 노출/클릭을 기록합니다:

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getContentCards();
Braze.requestContentCardsRefresh();
Braze.launchContentCards(); // default Braze UI

Braze.logContentCardImpression(cardId);
Braze.logContentCardClicked(cardId);
```

`Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, ...)`로 업데이트를 수신합니다.

### 배너 {#banners}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.requestBannersRefresh(["homepage_banner"]);
const banner = await Braze.getBanner("homepage_banner");

// Or use the native Banner view:
// <Braze.BrazeBannerView placementID="homepage_banner" />
```

### 푸시 알림 {#push-notifications}

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`**: 알림에서 앱이 열릴 때 RN `Linking` 경합 조건을 방지하기 위해 사용합니다. TypeScript 문서 주석 및 샘플 앱에 설명된 대로 네이티브 후크(iOS의 `BrazeReactUtils`, Android의 `BrazeReactUtils.populateInitialPushPayloadFromIntent`)가 필요합니다.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`**는 공개 타이핑에 따라 **Android 전용**입니다.

### 피처 플래그 {#feature-flags}

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### 분석 및 구매 {#analytics-and-purchases}

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

참고: `logPurchase`는 **가격을 문자열로** 받습니다(타이핑 참조).

### 데이터 관리 및 SDK 상태 {#data-management-and-sdk-state}

**`changeUser`**는 Braze에 **새로운** 활동을 어떤 사용자 ID에 귀속시킬지만 알려줍니다. 기기에 캐시된 SDK 데이터를 지우지 **않습니다**. 별도의 "로그아웃" API는 없습니다: 기존 로그아웃(이전 사용자의 캐시된 프로필, 메시지, 토큰이 이 설치에서 사라지도록 로컬 Braze 상태를 지우는 것)이 필요한 경우 일반적으로 **`wipeData()`**를 사용합니다. 이는 전체 로컬 초기화입니다.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — 이 설치에 대한 Braze의 **로컬** 데이터(캐시된 사용자/세션/카드 상태, 푸시 토큰 연결 등)를 지웁니다. 이전 사용자의 Braze 상태를 기기에 남기지 않아야 하는 **로그아웃 스타일** 동작, **"이 기기에서 내 데이터 삭제"**, 재설치 없이 **QA** 초기화, 또는 엄격한 **개인정보** 흐름에 사용합니다. **`changeUser`**만으로는 해당 정리를 수행하지 않으며, **새로운** 이벤트를 수신할 사용자 ID만 설정합니다. **iOS**에서는 동작이 Android와 다를 수 있습니다(예: SDK 비활성화 상태와의 상호작용). 프로덕션에서 사용하는 경우 Braze의 네이티브 문서를 참조하세요.

**`disableSDK()`** — SDK 작동을 중지합니다(구성된 대로 수집/전달 없음). **사용자 옵트아웃** 토글, **제한 모드**(규정 준수, 어린이 설정), 또는 종속성을 제거하지 않고 **디버깅**에 사용합니다.

**`enableSDK()`** — **`disableSDK()`** 이후 SDK를 다시 켭니다. **iOS**에서는 다시 활성화가 **다음 앱 실행**까지 적용되지 않을 수 있습니다. 즉시 재활성화에 의존하기 전에 Braze Swift/iOS 설명서에서 확인하세요.

---

## 이벤트 {#events}

`Braze.addListener(event, callback)`로 구독합니다. 호출은 구독 오브젝트를 반환하며, 수신을 중지하려면 **`.remove()`**를 호출합니다.

**리스너 설정:**

``` typescript
import Braze from "@braze/react-native-sdk";

const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (update) => {
    console.log("Content cards:", update.cards);
  }
);
```

**리스너 제거:**

``` typescript
subscription.remove();
```

React 컴포넌트에서는 구독을 저장하고 정리 시 `.remove()`를 호출합니다(예: `useEffect`의 반환):

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| 이벤트 상수 | 페이로드 (요약) |
|----------------|-------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | 최신 Content Cards |
| `Braze.Events.BANNER_CARDS_UPDATED` | 최신 배너 |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | 피처 플래그 배열 |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | 인앱 메시지 이벤트 |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | SDK 인증 오류 세부 정보 |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | 푸시 페이로드 (**Android 전용**) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이벤트" }

---

## 통합 참고 사항 {#integration-notes}

- **Expo**: 가능한 경우 수동 네이티브 연결을 피하기 위해 [Braze Expo 플러그인](https://github.com/braze-inc/braze-expo-plugin)을 사용합니다.
- **새 아키텍처 / Turbo Modules**: 최신 플러그인 버전에서 지원됩니다. 마이그레이션하는 경우 개발자 가이드 및 샘플 `AppDelegate` / Gradle 설정을 따르세요.
- **개인정보 (iOS)**: `updateTrackingPropertyAllowList`와 같은 메서드는 개인정보 매니페스트 관련 구성을 지원합니다. [Swift 개인정보 매니페스트]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)를 참조하세요.
## - **Jest**: `react-native` 네이티브 모듈 또는 Braze Turbo 모듈을 모킹합니다(패턴은 이 리포지토리의 `__tests__/jest.setup.js`를 참조하세요). {#jest-mock-react-native-native-modules-or-the-braze-turbo-module-see-__tests__jestsetupjs-in-this-repo-for-patterns}

## 버전 지원 {#version-support}

{% alert note %}
이 SDK는 React Native 버전 **0.85.3**으로 테스트되었습니다.
{% endalert %}
다음 표는 Braze 플러그인 릴리스별 지원되는 React Native 버전을 나열합니다.

| Braze 플러그인 | React Native | 새 아키텍처 |
|--------------|--------------|------------------|
| 9.0.0+       | ≥ 0.71       | 예              |
| 6.0.0+       | ≥ 0.68       | 예 (≥ 0.70.0)   |
| 2.0.0+       | ≥ 0.68       | 예              |
| ≤ 1.41.0     | ≤ 0.71       | 아니요               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="버전 지원" }

네이티브 SDK 요구 사항도 확인하세요:

- [Android SDK 버전 정보](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Swift SDK 버전 정보](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Braze Expo 플러그인 {#braze-expo-plugin}

Expo 관리 워크플로의 경우 [Braze Expo 플러그인 리포지토리](https://github.com/braze-inc/braze-expo-plugin)를 참조하세요.

---

## 샘플 앱 {#sample-app}

이 리포지토리의 `BrazeProject`는 전체 샘플입니다(사용자 관리, Content Cards, 피처 플래그, 배너 등).

``` bash
cd BrazeProject/
yarn install
npx react-native start
```

**iOS** (`BrazeProject`에서):

``` bash
cd ios && pod install && cd ..
npx react-native run-ios
```

레거시 아키텍처가 필요한 경우 `RCT_NEW_ARCH_ENABLED=0 pod install`을 사용합니다.

**Android** (`BrazeProject`에서):

``` bash
npx react-native run-android
```

---

## 디버깅 및 문제 해결 {#debugging-and-troubleshooting}

개발 중 **네이티브** 구성에서 Braze 로깅을 활성화하여 SDK가 시스템 콘솔(Xcode / Android Logcat)에 기록하도록 합니다. 이를 통해 초기화, 사용자 변경, 이벤트 전달을 확인할 수 있습니다.

- **iOS** — `BrazeReactInitializer.configure`에 전달되는 `configure` 클로저에서 `config.logger.level = .debug`(또는 `.info`)를 설정합니다. 프로덕션에서는 사용자에게 로그가 표시되지 않도록 줄이거나 비활성화합니다.
- **Android** — `braze.xml`에서 `com_braze_logger_initial_log_level` 리소스를 사용하거나 `BrazeConfig.Builder`에서 동등한 설정을 합니다([BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html) 참조). 릴리스 전에 비상세 수준을 사용하거나 재정의를 제거합니다.

더 깊은 문제 해결(네트워크, 세션 또는 Campaign 동작)은 [Braze React Native 개발자 가이드]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) 및 네이티브 SDK 문서([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk))를 참조하세요.

---

## 추가 리소스 {#additional-resources}

- [Braze 개발자 가이드 — React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native)
- [푸시 알림 — React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications)
- [GitHub 리포지토리](https://github.com/braze-inc/braze-react-native-sdk)
- [npm 패키지](https://www.npmjs.com/package/@braze/react-native-sdk)

## 문의 {#contact}

질문이 있으시면 [support@braze.com](mailto:support@braze.com)으로 연락해 주세요.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk)를 참조하세요.