---
nav_title: 마이그레이션 FAQ
article_title: iOS SDK 마이그레이션 FAQ
platform: iOS
page_order: 12
description: "이 페이지에서는 Appboy iOS SDK(Objective-C)에서 Braze Swift SDK로 마이그레이션할 때 자주 묻는 질문에 대한 답변을 제공합니다."
noindex: true
---

# iOS SDK 마이그레이션 FAQ {#ios-sdk-migration-faq}

> 이 페이지에서는 레거시 Appboy iOS SDK(Objective-C SDK라고도 함)에서 Braze Swift SDK로 마이그레이션할 때 자주 묻는 질문에 대한 답변을 제공합니다.

{% multi_lang_include deprecations/objective-c.md %}

## 버전 지원 및 지원 종료 {#version-support-and-end-of-life}

### Appboy iOS SDK 4.7.0은 지원이 종료되었나요? {#is-appboy-ios-sdk-470-end-of-life}

네, Appboy iOS SDK 4.7.0(및 모든 4.x 버전)은 지원이 종료되었습니다. 보안 수정이나 중요한 버그 수정은 제공되지 않습니다. 메시징 및 분석 기능은 정상적으로 작동하지만, 보안 관점에서 4.7.0 버전은 지원되지 않는 것으로 간주해야 합니다.

### 프로덕션 지원을 위한 최소 Swift SDK 버전은 무엇인가요? {#what-is-the-minimum-swift-sdk-version-for-production-support}

현재 메이저 버전(16.x 이상)이 지속적인 지원, 버그 수정 및 새로운 기능의 대상입니다. 이전 마이너 버전은 지속적인 유지보수를 받지 못할 수 있습니다.

## 호환성 라이브러리 {#compatibility-libraries}

### BrazeKitCompat 및 BrazeUICompat는 Swift SDK 17.x에서 프로덕션 사용이 지원되나요? {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

네, `BrazeKitCompat` 및 `BrazeUICompat`는 마이그레이션 기간 동안 프로덕션 사용이 지원됩니다. 이 라이브러리들은 Appboy SDK에서 Swift SDK로 최소한의 코드 변경으로 전환할 수 있도록 돕는 최소 마이그레이션 "디딤돌"로 자리매김되어 있으며, 장기적인 목적지가 아닙니다. 공식적으로 지원되며 여전히 버그 수정을 받고 있지만, 궁극적으로는 이러한 호환성 라이브러리에서 최신 Swift SDK API로 마이그레이션하는 것이 목표입니다.

### BrazeKitCompat 및 BrazeUICompat는 언제 제거되나요? {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

Swift SDK 팀은 `BrazeKitCompat` 라이브러리를 종료할 계획이 있지만, 아직 구체적인 일정은 발표되지 않았습니다. 호환성 라이브러리에 무기한 의존하기보다는 최신 Swift SDK API(`BrazeKit`, `BrazeUI`)로의 전체 마이그레이션을 계획하는 것을 권장합니다.

## 지연 초기화 {#delayed-initialization}

### 사용자 동의를 받을 때까지 SDK 초기화를 지연할 수 있나요? {#can-i-delay-sdk-initialization-until-after-user-consent}

네. Swift SDK는 지연 초기화를 지원하며, 이는 SDK를 시작하기 전에 사용자 동의를 기다려야 하는 앱에 유용합니다. `application(_:didFinishLaunchingWithOptions:)`에서 초기에 `Braze.prepareForDelayedInitialization()`을 호출하고(선택적으로 `analyticsBehavior` 매개변수 포함), 동의를 받은 후 표준 Braze 이니셜라이저를 호출하여 SDK를 나중에 초기화합니다.

자세한 구현 방법은 [지연 초기화 설정]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional)을 참조하세요.

### 지연 초기화에 필요한 최소 Swift SDK 버전은 무엇인가요? {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

Swift SDK 11.2.0이 지연 초기화를 위한 최소 버전입니다. 지연 초기화에 대한 푸시 및 딥링크 안정성은 14.1.0 버전에서 더욱 개선되었습니다. Swift SDK 17.0.0은 이 두 기준을 모두 충분히 넘습니다.

### SDK가 초기화되기 전에 수신된 이벤트는 어떻게 되나요? {#what-happens-to-events-received-before-the-sdk-is-initialized}

SDK가 초기화되면 대기줄에 있는 항목이 처리됩니다. 그러나 채널에 따라 동작이 다릅니다.

| 채널 | 초기화 전 동작 |
|---------|----------------------------|
| 푸시 토큰 | 대기줄에 추가됨; 초기화 시 처리됨 |
| 푸시 열람/분석 | 기본적으로 대기줄에 추가됨(`analyticsBehavior`를 통해 삭제하도록 설정 가능) |
| 딥링크 | 대기줄에 추가됨; 초기화 시 처리됨 |
| 인앱 메시지 | 초기화 전에는 버퍼링되지 않음; SDK가 실행 중이어야 함 |
| Content Cards | 초기화 전에는 버퍼링되지 않음; 초기화 후 서버에서 동기화됨 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
초기화 전에 수신된 인앱 메시지와 Content Cards는 전달이 보장되지 않습니다. 이러한 채널을 표시하기 전에 SDK가 초기화되어 있는지 확인하세요.
{% endalert %}

## 리소스 번들 및 SPM 통합 {#resource-bundles-and-spm-integration}

### `braze-swift-sdk_BrazeUI.bundle` 누락에 대한 런타임 오류가 표시되는 이유는 무엇인가요? {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

이것은 알려진 SDK 버그가 아니며 통합 구성 오류로 인한 것일 가능성이 높습니다. Swift SDK 12.0.0부터 정적 XCFrameworks는 외부 리소스 번들에 의존하지 않고 리소스를 직접 포함합니다.

### 리소스 임베딩을 위한 SPM/Xcode/아카이브 요구 사항은 무엇인가요? {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

Swift SDK 12.0.0부터 Xcode 프로젝트 설정에서 Braze XCFrameworks에 대해 **Embed & Sign**을 선택해야 합니다. 이는 정적 및 동적 배리언트 모두에 적용됩니다. 이것이 아카이브 또는 릴리스 시 번들 누락 오류의 가장 일반적인 근본 원인입니다.

### 비표준 빌드 시스템에서 리소스 번들을 재정의하려면 어떻게 하나요? {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

비표준 빌드 시스템(Tuist, Bazel, Buck, CI)의 경우 승인된 재정의 API를 사용하세요:

- `BrazeKit.overrideResourcesBundle`(복수형 "Resources"에 유의)
- `BrazeUI.overrideResourcesBundle`(복수형 "Resources"에 유의)

단수형 `overrideResourceBundle`은 Swift SDK 8.1.0에서 더 이상 사용되지 않으며 사용해서는 안 됩니다.

## 사용자 ID 및 푸시 토큰 {#user-identity-and-push-tokens}

### 프로필, 기기 연결 및 푸시 토큰을 보존하기 위한 검증 체크리스트가 있나요? {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

공식적인 마이그레이션 전용 체크리스트는 설명서에 존재하지 않습니다. 다음 검증 단계를 수행하는 것을 권장합니다:

1. 마이그레이션 후 `registerDeviceToken` 또는 푸시 자동화가 올바르게 연결되어 있는지 확인합니다.
2. 출시 전후로 대시보드에서 푸시 등록 사용자 수를 확인합니다.
3. 몇 가지 특정 외부 ID를 샘플 확인하여 기기 연결이 그대로 유지되는지 확인합니다.

### `changeUser`는 푸시 토큰이 새 사용자를 따라가는 것을 보장하나요? {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

문서에 명시적인 보장이 기재되어 있지는 않습니다. 그러나 설계 의도는 푸시 토큰이 사용자가 아닌 기기를 따르는 것입니다. `changeUser`를 호출하면 기존 기기 토큰이 새 고객 프로필에 다시 연결됩니다. 대규모 출시 전에 `changeUser`를 테스트하고, 대시보드를 확인하며, 새 프로필에 토큰이 표시되는지 확인해야 합니다.