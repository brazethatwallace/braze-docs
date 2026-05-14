---
nav_title: 기타 SDK 커스터마이징
article_title: iOS용 기타 SDK 커스터마이징
platform: iOS
description: "이 참조 문서에서는 로그 수준, IDFA 수집 및 기타 커스터마이징과 같은 SDK 커스터마이징을 다룹니다."
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 기타 SDK 커스터마이징 {#other-sdk-customizations}

## Braze 로그 수준 {#braze-log-level}

Braze iOS SDK의 기본 로그 수준은 최소, 즉 다음 차트에서 `8`입니다. 이 수준은 대부분의 로깅을 억제하여 프로덕션 출시 애플리케이션에서 민감한 정보가 기록되지 않도록 합니다.

사용 가능한 로그 수준은 다음 목록을 참조하세요:

### 로그 수준 {#log-levels}

| 수준    | 설명 |
|----------|-------------|
| 0        | 상세. 모든 로그 정보가 iOS 콘솔에 기록됩니다.  |
| 1        | 디버그. 디버그 및 상위 로그 정보가 iOS 콘솔에 기록됩니다.  |
| 2        | 경고. 경고 및 상위 로그 정보가 iOS 콘솔에 기록됩니다.  |
| 4        | 오류. 오류 및 상위 로그 정보가 iOS 콘솔에 기록됩니다.  |
| 8        | 최소. 최소한의 정보가 iOS 콘솔에 기록됩니다. SDK의 기본 설정입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Log levels" }

### 상세 로깅 {#verbose-logging}

로그 수준을 사용 가능한 값으로 구성할 수 있습니다. 그러나 로그 수준을 상세 또는 `0`으로 설정하면 통합 문제를 디버깅하는 데 매우 유용할 수 있습니다. 이 수준은 개발 환경에서만 사용하도록 되어 있으며 출시된 애플리케이션에서는 설정하지 않아야 합니다. 상세 로깅은 Braze에 추가 또는 새로운 사용자 정보를 전송하지 않습니다.

### 로그 수준 설정 {#setting-log-level}

로그 수준은 컴파일 시 또는 런타임 시에 할당할 수 있습니다:

{% tabs local %}
{% tab 컴파일 시 %}

`Info.plist` 파일에 `Braze`라는 사전을 추가합니다. `Braze` 사전 내에서 `LogLevel` 문자열 하위 항목을 추가하고 값을 `0`으로 설정합니다.

{% alert note %}
Braze iOS SDK v4.0.2 이전 버전에서는 `Braze` 대신 `Appboy` 사전 키를 사용해야 합니다.
{% endalert %}

`Info.plist` 콘텐츠 예시:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab 런타임 %}

`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달되는 `appboyOptions` 매개변수 내에 `ABKLogLevelKey`를 추가합니다. 값을 정수 `0`으로 설정합니다.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
로그 수준은 Braze iOS SDK v4.4.0 이상에서만 런타임에 설정할 수 있습니다. 이전 버전의 SDK를 사용하는 경우 컴파일 시점에 로그 수준을 설정하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

## 선택적 IDFV 수집 - Swift {#optional-idfv-collection-swift}

이전 버전의 Braze iOS Swift SDK에서는 IDFV(공급업체 식별자) 필드가 사용자의 기기 ID로 자동 수집되었습니다.

Swift SDK v5.7.0부터 IDFV 필드를 선택적으로 비활성화할 수 있으며, 대신 Braze가 임의의 UUID를 기기 ID로 설정합니다. 자세한 내용은 [IDFV 수집]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)을 참조하세요.

## 선택적 IDFA 수집 {#optional-idfa-collection}

IDFA 수집은 Braze SDK 내에서 선택 사항이며 기본적으로 비활성화되어 있습니다. IDFA 수집은 Braze 내에서 [설치 경로 통합]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/)을 사용하려는 경우에만 필요합니다. IDFA를 저장하기로 선택하면 무료로 저장해 드리므로, 추가 개발 작업 없이 출시 즉시 이러한 옵션을 활용할 수 있습니다.

따라서 다음 기준 중 하나라도 충족하는 경우 IDFA를 계속 수집하는 것이 좋습니다:

- 이전에 게재된 광고에 앱 설치를 기여하는 경우
- 이전에 게재된 광고에 애플리케이션 내 동작을 기여하는 경우

### iOS 14.5 AppTrackingTransparency

Apple은 IDFA를 수집하기 위해 사용자가 권한 프롬프트를 통해 옵트인하도록 요구합니다.

IDFA를 수집하려면 `ABKIDFADelegate` 프로토콜을 구현하는 것 외에도, 앱 추적 투명성 프레임워크에서 Apple의 `ATTrackingManager`를 사용하여 사용자에게 승인을 요청해야 합니다. 자세한 내용은 Apple의 [사용자 개인정보 보호 문서](https://developer.apple.com/app-store/user-privacy-and-data-use/)를 참조하세요.

앱 추적 투명성 승인 프롬프트에는 식별자 사용을 설명하기 위한 `Info.plist` 항목이 필요합니다:

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### IDFA 수집 구현 {#implementing-idfa-collection}

다음 단계를 따라 IDFA 수집을 구현합니다:

##### 1단계: ABKIDFADelegate 구현 {#step-1-implement-abkidfadelegate}

[`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h) 프로토콜을 준수하는 클래스를 생성합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### 2단계: Braze 초기화 중 델리게이트 설정 {#step-2-set-the-delegate-during-braze-initialization}

`startWithApiKey:inApplication:withAppboyOptions:`에 전달되는 `appboyOptions` 사전에서 `ABKIDFADelegateKey` 키를 `ABKIDFADelegate`를 준수하는 클래스의 인스턴스로 설정합니다.

## 대략적인 iOS SDK 크기 {#ios-sdk-size}

대략적인 iOS SDK 프레임워크 파일 크기는 30&nbsp;MB이며, 대략적인 .ipa(앱 파일에 추가) 크기는 1&nbsp;MB에서 2&nbsp;MB 사이입니다.

Braze는 Apple의 [앱 크기에 대한 권장 사항](https://developer.apple.com/library/content/qa/qa1795/_index.html)에 따라 `.ipa` 크기에 대한 SDK의 영향을 관찰하여 iOS SDK의 크기를 측정합니다. 애플리케이션에 대한 iOS SDK 크기 추가를 계산하는 경우, Braze iOS SDK를 통합하기 전후의 `.ipa` 크기 차이를 비교하기 위해 [앱 크기 보고서 가져오기](https://developer.apple.com/library/content/qa/qa1795/_index.html)를 따르는 것이 좋습니다. 앱 씨닝 크기 보고서에서 크기를 비교할 때, 씨닝된 `.ipa` 파일의 앱 크기도 확인하는 것이 좋습니다. 유니버설 `.ipa` 파일은 App Store에서 다운로드하여 사용자 기기에 설치되는 바이너리보다 크기가 크기 때문입니다.

{% alert note %}
`use_frameworks!`와 함께 CocoaPods를 통해 통합하는 경우, 정확한 크기 측정을 위해 타겟의 빌드 설정에서 `Enable Bitcode = NO`를 설정하세요.
{% endalert %}