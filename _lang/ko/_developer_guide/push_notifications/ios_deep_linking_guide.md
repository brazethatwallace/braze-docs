---
page_order: 1.1
nav_title: iOS 딥링킹 가이드
article_title: iOS 딥링킹 가이드
description: "iOS 앱에 사용할 딥링크 유형, AASA 파일이 필요한 시점, 구현해야 할 앱 델리게이트 메서드를 알아보세요."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# iOS 딥링킹 가이드 {#ios-deep-linking-guide}

> 이 가이드는 사용 중인 메시징 채널과 Branch 같은 타사 링크 제공업체 사용 여부에 따라 iOS 앱에 적합한 딥링킹 전략을 선택하는 데 도움을 줍니다.

구현 세부 사항은 [딥링킹]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift)을 참조하세요. 문제 해결은 [딥링킹 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)을 참조하세요.

## 링크 유형 선택 {#choosing-a-link-type}

iOS 앱에서 Braze 메시지의 링크를 처리하는 방법은 세 가지입니다. 각각의 방식은 서로 다르게 작동하며, 서로 다른 채널과 사용 사례에 적합합니다.

| 링크 유형 | 예시 | 적합한 용도 | 앱이 설치되지 않은 상태에서도 열리나요? |
|---|---|---|---|
| **커스텀 스킴** | `myapp://products/123` | 푸시 알림, 인앱 메시지, Content Cards | 아니요 — 링크 실패 |
| **유니버설 링크** | `https://myapp.com/products/123` | 이메일, SMS, 클릭 추적이 있는 채널 | 예 — 웹으로 대체됩니다 |
| **앱 내에서 웹 URL 열기** | 모든 `https://` URL | 모달 WebView에서 웹 콘텐츠 표시 | 해당 없음 — WebView에 표시됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="링크 유형 선택" }

### 커스텀 스킴 딥링크 {#custom-scheme-deep-links}

커스텀 스킴 딥링크(예: `myapp://products/123`)는 앱을 특정 화면으로 직접 엽니다. 타사에 의해 링크가 수정되지 않는 채널에서 가장 간단한 옵션입니다.

**다음과 같은 경우 커스텀 스킴 딥링크를 사용하세요:**
- 푸시 알림, 인앱 메시지 또는 Content Cards 발송
- 앱이 설치되어 있지 않을 때 링크가 작동할 필요가 없는 경우
- 클릭 추적(이메일 서비스 공급자 링크 래핑)이 필요하지 않은 경우

**다음과 같은 경우에는 커스텀 스킴 딥링크를 사용하지 마세요:**
- 이메일 발송 — 이메일 서비스 공급자는 클릭 추적을 위해 링크를 래핑하므로 커스텀 스킴이 깨집니다
- 앱이 설치되지 않은 경우 웹 페이지로 대체되는 링크가 필요한 경우

### 유니버설 링크 {#universal-links}

유니버설 링크(예: `https://myapp.com/products/123`)는 iOS가 브라우저에서 열지 않고 앱으로 라우팅할 수 있는 표준 HTTPS URL입니다. 서버 측 구성(AASA 파일)과 앱 측 설정(Associated Domains 권한)이 필요합니다.

**다음과 같은 경우에 유니버설 링크를 사용하세요:**
- 이메일 발송 시. 이메일 서비스 공급자가 클릭 추적을 위해 링크를 래핑하므로 링크는 반드시 HTTPS여야 합니다.
- 링크가 래핑되거나 단축되는 SMS 또는 기타 채널을 통해 발송하는 경우.
- 앱이 설치되지 않았을 때 웹 페이지로 대체되는 링크가 필요한 경우.
- Branch 또는 AppsFlyer 같은 타사 링크 제공업체를 사용하는 경우.

**다음과 같은 경우에는 유니버설 링크를 사용하지 마세요:**
- 푸시 알림, 인앱 메시지 또는 Content Cards에서만 딥링크가 필요한 경우. 커스텀 스킴이 더 간단합니다.

### "앱 내에서 웹 URL 열기" {#open-web-url-inside-app}

이 옵션은 앱 내의 모달 WebView에서 웹 페이지를 엽니다. `Braze.WebViewController`를 사용하여 Braze SDK가 전적으로 처리하므로 URL 처리 코드를 직접 작성할 필요가 없습니다.

**다음과 같은 경우에 "앱 내에서 웹 URL 열기"를 사용하세요:**
- 앱을 벗어나지 않고 웹 페이지(예: 프로모션이나 문서)를 표시하고 싶은 경우.
- URL이 특정 앱 화면으로의 딥링크가 아닌 표준 HTTPS 웹 페이지인 경우.

**다음과 같은 경우에는 "앱 내에서 웹 URL 열기"를 사용하지 마세요:**
- 앱에서 특정 뷰로 이동해야 하는 경우. 대신 커스텀 스킴이나 유니버설 링크를 사용하세요.
- 웹 페이지에 인증이 필요하거나 임베딩을 차단하는 콘텐츠 보안 정책 헤더가 있는 경우.

## 각 링크 유형에 필요한 사항 {#what-you-need-for-each-link-type}

### 커스텀 스킴 딥링크

| 요구 사항 | 세부 정보 |
|---|---|
| AASA 파일 | 필요하지 않음 |
| `Info.plist` | `CFBundleURLTypes` 아래에 스킴을 등록하고 `LSApplicationQueriesSchemes`에 추가 |
| 앱 델리게이트 메서드 | URL을 구문 분석하고 이동하도록 `application(_:open:options:)` 구현 |
| Braze SDK 구성 | 없음 — SDK는 기본적으로 커스텀 스킴 URL을 엽니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 스킴 딥링크" }

### 유니버설 링크

| 요구 사항 | 세부 정보 |
|---|---|
| AASA 파일 | 필수 — `https://yourdomain.com/.well-known/apple-app-site-association`에 호스팅 |
| Associated Domains | Xcode의 **Signing & Capabilities** 아래에 `applinks:yourdomain.com` 추가 |
| 앱 델리게이트 메서드 | `NSUserActivity`를 처리하도록 `application(_:continue:restorationHandler:)` 구현 |
| Braze SDK 구성 | `configuration.forwardUniversalLinks = true` 설정 |
| BrazeDelegate(선택 사항) | 커스텀 라우팅을 위해 `braze(_:shouldOpenURL:)` 구현(예: Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="유니버설 링크" }

{% alert important %}
Braze를 통해 이메일을 발송하는 경우, 이메일 서비스 공급자(SendGrid, SparkPost 또는 Amazon SES)가 링크를 클릭 추적 도메인으로 래핑합니다. AASA 파일은 기본 도메인뿐만 아니라 클릭 추적 도메인에도 호스팅해야 합니다. 전체 설정 방법은 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)를 참조하세요.
{% endalert %}

### "앱 내에서 웹 URL 열기"

| 요구 사항 | 세부 정보 |
|---|---|
| AASA 파일 | 필요하지 않음 |
| 앱 델리게이트 메서드 | 필요 없음 — SDK가 자동으로 처리합니다 |
| Braze SDK 구성 | 없음 — Campaign 작성기에서 **Open Web URL Inside App**을 선택 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="앱 내에서 웹 URL 열기" }

## AASA 파일이 필요한 경우 {#when-aasa}

Apple App Site Association(AASA) 파일은 **유니버설 링크**를 사용할 때만 필요합니다. 앱이 처리할 수 있는 URL을 iOS에 알려줍니다.

다음과 같은 경우 AASA 파일이 필요합니다:

- 이메일 Campaign에서 딥링크를 발송하는 경우(이메일 서비스 공급자가 링크를 HTTPS 클릭 추적 URL로 래핑하기 때문입니다).
- SMS Campaign에서 딥링크를 발송하는 경우(링크가 HTTPS URL로 단축될 수 있기 때문입니다).
- Branch, AppsFlyer 또는 다른 링크 제공업체를 사용하는 경우(해당 업체들이 자체 HTTPS 도메인을 사용하기 때문입니다).
- 푸시 알림, 인앱 메시지 또는 Content Cards에서 유니버설 링크를 사용하는 경우(덜 일반적이지만 `forwardUniversalLinks = true`로 가능합니다).

다음과 같은 경우에는 AASA 파일이 필요하지 않습니다:

- 푸시 알림, 인앱 메시지 또는 Content Cards에서 커스텀 스킴 딥링크(예: `myapp://`)만 사용하는 경우.
- **앱 내에서 웹 URL 열기** 옵션을 사용하는 경우.

AASA 설정 방법은 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#setting-up-universal-links-and-app-links)를 참조하세요.

## 앱 코드에서 링크를 처리해야 하는 경우 {#when-app-code}

구현할 델리게이트 메서드는 사용하는 링크 유형에 따라 달라집니다:

| 델리게이트 메서드 | 처리 대상 | 구현 시점 |
|---|---|---|
| `application(_:open:options:)` | 커스텀 스킴 딥링크(`myapp://`) | 모든 채널에서 커스텀 스킴 딥링크를 사용하는 경우 |
| `application(_:continue:restorationHandler:)` | 유니버설 링크(`https://`) | 이메일, SMS 또는 `forwardUniversalLinks = true`와 함께 유니버설 링크를 사용하는 경우 |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | SDK가 여는 모든 URL | 커스텀 라우팅 로직이 필요한 경우(예: Branch, 조건부 처리, 분석) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="앱 코드에서 링크를 처리해야 하는 경우" }

{% alert tip %}
Branch 같은 타사 링크 제공업체를 사용하는 경우, URL을 가로채서 해당 제공업체의 SDK로 전달하도록 `BrazeDelegate.braze(_:shouldOpenURL:)`를 구현하세요. 전체 예제는 [딥링킹용 Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)를 참조하세요.
{% endalert %}

## Braze에서 Branch 사용하기 {#branch}

[Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)를 링크 제공업체로 사용하는 경우, 표준 유니버설 링크 구성 외에 몇 가지 추가 단계가 필요합니다:

1. **Branch SDK**: [Branch 설명서](https://help.branch.io/developers-hub/docs/native-sdks-overview)에 따라 Branch SDK를 통합하세요.
2. **Associated Domains**: Xcode의 **Signing & Capabilities** 아래에 Branch 도메인(예: `applinks:yourapp.app.link`)을 추가하세요.
3. **BrazeDelegate**: Branch 링크를 Braze가 직접 처리하지 않고 Branch SDK로 라우팅하도록 `braze(_:shouldOpenURL:)`를 구현하세요.
4. **유니버설 링크 전달**: Braze SDK 구성에서 `configuration.forwardUniversalLinks = true`를 설정하세요.

구현 세부 사항 및 디버깅 안내는 [딥링킹용 Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)를 참조하세요.