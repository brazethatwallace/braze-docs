---
nav_title: Flutter SDK
article_title: Flutter SDK 리포지토리 가이드
page_order: 6
description: "GitHub에서 미러링된 Braze Flutter SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Flutter SDK 소개 {#about-the-braze-flutter-sdk}

Braze Flutter SDK는 Braze 메시징, 분석 및 사용자 참여 기능을 애플리케이션에 통합하는 데 도움을 줍니다.

시작하려면 다음 리소스를 참조하세요:

- [Braze 사용자 가이드]({{site.baseurl}}/user_guide/introduction/)
- [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=flutter)

## 빠른 시작 {#quickstart}

``` bash
flutter pub add braze_plugin
```

### Android

``` xml
<!-- android/res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### iOS

``` swift
// AppDelegate.swift
import BrazeKit
import braze_plugin

class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
  ) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
      apiKey: "<BRAZE_API_KEY>",
      endpoint: "<BRAZE_ENDPOINT>"
    )
    // - Enable logging or customize configuration here
    configuration.logger.level = .info
    let braze = BrazePlugin.initBraze(configuration)
    AppDelegate.braze = braze

    return true
  }
}
```

### Dart

``` dart
import 'package:braze_plugin/braze_plugin.dart';

// ...
_braze = new BrazePlugin();

// ...
_braze.changeUser("Jane Doe");
```

고급 통합 옵션은 [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=flutter)를 참조하세요.

## 버전 지원 {#version-support}

| 도구                                                         | 최소 지원 버전            |
| :----------------------------------------------------------- | :------------------------ |
| Dart                                                         | 2.17.0+                   |
| Flutter (CocoaPods를 통한 통합)                               | 1.10.0+                   |
| Flutter (CocoaPods 또는 스위프트 패키지 매니저를 통한 통합)     | 3.24.0+                   |
| iOS 배포 타겟                                                 | 12.0+                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="버전 지원" }

이 SDK는 기본 Braze 네이티브 SDK의 요구 사항도 상속합니다. [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) 및 [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk)에 정의된 버전 지원 정보도 반드시 준수하세요.

## 샘플 앱 {#sample-app}

[`/example`](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) 폴더에는 이 패키지의 API를 통합하고 사용하는 방법을 보여주는 샘플 앱이 포함되어 있습니다.

## 문의 {#contact}

질문이 있으시면 [support@braze.com](mailto:support@braze.com)으로 연락해 주세요.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-flutter-sdk](https://github.com/braze-inc/braze-flutter-sdk)를 참조하세요.