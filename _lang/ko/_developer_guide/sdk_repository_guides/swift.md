---
nav_title: Swift SDK
article_title: Swift SDK 리포지토리 가이드
page_order: 3
description: "GitHub에서 미러링된 Braze Swift SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Swift SDK 소개 {#about-the-braze-swift-sdk}

Braze Swift SDK는 Braze 메시징, 분석 및 사용자 참여 기능을 애플리케이션에 통합하는 데 도움을 줍니다.

시작하려면 다음 리소스를 참조하세요:

- [Braze 사용자 가이드](https://www.braze.com/docs/user_guide/introduction/)
- [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)

## 빠른 시작 {#quickstart}

``` swift
// AppDelegate.swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  // ...
  static var braze: Braze? = nil

  // ...
   func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // ...
        let configuration = Braze.Configuration(
            apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
            endpoint: "YOUR-BRAZE-ENDPOINT"
        )
        let braze = Braze(configuration: configuration)

        AppDelegate.braze = braze
        // ...
    }
}
```

``` swift
AppDelegate.braze?.changeUser(userId: "Jane Doe")
```

고급 통합 옵션은 [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)를 참조하세요.

## 버전 지원 {#version-support}

도구 | 최소 지원 버전
:----|:----
iOS|12.0+
Mac Catalyst|16.0+
tvOS|12.0+
visionOS|1.0+
Xcode|26.0+ (17A324)

## 패키지 매니저 {#package-managers}
- 스위프트 패키지 매니저
- CocoaPods

## 라이브러리 {#libraries}

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                             | iOS |     tvOS      | macCatalyst |   visionOS    |
|-----------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _[분석] 및 [푸시 알림]을 지원하는 메인 SDK 라이브러리._                            |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _[In-App Messages] 및 [Content Cards]를 위한 Braze 제공 사용자 인터페이스 라이브러리._                         |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _[위치 분석 및 지오펜스 모니터링]을 지원하는 위치 라이브러리._               |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _[리치 푸시 알림]을 지원하는 알림 서비스 확장 라이브러리._  |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _[Push Stories]를 지원하는 알림 콘텐츠 확장 라이브러리._                      |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="라이브러리" }

<sup>1</sup> _tvOS에서는 푸시 알림이 지원되지 않습니다_<br/>
<sup>2</sup> _tvOS 및 visionOS에서는 지오펜스 모니터링이 지원되지 않습니다_

[분석]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[푸시 알림]: https://www.braze.com/docs/user_guide/message_building_by_channel/push
[In-App Messages]: https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards
[위치 분석 및 지오펜스 모니터링]: https://www.braze.com/docs/user_guide/engagement_tools/locations_and_geofences
[리치 푸시 알림]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## 예제 {#examples}

여러 기능의 통합을 보여주는 [예제 프로젝트](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples)를 살펴보세요.

## 대체 리포지토리 {#alternative-repositories}

| 배리언트                               |                                     리포지토리 | GH 이슈, SDK 정보 |
|---------------------------------------|-----------------------------------------------:|--------------------:|
| → **소스 및 정적 XCFrameworks** |                    [braze-inc/braze-swift-sdk] |                   ✓ |
| 정적 XCFrameworks                   |    [braze-inc/braze-swift-sdk-prebuilt-static] |                   ✗ |
| 동적 XCFrameworks                  |   [braze-inc/braze-swift-sdk-prebuilt-dynamic] |                   ✗ |
| 병합 가능 XCFrameworks (얼리 액세스) | [braze-inc/braze-swift-sdk-prebuilt-mergeable] |                   ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="대체 리포지토리" }

## 연락처 {#contact}

질문이 있으시면 [support@braze.com](mailto:support@braze.com)으로 문의해 주세요.

[braze-inc/braze-swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-sdk-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-sdk-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-sdk-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk)를 참조하세요.