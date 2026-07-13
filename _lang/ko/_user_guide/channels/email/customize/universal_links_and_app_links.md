---
nav_title: "유니버설 링크 및 앱 링크"
article_title: "유니버설 링크 및 앱 링크"
page_order: 6.4
page_type: reference
description: "이 문서에서는 Apple 유니버설 링크와 Android 앱 링크를 설정하는 방법을 설명합니다."
channel: email
---

# 유니버설 링크 및 앱 링크 {#universal-links-and-app-links}

> 이 문서에서는 Apple 유니버설 링크와 Android 앱 링크를 설정하는 방법을 설명합니다.

{% alert tip %}
모든 메시징 채널에서의 링크 유형 비교와 AASA 파일이 필요한 시점에 대한 안내는 [iOS 딥링킹 가이드]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide)를 참조하세요.
{% endalert %}

Apple 유니버설 링크와 Android 앱 링크는 웹 콘텐츠와 모바일 앱 간의 원활한 전환을 제공하기 위해 고안된 메커니즘입니다. 유니버설 링크는 iOS에 특화되어 있으며, Android 앱 링크는 Android 애플리케이션에서 동일한 목적을 수행합니다.

## 유니버설 링크 및 앱 링크의 작동 방식 {#how-universal-links-and-app-links-work}

유니버설 링크(iOS)와 앱 링크(Android)는 웹 페이지와 앱 내 콘텐츠 모두를 가리키는 표준 웹 링크(`http://mydomain.com`)입니다.

유니버설 링크 또는 앱 링크가 열리면 운영 체제는 해당 도메인에 등록된 설치된 앱이 있는지 확인합니다. 앱이 발견되면 웹 페이지를 로드하지 않고 즉시 앱이 실행됩니다. 앱이 발견되지 않으면 사용자의 기본 웹 브라우저에서 웹 URL이 로드되며, 이 경우 각각 App Store 또는 Google Play Store로 리디렉션되도록 구성할 수도 있습니다.

간단히 말해, 유니버설 링크를 사용하면 웹사이트가 자체 웹 페이지를 특정 앱 화면과 연결할 수 있으므로, 사용자가 앱 화면에 해당하는 웹 페이지 링크를 클릭하면 앱이 직접 열릴 수 있습니다(앱이 현재 설치되어 있는 경우).

{% alert important %}
Firebase Dynamic Links는 지원이 중단되었습니다. Braze는 Firebase와 직접 통합되어 있지 않으며, 딥링킹은 Braze 플랫폼 외부에서 관리됩니다. 플랫폼 네이티브 솔루션(이 문서에서 설명하는 Apple 유니버설 링크 및 Android 앱 링크) 또는 대체 딥링킹 서비스 제공업체로 마이그레이션하세요. 마이그레이션 안내는 [Firebase 마이그레이션 FAQ](https://firebase.google.com/support/dynamic-links-faq)를 참조하세요.
{% endalert %}

다음 표는 유니버설 링크와 기존 딥링크 간의 주요 차이점을 보여줍니다:

|                        | 유니버설 링크 및 앱 링크                                  | 딥링크                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| 플랫폼 호환성 | iOS(버전 9 이상) 및 Android(버전 6.0 이상)  | 다양한 모바일 OS에서 사용    |
| 목적                | iOS 및 Android 기기에서 웹과 앱 콘텐츠를 원활하게 연결 | 특정 앱 콘텐츠로 연결 |
| 기능               | 컨텍스트에 따라 웹 페이지 또는 앱 콘텐츠로 이동           | 특정 앱 화면을 열기   |
| 앱 설치       | 앱이 설치되어 있으면 앱을 열고, 그렇지 않으면 웹 콘텐츠를 열기 | 앱이 설치되어 있어야 함 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="유니버설 링크 및 앱 링크의 작동 방식" }

## 사용 사례 {#use-cases}

유니버설 링크와 앱 링크는 이메일 Campaign에서 가장 일반적으로 사용됩니다. 이메일은 데스크탑과 모바일 기기 모두에서 열고 클릭할 수 있기 때문입니다.

일부 채널은 이러한 링크와 잘 작동하지 않습니다. 예를 들어, 푸시 알림, In-App Messages, Content Cards는 스킴 기반 딥링크(`mydomain://`)를 사용해야 합니다.

{% alert note %}
Android 앱 링크는 해당 도메인의 링크를 다른 웹 URL과 별도로 처리하는 로직이 포함된 커스텀 `IBrazeDeeplinkHandler`가 필요합니다. 딥링크를 사용하고 이메일 이외의 채널에서 링크 사용 방식을 통일하는 것이 더 쉬울 수 있습니다.
{% endalert %}

## 필수 조건 {#prerequisites}

유니버설 링크와 앱 링크를 사용하려면:

- 웹사이트가 HTTPS를 통해 접근 가능해야 합니다
- 앱이 App Store(iOS) 또는 Google Play Store(Android)에서 사용 가능해야 합니다

## 유니버설 링크 및 앱 링크 설정 {#setting-up-universal-links-and-app-links}

앱이 유니버설 링크 또는 앱 링크를 지원하려면 iOS와 Android 모두 링크 도메인에 특별한 권한 파일이 호스팅되어야 합니다. 이 파일에는 해당 도메인의 링크를 열 수 있는 앱의 정의가 포함되어 있으며, iOS의 경우 해당 앱이 열 수 있는 경로도 포함됩니다:

- **iOS:** Apple App Site Association(AASA) 파일
- **Android:** Digital Asset Links 파일

이 권한 파일 외에도, 앱 내에 설정된 앱이 열 수 있는 링크 도메인에 대한 하드코딩된 정의가 있습니다:

- **iOS:** Xcode에서 "Associated Domains"로 설정
- **Android:** 앱의 `AndroidManifest.xml` 파일에 정의

이 두 부분으로 구성된 도메인-앱 연결은 유니버설 링크 또는 앱 링크가 작동하는 데 필수적이며, 어떤 앱이든 특정 도메인의 링크를 가로채거나 어떤 도메인이든 특정 앱을 여는 것을 방지합니다.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

이 단계는 Apple 개발자 설명서를 기반으로 작성되었습니다. 자세한 내용은 [앱과 웹사이트가 콘텐츠에 링크하도록 허용하기](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc)를 참조하세요.

### 1단계: 앱 자격 구성 {#step-1-configure-your-app-entitlements}

{% alert note %}
[Xcode 13 이상](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/)에서는 Xcode가 자격 프로비저닝을 자동으로 처리할 수 있습니다. [1c단계](#step-1c)로 건너뛰고 문제가 발생하면 이 지침을 다시 참조할 수 있습니다.
{% endalert %}

#### 1a단계: 앱 등록 {#step-1a}

1. developer.apple.com으로 이동하여 로그인합니다.
2. **Certificates, Identifiers & Profiles**를 클릭합니다.
3. **Identifiers**를 클릭합니다.
4. 등록된 App Identifier가 아직 없는 경우 +를 클릭하여 새로 만듭니다.
   a. **Name**을 입력합니다. 원하는 이름을 입력할 수 있습니다.
   b. **Bundle ID**를 입력합니다. 적절한 빌드 타겟에 대한 Xcode 프로젝트의 **General** 탭에서 번들 ID를 찾을 수 있습니다.

#### 1b단계: App Identifier에서 Associated Domains 활성화 {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. 기존 또는 새로 생성한 App Identifier에서 **App Services** 섹션을 찾습니다.
2. **Associated Domains**를 선택합니다.
3. **Save**를 클릭합니다.

![App Services 섹션]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### 1c단계: Xcode 프로젝트에서 Associated Domains 활성화 {#step-1c}

진행하기 전에 Xcode 프로젝트에서 App Identifier를 등록한 곳과 동일한 팀이 선택되어 있는지 확인하세요.

1. Xcode에서 프로젝트 파일의 **Capabilities** 탭으로 이동합니다.
2. **Associated Domains**를 활성화합니다.

##### 문제 해결 팁 {#troubleshooting-tip}

"An App ID with Identifier 'your-app-id' is not available. Please enter a different string" 오류가 표시되면 다음을 수행하세요:

1. 올바른 팀이 선택되어 있는지 확인합니다.
2. Xcode 프로젝트의 번들 ID([1a단계](#step-1a))가 App Identifier 등록 시 사용한 것과 일치하는지 확인합니다.

#### 1d단계: 도메인 자격 추가 {#step-1d-add-the-domain-entitlement}

도메인 섹션에서 적절한 도메인 태그를 추가합니다. `applinks:` 접두사를 붙여야 합니다. 이 경우 `applinks:yourdomain.com`을 추가한 것을 확인할 수 있습니다.

![Associated Domains 섹션]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### 1e단계: 자격 파일이 빌드에 포함되어 있는지 확인 {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

프로젝트 브라우저에서 새 자격 파일이 **Target Membership** 아래에 선택되어 있는지 확인합니다.

Xcode가 이를 자동으로 처리합니다.

### 2단계: AASA 파일을 호스팅하도록 웹사이트 구성 {#step-2-configure-your-website-to-host-the-aasa-file}

웹사이트 도메인을 iOS의 네이티브 앱과 연결하려면 웹사이트에 Apple App Site Association(AASA) 파일을 호스팅해야 합니다. 이 파일은 iOS에 도메인 소유권을 안전하게 확인하는 방법으로 사용됩니다. iOS 9 이전에는 개발자가 어떤 검증 없이도 앱을 열기 위한 URI 스킴을 등록할 수 있었습니다. 그러나 AASA를 통해 이 프로세스가 훨씬 더 안전하고 신뢰할 수 있게 되었습니다.

AASA 파일에는 앱 목록과 유니버설 링크로 포함하거나 제외해야 하는 도메인의 URL 경로가 포함된 JSON 오브젝트가 있습니다. 다음은 AASA 파일의 예시입니다:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: 앱의 **Team ID**(`https://developer.apple.com/account/#/membership/`에서 팀 ID를 확인할 수 있음)와 **Bundle Identifier**를 결합하여 구성됩니다. 위 예시에서 "JHGFJHHYX"는 팀 ID이고 "com.facebook.ios"는 번들 ID입니다.
- `paths`: 연결에 포함하거나 제외할 경로를 지정하는 문자열 배열입니다. 경로 앞에 `NOT`을 사용하여 경로를 비활성화할 수 있습니다. 이 예시에서는 이 경로의 모든 링크가 앱을 여는 대신 웹으로 이동합니다. `*`를 와일드카드로 사용하여 디렉토리의 모든 경로를 활성화하고, `?`를 사용하여 단일 문자를 매칭할 수 있습니다(예: /archives/201?/로 2010-2019의 모든 숫자를 매칭).

{% alert note %}
이 문자열은 대소문자를 구분하며 쿼리 문자열과 프래그먼트 식별자는 무시됩니다.
{% endalert %}

### 3단계: 도메인에 AASA 파일 호스팅 {#step-3-host-the-aasa-file-on-your-domain}

AASA 파일이 준비되면 `https://<<yourdomain>>/apple-app-site-association` 또는 `https://<<yourdomain>>/.well-known/apple-app-site-association`에 호스팅할 수 있습니다.

`apple-app-site-association` 파일을 HTTPS 웹 서버에 업로드합니다. 파일을 서버의 루트 또는 `.well-known` 하위 디렉토리에 배치할 수 있습니다. 파일 이름에 `.json`을 추가하지 마세요.

{% alert important %}
iOS는 보안 연결(HTTPS)을 통해서만 AASA 파일을 가져오려고 시도합니다.
{% endalert %}

AASA 파일을 호스팅할 때 파일이 다음 가이드라인을 따르는지 확인하세요:

- HTTPS를 통해 제공됩니다.
- `application/json` MIME 유형을 사용합니다.
- 128KB를 초과하지 않습니다(iOS 9.3.1 이상의 요구 사항)

### 4단계: 유니버설 링크를 처리하도록 앱 준비 {#step-4-prepare-your-app-to-handle-universal-links}

사용자가 iOS 기기에서 유니버설 링크를 탭하면 기기가 앱을 실행하고 [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) 오브젝트를 전송합니다. 그러면 앱은 NSUserActivity 오브젝트를 쿼리하여 어떻게 실행되었는지 확인할 수 있습니다.

앱에서 유니버설 링크를 지원하려면 다음 단계를 수행하세요:

1. 앱이 지원하는 도메인을 지정하는 자격을 추가합니다.
2. NSUserActivity 오브젝트를 수신할 때 적절하게 응답하도록 앱 델리게이트를 업데이트합니다.

Xcode에서 **Capabilities** 탭의 **Associated Domains** 섹션을 열고 앱이 지원하는 각 도메인에 대한 항목을 `applinks:` 접두사와 함께 추가합니다. 예: `applinks:www.mywebsite.com`.

{% alert note %}
Apple은 이 목록을 20~30개 도메인 이하로 제한할 것을 권장합니다.
{% endalert %}

### 5단계: 유니버설 링크 테스트 {#step-5-test-your-universal-link}

유니버설 링크를 이메일에 추가하고 테스트 기기로 전송합니다. Safari URL 필드에 유니버설 링크를 직접 붙여넣으면 앱이 자동으로 열리지 않습니다. 이 경우 웹사이트를 수동으로 아래로 당겨야 상단에 해당 앱을 열 것인지 묻는 프롬프트가 나타납니다.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

이 단계는 Android 개발자 설명서를 기반으로 작성되었습니다. 자세한 내용은 [Android 앱 링크 추가](https://developer.android.com/training/app-links#add-app-links) 및 [앱 콘텐츠에 대한 딥링크 생성](https://developer.android.com/training/app-links/deep-linking)을 참조하세요.

{% alert note %}
Android 앱 링크는 해당 도메인의 링크를 다른 웹 URL과 별도로 처리하는 로직이 포함된 커스텀 `IBrazeDeeplinkHandler`가 필요합니다. 딥링크를 사용하고 이메일 이외의 채널에서 링크 사용 방식을 통일하는 것이 더 쉬울 수 있습니다.
{% endalert %}

### 1단계: 딥링크 생성 {#step-1-create-deep-links}

먼저 Android 앱에 대한 딥링크를 생성해야 합니다. `AndroidManifest.xml` 파일에 [인텐트 필터](https://developer.android.com/guide/components/intents-filters)를 추가하여 수행할 수 있습니다. 인텐트 필터에는 `VIEW` 액션과 `BROWSABLE` 카테고리, 그리고 데이터 요소에 웹사이트의 URL이 포함되어야 합니다.

### 2단계: 앱을 웹사이트와 연결 {#step-2-associate-your-app-with-your-website}

앱을 웹사이트와 연결해야 합니다. Digital Asset Links 파일을 생성하여 수행할 수 있습니다. 이 파일은 JSON 형식이어야 하며 웹사이트의 링크를 열 수 있는 Android 앱에 대한 세부 정보가 포함됩니다. 웹사이트의 `.well-known` 디렉토리에 배치해야 합니다.

### 3단계: 앱 매니페스트 파일 업데이트 {#step-3-update-your-app-manifest-file}

`AndroidManifest.xml` 파일에서 application 요소 내에 meta-data 요소를 추가합니다. meta-data 요소에는 "asset_statements"라는 `android:name` 속성과 웹사이트의 URL이 포함된 문자열 배열이 있는 리소스 파일을 가리키는 `android:resource` 속성이 있어야 합니다.

### 4단계: 딥링크를 처리하도록 앱 준비 {#step-4-prepare-your-app-to-handle-deep-links}

Android 앱에서 수신되는 딥링크를 처리해야 합니다. 액티비티를 시작한 인텐트를 가져오고 그로부터 데이터를 추출하여 수행할 수 있습니다.

### 5단계: 딥링크 테스트 {#step-5-testing-your-deep-links}

마지막으로 딥링크를 테스트할 수 있습니다. 메시징 앱이나 이메일을 통해 자신에게 링크를 보내고 클릭합니다. 모든 것이 올바르게 설정되어 있으면 앱이 열립니다.

{% endtab %}
{% endtabs %}

## 유니버설 링크, 앱 링크 및 클릭 추적 {#universal-links-app-links-and-click-tracking}

{% alert note %}
클릭 추적 링크는 일반적으로 이메일 온보딩의 일부로 설정됩니다. 고객 온보딩 중에 완료되지 않은 경우 계정 매니저에게 도움을 요청하세요.
{% endalert %}

이메일 발송 파트너는 클릭 추적 도메인을 사용하여 모든 링크를 래핑하고 Braze 이메일의 클릭 추적을 위한 URL 매개변수를 포함합니다.

예를 들어, `https://www.example.com`과 같은 링크는 `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`과 같은 형태가 됩니다.

클릭 추적이 포함된 이메일 링크가 유니버설 링크 또는 앱 링크로 작동하도록 하려면 추가 설정이 필요합니다. 클릭 추적 도메인(`links.email.example.com`)을 앱이 열 수 있는 도메인으로 추가해야 합니다. 또한 클릭 추적 도메인이 AASA(iOS) 또는 Digital Asset Links(Android) 파일을 제공해야 합니다. 이렇게 하면 클릭 추적이 포함된 이메일 링크가 원활하게 작동합니다.

모든 클릭 추적 링크를 유니버설 링크 또는 앱 링크로 만들고 싶지 않은 경우, 이메일 발송 파트너에 따라 어떤 링크를 유니버설 링크로 지정할지 선택할 수 있습니다. 자세한 내용은 다음 탭을 참조하세요.

{% tabs %}
{% tab SendGrid %}

SendGrid 클릭 추적 링크를 유니버설 링크로 처리하려면:

1. URL 경로에 `/uni/`가 포함된 링크만 유니버설 링크로 처리하도록 AASA 또는 AndroidManifest pathPrefix 값을 설정합니다.
2. 링크의 앵커 태그(`<a>`)에 `universal="true"` 속성을 추가합니다. 이렇게 하면 래핑된 링크의 URL 경로에 `/uni/`가 포함됩니다.

{% alert note %}
AMP 이메일의 경우 이 속성은 data-universal="true"여야 합니다.
{% endalert %}

예시:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. 앱이 래핑된 링크를 올바르게 처리하도록 설정되어 있는지 확인합니다. SendGrid의 [SendGrid 클릭 추적 링크 해석](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) 문서를 참조하고 운영 체제에 맞는 단계를 따르세요. 이 문서에는 [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) 및 [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android)용 예시 코드가 포함되어 있습니다.

이 구성을 사용하면 URL 경로에 `/uni/`가 포함된 링크는 유니버설 링크로 작동하고, 다른 모든 링크는 웹 링크로 작동합니다.

{% endtab %}
{% tab SparkPost %}

SparkPost 클릭 추적 링크를 유니버설 링크로 처리하려면 이메일용 드래그 앤 드롭 편집기의 속성 섹션에 다음 속성을 추가하거나, 링크 HTML을 수동으로 편집하여 링크의 앵커 태그에 다음 속성을 포함합니다: `data-msys-sublink="custom_path"`.

이 커스텀 경로를 사용하면 해당 값이 포함된 URL을 유니버설 링크로 선택적으로 처리할 수 있습니다.

예시:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

그런 다음 앱이 커스텀 경로를 올바르게 처리하도록 설정되어 있는지 확인합니다. SparkPost의 [딥링크에서 SparkPost 클릭 추적 사용](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links) 문서를 참조하세요. 이 문서에는 [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) 및 [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost)용 예시 코드가 포함되어 있습니다.

{% endtab %}
{% tab Amazon SES %}

커스텀 경로를 사용하여 이메일 클릭 추적 URL에 경로 세그먼트를 추가합니다. 이렇게 하면 모바일 운영 체제가 유니버설 링크 및 앱 링크로 인식할 수 있는 예측 가능한 URL 패턴이 생성됩니다.

사용자가 모바일 기기에서 이메일 링크를 탭할 때, 커스텀 경로를 사용하면 링크가 기본 모바일 앱, 전문 앱 또는 모바일 브라우저(예: 제품 페이지, 로열티 프로그램, 구독 취소 링크 또는 법적 페이지)에서 열리는지 제어할 수 있습니다.

Amazon SES 클릭 추적 링크를 유니버설 링크 또는 앱 링크로 처리하려면:

1. 이메일 HTML의 앵커 태그에 `ses:custom-path` 속성을 추가하거나, 이메일용 드래그 앤 드롭 편집기의 **속성** 섹션에서 속성을 추가합니다. 커스텀 경로는 래핑된 클릭 추적 URL에 삽입됩니다.

예시:

```html
<!-- Opens main shopping app -->
<a href="https://yourstore.com/product" ses:custom-path="shop">Shop Now</a>
<!-- Opens loyalty app -->
<a href="https://yourstore.com/rewards" ses:custom-path="rewards">My Rewards</a>
<!-- Opens specialized app -->
<a href="https://yourstore.com/limited" ses:custom-path="limited">Limited Edition</a>
<!-- Stays in browser -->
<a href="https://yourstore.com/unsubscribe" ses:no-track>Unsubscribe</a>
```

커스텀 경로가 다음 요구 사항을 따르는지 확인하세요:

- **형식:** 영숫자 문자, 점, 밑줄, 하이픈만 사용 가능
- **길이:** 1~32자
- **대소문자 구분:** 모바일 OS 요구 사항에 맞게 경로는 대소문자를 구분합니다

{:start="2"}
2. 래핑된 추적 URL에 커스텀 경로 세그먼트가 포함되어 있는지 확인합니다. 링크는 다음 형식을 따릅니다: `track.yourstore.com/L1/{customPath}/...`

예시:

- `track.yourstore.com/L1/shop/...`
- `track.yourstore.com/L1/rewards/...`

{:start="3"}
3. 클릭 추적 도메인에서 사이트 연결 파일을 구성하여 경로가 `/L1/{customPath}/`와 일치하도록 합니다.

**iOS(Apple App Site Association):**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/L1/shop/*", "/L1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/L1/limited/*"]
    }]
  }
}
```

**Android(Digital Asset Links):**

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourcompany.mainapp",
    "sha256_cert_fingerprints": ["..."]
  },
  "include": ["/L1/shop/*", "/L1/rewards/*"]
}]
```

앱이 이러한 래핑된 링크를 처리하도록 설정되어 있는지 확인하세요. 클릭 추적 도메인을 앱의 associated domains(iOS) 또는 인텐트 필터(Android)에 추가하고, 이 문서의 앞부분에서 설명한 대로 해당 도메인에 AASA 또는 Digital Asset Links 파일을 호스팅하세요.

{% endtab %}
{% endtabs %}

### 링크별 클릭 추적 비활성화 {#turning-off-click-tracking-on-a-link-to-link-basis}

HTML 편집기의 이메일 메시지에 HTML 코드를 추가하거나 드래그 앤 드롭 편집기의 HTML 블록에 추가하여 특정 링크의 클릭 추적을 비활성화할 수 있습니다.

#### SendGrid

이메일 서비스 공급자가 SendGrid인 경우 다음과 같이 `clicktracking=off` HTML 코드를 사용합니다:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

이메일 서비스 공급자가 SparkPost인 경우 다음과 같이 `data-msys-clicktrack="0"` HTML 코드를 사용합니다:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

이메일 서비스 공급자가 Amazon SES인 경우 다음과 같이 `ses:no-track` HTML 코드를 사용합니다:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### 드래그 앤 드롭 편집기 {#drag-and-drop-editor}

드래그 앤 드롭 이메일 편집기를 사용할 때 링크가 텍스트, 버튼 또는 이미지에 연결된 경우 HTML 코드를 커스텀 속성으로 입력합니다.

##### 텍스트 링크의 커스텀 속성 {#custom-attribute-for-a-text-link}

#### SendGrid

커스텀 속성에 다음을 선택합니다:

- **Name:** `clicktracking`
- **Value:** `off`

#### SparkPost

커스텀 속성에 다음을 선택합니다:

- **Name:** `data-msys-clicktrack`
- **Value:** `0`

![텍스트 링크의 커스텀 속성]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### 버튼 또는 이미지의 커스텀 속성 {#custom-attribute-for-a-button-or-image}

#### SendGrid

커스텀 속성에 다음을 선택합니다:

- **Name:** `clicktracking`
- **Value:** `off`
- **Type:** Link

#### SparkPost

커스텀 속성에 다음을 선택합니다:

- **Name:** `data-msys-clicktrack`
- **Value:** `0`
- **Type:** Link

![버튼의 커스텀 속성]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### 클릭 추적이 포함된 유니버설 링크 문제 해결 {#troubleshooting-universal-links-with-click-tracking}

이메일에서 유니버설 링크가 예상대로 작동하지 않는 경우(예: 수신자가 이메일 앱에서 웹 브라우저로 이동한 후 최종적으로 앱으로 리디렉션되는 경우), 다음 팁을 참조하여 유니버설 링크 설정 문제를 해결하세요.

#### Outlook에서 `[?it=` 또는 원시 URL 텍스트가 버튼 대신 표시되는 경우 {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

Outlook은 링크가 유효한 **`http://` 또는 `https://`** URL 스킴을 사용하지 않을 때 `[?it=`과 같은 콜투액션 텍스트를 표시하거나 `href`의 일부를 출력할 수 있습니다. 커스텀 스킴, 누락된 스킴 또는 잘못된 형식의 URL은 하이퍼링크로 처리되지 않으므로 클라이언트가 속성 텍스트를 대신 표시합니다. 모든 버튼, 이미지 링크 및 추적 URL이 전체 `https://`(또는 `http://`) 대상을 사용하는지 확인하세요. 이는 유니버설 링크와 표준 웹 링크 모두에 적용됩니다.

#### 링크 파일 위치 확인 {#verify-link-file-location}

AASA 파일(iOS) 또는 Digital Asset Links 파일(Android)이 올바른 위치에 있는지 확인합니다:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

이러한 파일이 항상 공개적으로 접근 가능한지 확인하는 것이 중요합니다. 접근할 수 없는 경우 이메일용 유니버설 링크 설정 단계를 놓쳤을 수 있습니다.

#### 도메인 정의 확인 {#verify-domain-definitions}

앱이 열 수 있는 도메인에 대한 올바른 정의가 있는지 확인합니다.

- **iOS:** Xcode에서 앱에 설정된 Associated Domains를 검토합니다([1c단계: Xcode 프로젝트에서 Associated Domains 활성화]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links?tab=ios#step-1c)). 클릭 추적 도메인이 해당 목록에 포함되어 있는지 확인합니다.
- **Android:** 앱 정보 페이지를 엽니다(앱 아이콘을 길게 누르고 ⓘ를 클릭). 앱 정보 메뉴에서 **기본으로 열기**를 찾아 탭합니다. 앱이 열 수 있는 모든 확인된 링크가 표시되는 화면이 나타납니다. 클릭 추적 도메인이 해당 목록에 포함되어 있는지 확인합니다.

#### 추적 도메인에서 .well-known 파일을 제공할 수 없는 경우 {#tracking-domain-cant-serve-well-known-files}

경우에 따라 ESP 제한이나 인프라 제약으로 인해 클릭 추적 도메인에서 필요한 `.well-known` 파일을 호스팅할 수 없을 수 있습니다. 추적 도메인에서 AASA 또는 Digital Asset Links 파일을 호스팅할 수 없는 경우 다음 옵션을 고려하세요:

- **딥링크 URL에서 클릭 추적을 선택적으로 비활성화:** 특정 유니버설 링크에 대해 클릭 추적을 비활성화하여 기본 도메인(AASA 또는 Digital Asset Links 파일을 호스팅할 수 있는 곳)으로 직접 이동하도록 할 수 있습니다. 이 방법은 해당 특정 링크에 대한 클릭 분석 데이터가 손실될 수 있습니다. 자세한 내용은 [링크별 클릭 추적 비활성화](#turning-off-click-tracking-on-a-link-to-link-basis)를 참조하세요.
- **추적 하위 도메인 앞에 CDN 배치:** 전체 클릭 추적 범위와 딥링킹이 모두 필요한 경우 추적 하위 도메인 앞에 CDN(예: Cloudflare 또는 CloudFront)을 배치할 수 있습니다. CDN이 `.well-known` 파일을 로컬에서 제공하고 다른 모든 트래픽을 ESP로 프록시하도록 구성합니다. 이 접근 방식은 더 복잡하지만 클릭 추적과 유니버설 링크 모두를 완전히 제어할 수 있습니다.