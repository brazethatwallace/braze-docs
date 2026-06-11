---
nav_title: 딥링킹을 위한 Branch
article_title: 딥링킹을 위한 Branch
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "이 참조 문서에서는 Braze와 Branch 간의 파트너십과 이를 활용하여 딥링킹을 지원하는 방법을 설명합니다."
search_tag: Partner

---

# 딥링킹을 위한 Branch {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/)는 사용자 터치포인트에 대한 전체적인 뷰를 제공하여 기기, 채널, 플랫폼 전반에서 고객 확보, 참여, 측정에 사용되는 모바일 연결 플랫폼입니다.

_이 통합은 Branch에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Branch 통합을 사용하면 사용자 여정의 시작을 적절히 [기여도 분석]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/)하고 딥링크를 통해 의도한 위치로 연결하여 고객에게 더 나은 경험을 제공할 수 있습니다.

{% alert tip %}
사용 사례에 적합한 딥링킹 접근 방식을 선택하는 데 도움이 필요하면 [iOS 딥링킹 가이드]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/)를 참조하세요.
{% endalert %}

## 통합 {#integration}

[Branch의 SDK 통합 가이드](https://help.branch.io/developers-hub/docs/native-sdks-overview)를 따라 Branch 통합을 설정하세요. 추가 사용 사례는 아래를 참조하세요.

### iOS 유니버설 링크 지원 {#support-ios-universal-links}

Braze 내에서 iOS 유니버설 링크를 딥링크로 전송하려면 다음을 수행하세요.

#### 1단계: Branch 유니버설 링크 설정 {#step-1-set-up-branch-universal-links}

Branch 설명서를 따라 [유니버설 링크](https://help.branch.io/developers-hub/docs/ios-universal-links)를 설정하세요. 이 설정의 일부로 Branch는 Branch 링크 도메인(예: `yourapp.app.link`)에 AASA 파일을 자동으로 호스팅합니다.

#### 2단계: Associated Domains 구성 {#step-2-configure-associated-domains}

Xcode에서 앱 타겟 > **Signing & Capabilities**로 이동하여 **Associated Domains** 아래에 Branch 링크 도메인을 추가하세요:

```
applinks:yourapp.app.link
applinks:yourapp-alternate.app.link
```

커스텀 Branch 도메인을 사용하는 경우 해당 도메인도 추가하세요.

#### 3단계: Braze에서 유니버설 링크 전달 {#step-3-forward-universal-links-in-braze}

Braze SDK 구성에서 `forwardUniversalLinks`를 `true`로 설정하여 SDK가 유니버설 링크를 앱의 `AppDelegate`로 전달하도록 하세요:

{% tabs %}
{% tab swift %}
```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
let braze = Braze(configuration: configuration)
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
configuration.forwardUniversalLinks = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endtab %}
{% endtabs %}

#### 4단계: BrazeDelegate로 Branch 링크 라우팅 {#step-4-route-branch-links-with-brazedelegate}

[`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate)를 구현하여 Braze가 처리하기 전에 Branch 링크를 가로채세요. 이렇게 하면 Branch가 링크를 처리하고 자체 라우팅을 수행할 수 있습니다:

{% tabs %}
{% tab swift %}
```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host,
     host.contains("app.link") || host.contains("yourdomain.com") {
    // Let Branch handle this link
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle all other links
  return true
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  NSString *host = context.url.host;
  if (host && ([host containsString:@"app.link"] || [host containsString:@"yourdomain.com"])) {
    [[Branch getInstance] handleDeepLink:context.url];
    return NO;
  }
  return YES;
}
```
{% endtab %}
{% endtabs %}

해당하는 경우 `yourdomain.com`을 커스텀 Branch 도메인으로 교체하세요.

### 이메일에서의 딥링킹 {#deep-linking-in-email}

[유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/) 설명서를 참조하거나 [Branch 설명서](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work)를 확인하여 Braze를 통해 발송된 이메일에서 딥링킹을 설정하세요.

전화번호 링크(`href`에 `tel` 추가)는 사용자가 앱에 통화 권한을 부여하지 않는 한 iOS용 Gmail 앱에서 지원되지 않습니다.

이메일 서비스 공급자에 따라 클릭 추적 유니버설 링크를 지원하기 위해 추가 커스터마이징이 필요할 수 있습니다. 이 정보는 전용 문서에 설명되어 있습니다. 자세한 내용은 다음 참조 자료를 확인하세요:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)

## 문제 해결 {#troubleshooting}

Braze Campaign에서 Branch 링크가 예상대로 작동하지 않는 경우 다음 단계를 따르세요.

### Braze 외부에서 링크 작동 확인 {#verify-the-link-works-outside-of-braze}

실제 iOS 기기의 메모 앱에서 Branch 링크를 열어보세요. 앱이 열리지 않는 경우:

- 문제는 Braze가 아닌 Branch 또는 AASA 구성에 있습니다.
- `https://yourapp.app.link/.well-known/apple-app-site-association`에서 Branch AASA를 검증하세요.
- Branch 대시보드에서 Bundle ID와 Team ID가 일치하는지 확인하세요.

### 이중 로깅 활성화 {#enable-dual-logging}

1. **Braze**: [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/)하고 `Opening '<URL>':` 항목을 확인하세요. 이를 통해 SDK가 링크를 수신했는지 확인할 수 있습니다.
2. **Branch**: [Branch 테스트 모드](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking)를 활성화하고 Branch 대시보드에서 링크 클릭 이벤트를 확인하세요.
3. **비교**: Braze가 링크를 로깅하지만 Branch에서 클릭이 표시되지 않는 경우, `BrazeDelegate` 라우팅 로직이 링크를 올바르게 가로채지 못하고 있을 가능성이 높습니다. `shouldOpenURL`의 도메인 매칭에 Branch 도메인이 포함되어 있는지 확인하세요.

### 일반적인 문제 {#common-issues}

| 증상 | 가능한 원인 | 해결 방법 |
|---|---|---|
| Branch 링크가 Safari에서 열림 | Branch 도메인에서 AASA가 유효하지 않거나 누락됨 | Associated Domains 및 AASA 파일을 확인하세요 |
| Branch 링크가 열리지만 잘못된 화면으로 이동 | Branch 링크 데이터가 잘못 구성됨 | Branch 대시보드에서 라우팅 규칙을 확인하세요 |
| 푸시에서는 작동하지만 이메일에서는 작동하지 않음 | 클릭 추적 도메인에 AASA가 누락됨 | 이메일 서비스 공급자의 클릭 추적 도메인에 AASA를 호스팅하세요. [이메일 설정](#deep-linking-in-email) 참조 |
| Branch 링크에 대해 `shouldOpenURL`이 실행되지 않음 | `forwardUniversalLinks`가 활성화되지 않음 | `configuration.forwardUniversalLinks = true`로 설정하세요 |
| 메모에서는 작동하지만 Braze에서는 작동하지 않음 | `BrazeDelegate`가 Branch URL에 대해 `true`를 반환함 | `shouldOpenURL`의 도메인 확인이 Branch 도메인과 일치하는지 확인하세요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="일반적인 문제" }

더 많은 딥링킹 문제 해결 시나리오는 [딥링킹 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting/)을 참조하세요.