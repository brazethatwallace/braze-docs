---
nav_title: 딥링킹 문제 해결
article_title: 딥링킹 문제 해결
description: "증상 색인, 표준 조사 경로, 플랫폼별 점검 사항을 활용하여 iOS 딥링킹 문제를 진단합니다."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# 딥링킹 문제 해결 {#troubleshoot-deep-linking}

> 이 페이지를 활용하여 iOS에서 발생하는 일반적인 딥링킹 문제를 진단할 수 있습니다. 적합한 링크 유형 선택에 대한 도움말은 [iOS 딥링킹 가이드]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide)를 참조하세요. 구현 세부 사항은 [딥링킹]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift)을 참조하세요.

## 여기서 시작하세요: 증상 확인하기 {#start-here-match-your-symptom}

아래 표에서 현재 겪고 있는 동작을 찾은 다음, 해당 섹션의 단계를 따르세요. 어떤 섹션이 적용되는지 확실하지 않은 경우 [표준 조사 경로](#standard-investigation-path)를 사용하세요.

| 증상 | 이동 |
| --- | --- |
| 커스텀 스킴 링크가 앱을 열지만 잘못된 화면이 표시됨 | [커스텀 스킴 딥링크가 올바른 뷰를 열지 않음](#custom-scheme-deep-link-does-not-open-the-correct-view) |
| 유니버설 링크가 앱 대신 Safari를 열음 | [유니버설 링크가 앱 대신 Safari에서 열림](#universal-link-opens-in-safari-instead-of-the-app) |
| 이메일 링크가 앱을 열지 않음 | [이메일의 딥링크가 앱을 열지 않음](#deep-link-from-email-does-not-open-the-app) |
| 모든 이메일 링크가 앱을 열음 | [모든 이메일 링크가 앱을 열음](#every-email-link-opens-the-app) |
| 푸시에서는 작동하지만 인앱 메시지에서는 작동하지 않음 (또는 그 반대) | [딥링크가 푸시에서는 작동하지만 인앱 메시지에서는 작동하지 않음](#deep-link-works-from-push-but-not-from-in-app-message) |
| "Open Web URL Inside App"이 빈 WebView를 표시함 | ["Open Web URL Inside App"이 빈 페이지 또는 깨진 페이지를 표시함](#open-web-url-inside-app-shows-a-blank-or-broken-page) |
| Branch 링크가 앱을 열지 않거나 올바르게 라우팅되지 않음 | [Braze에서 Branch 문제 해결](#branch) |
| 명확한 원인 없이 딥링크가 실패함 | [일반 디버깅 팁](#general-debugging-tips) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="딥링킹 증상" }

## 표준 조사 경로 {#standard-investigation-path}

모든 딥링킹 문제에 대해 이 워크플로우를 사용합니다. 1단계부터 시작하세요.

1. Braze 외부에서 링크를 테스트합니다. 커스텀 스킴의 경우 터미널에서 `xcrun simctl openurl booted "<URL>"`을 실행합니다(예: `xcrun simctl openurl booted "myapp://products/123"`). 유니버설 링크의 경우 실제 기기의 메모 앱에 URL을 붙여넣고 탭합니다.
2. [상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)하고 문제를 재현합니다. `channel`, `useWebView`, `isUniversalLink`가 포함된 `Opening '<URL>':` 항목을 확인합니다.
3. 유니버설 링크의 경우 AASA 파일과 Associated Domains 자격을 검증합니다.
4. 이메일 링크의 경우 클릭 추적 도메인이 유효한 AASA 파일을 호스팅하는지 확인합니다.
5. `BrazeDelegate.braze(_:shouldOpenURL:)`를 구현한 경우, 모든 채널에서 링크를 일관되게 처리하는지 확인합니다.
6. 문제가 지속되면 상세 로그와 링크 URL을 포함하여 [Braze 지원]({{site.baseurl}}/braze_support)에 문의하세요.

## 커스텀 스킴 딥링크가 올바른 뷰를 열지 않음 {#custom-scheme-deep-link-does-not-open-the-correct-view}

**증상:** 커스텀 스킴 딥링크(예: `myapp://products/123`)가 앱을 열지만 의도한 화면으로 이동하지 않습니다.

1. **스킴이 등록되어 있는지 확인합니다.** Xcode에서 `Info.plist`의 `CFBundleURLTypes` 아래에 스킴이 나열되어 있는지 확인합니다.
2. **핸들러를 확인합니다.** `application(_:open:options:)`에 브레이크포인트를 설정하여 호출되고 있는지 확인하고 `url` 파라미터를 검사합니다.
3. **링크를 독립적으로 테스트합니다.** 터미널에서 다음 명령을 실행하여 Braze 외부에서 딥링크를 테스트합니다:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   여기서 링크가 작동하지 않으면 문제는 Braze가 아니라 앱의 URL 처리에 있습니다.
4. **URL 형식을 확인합니다.** Campaign의 URL이 핸들러에서 기대하는 형식과 일치하는지 확인합니다. 경로 구성 요소 누락이나 잘못된 대소문자 사용이 흔한 실수입니다.

## 유니버설 링크가 앱 대신 Safari에서 열리는 경우 {#universal-link-opens-in-safari-instead-of-the-app}

**증상:** 유니버설 링크(예: `https://myapp.com/products/123`)가 앱 대신 Safari에서 열립니다.

### Associated Domains 권한 확인 {#verify-the-associated-domains-entitlement}

Xcode에서 앱 타겟 > **Signing & Capabilities**로 이동하여 **Associated Domains** 아래에 `applinks:yourdomain.com`이 나열되어 있는지 확인하세요.

### AASA 파일 유효성 검사 {#validate-the-aasa-file}

Apple App Site Association(AASA) 파일은 다음 위치 중 하나에 호스팅되어야 합니다:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

다음 사항을 확인하세요:

- 파일이 유효한 인증서를 사용하여 HTTPS로 제공됩니다.
- `Content-Type`이 `application/json`입니다.
- 파일 크기가 128KB 미만입니다.
- `appID`가 팀 ID 및 번들 ID와 일치합니다(예: `ABCDE12345.com.example.myapp`).
- `paths` 또는 `components` 배열에 예상하는 URL 패턴이 포함되어 있습니다.

AASA를 검증하려면 [Apple의 검색 검증 도구](https://search.developer.apple.com/appsearch-validation-tool/)를 사용하거나 다음 명령어를 실행하세요:

```bash
swcutil dl -d yourdomain.com
```

### `AppDelegate` 확인 {#check-the-appdelegate}

`AppDelegate`에 `application(_:continue:restorationHandler:)`가 구현되어 있고 `NSUserActivity`를 올바르게 처리하는지 확인하세요:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Braze SDK 구성 확인 {#verify-braze-sdk-configuration}

Braze에서 전송된 푸시 알림, 인앱 메시지 또는 Content Cards에서 유니버설 링크를 사용하는 경우 `forwardUniversalLinks`가 활성화되어 있는지 확인하세요:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
유니버설 링크 전달에는 애플리케이션 권한에 대한 접근이 필요합니다. 시뮬레이터에서 실행할 때는 이러한 권한을 직접 사용할 수 없습니다. 시뮬레이터에서 테스트하려면 **Copy Bundle Resources** 빌드 단계에 `.entitlements` 파일을 추가하세요.
{% endalert %}

### 길게 누르기 문제 확인 {#check-for-the-long-press-issue}

유니버설 링크를 길게 눌러 **열기**를 선택하면 iOS가 해당 도메인의 유니버설 링크 연결을 "해제"할 수 있습니다. 이는 iOS의 알려진 동작입니다. 재설정하려면 링크를 다시 길게 누르고 **[앱 이름]에서 열기**를 선택하세요.

## 이메일의 딥링크가 앱을 열지 않는 경우 {#deep-link-from-email-does-not-open-the-app}

**증상:** 이메일의 링크가 유니버설 링크를 통해 앱을 열지 않습니다.

이메일 링크는 ESP의 클릭 추적 시스템을 거치며, 이 시스템이 링크를 추적 도메인으로 래핑합니다(예: `https://click.yourdomain.com/...`). 이메일에서 유니버설 링크가 작동하려면 기본 도메인뿐만 아니라 클릭 추적 도메인에도 AASA 파일을 구성해야 합니다.

### 클릭 추적 도메인 AASA 확인 {#verify-click-tracking-domain-aasa}

1. ESP 설정(SendGrid, SparkPost 또는 Amazon SES)에서 클릭 추적 도메인을 확인합니다.
2. `https://your-click-tracking-domain/.well-known/apple-app-site-association`에 AASA 파일을 호스팅합니다.
3. 클릭 추적 도메인의 AASA 파일에 동일한 `appID`와 유효한 경로 패턴이 포함되어 있는지 확인합니다.

ESP별 설정 안내는 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)를 참조하세요.

### 리다이렉트 체인 확인 {#check-the-redirect-chain}

일부 ESP는 클릭 추적 URL에서 최종 URL로 리다이렉트를 수행합니다. 유니버설 링크는 iOS가 *초기* 도메인(클릭 추적 도메인)을 앱과 연결된 것으로 인식하는 경우에만 작동합니다. 리다이렉트가 AASA 확인을 우회하면 링크가 Safari에서 열립니다.

테스트 방법:

1. 자신에게 테스트 이메일을 보냅니다.
2. 링크를 길게 눌러 URL을 확인합니다. 이것이 클릭 추적 URL입니다.
3. 이 도메인에 유효한 AASA 파일이 있는지 확인합니다.

## 모든 이메일 링크가 앱을 여는 경우 {#every-email-link-opens-the-app}

**증상:** 이메일의 모든 링크가 브라우저에서 열릴 것으로 예상되는 링크까지 포함하여 앱을 엽니다.

클릭 추적 도메인의 AASA 파일이 해당 도메인의 모든 URL과 일치하는 `paths`를 사용하고 있습니다(예: `*` 또는 `/*`). 이 경우 iOS는 클릭 추적된 모든 이메일 링크를 유니버설 링크로 처리합니다.

`paths`를 앱에서 열어야 하는 URL로만 제한하세요. SendGrid의 경우 `/uni/`를 매칭하고 해당 링크에만 `universal="true"`를 추가하세요.

Android `pathPrefix` 값을 포함한 ESP별 설정에 대해서는 [유니버설 링크 및 App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#universal-links-app-links-and-click-tracking)를 참조하세요.

## 딥링크가 푸시에서는 작동하지만 인앱 메시지에서는 작동하지 않는 경우(또는 그 반대) {#deep-link-works-from-push-but-not-from-in-app-message}

**증상:** 동일한 딥링크가 하나의 Braze 채널에서는 작동하지만 다른 채널에서는 작동하지 않습니다.

### BrazeDelegate 확인 {#check-the-brazedelegate}

`BrazeDelegate.braze(_:shouldOpenURL:)`를 구현하는 경우, 채널 간에 링크를 일관되게 처리하는지 확인하세요. `context` 매개변수에는 소스 채널이 포함됩니다. 특정 채널의 링크를 실수로 필터링할 수 있는 조건 로직이 있는지 확인하세요.

### 상세 로깅 활성화 {#enable-verbose-logging}

[상세 로깅을 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)하고 문제를 재현하세요. `Opening` 로그 항목을 확인합니다:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

작동하는 채널과 작동하지 않는 채널의 로그 출력을 비교하세요. `useWebView` 또는 `isUniversalLink`의 차이는 SDK가 링크를 다르게 해석하고 있음을 나타냅니다.

### 커스텀 디스플레이 델리게이트 확인 {#check-for-custom-display-delegates}

커스텀 인앱 메시지 디스플레이 델리게이트 또는 Content Cards 클릭 핸들러를 사용하는 경우, 링크 이벤트를 Braze SDK에 올바르게 전달하여 처리하도록 하는지 확인하세요.

## "앱 내에서 웹 URL 열기" 시 빈 페이지 또는 깨진 페이지가 표시되는 경우 {#open-web-url-inside-app-shows-a-blank-or-broken-page}

**증상:** **앱 내에서 웹 URL 열기**를 선택했을 때 빈 페이지 또는 깨진 WebView가 표시됩니다.

1. **URL이 HTTPS를 사용하는지 확인하세요.** SDK의 WebView는 ATS 호환 URL을 요구합니다. HTTP 링크는 오류 없이 조용히 실패합니다.
2. **Content Security Policy 헤더를 확인하세요.** 대상 웹 페이지가 `X-Frame-Options: DENY` 또는 제한적인 `Content-Security-Policy`를 설정하면 WebView에서 렌더링이 차단됩니다.
3. **커스텀 스킴으로의 리디렉션을 확인하세요.** 웹 페이지가 커스텀 스킴(예: `myapp://`)으로 리디렉션되는 경우 WebView는 이를 처리할 수 없습니다.
4. **Safari에서 URL을 테스트하세요.** 해당 기기의 Safari에서 페이지가 로드되지 않는다면, WebView에서도 로드되지 않습니다.

## Braze에서 Branch 문제 해결 {#branch}

[Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)를 링크 제공업체로 사용하는 경우:

### BrazeDelegate가 Branch로 라우팅하는지 확인 {#verify-the-brazedelegate-routes-to-branch}

`BrazeDelegate`가 Branch 링크를 가로채서 Branch SDK로 전달해야 합니다. 다음 사항을 확인하세요:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

`shouldOpenURL`이 Branch 링크에 대해 `true`를 반환하면, Braze가 Branch로 라우팅하지 않고 직접 처리합니다.

### Branch 링크 도메인 확인 {#check-branch-link-domain}

`BrazeDelegate`의 Branch 도메인이 실제 Branch 링크 도메인과 일치하는지 확인하세요. Branch는 여러 도메인 형식을 사용합니다:

- `yourapp.app.link` (기본값)
- `yourapp-alternate.app.link` (대체)
- 커스텀 도메인 (Branch 대시보드에서 설정한 경우)

### 두 SDK의 로깅 모두 활성화 {#enable-both-sdks-logging}

링크가 체인에서 끊어지는 지점을 진단하려면:

1. [Braze 상세 로깅]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)을 활성화하세요. SDK가 링크를 수신했는지 확인하기 위해 `Opening '<URL>':` 항목을 찾으세요.
2. [Branch 테스트 모드](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking)를 활성화하세요. Branch 대시보드에서 링크 클릭 이벤트를 확인하세요.
3. Braze가 링크를 기록했지만 Branch에서 클릭이 감지되지 않는다면, `BrazeDelegate` 라우팅 로직에 문제가 있을 가능성이 높습니다.

### Branch 대시보드 구성 확인 {#check-branch-dashboard-configuration}

Branch 대시보드에서 다음을 확인하세요:

- 앱의 **Bundle ID**와 **Team ID**가 Xcode 프로젝트와 일치합니다.
- **Associated Domains**에 Branch 링크 도메인이 포함되어 있습니다.
- Branch AASA 파일이 유효합니다(Branch는 `app.link` 도메인에서 자동으로 호스팅합니다).

### Branch 링크를 독립적으로 테스트 {#test-branch-links-independently}

문제를 격리하기 위해 Braze 외부에서 Branch 링크를 테스트하세요:

1. 기기에서 Safari로 Branch 링크를 여세요. 앱이 열리지 않는다면, 문제는 Braze가 아닌 Branch 또는 AASA 구성에 있습니다.
2. Branch 링크를 메모 앱에 붙여넣고 탭하세요. 유니버설 링크는 Safari 주소창보다 메모 앱에서 더 안정적으로 작동합니다.

## 일반적인 디버깅 팁 {#general-debugging-tips}

### 상세 로깅 사용 {#use-verbose-logging}

[상세 로깅 활성화]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)를 통해 SDK가 링크를 어떻게 처리하는지 정확히 확인할 수 있습니다. 확인해야 할 주요 항목은 다음과 같습니다:

| 로그 항목 | 의미 |
|---|---|
| `Opening '<URL>': - channel: notification` | SDK가 푸시 알림의 링크를 처리하고 있습니다 |
| `Opening '<URL>': - channel: inAppMessage` | SDK가 인앱 메시지의 링크를 처리하고 있습니다 |
| `Opening '<URL>': - channel: contentCard` | SDK가 콘텐츠 카드의 링크를 처리하고 있습니다 |
| `useWebView: true` | SDK가 인앱 WebView에서 URL을 엽니다 |
| `isUniversalLink: true` | SDK가 해당 URL을 유니버설 링크로 식별했습니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="상세 로깅 사용" }

이 로그를 읽는 방법에 대한 자세한 내용은 [상세 로그 읽기]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)를 참조하세요.

### 링크를 개별적으로 테스트 {#test-links-in-isolation}

Braze를 통해 테스트하기 전에, 딥링크 또는 유니버설 링크가 자체적으로 정상 작동하는지 확인하세요:

- **커스텀 스킴**: 터미널에서 `xcrun simctl openurl booted "myapp://path"`를 실행합니다.
- **유니버설 링크**: 실제 기기의 메모 앱에 URL을 붙여넣고 탭합니다. Safari 주소창에서 테스트하지 마세요. iOS는 입력된 URL과 탭한 링크를 다르게 처리합니다.
- **Branch 링크**: 기기의 메모 앱에서 Branch 링크를 엽니다.

### 실제 기기에서 테스트 {#test-on-a-physical-device}

유니버설 링크는 iOS 시뮬레이터에서 제한적으로 지원됩니다. 정확한 결과를 위해 항상 실제 기기에서 테스트하세요. 시뮬레이터에서 테스트해야 하는 경우, `.entitlements` 파일을 **Copy Bundle Resources** 빌드 단계에 추가하세요.