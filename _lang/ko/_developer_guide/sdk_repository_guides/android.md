---
nav_title: Android SDK
article_title: Android SDK 리포지토리 가이드
page_order: 2
description: "GitHub에서 미러링된 Braze Android SDK README 참조 문서입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
# Android SDK 리포지토리 가이드 {#android-sdk-repository-guide}

## Braze Android SDK 소개 {#about-the-braze-android-sdk}

Braze Android SDK는 Braze 메시징, 분석 및 사용자 참여 기능을 애플리케이션에 통합하는 데 도움을 줍니다.

시작하려면 다음 리소스를 참조하세요:

- [Braze 사용자 가이드](https://www.braze.com/docs/user_guide/introduction/)
- [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android)

## 빠른 시작 {#quickstart}

다음 스니펫은 Braze Android SDK를 앱에 추가하는 데 필요한 최소 구성을 보여줍니다.

``` groovy
// build.gradle

// ...
repositories {
  mavenCentral()
}
// ...
dependencies {
  `implementation 'com.braze:android-sdk-ui:42.3.+'`
  `implementation 'com.braze:android-sdk-location:42.3.+'`
}
// ...
```

``` xml
<!-- res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` kotlin
Braze.getInstance(context).changeUser("Jane Doe");
```

고급 통합 옵션에 대한 자세한 내용은 [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android)를 참조하세요.

## 버전 지원 {#version-support}

{% alert important %}
Braze Android SDK는 `minSdkVersion`을 API 21+로 선언하여 SDK가 API 21 이상을 지원하는 앱에 컴파일될 수 있도록 합니다. SDK가 해당 버전에 대해 컴파일되지만, Braze는 API 25 미만의 버전에 대해 공식 지원을 제공하지 않으며, 해당 버전을 실행하는 기기에서 SDK가 의도한 대로 작동하지 않을 수 있습니다.

앱이 해당 버전을 지원하는 경우 다음을 수행하세요:

- 해당 API 버전에 대해 SDK 통합이 물리적 기기(에뮬레이터가 아닌)에서 의도한 대로 작동하는지 검증합니다.
- 예상 동작을 검증할 수 없는 경우, 해당 버전에서 [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html)를 호출하거나 SDK 초기화를 건너뛰어야 합니다. 그렇지 않으면 사용자 기기에서 의도하지 않은 부작용이나 성능 저하가 발생할 수 있습니다.
{% endalert %}
다음 표는 Braze Android SDK에서 사용하는 도구의 최소 지원 버전을 나열합니다.

도구 | 최소 지원 버전
:----|:----
minSdk|5.0+ / API 21+ (Lollipop 이상)
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|24.1.2
Font Awesome|4.3.0

## 모듈 {#modules}

다음 표는 Braze Android SDK의 각 모듈을 설명합니다.

모듈 | 설명
:----|:----
`android-sdk-base`|Braze SDK 기본 분석 라이브러리입니다.
`android-sdk-ui`|인앱 메시지, 푸시, Content Cards 및 배너를 위한 Braze SDK 사용자 인터페이스 라이브러리입니다.
`android-sdk-location`|위치 및 지오펜스를 위한 Braze SDK 위치 라이브러리입니다.
`android-sdk-jetpack-compose`|Jetpack Compose 지원을 위한 Braze SDK 라이브러리입니다.
`droidboy`|Braze를 심층적으로 사용하는 방법을 보여주는 샘플 앱입니다.
`android-sdk-unity`|Unity에서 Braze SDK 통합을 가능하게 하는 라이브러리입니다.
`samples`|다양한 통합 옵션을 위한 샘플 앱이 포함된 폴더입니다.

## 연락처 {#contact}

질문이 있으시면 Braze 기술 고객지원에 문의하세요.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk)를 참조하세요.