---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "이 참조 문서에서는 앱을 분석하고 최적화할 수 있도록 도와주는 모바일 마케팅 분석 및 기여도 플랫폼인 AppsFlyer와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [AppsFlyer](https://www.appsflyer.com/)는 마케팅 분석, 모바일 기여도, 딥링킹을 통해 앱을 분석하고 최적화할 수 있도록 도와주는 모바일 마케팅 분석 및 기여도 플랫폼입니다.

Braze와 AppsFlyer 통합을 통해 AppsFlyer의 모바일 설치 기여도 데이터를 활용하여 Campaign을 최적화하고 보다 전체적인 Campaign을 구축하는 방법을 더 잘 이해할 수 있습니다.

또한 [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences) 통합을 통해 AppsFlyer 오디언스(코호트)를 Braze로 직접 전달하여, 적절한 시점에 적절한 사용자를 타겟으로 하는 강력한 고객 참여 Campaign을 만들 수 있습니다.

## 전제 조건 {#prerequisites}

| 요건 | 설명 |
|---|---|
| AppsFlyer 계정 | 이 파트너십을 활용하려면 AppsFlyer 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. 이러한 요건에 대한 자세한 내용은 통합 프로세스의 1단계에서 확인할 수 있습니다. |
| AppsFlyer SDK | 필수 Braze SDK 외에도 [AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started)를 설치해야 합니다.
| 이메일 도메인 설정 완료 | Braze 온보딩 중 이메일 설정의 [IP 및 도메인 설정 단계]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains)를 완료해야 합니다. |
| SSL 인증서 | [SSL 인증서]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate)가 구성되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: 기기 ID 매핑 {#step-1-map-device-id}

{% tabs local %}
{% tab Android %}
Android 앱이 있는 경우, 고유한 Braze 기기 ID를 AppsFlyer에 전달해야 합니다.

다음 코드 줄이 올바른 위치에 삽입되었는지 확인하세요. Braze SDK가 실행된 후, AppsFlyer SDK의 초기화 코드 이전에 삽입해야 합니다. 자세한 내용은 AppsFlyer [Android SDK 통합 가이드](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)를 참조하세요.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
2023년 2월 이전에는 AppsFlyer 어트리뷰션 통합에서 IDFV(Identifier for Vendor)를 iOS 어트리뷰션 데이터를 매칭하는 기본 식별자로 사용했습니다. Objective-C를 사용하는 Braze 고객은 설치 시 Braze `device_id`를 가져와 AppsFlyer에 전송할 필요가 없습니다. 서비스 중단이 없기 때문입니다.
{% endalert%}

Swift SDK v5.7.0 이상을 사용하는 경우, IDFV를 상호 식별자로 계속 사용하려면 `useUUIDAsDeviceId` 필드가 `false`로 설정되어 있는지 확인하여 통합이 중단되지 않도록 해야 합니다.

`true`로 설정된 경우, Braze가 iOS 어트리뷰션을 적절히 매칭할 수 있도록 앱 설치 시 Braze `device_id`를 AppsFlyer에 전달하기 위해 Swift용 iOS 기기 ID 매핑을 구현해야 합니다.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab unity %}
Unity에서 기기 ID를 매핑하려면 다음을 사용합니다:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### 2단계: Braze 데이터 가져오기 키 받기 {#step-2-get-the-braze-data-import-key}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하고 **AppsFlyer**를 선택합니다.

여기에서 REST 엔드포인트를 확인하고 Braze 데이터 가져오기 키를 생성할 수 있습니다. 키가 생성된 후 새 키를 만들거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 다음 단계에서 AppsFlyer 대시보드에서 포스트백을 설정할 때 사용됩니다.<br><br>![AppsFlyer 기술 페이지에서 사용할 수 있는 '설치 어트리뷰션 데이터 가져오기' 상자. 이 상자에는 데이터 가져오기 키와 REST 엔드포인트가 포함되어 있습니다.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### 3단계: AppsFlyer 대시보드에서 Braze 구성 {#step-3-configure-braze-in-appsflyers-dashboard}

1. AppsFlyer에서 탐색 메뉴의 **Integrated Partners** 페이지로 이동합니다. 그런 다음 **Braze**를 검색하고 Braze 로고를 선택하여 구성 창을 엽니다.
2. **Integration** 탭에서 **Activate Partner**를 켭니다.
3. Braze 대시보드에서 확인한 데이터 가져오기 키와 REST 엔드포인트를 제공합니다.
4. **Advanced Privacy**를 끄고 구성을 저장합니다.

{% alert important %}
AppsFlyer의 Integration 탭에서 Braze REST 엔드포인트를 입력할 때 `https://` 프로토콜과 `/attribution/appsflyer` 경로 없이 도메인만 입력하세요(예: `rest.fra-02.braze.eu`). AppsFlyer가 자동으로 프로토콜을 앞에 추가하고 경로를 뒤에 추가합니다. 입력에 이 중 하나라도 포함하면 포스트백 실패가 발생합니다.
{% endalert %}

이 안내에 대한 추가 정보는 [AppsFlyer 설명서](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration)에서 확인할 수 있습니다.

### 4단계: 통합 확인 {#step-4-confirm-the-integration}

Braze의 AppsFlyer 기술 파트너 페이지에서 연결 표시기는 2단계에서 데이터 가져오기 API 키를 생성할 때까지 **Not Connected**로 표시됩니다. 키를 생성하면 표시기가 **Connected**로 변경되고 타임스탬프가 표시됩니다. 이 타임스탬프는 AppsFlyer가 마지막으로 포스트백을 보낸 시점이 아니라, Braze에서 통합이 처음 설정된 시점(데이터 가져오기 키가 생성된 시점)을 나타냅니다.

AppsFlyer에서 설치 어트리뷰션 데이터가 전달되고 있는지 확인하려면, 5단계를 사용하여 비오가닉 설치 데이터가 Braze Segment 필터에 나타나는지 검증합니다. Braze는 AppsFlyer 포스트백의 오가닉 설치를 무시하며 어트리뷰션된 설치 데이터로 저장하지 않습니다.

### 5단계: 사용자 어트리뷰션 데이터 보기 {#step-5-viewing-user-attribution-data}

#### 사용 가능한 데이터 필드 {#available-data-fields}

통합이 성공하면, Braze는 모든 비오가닉 설치 데이터를 Segment 필터에 매핑합니다.

| AppsFlyer 데이터 필드 | Braze Segment 필터 |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 가능한 데이터 필드" }

Braze 대시보드에서 설치 어트리뷰션 필터를 사용하여 어트리뷰션 데이터별로 사용자 기반을 세그먼팅할 수 있습니다.

![사용 가능한 네 가지 필터. 첫 번째는 '설치 어트리뷰션 소스가 network_val_0'입니다. 두 번째는 '설치 어트리뷰션 소스가 campaign_val_0'입니다. 세 번째는 '설치 어트리뷰션 소스가 adgroup_val_0'입니다. 네 번째는 '설치 어트리뷰션 소스가 creative_val_0'입니다. 나열된 필터 옆에서 이러한 어트리뷰션 소스가 고객 프로필에 어떻게 추가되는지 확인할 수 있습니다. 사용자 정보 페이지의 '설치 어트리뷰션' 상자에서 설치 소스는 network_val_0으로, campaign은 campaign_val_0으로 나열됩니다.]({% image_buster /assets/img/braze_attribution.png %})

또한 특정 사용자의 어트리뷰션 데이터는 Braze 대시보드에서 각 사용자의 프로필에서 확인할 수 있습니다.

{% alert note %}
Facebook 및 X(구 Twitter) Campaigns에 대한 어트리뷰션 데이터는 파트너를 통해 제공되지 않습니다. 이러한 미디어 소스는 파트너가 어트리뷰션 데이터를 제3자와 공유하는 것을 허용하지 않으므로, 파트너가 해당 데이터를 Braze에 전송할 수 없습니다.
{% endalert %}

## AppsFlyer와 Braze 통합을 통한 딥링킹 {#integrate-appsflyer-with-braze-for-deep-linking}

딥링크는 사용자를 앱이나 웹사이트 내 특정 페이지 또는 위치로 안내하는 링크로, 맞춤화된 사용자 경험을 제공하는 데 사용됩니다.

딥링크는 널리 사용되고 있지만, 사용자 데이터 수집에 활용되는 또 다른 중요한 기능인 클릭 추적 기술과 함께 이메일 딥링크를 사용할 때 문제가 발생할 수 있습니다. 이러한 문제는 이메일 서비스 공급자(ESP)가 딥링크를 클릭 기록 도메인으로 래핑하면서 원래 링크가 깨지기 때문에 발생합니다. 따라서 딥링크를 지원하려면 추가 설정이 필요합니다.

AppsFlyer는 이러한 문제를 방지하는 [서비스](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer)를 제공하며, AppsFlyer가 ESP 서버와 도메인 이름 사이에서 중개 역할을 할 수 있도록 합니다. 프록시 역할을 통해 연결 파일(AASA/에셋 링크)을 제공하여 딥링킹을 지원합니다.

## 1단계 - 클릭 추적 도메인 만들기 {#step-1-create-a-click-tracking-domain}

[Braze 이메일 설정 안내]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate)의 초기 항목에 따라 이메일 발송 도메인과 클릭 추적 도메인을 만듭니다. 지원이 필요한 경우 Braze 대시보드를 통해 티켓을 제출하여 Braze 이메일 팀과 함께 새 CTD 설정을 시작할 수 있습니다.

![상단 내비게이션 바의 'Support' 버튼 아래에 있는 'Get Help' 버튼을 보여주는 Braze UI.]({% image_buster /assets/img/attribution/appsflyer/1.png %})

이미 기존 CTD를 사용하고 있더라도 새 CTD를 만드는 것은 필수입니다. 이를 통해 현재 실행 중인 이메일 Campaign의 트래픽에 영향을 주지 않도록 보장합니다.

{% alert important%}
AppsFlyer가 SSL 인증서를 생성합니다. 이 단계에서는 이메일 링크가 보안되지 않을 수 있으며, 이는 URL 접두사가 HTTPS가 아닌 HTTP임을 의미합니다. 이 문제는 이후 단계에서 해결됩니다.
{%endalert%}

## 2단계 - AppsFlyer에서 OneLink 템플릿 만들기 {#step-2-create-a-onelink-template-in-appsflyer}
[OneLink 템플릿](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures)을 만들고 "When app is installed"에서 유니버설 링크/앱 링크를 설정합니다. 이 템플릿은 이후 이메일 캠페인용 OneLink 링크를 만들 때 사용됩니다.

{% alert note%} 유니버설 링크/앱 링크를 활성화하는 기존 OneLink 템플릿이 이미 구성되어 있는 경우 해당 템플릿을 사용할 수 있습니다.
{%endalert%}

## 3단계 - AppsFlyer에서 Braze 통합 설정하기 {#step-3-set-up-your-braze-integration-in-appsflyer}
이제 AppsFlyer에서 Braze 통합을 설정할 차례입니다. 이 단계와 다음 단계("앱 구성")는 동시에 설정할 수 있습니다.
AppsFlyer에서 Braze 통합을 설정하려면 다음을 수행합니다:

### 1. AppsFlyer에서 사이드 메뉴의 Engage > ESP integration을 선택합니다. {#1-in-appsflyer-from-the-side-menu-select-engage-esp-integration}
![AppsFlyer UI에서 내비게이션 메뉴의 "ESP Integration" 버튼을 보여주는 화면.]({% image_buster /assets/img/attribution/appsflyer/2.png %})


### 2. Braze를 선택합니다. {#2-select-braze}
![Braze를 포함한 ESP Integration 목록을 보여주는 AppsFlyer UI.]({% image_buster /assets/img/attribution/appsflyer/3.png %})


### 3. 이메일 캠페인에 사용할 OneLink 템플릿을 선택한 다음 Next를 클릭합니다. {#3-select-the-onelink-template-you-want-to-use-for-email-campaigns-then-click-next}
![사용자가 템플릿을 선택할 수 있는 드롭다운을 보여주는 AppsFlyer UI.]({% image_buster /assets/img/attribution/appsflyer/4.png %})


### 4. 클릭 추적 도메인과 "Braze endpoint" 값을 입력합니다. 이 값은 1단계에서 생성한 새 CTD와 함께 제공된 것이며, 입력 후 Validate connection을 클릭합니다. {#4-enter-your-click-tracking-domain-and-braze-endpoint-value-which-was-provided-with-the-new-ctd-created-in-step-1-then-click-validate-connection}

이렇게 하면 클릭 추적 도메인이 입력한 엔드포인트를 가리키는지 검증합니다.

![고객이 클릭 추적 도메인과 관련 세부 정보를 추가해야 하는 위치를 강조 표시한 AppsFlyer UI.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

"Braze Endpoint"란 이 가이드의 1단계에서 Braze가 제공한 세부 정보, 특히 새 CTD를 의미합니다.

그런 다음 **Validate connection**을 클릭하여 클릭 추적 도메인이 입력한 엔드포인트를 가리키는지 검증합니다.
완료되면 **Next**를 클릭합니다.

### 5. 링크 트래픽을 AppsFlyer로 라우팅합니다: {#5-route-link-traffic-to-appsflyer}

#### a. AppsFlyer에서 미리 제작된 맞춤형 안내를 복사하여 IT 또는 도메인 관리자에게 전달합니다. {#a-copy-and-send-the-customized-pre-fabricated-instructions-in-appsflyer-to-your-it-or-domain-administrator}

관리자는 DNS CNAME 레코드를 AppsFlyer가 제공한 새 도메인으로 업데이트하여 이메일 캠페인 트래픽을 ESP 서버에서 AppsFlyer 서버로 재라우팅해야 합니다.

그 결과, 링크가 클릭될 때마다 해당 클릭은 AppsFlyer로 리디렉션되고, AppsFlyer는 다시 ESP 엔드포인트로 리디렉션합니다.

![도메인에서 AppsFlyer로, 다시 ESP 엔드포인트로 클릭 데이터가 전달되는 과정을 보여주는 다이어그램]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. 안내를 복사하여 전달한 후 Done을 클릭합니다. {#b-after-copying-and-sending-the-instructions-click-done}
Braze 통합이 생성되었습니다.

{%alert important%}
Braze 통합 상태는 대기 중(pending)이며 CNAME 레코드가 매핑된 후에만 작동을 시작합니다. 매핑 후 새 통합이 작동을 시작하고 활성화되기까지 최대 24시간이 걸릴 수 있습니다.
{%endalert%}

## 4단계: 앱 구성하기 (개발자 작업) {#step-4-configure-your-app-developer-task}
AppsFlyer는 유니버설 링킹을 지원하기 위해 웹 또는 앱 팀이 따라야 하는 올바른 앱 구성에 대한 [가이드를 제공합니다](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task).

## 5단계: Braze에서 SSL 클릭 추적이 활성화되어 있는지 확인 {#step-5-confirm-ssl-click-tracking-is-enabled-with-braze}

이 단계에서는 AppsFlyer에서 CTD 세부 정보를 공유하고 검증한 후, OneLink 전송 도메인에 SSL 인증서가 있는지 확인하기 위해 테스트 전송을 수행하는 것을 권장합니다. 이는 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) 가이드와 일치합니다.

OneLink를 사용하여 딥링크를 전송하면 품질 보증 및 문제 해결을 수행할 수 있습니다. OneLink 사용에 대한 자세한 내용은 [AppsFlyer 설명서](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)를 참조하세요.

CTD 링크가 HTTP로 식별되는 경우, Braze의 이메일 운영 팀에 연락하여 SSL 클릭 추적을 활성화하세요. 이렇게 하면 모든 HTTP 링크가 자동으로 HTTPS로 변환됩니다.
1단계에서와 같이 고객 성공 매니저에게 연락하거나 Braze 대시보드에서 티켓을 생성할 때 다음 샘플 메시지 텍스트를 사용할 수 있습니다:

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS.
```

### Braze에서 AppsFlyer 클릭 추적 URL 사용 (선택 사항) {#appsflyer-click-tracking-urls-in-braze-optional}

푸시, 이메일 등 Braze Campaigns 전반에서 AppsFlyer의 [OneLink 기여도 링크](https://support.AppsFlyer.com/hc/en-us/articles/360001294118)를 사용할 수 있습니다. 이를 통해 Braze Campaigns의 설치 또는 재참여 기여도 데이터를 AppsFlyer로 다시 전송할 수 있습니다. 그 결과, 마케팅 활동을 보다 효과적으로 측정하고 데이터 중심의 의사결정을 내릴 수 있습니다.

AppsFlyer에서 OneLink 추적 URL을 생성하고 Braze Campaigns에 직접 삽입하기만 하면 됩니다. 그러면 AppsFlyer는 [확률적 기여도 방법론](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)을 사용하여 링크를 클릭한 사용자를 기여시킵니다. Braze Campaigns에서 기여도의 정확성을 높이기 위해 AppsFlyer 추적 링크에 기기 식별자를 추가하는 것을 권장합니다. 이렇게 하면 링크를 클릭한 사용자를 결정적으로 기여시킬 수 있습니다.

{% tabs local %}
{% tab Android %}
Android의 경우, Braze에서는 고객이 [Google 광고 ID 수집(GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id)에 옵트인할 수 있습니다. AppsFlyer SDK 통합도 GAID를 수집합니다. 다음 Liquid 로직을 사용하여 AppsFlyer 클릭 추적 링크에 GAID를 포함할 수 있습니다:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOS의 경우, Braze와 AppsFlyer 모두 SDK 통합을 통해 IDFV를 기본적으로 자동 수집합니다. IDFV를 기기 식별자로 사용할 수 있습니다. 다음 Liquid 로직을 사용하여 AppsFlyer 클릭 추적 링크에 IDFV를 포함할 수 있습니다:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}