---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "이 참조 문서에서는 Braze와 Linkrunner 간의 파트너십에 대해 설명합니다. Linkrunner는 모바일 기여도 및 분석 플랫폼으로, 기여도 데이터를 가져와 사용자 획득 캠페인을 더 잘 이해할 수 있도록 해줍니다."
page_type: partner
search_tag: Partner

---

# Linkrunner

> [Linkrunner](https://linkrunner.io/)는 사용자 획득 캠페인을 추적하고 분석할 수 있도록 도와주는 모바일 기여도 및 분석 플랫폼입니다.

_이 통합은 Linkrunner에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Linkrunner 통합을 사용하면 기여도 데이터를 가져와 어떤 캠페인이 사용자 획득과 참여를 이끌고 있는지 더 잘 이해할 수 있습니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다.

| 요구 사항 | 설명 |
|---|---|
| Linkrunner 계정 | 이 파트너십을 활용하려면 Linkrunner 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. |
| Linkrunner SDK | [Linkrunner SDK](https://docs.linkrunner.io/introduction)를 설치해야 합니다. |
| Braze SDK | [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/)를 통합해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: 사용자 ID 매핑 {#step-1-map-user-ids}

Braze SDK의 `changeUser` 함수를 사용하는 경우, Linkrunner SDK `signup` 함수의 `userData` 매개변수에 동일한 사용자 ID를 전달합니다.

`changeUser`를 사용하지 않는 경우, Linkrunner SDK `signup` 함수의 `userData` 매개변수에 `brazeDeviceId`를 전달합니다. `brazeDeviceId`는 Braze SDK에서 가져옵니다.

{% tabs local %}
{% tab Android (Kotlin) %}
```kotlin
val userData = UserDataRequest(
    id = "123", // Your user ID
    // ...other user fields
    brazeDeviceId = "BRAZE_DEVICE_ID", // Braze device ID from the Braze SDK (Required if you are not using the changeUser function)
)

LinkRunner.getInstance().signup(userData = userData)
```
{% endtab %}

{% tab iOS (Swift) %}
```swift
let userData = UserData(
    id: "123", // Your user ID
    // ...other user fields
    brazeDeviceId: "BRAZE_DEVICE_ID" // Braze Device ID from the Braze SDK (Required if you are not using the changeUser function)
)

try await LinkrunnerSDK.shared.signup(userData: userData)
```
{% endtab %}
{% endtabs %}

### 2단계: Braze에서 API 키 생성 {#step-2-create-api-key-in-braze}

Braze 대시보드에서 **설정** > **설정 및 테스트** > **API 키**로 이동합니다.

1. **API 키 생성**을 선택합니다.
2. **사용자 데이터**에서 다음 권한을 선택합니다:
   - `users.track`
   - `users.export.ids`
3. API 키를 저장합니다.
4. API 키와 REST 엔드포인트를 복사합니다.

![Braze의 API 키 페이지로, Linkrunner 통합에 필요한 데이터 가져오기 키와 REST 엔드포인트를 포함하여 API 키를 생성하고 관리할 수 있습니다.]({% image_buster /assets/img/attribution/linkrunner/1.png %})

### 3단계: Linkrunner 대시보드에서 Braze 구성 {#step-3-configure-braze-in-linkrunners-dashboard}

1. Linkrunner에서 왼쪽 패널의 **Integrations**로 이동합니다.
2. **Analytics**에서 Braze의 **Configure**를 선택합니다.
3. 2단계에서 복사한 API 키와 REST 엔드포인트를 입력합니다.

자세한 내용은 [Linkrunner 설명서](https://docs.linkrunner.io/analytics-integrations/braze)를 참조하세요.

### 4단계: 사용자 기여도 데이터 확인 {#step-4-view-user-attribution-data}

Linkrunner는 `lr_campaign`과 `lr_ad_network`를 커스텀 속성으로 전송합니다. 이 데이터는 Braze 대시보드의 고객 프로필에 있는 **커스텀 속성** 섹션에서 확인할 수 있습니다.

## Facebook 및 X(구 Twitter) 기여도 데이터 {#facebook-and-x-formerly-twitter-attribution-data}

Facebook 및 X(구 Twitter) 캠페인의 기여도 데이터는 파트너를 통해 제공되지 않습니다. 이러한 미디어 소스는 파트너가 기여도 데이터를 제3자와 공유하는 것을 허용하지 않으므로, 파트너가 해당 데이터를 Braze로 전송할 수 없습니다.