---
nav_title: 매뉴얼
article_title: iOS용 수동 통합 옵션
platform: iOS
page_order: 4
description: "이 참조 문서에서는 iOS용 Braze SDK를 수동으로 통합하는 방법을 보여줍니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 수동 통합 {#manual-integration}

{% alert tip %}
SDK를 [스위프트 패키지 매니저]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods), 또는 [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration)와 같은 패키지 매니저를 통해 구현할 것을 강력히 권장합니다. 그러면 많은 시간을 절감하고 프로세스의 많은 부분을 자동화할 수 있습니다. 그러나 그렇게 할 수 없는 경우 지침을 따라 통합을 수동으로 완료할 수 있습니다.
{% endalert %}

## 1단계: Braze SDK 다운로드 {#step-1-downloading-the-braze-sdk}

### 옵션 1: 동적 XCFramework {#option-1-dynamic-xcframework}

1. `Appboy_iOS_SDK.xcframework.zip`을 [릴리스 페이지](https://github.com/appboy/appboy-ios-sdk/releases)에서 다운로드하여 파일을 추출합니다.
2. Xcode에서 이 `.xcframework`를 프로젝트에 드래그 앤 드롭합니다.
3. 프로젝트의 **General** 탭에서 `Appboy_iOS_SDK.xcframework`에 대해 **Embed & Sign**을 선택합니다.

### 옵션 2: 정적 통합을 위한 정적 XCFramework {#option-2-static-xcframework-for-static-integration}

1. `Appboy_iOS_SDK.zip`을 [릴리스 페이지](https://github.com/appboy/appboy-ios-sdk/releases)에서 다운로드합니다.<br><br>
2. Xcode의 프로젝트 탐색기에서 Braze의 대상 프로젝트 또는 그룹을 선택합니다.<br><br>
3. **File > Add Files > Project_Name**으로 이동합니다.<br><br>
4. `AppboyKit` 및 `AppboyUI` 폴더를 그룹으로 프로젝트에 추가합니다.
	- 처음 통합하는 경우 **Copy items into destination group's folder** 옵션이 선택되어 있는지 확인합니다. 파일 선택기에서 **Options**를 확장하여 **Copy items if needed** 및 **Create groups**를 선택합니다.
	- `AppboyKit/include` 및 `AppboyUI/include` 디렉터리를 삭제합니다.<br><br>
5. (선택 사항) 다음 중 하나에 해당하는 경우:
  - SDK의 핵심 분석 기능만 원하고 UI 기능(예: 인앱 메시지 또는 Content Cards)은 사용하지 않는 경우.
  - Braze UI 기능에 대한 커스텀 UI를 가지고 있으며 이미지 다운로드를 직접 처리하는 경우.<br><br>`ABKSDWebImageProxy.m` 및 `Appboy.bundle` 파일을 제거하여 SDK의 핵심 버전을 사용할 수 있습니다. 이렇게 하면 `SDWebImage` 프레임워크 종속성과 모든 UI 관련 리소스(예: Nib 파일, 이미지, 현지화 파일)가 SDK에서 제거됩니다.

{% alert warning %}
SDK의 핵심 버전을 Braze UI 기능 없이 사용하려고 하면 인앱 메시지가 표시되지 않습니다. 핵심 버전에서 Braze Content Cards UI를 표시하려고 하면 예측할 수 없는 동작이 발생합니다.
{% endalert %}

## 2단계: 필수 iOS 라이브러리 추가 {#step-2-adding-required-ios-libraries}

1. 왼쪽 탐색을 사용하여 프로젝트의 타겟을 클릭하고 **Build Phases** 탭을 선택합니다.<br><br>
2. **Link Binary With Libraries** 아래의 <i class="fas fa-plus" aria-label="추가"></i> 버튼을 클릭합니다.<br><br>
3. 메뉴에서 `SystemConfiguration.framework`를 선택합니다.<br><br>
4. `SystemConfiguration.framework` 옆의 풀다운 메뉴를 사용하여 이 라이브러리를 필수로 표시합니다.<br><br>
5. 다음 필수 프레임워크를 프로젝트에 추가하고 각각을 "필수"로 표시합니다.
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. 다음 프레임워크를 추가하고 선택 사항으로 표시합니다:
	- `CoreTelephony.framework`<br><br>
7. **Build Settings** 탭을 선택합니다. **Linking** 섹션에서 **Other Linker Flags** 설정을 찾아 `-ObjC` 플래그를 추가합니다.<br><br>
8. `SDWebImage` 프레임워크는 Content Cards 및 인앱 메시징이 제대로 작동하는 데 필요합니다. `SDWebImage`는 GIF를 포함하여 이미지를 다운로드하고 표시하는 데 사용됩니다. Content Cards 또는 인앱 메시지를 사용하려면 SDWebImage 통합 단계를 따르세요.

### SDWebImage 통합 {#sdwebimage-integration}

`SDWebImage`를 설치하려면 해당 [지침](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework)을 따른 다음 결과로 생성된 `XCFramework`를 프로젝트에 드래그 앤 드롭합니다.

### 선택적 위치 추적 {#optional-location-tracking}

1. `CoreLocation.framework`를 추가하여 위치 추적을 활성화합니다.
2. 앱에서 `CLLocationManager`를 사용하여 사용자의 위치를 승인해야 합니다.

## 3단계: Objective-C 브리징 헤더 {#step-3-objective-c-bridging-header}

{% alert note %}
프로젝트에서 Objective-C만 사용하는 경우 이 단계를 건너뛰세요.
{% endalert %}

프로젝트에서 Swift를 사용하는 경우 브리징 헤더 파일이 필요합니다.

브리징 헤더 파일이 없는 경우 **File > New > File > (iOS or OS X) > Source > Header File**을 선택하여 `your-product-module-name-Bridging-Header.h`라는 이름으로 새로 만듭니다. 그런 다음 브리징 헤더 파일의 맨 위에 다음 코드 줄을 추가합니다:
```
#import "AppboyKit.h"
```

프로젝트의 **Build Settings**에서 헤더 파일의 상대 경로를 `Swift Compiler - Code Generation` 아래의 `Objective-C Bridging Header` 빌드 설정에 추가합니다.

## 다음 단계 {#next-steps}

[통합 완료]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration) 지침을 따르세요.