---
nav_title: 홈
article_title: Braze의 새로운 기능
description: "Braze 릴리스 노트는 매월 게시되어 주요 제품 릴리스, 지속적인 제품 개선, Braze 파트너십, SDK 주요 변경 사항 및 기능 지원 중단에 대한 최신 정보를 확인할 수 있습니다."
page_order: 0
search_rank: 1
page_type: reference

---

# Braze의 새로운 기능 {#whats-new-in-braze}

{% alert tip %}
이 페이지에 나열된 업데이트에 대한 자세한 내용은 계정 매니저에게 문의하거나 [지원 티켓을 개설하세요]({{site.baseurl}}/user_guide/administer/personal/braze_support/). 월간 SDK 릴리스, 개선 사항 및 주요 변경 사항에 대한 자세한 내용은 [SDK 체인지로그]({{site.baseurl}}/developer_guide/changelogs/)에서 확인할 수 있습니다.
{% endalert %}

{% details 2026년 5월 28일 %}

## 2026년 5월 28일 릴리스 {#may-28-2026-release}

### 데이터 및 보고 {#data-reporting}

#### 푸시 성과 대시보드 {#push-performance-dashboard}

[푸시 성과 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard)는 구성 가능한 시간 범위에 걸쳐 전송, 반송, 전달, 직접/영향/총 열람률을 포함한 푸시 참여에 대한 단일 채널 수준 뷰를 제공합니다. 개별 캠페인이나 Canvas의 데이터를 집계하지 않고도 푸시 채널의 전반적인 상태를 파악하는 데 사용할 수 있습니다.

#### 카탈로그 선택에서의 지리 위치 필드 {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

카탈로그는 이제 새로운 지리 위치 필드 유형과 카탈로그 선택 연산자를 사용한 거리 기반 필터링을 지원합니다. 이를 통해 각 사용자에게 가장 가까운 레스토랑을 표시하거나, 부동산 캠페인을 위해 50km 이내의 매물을 필터링하거나, 특정 이벤트 근처의 매장을 타겟팅하는 등 더 관련성 높은 위치 인식 경험을 만들 수 있습니다. 도시 또는 지역 코드로 지리적 타겟팅을 근사하는 대신, 사용자의 가장 최근 위치와 같은 Liquid 사용자 속성을 포함하여 중심점에 대한 근접성으로 카탈로그 항목을 필터링할 수 있습니다. 자세한 내용은 [선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#how-it-works)을 참조하세요.

#### 보고서 빌더에 배너 및 RCS 추가 {#banner-and-rcs-for-report-builder}

[보고서 빌더]({{site.baseurl}}/report_builder/)는 배너를 채널로, RCS를 SMS의 하위 카테고리로 지원하므로 다른 모든 Braze 채널과 함께 커스텀 보고서에서 두 가지 모두의 성과를 직접 측정할 수 있습니다.

#### `ecommerce.cart_updated` 이벤트 액션 {#ecommercecart_updated-event-actions}

[`ecommerce.cart_updated` 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples)는 `replace`와 함께 `add` 및 `remove` 액션을 지원하여 매번 업데이트할 때마다 전체 장바구니 스냅샷 대신 증분 장바구니 변경 사항을 전송할 수 있습니다.

### BrazeAI<sup>TM</sup>

#### SMS, MMS 및 RCS 메시지를 위한 콘텐츠 최적화 프로그램 {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

[콘텐츠 최적화 프로그램]({{site.baseurl}}/user_guide/brazeai/content_optimizer/)을 사용하여 SMS, MMS 및 RCS 메시지의 훅, 본문 및 CTA를 최적화할 수 있습니다. 콘텐츠 최적화 프로그램은 AI를 사용하여 대량의 콘텐츠 변형을 자동으로 생성하고 평가하여 메시지 콘텐츠를 대규모로 테스트하고 최적화하는 데 도움이 되는 에이전트입니다.

### 오케스트레이션 {#orchestration}

#### 워크스페이스 시간대 {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

[워크스페이스 시간대]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone/)를 사용하여 개별 워크스페이스에 대한 특정 시간대를 정의할 수 있습니다. 이를 통해 예약된 캠페인과 Canvas(현지 시간 또는 Intelligent Timing을 사용하지 않는 경우)가 전체 회사 시간대가 아닌 워크스페이스의 지정된 시간대에 따라 전송됩니다.

메시지 전송을 위한 워크스페이스 시간대는 점진적으로 출시되고 있으므로 대시보드에서 아직 이러한 설정이 표시되지 않을 수 있습니다.

### 채널 및 터치포인트 {#channels-touchpoints}

#### WhatsApp `inbound_profile_name`

Meta의 인바운드 메시징 웹훅에서 사용자의 WhatsApp 표시 이름을 자동으로 캡처하여 사용자의 Braze 프로필에 기록할 수 있습니다. 인바운드 WhatsApp 메시지가 수신되면 Braze는 프로필 이름을 새로운 WhatsApp Liquid 속성인 [{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)으로 노출하며, 이를 Canvas 사용자 업데이트 단계에서 참조하여 프로필 필드에 저장할 수 있습니다.

#### 고아 SMS 구독 상태 {#orphaned-sms-subscription-states}

Braze는 [고아 구독 상태 레코드를 자동으로 관리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#how-braze-handles-orphaned-subscription-states)합니다(사용자 프로필에 연결되지 않은 전화번호 또는 이메일 주소에 저장된 구독 데이터). 이를 통해 의도하지 않은 구독 상태 상속을 방지합니다. 이는 새로 생성된 사용자 프로필이 이전에 삭제되었거나 관련 없는 사용자의 구독 상태를 잘못 상속하는 시나리오로부터 사용자를 보호합니다.

### 파트너십 {#partnerships}

#### Chord - 고객 데이터 플랫폼 {#chord-customer-data-platform}

[Chord](https://www.chord.co/)는 이커머스 스토어프론트에서 이벤트를 캡처하고 표준화하는 고객 데이터 플랫폼을 제공합니다. Chord를 Braze에 연결하면 구매 활동, 행동 이벤트 및 ID 업데이트가 Braze로 유입되어 파이프라인을 직접 구축하지 않고도 캠페인을 트리거하고 프로필을 최신 상태로 유지할 수 있습니다.

자세한 내용은 [Chord]({{site.baseurl}}/partners/chord/)를 참조하세요.

#### Better Email - 템플릿 {#better-email-templates}

[Better Email](https://www.betteremail.dev)은 이메일 디자인 시스템을 중심으로 구축된 협업 이메일 제작 플랫폼입니다. 팀은 공유 블록 및 스타일 시스템에서 프로덕션 준비가 된 이메일을 디자인, 관리 및 내보낼 수 있어 개발자나 에이전시에 의존하지 않고도 대규모로 브랜드 일관성을 보장할 수 있습니다.

자세한 내용은 [Better Email]({{site.baseurl}}/partners/better_email/)을 참조하세요.

#### DailyPlay - 동적 콘텐츠 {#dailyplay-dynamic-content}

[DailyPlay](https://dailyplay.ai/)는 게임화 플랫폼입니다. 개인화된 브랜드 게임과 내장 보상 시스템을 출시하여 참여를 심화하고 유지율을 개선하는 데 사용할 수 있습니다.

자세한 내용은 [DailyPlay]({{site.baseurl}}/partners/dailyplay/)를 참조하세요.

### SDK

#### SDK 주요 업데이트 {#sdk-breaking-updates}

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Flutter SDK 19.0.0](https://pub.dev/packages/braze_plugin/changelog#1900)
    - 지원되는 최소 Dart 버전은 `2.17.0`입니다.
    - SDK 로깅은 이제 Dart 레이어에서 제어됩니다.
    - [Braze Android SDK 41.1.1에서 42.2.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v41.1.1...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 Android 브리지를 포함한 네이티브 SDK 바인딩을 업데이트합니다.
    - 크래시를 수정합니다.
- [Cordova 16.0.1](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/16.0.1)
    - `SwiftDelegate` 템플릿과 함께 `cordova-ios` 8을 사용할 때 iOS 초기화 문제를 수정합니다.
- [Unity SDK 11.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Braze [Swift SDK 13.2.0에서 14.1.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 iOS 브리지를 포함한 네이티브 SDK 바인딩을 업데이트합니다.
    - [Braze Android SDK 36.0.0에서 42.2.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 Android 브리지를 업데이트합니다.
        - 필요한 최소 Android SDK 버전은 23입니다. 자세한 내용은 [Braze Android SDK 버전 정보](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)를 참조하세요.
    - 필요한 최소 Unity 버전을 Unity 6([6000.0.66f2](https://unity.com/releases/editor/whats-new/6000.0.66f2) 이상)으로 업데이트했습니다.
    - News Feed를 제거했습니다.
        - `RequestFeedRefresh()`, `RequestFeedRefreshFromCache()`, `LogFeedDisplayed()`, `LogCardImpression(string)`, `LogCardClicked(string)`을 제거했습니다.
    - 사소한 버그를 수정합니다.
- [React Native 20.1.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/20.1.0)
    - Android SDK 바인딩을 업데이트합니다.
    - 푸시 알림 딥링킹 문제를 수정합니다.
- [Segment Swift 8.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#800)
    - Braze Swift SDK 바인딩을 `14.0.0+` SemVer 디노미네이션의 릴리스가 필요하도록 업데이트합니다.
        - 이를 통해 `14.0.0`에서 `15.0.0` 미만까지의 모든 버전의 Braze SDK와 호환이 가능합니다.
        - 잠재적인 주요 변경 사항에 대한 자세한 내용은 [`14.0.0` 체인지로그 항목](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1400)을 참조하세요.
    - SDK 인증 지원을 추가합니다.

{% enddetails %}
{% details 2026년 4월 30일 %}

## 2026년 4월 30일 릴리스 {#april-30-2026-release}

### 데이터 및 보고

#### 개별 프로필 생성을 위한 빠른 사용자 추가 {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

이제 **사용자 가져오기**에서 **빠른 사용자 추가**를 선택하고 이메일 또는 외부 ID를 입력하여 개별 사용자 프로필을 생성할 수 있습니다.

이전에는 이 워크플로우에서 사용자를 생성하려면 CSV 업로드 또는 자동화된 수집 방법이 필요했습니다.

자세한 내용은 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)를 참조하세요.

#### Canvas 트리거를 위한 제로 카피 CDI 동기화 {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

CDI는 이제 제로 카피 개인화를 위한 `Canvas triggers` 데이터 유형을 지원합니다. 웨어하우스 또는 S3 데이터에서 Canvas를 트리거하고 Braze 사용자 프로필에 해당 필드를 유지하지 않고도 컨텍스트 필드를 전달할 수 있습니다.

이전에는 CDI 동기화에서 이러한 유형의 개인화 워크플로우를 위해 데이터를 Braze 프로필에 기록해야 했습니다.

자세한 내용은 [CDI를 사용한 제로 카피 개인화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/)를 참조하세요.

#### eCommerce 추천 이벤트 {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

[eCommerce 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/)는 구매 여정의 6단계를 다룹니다: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled`, `order_refunded`. 이러한 이벤트를 성공적으로 전송하면 Braze가 데이터를 검증하고 점점 늘어나는 플랫폼 기능 세트에서 사용할 수 있도록 합니다.

### 커런츠 및 데이터 공유 {#currents-and-datashare}

#### 새로운 배너 및 WhatsApp 커런츠 업데이트 {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

커런츠 및 데이터 공유에 새로운 `Banner.Dismiss` 이벤트와 기존 WhatsApp 이벤트에 대한 추가 필드가 포함되었습니다.

이전에는 이러한 배너 해제 이벤트와 WhatsApp 필드를 내보내기 데이터에서 사용할 수 없었습니다.

자세한 내용은 [커런츠 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)를 참조하세요.

### 오케스트레이션

#### 다국어 번역 {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

복잡한 코드 없이 빠른 일회성 로캘 설정으로 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)를 작성하여 모든 시장에 자신 있게 전송할 수 있습니다.

#### 세분화된 권한 마이그레이션 {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

계정에 액세스하고 특정 작업을 수행할 수 있는 사람을 관리하는 것은 보안과 운영 효율성 모두에 중요합니다. 더 많은 제어를 제공하기 위해 Braze는 계정 전반에서 사용자 액세스를 관리하는 더 유연하고 정밀한 방법인 [세분화된 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration/)을 도입합니다.

#### 대상으로 보내기 Canvas 구성요소 {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

[대상으로 보내기 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination/)를 사용하면 한 Canvas에서 다른 Canvas로 사용자를 보낼 수 있습니다. 예를 들어, 프로모션 오퍼에 대한 메시징을 공유하는 두 개의 Canvas가 있는 경우 대상으로 보내기를 사용하여 이러한 Canvas를 연결할 수 있습니다.

#### Canvas 컨텍스트 개선 사항 {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

Canvas에서 이제 컨텍스트 변수를 참조하여 다음을 설정할 수 있습니다:

- Content Cards의 제거 이벤트
- Content Cards의 만료

자세한 내용은 [카드 생성]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas)을 참조하세요.

#### 메시지 단계의 전달 유효성 검사 진행 동작 {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

[전달 유효성 검사]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations)는 메시지 전송 시 오디언스가 전달 기준을 충족하는지 확인하기 위한 추가 검사를 제공합니다. 사용자가 메시지 단계에 대해 설정된 전달 유효성 검사를 충족하지 않는 경우 **전달 유효성 검사 진행 동작** 설정을 사용하여 사용자가 다음 단계로 진행할지 Canvas를 종료할지 결정할 수 있습니다.

#### 워크스페이스 메시징 사용량 제한 {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

[워크스페이스 메시징 사용량 제한]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits/)을 사용하여 플랫폼에서 발신 메시지의 전달 속도를 조절하여 사용자가 필요한 메시지를 받을 수 있도록 합니다. 워크스페이스 메시징 사용량 제한은 점진적으로 출시되고 있으므로 대시보드에서 아직 이러한 설정이 표시되지 않을 수 있습니다.

### 채널 및 터치포인트

#### WhatsApp 템플릿 빌더 {#whatsapp-template-builder}

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp 템플릿 빌더]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/)를 사용하면 Braze에서 직접 WhatsApp 메시지 템플릿을 생성하고 제출할 수 있어 Braze와 Meta 비즈니스 매니저 사이를 전환할 필요가 없습니다. Meta가 템플릿을 승인하면 원하는 만큼 많은 캠페인과 Canvas에서 사용할 수 있습니다.

#### Shopify 제품 태그, 메타필드 및 컬렉션 {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

이제 Shopify 스토어에서 [Shopify 제품 태그, 컬렉션 및 메타필드를 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/)하여 Braze 카탈로그에 저장할 수 있습니다. 이를 통해 커스텀 해결 방법 없이 개인화, 세분화 및 카탈로그 기반 메시징을 위한 더 풍부한 제품 데이터를 제공합니다.

### 파트너십

#### GRAVITY - 데이터 및 분석 - 로열티 {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/)는 Loyalty Juggernaut Inc.(LJI)의 엔터프라이즈급 로열티 플랫폼으로, 소매, 여행, 레스토랑(퀵서비스 레스토랑 포함) 및 금융 서비스 전반의 브랜드가 차세대 프로그램을 설계, 관리 및 확장할 수 있도록 지원하여 개인화된 데이터 중심 경험을 통해 참여, 유지 및 고객 생애주기 가치에서 측정 가능한 성장을 이끌어냅니다.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

다음 SDK 업데이트가 릴리스되었습니다. 자세한 내용은 [SDK 체인지로그]({{site.baseurl}}/releases/sdk_changelogs/)를 참조하세요.

#### SDK 주요 업데이트

{% multi_lang_include release_type.md release="General availability" %}

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [React Native SDK 19.2.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.2.0)
    - 지연 초기화 지원.
- [Android SDK 42.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.0.0)
    - 인앱 메시지 및 배너 관련 버그 수정.
- [Swift SDK 14.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.1.0)
    - 배너 해제 지원.
- [Web SDK 6.7.0](https://github.com/braze-inc/braze-web-sdk/releases/tag/v6.7.0)
    - 배너 해제 지원.
- [Android SDK 42.1.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.1.0)
    - 배너 해제 지원.
- [Braze Segment Android 17.0.0](https://github.com/braze-inc/braze-segment-android/releases/tag/v17.0.0)
    - 이것은 Analytics-Android를 사용하는 Braze Segment Android 플러그인의 최종 릴리스입니다. Analytics-Android는 2026년 3월에 지원이 종료되었습니다. [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin)을 사용하는 [Braze Segment Kotlin 플러그인](https://github.com/braze-inc/braze-segment-kotlin)으로 마이그레이션하세요.
    - 네이티브 SDK 버전을 업그레이드합니다.

{% enddetails %}
{% details 2026년 4월 2일 %}

## 2026년 4월 2일 릴리스 {#april-2-2026-release}

### 데이터 및 보고

#### 커런츠 및 데이터 공유 이벤트의 새로운 배너 채널 필드 {#new-banner-channel-fields-in-currents-and-datashare-events}

Braze는 커런츠 및 데이터 공유 내보내기의 기존 배너 채널 이벤트에 필드를 추가했습니다. 이러한 이벤트 및 필드 업데이트 목록은 [버전 7의 변경 사항]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage)을 참조하세요.

#### 커런츠를 위한 Mixpanel EU 및 인도 데이터 센터 지원 {#mixpanel-eu-and-india-data-center-support-for-currents}

커런츠 Mixpanel 통합은 이제 Mixpanel의 EU 및 인도 데이터 센터를 지원합니다. Mixpanel 통합을 구성할 때 Braze가 데이터를 전송할 Mixpanel 리전을 선택할 수 있습니다. 이 업데이트는 상호 고객을 위한 Mixpanel의 성장하는 국제적 인프라를 지원합니다. 자세한 내용은 [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)을 참조하세요.

#### 재사용 가능한 클라우드 데이터 수집(CDI) 소스 및 동기화 {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

클라우드 데이터 수집(CDI)에 소스와 동기화를 분리하는 새로운 디자인이 적용되어 하나의 소스를 여러 동기화에서 재사용할 수 있습니다. 기존 동기화는 중단 시간 없이 새로운 소스 및 동기화 모델로 자동 마이그레이션됩니다. **클라우드 데이터 수집** > **소스**로 이동하여 소스를 보거나 편집하거나 생성한 다음, 동기화를 생성할 때 드롭다운에서 소스를 선택하세요. 이 변경으로 반복적인 설정이 줄어들고 향후 개선을 위한 기반이 마련됩니다. 자세한 내용은 [데이터 웨어하우스 통합 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations)을 참조하세요.

### BrazeAI<sup>TM</sup>

#### BrazeAI Operator<sup>TM</sup>에서 지원 티켓 제출 {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)에 대시보드를 떠나지 않고 Braze 지원 티켓을 제출할 수 있는 플로우가 포함되었습니다. 단계, 자동 포함 컨텍스트 및 빠른 해결을 위한 팁은 [BrazeAI Operator로 지원 티켓 제출]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/)을 참조하세요.

### 오케스트레이션

#### 다국어 번역

{% multi_lang_include release_type.md release="General availability" %}

워크스페이스에 로캘을 추가한 후 [다국어 번역]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)을 사용하여 단일 푸시, 이메일, 배너, 인앱 메시지 또는 Content Block 내에서 다양한 언어의 사용자를 타겟팅할 수 있습니다.

![로캘 미리보기]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Canvas 컨텍스트 개선 사항

{% multi_lang_include release_type.md release="General availability" %}

Canvas에서 이제 컨텍스트 변수를 참조하여 다음을 설정할 수 있습니다:

- 메시지 단계에서 배너 및 인앱 메시지의 [만료]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#set-an-expiration)
- 행동 경로 단계의 [개인화된 지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-delays)

컨텍스트 변수 이름 필드에서 컨텍스트 변수 이름을 직접 입력하거나 단계 편집기의 드롭다운에서 선택할 수도 있습니다. 자세한 내용은 [컨텍스트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/) 및 [컨텍스트 변수]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/)를 참조하세요.

### 채널 및 터치포인트

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk/)은 브로드캐스트 메시징과 사용자와의 1:1 채팅을 가능하게 하는 메시징 채널입니다. Liquid 및 기타 동적 콘텐츠를 사용하여 브랜드와의 풍부한 사용자 경험을 촉진하고 향상시키는 개인화된 사용자 경험을 만들 수 있습니다.

![KakaoTalk 리스트 아이템 메시지.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Canvas의 배너 {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Canvas [메시지 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)에서 [배너]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)를 메시징 채널로 사용할 수 있습니다. 배너를 사용하면 앱 또는 웹사이트 콘텐츠를 동적으로 개인화하여 실시간 사용자 자격 및 행동을 반영할 수 있습니다.

### 파트너십

#### CataBoom - 메시지 개인화 - 시각적 및 인터랙티브 콘텐츠 {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom/)은 게임화 플랫폼입니다. 브랜드는 이를 사용하여 스핀 투 윈 게임, 퀴즈, 즉석 당첨 게임 등 인터랙티브 디지털 경험을 구축하고 출시합니다. 이러한 경험은 참여를 심화하고 퍼스트파티 데이터를 수집합니다.

#### Denada - 메시지 오케스트레이션 - 템플릿 {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada/)는 주제 전문가가 자연스러운 대화를 통해 브랜드에 맞는 마케팅 자료를 만들 수 있게 해주는 AI 기반 마케팅 크리에이티브 플랫폼입니다. Denada를 사용하면 팀이 디자인 전문 지식 없이도 아이디어 구상에서 완성된 이메일 콘텐츠까지 진행할 수 있습니다.

#### Poq - 이커머스 - 모바일 앱 플랫폼 {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq/)는 기업이 완전한 네이티브 iOS 및 Android 앱을 신속하게 출시, 관리 및 확장할 수 있도록 지원하여 커머스를 촉진하고 브랜드 약속을 실현하는 고성능 모바일 경험을 제공합니다.

#### The Trade Desk – Canvas 오디언스 동기화 {#the-trade-desk-canvas-audience-sync}

[Braze 오디언스 동기화를 The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/)에 사용하면 Braze에서 퍼스트파티 사용자 데이터를 The Trade Desk로 직접 동적으로 동기화하여 광고 리타겟팅, 유사 모델링 및 억제에 활용할 수 있습니다.

### SDK

#### 통합 개발 환경(IDE)을 Docs MCP에 연결 {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

AI 코딩 어시스턴트를 사용하여 Context7을 통해 통합 개발 환경(IDE)을 Braze Docs MCP에 연결하여 Braze 통합 워크플로우를 가속화하세요. 이를 통해 어시스턴트가 최신 Braze 문서에 직접 액세스할 수 있어 개발 환경에서 더 정확한 SDK 가이드, 코드 예제 및 문제 해결 도움을 생성할 수 있습니다. Cursor, Claude Desktop 및 VS Code에서의 설정 단계는 [LLM으로 빌드하기]({{site.baseurl}}/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp)를 참조하세요.

#### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Cordova 15.0.0](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/15.0.0)
    - 네이티브 Android 브리지를 [Braze Android SDK 39.0.0에서 41.1.1로](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - 네이티브 iOS 브리지를 [Braze Swift SDK 13.2.0에서 14.0.1로](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - 성공 콜백과 관련된 `subscribeToInAppMessage` 문제를 수정했습니다.
- [Roku SDK 2.2.1](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.2.1)
    - 기기의 연결이 간헐적이거나 없는 상태에서 템플릿 인앱 메시지에 대한 실패한 HTTP 요청을 처리할 때 발생하는 크래시를 수정했습니다.
- [Web SDK 6.6.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#660)
    - 기본 400일에서 쿠키 기간을 구성할 수 있는 `cookieExpiryInDays` 초기화 옵션을 추가했습니다.
- [Flutter SDK 18.0.0](https://pub.dev/packages/braze_plugin/changelog#1800)
    - 지연 초기화 지원을 추가했습니다.
    - 네이티브 SDK에서 Content Cards, 배너, 기능 플래그, 인앱 메시지 또는 푸시 알림 업데이트를 전달하기 위해 네이티브 코드를 작성할 필요가 없도록 iOS 통합 프로세스를 간소화했습니다.
        - 이제 SDK는 Braze 인스턴스가 생성될 때 이러한 구독을 자동으로 설정합니다.
        - 이는 Android의 기존 동작과 일치합니다.
        - 마이그레이션하려면 `AppDelegate`에서 `braze.contentCards.subscribeToUpdates()`, `braze.banners.subscribeToUpdates()`, `braze.notifications.subscribeToUpdates`, `braze.featureFlags.subscribeToUpdates` 및 `braze.inAppMessagePresenter`에 대한 수동 호출을 제거하세요.
        - 기본적으로 인앱 메시지가 표시됩니다. 이를 재정의하려면 `BrazePlugin.configure(_:postInitialization:)`의 `postInitialization` 클로저를 사용하여 커스텀 인앱 메시지 프레젠터를 설정하세요.
- [Swift SDK 14.0.4](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1404)
    - SDK 재초기화 시 푸시 자동화 관련 버그를 수정했습니다.
    - Push Stories에서 유효하지 않은 이미지가 필터링되지 않는 문제를 수정했습니다.
- [Swift SDK 14.0.3](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1403)

{% enddetails %}

{% details 2026년 3월 5일 %}

## 2026년 3월 5일 릴리스 {#march-5-2026-release}

### 데이터 및 보고

#### 새로운 데이터 센터 {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Braze가 새로운 [데이터 센터]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/)를 출시했습니다: JP-01. Braze 계정을 설정할 때 리전별 데이터 센터에 가입할 수 있습니다.

#### 컨텍스트 변수 {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

[컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)는 특정 Canvas를 통한 사용자 여정 내에서 생성하고 사용할 수 있는 임시 데이터입니다. 사용자가 Canvas에 진입할 때마다(이전에 진입한 적이 있더라도) 컨텍스트 변수는 최신 진입 데이터와 Canvas 설정을 기반으로 재정의됩니다. 이 접근 방식을 통해 각 Canvas 진입이 자체적인 독립 컨텍스트를 유지할 수 있어 사용자가 동일한 여정 내에서 여러 활성 상태를 가지면서 각 상태에 대한 특정 컨텍스트를 유지할 수 있습니다.

#### 클라우드 데이터 수집 소스 {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

[클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze)에 소스와 동기화를 분리하는 새로운 UI가 적용되어 단일 소스를 여러 동기화에서 재사용할 수 있습니다. 이를 통해 중복 구성이 줄어들고 여러 동기화가 있을 때 설정이 간소화됩니다. 기존 동기화가 있는 경우 중단 시간 없이 새로운 소스 및 동기화 구조로 자동 마이그레이션됩니다. 시작하려면 **클라우드 데이터 수집** > **소스**로 이동하여 소스를 보거나 편집하거나 생성한 다음, 동기화를 생성할 때 드롭다운에서 소스를 선택하세요.

#### 커런츠 및 데이터 공유 이벤트의 추가 필드 {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

[커런츠 및 데이터 공유 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04)에 분석 및 다운스트림 시스템에서 사용할 수 있는 데이터를 심화하기 위해 다음과 같은 새로운 필드가 포함되었습니다:

- `agentconsole.AgentExecuted`: `error`(문자열) 추가—발생한 오류에 대한 설명.
- `agentconsole.ToolInvocation`: `request_id`(문자열) 추가—전체 LLM 요청 및 완전한 실행에 대한 고유 ID.
- `users.messages.rcs.InboundReceive`: `canvas_variation_name`(문자열) 추가—이 사용자가 받은 Canvas 변형의 이름.

#### Snowflake 데이터 공유를 위한 Campaign 및 Canvas 필드 {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake 데이터 공유]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3)에 66개의 기존 테이블에 걸쳐 Campaign 및 Canvas 정보를 반영하는 추가 필드가 포함되었습니다:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV 사전 가져오기 유효성 검사 및 오류 보고 {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

[CSV 사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/)에서 이제 사전 가져오기 유효성 검사 및 상세 오류 보고를 지원합니다. 가져오기 전에 **사용자 가져오기** 페이지에서 **가져오기 전 파일 유효성 검사**를 선택하면 Braze가 파일을 스캔하고 완전히 실패할 행(오류)과 일부 값이 건너뛰어지면서 성공할 행(경고)을 식별하는 보고서를 생성합니다. 보고서를 다운로드하고 CSV를 수정하여 다시 업로드하거나 그대로 진행할 수 있습니다. 가져오기가 완료된 후에도 실패한 행에 대한 다운로드 가능한 보고서가 제공되며, 각 문제에 대한 정확한 이유가 포함됩니다.

#### 메시징 진단 대시보드 {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="Early access" %}

[메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/)는 메시지 전송 결과에 대한 상위 수준 분석을 제공하여 메시징 설정의 트렌드를 파악하고 잠재적 문제를 진단할 수 있게 해줍니다. 이 대시보드는 캠페인이나 Canvas의 메시지가 예상대로 전송되지 않은 이유를 이해하는 데 도움이 됩니다.

### BrazeAI<sup>TM</sup>

#### 에이전트 콘솔의 Braze 에이전트 {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

[Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/)는 Braze 내에서 생성할 수 있는 AI 기반 도우미입니다. 에이전트는 콘텐츠를 생성하고, 지능적인 의사 결정을 내리고, 데이터를 보강하여 더욱 개인화된 고객 경험을 제공할 수 있습니다. 에이전트를 생성할 때 목적을 정의하고 동작 방식에 대한 가드레일을 설정합니다. 에이전트가 활성화되면 Braze에서 [배포]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)하여 개인화된 카피를 생성하거나, 실시간 의사 결정을 내리거나, 카탈로그 필드를 업데이트할 수 있습니다.

### 오케스트레이션

#### 세분화된 사용자 권한 {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze는 사용자 액세스를 관리하는 더 유연한 방법인 [세분화된 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)을 도입합니다. 레거시 권한이 세분화된 권한에 어떻게 매핑되는지를 포함한 마이그레이션 프로세스에 대해 알아보려면 [세분화된 권한으로 마이그레이션]({{site.baseurl}}/granular_permissions_migration/)을 참조하세요.

#### 채널 기반 사용량 제한 {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

멀티채널 캠페인 또는 Canvas에 대한 전달 속도 사용량 제한을 설정할 때 공유 사용량 제한 또는 [채널 기반 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases)을 설정할 수 있습니다. 멀티채널 캠페인 또는 Canvas가 채널 기반 사용량 제한을 사용하면 선택한 각 채널에 사용량 제한이 적용됩니다. 예를 들어, 캠페인 또는 Canvas에서 분당 최대 5,000개의 웹훅과 2,500개의 SMS 메시지를 전송하도록 설정할 수 있습니다.

#### Canvas 컨텍스트 단계 {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

[Canvas 컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)를 사용하면 사용자가 Canvas를 이동할 때 하나 이상의 변수를 생성하고 업데이트할 수 있습니다. 예를 들어, 시즌 할인을 관리하는 Canvas가 있는 경우 컨텍스트 변수를 사용하여 사용자가 Canvas에 진입할 때마다 다른 할인 코드를 저장할 수 있습니다.

### 채널 및 터치포인트

#### Content Blocks에서 로캘 번역 {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

워크스페이스에 로캘을 추가한 후 Content Block 내에서 [다양한 언어의 사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)할 수 있습니다.

### 파트너십

#### Algolia - 검색 추천 {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia/)는 개발자가 빠르고 관련성 높으며 확장 가능한 검색 경험을 구축할 수 있도록 돕는 검색 및 디스커버리 플랫폼입니다. 강력한 API 우선 접근 방식으로 Algolia는 고급 랭킹 알고리즘과 AI 기반 인사이트를 결합하여 원활한 사이트 검색, 내비게이션 및 개인화된 콘텐츠 디스커버리를 제공합니다.

#### Anthropic - AI 모델 제공업체 {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic/)은 다양한 언어 작업에 유용하고 정직하며 안전하도록 설계된 차세대 AI 어시스턴트 Claude를 개발하는 AI 안전 및 연구 회사입니다.

#### Canva - 메시지 개인화 - 크리에이티브 스튜디오 {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva/)는 Canva의 이미지를 Braze 미디어 라이브러리에 직접 동기화하여 크리에이티브 워크플로우를 간소화하고 모든 메시징 채널에서 시각적 자산을 최신 상태로 유지합니다.

#### DOTS.ECO - 보상 {#dotseco-rewards}

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco/)를 사용하면 추적 가능한 디지털 인증서를 통해 실제 환경에 미치는 영향에 대해 사용자에게 보상할 수 있습니다. 각 인증서에는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터가 포함될 수 있어 사용자가 자신의 영향력 증명을 보고 다시 방문할 수 있습니다.

#### Figma - 메시지 개인화 - 크리에이티브 스튜디오 {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma/)는 제품을 빌드, 디자인 및 프로토타입할 수 있는 협업 디자인 플랫폼입니다. 이 통합을 사용하여 Figma에서 Braze 미디어 라이브러리로 이미지와 시각적 자산을 직접 전송할 수 있습니다.

#### Flybuy - 메시지 개인화 - 위치 {#flybuy-message-personalization-location}

Radius Networks의 [Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy/)는 AI 기반 기술을 활용하여 픽업, 배달, 드라이브스루 및 매장 내 식사 전반에 걸쳐 서비스 속도를 최적화하는 선도적인 옴니채널 위치 플랫폼입니다. 통합 마케팅 스위트를 통해 Flybuy는 브랜드가 하이퍼 타겟팅된 순간 기반 메시지를 전달하여 참여를 유도하고 주문 금액을 늘리며 더 넓은 로열티 이니셔티브를 지원할 수 있도록 합니다.

#### Google Gemini - AI 모델 제공업체 {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini/)는 텍스트, 코드 및 이미지 전반에 걸친 고급 추론을 결합하여 브랜드가 더 스마트하고 개인화된 경험을 제공할 수 있도록 돕는 Google의 AI 모델 제품군입니다.

#### Limbik - 메시지 개인화 - 개인화 엔진 {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik/)은 AI 공명 레이어로, 실제 오디언스가 메시지, 개념 및 AI 출력을 시장에 도달하기 전에 어떻게 해석하고 반응하는지 예측합니다. 60개 이상의 국가와 25개 이상의 언어에 걸친 지속적인 1차 연구를 기반으로 Limbik은 인간이 검증한 합성 오디언스를 제공합니다. 이는 기계 속도와 연구 수준의 정확도(95% 신뢰도, 1.5%~3% 오차 범위)로 실제 오디언스 반응을 시뮬레이션하는 디지털 인구입니다. Limbik은 메시징이 타겟 오디언스가 믿고 느끼는 것과 공명하는지 즉시 확인할 수 있는 능력을 제공합니다.

#### Linkrunner - 메시지 오케스트레이션 - 기여도 {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner/)는 사용자 획득 캠페인을 추적하고 분석하는 데 도움이 되는 모바일 기여도 및 분석 플랫폼입니다.

#### Mailizio - 메시지 오케스트레이션 - 템플릿 {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio/)는 직관적인 시각적 편집기를 사용하여 재사용 가능하고 브랜드에 안전한 콘텐츠를 쉽게 디자인할 수 있는 이메일 제작 및 관리 플랫폼입니다. Mailizio를 Braze에 통합하면 콘텐츠 블록과 이메일 템플릿을 내보낸 다음 동일한 자산에서 인앱 메시지를 자동으로 생성하여 빠르고 완벽하게 제어되는 캠페인 배포를 할 수 있습니다.

#### Open Loyalty - 데이터 및 분석 - 로열티 {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty/)는 고객 로열티 및 보상 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 Open Loyalty 통합은 포인트 잔액, 등급 변경, 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 이를 통해 사용자의 로열티 상태가 변경되면 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

#### OpenAI - AI 모델 제공업체 {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai/)는 자연어 이해 및 생성을 가능하게 하는 GPT와 같은 고급 AI 모델을 만들어 브랜드가 의미 있는 고객 상호작용을 구축하고 확장할 수 있도록 지원합니다.

#### Shopgate - 채널 {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate/)는 상인이 쇼핑 앱을 만들고 풀필먼트 도구와 클라이언텔링(고객 데이터를 기반으로 한 개인화된 매장 내 고객 지원)을 통해 오프라인 매장의 효율성을 개선할 수 있도록 돕는 모바일 커머스 및 옴니채널 플랫폼입니다.

#### Splio - 데이터 및 분석 - 코호트 가져오기 {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio/)는 고객 경험을 해치지 않으면서 캠페인 수와 수익을 늘릴 수 있는 오디언스 구축 도구이며, 온라인 및 오프라인 CRM 캠페인의 성과를 추적하는 분석을 제공합니다.

### SDK

#### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Android 바인딩을 [Braze Android SDK 37.0.0에서 41.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - iOS 바인딩을 [Braze Swift SDK 13.3.0에서 14.0.1로](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - Braze Android SDK에 필요한 새로운 전이적 NuGet 종속성을 추가했습니다:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib가 2.0.21.3에서 2.3.0.1로 업데이트되었습니다. 프로젝트에서 이 패키지를 이전 버전으로 명시적으로 고정한 경우 복원 오류를 방지하기 위해 업데이트해야 합니다.
    - News Feed 기능을 제거했습니다.
        - 이 기능은 네이티브 Android SDK 버전 [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0)에서 제거되었습니다.
        - 이 기능은 네이티브 Swift SDK 버전 [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0)에서 제거되었습니다.
    - BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData 열거형 케이스가 BRZInAppMessageDismissalReason.WipeData로 이름이 변경되었습니다.
- [Expo Plugin 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - 이 버전은 Braze React Native SDK 19.0.0이 필요합니다.
    - (Android) 데이터 지속성 레이어의 메모리 누수를 수정했습니다.
    - (Android) 앱이 종료된 상태에서 실행될 때 푸시 알림 딥링크를 처리하기 위한 Braze.getInitialPushPayload() 지원을 추가했습니다. 이를 통해 앱이 콜드 스타트될 때 Android에서 푸시 알림의 딥링크가 처리되지 않는 문제가 해결됩니다.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - 네이티브 Swift SDK 버전 바인딩을 Braze Swift SDK 13.3.0에서 14.0.1로 업데이트합니다.
    - 네이티브 Android SDK 버전 바인딩을 Braze Android SDK 40.0.2에서 41.0.0으로 업데이트합니다.

{% enddetails %}

{% details 2026년 2월 5일 %}

## 2026년 2월 5일 릴리스 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### 콘텐츠 최적화 프로그램 {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

[콘텐츠 최적화 프로그램]({{site.baseurl}}/user_guide/brazeai/content_optimizer/)은 자동화된 참여 최적화를 제공하는 지속적인 고변형 콘텐츠 테스트 캔버스 단계입니다. 메시지 단계와 유사한 드래그 앤 드롭 인터페이스를 사용하여 테스트할 구성 요소를 정의하고, AI를 사용하여 변형을 생성하거나 수동으로 입력한 다음, Liquid 태그를 사용하여 이러한 구성 요소를 메시지 콘텐츠에 매핑할 수 있습니다.

비상황별 멀티암드 밴딧 옵티마이저를 기반으로 구축된 콘텐츠 최적화 프로그램은 사용자당 단일 메시지를 전송하며, 예측 추천을 기반으로 전달할 구성 요소 변형 조합을 결정합니다. 단계가 시간이 지남에 따라 데이터를 수집하면서 성능이 우수한 변형은 자연스럽게 전송 할당이 증가하고 성능이 낮은 변형은 감소합니다. 콘텐츠 최적화 프로그램은 지속적인 최적화를 위해 일일 사용자 수가 일정한(하루 최소 수천 명) 반복 전송 Canvas에서 가장 잘 작동합니다.

### 데이터 및 보고

#### eCommerce 추천 이벤트

{% multi_lang_include release_type.md release="Early access" %}

eCommerce 추천 이벤트와 기존 구매 이벤트를 일치시키기 위해 "구매하기"와 유사한 ["주문하기" 전환 이벤트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report)를 추가했습니다.

### 채널 및 터치포인트

#### 배너의 로캘 번역 {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

워크스페이스에 로캘을 추가한 후 단일 배너 내에서 [다양한 언어의 사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#translating-locales)할 수 있습니다.

#### 드래그 앤 드롭 Content Blocks의 너비 구성 {#configure-width-for-drag-and-drop-content-blocks}

탐색 메뉴에서 버튼을 선택하여 [Content Block의 너비를 조정]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/#using-the-editor-to-add-a-content-block)합니다. 이메일 글로벌 스타일 설정에서 지정하지 않은 경우 기본 너비는 100%이며, 그렇지 않은 경우 글로벌 설정이 적용됩니다.

![너비를 편집할 수 있는 양면 화살표.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### 자동화된 IP 워밍 사용 {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

[자동화된 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/#automated-ip-warming)을 사용하여 일일 전송량을 점진적으로 늘려 수신편지함 제공업체가 전송 패턴을 학습하고 신뢰할 수 있도록 합니다. Braze는 참여도가 가장 높은 가입자에게 먼저 전송하므로 일일 볼륨이 모범 사례에 맞는 속도로 증가할 수 있습니다.

### 파트너십

#### LinkedIn – Canvas 오디언스 동기화 {#linkedin-canvas-audience-sync}

[Braze 오디언스 동기화를 LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/)에 사용하면 Braze 통합의 사용자 데이터를 LinkedIn 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 게재할 수 있습니다. 일반적으로 사용자 데이터를 기반으로 Braze Canvas에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 사용했던 모든 기준을 이제 LinkedIn 고객 목록에서 해당 사용자에게 광고를 트리거할 수 있습니다.

#### Oracle CrowdTwist - 데이터 및 분석 {#oracle-crowdtwist-data-analytics}

[Oracle CrowdTwist]({{site.baseurl}}/partners/crowdtwist/)는 브랜드가 개인화된 고객 경험을 제공할 수 있도록 지원하는 선도적인 클라우드 네이티브 고객 로열티 솔루션입니다. 이 솔루션은 100개 이상의 즉시 사용 가능한 참여 경로를 제공하여 마케터가 고객에 대한 보다 완전한 시각을 개발할 수 있도록 빠른 가치 창출 시간을 제공합니다.

#### Fullstory - 동적 콘텐츠 {#fullstory-dynamic-content}

[Fullstory의]({{site.baseurl}}/partners/fullstory/) 행동 데이터 플랫폼은 기술 리더가 더 나은 정보에 기반한 의사 결정을 내릴 수 있도록 지원합니다. 디지털 행동 데이터를 분석 스택에 주입하여 Fullstory의 특허 기술은 양질의 행동 데이터를 대규모로 활용함으로써 모든 디지털 방문을 유용한 인사이트로 전환합니다.

#### Open Loyalty - 데이터 및 분석 {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty/)는 고객 로열티 및 보상 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 Open Loyalty 통합은 포인트 잔액, 등급 변경, 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 이를 통해 사용자의 로열티 상태가 변경되면 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

#### DOTS.ECO - 확장 {#dotseco-extensions}

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco)를 사용하면 추적 가능한 디지털 인증서를 통해 실제 환경에 미치는 영향에 대해 사용자에게 보상할 수 있습니다. 각 인증서에는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터가 포함될 수 있어 사용자가 자신의 영향력 증명을 보고 다시 방문할 수 있습니다.

#### Mailizio - 메시지 오케스트레이션 {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio/)는 직관적인 시각적 편집기를 사용하여 재사용 가능하고 브랜드에 안전한 콘텐츠를 쉽게 디자인할 수 있는 이메일 제작 및 관리 플랫폼입니다. Mailizio를 Braze에 통합하면 콘텐츠 블록과 이메일 템플릿을 내보낸 다음 동일한 자산에서 인앱 메시지를 자동으로 생성하여 빠르고 완벽하게 제어되는 캠페인 배포를 할 수 있습니다.

### API {#apis}

#### 미디어 라이브러리 POST API {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

이제 API를 통해 미디어 라이브러리 자산을 추가할 수 있어 고객, 파트너, 대행사가 메시지 제작 워크플로우를 더 많이 자동화할 수 있습니다. [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/)를 사용하여 자산 파일을 직접 업로드하거나 기존 URL에서 파일을 복사할 수 있습니다. 이 기능을 통해 통합 및 자동화 기능을 사용할 수 있습니다.

### 커런츠 및 데이터 공유

#### 스토리지 대상 및 데이터 공유를 위한 에이전트 콘솔 이벤트 {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

이제 스토리지 대상(AWS S3, GCS, Azure Blob Storage) 및 Snowflake 데이터 공유를 위한 두 가지 새로운 [이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)(`agentconsole.AgentExecuted` 및 `agentconsole.ToolInvocation`)를 사용할 수 있습니다. 이러한 이벤트를 통해 다운스트림 시스템에서 에이전트 콘솔 사용량과 세부 정보를 분석하여 에이전트 사용량을 이해하고 최대한 활용할 수 있습니다. 에이전트를 사용하면 Canvas 또는 카탈로그에서 콘텐츠를 생성하고 지능적인 의사 결정에 따라 사용자를 다른 경로로 라우팅하는 등 Braze 전반에서 특정 작업을 수행할 수 있는 지능형 에이전트를 만들고 배포할 수 있습니다. 자세한 내용은 [커런츠 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### 개별 채널에 대한 새로운 '재시도' 이벤트 {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

이제 이메일, LINE, 푸시 알림, SMS, 웹훅, WhatsApp 채널에 새로운 [재시도 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)를 사용할 수 있습니다. 이러한 이벤트는 최대 게재빈도 설정으로 인해 예약된 메시지가 중단되지 않고 지연되는 경우에 대한 가시성을 제공합니다. 메시지의 우선순위가 낮아지거나 게재빈도가 제한되는 경우 이제 구성된 재시도 기간 내에 재시도할 수 있어 메시지 전달 패턴과 최대 게재빈도 제한의 영향에 대해 더 나은 인사이트를 얻을 수 있습니다. 자세한 내용은 [커런츠 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### TokenStateChange 이벤트에 새로운 'time_ms' 필드 추가 {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

[`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) 이벤트에 새로운 `time_ms` 필드가 추가되어 푸시 토큰 상태 변화를 추적하기 위한 밀리초 수준의 세분성을 제공합니다. 이 향상된 정밀도는 같은 초 내에 여러 변경 사항이 발생할 때 푸시 토큰의 최신 상태를 파악하는 데 도움이 되며, 다운스트림 시스템에서 올바른 구독 상태를 유지하고 있다는 확신을 줍니다. 자세한 내용은 [커런츠 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### Tealium 대상으로 익명 사용자 보내기 {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

이제 외부 사용자 ID가 정의되지 않은 이벤트도 [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents) 대상으로 스트리밍할 수 있습니다. 커런츠 통합에서 "익명 사용자의 이벤트 포함" 확인란을 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 대상에게 전송됩니다. 이 기능은 비식별 및 익명 사용자와 관련된 다운스트림 분석 및 사용 사례에 매우 중요합니다.

##### CustomHTTP 대상으로 익명 사용자 보내기 {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

이제 외부 사용자 ID가 정의되지 않은 이벤트도 CustomHTTP 대상으로 스트리밍할 수 있습니다. 커런츠 통합에서 "익명 사용자의 이벤트 포함" 확인란을 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 대상에게 전송됩니다. 이 기능은 비식별 및 익명 사용자와 관련된 다운스트림 분석 및 사용 사례에 매우 중요합니다.

#### 이메일 열기 이벤트 — "machine_open" 필드 {#email-open-event-machine_open-field}

[이메일 열기 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#email-open-events)는 이제 "machine_open" 필드 값을 생성하여 [_머신 열기_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens) 측정기준을 보고할 수 있습니다.

### SDK

다음 SDK 업데이트가 릴리스되었습니다. Swift SDK v14.0.1에서 유니버설 링크 처리 관련 문제가 수정되었습니다. Android SDK v40.2.0은 잠재적인 메모리 누수를 수정하고 투명 활동이 있을 때 여러 세션이 열리는 문제를 해결합니다. Expo SDK v3.2.0에는 네이티브 Swift SDK의 유니버설 링크 처리를 구성할 수 있는 `forwardUniversalLinks` 옵션(기본값: false)이 추가되었습니다.

#### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - `BrazeConfig.Builder.setIsLocationCollectionEnabled()`의 이름을 `setIsAutomaticLocationCollectionEnabled()`로 변경했습니다.
    - `BrazeConfig.isLocationCollectionEnabled`의 이름을 `isAutomaticLocationCollectionEnabled`로 변경했습니다.
    - `BrazeConfigurationProvider.isLocationCollectionEnabled`의 이름을 `isAutomaticLocationCollectionEnabled`로 변경했습니다.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details 2026년 1월 8일 %}
## 2026년 1월 8일 릴리스 {#january-8-2026-release}

### 데이터 및 보고

#### 커런츠 이벤트 업데이트 {#updates-to-currents-events}

{% multi_lang_include release_type.md release="General availability" %}

버전 4에서 커런츠에 적용된 변경 사항은 다음과 같습니다:

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`의 필드 변경:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.pushnotification.Bounce`의 필드 변경:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.pushnotification.Send`의 필드 변경:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.rcs.Click`의 필드 변경:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 Canvas 변형의 이름
    * `user_phone_number` 필드는 이제 *선택* 사항입니다.
* 이벤트 유형 `users.messages.rcs.InboundReceive`의 필드 변경:
    * `user_id` 필드는 이제 *선택* 사항입니다.
* 이벤트 유형 `users.messages.rcs.Rejection`의 필드 변경:
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID

각 릴리스의 이벤트 변경 사항은 [커런츠 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)를 참조하세요.

#### 모든 행을 기준으로 동기화 로그 내보내기 {#export-sync-logs-by-all-rows}

{% multi_lang_include release_type.md release="Early access" %}

[클라우드 데이터 수집 **동기화 로그** 대시보드]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs)에서 동기화 실행에 대한 행 수준 로그를 내보내도록 선택할 수 있습니다:

* **오류가 있는 행:** **Error** 상태인 행만 포함된 파일을 다운로드합니다.
* **모든 행:** 실행 중에 처리된 모든 행이 포함된 파일을 다운로드합니다.

### 채널 및 터치포인트

#### BYO(Bring Your Own) WhatsApp 커넥터 {#bring-your-own-byo-whatsapp-connector}

[BYO(Bring Your Own) WhatsApp 커넥터]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector/)는 Braze와 Infobip 간의 파트너십을 통해 Infobip WhatsApp 비즈니스 매니저(WABA)에 대한 액세스 권한을 Braze에 부여하는 기능을 제공합니다. 이를 통해 세분화, 개인화, 캠페인 오케스트레이션을 위해 Braze를 사용하면서 Infobip으로 직접 메시징 비용을 관리하고 결제할 수 있습니다.

#### Canvas의 배너

{% multi_lang_include release_type.md release="Early access" %}

Canvas의 [메시지 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)에서 **배너**를 메시징 채널로 선택할 수 있습니다. 드래그 앤 드롭 편집기를 사용하여 개인화된 인라인 메시지를 생성하여 각 사용자 세션이 시작될 때 자동으로 업데이트되는 방해받지 않는 상황별 관련성 높은 경험을 제공할 수 있습니다.

#### 동적 BCC {#dynamic-bcc}

{% multi_lang_include release_type.md release="General availability" %}

[동적 BCC]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc)를 사용하면 BCC 주소에 Liquid를 사용할 수 있습니다. 이 기능은 **이메일 환경설정**에서만 사용할 수 있으며 캠페인 자체에서는 설정할 수 없습니다. 이메일 수신자당 하나의 BCC 주소만 허용됩니다.

#### 채널 기반 사용량 제한 {#channel-based-rate-limits}

전체 멀티채널 캠페인 또는 Canvas에서 공유되는 사용량 제한 대신 채널별로 특정 사용량 제한을 선택할 수 있습니다. 이 경우 선택한 각 채널에 사용량 제한이 적용됩니다. 예를 들어, 캠페인 또는 Canvas에서 분당 최대 5,000개의 웹훅과 2,500개의 SMS 메시지를 전송하도록 설정할 수 있습니다. 자세한 내용은 [사용량 제한 및 최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/)을 참조하세요.

### 파트너십

#### LILT - 현지화 {#lilt-localization}

[LILT]({{site.baseurl}}/partners/lilt/)는 기업용 번역 및 콘텐츠 제작을 위한 완벽한 AI 솔루션입니다. LILT는 글로벌 조직이 AI 에이전트와 완전 자동화된 워크플로우를 통해 콘텐츠, 제품, 커뮤니케이션 및 지원 운영을 확장하고 최적화할 수 있도록 지원합니다.

### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - News Feed를 제거합니다.
        - News Feed와 관련된 모든 UI 요소, 데이터 모델 및 작업이 완전히 제거됩니다.
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 2025년 12월 9일 %}

## 2025년 12월 9일 {#december-9-2025}

### 데이터 및 보고

#### 랜딩 페이지에 Google Tag Manager 추가하기 {#adding-google-tag-manager-to-a-landing-page}

랜딩 페이지에 Google Tag Manager를 추가하려면 드래그 앤 드롭 편집기에서 랜딩 페이지에 커스텀 코드 블록을 추가한 다음 블록에 [Tag Manager 코드를 삽입]({{site.baseurl}}/user_guide/messaging/landing_pages/#adding-google-tag-manager-to-a-landing-page)합니다.

### 오케스트레이션

#### SMS Liquid 사용 사례 {#sms-liquid-use-case}

[인바운드 SMS 키워드에 따라 다른 메시지로 응답]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/#sms-keyword-response) 사용 사례는 동적 SMS 키워드 처리를 통합하여 특정 인바운드 메시지에 다른 메시지 카피로 응답합니다. 예를 들어, 누군가 "START" 문자를 보낼 때와 "JOIN" 문자를 보낼 때 다른 응답을 보낼 수 있습니다.

#### 연결된 콘텐츠에 대한 허용 목록 {#allowlisting-for-connected-content}

[연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)에 사용할 특정 URL을 허용 목록에 추가할 수 있습니다. 이 기능을 이용하려면 고객 성공 매니저에게 문의하세요.

### 채널 및 터치포인트

#### SMS 문자 인코딩 {#sms-character-encoding}

[SMS 세그먼트 계산기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator)에 이제 문자 인코딩 기능이 추가되었습니다! **문자 인코딩 표시**를 선택하여 어떤 문자가 GSM-7 또는 UCS-2로 인코딩되는지 식별할 수 있습니다.

![텍스트 상자에 샘플 SMS 메시지를 입력하고 문자 인코딩이 켜져 있는 SMS 세그먼트 계산기.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### 최적화가 적용된 WhatsApp 메시지 {#whatsapp-messages-with-optimization}

WhatsApp용 MM API는 100% 전달 가능성을 제공하지 않으므로, 다른 채널에서 메시지를 받지 못한 사용자를 리타겟팅하는 방법을 이해하는 것이 중요합니다.

사용자를 리타겟팅하려면 특정 메시지를 수신하지 않은 사용자 세그먼트를 구축하는 것이 좋습니다. 이렇게 하려면 오류 코드 `131049`로 필터링하세요. 이는 WhatsApp의 사용자별 마케팅 템플릿 제한 적용으로 인해 마케팅 템플릿 메시지가 전송되지 않았음을 나타냅니다. 이 작업은 [Braze 커런츠 또는 SQL 세그먼트 확장을 사용하여]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/#retargeting-users-on-other-braze-channels) 수행할 수 있습니다.

### 파트너십

#### OtherLevels - 동적 콘텐츠 {#otherlevels-dynamic-content}

[OtherLevels]({{site.baseurl}}/partners/otherlevels/)는 제너레이티브 AI를 사용하여 스포츠 브랜드, 퍼블리셔 및 운영자가 기존 콘텐츠를 대규모의 브랜드 개인화된 비디오 및 리치 미디어 경험으로 전환함으로써 고객과 연결하는 방식을 혁신하는 경험 플랫폼입니다.

### SDK

#### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 2025년 11월 11일 %}

## 2025년 11월 11일 {#november-11-2025}

### 데이터 유연성 {#data-flexibility}

#### `Live Activities Push to Start Registered for App` 세분화 필터 {#live-activities-push-to-start-registered-for-app-segmentation-filter}

`Live Activities Push to Start Registered for App` 필터는 특정 앱에 대한 iOS 푸시 알림을 통해 라이브 활동을 시작하도록 등록되었는지 여부에 따라 사용자를 세분화합니다.

#### RFM SQL 세그먼트 확장 {#rfm-sql-segment-extension}

[RFM(최근성, 빈도, 금액) 세그먼트 확장]({{site.baseurl}}/rfm_segments/)을 생성하여 구매 습관을 측정하여 우수 사용자를 타겟팅할 수 있습니다.

RFM 분석은 각 카테고리(최근성, 빈도, 금액)별로 사용자에게 0~3점(3점이 최고점, 0점이 최저점)의 점수를 부여하여 최고의 사용자를 식별하는 마케팅 기법입니다. 최근성, 빈도 및 금전적 가치는 모두 사용자가 선택한 특정 시간 범위의 데이터를 기반으로 합니다.

#### 커스텀 속성 — 값 {#custom-attributes-values}

사용량 보고서를 볼 때 [**값** 탭]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab)을 선택하면 약 250,000명의 사용자 샘플을 기준으로 선택한 커스텀 속성의 상위 값을 볼 수 있습니다.

#### 클라우드 데이터 수집을 위한 동기화 로그 및 관측 가능성 {#sync-logs-and-observability-for-cloud-data-ingestion}

{% multi_lang_include release_type.md release="General availability" %}

클라우드 데이터 수집(CDI) [동기화 로그 대시보드]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/)를 사용하면 CDI에서 처리한 모든 데이터를 모니터링하고, 데이터가 성공적으로 동기화되었는지 확인하고, "부정확하거나" 누락된 데이터의 문제를 진단할 수 있습니다.

#### 다중 규칙 기능 플래그 롤아웃 {#multi-rule-feature-flag-rollouts}

[다중 규칙 기능 플래그 롤아웃]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts)을 사용하여 사용자를 평가하기 위한 일련의 규칙을 정의하면 정확한 세분화와 제어된 기능 릴리스가 가능합니다. 이 방법은 다양한 오디언스에게 동일한 기능을 배포하는 데 이상적입니다.

#### 드래그 앤 드롭 제품 블록을 위한 카탈로그 필드에 매핑하기 {#mapping-to-catalog-fields-for-drag-and-drop-product-blocks}

카탈로그 설정에서 **제품 블록** 토글을 선택하여 카탈로그의 [특정 필드 및 정보에 매핑]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/#catalog-setup)할 수 있습니다. 이를 통해 제품 제목, 제품 URL, 이미지 URL로 사용할 필드를 선택할 수 있습니다.

#### 커런츠에서 최대 게재빈도 설정 중단 이벤트 {#frequency-capping-abort-events-in-currents}

커런츠 사용 시 채널 중단 이벤트에서 `abort_type`을 참조할 수 있습니다. 최대 게재빈도 설정으로 인해 메시지가 중단되었음을 식별하고 중단의 원인이 된 최대 게재빈도 설정 규칙을 포함합니다. 최대 게재빈도 설정 규칙을 설정하는 데 도움이 됩니다. 특정 커런츠 이벤트에 대한 자세한 내용은 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)를 참조하세요.

### 강력한 채널 {#robust-channels}

#### 배경 행 이미지 {#background-row-images}

{% multi_lang_include release_type.md release="General availability" %}

**행 속성** 패널에서 인앱 메시지 또는 랜딩 페이지에 [배경 행 이미지를 추가]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#background-image)할 수 있습니다. **배경 이미지**를 토글한 다음 이미지 URL을 입력하거나 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)에서 이미지를 선택합니다. 마지막으로 대체 텍스트, 크기, 위치, 이미지 반복 여부를 구성하여 행 전체에 패턴을 만들 수 있습니다.

![가로 반복 패턴이 있는 피자의 행 배경 이미지.]({% image_buster /assets/img_archive/background_row.png %})

#### 미리보기 링크 복사 {#copy-preview-link}

[배너]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-5-test-your-message-optional), [이메일 커스텀 바닥글]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/#creating-your-custom-footer), [이메일 옵트인 및 탈퇴 페이지]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=custom%20footer#subscription-pages-and-footers)에서 **미리보기 링크 복사**를 사용하여 콘텐츠가 임의의 사용자에게 어떻게 보이는지 보여주는 공유 가능한 링크를 생성할 수 있습니다.

#### 최적화된 전달이 가능한 WhatsApp 메시지 {#whatsapp-messages-with-optimized-delivery}

Meta의 고급 AI 시스템을 사용하여 참여 가능성이 가장 높은 더 많은 사용자에게 마케팅 메시지를 전달하여 전달 가능성과 메시지 참여도를 크게 높일 수 있습니다.

[전달이 최적화된 WhatsApp 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/)는 기존 클라우드 API에 비해 뛰어난 성능을 제공하는 Meta의 새로운 [마케팅 메시지 라이트 API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/)를 사용하여 전송됩니다. 이 새로운 전송 파이프라인을 사용하면 메시지를 소중히 여기고 수신하고자 하는 사용자에게 더 효과적으로 도달할 수 있습니다.

#### WhatsApp Flows

WhatsApp Flow 메시지를 Braze Canvas 또는 캠페인에 통합할 때, 사용자가 Flow를 통해 제출하는 특정 정보를 캡처하여 활용하고 싶을 수 있습니다. Braze는 필요한 중첩 고객 속성(NCA) 스키마를 생성하기 위해 사용자 응답의 구조, 특히 JSON 응답의 예상 형태에 관한 추가 정보를 수신해야 합니다.

이제 [Flow 응답을 커스텀 속성으로 저장]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute)하고 테스트 전송을 완료하여 응답 구조에 대한 정보를 Braze에 제공할 수 있습니다.

#### 편집 가능한 사용자 미리보기 {#editable-user-preview}

[무작위 또는 기존 사용자의 개별 필드를 편집]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook#customizing-an-existing-user)하여 메시지 내의 동적 콘텐츠를 테스트할 수 있습니다. **편집**을 선택하여 선택한 사용자를 수정할 수 있는 커스텀 사용자로 전환합니다.

!["편집" 버튼이 있는 "사용자로 미리보기" 탭.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### AI 및 ML 자동화 {#ai-and-ml-automation}

#### BrazeAI Decisioning Studio™ Go

이제 다음 구성 문서를 참조하여 [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)와의 통합을 설정할 수 있습니다:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)

#### Braze 에이전트를 위한 새로운 기능 {#new-features-for-braze-agents}

{% multi_lang_include release_type.md release="Beta" %}

이제 [Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)를 다음과 같이 커스터마이즈할 수 있습니다:

- 에이전트가 응답할 때 준수해야 할 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/)을 적용합니다.
- 카탈로그를 참조하여 메시지를 더욱 개인화할 수 있습니다.
- [출력 형식]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format)을 제공하여 에이전트의 출력을 구조화합니다.
- 에이전트의 출력에 대한 편차 수준에 맞게 [온도]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature)를 조정합니다.

### BrazeAI Operator<sup>TM</sup>를 사용한 ChatGPT 모델 {#chatgpt-models-with-brazeai-operatortm}

{% multi_lang_include release_type.md release="Beta" %}

이러한 GPT 모델 중에서 선택하여 [Operator]({{site.baseurl}}/user_guide/brazeai/operator/)의 다양한 요청 유형에 사용할 수 있습니다:

- GPT-5 nano
- GPT-5 mini(기본값)
- GPT-5

### 새로운 Braze 파트너십 {#new-braze-partnerships}

#### StackAdapt - 광고 {#stackadapt-advertising}

[StackAdapt]({{site.baseurl}}/partners/stackadapt/)는 타겟팅된 성과 중심 광고를 제공하는 AI 기반 마케팅 플랫폼입니다. Braze의 사용자 프로필 데이터를 StackAdapt 데이터 허브에 동기화할 수 있습니다. 두 플랫폼을 연결하면 고객에 대한 통합된 뷰를 생성하고 퍼스트파티 데이터를 활성화하여 광고 성과를 개선할 수 있습니다.

#### Cloudinary - 동적 콘텐츠 {#cloudinary-dynamic-content}

[Cloudinary]({{site.baseurl}}/partners/cloudinary/)는 채널과 고객 여정에 걸쳐 모든 캠페인에 이미지와 비디오를 대규모로 관리, 편집, 최적화 및 전달할 수 있도록 지원하는 이미지 및 비디오 플랫폼입니다. 통합 및 활성화가 완료되면 Cloudinary의 미디어 관리가 Braze 캠페인과 Canvas에 동적, 상황별, 개인화된 자산을 전달할 수 있습니다.

#### Kameleoon - A/B 테스트 {#kameleoon-ab-testing}

[Kameleoon]({{site.baseurl}}/partners/kameleoon/)은 하나의 통합 플랫폼에서 실험, AI 기반 개인화 및 기능 관리 기능을 갖춘 최적화 솔루션입니다.

### SDK 업데이트 {#sdk-updates}

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - `subscribeToInAppMessage` 및 `addListener`의 콜백에 대한 Typescript 유형을 `Braze.Events.IN_APP_MESSAGE_RECEIVED`로 수정했습니다.
        - 이제 이러한 리스너는 새로운 `InAppMessageEvent` 유형의 콜백을 올바르게 반환합니다. 이전에는 메서드에 `BrazeInAppMessage` 유형을 반환하도록 주석이 달렸지만 실제로는 `String`을 반환했습니다.
         - 두 가지 구독 API 중 하나를 사용하는 경우 이 버전으로 업데이트한 후 인앱 메시지의 동작이 변경되지 않았는지 확인하세요. `BrazeProject.tsx`에서 샘플 코드를 확인하세요.
    - 이제 API `logInAppMessageClicked`, `logInAppMessageImpression`, `logInAppMessageButtonClicked`는 기존 공개 인터페이스와 일치하도록 `BrazeInAppMessage` 객체만 허용합니다.
        - 이전에는 `BrazeInAppMessage` 객체와 `String`을 모두 허용했습니다.
    - `BrazeInAppMessage.toString()`은 이제 JSON 문자열 표현 대신 사람이 읽을 수 있는 문자열을 반환합니다.
        - 인앱 메시지의 JSON 문자열 표현을 얻으려면 `BrazeInAppMessage.inAppMessageJsonString`을 사용합니다.
    - iOS에서 `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]`가 `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`로 이동되었습니다.
        - 이 새로운 메서드는 이제 인스턴스 메서드가 아닌 클래스 메서드입니다.
    - `BrazeReactUtils` 메서드에 null 가능성 어노테이션을 추가합니다.
    - API에서 더 이상 사용되지 않는 다음 메서드와 속성을 제거합니다:
        - `getInstallTrackingId(callback:)` → `getDeviceId` 사용.
        - `registerAndroidPushToken(token:)` → `registerPushToken` 사용.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` → `setAdTrackingEnabled` 사용.
        - `PushNotificationEvent.push_event_type` → `payload_type` 사용.
        - `PushNotificationEvent.deeplink` → `url` 사용.
        - `PushNotificationEvent.content_text` → `body` 사용.
        - `PushNotificationEvent.raw_android_push_data` → `android` 사용.
        - `PushNotificationEvent.kvp_data` → `braze_properties` 사용.
    - 네이티브 Android SDK 버전 바인딩을 [Braze Android SDK 39.0.0에서 40.0.2로](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [.NET MAUI (Xamarin) SDK 버전 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - iOS 바인딩을 [Braze Swift SDK 12.1.0에서 13.3.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다. 여기에는 Xcode 26 지원이 포함됩니다.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - 네이티브 Android 브리지를 [Braze Android SDK 39.0.0에서 40.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}