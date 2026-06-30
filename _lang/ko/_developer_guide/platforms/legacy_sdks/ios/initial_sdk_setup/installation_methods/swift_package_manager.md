---
nav_title: 스위프트 패키지 매니저
article_title: iOS용 스위프트 패키지 매니저 통합
platform: iOS
page_order: 3
description: "이 튜토리얼에서는 iOS용 스위프트 패키지 매니저를 사용하여 Braze SDK를 설치하는 방법을 다룹니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 스위프트 패키지 매니저 통합 {#swift-package-manager-integration}

[스위프트 패키지 매니저](https://swift.org/package-manager/)(SPM)를 통해 iOS SDK를 설치하면 대부분의 설치 프로세스가 자동화됩니다. 이 프로세스를 시작하기 전에 Xcode 12 이상을 사용하고 있는지 확인하세요.

{% alert note %}
tvOS는 현재 스위프트 패키지 매니저를 통해 사용할 수 없습니다.
{% endalert %}

## 1단계: 프로젝트에 종속성 추가하기 {#step-1-adding-the-dependency-to-your-project}

### SDK 버전 가져오기 {#import-sdk-version}

프로젝트를 열고 프로젝트 설정으로 이동합니다. **Swift Packages** 탭을 선택하고 패키지 목록 아래에 있는 <i class="fas fa-plus" aria-label="추가"></i> 추가 버튼을 클릭합니다.

![Swift Packages 탭이 선택된 Xcode 프로젝트 설정.]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

SDK 버전 `3.33.1` 이상을 가져올 때 텍스트 필드에 iOS SDK 리포지토리의 URL(`https://github.com/braze-inc/braze-ios-sdk`)을 입력하고 **Next**를 클릭합니다.

버전 `3.29.0`~`3.32.0`의 경우 URL `https://github.com/Appboy/Appboy-ios-sdk`를 사용합니다.

![Braze iOS SDK 리포지토리 URL을 입력하는 Xcode 패키지 종속성 추가 대화 상자.]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

다음 화면에서 SDK 버전을 선택하고 **Next**를 클릭합니다. 버전 `3.29.0` 이상은 스위프트 패키지 매니저와 호환됩니다.

![Braze iOS SDK의 Xcode 패키지 버전 선택 화면.]({% image_buster /assets/img/ios/spm/select_version.png %})

### 패키지 선택 {#select-packages}

요구 사항에 가장 적합한 패키지를 선택하고 **Finish**를 클릭합니다. `AppboyKit` 또는 `AppboyUI` 중 하나를 선택해야 합니다. 두 패키지를 모두 포함하면 원치 않는 동작이 발생할 수 있습니다:

- `AppboyUI`
  - Braze에서 제공하는 UI 구성요소를 사용하려는 경우에 가장 적합합니다.
  - `AppboyKit`를 자동으로 포함합니다.
- `AppboyKit`
  - Braze에서 제공하는 UI 구성요소(예: Content Cards, 인앱 메시지 등)를 사용할 필요가 없는 경우에 가장 적합합니다.
- `AppboyPushStory`
  - 앱에 Push Stories를 통합한 경우 이 패키지를 포함하세요. 버전 `3.31.0`부터 지원됩니다.
  - **Add to Target** 아래의 드롭다운에서 기본 앱의 타겟 대신 `ContentExtension` 타겟을 선택합니다.

![Braze SDK 라이브러리 타겟을 선택하는 Xcode 패키지 추가 화면.]({% image_buster /assets/img/ios/spm/add_package.png %})

## 2단계: 프로젝트 구성 {#step-2-configuring-your-project}

그런 다음, 프로젝트 **빌드 설정**으로 이동하고 **Other Linker Flags** 설정에 `-ObjC` 플래그를 추가합니다. SDK를 추가로 통합하려면 이 플래그를 추가하고 모든 [오류](https://developer.apple.com/library/archive/qa/qa1490/_index.html)를 해결해야 합니다.

![Other Linker Flags 필드가 표시된 Xcode 빌드 설정.]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
`-ObjC` 플래그를 추가하지 않으면 API의 일부가 누락되고 동작이 정의되지 않을 수 있습니다. "unrecognized selector sent to class", 애플리케이션 충돌 및 기타 문제와 같은 예기치 않은 오류가 발생할 수 있습니다.
{% endalert %}

## 3단계: 타겟의 스키마 편집 {#step-3-editing-the-targets-scheme}
{% alert important %}
Xcode 12.5 이상을 사용하는 경우 이 단계를 건너뛰세요.
{% endalert %}

Xcode 12.4 이하 버전을 사용하는 경우 Appboy 패키지를 포함한 타겟의 스키마를 편집합니다(**Product > Scheme > Edit Scheme** 메뉴 항목):
1. **Build** 메뉴를 확장하고 **Post-actions**를 선택합니다. 더하기(+) 버튼을 누르고 **New Run Script Action**을 선택합니다.
2. **Provide build settings from** 드롭다운에서 앱의 타겟을 선택합니다.
3.  이 스크립트를 열린 필드에 복사합니다:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![실행 스크립트 빌드 단계를 추가하는 Xcode Build Phases 메뉴.]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## 다음 단계 {#next-steps}

[통합 완료하기]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration) 지침을 따르세요.