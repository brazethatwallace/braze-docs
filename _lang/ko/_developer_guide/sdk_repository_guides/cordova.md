---
nav_title: Cordova SDK
article_title: Cordova SDK 리포지토리 가이드
page_order: 5
description: "GitHub에서 미러링된 Braze Cordova SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Cordova SDK 소개 {#about-the-braze-cordova-sdk}

Braze Cordova SDK는 Braze 메시징, 분석 및 사용자 참여 기능을 애플리케이션에 통합하는 데 도움을 줍니다.

시작하려면 다음 리소스를 참조하세요.

- [Braze 사용자 가이드]({{site.baseurl}}/user_guide/introduction/)
- [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=cordova)

## 최소 버전 요구 사항 {#minimum-version-requirements}

| Braze 플러그인 | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="최소 버전 요구 사항" }

이 SDK는 기본 Braze 네이티브 SDK의 요구 사항도 상속합니다. 아래 목록도 반드시 준수하세요.
* [Android SDK 요구 사항](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [Swift SDK 요구 사항](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## SDK 설치 {#installing-the-sdk}
{% alert warning %}
아래 방법으로만 Braze Cordova SDK를 추가하세요. 다른 방법으로 설치를 시도하면 보안 위반이 발생할 수 있습니다.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## 샘플 애플리케이션 실행 {#running-the-sample-application}
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk)를 참조하세요.